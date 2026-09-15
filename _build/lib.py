#!/usr/bin/env python3
"""Shared templating, schema and components for magnumsports.co.nz."""
import json, os, html
from paa_data import PAA
from pixels import px, trim_to_px, LIMIT as TITLE_PX

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://magnumsports.co.nz"
NAME = "Magnum Sports"
TAG = "Outdoors Store & NZ Betting Guide"

# The retail business this domain has always belonged to. Facts here are the
# store's own published trading details — do not invent additions.
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
    "products": 678,
}

# (name, slug, icon, blurb). A photo at images/departments/<slug>.jpg is used
# automatically when present; until then the card shows a brand gradient tile
# with the icon. Drop files in and rebuild — no markup changes needed.
DEPARTMENTS = [
    ("Airguns", "airguns", "target",
     "Air rifles and air pistols, pellets, targets and scopes. The sensible "
     "starting point for pest control on the farm and for target shooting."),
    ("Ammunition", "ammunition", "cartridge",
     "Rimfire, centrefire and shotgun ammunition from the calibres Taranaki "
     "hunters actually use. Firearms licence required — see below."),
    ("Apparel", "apparel", "shirt",
     "Bush shirts, thermals, rainwear, hunting camo and everyday outdoor "
     "clothing built for a Taranaki winter rather than a catalogue shoot."),
    ("Bags", "bags", "pack",
     "Day packs, hunting packs, meat packs, dry bags, rod tubes and gun bags "
     "— carry gear that survives more than one season."),
    ("Firearms and Accessories", "firearms-and-accessories", "shield",
     "Rifles, shotguns, scopes, mounts, slings, cases and safes. Licence and "
     "in-store paperwork required on every firearm we sell."),
    ("Fishing", "fishing", "fish",
     "Freshwater and saltwater — rods, reels, line, lures, flies, nets and "
     "terminal tackle for the Taranaki rivers and the coast."),
    ("Footwear", "footwear", "boot",
     "Boots for the bush, gumboots for the paddock, wading boots for the "
     "river, and socks worth the money."),
    ("Hunting Accessories", "hunting-accessories", "compass",
     "Knives, game bags, calls, rangefinders, headlamps, bipods and the "
     "hundred small things you notice only when you have forgotten one."),
    ("Outdoor Leisure", "outdoor-leisure", "tent",
     "Camping, tramping and family gear — tents, sleeping bags, chilly bins, "
     "cookers, torches and chairs."),
    ("Reloading", "reloading", "scale",
     "Presses, dies, powder, primers, projectiles, tumblers and scales for "
     "handloading your own."),
    ("Sporting Goods", "sporting-goods", "ball",
     "General sports equipment and club gear — the side of the shop that has "
     "kept Stratford supplied for years."),
    ("Clearance", "clearance", "tag",
     "End-of-line, ex-display and last-season stock at reduced prices. "
     "Changes constantly; worth a look every visit."),
]

# The only products we can evidence from the store's own catalogue. Add the
# rest from the real stock list before launch — do not invent SKUs or prices.
FEATURED = [
    ("4 Piece Hunters Pack", "109.99", "Hunting Accessories",
     "A starter bundle for anyone getting into the bush — the four things "
     "people come back for after their first trip without them."),
    ("5 TO 9 Track Pant", "109.99", "Apparel",
     "Hard-wearing track pant that works on the hill and in town. One of the "
     "steadiest sellers on the apparel wall."),
    ("360° Wide Brim Hat", "49.99", "Apparel",
     "Full-brim sun protection for fishing, farm work and summer tramping. "
     "Also stocked in a heavier $59.99 version."),
]
EMAIL = "editor@magnumsports.co.nz"
PUBLISHED = "2026-02-02"
UPDATED = "2026-09-14"
UPDATED_NZ = "14/09/2026"

# Title/description freshness stamp. ONE edit per month — change MONTH (and
# YEAR in January) and rebuild; every title, description and H1 follows.
# A stale month is worse than no month, so this is a standing commitment.
MONTH = "September"
YEAR = "2026"
MONTH_YEAR = f"{MONTH} {YEAR}"

