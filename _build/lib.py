#!/usr/bin/env python3
"""Shared templating, schema and components for magnumsports.co.nz."""
import json, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://magnumsports.co.nz"
NAME = "Magnum Sports"
TAG = "NZ Casino & Betting Guide"
EMAIL = "editor@magnumsports.co.nz"
PUBLISHED = "2026-02-02"
UPDATED = "2026-09-14"
UPDATED_NZ = "14/09/2026"

OPS = json.load(open(os.path.join(ROOT, "_build", "operators.json")))
BY = {o["slug"]: o for o in OPS}
CASINOS = sorted([o for o in OPS if o["casino"]], key=lambda o: o["rank"])
SPORTS = sorted([o for o in OPS if o["sports"]], key=lambda o: o.get("sports_rank", 99))

AUTHORS = {
    "tama-whitiora": {
        "name": "Tama Whitiora", "role": "Lead Casino Reviewer",
        "img": "/images/authors/tama-whitiora.jpg",
        "knows": ["online casinos", "online pokies", "casino bonus terms",
                  "withdrawal testing", "New Zealand gambling regulation"],
        "bio": "Tama has reviewed online casinos for New Zealand audiences since 2017, first as a "
               "freelance contributor to trade publications and since 2023 as Magnum Sports' lead "
               "reviewer. He opens and funds every account on this site personally, logs each "
               "withdrawal against a stopwatch, and reads the bonus terms line by line before a "
               "single score is written.",
        "short": "Reviews and scores every casino on this site, and personally funds and times each withdrawal test.",
    },
    "holly-mcgrath": {
        "name": "Holly McGrath", "role": "Payments & Banking Editor",
        "img": "/images/authors/holly-mcgrath.jpg",
        "knows": ["NZD payment methods", "bank transfers", "e-wallets", "cryptocurrency payments",
                  "KYC and verification", "anti-money-laundering rules"],
        "bio": "Holly spent nine years in retail banking operations in Auckland before moving into "
               "gambling media. She covers how money actually moves between a New Zealand bank "
               "account and an offshore casino — which methods clear, which get declined, what "
               "verification you will be asked for and where the hidden conversion spreads sit.",
        "short": "Covers NZD deposits, withdrawals, verification and the conversion costs nobody advertises.",
    },
    "daniel-ashworth": {
        "name": "Daniel Ashworth", "role": "Betting Analyst & Compliance Editor",
        "img": "/images/authors/daniel-ashworth.jpg",
        "knows": ["sports betting", "rugby union betting", "odds comparison", "New Zealand gambling law",
                  "Racing Industry Act 2020", "responsible gambling"],
        "bio": "Daniel tracks New Zealand gambling legislation and prices sports markets for a living. "
               "He fact-checks every legal and regulatory claim published on Magnum Sports against "
               "the primary source — the Act, the DIA notice or the operator's own licence register "
               "entry — and he is the reason several claims you will find on rival sites do not "
               "appear on this one.",
        "short": "Fact-checks every legal and regulatory claim on this site against the primary source.",
    },
}

NAV = [
    ("Home", "/", None),
    ("Online Casinos", "/online-casinos/", [
        ("Online Casinos NZ", "/online-casinos/"),
        ("Online Pokies", "/online-pokies/"),
        ("High Payout Casinos", "/high-payout-casinos/"),
        ("Fast Payout Casinos", "/fast-payout-casinos/"),
        ("Live Dealer Casinos", "/live-casinos/"),
        ("Crypto Casinos", "/best-crypto-casinos/"),
        ("Casino Bonuses", "/online-casinos/bonuses/"),
        ("No Deposit Bonuses", "/no-deposit-casinos/"),
        ("Casino Reviews", "/casino-reviews/"),
    ]),
    ("Betting", "/online-betting/", [
        ("Online Betting NZ", "/online-betting/"),
        ("Best Sports Betting Sites", "/best-sports-betting-sites/"),
    ]),
    ("Guides", None, [
        ("NZ Online Casino Law", "/nz-online-casino-law/"),
        ("Tax on Gambling Winnings", "/gambling-winnings-tax-nz/"),
        ("NZ Payment Methods", "/payment-methods/"),
        ("How We Review", "/how-we-review/"),
        ("Responsible Gambling", "/responsible-gambling/"),
    ]),
    ("About", "/about/", None),
    ("Contact", "/contact/", None),
]

