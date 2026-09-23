#!/usr/bin/env python3
"""Shared templating, schema and components for magnumsports.co.nz."""
import json, os, re, html, hashlib, datetime
from pixels import px, trim_to_px, LIMIT as TITLE_PX

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://magnumsports.co.nz"
NAME = "Magnum Sports"
TAG = "Outdoor Gear Online"

# The business behind the online shop. Facts here are its published trading
# details — do not invent additions. The address is shown as the business
# address (NZ consumer law expects one), not as a shop to visit.
STORE = {
    "name": "Magnum Sports",
    "legal": "Magnum Sports New Zealand",
    "tagline": "Hunting, Fishing, Camping, Clothing and more.",
    "blurb": ("Magnum Sports Taranaki, New Zealand for your outdoor gear and "
              "sports equipment."),
    "street": "220 Broadway",
    "suburb": "Stratford",
    "region": "Taranaki",
    "postcode": "4332",
    "country": "NZ",
    "phone_display": "06 765 7248",
    "phone_tel": "+6467657248",
}

# (name, slug, icon, blurb). The shop's categories. A department appears on
# the site only once it has products; the rest are ready for when they do.
DEPARTMENTS = [
    ("Apparel", "apparel", "shirt",
     "Gloves, bush shirts, thermals, rainwear, camo and everyday outdoor clothing "
     "built for a New Zealand winter rather than a catalogue shoot."),
    ("Bags", "bags", "pack",
     "Pouches, day packs, hunting packs, dry bags and storage: carry gear that "
     "survives more than one season."),
    ("Fishing", "fishing", "fish",
     "Freshwater and saltwater: rods, reels, line, lures, flies, nets and "
     "terminal tackle."),
    ("Footwear", "footwear", "boot",
     "Boots for the bush, gumboots for the paddock, wading boots for the "
     "river, and socks worth the money."),
    ("Hunting Accessories", "hunting-accessories", "compass",
     "Bipods, game bags, calls, rangefinders, headlamps and the hundred small "
     "things you notice only when you have forgotten one."),
    ("Outdoor Leisure", "outdoor-leisure", "tent",
     "Camping, tramping and family gear: tents, sleeping bags, chilly bins, "
     "cookers, torches and chairs."),
    ("Sporting Goods", "sporting-goods", "ball",
     "General sports equipment and club gear."),
    ("Clearance", "clearance", "tag",
     "End-of-line and last-season stock at reduced prices."),
]

# The online catalogue, one product per entry in products.json. Only products
# we can evidence from the store's own catalogue are in it; add the rest from
# the real stock list — do not invent SKUs or prices. Fields:
#   sku       stable id, lowercase-hyphenated; the cart stores it, so never reuse one
#   name      as shown to customers
#   price     NZD as a string, e.g. "109.99"
#   dept      exactly one DEPARTMENTS name
#   blurb     one or two sentences
#   options   optional list, e.g. sizes ["S", "M", "L"] — the customer must pick one
#   featured  optional true — also shown on the homepage
PRODUCTS = json.load(open(os.path.join(ROOT, "_build", "products.json"), encoding="utf-8"))


def _supplier_products():
    """Rows from the supplier price sheets in _build/supplier/*.csv that the
    shop has chosen to sell (sell = yes) AND priced (retail_nzd). Everything
    else on a sheet stays off the site."""
    import csv, glob
    out = []
    for path in sorted(glob.glob(os.path.join(ROOT, "_build", "supplier", "*.csv"))):
        for n, row in enumerate(csv.DictReader(open(path, encoding="utf-8-sig")), 2):
            if row.get("sell", "").strip().lower() not in ("y", "yes", "1", "true"):
                continue
            price = row.get("retail_nzd", "").strip().lstrip("$").replace(",", "")
            if not price:
                raise ValueError(f"{os.path.basename(path)} line {n}: sell is yes but retail_nzd is empty")
            try:
                price = f"{float(price):.2f}"
            except ValueError:
                raise ValueError(f"{os.path.basename(path)} line {n}: retail_nzd {price!r} is not a number")
            specs = [tuple(x.split(": ", 1)) for x in row.get("specs", "").split(" | ") if ": " in x]
            out.append({"sku": row["sku"].strip(), "name": row["name"].strip(), "price": price,
                        "supplier": row.get("supplier", "").strip(),
                        "dept": row["dept"].strip(), "blurb": row["blurb"].strip(),
                        "model": row.get("model", "").strip(), "specs": specs,
                        "origin": row.get("origin", "").strip()})
    return out


