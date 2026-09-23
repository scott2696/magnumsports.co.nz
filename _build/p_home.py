# -*- coding: utf-8 -*-
"""Homepage — Magnum Sports, outdoor gear online."""
from lib import *
from faq_data import HOME as FAQ

PATH = "/"
TITLE, DESC = META[PATH]
PER_DEPT = 5

# Hero collage: (sku, two short facts for its hotspot). Facts must be true of
# the product: take them from its name or specifications.
HERO_PICKS = [
    ("petram-lm201", ["MOLLE webbing all round", "Room for a multi-day trip"]),
    ("petram-a27-blk", ["Touchscreen fingertips", "Full-finger protection"]),
    ("petram-v8-b", ["6&ndash;9 inch legs", "360&deg; tilt"]),
    ("petram-lb-122", ["MOLLE-mount first aid pouch", "Room for a personal kit"]),
]


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


def hero_card(i, p, facts):
    """One product in the hero collage, with its '+' hotspot card."""
    name = esc(p["name"].split(" — ")[0])
    url = product_url(p)
    load = 'fetchpriority="high"' if i == 0 else 'loading="lazy"'
    items = "".join(f"<li>{f}</li>" for f in facts)
    return (f'<figure class="hs-card hs-card--{i}">'
            f'<a href="{url}" tabindex="-1" aria-hidden="true"><img src="{product_image(p["sku"])}" alt="" '
            f'width="600" height="600" {load} decoding="async"></a>'
            f'<details class="hs-spot"><summary aria-label="About the {name}"><span aria-hidden="true">+</span></summary>'
            f'<div class="hs-pop"><div class="hs-pop-head"><img src="{product_image(p["sku"])}" alt="" '
            f'width="64" height="64" loading="lazy" decoding="async">'
            f'<div><span class="hs-pop-dept">{esc(p["dept"])}</span><b>{name}</b></div></div>'
            f'<ul>{items}</ul><a href="{url}">View product &rarr;</a></div></details></figure>')


def build():
    depts = by_dept()
    total = sum(len(d[4]) for d in depts)
    schema = page_schema("WebPage", TITLE, DESC, PATH,
                         extra=[store_schema(), crumb_schema([("Home", "/")]),
                                faq_schema(FAQ, f"{SITE}/#faq")])
    o = [head(TITLE, DESC, PATH, schema)]

    # ------------------------------------------------------------ hero
    # Dawn over the ranges (drawn in SVG, so no photo licence and almost no
    # weight), four real products in a staggered collage, each with a "+"
    # hotspot (a <details>, so it works without script and by tap), and only
    # trust claims that are true.
    picks = [p for s in HERO_PICKS for p in PRODUCTS if p["sku"] == s[0]]
    facts = {s[0]: s[1] for s in HERO_PICKS}
    collage = "".join(hero_card(i, p, facts[p["sku"]]) for i, p in enumerate(picks))
    trust = [("truck", "Free delivery", "Anywhere in NZ, 7&ndash;10 days"),
             ("lock", "Secure payment", "Through Stripe, incl. PayPal"),
             ("tag", f"{total} products", f"Across {len(depts)} departments"),
             ("chat", "Real people", "Replies usually same working day")]
    o.append(f'''<section class="hero hero--shop"><div class="hs-scene" aria-hidden="true">
<svg viewBox="0 0 1600 700" preserveAspectRatio="xMidYMax slice"><defs>
<linearGradient id="hs-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0C0B10"/><stop offset=".55" stop-color="#1B1622"/><stop offset=".86" stop-color="#4A2E1C"/><stop offset="1" stop-color="#8A531F"/></linearGradient>
<radialGradient id="hs-sun" cx=".72" cy=".86" r=".42"><stop offset="0" stop-color="#FFBC4D" stop-opacity=".75"/><stop offset=".35" stop-color="#F5A524" stop-opacity=".22"/><stop offset="1" stop-color="#F5A524" stop-opacity="0"/></radialGradient></defs>
<rect width="1600" height="700" fill="url(#hs-sky)"/><rect width="1600" height="700" fill="url(#hs-sun)"/>
<circle cx="1152" cy="604" r="38" fill="#FFD27A" opacity=".85"/>
<path d="M0 560 L140 470 L260 520 L420 400 L560 500 L700 430 L860 520 L1010 440 L1160 520 L1300 450 L1460 520 L1600 470 V700 H0Z" fill="#2A1C1C" opacity=".85"/>
<path d="M0 610 L180 520 L330 590 L520 500 L690 600 L880 530 L1060 610 L1240 540 L1420 610 L1600 560 V700 H0Z" fill="#1A1418"/>
<path d="M0 660 L220 600 L460 650 L700 590 L960 660 L1200 610 L1440 660 L1600 630 V700 H0Z" fill="#0F0D12"/>
</svg></div>
<div class="wrap hs-grid">
<div class="hs-copy">
<span class="eyebrow">{icon("compass")} {esc(STORE["name"])} &middot; Outdoor gear online</span>
<h1>Gear that goes the distance</h1>
<p class="lede">Tactical gloves, packs, pouches, bipods and outdoor clothing, built for hard use and delivered free anywhere in New Zealand.</p>
<div class="hs-ctas"><a class="btn hs-cta" href="/shop/">{icon("cart")} Shop the range</a><a class="btn btn--ghost hs-cta" href="/search/">{icon("search")} Find your gear</a></div>
<ul class="hs-trust">{"".join(f'<li>{icon(ic)}<span><b>{t}</b>{d}</span></li>' for ic, t, d in trust)}</ul>
</div>
<div class="hs-art">{collage}</div>
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
 ("cart", "1. Add to your cart" if SHOW_PRICES else "1. Add to your enquiry", "Browse by department or search, and add what you want. Your list is kept in your browser until you send it.", "/shop/", "Start shopping"),
 ("mail", "2. Send your order" if SHOW_PRICES else "2. Send your enquiry", "Fill in your details and delivery address. We reply, usually the same working day, to confirm stock. Delivery is already in the price." if SHOW_PRICES else "Fill in your details and delivery address. We reply, usually the same working day, with prices and stock. Delivery is free.", None),
 ("wallet", "3. Pay and we deliver", "Payment is made through Stripe: Visa, Mastercard, American Express, Apple Pay, Google Pay, PayPal or Link. We deliver anywhere in New Zealand in 7 to 10 days.", None),
])}
<div style="margin-top:22px">{pay_badges()}</div>
</div></section>
''')

    o.append(faq_block(FAQ, "Common questions"))
    o.append(footer())
    return write(PATH, "".join(o))