FOOTER = [
    ("Casinos", [("Online Casinos NZ", "/online-casinos/"), ("Online Pokies", "/online-pokies/"),
                 ("High Payout Casinos", "/high-payout-casinos/"), ("Fast Payout Casinos", "/fast-payout-casinos/"),
                 ("Live Dealer Casinos", "/live-casinos/"), ("Crypto Casinos", "/best-crypto-casinos/")]),
    ("Bonuses & Betting", [("Casino Bonuses", "/online-casinos/bonuses/"), ("No Deposit Bonuses", "/no-deposit-casinos/"),
                           ("Online Betting NZ", "/online-betting/"), ("Sports Betting Sites", "/best-sports-betting-sites/"),
                           ("Casino Reviews", "/casino-reviews/")]),
    ("Guides", [("NZ Online Casino Law", "/nz-online-casino-law/"), ("Tax on Winnings", "/gambling-winnings-tax-nz/"),
                ("Payment Methods", "/payment-methods/"), ("How We Review", "/how-we-review/")]),
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
}


# ---------------------------------------------------------------- metas ----
# One place for every title/description. Titles <= 60 chars, descriptions
# <= 158, each targeting a different head-keyword variant so pages do not
# compete with one another in the SERP.
META = {
 "/": ("Best Online Casino Sites NZ 2026 | Top 16 Tested",
       "Compare the best online casino sites NZ players can use in 2026. 41 casinos tested with real NZD, every withdrawal timed. Payouts, bonuses and pokies ranked."),
 "/online-casinos/": ("Online Casinos NZ | Real Money Casino Sites 2026",
       "Every real money online casino NZ players can join, reviewed and ranked. NZD banking, payout times, bonus terms and the 2026 licensing changes explained."),
 "/online-pokies/": ("Online Pokies NZ 2026 | Best Real Money Pokies Sites",
       "The best online pokies NZ sites for real money in 2026. Compare RTP, volatility, studios and free spins, plus how online pokies beat NZ pub machines."),
 "/high-payout-casinos/": ("High Payout Casinos NZ | Highest RTP Sites 2026",
       "The highest payout online casino NZ options for 2026. Real RTP by game, which sites publish their figures, and five changes that lift your actual return."),
 "/fast-payout-casinos/": ("Fast Payout Casinos NZ | Fastest Withdrawals 2026",
       "We timed 168 withdrawals across 41 sites. The fastest payout online casino NZ picks for 2026, with real times by method, weekly caps and what causes delays."),
 "/live-casinos/": ("Live Casinos NZ 2026 | Best Live Dealer Sites",
       "The best live dealer casino NZ sites for 2026. Evolution and Pragmatic Live coverage, NZD table limits, RTP by game and which tables run at 9pm NZT."),
 "/best-crypto-casinos/": ("Best Crypto Casinos NZ 2026 | Bitcoin &amp; USDT Sites",
       "The best crypto casino NZ sites for 2026. Bitcoin, USDT and Litecoin casinos compared on payout speed, provably fair games and the NZ crypto tax rules."),
 "/online-casinos/bonuses/": ("Casino Bonuses NZ 2026 | Best Welcome Offers",
       "Every online casino bonus NZ players can claim, compared on wagering, max bet, game contribution and expiry. Worked examples in NZD, no hype."),
 "/no-deposit-casinos/": ("No Deposit Bonus Casinos NZ 2026 | Verified Offers",
       "We checked every no deposit bonus NZ casinos advertise and found one that is genuinely live. Here it is, with the wagering, the cap and the real value."),
 "/casino-reviews/": ("Casino Reviews NZ | 19 Sites Tested With Our Money",
       "Hands-on online casino reviews NZ players can trust. Real NZD deposits, timed withdrawals, published scores, and the 22 operators we refused to list."),
 "/online-betting/": ("Online Betting NZ 2026 | Best Betting Sites for Kiwis",
       "Online betting NZ explained: what the 2025 TAB monopoly law changed, which betting sites still accept Kiwis, NZD deposits, rugby markets and odds compared."),
 "/best-sports-betting-sites/": ("Best Sports Betting Sites NZ 2026 | Ranked",
       "The best sports betting sites NZ punters can use in 2026, ranked on rugby and NRL market depth, odds margins, in-play quality, NZD banking and free bets."),
 "/nz-online-casino-law/": ("NZ Online Casino Law | Is Online Gambling Legal?",
       "Is online gambling legal in New Zealand? The Gambling Act 2003, the 15-licence auction and the 1 December 2026 deadline, explained in plain English."),
 "/gambling-winnings-tax-nz/": ("Gambling Winnings Tax NZ | Do You Pay Tax on Wins?",
       "Do you pay tax on gambling winnings in NZ? No, for recreational players — with two exceptions. Professional gambling and crypto, with worked examples."),
 "/payment-methods/": ("NZ Casino Payment Methods | Deposits &amp; Withdrawals",
       "Which casino payment methods NZ banks actually clear. Bank transfer, crypto, cards, Skrill, Neosurf and POLi tested across 41 sites and 5 NZ banks."),
 "/how-we-review/": ("How We Review Online Casinos | Our Methodology",
       "Our review methodology: six weighted criteria, 41 operators tested with our own money, 168 timed withdrawals, and exactly how affiliate commission is handled."),
 "/responsible-gambling/": ("Responsible Gambling NZ | Free Help and Support",
       "Free, confidential gambling help in NZ. Gambling Helpline 0800 654 655, deposit limits, self-exclusion, blocking software and bank gambling blocks."),
 "/about/": ("About Magnum Sports | Independent NZ Casino Reviews",
       "Who we are, how we test online casinos with our own NZD, how affiliate commission is handled, and what we will not do. Independent reviews for Kiwis."),
 "/contact/": ("Contact Magnum Sports | NZ Casino &amp; Betting Guide",
       "Contact the Magnum Sports team. Corrections, operator complaints, privacy requests and commercial enquiries, with a two-working-day reply."),
 "/authors/": ("Our Authors | Who Writes Magnum Sports",
       "Meet the three people who write Magnum Sports: backgrounds, areas of responsibility, the pages they write and how to contact them directly."),
 "/terms/": ("Terms and Conditions | Magnum Sports",
       "Terms for using magnumsports.co.nz: age restriction, affiliate disclosure, third-party operators, limitation of liability and governing law."),
 "/privacy/": ("Privacy Policy | Magnum Sports",
       "How Magnum Sports collects, uses and protects personal information under the Privacy Act 2020, and how to access, correct or delete your data."),
 "/cookie-policy/": ("Cookie Policy | Magnum Sports",
       "Which cookies magnumsports.co.nz sets, what each does, which need consent, and how to refuse or delete them in any browser."),
}


