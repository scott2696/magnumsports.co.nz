/* Magnum Sports Worker: Stripe checkout for the cart, and email delivery of
   order requests, enquiries and contact messages.

   POST /checkout  {"items": [{"sku": "petram-a2-blk", "qty": 2}, ...]}
     -> {"url": "https://checkout.stripe.com/..."}

   The browser sends only SKUs and quantities. Names, prices and photos come
   from the site's own published catalogue (CATALOGUE_URL), so a price edited
   in someone's browser never reaches Stripe. Prices include GST and, for single items, delivery; packs are refused (quoted by email).

   POST /message   {"kind": "order"|"enquiry"|"contact", "name", "email", ...}
     -> emails the shop through Cloudflare Email Routing (binding NOTIFY), with
        Reply-To set to the customer so a reply goes straight to them.

   Secrets (set with `wrangler secret put`, never in this repository):
     STRIPE_SECRET_KEY  a *restricted* key that can only write Checkout Sessions
     NOTIFY_TO          where messages are delivered; must be a verified
                        destination address in Email Routing */

import { EmailMessage } from "cloudflare:email";

const MAX_LINES = 50;
const MAX_QTY = 99;

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";
    const allowed = (env.ALLOWED_ORIGINS || "").split(",").map((s) => s.trim()).filter(Boolean);
    const cors = {
      "Access-Control-Allow-Origin": allowed.includes(origin) ? origin : allowed[0] || "",
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
      "Vary": "Origin",
    };
    const reply = (body, status = 200) =>
      new Response(JSON.stringify(body), { status, headers: { ...cors, "Content-Type": "application/json" } });

    if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: cors });
    const url = new URL(request.url);
    // GET /selftest: is the Stripe key present and accepted? Says only ok /
    // invalid / missing permission / not set - never anything about the key.
    // GET /methods: which payment methods Stripe offers this account for an
    // NZD checkout. Creates an unpaid session that simply expires.
    if (request.method === "GET" && url.pathname === "/methods") {
      if (!env.STRIPE_SECRET_KEY) return reply({ stripe: "not set" });
      const f = new URLSearchParams();
      f.set("mode", "payment");
      f.set("success_url", env.SITE_URL + "/");
      f.set("line_items[0][quantity]", "1");
      f.set("line_items[0][price_data][currency]", (url.searchParams.get("currency") || "nzd").toLowerCase().slice(0, 3));
      f.set("line_items[0][price_data][unit_amount]", "5000");
      f.set("line_items[0][price_data][product_data][name]", "Payment methods check (not a real order)");
      const r = await fetch("https://api.stripe.com/v1/checkout/sessions", {
        method: "POST",
        headers: { Authorization: `Bearer ${env.STRIPE_SECRET_KEY}`, "Content-Type": "application/x-www-form-urlencoded" },
        body: f,
      });
      const d = await r.json();
      if (d.id) {
        await fetch(`https://api.stripe.com/v1/checkout/sessions/${d.id}/expire`, {
          method: "POST", headers: { Authorization: `Bearer ${env.STRIPE_SECRET_KEY}` },
        });
      }
      return reply(r.ok ? { methods: d.payment_method_types, currency: d.currency } : { error: d.error && d.error.message });
    }
    if (request.method === "GET" && url.pathname === "/selftest") {
      if (!env.STRIPE_SECRET_KEY) return reply({ stripe: "not set" });
      const r = await fetch("https://api.stripe.com/v1/checkout/sessions?limit=1", {
        headers: { Authorization: `Bearer ${env.STRIPE_SECRET_KEY}` },
      });
      const d = await r.json().catch(() => ({}));
      const msg = (d.error && d.error.message) || "";
      const mode = env.STRIPE_SECRET_KEY.startsWith("rk_live_") || env.STRIPE_SECRET_KEY.startsWith("sk_live_") ? "live" : "test";
      const kind = env.STRIPE_SECRET_KEY.startsWith("rk_") ? "restricted key" : "full secret key";
      if (r.ok) return reply({ stripe: "ok", mode, kind });
      if (/invalid api key/i.test(msg)) return reply({ stripe: "invalid key" });
      if (/permission/i.test(msg)) return reply({ stripe: "key accepted; it cannot list sessions (fine for checkout)", mode });
      return reply({ stripe: "error", status: r.status });
    }
    if (request.method === "POST" && url.pathname === "/message") {
      if (!allowed.includes(origin)) return reply({ error: "Origin not allowed" }, 403);
      return sendMessage(request, env, reply);
    }
    if (request.method !== "POST" || url.pathname !== "/checkout") return reply({ error: "Not found" }, 404);
    if (!allowed.includes(origin)) return reply({ error: "Origin not allowed" }, 403);
    if (!env.STRIPE_SECRET_KEY) return reply({ error: "Checkout is not configured" }, 503);

    let body;
    try {
      body = await request.json();
    } catch (e) {
      return reply({ error: "Bad request" }, 400);
    }
    const items = Array.isArray(body && body.items) ? body.items.slice(0, MAX_LINES) : [];
    if (!items.length) return reply({ error: "Your cart is empty" }, 400);

    // The catalogue the site publishes: [{s: sku, n: name, p: "109.99", i: "/images/..", u: "/shop/.."}]
    let catalogue;
    try {
      const r = await fetch(env.CATALOGUE_URL, { cf: { cacheTtl: 300 } });
      catalogue = new Map((await r.json()).map((p) => [p.s, p]));
    } catch (e) {
      return reply({ error: "Could not load the catalogue. Please try again." }, 502);
    }

    const site = env.SITE_URL.replace(/\/$/, "");
    const form = new URLSearchParams();
    form.set("mode", "payment");
    form.set("currency", "nzd");
    form.set("success_url", `${site}/shop/thanks/?session_id={CHECKOUT_SESSION_ID}`);
    form.set("cancel_url", `${site}/shop/#cart`);
    form.set("shipping_address_collection[allowed_countries][0]", "NZ");
    form.set("phone_number_collection[enabled]", "true");
    form.set("billing_address_collection", "auto");
    form.set("invoice_creation[enabled]", "true");          // a receipt/invoice for every order
    form.set("submit_type", "pay");
    // Sizes, colours, hand measurements: shown on Stripe's page, returned on the payment.
    form.set("custom_fields[0][key]", "notes");
    form.set("custom_fields[0][label][type]", "custom");
    form.set("custom_fields[0][label][custom]", "Size, colour or notes");
    form.set("custom_fields[0][type]", "text");
    form.set("custom_fields[0][optional]", "true");
    const skus = [];
    const cn = [];
    let n = 0;
    let kg = 0;          // weight of lines whose delivery is charged by weight (search.json "x", "w")
    for (const it of items) {
      const p = catalogue.get(String(it.sku || ""));
      const qty = Math.max(1, Math.min(MAX_QTY, parseInt(it.qty, 10) || 0));
      if (!p) return reply({ error: `A product in your cart is no longer available (${it.sku}). Please remove it and try again.` }, 409);
      // Bulk packs exclude delivery: they are quoted by email, never paid for here.
      if (p.k) return reply({ error: "Your cart has a bulk pack, whose delivery is quoted. Please use Request my total." }, 409);
      const cents = Math.round(parseFloat(p.p) * 100);
      if (!(cents > 0)) return reply({ error: "Bad price" }, 500);
      const k = `line_items[${n}]`;
      form.set(`${k}[quantity]`, String(qty));
      form.set(`${k}[price_data][currency]`, "nzd");
      form.set(`${k}[price_data][unit_amount]`, String(cents));
      form.set(`${k}[price_data][tax_behavior]`, "inclusive");
      const opt = String(it.opt || "").slice(0, 40);
      const pname = p.n + (p.k ? ` (pack of ${p.k})` : "") + (opt ? ` (size ${opt})` : "");
      // Supplier size behind the NZ size: for us only (Stripe metadata), never shown to the customer.
      if (opt && p.z && p.z[opt]) cn.push(`${p.s} ${opt}=China ${p.z[opt]}`);
      form.set(`${k}[price_data][product_data][name]`, pname.slice(0, 250));
      form.set(`${k}[price_data][product_data][metadata][sku]`, p.s);
      if (p.i) form.set(`${k}[price_data][product_data][images][0]`, site + p.i);
      skus.push(`${p.s}x${qty}`);
      if (p.x) kg += (parseFloat(p.w) || 0) * qty;
      n++;
    }
    form.set("metadata[skus]", skus.join(",").slice(0, 500));
    if (cn.length) form.set("metadata[china_sizes]", cn.join("; ").slice(0, 500));
    if (kg > 0) {
      // Delivery by destination and weight: the site's published rate table (delivery.json).
      let rates = [];
      try {
        const r = await fetch(env.CATALOGUE_URL.replace("search.json", "delivery.json"), { cf: { cacheTtl: 300 } });
        rates = await r.json();
      } catch (e) { return reply({ error: "Could not load delivery rates. Please try again." }, 502); }
      const dest = rates.find((c) => c.id === String(body.city || ""));
      if (!dest) return reply({ error: "Please choose your city in the cart so we can add delivery." }, 400);
      // Outside New Zealand only weight-priced items ship at these rates.
      if (dest.country !== "NZ" && items.some((it) => { const q = catalogue.get(String(it.sku || "")); return !q || !q.x; }))
        return reply({ error: "Some items in your cart only ship within New Zealand. Please use Request my total." }, 409);
      const whole = Math.max(1, Math.ceil(Math.round(kg * 1000) / 1000));
      const fee = Math.round(dest.first * 100) + Math.round(dest.extra * 100) * (whole - 1);
      form.set("shipping_address_collection[allowed_countries][0]", dest.country);
      form.set("metadata[delivery_city]", `${dest.city} ${dest.postcode}`);
      const o = "shipping_options[0][shipping_rate_data]";
      form.set(`${o}[type]`, "fixed_amount");
      form.set(`${o}[display_name]`, `Delivery to ${dest.city} (${whole} kg)`);
      form.set(`${o}[fixed_amount][amount]`, String(fee));
      form.set(`${o}[fixed_amount][currency]`, "nzd");
      form.set(`${o}[tax_behavior]`, "inclusive");
      form.set(`${o}[delivery_estimate][minimum][unit]`, "business_day");
      form.set(`${o}[delivery_estimate][minimum][value]`, "7");
      form.set(`${o}[delivery_estimate][maximum][unit]`, "business_day");
      form.set(`${o}[delivery_estimate][maximum][value]`, "10");
      form.set("metadata[delivery_kg]", String(Math.round(kg * 100) / 100));
    }
    form.set("payment_intent_data[description]", "Magnum Sports online order");

    const s = await fetch("https://api.stripe.com/v1/checkout/sessions", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${env.STRIPE_SECRET_KEY}`,
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: form,
    });
    const session = await s.json();
    if (!s.ok || !session.url) {
      console.log("stripe error", JSON.stringify(session.error || session));
      return reply({ error: "Payment could not be started. Please try again, or send an order request instead." }, 502);
    }
    return reply({ url: session.url });
  },
};


// ---------------------------------------------------------------- messages
const one = (v, n = 200) => String(v == null ? "" : v).replace(/[\r\n]+/g, " ").trim().slice(0, n);
const many = (v, n = 4000) => String(v == null ? "" : v).replace(/\r\n?/g, "\n").trim().slice(0, n);
const EMAIL_RE = /^[^\s@<>",;]+@[^\s@<>",;]+\.[^\s@<>",;]+$/;

async function sendMessage(request, env, reply) {
  if (!env.NOTIFY || !env.NOTIFY_TO) return reply({ error: "Messaging is not configured" }, 503);
  let b;
  try {
    b = await request.json();
  } catch (e) {
    return reply({ error: "Bad request" }, 400);
  }
  if (b.website) return reply({ ok: true });            // honeypot: bots fill hidden fields
  const kind = ["order", "enquiry", "contact"].includes(b.kind) ? b.kind : "contact";
  const name = one(b.name, 100), email = one(b.email, 200);
  if (!name || !EMAIL_RE.test(email)) return reply({ error: "Please give your name and a valid email address." }, 400);

  const lines = [];
  let subtotal = "";
  if (kind !== "contact") {
    let cat = new Map();
    try {
      const r = await fetch(env.CATALOGUE_URL, { cf: { cacheTtl: 300 } });
      cat = new Map((await r.json()).map((p) => [p.s, p]));
    } catch (e) { /* names fall back to SKUs */ }
    const items = Array.isArray(b.items) ? b.items.slice(0, 50) : [];
    if (!items.length) return reply({ error: "Your list is empty." }, 400);
    const site = env.SITE_URL.replace(/\/$/, "");
    let sub = 0, kgx = 0;
    for (const it of items) {
      const sku = one(it.sku, 80), qty = Math.max(1, Math.min(99, parseInt(it.qty, 10) || 1));
      const p = cat.get(sku);
      const price = p && p.p ? `  @ NZ$${p.p}` : "";
      if (p && p.p) sub += Math.round(parseFloat(p.p) * 100) * qty;
      if (p && p.x) kgx += (parseFloat(p.w) || 0) * qty;
      lines.push(`${qty} x ${p ? p.n : sku}${p && p.k ? ` (pack of ${p.k})` : ""}${it.opt ? " (size " + one(it.opt, 60) + (p && p.z && p.z[it.opt] ? ", order China " + p.z[it.opt] : "") + ")" : ""}${price}   [${sku}]`,
                 p ? `    ${site}${p.u}` : "");
    }
    if (sub) subtotal = `Subtotal: NZ$${(sub / 100).toFixed(2)} incl. GST, EXCLUDING delivery.\n` +
      "Reply with the total including delivery and a Stripe payment link." +
      (kgx ? `\nItems charged by weight: ${Math.round(kgx * 100) / 100} kg (NZ$30.11 first kg + NZ$22.19 each extra kg).` : "");
  }
  const title = { order: "Quote request", enquiry: "Enquiry", contact: "Contact" }[kind];
  const body = [
    `${title} from ${name}`, "",
    ...(lines.length ? ["ITEMS", ...lines.filter(Boolean), "", ...(subtotal ? [subtotal, ""] : [])] : []),
    `Name:     ${name}`, `Email:    ${email}`,
    b.phone ? `Phone:    ${one(b.phone, 40)}` : "",
    b.address ? `Deliver:  ${one(b.address, 400)}` : "",
    b.city ? `City:     ${b.city === "other" ? "not on the rate card (quote delivery)" : one(b.city, 60)}` : "",
    b.payment ? `Payment:  ${one(b.payment, 80)}` : "",
    b.topic ? `Topic:    ${one(b.topic, 80)}` : "",
    b.notes ? `\nNotes:\n${many(b.notes)}` : "",
    b.message ? `\nMessage:\n${many(b.message)}` : "",
    "", "Reply to this email to answer the customer directly.",
  ].filter((l) => l !== "").join("\n");

  const from = env.NOTIFY_FROM || "orders@magnumsports.co.nz";
  const subject = `${title}: ${name}${lines.length ? ` (${lines.filter((l) => !l.startsWith("    ")).length} item${lines.length > 2 ? "s" : ""})` : ""}`;
  const raw = [
    `From: Magnum Sports website <${from}>`,
    `To: <${env.NOTIFY_TO}>`,
    `Reply-To: ${name.replace(/["<>]/g, "")} <${email}>`,
    `Subject: ${subject.replace(/[^\x20-\x7e]/g, "")}`,
    `Date: ${new Date().toUTCString()}`,
    `Message-ID: <${crypto.randomUUID()}@magnumsports.co.nz>`,
    "MIME-Version: 1.0",
    "Content-Type: text/plain; charset=utf-8",
    "Content-Transfer-Encoding: 8bit",
    "", body,
  ].join("\r\n");
  try {
    await env.NOTIFY.send(new EmailMessage(from, env.NOTIFY_TO, raw));
  } catch (e) {
    console.log("email error", String(e && e.message || e));
    return reply({ error: "Your message could not be sent. Please email editor@magnumsports.co.nz instead." }, 502);
  }
  return reply({ ok: true });
}
