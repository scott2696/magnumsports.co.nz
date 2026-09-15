# -*- coding: utf-8 -*-
"""Homepage — Magnum Sports, the outdoors store in Stratford, Taranaki.
Outdoors first; sports betting second; online casinos signposted."""
from lib import *

TITLE = "Magnum Sports | Outdoors Store, Stratford Taranaki"
DESC = ("Hunting, fishing, camping and outdoor gear in Stratford, Taranaki. Airguns, "
        "ammunition, firearms, apparel, footwear and tackle. Call 06 765 7248.")
PATH = "/"

FAQ = [
 ("Where is Magnum Sports?",
  f"<p>We are at <strong>{STORE['street']}, {STORE['suburb']}</strong>, {STORE['region']} "
  f"{STORE['postcode']} &mdash; on the main road through Stratford, so you will not miss us. "
  f"Phone <a href='tel:{STORE['phone_tel']}'>{STORE['phone_display']}</a>. Stratford sits "
  "roughly 40 minutes south of New Plymouth and an hour north of H&#257;wera, which makes us the "
  "practical stop for anyone heading to the Taranaki back country, the Whanganui headwaters or "
  "the coast.</p>"),
 ("What does Magnum Sports sell?",
  "<p>Hunting, fishing, camping and general outdoor gear, across "
  f"<strong>{len(DEPARTMENTS)} departments</strong> and roughly {STORE['products']} lines. "
  "Airguns, ammunition, firearms and accessories, reloading supplies, fishing tackle, apparel, "
  "footwear, bags, hunting accessories, outdoor leisure and sporting goods, plus a clearance "
  "rack that changes constantly. <a href='/#shop'>Browse the departments</a> or call the shop "
  "and ask &mdash; there is more on the floor than any website shows.</p>"),
 ("Do I need a firearms licence to buy from you?",
  "<p><strong>Yes, for firearms and ammunition.</strong> New Zealand law requires a valid "
  "firearms licence, and for some items an endorsement and a permit to procure. All firearm and "
  "ammunition sales are completed in store with the paperwork done properly &mdash; we do not "
  "sell them online, and we do not ship them. Airgun, fishing, camping, apparel and general "
  "sporting goods have no such restriction. If you are unsure what applies to you, "
  f"<a href='tel:{STORE['phone_tel']}'>call us</a> before you drive over.</p>"),
 ("Can I buy online?",
  "<p>Not at the moment. Our online shop is being rebuilt, so for now the fastest route is to "
  f"<a href='tel:{STORE['phone_tel']}'>phone the shop on {STORE['phone_display']}</a> or "
  "<a href='/contact/'>send us a message</a>. We can check stock, put an item aside, and answer "
  "the question you actually have rather than the one a product page anticipated.</p>"),
 ("Do you do mail order within New Zealand?",
  "<p>For most non-restricted gear, yes &mdash; give us a call and we will sort freight. "
  "Firearms and ammunition are the exception and must be handled in store under the Arms Act. "
  "Bulky items such as tents and chilly bins are usually cheaper to collect than to freight, so "
  "ask us either way.</p>"),
 ("Why is there betting and casino content on an outdoors website?",
  "<p>Fair question. Magnum Sports has always been a sports shop, and alongside the gear side of "
  "the business we publish independent guides to <a href='/online-betting/'>online betting</a> "
  "and <a href='/online-casinos/'>online casino sites</a> for New Zealanders. They are written "
  "by a named team, funded by affiliate commission which we disclose on every page, and they are "
  "kept entirely separate from the shop. If you are here for a rod or a pair of boots, the "
  "gambling pages will not follow you around. If you are here for the guides, they are "
  "<a href='/how-we-review/'>tested properly</a>. Strictly 18+.</p>"),
]