OPS = json.load(open(os.path.join(ROOT, "_build", "operators.json")))
BY = {o["slug"]: o for o in OPS}
# One list per operator, in the order the operator table was supplied.
OPS.sort(key=lambda o: o["order"])
CASINOS = [o for o in OPS if o["list"] == "casino"]
SPORTS = [o for o in OPS if o["list"] == "sports"]


def pick_ops(slugs, listname="casino"):
    """A curated subset of operators, always returned in the master order from
    the operator table and filtered to the right toplist — so a casino page can
    never show a sportsbook-only brand, and a reorder propagates everywhere."""
    want = set(slugs)
    unknown = want - {o["slug"] for o in OPS}
    if unknown:
        raise KeyError(f"unknown operator slug(s): {sorted(unknown)}")
    return [o for o in OPS if o["slug"] in want and o["list"] == listname]

AUTHORS = {
    "angus-mclean": {
        "name": "Angus McLean", "role": "Writer",
        "img": "/images/authors/angus-mclean.jpg",
        "location": "Wellington, New Zealand",
        "since": "2026",
        # Add LinkedIn and any external bylines here before launch.
        "sameAs": [],
        "knows": ["online casinos", "online pokies", "casino bonus terms",
                  "withdrawal testing", "NZD payment methods", "sports betting",
                  "consumer affairs", "New Zealand gambling regulation"],
        "bio": "Angus McLean writes every review, guide and comparison on Magnum Sports. He came "
               "to gambling from consumer journalism, where the job was reading the contract "
               "nobody else had read, and he approaches an online casino the same way: open the "
               "account, deposit real money, request the withdrawal, and time what actually "
               "happens rather than what the marketing promises.",
        "short": "Writes every page on this site, and personally funds and times each withdrawal test.",
    },
    "witi-king": {
        "name": "Witi King", "role": "Fact Checker",
        "img": "/images/authors/witi-king.jpg",
        "location": "Taupō, New Zealand",
        "since": "2026",
        "sameAs": [],
        "knows": ["New Zealand gambling law", "Gambling Act 2003", "Racing Industry Act 2020",
                  "licensing and regulation", "tax on gambling winnings",
                  "gambling harm minimisation", "editorial standards", "responsible gambling"],
        "bio": "Witi King checks every factual claim on Magnum Sports before it is published. He "
               "spent most of his working life on the harm side of gambling rather than the "
               "marketing side, and he reads the legislation itself rather than someone else's "
               "summary of it — which is why several claims you will find on rival New Zealand "
               "sites do not appear on this one.",
        "short": "Checks every claim on this site against the primary source before it is published.",
    },
}

NAV = [
    ("Home", "/", None),
    ("Outdoors Store", "/#shop", [
        ("Shop by Department", "/#shop"),
        ("Airguns", "/#airguns"),
        ("Ammunition", "/#ammunition"),
        ("Apparel", "/#apparel"),
        ("Firearms and Accessories", "/#firearms-and-accessories"),
        ("Fishing", "/#fishing"),
        ("Hunting Accessories", "/#hunting-accessories"),
        ("Outdoor Leisure", "/#outdoor-leisure"),
        ("Visit the Store", "/#visit"),
    ]),
    ("Betting", "/online-betting/", None),
    ("Online Casinos", "/online-casinos/", [
        ("Best Online Casinos NZ", "/online-casinos/"),
        ("Licensed Online Casinos NZ", "/licensed-online-casinos/"),
        ("New Online Casinos NZ", "/new-casinos-nz/"),
        ("Online Pokies NZ", "/online-pokies/"),
        ("Casino Payout Percentages", "/casino-payout-percentages/"),
        ("Fast Payout Casinos", "/fast-payout-casinos/"),
        ("Live Casino NZ", "/live-casino/"),
        ("Crypto Casinos NZ", "/crypto-casinos-nz/"),
        ("Casino Bonus NZ", "/casino-bonus/"),
        ("No Deposit Bonus NZ", "/no-deposit-bonus/"),
        ("Casino Payment Methods", "/casino-payment-methods/"),
        ("Casino Reviews", "/casino-reviews/"),
    ]),
    ("Guides", None, [
        ("Is Online Gambling Legal in NZ?", "/licensed-online-casinos/"),
        ("Tax on Gambling Winnings NZ", "/gambling-winnings-tax-nz/"),
        ("Casino Payment Methods NZ", "/casino-payment-methods/"),
        ("How We Rate Casinos", "/how-we-rate-casinos/"),
        ("Responsible Gambling NZ", "/responsible-gambling/"),
    ]),
    ("About", "/about/", None),
    ("Contact", "/contact/", None),
]

