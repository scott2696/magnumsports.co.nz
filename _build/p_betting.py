# -*- coding: utf-8 -*-
"""/online-betting/ — the single betting page.

Merged from the former /online-betting/ and /best-sports-betting-sites/, which
covered the same ground. This URL survives: it carried the unique legal
explainer and the higher-volume head terms ("online betting NZ" + "betting
sites NZ" vs "best sports betting sites NZ").
"""
from lib import *

TITLE = "Online Betting NZ | Best Sports Betting Sites 2026"
DESC = ("Online betting NZ explained: what the 2025 TAB monopoly law changed, which sports "
        "betting sites still accept Kiwis, NZD deposits, rugby markets, odds and free bets.")
PATH = "/online-betting/"

# Sports coverage, live betting and cash-out, per book.
FEATURES = {
 "rooster-bet":       ("10+ incl. both rugby codes", "<span class='t-yes'>Yes + streaming</span>", "<span class='t-yes'>Yes</span>"),
 "gunsbet":           ("8, football-led",            "<span class='t-yes'>Yes</span>",            "<span class='t-yes'>Yes</span>"),
 "betandplay":        ("8 incl. both rugby codes",   "<span class='t-yes'><b>Best in class</b></span>", "<span class='t-no'>Partial</span>"),
 "ivibet-sportsbook": ("10 incl. netball",           "<span class='t-yes'>Yes</span>",            "<span class='t-yes'>Yes</span>"),
 "kingdom":           ("Full international book",    "<span class='t-yes'>Yes</span>",            "<span class='t-yes'>Yes</span>"),
 "fortune-play":      ("Full international book",    "<span class='t-yes'>Yes</span>",            "<span class='t-yes'>Yes</span>"),
 "smash":             ("Full international book",    "<span class='t-yes'>Yes</span>",            "<span class='t-yes'>Yes</span>"),
 "rivo":              ("Full international book",    "<span class='t-yes'>Yes</span>",            "<span class='t-yes'>Yes</span>"),
 "madcasino":         ("Full international book",    "<span class='t-yes'>Yes</span>",            "<span class='t-yes'>Yes</span>"),
 "lucky-vibe":        ("Full international book",    "<span class='t-yes'>Yes</span>",            "<span class='t-yes'>Yes</span>"),
 "spino":             ("Crypto-first book",          "<span class='t-yes'>Yes</span>",            "<span class='t-no'>Partial</span>"),
 "roby-casino":       ("Full international book",    "<span class='t-yes'>Yes</span>",            "<span class='t-yes'>Yes</span>"),
}

TURNOVER = {
 "rooster-bet": "6x free bet", "gunsbet": "40x", "betandplay": "<b>5x @ 1.80+</b>",
 "ivibet-sportsbook": "5x @ 2.00+", "kingdom": "30x", "smash": "<b>15x</b>",
 "fortune-play": "40x", "rivo": "35x", "madcasino": "40x", "lucky-vibe": "40x",
 "spino": "<b>0x</b> crypto offer", "roby-casino": "45x",
}