def build():
    top_books = SPORTS[:5]
    schema = page_schema(
        "WebPage", TITLE, DESC, PATH,
        extra=[store_schema(),
               crumb_schema([("Home", "/")]),
               faq_schema(FAQ, f"{SITE}/#faq")])
    o = [head(TITLE, DESC, PATH, schema)]

    # ------------------------------------------------------------ hero
    o.append(f'''<section class="hero"><div class="wrap">
<span class="eyebrow">{icon("flag")} {esc(STORE["suburb"])}, {esc(STORE["region"])} &middot; Est. as your local outdoors shop</span>
<h1>{esc(STORE["name"])}: Outdoors Store, {esc(STORE["suburb"])}</h1>
<p class="lede"><strong>{esc(STORE["tagline"])}</strong> {esc(STORE["blurb"])} Come in off Broadway, tell us where you are going and what you are after, and we will sort you out.</p>
<div class="hero-stats">
<div class="hero-stat"><b>{STORE["products"]}+</b><span>Lines in store</span></div>
<div class="hero-stat"><b>{len(DEPARTMENTS)}</b><span>Departments</span></div>
<div class="hero-stat"><b>{esc(STORE["street"])}</b><span>{esc(STORE["suburb"])}, {esc(STORE["region"])}</span></div>
<div class="hero-stat"><b><a href="tel:{STORE["phone_tel"]}" style="color:#fff">{esc(STORE["phone_display"])}</a></b><span>Call the shop</span></div>
</div>
</div></section>
''')

    # ------------------------------------------------------- departments
    dept_cards = []
    for name, slug, ic, blurb in DEPARTMENTS:
        dept_cards.append(
            f'<div id="{slug}" class="card card--link" style="scroll-margin-top:90px">'
            f'<div class="card-ic">{icon(ic)}</div><h3>{esc(name)}</h3><p>{blurb}</p></div>')
    o.append(f'''<section id="shop" class="sec sec--haze"><div class="wrap">
<div class="sec-head"><span class="kicker">The shop</span><h2>Shop by department</h2>
<p>Twelve departments and roughly {STORE["products"]} lines on the floor. Stock moves, so if you want something specific put a call through before you make the trip &mdash; we will check the shelf and put it aside.</p></div>
<div class="grid grid--3">{"".join(dept_cards)}</div>
<div class="note note--amber" style="margin-top:26px"><b>Firearms, ammunition and reloading</b>
<p>These are sold <strong>in store only</strong>, to holders of a valid New Zealand firearms licence, with the required endorsement or permit to procure where the law calls for one. We do not sell or ship them online and we complete the paperwork properly, every time. Everything else on this page &mdash; airguns, fishing, camping, apparel, footwear and sporting goods &mdash; is unrestricted. Not sure which applies to you? <a href="tel:{STORE["phone_tel"]}">Give us a ring on {esc(STORE["phone_display"])}</a> before you drive over.</p></div>
</div></section>
''')

    # ---------------------------------------------------------- featured
    feat = []
    for pname, price, dept, blurb in FEATURED:
        feat.append(f'''<div class="pick"><span class="pick-cat">{esc(dept)}</span>
<div class="pick-brand"><b>{esc(pname)}</b></div>
<p>{blurb}</p>
<div style="font-family:var(--disp);font-size:1.5rem;color:var(--red);font-weight:800">NZ${esc(price)}</div>
<a class="btn btn--sm btn--ghost" href="tel:{STORE["phone_tel"]}">Check stock &mdash; {esc(STORE["phone_display"])}</a></div>''')
    o.append(f'''<section class="sec"><div class="wrap">
<div class="sec-head"><span class="kicker">On the floor</span><h2>A few things people keep coming back for</h2>
<p>A small sample rather than the catalogue. Prices are current in store; ring to confirm size and colour before you travel.</p></div>
<div class="picks">{"".join(feat)}</div>
</div></section>
''')

    # ------------------------------------------------------------- visit
    o.append(f'''<section id="visit" class="sec sec--haze"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">Find us</span>
<h2>Visit the store</h2>
{keyfacts([("Address", f'{esc(STORE["street"])}<br>{esc(STORE["suburb"])}'),
           ("Region", f'{esc(STORE["region"])} {esc(STORE["postcode"])}'),
           ("Phone", f'<a href="tel:{STORE["phone_tel"]}">{esc(STORE["phone_display"])}</a>'),
           ("Departments", str(len(DEPARTMENTS))),
           ("Lines in store", f'{STORE["products"]}+'),
           ("Online shop", "Being rebuilt")])}
<p>We are on <strong>Broadway</strong>, the main road through Stratford, which puts us within easy reach of most of Taranaki &mdash; about forty minutes south of New Plymouth, an hour north of H&#257;wera, and directly on the route for anyone heading into the ranges or over to the Whanganui side.</p>
<p>What you get by coming in rather than ordering from a screen is the part a website cannot do: someone who has fished the local rivers, knows which boot survives a Taranaki winter, and will tell you when the cheaper option is the right one. That has always been the point of the shop.</p>
<p>The online store is currently being rebuilt. Until it is back, the quickest way to check stock, hold an item or ask a question is to <a href="tel:{STORE["phone_tel"]}">phone {esc(STORE["phone_display"])}</a> or <a href="/contact/">send us a message</a>.</p>
<div class="band" style="margin-top:28px"><div class="band-txt">
<h3>Ring the shop</h3><p>Stock check, advice, or put something aside &mdash; {esc(STORE["phone_display"])}. We would rather talk it through than have you drive over for nothing.</p></div>
<a class="btn btn--light" href="tel:{STORE["phone_tel"]}">{esc(STORE["phone_display"])}</a></div>
</div></div></section>
''')

    # --------------------------------------------------- sports betting
    rows = "".join(lb_row(b, i, "sports", feat=(i == 1)) for i, b in enumerate(top_books, 1))
    o.append(f'''<section id="betting" class="sec"><div class="wrap">
<div class="sec-head"><span class="kicker">The other side of the shop</span>
<h2>Sports betting in New Zealand</h2>
<p>Alongside the gear, we publish independent guides to online betting for Kiwi punters &mdash; written by a named team, tested with real money, and funded by affiliate commission that we disclose rather than hide. Rugby, league, cricket, netball and racing, priced and compared properly.</p></div>
{disclosure()}
<div class="note"><b>Read the law before you open an account</b>
<p>New Zealand&rsquo;s betting rules changed on <strong>28 June 2025</strong>. The Racing Industry Amendment Act extended TAB NZ&rsquo;s monopoly to online racing and sports betting, so only TAB NZ and its partner may lawfully offer or promote betting to a person in New Zealand. The Act expressly provides that <strong>an individual may not be convicted for placing a bet</strong> with an offshore operator &mdash; the restriction sits on the supply side. What it does mean is that an offshore book is not accountable to any New Zealand regulator. Our <a href="/online-betting/">online betting guide</a> sets the whole position out before it lists anything.</p></div>
<div class="lb" style="margin-top:22px">
<div class="lb-head" aria-hidden="true"><span>#</span><span>Site</span><span>Our score</span><span>Offer</span><span></span></div>
<ol class="lb-rows">{rows}</ol>
</div>
<p style="font-size:.79rem;color:var(--mute);margin-top:14px">Offers as published at our last check on {UPDATED_NZ}. Terms change without notice. 18+ only.</p>
<div class="grid grid--3" style="margin-top:30px">
<div class="card card--link"><div class="card-ic">{icon("scale")}</div><h3>Online Betting NZ</h3><p>The full legal position, which books still accept New Zealanders, NZD banking, odds margins and free bet terms compared.</p><p><a href="/online-betting/">Read the guide &rarr;</a></p></div>
<div class="card card--link"><div class="card-ic">{icon("ball")}</div><h3>Best Sports Betting Sites</h3><p>All twelve books ranked on rugby union and NRL market depth, the margin you pay on every bet, in-play reliability and how fast the money comes back.</p><p><a href="/online-betting/#sites">Compare bookmakers &rarr;</a></p></div>
<div class="card card--link"><div class="card-ic">{icon("coin")}</div><h3>Tax on Winnings</h3><p>Recreational betting winnings are not taxable in New Zealand. Here are the two exceptions that catch people out, with worked examples.</p><p><a href="/gambling-winnings-tax-nz/">Read the tax guide &rarr;</a></p></div>
</div>
</div></section>
''')

    # --------------------------------------------------------- casinos
    o.append(f'''<section class="sec sec--haze"><div class="wrap">
<div class="sec-head"><span class="kicker">Also from our team</span><h2>Online casino guides</h2>
<p>We opened and funded accounts at 41 online casinos, deposited our own New Zealand dollars and timed every withdrawal. The full rankings, the payout data and the 2026 licensing changes live on our casino pages.</p></div>
{cards([
 ("star","Best online casino sites NZ","Sixteen tested sites ranked on payout speed, NZD banking, pokies range and bonus terms a Kiwi can actually clear.","/online-casinos/","See the rankings"),
 ("dice","Online pokies NZ","Which studios matter, what RTP and volatility really mean, and how online pokies compare to New Zealand pub machines.","/online-pokies/","Best pokies sites"),
 ("bolt","Fast payout casinos","168 withdrawals timed with a stopwatch. Real times by method, weekly caps, and the two habits that halve the wait.","/fast-payout-casinos/","Fastest payouts"),
 ("scale","NZ online casino law","The Gambling Act 2003, the 15-licence auction and the 1 December 2026 deadline, checked against the primary sources.","/nz-online-casino-law/","Read the law"),
])}
</div></section>
''')

    o.append(rg_block())
    o.append(faq_block(FAQ, "Magnum Sports: common questions"))

    o.append(f'''<section class="sec"><div class="wrap"><div class="prose prose--wide">
<h2>About Magnum Sports</h2>
<p>Magnum Sports is an outdoors and sporting goods store at {esc(STORE["street"])}, {esc(STORE["suburb"])}, in {esc(STORE["region"])}. Hunting, fishing, camping, clothing and more &mdash; the gear Taranaki people actually use, sold by people who use it.</p>
<p>The same business publishes the independent betting and casino guides on this site. Those pages are written by a <a href="/authors/">named team</a>, follow a <a href="/how-we-review/">published review methodology</a>, and carry an advertising disclosure wherever they contain a commercial link. They are strictly for readers aged 18 and over.</p>
<p><a href="/about/">More about us</a> &middot; <a href="/contact/">Contact us</a> &middot; <a href="tel:{STORE["phone_tel"]}">{esc(STORE["phone_display"])}</a></p>
</div></div></section>
''')

    o.append(footer())
    return write(PATH, "".join(o))