FOOTER = [
    ("Outdoors Store", [("Shop by Department", "/#shop"), ("Firearms & Ammunition", "/#firearms-and-accessories"),
                        ("Fishing", "/#fishing"), ("Hunting Accessories", "/#hunting-accessories"),
                        ("Visit Us in Stratford", "/#visit")]),
    ("Casinos", [("Best Online Casinos NZ", "/online-casinos/"), ("Licensed Online Casinos NZ", "/licensed-online-casinos/"),
                 ("New Online Casinos NZ", "/new-casinos-nz/"), ("Online Pokies NZ", "/online-pokies/"),
                 ("Casino Payout Percentages", "/casino-payout-percentages/"), ("Fast Payout Casinos NZ", "/fast-payout-casinos/"),
                 ("Live Casino NZ", "/live-casino/"), ("Crypto Casinos NZ", "/crypto-casinos-nz/")]),
    ("Bonuses & Betting", [("Casino Bonus NZ", "/casino-bonus/"), ("No Deposit Bonus NZ", "/no-deposit-bonus/"),
                           ("Online Betting NZ", "/online-betting/"),
                           ("Casino Reviews NZ", "/casino-reviews/")]),
    ("Guides", [("Is Online Gambling Legal in NZ?", "/licensed-online-casinos/"), ("Tax on Winnings NZ", "/gambling-winnings-tax-nz/"),
                ("Casino Payment Methods NZ", "/casino-payment-methods/"), ("How We Rate Casinos", "/how-we-rate-casinos/")]),
    ("Company", [("About Us", "/about/"), ("Contact Us", "/contact/"), ("Our Authors", "/authors/"),
                 ("Responsible Gambling", "/responsible-gambling/")]),
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
 "tag": '<path d="M20.6 12.6 12.4 20.8 3.2 11.6V3.2h8.4z"/><circle cx="7.9" cy="7.9" r="1.5"/>',
}


