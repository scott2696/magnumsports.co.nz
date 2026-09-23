/* Magnum Sports Worker: Stripe checkout for the cart, and email delivery of
   order requests, enquiries and contact messages.

   POST /checkout  {"items": [{"sku": "petram-a2-blk", "qty": 2}, ...]}
     -> {"url": "https://checkout.stripe.com/..."}

   The browser sends only SKUs and quantities. Names, prices and photos come
   from the site's own published catalogue (CATALOGUE_URL), so a price edited
   in someone's browser never reaches Stripe. Prices include GST and delivery.

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
    const skus = [];
    let n = 0;
    for (const it of items) {
      const p = catalogue.get(String(it.sku || ""));
      const qty = Math.max(1, Math.min(MAX_QTY, parseInt(it.qty, 10) || 0));
      if (!p) return reply({ error: `A product in your cart is no longer available (${it.sku}). Please remove it and try again.` }, 409);
      const cents = Math.round(parseFloat(p.p) * 100);
      if (!(cents > 0)) return reply({ error: "Bad price" }, 500);
      const k = `line_items[${n}]`;
      form.set(`${k}[quantity]`, String(qty));
      form.set(`${k}[price_data][currency]`, "nzd");
      form.set(`${k}[price_data][unit_amount]`, String(cents));
      form.set(`${k}[price_data][tax_behavior]`, "inclusive");
      form.set(`${k}[price_data][product_data][name]`, (it.opt ? `${p.n} (${it.opt})` : p.n).slice(0, 250));
      form.set(`${k}[price_data][product_data][metadata][sku]`, p.s);
      if (p.i) form.set(`${k}[price_data][product_data][images][0]`, site + p.i);
      skus.push(`${p.s}x${qty}`);
      n++;
    }
    form.set("metadata[skus]", skus.join(",").slice(0, 500));
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
  if (kind !== "contact") {
    let cat = new Map();
    try {
      const r = await fetch(env.CATALOGUE_URL, { cf: { cacheTtl: 300 } });
      cat = new Map((await r.json()).map((p) => [p.s, p]));
    } catch (e) { /* names fall back to SKUs */ }
    const items = Array.isArray(b.items) ? b.items.slice(0, 50) : [];
    if (!items.length) return reply({ error: "Your list is empty." }, 400);
    const site = env.SITE_URL.replace(/\/$/, "");
    for (const it of items) {
      const sku = one(it.sku, 80), qty = Math.max(1, Math.min(99, parseInt(it.qty, 10) || 1));
      const p = cat.get(sku);
      const price = p && p.p ? `  @ NZ$${p.p}` : "";
      lines.push(`${qty} x ${p ? p.n : sku}${it.opt ? " (" + one(it.opt, 60) + ")" : ""}${price}   [${sku}]`,
                 p ? `    ${site}${p.u}` : "");
    }
  }
  const title = { order: "Order request", enquiry: "Enquiry", contact: "Contact" }[kind];
  const body = [
    `${title} from ${name}`, "",
    ...(lines.length ? ["ITEMS", ...lines.filter(Boolean), ""] : []),
    `Name:     ${name}`, `Email:    ${email}`,
    b.phone ? `Phone:    ${one(b.phone, 40)}` : "",
    b.address ? `Deliver:  ${one(b.address, 400)}` : "",
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
    return reply({ error: "Your message could not be sent. Please call us instead." }, 502);
  }
  return reply({ ok: true });
}