PRODUCTS += _supplier_products()
_depts = {d[0] for d in DEPARTMENTS}
_skus = set()
for _p in PRODUCTS:
    if _p["dept"] not in _depts:
        raise ValueError(f"products.json: {_p['sku']} has unknown dept {_p['dept']!r}")
    if not re.fullmatch(r"[a-z0-9-]+", _p["sku"]) or _p["sku"] in _skus:
        raise ValueError(f"products.json: bad or duplicate sku {_p['sku']!r}")
    if not re.fullmatch(r"\d+\.\d{2}", _p["price"]):
        raise ValueError(f"products.json: {_p['sku']} price must look like 109.99")
    _skus.add(_p["sku"])
FEATURED = [p for p in PRODUCTS if p.get("featured")]
DEPT_SLUG = {d[0]: d[1] for d in DEPARTMENTS}


def dept_url(dept):
    return f"/shop/{DEPT_SLUG[dept]}/"


def product_url(p):
    return f"/shop/{DEPT_SLUG[p['dept']]}/{p['sku']}/"
EMAIL = "editor@magnumsports.co.nz"
# Card checkout. The Cloudflare Worker in _build/stripe-worker/ holds the Stripe
# key and opens Stripe Checkout for the cart. Paste its address here once it is
# deployed (e.g. "https://magnumsports-checkout.<you>.workers.dev/checkout");
# while it is empty the site offers order requests only, as before.
CHECKOUT_WORKER = "https://magnumsports-checkout.scott2696.workers.dev/checkout"

# Prices on the site. While False (prices not yet confirmed with suppliers):
# no price is shown or published anywhere, the cart is an enquiry list, and
# card checkout is off. Set True and rebuild to show prices and take payment.
SHOW_PRICES = False
CHECKOUT_URL = CHECKOUT_WORKER if SHOW_PRICES else ""
# Order requests, enquiries and contact messages are posted here; the Worker
# emails them to the shop's private inbox (its NOTIFY_TO secret), so that
# address never appears on the site. Empty = fall back to opening the
# customer's email app addressed to ORDER_EMAIL.
MESSAGE_URL = CHECKOUT_WORKER.rsplit("/", 1)[0] + "/message"

# Payment is through Stripe only. PAYMENT drives the badges and the structured
# data; METHODS is the plain-English list used in the copy. Only name methods
# switched on in Stripe (Settings -> Payment methods); Stripe shows each
# customer the methods that suit their country and device.
PAYMENT = ["Stripe", "Visa", "Mastercard", "American Express", "Apple Pay", "Google Pay"]
METHODS = ("Visa, Mastercard and American Express cards, Apple Pay, Google Pay, and any other "
           "payment method Stripe offers in your country")
if CHECKOUT_URL:
    PAY_HOW = ("Pay at checkout through <strong>Stripe</strong>&rsquo;s secure payment page, by "
               f"{METHODS}. If anything you have paid for turns out to be unavailable, we refund it in full.")
else:
    PAY_HOW = ("Once we confirm your order, we email you a secure <strong>Stripe</strong> payment link. "
               f"Pay by {METHODS}.")
# The shop's public address, shown on the site and used only if the Worker is
# unreachable. Cloudflare Email Routing forwards it to the private inbox.
ORDER_EMAIL = EMAIL
PUBLISHED = "2026-02-02"
# Resolved per page in write(), from the content-hash manifest below. A page
# that did not change keeps the date it already had, so "last updated" means
# something rather than "the day someone last ran the build".
UPDATED = "@@LASTMOD@@"
UPDATED_NZ = "@@LASTMOD_NZ@@"


NAV = [
    ("Home", "/", None),
    ("Shop", "/shop/", [("All Departments", "/shop/")]
                       + [(d[0], f"/shop/{d[1]}/") for d in DEPARTMENTS
                          if d[0] in {p["dept"] for p in PRODUCTS}]
                       + [("Search", "/search/"), ("Your Cart", "/shop/#cart")]),
    ("About", "/about/", None),
    ("Contact", "/contact/", None),
]

FOOTER = [
    ("Shop Online", [("All Departments", "/shop/")]
                    + [(d[0], f"/shop/{d[1]}/") for d in DEPARTMENTS
                       if d[0] in {p["dept"] for p in PRODUCTS}]
                    + [("Your Cart", "/shop/#cart")]),
    ("Company", [("About Us", "/about/"), ("Contact Us", "/contact/"), ("Search", "/search/")]),
    ("Legal", [("Terms and Conditions", "/terms/"), ("Privacy Policy", "/privacy/"),
               ("Cookie Policy", "/cookie-policy/"), ("Sitemap", "/sitemap.xml")]),
]

