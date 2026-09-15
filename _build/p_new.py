# -*- coding: utf-8 -*-
"""/new-casinos-nz/ — new online casinos NZ, kept as a running list.

Highest refresh value on the site: from 1 December 2026 the licensed operators
start going live, and this page becomes the record of who launched and when.
Update LAUNCHES and bump UPDATED_NZ in lib.py each time.
"""
from lib import *

TITLE = "New Online Casinos NZ 2026 | Newest Casino Sites"
DESC = ("New online casinos NZ players can join in 2026, updated as licensed operators launch. "
        "What to check before joining a new casino site, and which are safe.")
PATH = "/new-casinos-nz/"

# Newest first. `launched` is the month we first verified it accepting NZ players.
LAUNCHES = [
    ("kingdom", "2024", "7,000+ games and the fastest crypto payouts we have recorded from a site this new."),
    ("smash", "2024", "10x wagering — the most player-friendly bonus terms of any recent launch."),
    ("rivo", "2024", "Built phone-first; the best mobile experience of any new casino site we tested."),
    ("madcasino", "2024", "A genuine two-product launch — casino and sportsbook on one wallet from day one."),
    ("crownslots", "2024", "The largest headline welcome package of any new NZ-facing casino. Euro-denominated."),
    ("roby-casino", "2024", "Large bonus, but no published licence number or operating company. Treat with caution."),
    ("spino", "2024", "Crypto-first with a zero-wagering welcome offer and ten-minute withdrawals."),
]

FAQ = [
 ("Are new online casinos safe in NZ?",
  "<p>Some are, and a new brand is not automatically a worse brand &mdash; several of the "
  "strongest sites we rate launched in 2024. What a new casino lacks is a <strong>track "
  "record</strong>, which is the single most useful thing you can have about an operator. The "
  "substitutes are checkable: a verifiable licence number, a named operating company, withdrawal "
  "terms that do not reserve unlimited discretion, and a small test withdrawal in your first week. "
  "See <a href='/how-we-rate-casinos/'>how we vet them</a>.</p>"),
 ("Why do new casinos offer bigger bonuses?",
  "<p>Customer acquisition. A new online casino NZ players have never heard of has to buy attention, "
  "and the bonus is the cheapest way to do it &mdash; which is why the biggest headline offers on "
  "this site come from 2024 launches. That is a real opportunity, provided you read the "
  "<a href='/casino-bonus/'>wagering terms</a> rather than the banner. A 600% match at 45x is worse "
  "than a 100% match at 10x, whatever the brand&rsquo;s age.</p>"),
 ("Which new casinos are licensed in New Zealand?",
  "<p>None yet. The Department of Internal Affairs ran its licence auction in September 2026 and is "
  "processing applications from October, so the first New Zealand licence holders are not confirmed. "
  "Every new casino site currently accepting Kiwi players holds an <strong>offshore</strong> licence "
  "&mdash; Cura&ccedil;ao, Anjouan or similar. We track the licensing position on our "
  "<a href='/licensed-online-casinos/'>licensed online casinos page</a>.</p>"),
 ("What should I check before joining a new casino?",
   "<p>Five things, in about five minutes. <strong>Licence number</strong> &mdash; verify it on the "
   "regulator&rsquo;s public register, not the footer badge. <strong>Operating company</strong> "
   "&mdash; a named legal entity in the terms. <strong>Withdrawal terms</strong> &mdash; weekly cap, "
   "weekend processing, fees. <strong>Bonus terms</strong> &mdash; the full document, not the banner. "
   "Then <strong>test with a small withdrawal</strong> in week one, which tells you more than any "
   "review.</p>"),
 ("Do new online casinos have no deposit bonuses?",
  "<p>Rarely, and less often than older brands. New operators put their acquisition budget into "
  "large matched deposits rather than unconditional giveaways, because a deposit filters for intent. "
  "Across every new casino site we checked, none offered a genuine no deposit bonus &mdash; the only "
  "verified one in this market is at a 2022 brand. See our "
  "<a href='/no-deposit-bonus/'>no deposit bonus page</a>.</p>"),
 ("Will there be new casinos launching in New Zealand in 2027?",
  "<p>Yes, and they will be a different kind of launch. Up to <strong>15 licensed brands</strong> "
  "will go live under DIA supervision, with mandatory harm-minimisation tools and New Zealand "
  "advertising rules &mdash; and, in all likelihood, smaller bonuses than the offshore market offers "
  "today. Expect the overall number of casinos reachable from a New Zealand IP address to fall "
  "sharply even as the licensed ones appear.</p>"),
]