# ---------------------------------------------------------------- metas ----
# One place for every title/description. Titles <= 60 chars, descriptions
# <= 158, each targeting a different head-keyword variant so pages do not
# compete with one another in the SERP.
META = {
 "/": ("Magnum Sports | Outdoors Store, Stratford Taranaki",
       "Hunting, fishing, camping and outdoor gear in Stratford, Taranaki. Airguns, ammunition, firearms, apparel, footwear and tackle. Call 06 765 7248."),
 "/online-casinos/": (f"Best Online Casinos NZ [{MONTH_YEAR}] | Real Money Sites",
       f"Compare the best online casinos NZ has for real money play, updated {MONTH_YEAR}. 15 NZ casino sites tested with our own NZD — payouts and bonuses ranked."),
 "/online-pokies/": (f"Online Pokies NZ [{MONTH_YEAR}] | Real Money Pokies",
       f"The best online pokies NZ players can spin, updated {MONTH_YEAR}. Real money pokies sites compared on RTP, free spins and jackpots, plus free pokies explained."),
 "/casino-payout-percentages/": (f"Casino Payout Percentage NZ [{MONTH_YEAR}] | Highest RTP",
       f"What RTP means and how casino payout percentages work, updated {MONTH_YEAR}. The highest RTP casinos NZ players can use, with real figures by game."),
 "/fast-payout-casinos/": (f"Fast Payout Casinos NZ [{MONTH_YEAR}] | Fast Withdrawals",
       f"We timed 168 withdrawals. The fastest paying online casino NZ options as at {MONTH_YEAR}, how long casino withdrawals take by method, and why yours is pending."),
 "/live-casino/": (f"Live Casino NZ [{MONTH_YEAR} Guide] | Best Live Dealers",
       f"The best live casino NZ sites as at {MONTH_YEAR}. Live dealer blackjack, roulette and baccarat from Evolution, with NZD table limits and minimum bets compared."),
 "/crypto-casinos-nz/": (f"Crypto Casinos NZ [{MONTH_YEAR} Guide] | Bitcoin Casinos",
       f"The best crypto casino NZ sites, updated {MONTH_YEAR}. Bitcoin, Ethereum and USDT casinos compared on payout speed and provably fair games, plus NZ crypto tax."),
 "/casino-bonus/": (f"Casino Bonus NZ [{MONTH_YEAR} Guide] | Best Offers",
       f"Every casino bonus NZ players can claim, updated {MONTH_YEAR}. Compared on wagering, max bet and expiry, with $1, $5 and $10 deposit offers and the real turnover."),
 "/no-deposit-bonus/": (f"No Deposit Bonus NZ [{MONTH_YEAR}] | Free Spins Offers",
       f"Every no deposit bonus NZ casinos advertise, checked {MONTH_YEAR}. One free spins no deposit offer is genuinely live — with the wagering and max cashout explained."),
 "/casino-reviews/": (f"Casino Reviews NZ [{MONTH_YEAR}] | 19 Sites Tested",
       f"Hands-on online casino reviews NZ players can trust, updated {MONTH_YEAR}. Real NZD deposits, timed withdrawals, and the 22 operators we refused to list."),
 "/online-betting/": (f"Online Betting NZ [{MONTH_YEAR} Guide] | Betting Sites",
       f"Online betting NZ explained, current to {MONTH_YEAR}: what the 2025 TAB monopoly law changed, which sports betting sites accept Kiwis, NZD deposits and odds."),
 "/licensed-online-casinos/": (f"Licensed Online Casinos NZ [{MONTH_YEAR}] | Is It Legal?",
       f"Are online casinos legal in New Zealand? Updated {MONTH_YEAR}: the DIA 15-licence auction, the 1 December 2026 deadline and which casinos are licensed."),
 "/gambling-winnings-tax-nz/": (f"Gambling Winnings Tax NZ [{MONTH_YEAR} Guide]",
       f"Do you pay tax on gambling winnings in NZ? No, for recreational players — with two exceptions. Professional gambling and crypto, current to {MONTH_YEAR}."),
 "/casino-payment-methods/": (f"Casino Payment Methods NZ [{MONTH_YEAR} Guide]",
       f"Which casino payment methods NZ banks clear, checked {MONTH_YEAR}: POLi, Paysafecard, Neosurf, Skrill, bank transfer, crypto and cards across 41 sites."),
 "/how-we-rate-casinos/": (f"How We Rate Online Casinos [{MONTH_YEAR}] | Methodology",
       f"How to choose an online casino NZ players can trust, and the six weighted criteria behind every score on this site. Methodology current to {MONTH_YEAR}."),
 "/responsible-gambling/": (f"Responsible Gambling NZ [{MONTH_YEAR}] | Free Help",
       f"Free, confidential gambling help in NZ. Gambling Helpline 0800 654 655, deposit limits, self-exclusion, blocking software and bank gambling blocks."),
 "/about/": ("About Magnum Sports | Independent NZ Casino Reviews",
       "Who we are, how we test online casinos with our own NZD, how affiliate commission is handled, and what we will not do. Independent reviews for Kiwis."),
 "/contact/": ("Contact Magnum Sports | NZ Casino & Betting Guide",
       "Contact the Magnum Sports team. Corrections, operator complaints, privacy requests and commercial enquiries, with a two-working-day reply."),
 "/authors/": ("Our Authors | Who Writes Magnum Sports",
       "Meet the three people who write Magnum Sports: backgrounds, areas of responsibility, the pages they write and how to contact them directly."),
 "/terms/": ("Terms and Conditions | Magnum Sports",
       "Terms for using magnumsports.co.nz: age restriction, affiliate disclosure, third-party operators, limitation of liability and governing law."),
 "/privacy/": ("Privacy Policy | Magnum Sports",
       "How Magnum Sports collects, uses and protects personal information under the Privacy Act 2020, and how to access, correct or delete your data."),
 "/cookie-policy/": ("Cookie Policy | Magnum Sports",
       "Which cookies magnumsports.co.nz sets, what each does, which need consent, and how to refuse or delete them in any browser."),
 "/new-casinos-nz/": (f"New Online Casinos NZ [{MONTH_YEAR}] | Newest Sites",
       f"New online casinos NZ players can join, updated {MONTH_YEAR} as licensed operators launch. What to check before joining a new casino site, and which are safe."),
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
<meta name="rating" content="adult">
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
             '<a href="/cookie-policy/">Cookie Policy</a><a href="/authors/">Our Authors</a>')
    o.append('</div></details></div></header>\n')
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
<p>Hunting, fishing, camping and outdoor gear from our Stratford shop, plus independent guides to online betting and casino sites for New Zealanders.</p>
<p><b style="color:#c3cddf">220 Broadway, Stratford<br>Taranaki 4332</b><br><a href="tel:+6467657248">06 765 7248</a></p>
<p><a href="/#shop">Shop by department</a> &middot; <a href="/how-we-rate-casinos/">How we review</a></p>
</div>
{cols}
</div>
<div class="foot-bot">
<p><strong>18+ only. Gambling can be harmful.</strong> Magnum Sports is an independent comparison site. We earn commission when readers open an account through links on this page, which funds our testing and never changes a ranking &mdash; see <a href="/how-we-rate-casinos/">how we review</a> and our <a href="/terms/">terms</a>. Information is provided for general purposes and is not legal or financial advice. Free, confidential help is available from the Gambling Helpline on <a href="tel:0800654655">0800 654 655</a>, 24 hours a day.</p>
<div class="foot-badges">
<span class="badge18" aria-label="Eighteen plus only">18+</span>
<a href="/responsible-gambling/">Responsible Gambling</a>
<a href="https://www.gamblinghelpline.co.nz/" rel="nofollow noopener" target="_blank">Gambling Helpline</a>
<a href="/contact/">Contact</a>
</div>
</div>
<p style="margin-top:22px;font-size:.78rem">&copy; 2026 {esc(NAME)}. All rights reserved. magnumsports.co.nz</p>
</div></footer>
</body>
</html>
'''


def disclosure(extra=""):
    return ('<div class="disc"><p><strong>Advertising disclosure.</strong> Magnum Sports is free to '
            'read because operators pay us a commission when a reader opens an account through one of '
            'our links. It does not cost you anything, it does not change the price of anything, and '
            'it does not buy a position on this page &mdash; scores come from the criteria set out in '
            '<a href="/how-we-rate-casinos/">our review methodology</a>, and sites we cannot recommend are '
            'left off regardless of what they offer to pay. ' + extra + '</p></div>')


def disclosure_section(extra=""):
    """Advertising disclosure as a standalone section, placed at the foot of
    the page (above the footer) rather than above the affiliate table."""
    return ('<section id="disclosure" class="sec sec--haze" style="padding-top:34px;padding-bottom:34px">'
            '<div class="wrap"><div class="prose prose--wide">' + disclosure(extra)
            + '</div></div></section>\n')


def byline(author="angus-mclean", checker="witi-king", updated=None):
    a = AUTHORS[author]
    c = AUTHORS[checker] if checker else None
    fc = (f' &middot; Fact-checked by <a class="by-link" href="/authors/#{checker}"><b>{esc(c["name"])}</b></a>'
          if c else "")
    return f'''<div class="byline">