IC = {
 "star": '<path d="M12 3l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9 6.8 19.2l1-5.8L3.5 9.2l5.9-.9z"/>',
 "bolt": '<path d="M13 2 3 14h7l-1 8 10-12h-7z"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "shield": '<path d="M12 3l7.5 3v5.4c0 4.4-3 8.3-7.5 9.6-4.5-1.3-7.5-5.2-7.5-9.6V6z"/><path d="M9.2 12.2l2 2 3.6-3.8"/>',
 "wallet": '<rect x="3" y="6" width="18" height="13" rx="2.5"/><path d="M3 10h18M16.5 14.5h.01"/>',
 "dice": '<rect x="3" y="3" width="18" height="18" rx="4"/><circle cx="8.5" cy="8.5" r="1.3"/><circle cx="15.5" cy="15.5" r="1.3"/><circle cx="12" cy="12" r="1.3"/>',
 "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
 "coin": '<circle cx="12" cy="12" r="9"/><path d="M14.8 9.3A3 3 0 0 0 9.5 11c0 2.8 5 1.4 5 4.2a3 3 0 0 1-5.3 1.7M12 6.5v11"/>',
 "chat": '<path d="M21 12a8 8 0 0 1-11.6 7.1L3 21l1.9-6.4A8 8 0 1 1 21 12z"/>',
 "mobile": '<rect x="6" y="2.5" width="12" height="19" rx="2.8"/><path d="M11 18.5h2"/>',
 "ball": '<circle cx="12" cy="12" r="9"/><path d="M12 3v18M3.6 8.5h16.8M3.6 15.5h16.8"/>',
 "book": '<path d="M4 4.5A2.5 2.5 0 0 1 6.5 2H20v17H6.5A2.5 2.5 0 0 0 4 21.5z"/><path d="M4 17.5h16"/>',
 "flag": '<path d="M5 21V4M5 4h11l-1.8 3.5L16 11H5"/>',
 "lock": '<rect x="4" y="10" width="16" height="11" rx="2.5"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
 "mail": '<rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="m3 7 9 6 9-6"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
 "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M17 11.2a3.2 3.2 0 0 0 0-6.2M18 20h3.5a5.5 5.5 0 0 0-3.2-5"/>',
 "scale": '<path d="M12 3v18M7 21h10M12 6 5 9l3 5 3-5zM12 6l7 3-3 5-3-5z"/>',
 "target": '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3.1"/><path d="M12 1.6v3M12 19.4v3M1.6 12h3M19.4 12h3"/>',
 "cartridge": '<path d="M9 21h6V9.2L12 3 9 9.2z"/><path d="M9 13h6M9 17h6"/>',
 "shirt": '<path d="M8.6 3 5 5.1 3 9.2l3.1 1.5V21h11.8V10.7L21 9.2 19 5.1 15.4 3a3.4 3.4 0 0 1-6.8 0z"/>',
 "pack": '<rect x="5" y="7.5" width="14" height="13.5" rx="3"/><path d="M9 7.5V6a3 3 0 0 1 6 0v1.5"/><path d="M9.5 14h5"/>',
 "fish": '<path d="M20.4 12s-3 4.4-8 4.4S5.1 12 5.1 12s2.4-4.4 7.3-4.4 8 4.4 8 4.4z"/><path d="M5.1 12 1.9 8.7v6.6z"/><circle cx="16" cy="11" r=".9"/>',
 "boot": '<path d="M6 3h5v9.1c0 1.2.7 2.3 1.8 2.8l4.4 1.9c1.1.5 1.8 1.6 1.8 2.8V21H6z"/><path d="M6 17.2h13"/>',
 "compass": '<circle cx="12" cy="12" r="9"/><path d="m15.6 8.4-2.1 5.1-5.1 2.1 2.1-5.1z"/>',
 "tent": '<path d="M12 3.8 2.6 20.2h18.8z"/><path d="m12 3.8 4.1 16.4M12 3.8 7.9 20.2"/>',
 "gear": '<circle cx="12" cy="12" r="3.1"/><path d="M12 2.2v2.4M12 19.4v2.4M4.9 4.9l1.7 1.7M17.4 17.4l1.7 1.7M2.2 12h2.4M19.4 12h2.4M4.9 19.1l1.7-1.7M17.4 6.6l1.7-1.7"/>',
 "cart": '<circle cx="9.5" cy="20" r="1.4"/><circle cx="17.5" cy="20" r="1.4"/><path d="M2.5 3.5h2.6l2.4 12h11.3l2-8.5H6.1"/>',
 "tag": '<path d="M20.6 12.6 12.4 20.8 3.2 11.6V3.2h8.4z"/><circle cx="7.9" cy="7.9" r="1.5"/>',
}