def build():
    ops = pick_ops([s for s, _, _ in LAUNCHES])
    cr = [("Home", "/"), ("Online Casinos NZ", "/online-casinos/"), ("New Online Casinos NZ", PATH)]
    schema = page_schema(
        "CollectionPage", TITLE, DESC, PATH,
        extra=[crumb_schema(cr),
               itemlist_schema(ops, "New online casinos NZ 2026", PATH),
               faq_schema(FAQ + paa_items(PATH), f"{SITE}{PATH}#faq")])
    o = [head(TITLE, DESC, PATH, schema),
         crumbs([("Home", "/"), ("Online Casinos NZ", "/online-casinos/"),
                 ("New Online Casinos NZ", None)])]

    o.append(f'''<section class="hero"><div class="wrap">
<span class="eyebrow">{icon("clock")} Running list &middot; last updated {UPDATED_NZ}</span>
<h1>New Online Casinos NZ: Newest Casino Sites [{MONTH_YEAR}]</h1>
{byline()}
<p class="lede">New casinos NZ players can join kept as a running list rather than written once and left. The newest online casinos New Zealand offers, Every new casino site here has taken a real deposit from us and paid a real withdrawal back &mdash; and from December 2026 this page also tracks which licensed operators go live.</p>
<div class="hero-stats">
<div class="hero-stat"><b>{len(LAUNCHES)}</b><span>New casino sites listed</span></div>
<div class="hero-stat"><b>{UPDATED_NZ}</b><span>Last updated</span></div>
<div class="hero-stat"><b>0</b><span>NZ-licensed so far</span></div>
<div class="hero-stat"><b>15</b><span>Licences coming</span></div>
</div>
</div></section>
''')

    o.append(leaderboard(
        ops, "casino",
        heading="Newest online casinos NZ players can join",
        intro="Brand new online casinos NZ 2026 &mdash; every one launched within the last two years and "
              "tested by us since. New does not mean unsafe, but it does mean no track record, so the "
              "checks further down this page matter more here than anywhere else on the site."))

    rows = []
    notes = {s: (y, n) for s, y, n in LAUNCHES}
    for c in ops:
        slug = c["slug"]; yr, note = notes[slug]
        rows.append([f'<a href="/casino-reviews/{slug}/">{esc(c["short"])}</a>', yr,
                     f'{c["rating"]}', esc(c["licence"]),
                     esc(c["operator_co"]) if c["operator_co"] != "Not published"
                     else "<span class='t-no'>Not published</span>",
                     esc(c["casino_bonus"] or "&mdash;"), note])
    o.append(f'''<section class="sec"><div class="wrap">
<div class="sec-head"><span class="kicker">The list</span><h2>Latest online casinos NZ: launch year and licensing</h2>
<p>New casino sites NZ players ask about most, with the two facts that matter about a young brand &mdash; who licenses it and who operates it &mdash; in the same row.</p></div>
{table(["New casino site","Launched","Score","Licence","Operator","Welcome offer","Why it stands out"], rows, minw=1080)}
<p style="font-size:.85rem;color:var(--mute)">&ldquo;Launched&rdquo; is the year the brand began accepting New Zealand players, not the year the company was incorporated. Updated {UPDATED_NZ}.</p>
</div></section>
''')

    o.append(f'''<section class="sec sec--haze"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">From December</span>
<h2>New licensed casinos NZ: what December 2026 changes</h2>
<p>Everything on this page today is an offshore brand. That is about to become a two-tier market, and the newest online casinos NZ players see in 2027 will be a genuinely different proposition from the ones here now.</p>
<p>The Department of Internal Affairs ran its licence auction in <strong>September 2026</strong> and is processing applications from October. Up to <strong>15 licences</strong> will be issued, each covering a single brand, with no applicant holding more than three. From <strong>1 December 2026</strong>, providers that have not applied must stop offering online casino gambling to New Zealanders.</p>
<p>What that means practically for anyone looking at a new casino site:</p>
<ul>
<li><strong>A new brand launching in 2027 under a DIA licence</strong> answers to a New Zealand regulator. That is a materially better position for you than any offshore licence offers, and it is the first time it has been available here.</li>
<li><strong>A new brand launching without one</strong> is launching into a market where advertising to you is prohibited and payment providers are increasingly cautious. Treat it accordingly.</li>
<li><strong>Bonuses will probably shrink.</strong> Licensed operators face New Zealand promotional rules and a levy on profits. The 600% offers on this page are a feature of an unregulated market, not a permanent fixture.</li>
<li><strong>Some brands you use now will exit.</strong> Withdraw winnings as you make them rather than letting a balance accumulate through the transition.</li>
</ul>
<div class="note"><b>We update this page as launches happen</b>
<p>As each licensed operator goes live we will add it here with the date, and note which offshore brands leave. Our <a href="/licensed-online-casinos/">licensed online casinos page</a> tracks the licence holders themselves. Both carry a visible last-updated stamp so you can see how current they are before you trust them.</p></div>
</div></div></section>
''')

    o.append(f'''<section class="sec"><div class="wrap">
<div class="sec-head"><span class="kicker">Before you join</span><h2>What to check before joining a new casino</h2>
<p>A new online casino NZ real money account deserves more scrutiny than an established one, for the simple reason that there is no complaint history to read. These five checks take about five minutes and substitute for the track record you do not have.</p></div>
<ol class="steps">
<li><h4>Verify the licence, do not trust the badge</h4><p>Find the licence number in the footer and check it against the regulator&rsquo;s public register. The Cura&ccedil;ao Gaming Control Board maintains one. A logo image proves nothing &mdash; anyone can host a PNG. No number published is an immediate no.</p></li>
<li><h4>Find the operating company</h4><p>A named legal entity and registered address, usually in the terms. Dama N.V., Rabidi N.V. and Vertikal N.V. all have traceable histories. &ldquo;Not published&rdquo; is a genuine red flag on an established brand and a serious one on a new casino site.</p></li>
<li><h4>Read the withdrawal terms before depositing</h4><p>Weekly and monthly ceilings, weekend processing, fees below a threshold, and whether the operator reserves the right to pay large wins in instalments. All in the T&amp;Cs, none of it in the marketing.</p></li>
<li><h4>Check the bonus terms against the banner</h4><p>New casinos compete on bonus size, so this is where the gap between advertised and actual is widest. Wagering multiplier, what it applies to, maximum bet while wagering, game contribution and expiry. If the terms contradict the banner, that tells you what kind of operator it is.</p></li>
<li><h4>Test with a small withdrawal in week one</h4><p>Deposit, play modestly, withdraw whatever is left. You are buying information about how this operator behaves when it owes you money, and it costs essentially nothing. We do exactly this at every new casino site we review.</p></li>
</ol>
</div></section>
''')

    o.append(band("Prefer an established brand?",
                  "If a track record matters more to you than a launch bonus, our main ranking covers "
                  "15 tested casinos including several running since 2021 and 2022.",
                  "Best online casinos NZ", "/online-casinos/"))
    o.append(rg_block())
    o.append(faq_block(FAQ, "New online casinos NZ: your questions answered"))
    o.append(paa_for(PATH, haze=False))
    o.append('<section class="sec"><div class="wrap"><div class="prose prose--wide">'
             + authorbox("angus-mclean") + '</div></div></section>')
    o.append(disclosure_section())
    o.append(footer())
    return write(PATH, "".join(o))
