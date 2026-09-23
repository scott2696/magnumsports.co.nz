/* Magnum Sports checkout: turns a cart into a Stripe Checkout page.

   POST /checkout  {"items": [{"sku": "petram-a2-blk", "qty": 2}, ...]}
     -> {"url": "https://checkout.stripe.com/..."}

   The browser sends only SKUs and quantities. Names, prices and photos come
   from the site's own published catalogue (CATALOGUE_URL), so a price edited
   in someone's browser never reaches Stripe. Prices include GST and delivery.

   Secrets: STRIPE_SECRET_KEY is set with `wrangler secret put` and lives only
   in Cloudflare. It is never in this repository. Use a *restricted* key that
   can only write Checkout Sessions. */

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
