# -*- coding: utf-8 -*-
"""The online shop:
  /shop/                   shop front: departments, cart and order form
  /shop/<dept>/            every product in one department
  /shop/<dept>/<sku>/      one product: photo, full description, specifications
Also writes assets/js/cart.js from _build/cart.js with the catalogue baked in,
so the cart can never show a price the page does not."""
from lib import *
from faq_data import DEPT as DEPT_FAQ

TITLE, DESC = META["/shop/"]
PATH = "/shop/"

FAQ = [
 ("How does ordering online work?",
  ("<p>Add what you want to the cart, fill in your details and press <strong>Send order "
   "request</strong>. Your email app opens with the order written out; send it and we reply, "
   "usually the same working day, to confirm stock and how to pay. Nothing is charged until we have "
   "confirmed it with you.</p>") if SHOW_PRICES else
  ("<p>We are confirming prices with our suppliers, so for now every product is <strong>price on "
   "request</strong>. Add what you want to your enquiry list, fill in your details and press "
   "<strong>Send enquiry</strong>. We reply, usually the same working day, with prices, stock and how "
   "to pay. Nothing is charged until you have agreed the price.</p>")),
 ("How long does delivery take?",
  "<p>Delivery takes <strong>7 to 10 days</strong> from when we confirm your order, and it is free: "
  "every price already includes delivery anywhere in New Zealand.</p>"),
 ("How do I pay?",
  f"<p>{PAY_HOW} Nothing is charged until we have confirmed your order. We never ask for card "
  "details by email, and our bank account number only ever comes in our reply to your order.</p>"),
 ("Is my cart saved?",
  "<p>Your cart is kept in this browser on this device until you send the order or clear it. "
  "We never see it until you send us the order email. See our "
  "<a href='/cookie-policy/'>cookie policy</a>.</p>"),
]


def write_cart_js():
    keys = ("name", "price", "options") if SHOW_PRICES else ("name", "options")
    cat = {p["sku"]: {k: p[k] for k in keys if k in p} for p in PRODUCTS}
    src = open(os.path.join(ROOT, "_build", "cart.js"), encoding="utf-8").read()
    src = (src.replace("/*@@CATALOGUE@@*/{}", json.dumps(cat, ensure_ascii=False, separators=(",", ":")))
              .replace("/*@@ORDER_EMAIL@@*/", ORDER_EMAIL)
              .replace("/*@@SHOW_PRICES@@*/true", "true" if SHOW_PRICES else "false"))
    d = os.path.join(ROOT, "assets", "js")
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "cart.js"), "w", encoding="utf-8").write(src)



def offer(p):
    return {"@type": "Offer", "price": p["price"], "priceCurrency": "NZD",
            "url": SITE + product_url(p), "seller": {"@id": f"{SITE}/#store"}}


def product_entity(p):
    img = product_image(p["sku"])
    d = {"@type": "Product", "@id": f"{SITE}{product_url(p)}#product", "name": p["name"],
         "sku": p["sku"], "description": p["blurb"], "category": p["dept"],
         "url": SITE + product_url(p)}
    if SHOW_PRICES:
        d["offers"] = offer(p)
    if img:
        d["image"] = SITE + img
    if p.get("model"):
        d["mpn"] = p["model"]
    return d


def itemlist(items, path, name):
    return {"@type": "ItemList", "@id": f"{SITE}{path}#catalogue", "name": name,
            "numberOfItems": len(items),
            "itemListElement": [{"@type": "ListItem", "position": i, "url": SITE + product_url(p)}
                                for i, p in enumerate(items, 1)]}


