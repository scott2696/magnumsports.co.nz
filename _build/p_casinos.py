# -*- coding: utf-8 -*-
"""/online-casinos/ — the casino pillar hub."""
from lib import *

TITLE = "Online Casinos NZ 2026 | Every Real Money Casino Site Reviewed"
DESC = ("The complete New Zealand online casino hub: 16 real money casino sites reviewed and ranked, "
        "plus guides to pokies, bonuses, payouts, live dealer, crypto and NZ gambling law.")
PATH = "/online-casinos/"

FAQ = [
 ("How many online casinos accept New Zealand players?",
  "<p>Several hundred will take a registration from a New Zealand IP address. Far fewer are worth your time. We "
  "assessed 41 this year and publish 16, having excluded the rest for slow or refused payouts, unverifiable "
  "licensing, bonus terms that contradict the advertised offer, or an inability to handle NZD without punitive "
  "conversion. That number will fall further from <strong>1 December 2026</strong>, when operators without a New "
  "Zealand licence application must stop serving New Zealanders.</p>"),
 ("What is the difference between an online casino and online pokies?",
  "<p>Pokies are a category of game; an online casino is the venue that hosts them. Every casino on this site "
  "offers pokies &mdash; typically 85 to 90% of the lobby &mdash; alongside table games, live dealer tables and "
  "increasingly crash titles. If pokies are all you play, our <a href='/online-pokies/'>online pokies page</a> "
  "ranks sites specifically on lobby quality, studio coverage, RTP transparency and volatility filtering rather "
  "than on the casino as a whole.</p>"),
 ("Can I play at more than one online casino?",
  "<p>Yes, and most regular players do. There is no register linking accounts across operators, and holding two "
  "or three lets you claim more than one welcome offer and compare payout behaviour before committing. The one "
  "thing to avoid is opening multiple accounts <em>at the same operator or operator group</em> &mdash; Rabidi "
  "N.V., Vertikal N.V. and TechOptions each run several brands on this page, and duplicate accounts within a "
  "group are routinely closed with bonuses voided.</p>"),
 ("What is RTP and does it really matter?",
  "<p>Return to player is the percentage a game pays back over millions of spins &mdash; 96% RTP means a "
  "theoretical NZ$4 loss per NZ$100 wagered, over the very long run. It matters cumulatively rather than in any "
  "single session. Over a year of NZ$5,000 turnover, the gap between a 94% and a 97% game is NZ$150 of expected "
  "difference. It does not predict tonight. Our <a href='/high-payout-casinos/'>high payout casinos page</a> "
  "covers which games and sites publish RTP honestly.</p>"),
 ("How long does a casino withdrawal take in New Zealand?",
  "<p>From our own timed tests: cryptocurrency 10 minutes to six hours, e-wallets four to 24 hours, and card or "
  "NZD bank transfer one to five business days. The variable that dwarfs all of these is verification &mdash; an "
  "unverified account can sit for three days before anyone looks at it. Upload your ID on day one. See "
  "<a href='/fast-payout-casinos/'>fast payout casinos</a> for the full data.</p>"),
 ("Are online casino games rigged?",
  "<p>Not at licensed operators running games from established studios, and the reason is structural rather than "
  "a matter of trust. The casino does not run the games; studios such as Pragmatic Play, Evolution, "
  "Play&rsquo;n GO and NetEnt do, on their own servers, with outcomes from tested random number generators "
  "audited by independent labs. An operator cannot adjust the RTP of a Pragmatic Play title any more than a pub "
  "can adjust a Sky broadcast. What a dishonest operator can do is refuse to pay you &mdash; which is why our "
  "scoring weights withdrawal behaviour at 25% and game fairness barely at all.</p>"),
]