def clamp(text, n):
    """Trim to n characters on a word boundary, entity-aware."""
    import html as _h
    plain = _h.unescape(text)
    if len(plain) <= n:
        return text
    cut = plain[:n].rsplit(" ", 1)[0].rstrip(" ,;:-\u2014")
    return _h.escape(cut, quote=True).replace("&#x27;", "'")


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
    title, desc = clamp(title, 60), clamp(desc, 158)
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
<meta name="theme-color" content="#0a1020">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Inter:wght@400;500;600;700&family=Roboto+Mono:wght@400;500&display=swap" rel="stylesheet">
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
         '<rect width="100" height="100" rx="22" fill="#121c33"/>',
         '<path d="M20.5 73.5V26.5L50 58.5L79.5 26.5V73.5" fill="none" stroke="#e11d2e" stroke-width="11.5" stroke-linecap="round" stroke-linejoin="round"/>',
         '<rect x="20.5" y="79.5" width="59" height="5.5" rx="2.75" fill="#ffb703"/></svg>',
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
<svg class="brand-mark" width="32" height="32" viewBox="0 0 100 100" aria-hidden="true"><rect width="100" height="100" rx="22" fill="#121c33"/><path d="M20.5 73.5V26.5L50 58.5L79.5 26.5V73.5" fill="none" stroke="#e11d2e" stroke-width="11.5" stroke-linecap="round" stroke-linejoin="round"/><rect x="20.5" y="79.5" width="59" height="5.5" rx="2.75" fill="#ffb703"/></svg>
<span class="brand-txt"><span class="brand-word">MAGNUM<i>.</i></span><span class="brand-tag">{esc(TAG)}</span></span></a>
<p>Independent reviews of online casinos and betting sites for New Zealanders. We open the accounts, deposit our own New Zealand dollars and time every withdrawal ourselves.</p>
<p><a href="/how-we-review/">How we review</a> &middot; <a href="/authors/">Meet the team</a></p>
</div>
{cols}
</div>
<div class="foot-bot">
<p><strong>18+ only. Gambling can be harmful.</strong> Magnum Sports is an independent comparison site. We earn commission when readers open an account through links on this page, which funds our testing and never changes a ranking &mdash; see <a href="/how-we-review/">how we review</a> and our <a href="/terms/">terms</a>. Information is provided for general purposes and is not legal or financial advice. Free, confidential help is available from the Gambling Helpline on <a href="tel:0800654655">0800 654 655</a>, 24 hours a day.</p>
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
            '<a href="/how-we-review/">our review methodology</a>, and sites we cannot recommend are '
            'left off regardless of what they offer to pay. ' + extra + '</p></div>')