<a href="/authors/#{author}" aria-label="{esc(a["name"])}, author"><img src="{a["img"]}" srcset="{a["img"]} 1x, {a["img"].replace(".jpg","@2x.jpg")} 2x" alt="{esc(a["name"])}" width="46" height="46" loading="eager" decoding="async"></a>
<div class="byline-txt">
<span>By <a href="/authors/#{author}"><b>{esc(a["name"])}</b></a>, {esc(a["role"])}{fc}</span>
<span class="byline-date">{icon("clock")} Updated {updated or UPDATED_NZ}</span>
</div></div>'''


def authorbox(author="angus-mclean"):
    a = AUTHORS[author]
    return f'''<aside class="authorbox">
<img src="{a["img"]}" srcset="{a["img"]} 1x, {a["img"].replace(".jpg","@2x.jpg")} 2x" alt="{esc(a["name"])}" width="78" height="78" loading="lazy" decoding="async">
<div><h4>{esc(a["name"])}</h4><div class="role">{esc(a["role"])}</div>
<p>{esc(a["bio"])}</p>
<p><a href="/authors/#{author}">Full profile and review history &rarr;</a> &middot; <a href="/how-we-rate-casinos/">How we test</a></p></div></aside>'''


# ------------------------------------------------------------ components ----

def lb_row(o, i, mode="casino", feat=False):
    url = o["casino_url"] if mode == "casino" else o["betting_url"]
    url = url or o["casino_url"] or o["betting_url"]
    bonus = o["casino_bonus"] if mode == "casino" else (o["sports_bonus"] or o["casino_bonus"])
    terms = o["casino_bonus_terms"] if mode == "casino" else (
        f'{o["wagering"]} &middot; min deposit {o["min_deposit"]}')
    terms = terms or f'{o["wagering"]} &middot; min deposit {o["min_deposit"]}'
    flag = (f'<span class="lb-flag">{icon("bolt")}{esc(o["highlights"][0])}</span>'
            if o.get("highlights") else "")
    rel = 'rel="nofollow sponsored noopener" target="_blank"'
    return f'''<li class="lb-row{' lb-row--feat' if feat else ''}">