# ---------------------------------------------------------------- metas ----
# One place for every title/description. Titles <= 60 chars, descriptions
# <= 158, each targeting a different head-keyword variant so pages do not
# compete with one another in the SERP.
META = {
 "/": ("Magnum Sports | Outdoor Gear Online, Delivered NZ-Wide",
       "Shop outdoor gear online from Magnum Sports: gloves, clothing, pouches, packs, bipods and hunting accessories, delivered across New Zealand in 7 to 10 days."),
 "/shop/": ("Shop Online | Magnum Sports",
       "Order outdoor gear online from Magnum Sports, with free delivery anywhere in New Zealand. Browse by department and send us your order or enquiry."),
 "/about/": ("About Magnum Sports | Outdoor Gear Online",
       "Magnum Sports is a New Zealand online store for outdoor gear: clothing, gloves, bags and hunting accessories, delivered NZ-wide."),
 "/contact/": ("Contact Magnum Sports",
       "Phone or email Magnum Sports about an order, delivery, stock or a product. We reply to every message."),
 "/terms/": ("Terms and Conditions | Magnum Sports",
       "Terms for using magnumsports.co.nz and ordering from our online shop: orders, pricing, payment, delivery, returns and your consumer rights."),
 "/privacy/": ("Privacy Policy | Magnum Sports",
       "How Magnum Sports collects, uses and protects personal information under the Privacy Act 2020, and how to access, correct or delete your data."),
 "/cookie-policy/": ("Cookie Policy | Magnum Sports",
       "Which cookies and browser storage magnumsports.co.nz uses, what each does, and how to refuse or delete them in any browser."),
}


def clamp(text, n):
    """Trim to n characters on a word boundary and return PLAIN text.

    Always returns unescaped text, whether or not it was truncated — callers
    escape once at render. Returning the original (entity-bearing) string when
    it fitted was double-escaping "&amp;" into "&amp;amp;".
    """
    import html as _h
    plain = _h.unescape(text)
    if len(plain) <= n:
        return plain
    return plain[:n].rsplit(" ", 1)[0].rstrip(" ,;:-\u2014")


def icon(k, cls=""):
    c = ' class="ic %s"' % cls if cls else ' class="ic"'
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{IC[k]}</svg>')


def esc(s):
    return html.escape(str(s), quote=True)


# ---------------------------------------------------------------- chrome ----

def head(title, desc, path, schema=None, image="/images/og-magnum.jpg", robots=None):
    if path in META:
        title, desc = META[path]
    title = trim_to_px(clamp(title, 90), TITLE_PX)
    desc = clamp(desc, 158)
    url = SITE + path
    r = robots or "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"
    s = f'''<!DOCTYPE html>
<html lang="en-NZ">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{r}">
<link rel="alternate" hreflang="en-nz" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta name="theme-color" content="#0C0B10">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,400..900&family=Hanken+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
<link rel="icon" type="image/png" sizes="144x144" href="/favicon-144x144.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192x192.png">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="shortcut icon" href="/favicon.ico">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="{NAME}">
<meta property="og:locale" content="en_NZ">
<meta property="og:image" content="{SITE}{image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE}{image}">
<link rel="stylesheet" href="/assets/css/site.css">
<script src="/assets/js/cart.js" defer></script>
<script src="/assets/js/search.js" defer></script>
'''
    if schema:
        s += ('<script type="application/ld+json">\n'
              + json.dumps(schema, ensure_ascii=False, separators=(",", ":")) + "\n</script>\n")
    s += "</head>\n<body>\n"
    s += '<a class="skip" href="#main">Skip to content</a>\n'
    return s + nav()