def byline(author="tama-whitiora", checker="daniel-ashworth", updated=None):
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


def authorbox(author="tama-whitiora"):
    a = AUTHORS[author]
    return f'''<aside class="authorbox">
<img src="{a["img"]}" srcset="{a["img"]} 1x, {a["img"].replace(".jpg","@2x.jpg")} 2x" alt="{esc(a["name"])}" width="78" height="78" loading="lazy" decoding="async">
<div><h4>{esc(a["name"])}</h4><div class="role">{esc(a["role"])}</div>
<p>{esc(a["bio"])}</p>
<p><a href="/authors/#{author}">Full profile and review history &rarr;</a> &middot; <a href="/how-we-review/">How we test</a></p></div></aside>'''


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
        "description": "Independent New Zealand comparison site for online casinos, online pokies and sports betting.",
        "publishingPrinciples": f"{SITE}/how-we-review/",
        "founder": {"@id": f"{SITE}/#author-tama-whitiora"},
    }


def site_schema():
    return {"@type": "WebSite", "@id": f"{SITE}/#website", "name": NAME, "url": SITE,
            "publisher": {"@id": f"{SITE}/#organization"}, "inLanguage": "en-NZ"}


def person_schema(slug):
    a = AUTHORS[slug]
    return {"@type": "Person", "@id": f"{SITE}/#author-{slug}", "name": a["name"],
            "url": f"{SITE}/authors/#{slug}", "jobTitle": a["role"],
            "image": SITE + a["img"],
            "worksFor": {"@id": f"{SITE}/#organization"}, "knowsAbout": a["knows"],
            "description": a["short"]}


def page_schema(kind, title, desc, path, author="tama-whitiora", extra=None):
    """Standard @graph for a content page."""
    g = [org_schema(), site_schema(), person_schema(author)]
    wp = {"@type": ["WebPage", kind] if kind and kind != "WebPage" else "WebPage",
          "@id": f"{SITE}{path}#webpage", "url": SITE + path, "name": title,
          "description": desc, "inLanguage": "en-NZ",
          "isPartOf": {"@id": f"{SITE}/#website"},
          "author": {"@id": f"{SITE}/#author-{author}"},
          "reviewedBy": {"@id": f"{SITE}/#author-daniel-ashworth"},
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
            "itemListOrder": "https://schema.org/ItemListOrderDescending",
            "itemListElement": el}


def write(path, body):
    """path: '/online-pokies/' -> online-pokies/index.html"""
    rel = path.strip("/")
    d = os.path.join(ROOT, rel) if rel else ROOT
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(body)
    return path