def cart_section():
    o = []
    o.append(f'''<section id="cart" class="sec sec--haze" style="scroll-margin-top:70px"><div class="wrap">
<div class="sec-head"><span class="kicker">{"Your cart" if SHOW_PRICES else "Your enquiry"}</span><h2>{"Your cart" if CHECKOUT_URL else ("Cart and order request" if SHOW_PRICES else "Enquiry list")}</h2>
<p>{"Pay now by card, or send an order request to pay by bank transfer or by phone. Delivery is included in every price." if CHECKOUT_URL else ("No payment is taken here. Send the request and we reply to confirm stock and how to pay. Delivery is included in every price." if SHOW_PRICES else "We are confirming prices with our suppliers. Add the products you want and send us your enquiry: we reply with prices, stock and how to pay. Delivery anywhere in New Zealand is free.")}</p></div>
<div class="cart-grid">
<div class="cart-box"><div id="cart-lines"><p class="cart-empty">Loading your cart&hellip;</p></div>
{f'<div class="cart-paynow" id="pay-now-wrap" hidden><button class="btn btn--wide" type="button" id="pay-now" data-checkout="{esc(CHECKOUT_URL)}">{icon("lock")} Pay now by card</button><p class="cart-fine">Secure checkout by Stripe. You enter your delivery address there.</p><p class="cart-error" id="pay-now-error" role="alert" hidden></p></div>' if CHECKOUT_URL else ""}
<div class="cart-pay">{pay_badges()}<p>{PAY_HOW}</p></div>
<noscript><p class="cart-empty">The cart needs JavaScript. Call <a href="tel:{STORE["phone_tel"]}">{esc(STORE["phone_display"])}</a> to order instead.</p></noscript></div>
<div>
<form id="order-form" class="form" hidden>
<div class="field"><label for="o-name">Your name</label><input id="o-name" name="name" type="text" autocomplete="name" required></div>
<div class="field"><label for="o-email">Email address</label><input id="o-email" name="email" type="email" autocomplete="email" required></div>
<div class="field"><label for="o-phone">Phone</label><input id="o-phone" name="phone" type="tel" autocomplete="tel" required></div>
<div class="field"><label for="o-address">Delivery address</label><textarea id="o-address" name="address" autocomplete="street-address" required style="min-height:90px"></textarea><span class="hint">Free delivery anywhere in New Zealand, 7 to 10 days once your order is confirmed.</span></div>
<fieldset class="field pay-choice"><legend>How would you like to pay?</legend>
{"" if CHECKOUT_URL else '<label><input type="radio" name="payment" value="Card online (Stripe payment link)" checked> Card online &mdash; we email you a secure Stripe link</label>'}
<label><input type="radio" name="payment" value="Bank transfer"{" checked" if CHECKOUT_URL else ""}> Bank transfer</label>
<label><input type="radio" name="payment" value="Visa or Mastercard (by phone)"> Visa or Mastercard, by phone</label></fieldset>
<div class="field"><label for="o-notes">Notes</label><textarea id="o-notes" name="notes" style="min-height:90px"></textarea><span class="hint">Sizes, colours, or anything else we should know.</span></div>
<button class="btn" type="submit">{"Send order request" if SHOW_PRICES else "Send enquiry"}</button>
<p style="font-size:.79rem;color:var(--mute);margin:0">This opens your email app with the order filled in. We use your details only to handle this order. See our <a href="/privacy/">privacy policy</a>.</p>
</form>
<div id="order-sent" class="note" hidden style="margin-top:18px"><b>Almost done: press send in your email app</b>
<p>If no email opened, copy the order below and email it to <a href="mailto:{ORDER_EMAIL}">{ORDER_EMAIL}</a>, or call <a href="tel:{STORE["phone_tel"]}">{esc(STORE["phone_display"])}</a>.</p>
<div class="field"><label for="order-copy">Your order</label><textarea id="order-copy" readonly style="min-height:160px;font-family:var(--mono);font-size:.8rem"></textarea></div>
<p style="display:flex;gap:10px;flex-wrap:wrap;margin-top:12px"><button class="btn btn--sm btn--ghost" type="button" id="order-copy-btn">Copy order</button>
<button class="btn btn--sm btn--ghost" type="button" id="order-clear">Sent it &mdash; clear my cart</button></p></div>
</div>
</div>
</div></section>
''')

    return "".join(o)





# ------------------------------------------------------------- shop front
def front(depts):
    schema = page_schema("CollectionPage", TITLE, DESC, PATH,
                         extra=[store_schema(),
                                crumb_schema([("Home", "/"), ("Shop Online", PATH)]),
                                faq_schema(FAQ, f"{SITE}{PATH}#faq")])
    o = [head(TITLE, DESC, PATH, schema), crumbs([("Home", "/"), ("Shop Online", None)])]
    o.append(f'''<section class="hero"><div class="wrap">
<span class="eyebrow">{icon("cart")} Order online &middot; Delivered across New Zealand in 7 to 10 days</span>
<h1>Shop Online at {esc(STORE["name"])}</h1>
<p class="lede">Add gear to your cart and send us an order request. We confirm stock with you before anything is charged, and every price includes delivery anywhere in New Zealand. Can&rsquo;t find something? <a href="/search/">Search the shop</a> or <a href="tel:{STORE["phone_tel"]}">ring {esc(STORE["phone_display"])}</a>.</p>
</div></section>
''')
    o.append(f'''<section class="sec"><div class="wrap">
<div class="sec-head"><span class="kicker">The shop</span><h2>Shop by department</h2>
<p>Pick a department to see everything in it. Click any product for its full description and specifications.</p></div>
{shop_tiles(depts)}
</div></section>
''')
    o.append(cart_section())
    o.append(faq_block(FAQ, "Ordering online: common questions"))
    o.append(footer())
    return write(PATH, "".join(o))