<a class="lb-cover" href="{esc(url)}" {rel} aria-label="Visit {esc(o["name"])} (opens in a new tab)"></a>
<span class="lb-rank">{i}</span>
<div class="lb-brand"><img class="lb-logo" src="{o["logo"]}" alt="{esc(o["name"])} logo" loading="lazy" decoding="async" width="88" height="46"><span class="lb-name">{esc(o["name"])}<span class="lb-sub">{esc(o["sub"])}</span></span></div>
<div class="lb-score"><span class="lb-score-top">{icon("star")}<b>{o["rating"]}/10</b></span><span class="lb-bar"><span style="width:{o["bar"]}%"></span></span>{flag}</div>
<div class="lb-bonus"><span class="lb-bonus-l">{'Welcome offer' if mode=='casino' else 'Betting offer'}</span><span class="lb-bonus-v">{esc(bonus)}</span></div>
<div class="lb-cta"><a class="btn btn--wide" href="{esc(url)}" {rel}>Get bonus</a><span class="lb-terms">{terms}</span><span class="lb-review"><a href="/casino-reviews/{o["slug"]}/">Read review</a></span></div>
</li>'''


def leaderboard(ops, mode="casino", heading=None, intro=None, hid="toplist"):
    rows = "".join(lb_row(o, i, mode, feat=(i == 1)) for i, o in enumerate(ops, 1))
    head_html = ""
    if heading:
        head_html = f'<div class="sec-head"><h2>{heading}</h2>' + (f'<p>{intro}</p>' if intro else "") + '</div>'
    return f'''<section id="{hid}" class="sec"><div class="wrap">
{head_html}
<div class="lb">
<div class="lb-head" aria-hidden="true"><span>#</span><span>Site</span><span>Our score</span><span>Offer</span><span></span></div>
<ol class="lb-rows">{rows}</ol>
</div>
<p style="font-size:.79rem;color:var(--mute);margin-top:14px">Offers shown are the operator&rsquo;s published welcome promotion at the time of our last check on {UPDATED_NZ}. Terms change without notice &mdash; always read the promotion page before you deposit. 18+ only.</p>
</div></section>
'''


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


def paa_block(items, heading, intro=None, haze=True, hid="people-also-ask"):
    """Real-query section. `items` is [(question, answer_html)].

    Questions come from search autosuggest (Google gl=nz, Bing en-NZ,
    DuckDuckGo nz-en) harvested by _build/harvest_queries.py — they are what
    New Zealanders actually type, not what we guessed they type. Answers lead
    with the direct response in the first sentence, which is the format Google
    extracts for featured snippets and People Also Ask.
    """
    out = []
    for i, (q, a) in enumerate(items, 1):
        out.append(f'<div class="paa-item"><h3><span>{i:02d}</span>{q}</h3>{a}</div>')
    i_html = f'<p>{intro}</p>' if intro else ""
    return (f'<section id="{hid}" class="sec{" sec--haze" if haze else ""}"><div class="wrap">'
            f'<div class="sec-head"><span class="kicker">People also ask</span><h2>{heading}</h2>{i_html}'
            f'<p class="paa-src">{icon("search")} Questions sourced from Google, Bing and DuckDuckGo '
            f'autosuggest for New Zealand &middot; checked {UPDATED_NZ}</p></div>'
            f'<div class="paa">' + "".join(out) + '</div></div></section>\n')


def dept_image(slug):
    """Path to a department photo if one has been added, else None."""
    for ext in ("jpg", "webp", "png"):
        rel = f"images/departments/{slug}.{ext}"
        if os.path.exists(os.path.join(ROOT, rel)):
            return "/" + rel
    return None


def paa_items(path):
    """The (question, answer) pairs harvested for a page, or []."""
    e = PAA.get(path)
    return e[2] if e else []


def paa_for(path, haze=True):
    """Render a page's People Also Ask section, or nothing if it has none."""
    e = PAA.get(path)
    if not e:
        return ""
    heading, intro, items = e
    return paa_block(items, heading, intro, haze=haze)


def picks(items):
    """items: [(category, slug, blurb)]"""
    out = []
    for cat, slug, blurb in items:
        o = BY[slug]
        url = o["casino_url"] or o["betting_url"]
        out.append(f'''<div class="pick"><span class="pick-cat">{esc(cat)}</span>