def nav():
    o = ['<header class="nav"><div class="wrap">',
         f'<a class="brand" href="/" aria-label="{NAME} — {TAG}">',
         '<svg class="brand-mark" width="34" height="34" viewBox="0 0 100 100" aria-hidden="true">',
         '<rect width="100" height="100" rx="22" fill="#2B2836"/>',
         '<path d="M20.5 73.5V26.5L50 58.5L79.5 26.5V73.5" fill="none" stroke="#F5A524" stroke-width="11.5" stroke-linecap="round" stroke-linejoin="round"/>',
         '<rect x="20.5" y="79.5" width="59" height="5.5" rx="2.75" fill="#F2EFE9"/></svg>',
         '<span class="brand-txt"><span class="brand-word">MAGNUM<i>.</i></span>',
         f'<span class="brand-tag">{esc(TAG)}</span></span></a>',
         '<nav class="nav-links" aria-label="Main">']
    ch = ('<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">'
          '<path d="M3 4.5l3 3 3-3"/></svg>')
    for label, href, kids in NAV:
        if not kids:
            o.append(f'<a href="{href}">{esc(label)}</a>')
        else:
            trig = (f'<a class="nav-trigger" href="{href}">{esc(label)} {ch}</a>' if href
                    else f'<span class="nav-trigger" tabindex="0" role="button">{esc(label)} {ch}</span>')
            inner = "".join(f'<a href="{h}">{esc(t)}</a>' for t, h in kids)
            o.append(f'<div class="nav-item">{trig}<div class="nav-dd"><div class="nav-dd-inner">{inner}</div></div></div>')
    o.append('</nav>')
    o.append(f'<button class="nav-search" type="button" aria-label="Search products" aria-expanded="false" '
             f'aria-controls="site-search">{icon("search")}</button>')
    o.append(f'<a class="nav-cart" href="/shop/#cart" aria-label="Cart">{icon("cart")}'
             '<span class="nav-cart-n" data-cart-count hidden>0</span></a>')
    o.append('<details class="menu"><summary aria-label="Open menu">'
             '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" '
             'stroke-width="2" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"/></svg></summary>'
             '<div class="menu-panel">')
    for label, href, kids in NAV:
        if not kids:
            o.append(f'<a href="{href}">{esc(label)}</a>')
        else:
            o.append(f'<b>{esc(label)}</b>')
            o += [f'<a href="{h}">{esc(t)}</a>' for t, h in kids]
    o.append('<b>Legal</b><a href="/terms/">Terms and Conditions</a><a href="/privacy/">Privacy Policy</a>'
             '<a href="/cookie-policy/">Cookie Policy</a>')
    o.append('</div></details></div>')
    o.append('<div class="search-panel" id="site-search" hidden><div class="wrap">'
             '<form action="/search/" method="get" role="search" class="search-form">'
             f'{icon("search")}<label for="site-q" class="sr-only">Search products</label>'
             '<input id="site-q" type="search" name="q" placeholder="Search products, e.g. gloves, bipod, pouch" '
             'autocomplete="off" enterkeyhint="search"><button class="btn btn--sm" type="submit">Search</button></form>'
             '<ul class="search-sugg" aria-live="polite"></ul></div></div>')
    o.append('</header>\n')
    return "".join(o)


def crumbs(items):
    """items: [(label, href|None)] — last has href None."""
    li = []
    for t, h in items:
        li.append(f'<li><a href="{h}">{esc(t)}</a></li>' if h else
                  f'<li><span aria-current="page">{esc(t)}</span></li>')
    return ('<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap"><ol>'
            + "".join(li) + '</ol></div></nav>\n')


def crumb_schema(items):
    el = []
    for i, (t, h) in enumerate(items, 1):
        d = {"@type": "ListItem", "position": i, "name": t}
        if h:
            d["item"] = SITE + h
        el.append(d)
    return {"@type": "BreadcrumbList", "@id": "#breadcrumb", "itemListElement": el}


def footer():
    cols = "".join(
        f'<div class="foot-col"><h4>{esc(h)}</h4><ul>'
        + "".join(f'<li><a href="{u}">{esc(t)}</a></li>' for t, u in links)
        + '</ul></div>' for h, links in FOOTER)
    return f'''<footer class="foot"><div class="wrap">
<div class="foot-top">
<div class="foot-col foot-about">
<a class="brand" href="/" style="margin-bottom:14px">
<svg class="brand-mark" width="32" height="32" viewBox="0 0 100 100" aria-hidden="true"><rect width="100" height="100" rx="22" fill="#2B2836"/><path d="M20.5 73.5V26.5L50 58.5L79.5 26.5V73.5" fill="none" stroke="#F5A524" stroke-width="11.5" stroke-linecap="round" stroke-linejoin="round"/><rect x="20.5" y="79.5" width="59" height="5.5" rx="2.75" fill="#F2EFE9"/></svg>
<span class="brand-txt"><span class="brand-word">MAGNUM<i>.</i></span><span class="brand-tag">{esc(TAG)}</span></span></a>
<p>Outdoor gear online, delivered across New Zealand in 7 to 10 days.</p>
<p><a href="tel:+6467657248">06 765 7248</a> &middot; <a href="mailto:{EMAIL}">{EMAIL}</a><br>{esc(STORE["legal"])}, {esc(STORE["street"])}, {esc(STORE["suburb"])} {esc(STORE["postcode"])}</p>
<p><a href="/shop/">Shop online</a> &middot; <a href="/search/">Search</a></p>
{pay_badges()}
</div>
{cols}
</div>
<div class="foot-bot">
<p>Prices are in New Zealand dollars and include GST and delivery anywhere in New Zealand. Orders are confirmed by us before payment and delivered in 7 to 10 days.</p>
<div class="foot-badges">
<a href="/shop/">Shop online</a>
<a href="tel:+6467657248">06 765 7248</a>
<a href="/contact/">Contact</a>
</div>
</div>
<p style="margin-top:22px;font-size:.78rem">&copy; 2026 {esc(NAME)}. All rights reserved. magnumsports.co.nz</p>
</div></footer>
</body>
</html>
'''