def build():
    ops = CASINOS
    schema = page_schema(
        "CollectionPage", TITLE, DESC, PATH,
        extra=[crumb_schema([("Home", "/"), ("Online Casinos", PATH)]),
               itemlist_schema(ops, "Online casinos NZ 2026", PATH),
               faq_schema(FAQ, f"{SITE}{PATH}#faq")])
    o = [head(TITLE, DESC, PATH, schema), crumbs([("Home", "/"), ("Online Casinos", None)])]

    o.append(f'''<section class="hero"><div class="wrap">
<span class="eyebrow">{icon("dice")} 41 tested &middot; 16 recommended</span>
<h1>Online Casinos NZ: The Complete Guide</h1>
{byline()}
<p class="lede">Everything we know about playing at an online casino from New Zealand, in one place. Sixteen reviewed sites, the banking methods that actually clear from a Kiwi bank account, the bonus terms worth taking, and where the 2026 licensing regime leaves you.</p>
</div></section>
''')
    o.append('<section class="sec" style="padding-bottom:0"><div class="wrap">' + disclosure() + '</div></section>')

    o.append(leaderboard(ops, "casino",
                         heading="Every online casino we recommend for NZ players",
                         intro="Scored on payout speed, NZD banking, bonus terms, game range, licensing and "
                               "support. Full detail in each review."))

    o.append(f'''<section class="sec sec--haze"><div class="wrap">
<div class="sec-head"><span class="kicker">Explore</span><h2>Find the right kind of casino</h2>
<p>Every page below is built on the same testing data as the ranking above, filtered and re-scored for one specific thing you might care about.</p></div>
{cards([
 ("dice","Online pokies NZ","The pokies-first ranking: studio coverage, RTP transparency, volatility filtering and which sites stock the high-variance titles Kiwi players actually seek out.","/online-pokies/","Best pokies sites"),
 ("bolt","Fast payout casinos","Ranked purely on the withdrawal times we recorded ourselves, method by method, including what actually causes delays.","/fast-payout-casinos/","Fastest payouts"),
 ("chart","High payout casinos","Highest RTP games and the sites that publish their figures. Where to get the longest play from a fixed budget.","/high-payout-casinos/","Best RTP casinos"),
 ("users","Live dealer casinos","Evolution and Pragmatic Live coverage, table limits in NZD, and which studios are open at 9pm New Zealand time.","/live-casinos/","Best live casinos"),
 ("lock","Crypto casinos","Bitcoin, Ethereum and USDT casinos, provably fair games, and the tax treatment Kiwis need to understand before they start.","/best-crypto-casinos/","Crypto casinos NZ"),
 ("coin","Casino bonuses","Every welcome offer on this site compared clause by clause — wagering, contribution, max bet, expiry and win caps.","/online-casinos/bonuses/","Compare bonuses"),
 ("star","No deposit bonuses","The handful of genuine no-deposit offers still available to New Zealanders, with the catch on each stated plainly.","/no-deposit-casinos/","No deposit offers"),
 ("book","All casino reviews","Full hands-on reviews of all 19 operators we cover, including the ones we do not recommend and why.","/casino-reviews/","Read reviews"),
])}
</div></section>
''')

    o.append(f'''<section class="sec"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">The basics</span>
<h2>How online casinos work for New Zealand players</h2>
<p>If you have never opened an account, the process is less involved than most people expect and the friction all sits in one place &mdash; verification &mdash; which you can eliminate entirely by dealing with it first.</p>
<ol class="steps">
<li><h4>Choose a site and register</h4><p>Registration takes two minutes: email, password, name, date of birth, address and currency. <strong>Select NZD if it is offered.</strong> This single choice saves you roughly 2&ndash;3% in conversion spread on every deposit and every withdrawal for the life of the account, and it cannot be changed later at most operators.</p></li>
<li><h4>Verify immediately, before you deposit</h4><p>Upload a New Zealand driver licence or passport, a proof of address dated within three months &mdash; a power bill, a council rates notice or a bank statement &mdash; and a screenshot of the payment method you intend to use. Doing this on day one converts verification from a three-day obstacle into a five-minute chore, and it is the single most useful habit in online gambling.</p></li>
<li><h4>Set your deposit limit</h4><p>Before the first deposit, in the account settings, while you are calm. Daily, weekly or monthly. It costs nothing to set and is deliberately slow to raise at every reputable operator, which is the entire point.</p></li>
<li><h4>Deposit</h4><p>NZD bank transfer and cryptocurrency were the only methods that never failed in our testing. Card deposits usually work but are declined by some New Zealand banks. If you intend to withdraw by crypto, deposit by crypto &mdash; most operators require the same method both ways.</p></li>
<li><h4>Decide on the bonus before you accept it</h4><p>Bonuses are opt-in at almost every site, and declining one is a legitimate choice. A bonus locks your balance until the wagering is cleared, so if you want the freedom to withdraw at any moment, play without it. Our <a href="/online-casinos/bonuses/">bonus guide</a> works through the arithmetic.</p></li>
<li><h4>Play, then withdraw properly</h4><p>Request the withdrawal and then leave it alone. Many operators run a &ldquo;reverse withdrawal&rdquo; window &mdash; a pending period during which you can cancel and play the money back, which is exactly what it is designed to make you do. Look for the setting that disables reversal, and turn it on.</p></li>
</ol>
</div></div></section>
''')

    o.append(f'''<section class="sec sec--haze"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">Context</span>
<h2>The New Zealand online casino market in 2026</h2>
<p>New Zealand is in the middle of the largest change to its gambling framework in two decades, and if you play online it is worth understanding where it is heading.</p>
<h3>From grey market to licensed market</h3>
<p>For twenty years the position was static: the Gambling Act 2003 prohibited operating interactive gambling from within New Zealand, said nothing about New Zealanders playing offshore, and the result was a large, entirely untaxed, entirely unsupervised offshore market. Estimates of the sums involved run into the hundreds of millions annually, none of it subject to New Zealand harm-minimisation requirements.</p>
<p>The <strong>Online Casino Gambling Act</strong> ends that. Up to <strong>15 licences</strong> are being issued by the Department of Internal Affairs, with the right to apply allocated through a competitive auction held in September 2026 and applications processed from October. Each licence covers a single brand, no applicant may hold more than three, and each runs for up to three years with a five-year renewal path. Licensed operators face a levy on profits, mandatory harm-minimisation obligations and New Zealand-specific advertising rules.</p>
<h3>What changes for you</h3>
<ul>
<li><strong>Fewer sites, better protected.</strong> A licensed operator answers to the DIA. If it withholds your winnings, there is a New Zealand body with jurisdiction over it. That is a genuine improvement over the current position, where your only recourse is a regulator in Curaçao or Anjouan.</li>
<li><strong>Mandatory harm-minimisation tools.</strong> Deposit limits, reality checks and self-exclusion become requirements rather than features an operator may choose to offer.</li>
<li><strong>A shrinking choice.</strong> Fifteen brands is a fraction of what is currently reachable. Some sites you like will not be available.</li>
<li><strong>A transition with real risk.</strong> Operators leaving a market have historically given short notice. A balance at a departing operator is a balance you may struggle to recover.</li>
</ul>
<div class="note"><b>What we would do between now and December 2026</b>
<p>Keep balances working rather than parked. Withdraw winnings as you make them. Keep verification current at every site you hold an account with, so a withdrawal request can never be stalled at short notice. And check our <a href="/nz-online-casino-law/">NZ online casino law page</a> before opening a new account late in the year &mdash; we update it as each DIA announcement lands.</p></div>
<h3>What does not change</h3>
<p>Tax treatment is unaffected: recreational gambling winnings remain outside the income tax net, with the narrow exceptions covered in our <a href="/gambling-winnings-tax-nz/">tax guide</a>. The minimum age remains 18 for online play and 20 for a physical casino venue. And the Gambling Helpline remains free and confidential on <a href="tel:0800654655">0800 654 655</a>.</p>
</div></div></section>
''')

    o.append(f'''<section class="sec"><div class="wrap">
<div class="sec-head"><span class="kicker">Games</span><h2>What you will find in a New Zealand-facing casino lobby</h2></div>
{table(["Category","Share of lobby","Typical RTP","House edge","Best for"], [
 ["Online pokies","85–90%","94–97.5%","2.5–6%","Volume of choice, jackpots, free spin features"],
 ["Blackjack","2–4%","99–99.6% at optimal play","0.4–1%","The longest play from a fixed bankroll"],
 ["Roulette (French)","1–2%","98.65%","1.35%","Low edge with simple rules — better than European, far better than American"],
 ["Roulette (European)","2–3%","97.3%","2.7%","The default. Avoid American (94.7%) wherever both are offered"],
 ["Baccarat","1–2%","98.9% on banker","1.06%","Simplicity — almost no decisions to get wrong"],
 ["Video poker","1–2%","98–99.5%","0.5–2%","Skill-responsive play with a very low edge on full-pay tables"],
 ["Live dealer","5–8%","Same as the table game","Varies","Atmosphere and trust — you watch the cards being dealt"],
 ["Crash / instant win","2–5%","96–99%","1–4%","Fast, high-variance sessions. Often excluded from bonus wagering"],
], minw=800)}
<p style="font-size:.86rem;color:var(--mute)">House edge is the long-run expected cost per dollar wagered. It is not a prediction of any single session, and no game on this table has a strategy that overcomes it.</p>
</div></section>
''')

    o.append(band("New to this?",
                  "Our methodology page explains exactly how each score is built, what we test, what disqualifies "
                  "an operator, and how we handle the commercial relationships that fund the testing.",
                  "How we review", "/how-we-review/"))

    o.append(rg_block())
    o.append(faq_block(FAQ, "Online casinos NZ: common questions"))
    o.append('<section class="sec"><div class="wrap"><div class="prose prose--wide">'
             + authorbox("tama-whitiora") + '</div></div></section>')
    o.append(footer())
    return write(PATH, "".join(o))