FAQ = [
 ("What is the best sports betting site in NZ?",
  "<p>For overall market depth and rugby coverage, <a href='/casino-reviews/rooster-bet/'>Rooster Bet</a> was the "
  "strongest offshore book we tested, scoring 9.0. For in-play betting, "
  "<a href='/casino-reviews/betandplay/'>Bet&amp;Play</a> is clearly ahead, and it also has the fairest free "
  "bet terms here. For the biggest welcome offer, <a href='/casino-reviews/gunsbet/'>Gunsbet</a>. And for New Zealand "
  "thoroughbred and harness racing, TAB NZ is both the authorised operator and, on the merits, the better "
  "product because the pools are domestic. Read the legal section above before opening any offshore account.</p>"),
 ("Is online betting legal in New Zealand?",
  "<p>For you as a punter, yes &mdash; and this is explicitly protected. The "
  "<strong>Racing Industry Amendment Act 2025</strong> makes it unlawful for anyone other than TAB NZ and its "
  "partner to <em>offer or promote</em> racing and sports betting to a person in New Zealand, but the Act "
  "expressly provides that an individual may not be convicted of an offence for placing a bet with an offshore "
  "betting operator. The prohibition sits on the supply side. Placing the bet is not an offence; supplying the "
  "bet to a New Zealander without authorisation is.</p>"),
 ("What changed on 28 June 2025?",
  "<p>TAB NZ&rsquo;s land-based monopoly on racing and sports betting was extended to cover online betting as "
  "well. Before that date, offshore bookmakers operated in a grey zone and took an estimated "
  "<strong>NZ$180&ndash;200 million a year</strong> in New Zealand turnover. After it, only TAB NZ and its "
  "partner operator may lawfully offer or advertise racing and sports betting to people in New Zealand. Several "
  "major European-licensed bookmakers withdrew from the New Zealand market over the following months rather than "
  "operate against the Act.</p>"),
 ("Who can legally take my sports bet in New Zealand?",
  "<p><strong>TAB NZ</strong> is the sole authorised domestic operator, operating in commercial partnership with "
  "Entain. Betcha operates under the same authorised framework. Every other betting site you can reach from a New "
  "Zealand IP address is offshore and is not authorised to offer or promote betting here, whatever its own "
  "licence says. That does not make you an offender for using one, but it does mean you have no New Zealand "
  "regulator to complain to if something goes wrong.</p>"),
 ("What are the practical risks of using an offshore sportsbook from NZ?",
  "<p>Three that matter. <strong>No local recourse:</strong> the Department of Internal Affairs cannot help you "
  "recover a withheld balance from an operator that is not authorised here, so your only avenue is the operator&rsquo;s "
  "own licensing body, which may be Curaçao or Anjouan. <strong>Payment friction:</strong> New Zealand banks "
  "increasingly decline transactions to offshore gambling merchants, and a declined withdrawal is a genuine "
  "problem. <strong>Market exit:</strong> operators leaving New Zealand have historically given short notice, and "
  "a balance you cannot withdraw in time is a balance you lose. Keep balances small and withdraw regularly.</p>"),
 ("Which betting site has the deepest rugby markets?",
  "<p><a href='/casino-reviews/rooster-bet/'>Rooster Bet</a>, by a clear margin among offshore books. It was the "
  "only one that consistently priced NPC matches alongside Super Rugby Pacific and the Rugby Championship, and "
  "the only one offering handicaps, first try-scorer and same-game multis across the full New Zealand domestic "
  "calendar rather than tests alone.</p>"),
 ("Can I bet on the All Blacks from New Zealand?",
  "<p>Yes. All Blacks tests are covered by TAB NZ and by every offshore book that accepts New Zealand "
  "registrations. Placing the bet is not an offence for you. Prices on headline tests are competitive across the "
  "board because liquidity is high; the difference between books shows up on the derivative markets &mdash; "
  "handicaps, margins, try-scorers &mdash; rather than the head-to-head.</p>"),
 ("Can I bet in New Zealand dollars?",
  "<p>At TAB NZ, always. At offshore books, sometimes. <a href='/casino-reviews/rooster-bet/'>Rooster Bet</a> and "
  "<a href='/casino-reviews/betandplay/'>Bet&amp;Play</a> both hold NZD balances. "
  "<a href='/casino-reviews/gunsbet/'>Gunsbet</a> is euro-only and "
  "<a href='/casino-reviews/ivibet-sportsbook/'>Ivibet Sportsbook</a> settles in other currencies, which costs "
  "a New Zealander roughly 2&ndash;3% on the way in and again on the way out. On a NZ$1,000 turnover that "
  "spread is larger than the margin difference between most books.</p>"),
 ("What is the fastest-paying betting site for Kiwis?",
  "<p><a href='/casino-reviews/rooster-bet/'>Rooster Bet</a> at two to six hours on crypto, with "
  "<a href='/casino-reviews/betandplay/'>Bet&amp;Play</a> close behind at two to eight. "
  "<a href='/casino-reviews/gunsbet/'>Gunsbet</a> is the slowest of the four because it has no crypto rail at "
  "all &mdash; e-wallet only, at 12 to 24 hours. NZD bank withdrawals take one to three business days "
  "everywhere. Unverified accounts are the main cause of delay, not the payment method &mdash; upload your ID "
  "on the day you register.</p>"),
 ("Do I pay tax on betting winnings in New Zealand?",
  "<p>No, not on recreational betting. Inland Revenue does not treat gambling winnings as assessable income, so a "
  "winning multi on the All Blacks is not declarable. The exceptions are the same as for casino play: professional "
  "gambling carried on as a business, and cryptocurrency held as property where its NZD value rises before you "
  "convert. Our <a href='/gambling-winnings-tax-nz/'>tax guide</a> covers both.</p>"),
 ("What sports do Kiwi punters actually bet on?",
  "<p>By turnover, the order is roughly: <strong>rugby union</strong> (Super Rugby Pacific, the Rugby "
  "Championship, All Blacks tests), <strong>rugby league</strong> (NRL, with the Warriors driving a "
  "disproportionate share), <strong>basketball</strong> (the NBA is the single largest offshore category), "
  "<strong>football</strong> (Premier League and A-League), <strong>cricket</strong> (Black Caps limited-overs "
  "and the IPL), then <strong>netball</strong>, <strong>golf</strong>, <strong>tennis</strong> and increasingly "
  "<strong>esports</strong>. Domestic thoroughbred and harness racing remain enormous at TAB NZ specifically.</p>"),
 ("Which betting site has the best odds for New Zealanders?",
  "<p>No single book leads on every market, which is why serious punters hold two or three accounts and compare "
  "before each bet. As a general pattern: TAB NZ is strongest on New Zealand thoroughbred and harness racing "
  "because its pools are domestic; offshore books tend to price international football, NBA and tennis more "
  "sharply because their liquidity is deeper. On rugby union, the gap is narrower than most punters assume. "
  "Always compare the actual price rather than the brand.</p>"),
 ("What is an acceptable free bet condition?",
  "<p><strong>5x turnover at odds of 1.80 or better</strong> is fair &mdash; that is what "
  "<a href='/casino-reviews/betandplay/'>Bet&amp;Play</a> asks. Anything above 8x, or a minimum odds requirement "
  "above 2.50, tips the offer toward the book. Watch three clauses: whether the stake is returned with winnings "
  "(usually it is not), whether cashed-out bets count toward turnover (usually they do not), and the expiry "
  "window, which on free bets is often as short as seven days. Treat any book advertising a &lsquo;no "
  "wagering&rsquo; free bet with scepticism and read the maximum-conversion clause before accepting it.</p>"),
 ("Can I use the TAB and an offshore book at the same time?",
  "<p>Nothing stops you, and many Kiwi punters do &mdash; TAB NZ for domestic racing pools and offshore books for "
  "international sport and in-play markets. Be aware that the two have different withdrawal mechanics, different "
  "verification standards and very different dispute paths. If you are going to hold both, keep the offshore "
  "balance small and treat it as a working float rather than a savings account.</p>"),
]