# ------------------------------------------------------------ components ----


def faq_block(items, heading="Frequently asked questions", intro=None):
    d = "".join(f'<details><summary>{q}</summary><div class="faq-body">{a}</div></details>'
                for q, a in items)
    i = f'<p>{intro}</p>' if intro else ""
    return (f'<section id="faq" class="sec sec--haze"><div class="wrap">'
            f'<div class="sec-head"><span class="kicker">Answers</span><h2>{heading}</h2>{i}</div>'
            f'<div class="faq">{d}</div></div></section>\n')


def faq_schema(items, pid="#faq"):
    import re
    def strip(t):
        return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t)).strip()
    return {"@type": "FAQPage", "@id": pid,
            "mainEntity": [{"@type": "Question", "name": strip(q),
                            "acceptedAnswer": {"@type": "Answer", "text": strip(a)}}
                           for q, a in items]}


def product_image(sku):
    """Path to a product photo at images/products/<sku>.webp|jpg, else None."""
    for ext in ("webp", "jpg", "png"):
        rel = f"images/products/{sku}.{ext}"
        if os.path.exists(os.path.join(ROOT, rel)):
            return "/" + rel
    return None


def price_html(p, extra=""):
    """The price, or 'Price on request' while prices are hidden."""
    if SHOW_PRICES:
        return f'<div class="prod-price{extra}">NZ${esc(p["price"])}</div>'
    return f'<div class="prod-price prod-price--ask{extra}">Price on request</div>'


def product_cta(p, size="btn--sm"):
    """Add-to-cart control (cart.js wires it up). Must sit inside an element
    with data-sku."""
    opts = ""
    if p.get("options"):
        oid = f'opt-{p["sku"]}'
        opts = (f'<div class="field prod-opt"><label for="{oid}">Option</label>'
                f'<select id="{oid}" data-opt><option value="">Choose&hellip;</option>'
                + "".join(f'<option>{esc(o)}</option>' for o in p["options"])
                + '</select></div>')
    label = "Add to cart" if SHOW_PRICES else "Add to enquiry"
    return (f'{opts}<button class="btn {size}" type="button" data-add="{esc(p["sku"])}">'
            f'{icon("cart")} {label}</button>')


def product_card(p, anchor=True):
    """One catalogue item: photo and name link to its own page. anchor=False
    drops the id, for a second copy of the same card on one page."""
    cta = product_cta(p)
    img = product_image(p["sku"])
    url = product_url(p)
    if img:
        media = (f'<a class="prod-img" href="{url}" tabindex="-1" aria-hidden="true"><img src="{img}" alt="" '
                 f'width="600" height="600" loading="lazy" decoding="async"></a>')
    else:
        # No photo yet: a square tile with the department icon keeps the row even.
        # Drop images/products/<sku>.jpg (or .webp/.png) in and rebuild to replace it.
        ic = next((d[2] for d in DEPARTMENTS if d[0] == p["dept"]), "tag")
        media = (f'<a class="prod-img prod-img--empty" href="{url}" tabindex="-1" aria-hidden="true">'
                 f'{icon(ic)}</a>')
    aid = f' id="{esc(p["sku"])}"' if anchor else ""
    return (f'<div class="pick prod"{aid} data-sku="{esc(p["sku"])}">{media}<span class="pick-cat">{esc(p["dept"])}</span>'
            f'<div class="pick-brand"><b><a class="prod-link" href="{url}">{esc(p["name"])}</a></b></div>'
            f'<p>{esc(p["blurb"])}</p>'
            f'{price_html(p)}{cta}</div>')


# ---------------------------------------------------------------- shop
def by_dept():
    """(name, slug, icon, blurb, products) for every department with stock online."""
    out = []
    for name, slug, ic, blurb in DEPARTMENTS:
        items = [p for p in PRODUCTS if p["dept"] == name]
        if items:
            out.append((name, slug, ic, blurb, items))
    return out


COVER = {"Apparel": "glove", "Bags": "pouch", "Hunting Accessories": "bipod"}