# ------------------------------------------------------------ departments
def dept_page(name, slug, ic, blurb, items):
    path = f"/shop/{slug}/"
    title = f"{name} | Shop Online | {STORE['name']}"
    desc = clamp(f"Shop {name.lower()} online from {STORE['name']}. "
                 f"{len(items)} products, delivered across New Zealand in 7 to 10 days.", 158)
    faq = DEPT_FAQ.get(name, [])
    schema = page_schema("CollectionPage", title, desc, path,
                         extra=[crumb_schema([("Home", "/"), ("Shop Online", PATH), (name, path)]),
                                itemlist(items, path, f"{name} at {STORE['name']}")]
                         + ([faq_schema(faq, f"{SITE}{path}#faq")] if faq else []))
    o = [head(title, desc, path, schema),
         crumbs([("Home", "/"), ("Shop Online", PATH), (name, None)])]
    o.append(f'''<section class="hero"><div class="wrap">
<span class="eyebrow">{icon(ic)} Shop Online &middot; {len(items)} product{"s" if len(items) != 1 else ""}</span>
<h1>{esc(name)}</h1>
<p class="lede">{blurb}</p>
</div></section>
''')
    others = "".join(f'<a href="/shop/{s}/">{esc(n)}</a>' for n, s, *_ in by_dept() if s != slug)
    o.append(f'''<section class="sec"><div class="wrap">
<div class="picks">{"".join(product_card(p) for p in items)}</div>
<nav class="shop-other" aria-label="Other departments"><b>Other departments</b>{others}<a href="{PATH}#cart">Your cart &rarr;</a></nav>
</div></section>
''')
    if faq:
        o.append(faq_block(faq, f"{name}: common questions"))
    o.append(footer())
    return write(path, "".join(o))


# --------------------------------------------------------------- products
def description(p):
    """The full description: our summary, then what the listing tells us."""
    parts = [f"<p>{esc(p['blurb'])}</p>"]
    facts = []
    if p.get("model"):
        facts.append(f"Model <strong>{esc(p['model'])}</strong>")
    if p.get("origin"):
        facts.append(esc(p["origin"]))
    if facts:
        parts.append(f"<p>{' &middot; '.join(facts)}.</p>")
    parts.append("<p>Order online and we deliver in <strong>7 to 10 days</strong> once your order is "
                 "confirmed. Delivery anywhere in New Zealand is included in the price.</p>")
    return "".join(parts)


def product_page(p, siblings):
    name, slug = p["dept"], DEPT_SLUG[p["dept"]]
    path = product_url(p)
    title = f"{p['name']} | {STORE['name']}"
    desc = clamp(f"{p['blurb']} " + (f"NZ${p['price']} " if SHOW_PRICES else "") + f"from {STORE['name']}. "
                 "Delivered in 7 to 10 days.", 158)
    img = product_image(p["sku"])
    schema = page_schema("ItemPage", title, desc, path,
                         extra=[crumb_schema([("Home", "/"), ("Shop Online", PATH), (name, f"/shop/{slug}/"),
                                              (p["name"], path)]),
                                product_entity(p)])
    o = [head(title, desc, path, schema, image=img or "/images/og-magnum.jpg"),
         crumbs([("Home", "/"), ("Shop Online", PATH), (name, f"/shop/{slug}/"), (p["name"], None)])]
    media = (f'<img src="{img}" alt="{esc(p["name"])}" width="600" height="600" decoding="async">'
             if img else f'<span class="dept-ic">{icon("tag")}</span>')
    specs = p.get("specs") or []
    spec_html = ""
    if specs:
        spec_html = ('<h2>Specifications</h2><div class="tw"><table class="specs"><tbody>'
                     + "".join(f'<tr><th scope="row">{esc(k)}</th><td>{esc(v)}</td></tr>' for k, v in specs)
                     + "</tbody></table></div>")
    o.append(f'''<section class="sec pdp-sec"><div class="wrap">
<div class="pdp" data-sku="{esc(p["sku"])}">
<div class="pdp-img{"" if img else " pdp-img--empty"}">{media}</div>
<div class="pdp-buy">
<a class="pick-cat" href="/shop/{slug}/">{esc(name)}</a>
<h1>{esc(p["name"])}</h1>
{price_html(p, " pdp-price")}
<p class="pdp-lede">{esc(p["blurb"])}</p>
<div class="pdp-cta">{product_cta(p, size="")}</div>
<p class="pdp-fine">{"Free delivery anywhere in New Zealand, 7 to 10 days. Price in NZD, including GST and delivery." if SHOW_PRICES else "We are confirming prices: add it to your enquiry and we reply with the price. Free delivery anywhere in New Zealand, 7 to 10 days."}</p>
{pay_badges()}
<p class="pdp-fine"><a href="{PATH}#cart">{"View your cart" if SHOW_PRICES else "View your enquiry list"} &rarr;</a></p>
</div>
</div>
<div class="pdp-desc prose prose--wide">
<h2>Description</h2>
{description(p)}
{spec_html}
</div>
</div></section>
''')
    more = [s for s in siblings if s["sku"] != p["sku"]][:4]
    if more:
        o.append(f'''<section class="sec sec--haze"><div class="wrap">
<div class="sec-head"><span class="kicker">{esc(name)}</span><h2>More in {esc(name)}</h2></div>
<div class="picks">{"".join(product_card(s) for s in more)}</div>
<p style="margin-top:18px"><a href="/shop/{slug}/">See all {esc(name.lower())} &rarr;</a></p>
</div></section>
''')
    o.append(footer())
    return write(path, "".join(o))


