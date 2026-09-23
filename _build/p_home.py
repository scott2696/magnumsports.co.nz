# -*- coding: utf-8 -*-
"""Homepage — Magnum Sports, outdoor gear online."""
from lib import *
from faq_data import HOME as FAQ

PATH = "/"
TITLE, DESC = META[PATH]
PER_DEPT = 5


def sample(items):
    """Five per department that show its range: one of each kind of product
    (by the first word of its description), commonest kind first, photographed
    ones only when there are enough, and no colourway twice."""
    pics = [p for p in items if product_image(p["sku"])]
    pool = pics if len(pics) >= PER_DEPT else items
    kinds = {}
    for p in pool:
        kinds.setdefault(p["blurb"].split(".")[0].lower(), []).append(p)
    queues = sorted(kinds.values(), key=len, reverse=True)
    out, seen = [], set()
    while len(out) < PER_DEPT and any(queues):
        for q in queues:
            while q and len(out) < PER_DEPT:
                p = q.pop(0)
                base = p["name"].split(" — ")[0]
                if base not in seen:
                    seen.add(base)
                    out.append(p)
                    break
    return out


def build():
    depts = by_dept()
    total = sum(len(d[4]) for d in depts)
    schema = page_schema("WebPage", TITLE, DESC, PATH,
                         extra=[store_schema(), crumb_schema([("Home", "/")]),
                                faq_schema(FAQ, f"{SITE}/#faq")])
    o = [head(TITLE, DESC, PATH, schema)]

    # ------------------------------------------------------------ hero
    o.append(f'''<section class="hero"><div class="wrap">
<span class="eyebrow">{icon("cart")} Outdoor gear online &middot; Delivered across New Zealand</span>
<h1>{esc(STORE["name"])}: Outdoor Gear, Delivered</h1>
<p class="lede">Gloves, clothing, pouches, packs, bipods and hunting accessories. Add what you need to your cart, send us the order, and we confirm stock before anything is charged. Every price includes delivery anywhere in New Zealand.</p>
<div class="hero-stats">
<div class="hero-stat"><b>{total}</b><span>Products online</span></div>
<div class="hero-stat"><b>{len(depts)}</b><span>Departments</span></div>
<div class="hero-stat"><b>Free delivery</b><span>NZ-wide, 7&ndash;10 days</span></div>
<div class="hero-stat"><b><a href="tel:{STORE["phone_tel"]}" style="color:inherit">{esc(STORE["phone_display"])}</a></b><span>Questions? Call us</span></div>
</div>
<p style="margin-top:22px"><a class="btn" href="/shop/">{icon("cart")} Shop now</a> <a class="btn btn--ghost" href="/search/">{icon("search")} Search</a></p>
</div></section>
''')

    # ----------------------------------------------------- departments
    groups = "".join(
        f'''<div class="shop-dept" id="all-{slug}"><h3 class="shop-dept-h">{icon(ic)} {esc(name)}
<a class="shop-dept-all" href="/shop/{slug}/">See all {len(items)} &rarr;</a></h3>
<div class="picks picks--5">{"".join(product_card(p, anchor=False) for p in sample(items))}</div></div>'''
        for name, slug, ic, _, items in depts)
    o.append(f'''<section id="shop-online" class="sec"><div class="wrap">
<div class="sec-head"><span class="kicker">Shop online</span><h2>Shop by department</h2>
<p>{total} products, delivered free anywhere in New Zealand in 7 to 10 days. Pick a department to see everything in it, or click any product for its full description and specifications.</p></div>
{shop_tiles(depts)}
</div></section>
<section id="shop-picks" class="sec sec--haze"><div class="wrap">
<div class="sec-head"><span class="kicker">From the shop</span><h2>A few from each department</h2>
<p>Five from each department. Add to your cart here, or open a department to see the rest.</p></div>
{groups}
</div></section>
''')

    # -------------------------------------------------------- featured
    if FEATURED:
        o.append(f'''<section class="sec"><div class="wrap">
<div class="sec-head"><span class="kicker">Our own range</span><h2>Long-standing favourites</h2>
<p>Lines our customers keep coming back for. Put your size and colour in the order notes and we confirm them before you pay.</p></div>
<div class="picks">{"".join(product_card(p, anchor=False) for p in FEATURED)}</div>
</div></section>
''')

    # ------------------------------------------------------ how it works
    o.append(f'''<section class="sec sec--haze"><div class="wrap">
<div class="sec-head"><span class="kicker">How it works</span><h2>Ordering, payment and delivery</h2></div>
{cards([
 ("cart", "1. Add to your cart", "Browse by department or search, and add what you want. Your cart is kept in your browser until you send it.", "/shop/", "Start shopping"),
 ("mail", "2. Send your order", "Fill in your details and delivery address. We reply, usually the same working day, to confirm stock. Delivery is already in the price.", None),
 ("wallet", "3. Pay and we deliver", "Pay by card online through a secure Stripe link we email you, by bank transfer, or by card over the phone. We deliver anywhere in New Zealand in 7 to 10 days.", None),
])}
<div style="margin-top:22px">{pay_badges()}</div>
</div></section>
''')

    o.append(faq_block(FAQ, "Common questions"))
    o.append(footer())
    return write(PATH, "".join(o))