<div class="pick-brand"><img src="{o["logo"]}" alt="{esc(o["name"])} logo" loading="lazy" decoding="async" width="70" height="38"><b>{esc(o["name"])}</b></div>
<p>{blurb}</p>
<a class="btn btn--sm" href="{esc(url)}" rel="nofollow sponsored noopener" target="_blank">Visit {esc(o["short"])}</a></div>''')
    return '<div class="picks">' + "".join(out) + '</div>'


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


def proscons(pros, cons, ptitle="What we liked", ctitle="What we didn't"):
    p = "".join(f"<li>{x}</li>" for x in pros)
    c = "".join(f"<li>{x}</li>" for x in cons)
    return (f'<div class="pc"><div class="pc-col pc-pro"><h4>{ptitle}</h4><ul>{p}</ul></div>'
            f'<div class="pc-col pc-con"><h4>{ctitle}</h4><ul>{c}</ul></div></div>')


def toc(items):
    li = "".join(f'<li><a href="#{a}">{t}</a></li>' for t, a in items)
    return f'<nav class="toc" aria-label="On this page"><b>On this page</b><ol>{li}</ol></nav>'


def band(title, body, cta_text, cta_href, external=False):
    rel = ' rel="nofollow sponsored noopener" target="_blank"' if external else ""
    return (f'<section class="sec"><div class="wrap"><div class="band"><div class="band-txt">'
            f'<h3>{title}</h3><p>{body}</p></div>'
            f'<a class="btn btn--light" href="{cta_href}"{rel}>{cta_text}</a></div></div></section>\n')


def rg_block():
    return f'''<section class="sec sec--ink"><div class="wrap">