def shop_tiles(depts=None):
    """One tile per online department: cover photo, name, product count."""
    depts = depts or by_dept()
    tiles = []
    for name, slug, ic, blurb, items in depts:
        # Cover photo: the first product of the department's most typical kind
        # (gloves for Apparel, pouches for Bags...), not whatever happens to sort first.
        want = COVER.get(name, "")
        pool = [p for p in items if want in p["name"].lower()] + items
        img = next((product_image(p["sku"]) for p in pool if product_image(p["sku"])), None)
        media = (f'<img src="{img}" alt="" width="600" height="600" loading="lazy" decoding="async">'
                 if img else f'<span class="dept-ic">{icon(ic)}</span>')
        n = len(items)
        tiles.append(f'''<a class="shop-cat" href="/shop/{slug}/"><span class="shop-cat-img{"" if img else " shop-cat-img--empty"}">{media}</span>
<span class="shop-cat-body"><b>{esc(name)}</b><span>{n} product{"s" if n != 1 else ""}</span></span></a>''')
    return '<div class="shop-cats">' + "".join(tiles) + '</div>'


_PAY_MARK = {
 "American Express": ('<svg viewBox="0 0 44 24" aria-hidden="true"><rect width="44" height="24" rx="3" fill="#2E77BC"/>'
                      '<text x="22" y="16" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="10" '
                      'font-weight="900" fill="#fff" letter-spacing=".6">AMEX</text></svg>'),
 "Apple Pay": ('<svg viewBox="0 0 62 24" aria-hidden="true"><text x="31" y="17" text-anchor="middle" '
               'font-family="-apple-system,Helvetica,Arial,sans-serif" font-size="14" font-weight="600" '
               'fill="#000">Apple Pay</text></svg>'),
 "Google Pay": ('<svg viewBox="0 0 70 24" aria-hidden="true"><text x="35" y="17" text-anchor="middle" '
                'font-family="Arial,Helvetica,sans-serif" font-size="13.5" font-weight="600" fill="#3c4043">'
                '<tspan fill="#4285F4">G</tspan><tspan fill="#EA4335">o</tspan><tspan fill="#FBBC04">o</tspan>'
                '<tspan fill="#4285F4">g</tspan><tspan fill="#34A853">l</tspan><tspan fill="#EA4335">e</tspan> Pay</text></svg>'),
 "Visa": ('<svg viewBox="0 0 48 16" aria-hidden="true"><text x="24" y="13" text-anchor="middle" '
          'font-family="Arial,Helvetica,sans-serif" font-size="15" font-weight="900" font-style="italic" '
          'fill="#1A1F71" letter-spacing=".5">VISA</text></svg>'),
 "Stripe": ('<svg viewBox="0 0 60 25" aria-hidden="true"><text x="30" y="19" text-anchor="middle" '
            'font-family="Arial,Helvetica,sans-serif" font-size="19" font-weight="700" fill="#635BFF" '
            'letter-spacing="-.4">stripe</text></svg>'),
 "Mastercard": ('<svg viewBox="0 0 38 24" aria-hidden="true"><circle cx="14" cy="12" r="9" fill="#EB001B"/>'
                '<circle cx="24" cy="12" r="9" fill="#F79E1B"/><path d="M19 4.6a9 9 0 0 1 0 14.8a9 9 0 0 1 0-14.8z" '
                'fill="#FF5F00"/></svg>'),
}


def pay_badges(label=True):
    """The accepted payment methods as small badges."""
    # Logo-only marks get a hidden text label; marks with visible text do not need one.
    marks = "".join(f'<li class="pay-{m.split()[0].lower()}" title="{esc(m)}">'
                    + ("" if "<span>" in _PAY_MARK[m] else f'<span class="sr-only">{esc(m)}</span>')
                    + f'{_PAY_MARK[m]}</li>' for m in PAYMENT)
    lead = '<span class="pay-lead">We accept</span>' if label else ""
    return f'<div class="pay">{lead}<ul class="pay-list">{marks}</ul></div>'


def cards(items, cls="grid--3"):
    """items: [(icon, title, body, link|None, linktext|None)]"""
    out = []
    for ic, t, b, *rest in items:
        link = ""
        if rest and rest[0]:
            link = f'<p><a href="{rest[0]}">{rest[1] if len(rest) > 1 else "Read more"} &rarr;</a></p>'
        out.append(f'<div class="card card--link"><div class="card-ic">{icon(ic)}</div>'
                   f'<h3>{t}</h3><p>{b}</p>{link}</div>')
    return f'<div class="grid {cls}">' + "".join(out) + '</div>'


def table(headers, rows, caption=None, minw=None):
    th = "".join(f"<th scope=\"col\">{h}</th>" for h in headers)
    tr = "".join("<tr>" + "".join(
        (f'<th scope="row" class="t-brand">{c}</th>' if i == 0 else f"<td>{c}</td>")
        for i, c in enumerate(r)) + "</tr>" for r in rows)
    cap = f"<caption>{caption}</caption>" if caption else ""
    style = f' style="min-width:{minw}px"' if minw else ""
    return f'<div class="tw">{cap}<table{style}><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'