def write_search():
    """assets/js/search.js (copied) and search.json, the index it searches."""
    d = os.path.join(ROOT, "assets", "js")
    os.makedirs(d, exist_ok=True)
    idx = [{"s": p["sku"], "n": p["name"], "d": p["dept"], **({"p": p["price"]} if SHOW_PRICES else {}),
            "u": product_url(p),
            "i": product_image(p["sku"]) or "", "b": p["blurb"], "m": p.get("model", ""),
            **({"o": 1} if p.get("options") else {})}
           for p in PRODUCTS]
    json.dump(idx, open(os.path.join(d, "search.json"), "w", encoding="utf-8"),
              ensure_ascii=False, separators=(",", ":"))
    src = open(os.path.join(ROOT, "_build", "search.js"), encoding="utf-8").read()
    open(os.path.join(d, "search.js"), "w", encoding="utf-8").write(src)


def search_page():
    """/search/: results are drawn by search.js from ?q=. Not indexed and kept
    out of the sitemap, since every result is its own product page already."""
    path = "/search/"
    title, desc = "Search | Magnum Sports", f"Search the {STORE['name']} online shop."
    o = [head(title, desc, path, page_schema("SearchResultsPage", title, desc, path), robots="noindex,follow"),
         crumbs([("Home", "/"), ("Shop Online", PATH), ("Search", None)])]
    o.append(f'''<section class="hero hero--slim"><div class="wrap">
<h1>Search the shop</h1>
<form id="search-form" class="search-form search-form--page" action="/search/" method="get" role="search">
{icon("search")}<label for="page-q" class="sr-only">Search products</label>
<input id="page-q" type="search" name="q" placeholder="Gloves, bipod, pouch, a model number&hellip;" autocomplete="off" enterkeyhint="search">
<button class="btn" type="submit">Search</button></form>
<p id="search-count" class="search-count" aria-live="polite"></p>
</div></section>
<section class="sec"><div class="wrap">
<div id="search-results" class="picks"></div>
<noscript><p>Search needs JavaScript. Browse the <a href="{PATH}">departments</a> instead.</p></noscript>
<p style="margin-top:26px"><a href="{PATH}">Browse all departments &rarr;</a></p>
</div></section>
''')
    o.append(footer())
    write(path, "".join(o))      # deliberately not returned: stays out of the sitemap


def thanks_page():
    """/shop/thanks/: where Stripe sends a customer after paying. Clears the
    cart (cart.js sees data-clear-cart). Not indexed, not in the sitemap."""
    path = "/shop/thanks/"
    title, desc = "Thank you | Magnum Sports", "Your order is paid."
    o = [head(title, desc, path, page_schema("WebPage", title, desc, path), robots="noindex,nofollow"),
         crumbs([("Home", "/"), ("Shop Online", PATH), ("Thank you", None)])]
    o.append(f'''<section class="hero hero--slim" data-clear-cart><div class="wrap">
<span class="eyebrow">{icon("cart")} Order received</span>
<h1>Thank you: your order is paid</h1>
<p class="lede">Stripe has emailed your receipt. We check your order and deliver it anywhere in New Zealand in 7 to 10 days. If anything is unavailable, we will contact you and refund it in full.</p>
<p style="margin-top:18px"><a class="btn" href="{PATH}">Keep shopping</a> <a class="btn btn--ghost" href="/contact/">Questions? Contact us</a></p>
</div></section>
''')
    o.append(footer())
    write(path, "".join(o))      # deliberately not returned: stays out of the sitemap


def build():
    write_cart_js()
    thanks_page()
    write_search()
    search_page()
    depts = by_dept()
    out = [front(depts)]
    for name, slug, ic, blurb, items in depts:
        out.append(dept_page(name, slug, ic, blurb, items))
        for i, p in enumerate(items):
            # "More in" shows the next few along, so neighbours link to each other
            ring = items[i + 1:] + items[:i]
            out.append(product_page(p, ring))
    return out