def build():
    ops = SPORTS
    cr = [("Home", "/"), ("Online Betting NZ", PATH)]
    schema = page_schema(
        "CollectionPage", TITLE, DESC, PATH, author="daniel-ashworth",
        extra=[person_schema("tama-whitiora"),
               crumb_schema(cr),
               itemlist_schema(ops, "Best sports betting sites NZ 2026", PATH, "sports"),
               faq_schema(FAQ + paa_items(PATH), f"{SITE}{PATH}#faq")])
    o = [head(TITLE, DESC, PATH, schema),
         crumbs([("Home", "/"), ("Online Betting NZ", None)])]

    o.append(f'''<section class="hero"><div class="wrap">
<span class="eyebrow">{icon("scale")} Law current to {UPDATED_NZ} &middot; 4 books listed</span>
<h1>Online Betting NZ: Best Sports Betting Sites [{MONTH_YEAR}]</h1>
{byline("daniel-ashworth", "tama-whitiora")}
<p class="lede">New Zealand&rsquo;s online betting rules changed fundamentally in June 2025 and most comparison sites have not caught up. This page explains exactly what the law now says, what it means for you rather than for operators, and ranks every sports betting site that still accepts New Zealand punters &mdash; with the risks stated plainly rather than buried.</p>
<div class="hero-stats">
<div class="hero-stat"><b>28 Jun 2025</b><span>Law in force</span></div>
<div class="hero-stat"><b>TAB NZ</b><span>Sole authorised operator</span></div>
<div class="hero-stat"><b>Not an offence</b><span>For the punter</span></div>
<div class="hero-stat"><b>NZ$0</b><span>Tax on winnings</span></div>
</div>
</div></section>
''')


    o.append(leaderboard(
        ops, "sports", hid="sites",
        heading="Best sports betting sites for New Zealand punters",
        intro="These four books currently accept New Zealand registrations and run a sportsbook as their "
              "own product rather than as a tab on a casino. Each score comes from our own testing of market "
              "depth, price, in-play quality, banking and withdrawal speed. None of them except TAB NZ is "
              "authorised to offer betting here &mdash; read the legal position below before you open an account."))

    o.append('''<section class="sec" style="padding-top:0"><div class="wrap">
<div class="note note--amber" style="margin-top:0"><b>Read this before you open an account</b>
<p>New Zealand&rsquo;s betting rules changed on <strong>28 June 2025</strong>. Only TAB NZ and its partner may lawfully offer or promote racing and sports betting to a person in New Zealand, so none of the books above is authorised here &mdash; though the Act expressly provides that <strong>you cannot be convicted for placing a bet</strong> with an offshore operator. What you give up is recourse: no New Zealand regulator stands behind them. <a href="#law">The full position is below</a>, and it is worth reading before you deposit.</p></div>
</div></section>
''')
    o.append('<section class="sec" style="padding-top:0;padding-bottom:0"><div class="wrap">'
             + toc([("What the 2025 law actually changed", "law"),
                    ("Where you can legally bet", "where"),
                    ("Best sports betting sites, ranked", "sites"),
                    ("Best betting site by what you want", "picks"),
                    ("Full comparison table", "compare"),
                    ("How we rank betting sites", "ranking"),
                    ("Sports Kiwis bet on", "sports"),
                    ("Racing betting in New Zealand", "racing"),
                    ("Deposits and withdrawals in NZD", "banking"),
                    ("Free bets and betting bonuses", "bonuses"),
                    ("Odds, margins and line shopping", "odds"),
                    ("In-play, cash out and betting tools", "tools"),
                    ("Betting on mobile", "mobile"),
                    ("Trust, safety and what to watch for", "trust"),
                    ("Responsible gambling", "rg"),
                    ("Frequently asked questions", "faq")])
             + '</div></section>')

    # --- LAW
    o.append(f'''<section id="law" class="sec"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">Start here</span>
<h2>What the 2025 law actually changed &mdash; and what it did not</h2>
<p>On <strong>28 June 2025</strong>, the Racing Industry Amendment Act 2025 came into force and extended TAB NZ&rsquo;s long-standing monopoly on racing and sports betting from land-based wagering to cover <strong>online betting as well</strong>. The stated purpose was to protect the financial sustainability of the New Zealand racing industry, which had been losing an estimated NZ$180 to NZ$200 million a year in turnover to offshore operators &mdash; a large share of it on NBA basketball.</p>
<p>The change matters because of where the Act places the obligation. It is now unlawful for any person other than TAB NZ or its partner organisation to <strong>offer or promote</strong> racing betting, sports betting, or other racing or sports betting to a person in New Zealand. That prohibition binds operators and promoters. It does not bind you.</p>
<div class="note note--mint"><b>The part most sites leave out</b>
<p>The legislation expressly provides that <strong>an individual may not be convicted of an offence for placing a bet with an offshore betting operator</strong>. If you place a bet from New Zealand with a bookmaker in Curaçao, you have not committed an offence. The offence, if there is one, belongs to the operator that offered you the bet. We state this plainly because a lot of coverage has blurred it into &ldquo;offshore betting is illegal in New Zealand&rdquo;, which is accurate about supply and misleading about you.</p></div>
<h3>What it means in practice</h3>
<ul>
<li><strong>Several major bookmakers left.</strong> A number of large European-licensed operators, including some household names, stopped actively serving New Zealand customers rather than operate against the Act. If a book you used in 2024 now blocks your login, this is why.</li>
<li><strong>Advertising largely disappeared.</strong> Promotion of offshore betting to New Zealanders is caught by the prohibition, so the television, radio and sponsorship presence of offshore books has collapsed.</li>
<li><strong>Some operators stayed.</strong> A smaller group, mostly casino-led sportsbooks licensed in Curaçao and Anjouan, continues to accept New Zealand registrations. These are the sites ranked further down this page.</li>
<li><strong>Your protections got thinner, not thicker.</strong> This is the honest consequence. An operator that is not authorised here is not accountable to the Department of Internal Affairs, so if a dispute arises your only route is that operator&rsquo;s own licensing body.</li>
</ul>
<h3>How this differs from the online casino rules</h3>
<p>The two regimes are moving in opposite directions and it is worth being clear about the difference. <strong>Casino gambling</strong> is being opened up: the Online Casino Gambling Act creates up to 15 New Zealand licences, allocated by auction in September 2026, with unlicensed operators required to exit from 1 December 2026. <strong>Sports and racing betting</strong> has been closed down to a single authorised domestic operator. A site can therefore be perfectly positioned to hold a New Zealand casino licence next year while its sportsbook remains outside the authorised framework. Our <a href="/licensed-online-casinos/">NZ online casino law page</a> tracks the casino side in detail.</p>
</div></div></section>
''')

    # --- WHERE
    o.append(f'''<section id="where" class="sec sec--haze"><div class="wrap">
<div class="sec-head"><span class="kicker">Your options</span><h2>Where New Zealanders can bet online</h2>
<p>There are exactly two categories, and they are not equivalent. Understanding which you are dealing with should come before you compare a single price.</p></div>
<div class="grid grid--2">
<div class="card"><div class="card-ic">{icon("shield")}</div>
<h3>TAB NZ &mdash; the authorised operator</h3>
<p><strong>The only bookmaker authorised to offer racing and sports betting to people in New Zealand</strong>, operating in commercial partnership with Entain. Betcha operates under the same authorised framework.</p>
<p><b>What you get:</b> New Zealand regulatory oversight, a domestic complaints path, guaranteed NZD banking, and the deepest thoroughbred and harness racing pools in the country by a wide margin. Profits fund the New Zealand racing industry and community sport.</p>
<p><b>What you give up:</b> a narrower international sports offering than the global books, generally thinner in-play markets, and no competitive pressure on price because there is no domestic competitor.</p></div>
<div class="card"><div class="card-ic">{icon("flag")}</div>
<h3>Offshore sportsbooks</h3>
<p>Books licensed in Curaçao, Anjouan or similar jurisdictions that continue to accept registrations from New Zealand. They are <strong>not authorised to offer or promote betting here</strong>, though using one is not an offence on your part.</p>
<p><b>What you get:</b> deeper international market coverage, sharper pricing on football, NBA and tennis, better in-play interfaces, crypto banking and larger welcome offers.</p>
<p><b>What you give up:</b> New Zealand regulatory protection entirely. No DIA recourse, payment friction with New Zealand banks, and genuine exit risk if the operator withdraws from the market at short notice.</p></div>
</div>
<div class="note note--amber" style="margin-top:24px"><b>Our editorial position</b>
<p>We list offshore books below because New Zealanders are using them and are better served by accurate information about them than by a page that pretends they do not exist. We are not going to tell you the risks are theoretical, because they are not. If you use one: keep the balance small, withdraw winnings promptly rather than letting them accumulate, complete verification on day one, and never deposit money you would be unable to absorb losing to an operator exit rather than to a bet.</p></div>
</div></section>
''')

    # --- PICKS
    o.append(f'''<section id="picks" class="sec sec--haze"><div class="wrap">
<div class="sec-head"><span class="kicker">Straight to it</span><h2>Best betting site by what you want</h2>
<p>No single book leads on everything, and the right account depends entirely on what you bet on and how often you cash out.</p></div>
{picks([
 ("Best overall & fastest payouts","rooster-bet","The deepest rugby union and rugby league markets of any offshore book, a real casino attached on the same wallet, and payouts inside six hours."),
 ("Best in-play","betandplay","Live prices refresh faster than anything else we tested and bets are accepted without the constant freezes that ruin live betting elsewhere. The fairest free bet terms here too, at 5x on odds of 1.80 or better."),
 ("Biggest welcome offer","gunsbet","285% up to €7,500 plus 285 free spins, from an operator running since 2016. Euro-denominated and no crypto, so budget for the conversion spread."),
 ("Best niche markets","ivibet-sportsbook","Netball, handball and table tennis priced properly rather than ignored. Worth an account if you bet outside the mainstream."),
])}
</div></section>
''')

    # --- COMPARE (single merged table, all 12 books)
    rows = []
    for b in ops:
        sports_cov, live, cash = FEATURES[b["slug"]]
        nzd = ("<span class='t-yes'>Yes</span>" if "NZD bank transfer" in b["payments"]
               else ("<span class='t-no'>Crypto only</span>" if b["slug"] == "spino"
                     else "<span class='t-no'>No</span>"))
        pay = b["payout_crypto"] if b["payout_crypto"] != "Not supported" else b["payout_ewallet"]
        rows.append([
            f'<a href="/casino-reviews/{b["slug"]}/">{esc(b["name"])}</a>',
            f'<b>{b["rating"]}</b>', esc(b["tagline"]),
            esc(b["sports_bonus"] or b["casino_bonus"] or "&mdash;"),
            TURNOVER.get(b["slug"], esc(b["wagering"])),
            sports_cov, live, cash, nzd, esc(pay)])
    o.append(f'''<section id="compare" class="sec"><div class="wrap">
<div class="sec-head"><span class="kicker">Side by side</span><h2>Online betting sites NZ compared</h2>
<p>All four books, on the ten things that decide which account is worth opening &mdash; with the free bet turnover condition shown rather than hidden. Scroll the table sideways on a phone.</p></div>
{table(["Betting site","Score","Best for","Welcome offer","Turnover condition","Sports covered","Live betting","Cash out","NZD","Payout speed"], rows, minw=1320)}
<p style="font-size:.85rem;color:var(--mute)">Payout speed is the cryptocurrency figure we recorded, except at Gunsbet which has no crypto rail &mdash; that figure is e-wallet. NZD bank withdrawals take one to three business days everywhere.</p>
</div></section>
''')

    # --- RANKING METHOD
    o.append(f'''<section id="ranking" class="sec sec--haze"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">Our method</span>
<h2>How we rank sports betting sites</h2>
<p>Our sportsbook scoring uses six criteria, weighted for what matters to a New Zealand punter rather than a British or American one. The weights are published so that any gap between a score and a ranking position would be visible to you.</p>
<ul>
<li><strong>Market depth on NZ-relevant sport (25%).</strong> Rugby union down to NPC level, rugby league including the Warriors, netball, and Black Caps cricket. A book with 40 football leagues and no NPC is not a New Zealand betting site.</li>
<li><strong>Price and margin (25%).</strong> We sample head-to-head and handicap prices across rugby, NBA, football and tennis and calculate the implied margin. A 2% difference here outweighs any welcome offer over a year.</li>
<li><strong>Withdrawal speed (20%).</strong> Timed by us from request to funds landing, separately for crypto, e-wallet and NZD bank.</li>
<li><strong>In-play quality (15%).</strong> Refresh rate, bet rejection rate and how the interface behaves on a patchy mobile connection.</li>
<li><strong>Banking (10%).</strong> Native NZD balances, which methods clear from New Zealand banks, and whether withdrawals fail.</li>
<li><strong>Trust and transparency (5%).</strong> Verifiable licence number, named operating company, and withdrawal terms that do not reserve unlimited discretion.</li>
</ul>
<p>Full detail is on our <a href="/how-we-rate-casinos/">review methodology page</a>, including what disqualifies an operator outright &mdash; we excluded 22 operators this year, several paying well above average commission.</p>
</div></div></section>
''')

    # --- SPORTS
    o.append(f'''<section id="sports" class="sec"><div class="wrap">
<div class="sec-head"><span class="kicker">Markets</span><h2>What Kiwis bet on, and where each book is strongest</h2>
<p>New Zealand&rsquo;s betting profile does not look like Britain&rsquo;s or America&rsquo;s. Rugby carries a weight here it carries almost nowhere else, and netball is a genuine market rather than a novelty. A book that prices those properly is worth more to a Kiwi punter than one with a marginally better Premier League margin.</p></div>
{cards([
 ("ball","Rugby union","Super Rugby Pacific, the Rugby Championship, All Blacks tests and the NPC. The market that matters most here and the one most international books treat as an afterthought. <a href='/casino-reviews/rooster-bet/'>Rooster Bet</a> was the only offshore book we tested that priced NPC matches consistently, including handicaps and first try-scorer."),
 ("ball","Rugby league","The NRL, and the Warriors in particular, drive a large share of New Zealand sports turnover. Look for books offering margin handicaps, first try-scorer and same-game multis rather than head-to-head alone."),
 ("chart","Basketball","The NBA is the single largest category by offshore turnover from New Zealand, helped by tip-off times that land in the Kiwi morning. Offshore books generally price the NBA more sharply than TAB NZ because their liquidity is far deeper."),
 ("ball","Football","Premier League, Champions League and the A-League. The most competitively priced sport across the board, with margins of 2–4% at the better books. Also where in-play depth varies most between operators."),
 ("ball","Cricket","Black Caps limited-overs and tests, the IPL, and the Super Smash. Outright and top-batsman markets are where the value tends to sit; match odds are efficiently priced almost everywhere."),
 ("ball","Netball","The ANZ Premiership and Silver Ferns tests. Almost ignored by international books, which is precisely why it can be worth finding one that prices it. <a href='/casino-reviews/ivibet-sportsbook/'>Ivibet</a> was the best of the offshore group here."),
 ("bolt","Esports","CS2, League of Legends, Dota 2 and Valorant, growing quickly with younger New Zealand punters. Coverage is deep at the crypto-friendly books and thin at TAB NZ."),
 ("coin","Racing","Thoroughbred, harness and greyhound. This is TAB NZ&rsquo;s stronghold — domestic pools, full form data and every New Zealand meeting. See the racing section below."),
])}
</div></section>
''')

    # --- RACING
    o.append(f'''<section id="racing" class="sec sec--haze"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">Racing</span>
<h2>Racing betting in New Zealand</h2>
<p>Racing deserves its own treatment because the domestic and offshore options are not remotely comparable, and because the 2025 law exists largely because of it.</p>
<p><strong>TAB NZ runs the domestic pools.</strong> New Zealand thoroughbred and harness racing is bet into totalisator pools operated here, which means the odds you see reflect New Zealand money and the dividends are calculated on New Zealand turnover. An offshore book pricing a Riccarton maiden is quoting a fixed price off someone else&rsquo;s market, usually with a wider margin and lower limits, and it will not offer the exotics &mdash; trifectas, First 4, Quinellas and multi-leg pools &mdash; that make up a large share of serious racing play here. It also will not carry full New Zealand form, sectional times or scratchings in real time.</p>
<p>Add to that the destination of the money. Betting duty and the point-of-consumption charges on racing turnover fund the New Zealand racing industry directly. If domestic racing is something you want to still exist in ten years, where you bet on it is not a neutral choice.</p>
<div class="note"><b>Our practical recommendation on racing</b>
<p>For New Zealand thoroughbred and harness racing, TAB NZ is both the lawful option and, on the merits, clearly the better product. Offshore books are worth an account for international sport and in-play markets where their depth and pricing genuinely beat what is available domestically. Splitting your play that way is what most experienced New Zealand punters we speak to actually do.</p></div>
<h3>International racing</h3>
<p>For Melbourne Cup carnival, Royal Ascot, the Breeders&rsquo; Cup and the Hong Kong internationals, both routes work. TAB NZ co-mingles into overseas pools for the major meetings, which usually gives better value than an offshore fixed price. For a mid-week Wolverhampton card, an offshore book may be the only place you can get a bet on at all.</p>
</div></div></section>
''')

    # --- BANKING
    o.append(f'''<section id="banking" class="sec"><div class="wrap">
<div class="sec-head"><span class="kicker">Banking</span><h2>Depositing and withdrawing in New Zealand dollars</h2>
<p>The mechanics are the same as for online casinos, with one difference that catches punters out: betting accounts turn money over far more often, so a slow withdrawal method costs you more here than it does at a casino.</p></div>
{table(["Method","Deposit","Withdrawal","NZD native","Notes for punters"], [
 ["NZD bank transfer","Instant–1 day","1–3 business days","<span class='t-yes'>Yes</span>","The most reliable route from an ANZ, ASB, BNZ, Kiwibank or Westpac account. Never failed in our testing."],
 ["Cryptocurrency","5–20 min","<b>2–8 hours</b>","<span class='t-no'>No</span>","Fastest by a distance and immune to bank declines. You need an exchange account and you carry price risk while funds are held."],
 ["Visa / Mastercard debit","Instant","2–5 business days","<span class='t-yes'>Yes</span>","Convenient but the most likely to be declined. Some NZ banks block gambling merchant codes outright."],
 ["Skrill / Neteller","Instant","4–24 hours","<span class='t-yes'>Usually</span>","A good compromise on speed. Check whether e-wallet deposits qualify for the free bet — at several books they do not."],
 ["Neosurf","Instant","<span class='t-no'>No</span>","<span class='t-yes'>Yes</span>","Cash voucher from a dairy or service station. Deposit-only, so plan a different withdrawal route from the start."],
 ["POLi","Instant","<span class='t-no'>No</span>","<span class='t-yes'>Yes</span>","Pays direct from your bank account, now via Open Banking APIs. <b>Deposit-only</b> &mdash; plan a separate withdrawal route."],
], minw=860)}
<div class="note note--amber"><b>The 2–3% nobody itemises</b>
<p>If a book holds your balance in euros &mdash; <a href="/casino-reviews/gunsbet/">Gunsbet</a> does &mdash; your bank converts twice, once on the way in and once on the way out, taking roughly 2 to 3% each time. On NZ$2,000 of turnover that is around NZ$100. It is larger than the margin difference between almost any two books, and it is the reason we weight NZD support heavily. <a href="/casino-payment-methods/">Full NZ payment methods guide &rarr;</a></p></div>
</div></section>
''')

    # --- BONUSES
    o.append(f'''<section id="bonuses" class="sec sec--haze"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">Offers</span>
<h2>Free bets and betting bonuses for New Zealanders</h2>
<p>Betting bonuses are structured differently from casino bonuses and are, on the whole, better value &mdash; but only if you read the turnover condition rather than the headline.</p>
<h3>The three shapes a betting offer takes</h3>
<ul>
<li><strong>Matched deposit.</strong> The book matches a percentage of your first deposit in bonus funds, which must be turned over a set number of times before anything can be withdrawn. Gunsbet&rsquo;s 285% is this shape. Large headline, substantial turnover.</li>
<li><strong>Free bet / bet credit.</strong> You place a qualifying bet, and the book credits a free bet of equal value. Crucially, the <strong>stake is usually not returned</strong> with your winnings: a NZ$50 free bet at odds of 2.00 returns NZ$50, not NZ$100. Bet&amp;Play and Rooster Bet use this shape.</li>
<li><strong>Risk-free / bet insurance.</strong> If your first bet loses, you are refunded &mdash; almost always in bonus funds with their own turnover requirement, not in cash. Read whether the refund is cash or credit, because it changes the value by roughly half.</li>
</ul>
<h3>What a fair condition looks like</h3>
{table(["Condition","Fair","Acceptable","Poor"], [
 ["Turnover multiple","<span class='t-yes'>1–5x</span>","6–10x","<span class='t-no'>Above 10x</span>"],
 ["Minimum odds","<span class='t-yes'>1.50–1.80</span>","1.81–2.50","<span class='t-no'>Above 2.50</span>"],
 ["Expiry window","<span class='t-yes'>30 days</span>","14 days","<span class='t-no'>7 days or less</span>"],
 ["Stake returned","<span class='t-yes'>Yes</span>","—","<span class='t-no'>No (the norm)</span>"],
 ["Cashed-out bets count","<span class='t-yes'>Yes</span>","—","<span class='t-no'>No (the norm)</span>"],
 ["Max win from bonus","<span class='t-yes'>Uncapped</span>","10x+ bonus","<span class='t-no'>Under 5x bonus</span>"],
], minw=680)}
<p>By that standard, <a href="/casino-reviews/betandplay/">Bet&amp;Play&rsquo;s 5x at odds of 1.80 or better</a> is comfortably the strongest offer available to New Zealanders here, with <a href="/casino-reviews/rooster-bet/">Rooster Bet&rsquo;s 6x free bet</a> next. <a href="/casino-reviews/ivibet-sportsbook/">Ivibet&rsquo;s 5x at odds of 2.00</a> is modest but clearable. Gunsbet&rsquo;s 285% at 40x is a very large number attached to a very large amount of work.</p>
<div class="note"><b>A note on multi and acca insurance</b>
<p>Several books offer &ldquo;money back if one leg lets you down&rdquo; on multis of four or more selections. These are genuinely decent promotions when the refund is cash and the minimum odds per leg are around 1.40. They are close to worthless when the refund is a bonus bet with its own 5x turnover attached. The distinction is one line in the terms and it changes the value completely.</p></div>
</div></div></section>
''')

    # --- ODDS
    o.append(f'''<section id="odds" class="sec"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">Value</span>
<h2>Odds, margins and why line shopping matters more than the bonus</h2>
<p>A welcome offer is a one-off. A bookmaker&rsquo;s margin applies to every bet you ever place with them. Over a year of regular betting, the margin is worth several times the bonus, and almost nobody compares it.</p>
<h3>How to read a margin</h3>
<p>Convert each price to an implied probability (1 divided by the decimal odds), add them up, and subtract 100%. On a two-way market priced 1.90 / 1.90, that is 52.6% + 52.6% = 105.3%, so a <strong>5.3% margin</strong>. At 1.95 / 1.95 it is 2.6%. That difference &mdash; five cents on the price &mdash; is the difference between a book you can beat over time and one you cannot.</p>
{table(["Market type","Sharp margin","Typical margin","Where it gets expensive"], [
 ["Football match odds","2–4%","5–7%","Correct score and first scorer: 15–25%"],
 ["NBA head-to-head","2–3%","4–6%","Player props: 8–14%"],
 ["Rugby union head-to-head","4–5%","6–9%","First try-scorer: 20%+"],
 ["Tennis match winner","2–4%","5–7%","Set betting: 8–12%"],
 ["Multis / accumulators","—","—","Margin compounds per leg — a 5% margin over four legs is roughly 21%"],
], minw=720)}
<div class="note note--amber"><b>The single most valuable habit in betting</b>
<p>Hold two or three accounts and check the price at each before every bet. A 3% average improvement on the price you take is worth more than every welcome bonus on this page combined once your annual turnover passes about NZ$3,000. It costs you thirty seconds a bet. Note also that multis compound the margin on every leg, which is why books promote them so heavily &mdash; a four-leg multi at a 5% per-leg margin gives the book roughly 21%.</p></div>
</div></div></section>
''')

    # --- TOOLS
    o.append(f'''<section id="tools" class="sec sec--haze"><div class="wrap">
<div class="sec-head"><span class="kicker">Features</span><h2>In-play, cash out and the tools worth having</h2>
<p>Feature lists on betting sites are long and mostly padding. These are the five that change how you actually bet.</p></div>
{cards([
 ("bolt","Live / in-play betting","Prices updating during the match. The quality differences here are enormous: <a href='/casino-reviews/betandplay/'>Bet&amp;Play</a> refreshed fastest with the fewest rejected bets, while two books we tested froze markets so often that in-play was effectively unusable. If you bet live, test this before you fund an account properly."),
 ("coin","Cash out","Settle a bet early for a guaranteed return below the full payout. Convenient, and expensive — the book builds a margin into every cash-out price, typically 5–10% worse than the fair value of your position. Useful for genuine risk management, costly as a habit."),
 ("chart","Bet builder / same-game multi","Combining several outcomes from one match. Hugely popular and hugely profitable for books, because correlated legs are priced with a compounding margin. Enjoy them for what they are; do not mistake them for value."),
 ("mobile","Live streaming","Watch the event you have bet on inside the account, usually requiring a funded balance or an active bet. Rooster Bet streams selected football and tennis. Rights restrictions mean almost nothing from New Zealand domestic sport is available this way."),
 ("clock","Early payout","Some books pay a football bet as a winner at two goals clear, or a rugby bet at a set margin, regardless of the final result. A genuinely player-favourable promotion when it is offered without conditions attached."),
 ("shield","Deposit and loss limits","Not a betting feature, a control. Every operator here offers deposit caps, session reminders, time-outs and self-exclusion. Set the limit when you open the account, when you are calm and it costs you nothing to be sensible.","/responsible-gambling/","Responsible gambling"),
])}
</div></section>
''')

    # --- MOBILE
    o.append(f'''<section id="mobile" class="sec"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">Mobile</span>
<h2>Betting on your phone in New Zealand</h2>
<p>Almost all New Zealand betting turnover happens on a phone, and almost no offshore bookmaker ships an app to the New Zealand App Store or Google Play, because both platforms restrict real-money gambling apps here. That is not the problem it sounds like.</p>
<p>What operators build instead is a <strong>progressive web app</strong> &mdash; a mobile site that you add to your home screen from the browser share menu, which then opens full-screen with no address bar and behaves like a native app. It does not need an app store account, it never asks you to install an update, and it takes about ten seconds to set up. On iOS: Safari, share button, <em>Add to Home Screen</em>. On Android: Chrome, menu, <em>Install app</em> or <em>Add to Home screen</em>.</p>
<p>What to check before you commit to a book on mobile: whether the bet slip stays reachable one-handed, whether live prices update without a manual refresh, whether the deposit flow works without bouncing you out to a broken bank redirect, and whether you can complete a withdrawal entirely on the phone. We test all four. <a href="/casino-reviews/rooster-bet/">Rooster Bet</a> had the best mobile build of the four books here, and <a href="/casino-reviews/betandplay/">Bet&amp;Play</a> handles a patchy connection best &mdash; it queues the bet and confirms on reconnection rather than simply failing.</p>
<p>One New Zealand-specific point: mobile data coverage outside the main centres is variable, and a betting interface that assumes constant connectivity will reject bets on a patchy 4G signal. Books that queue the bet and confirm on reconnection handle this far better than those that simply fail. It is a small thing that matters if you bet from a farm, a bach or a car park at a provincial ground.</p>
</div></div></section>
''')

    # --- TRUST
    o.append(f'''<section id="trust" class="sec sec--haze"><div class="wrap">
<div class="sec-head"><span class="kicker">Safety</span><h2>Trust, licensing and what to watch for</h2>
<p>With no New Zealand regulator standing behind an offshore book, the due diligence falls to you. These are the checks we run on every operator, and you can run them in about five minutes.</p></div>
<ol class="steps">
<li><h4>Find the licence number, then verify it</h4><p>It should be in the footer with a number, not just a badge. Take the number to the regulator&rsquo;s public register &mdash; the Curaçao Gaming Control Board maintains one &mdash; and confirm it is live and matches the company named. A badge image proves nothing; anyone can host a PNG. Any book that does not publish a number is an immediate no.</p></li>
<li><h4>Identify the operating company</h4><p>You are looking for a named legal entity and a registered address, usually in the terms and conditions. Dama N.V., Rabidi N.V. and Vertikal N.V. are all real companies with traceable histories. &ldquo;Not published&rdquo; is a genuine red flag, and an operator that will not name the company holding its licence is one we mark down wherever it appears on this site.</p></li>
<li><h4>Read the withdrawal terms before you deposit</h4><p>Specifically: the weekly and monthly withdrawal ceilings, whether withdrawals are processed on weekends, whether a fee applies below a threshold, and whether the book reserves a right to pay large wins in instalments. All of that is in the T&amp;Cs and none of it is in the marketing.</p></li>
<li><h4>Complete verification on day one</h4><p>Upload a New Zealand driver licence or passport, a proof of address dated within three months, and a screenshot of your payment method, before you have a balance worth withdrawing. Almost every &ldquo;they won&rsquo;t pay me&rdquo; story we investigate is an incomplete KYC file discovered at the worst possible moment.</p></li>
<li><h4>Test with a small withdrawal early</h4><p>Deposit, place a modest bet, and withdraw whatever is left within the first week. You are buying information about how this operator behaves when it owes you money, and the cost of that information is essentially zero. We do exactly this at every book we review.</p></li>
</ol>
<div class="note"><b>Signals we treat as disqualifying</b>
<p>No published licence number; no named operating company; terms that permit voiding winnings at the operator&rsquo;s sole discretion without defined grounds; a pattern of unresolved non-payment complaints on independent forums; or a withdrawal process that requires contacting support rather than a self-service request. Any one of these and the book does not appear on this site, regardless of commercial terms.</p></div>
</div></section>
''')

    o.append(band("Also from our team",
                  "We opened accounts at 41 online casinos, deposited our own New Zealand dollars and timed "
                  "every withdrawal. The full casino rankings, payout data and the 2026 licensing changes.",
                  "Best online casino sites NZ", "/online-casinos/"))

    o.append('<section id="rg" class="sec" style="padding:0"></section>')
    o.append(rg_block())
    o.append(faq_block(FAQ, "Online betting NZ: frequently asked questions"))
    o.append(paa_for(PATH, haze=False))

    o.append(f'''<section class="sec"><div class="wrap"><div class="prose prose--wide">
<h2>The bottom line on online betting in New Zealand</h2>
<p>New Zealand has made a deliberate policy choice: one authorised betting operator, with the proceeds directed to the racing industry and community sport. Whether you think that is the right call, it is the law as at {UPDATED_NZ}, and it is enforced against operators rather than against you.</p>
<p>If you bet on New Zealand racing, TAB NZ is both the lawful and the better option &mdash; the pools are domestic, the exotics exist, and the form data is complete. If you bet on international sport, offshore books offer depth and pricing that TAB NZ does not attempt to match, and using one does not put you in legal jeopardy. What it does is remove your safety net, so size your balance accordingly, verify your account on day one, and withdraw your winnings rather than letting them sit.</p>
<p>Whatever you choose, set a deposit limit before you place the first bet. It is the one decision on this page that is guaranteed to be worth making.</p>
{authorbox("daniel-ashworth")}
</div></div></section>
''')

    o.append(disclosure_section(
        "This page describes the legal position for players as at " + UPDATED_NZ
        + " and is general information, not legal advice."))
    o.append(footer())
    return write(PATH, "".join(o))