def keyfacts(pairs):
    return '<div class="keyfacts">' + "".join(
        f'<div class="keyfact"><span>{esc(k)}</span><b>{v}</b></div>' for k, v in pairs) + '</div>'


def org_schema():
    return {
        "@type": "Organization", "@id": f"{SITE}/#organization", "name": NAME, "url": SITE,
        "logo": {"@type": "ImageObject", "url": f"{SITE}/favicon-512x512.png", "width": 512, "height": 512},
        "email": EMAIL, "areaServed": {"@type": "Country", "name": "New Zealand"},
        "knowsLanguage": "en-NZ",
        "description": "Outdoors and sporting goods retailer in Stratford, Taranaki, New Zealand.",
        "telephone": STORE["phone_tel"],
    }


def store_schema():
    """OnlineStore entity for the business behind this domain."""
    return {
        "@type": "OnlineStore",
        "@id": f"{SITE}/#store",
        "name": STORE["legal"],
        "alternateName": STORE["name"],
        "url": SITE,
        "telephone": STORE["phone_tel"],
        "image": f"{SITE}/images/og-magnum.jpg",
        "logo": f"{SITE}/favicon-512x512.png",
        "description": f'{STORE["tagline"]} {STORE["blurb"]}',
        "address": {
            "@type": "PostalAddress",
            "streetAddress": STORE["street"],
            "addressLocality": STORE["suburb"],
            "addressRegion": STORE["region"],
            "postalCode": STORE["postcode"],
            "addressCountry": STORE["country"],
        },
        "areaServed": {"@type": "Country", "name": "New Zealand"},
        "currenciesAccepted": "NZD",
        "paymentAccepted": ", ".join(PAYMENT),
        "parentOrganization": {"@id": f"{SITE}/#organization"},
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Departments",
            "itemListElement": [
                {"@type": "OfferCatalog", "name": d[0],
                 "url": f"{SITE}/shop/{d[1]}/"} for d in DEPARTMENTS
                if d[0] in {p["dept"] for p in PRODUCTS}
            ],
        },
    }


def site_schema():
    return {"@type": "WebSite", "@id": f"{SITE}/#website", "name": NAME, "url": SITE,
            "publisher": {"@id": f"{SITE}/#organization"}, "inLanguage": "en-NZ"}


def page_schema(kind, title, desc, path, extra=None):
    """Standard @graph for a page."""
    g = [org_schema(), site_schema()]
    wp = {"@type": ["WebPage", kind] if kind and kind != "WebPage" else "WebPage",
          "@id": f"{SITE}{path}#webpage", "url": SITE + path, "name": title,
          "description": desc, "inLanguage": "en-NZ",
          "isPartOf": {"@id": f"{SITE}/#website"},
          "publisher": {"@id": f"{SITE}/#organization"},
          "datePublished": PUBLISHED, "dateModified": UPDATED,
          "primaryImageOfPage": {"@type": "ImageObject", "url": f"{SITE}/images/og-magnum.jpg"}}
    g.append(wp)
    if extra:
        g += extra
    return {"@context": "https://schema.org", "@graph": g}


# ---------------------------------------------------------------- lastmod
_MANIFEST_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lastmod.json")
try:
    _MANIFEST = json.load(open(_MANIFEST_FILE))
except Exception:
    _MANIFEST = {}
LASTMOD = {}          # path -> ISO date, filled as pages are written


def _hashable(body):
    """Body as it is hashed for lastmod. The date placeholders are still
    unresolved at this point, so a rebuild alone never changes the hash."""
    return body


def _stamp(path, body):
    h = hashlib.sha256(_hashable(body).encode("utf-8")).hexdigest()[:16]
    prev = _MANIFEST.get(path)
    date = prev["date"] if (prev and prev.get("hash") == h) \
        else datetime.date.today().isoformat()
    LASTMOD[path] = date
    _MANIFEST[path] = {"hash": h, "date": date}
    nz = "%s/%s/%s" % (date[8:10], date[5:7], date[:4])
    return body.replace("@@LASTMOD@@", date).replace("@@LASTMOD_NZ@@", nz)


def save_manifest():
    # Only pages built this run: a deleted page leaves no entry behind.
    keep = {p: _MANIFEST[p] for p in LASTMOD}
    json.dump(keep, open(_MANIFEST_FILE, "w"), indent=1, sort_keys=True)


def write(path, body):
    """path: '/shop/' -> shop/index.html"""
    body = _stamp(path, body)
    rel = path.strip("/")
    d = os.path.join(ROOT, rel) if rel else ROOT
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(body)
    return path