<div class="sec-head"><span class="kicker" style="color:var(--amber)">Play safe</span>
<h2>Gambling should cost you time, not your week&rsquo;s wages</h2>
<p>Every site on this page is built to make money from you over the long run. That is not a scandal, it is arithmetic &mdash; the house edge is published and it does not move. The only thing you control is how much you put through it.</p></div>
<div class="grid grid--4">
<div class="card"><div class="card-ic">{icon("wallet")}</div><h3>Set a deposit limit first</h3><p>Every casino here lets you cap daily, weekly or monthly deposits from the account settings. Do it before your first deposit, not after a bad night.</p></div>
<div class="card"><div class="card-ic">{icon("clock")}</div><h3>Use reality checks</h3><p>A pop-up every 30 or 60 minutes telling you how long you have been playing sounds trivial. In practice it is the single most effective tool these sites offer.</p></div>
<div class="card"><div class="card-ic">{icon("lock")}</div><h3>Self-exclude if you need to</h3><p>Time-outs run from 24 hours to six weeks. Self-exclusion runs six months or longer and cannot be reversed on request. Both are free and take two minutes.</p></div>
<div class="card"><div class="card-ic">{icon("chat")}</div><h3>Free help, 24/7</h3><p>The Gambling Helpline is free and confidential on <a href="tel:0800654655" style="color:var(--amber)">0800 654 655</a>. The Problem Gambling Foundation offers free counselling nationwide.</p></div>
</div>
<p style="margin-top:22px"><a href="/responsible-gambling/" style="color:var(--amber);font-weight:600">Read our full responsible gambling guide &rarr;</a></p>
</div></section>
'''


def org_schema():
    return {
        "@type": "Organization", "@id": f"{SITE}/#organization", "name": NAME, "url": SITE,
        "logo": {"@type": "ImageObject", "url": f"{SITE}/favicon-512x512.png", "width": 512, "height": 512},
        "email": EMAIL, "areaServed": {"@type": "Country", "name": "New Zealand"},
        "knowsLanguage": "en-NZ",
        "description": ("Outdoors retailer in Stratford, Taranaki, and independent New Zealand "
                        "guide to online betting, online casinos and pokies."),
        "telephone": STORE["phone_tel"],
        "publishingPrinciples": f"{SITE}/how-we-rate-casinos/",
        "founder": {"@id": f"{SITE}/#author-angus-mclean"},
    }


def store_schema():
    """SportingGoodsStore entity for the retail business behind this domain."""
    return {
        "@type": ["SportingGoodsStore", "LocalBusiness"],
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
        "parentOrganization": {"@id": f"{SITE}/#organization"},
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Departments",
            "itemListElement": [
                {"@type": "OfferCatalog", "name": d[0],
                 "url": f"{SITE}/#{d[1]}"} for d in DEPARTMENTS
            ],
        },
    }


def site_schema():
    return {"@type": "WebSite", "@id": f"{SITE}/#website", "name": NAME, "url": SITE,
            "publisher": {"@id": f"{SITE}/#organization"}, "inLanguage": "en-NZ"}


def person_schema(slug):
    a = AUTHORS[slug]
    d = {"@type": "Person", "@id": f"{SITE}/#author-{slug}", "name": a["name"],
         "url": f"{SITE}/authors/#{slug}", "jobTitle": a["role"],
         "image": SITE + a["img"],
         "worksFor": {"@id": f"{SITE}/#organization"}, "knowsAbout": a["knows"],
         "description": a["short"]}
    if a.get("location"):
        d["homeLocation"] = {"@type": "Place", "name": a["location"]}
    if a.get("sameAs"):
        d["sameAs"] = a["sameAs"]
    return d


def page_schema(kind, title, desc, path, author="angus-mclean", extra=None):
    """Standard @graph for a content page."""
    g = [org_schema(), site_schema(), person_schema(author)]
    wp = {"@type": ["WebPage", kind] if kind and kind != "WebPage" else "WebPage",
          "@id": f"{SITE}{path}#webpage", "url": SITE + path, "name": title,
          "description": desc, "inLanguage": "en-NZ",
          "isPartOf": {"@id": f"{SITE}/#website"},
          "author": {"@id": f"{SITE}/#author-{author}"},
          "reviewedBy": {"@id": f"{SITE}/#author-witi-king"},
          "publisher": {"@id": f"{SITE}/#organization"},
          "datePublished": PUBLISHED, "dateModified": UPDATED,
          "primaryImageOfPage": {"@type": "ImageObject", "url": f"{SITE}/images/og-magnum.jpg"}}
    g.append(wp)
    if extra:
        g += extra
    return {"@context": "https://schema.org", "@graph": g}


def itemlist_schema(ops, name, path, mode="casino"):
    el = []
    for i, o in enumerate(ops, 1):
        el.append({"@type": "ListItem", "position": i,
                   "item": {"@type": "Organization", "name": o["name"],
                            "url": f"{SITE}/casino-reviews/{o['slug']}/",
                            "logo": SITE + o["logo"]}})
    return {"@type": "ItemList", "@id": f"{SITE}{path}#ranking", "name": name,
            "numberOfItems": len(ops),
            "itemListOrder": "https://schema.org/ItemListUnordered",
            "itemListElement": el}


def write(path, body):
    """path: '/online-pokies/' -> online-pokies/index.html"""
    rel = path.strip("/")
    d = os.path.join(ROOT, rel) if rel else ROOT
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(body)
    return path
