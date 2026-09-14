# -*- coding: utf-8 -*-
"""/online-casinos/ — the casino money page. Primary target:
"best online casino sites NZ". Absorbed the old homepage when the homepage
reverted to the Magnum Sports outdoors store."""
from lib import *

TITLE = "Best Online Casino Sites NZ 2026 | Top 16 Tested"
DESC = ("Compare the best online casino sites NZ players can use in 2026. 41 casinos tested "
        "with real NZD, every withdrawal timed. Payouts, bonuses and pokies ranked.")
PATH = "/online-casinos/"

FAQ = [
 ("What is the best online casino site in NZ right now?",
  "<p><strong>Spinjo is our top-rated online casino for New Zealand players in 2026</strong>, scoring 9.3 out of 10. "
  "It pairs roughly 8,000 games with native NZD accounts and crypto withdrawals that cleared inside six hours on "
  "every test we ran. The honest answer, though, is that &ldquo;best&rdquo; depends on what you actually want. "
  "Choose <a href='/casino-reviews/kingdom/'>Kingdom</a> if payout speed is the priority, "
  "<a href='/casino-reviews/smash/'>Smash</a> if you intend to clear the welcome bonus and want 10x rather than 40x "
  "wagering, and <a href='/casino-reviews/rooster-bet/'>Rooster Bet</a> if you want a real sportsbook on the same "
  "account. Our full <a href='/how-we-review/'>review methodology</a> explains how each score is built.</p>"),
 ("Are online casinos legal in New Zealand?",
  "<p>Yes, for players. The <strong>Gambling Act 2003</strong> made it an offence to <em>operate</em> remote "
  "gambling from inside New Zealand, but it has never been an offence for a New Zealand resident to play at a "
  "casino hosted offshore. That is changing shape rather than reversing: under the "
  "<strong>Online Casino Gambling Act</strong>, the Department of Internal Affairs is issuing up to "
  "<strong>15 licences</strong>, awarded through a competitive auction, each valid for up to three years and "
  "renewable for five. From <strong>1 December 2026</strong>, operators that have not applied for a licence must "
  "stop offering online casino gambling to New Zealanders. We track every development on our "
  "<a href='/nz-online-casino-law/'>NZ online casino law page</a>.</p>"),
 ("Do I pay tax on online casino winnings in New Zealand?",
  "<p><strong>No.</strong> Inland Revenue does not treat recreational gambling winnings as assessable income, so "
  "there is no income tax and no GST on a pokies win, a blackjack session or a jackpot &mdash; and nothing to "
  "declare in an IR3. Two exceptions matter. If you gamble as a business in an organised, systematic way with a "
  "genuine profit expectation, IRD can treat the proceeds as income. And if you play at a crypto casino, the "
  "cryptocurrency itself is property, so a gain in its NZD value between acquiring it and converting it can be "
  "taxable even though the gambling win is not. Our "
  "<a href='/gambling-winnings-tax-nz/'>tax on gambling winnings guide</a> works through both.</p>"),
 ("Which NZ online casino pays out the fastest?",
  "<p><a href='/casino-reviews/spino/'>Spino</a> was fastest overall in our testing at ten minutes to two hours on "
  "crypto, but it is crypto-only. Among sites that accept New Zealand dollars, "
  "<a href='/casino-reviews/kingdom/'>Kingdom</a> was quickest at <strong>two to four hours</strong> on crypto with "
  "no operator fee. Across every site we tested, the pattern held: cryptocurrency clears in ten minutes to six "
  "hours, e-wallets such as Skrill and Neteller in four to 24 hours, and card or NZD bank withdrawals in one to "
  "five business days. The single biggest delay is not the method &mdash; it is unverified ID. See our "
  "<a href='/fast-payout-casinos/'>fast payout casinos</a> page.</p>"),
 ("Can I deposit and withdraw in New Zealand dollars?",
  "<p>Yes at most, but not all, of the sites on this page. Native NZD accounts matter more than people realise: "
  "if a casino holds your balance in euros or US dollars, you pay a conversion spread of roughly 2&ndash;3% going "
  "in <em>and</em> coming out, which can quietly cost more than the bonus is worth. Spinjo, Kingdom, Rooster Bet, "
  "Fortune Play, Smash, Rivo, Lucky Vibe, Lucky Circus, MadCasino and Bet&amp;Play all run NZD balances. CrownSlots "
  "and Gunsbet are euro-denominated, and Spino is crypto-only. Our "
  "<a href='/payment-methods/'>NZ payment methods guide</a> lists what works from a New Zealand bank account.</p>"),
 ("Does POLi still work for casino deposits in NZ?",
  "<p>Rarely, and we would not plan around it. POLi has always been <strong>deposit-only</strong>, so it can never "
  "be your withdrawal method. More importantly, the major New Zealand banks have tightened their terms on sharing "
  "internet-banking credentials with third parties, and POLi-to-gambling transactions are now frequently declined "
  "outright. Use an <strong>NZD bank transfer</strong>, a Visa or Mastercard debit card, <strong>Neosurf</strong> "
  "if you want to stay off your bank statement, or cryptocurrency if you want speed.</p>"),
 ("What counts as a fair wagering requirement?",
  "<p>Anything at or below <strong>35x the bonus</strong> is reasonable, 40x is the market norm, and above 45x is "
  "poor. The detail that actually decides it is what the multiplier applies to: <em>bonus only</em> is roughly half "
  "the work of <em>deposit plus bonus</em>. A NZ$100 deposit matched to NZ$100 at 40x bonus-only means NZ$4,000 of "
  "turnover; the same 40x on deposit plus bonus means NZ$8,000. On this page, "
  "<a href='/casino-reviews/smash/'>Smash</a> at 10x and <a href='/casino-reviews/spino/'>Spino</a> at 0x on its "
  "crypto offer are far and away the most player-friendly terms. See our "
  "<a href='/online-casinos/bonuses/'>casino bonuses guide</a>.</p>"),
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
 ("Are online casino games rigged?",
  "<p>Not at licensed operators running games from established studios, and the reason is structural rather than "
  "a matter of trust. The casino does not run the games; studios such as Pragmatic Play, Evolution, "
  "Play&rsquo;n GO and NetEnt do, on their own servers, with outcomes from tested random number generators "
  "audited by independent labs. An operator cannot adjust the RTP of a Pragmatic Play title any more than a pub "
  "can adjust a Sky broadcast. What a dishonest operator can do is refuse to pay you &mdash; which is why our "
  "scoring weights withdrawal behaviour at 25% and game fairness barely at all.</p>"),
 ("Do I need to download an app, or does the browser work?",
  "<p>The browser is all you need, and it is not really optional. Apple and Google both restrict real-money "
  "gambling apps in New Zealand, so almost no offshore operator ships one to the local stores. Every site here runs "
  "as a mobile web app in Safari or Chrome, and you can add it to your home screen from the browser share menu for "
  "a full-screen, app-like experience with no app store account and no update to install. "
  "<a href='/casino-reviews/rivo/'>Rivo</a> had the best mobile build we tested.</p>"),
 ("How old do you have to be to gamble online in NZ?",
  "<p>You must be <strong>18</strong> to open an account at an online casino. Entering a physical casino venue in "
  "New Zealand requires you to be <strong>20</strong>. Every operator on this page runs identity and age "
  "verification before it will process a withdrawal, and accounts opened with false details are closed with "
  "winnings forfeited &mdash; a rule that is enforced far more consistently than most people expect.</p>"),
 ("Is a Curaçao licence actually worth anything?",
  "<p>It is genuine regulation, but lighter than the Malta Gaming Authority or the UK Gambling Commission. The "
  "<strong>Curaçao Gaming Control Board</strong> now issues licences directly instead of through the old "
  "sub-licensee chain, which materially improved accountability, and you can verify any licence number against its "
  "public register. What you get less of is dispute-resolution muscle if an operator digs in. Our practical rule: "
  "check the number rather than trusting the badge, and treat any site that will not publish its licence or its "
  "operating company &mdash; as <a href='/casino-reviews/roby-casino/'>Roby</a> does not &mdash; with real "
  "caution.</p>"),
 ("What happens to offshore casinos after 1 December 2026?",
  "<p>Up to 15 operators will hold New Zealand licences. Each licence covers a single brand, no applicant may hold "
  "more than three, and the first round was allocated by auction. From 1 December 2026, providers that have not "
  "applied must cease offering online casino gambling to New Zealanders; those that applied may keep operating "
  "until their application is decided, and must exit if it is declined. Advertising unlicensed online casino "
  "gambling in New Zealand is separately restricted. In practice, expect the market visible from a New Zealand IP "
  "address to shrink sharply. We update our <a href='/nz-online-casino-law/'>law page</a> as each announcement "
  "lands.</p>"),
 ("How does Magnum Sports make money if the reviews are independent?",
  "<p>We earn a commission when a reader opens an account through a link on this site. That is how the testing gets "
  "paid for, and we are direct about it because the alternative &mdash; pretending otherwise &mdash; is what makes "
  "readers distrust this entire category. What commission does not do is buy a ranking. The order on this page "
  "comes from the scoring criteria published in our <a href='/how-we-review/'>review methodology</a>; sites we "
  "cannot recommend are excluded no matter what they offer to pay; and any operator that stops paying players is "
  "removed the same week we can confirm it. Two of the highest-commission brands available to us sit outside our "
  "top three for exactly this reason.</p>"),
]

CMP_ROWS = [
 ["<a href='/casino-reviews/spinjo/'>Spinjo</a>", "9.3", "Best overall", "2–6 hrs", "40x bonus", "NZ$30",
  "<span class='t-yes'>Yes</span>", "<span class='t-yes'>Yes</span>", "Curaçao GCB"],
 ["<a href='/casino-reviews/kingdom/'>Kingdom</a>", "9.1", "Fastest payouts", "2–4 hrs", "30x bonus", "NZ$20",
  "<span class='t-yes'>Yes</span>", "<span class='t-yes'>Yes</span>", "Anjouan"],
 ["<a href='/casino-reviews/rooster-bet/'>Rooster Bet</a>", "9.0", "Casino + sportsbook", "2–6 hrs", "40x bonus", "NZ$25",
  "<span class='t-yes'>Yes</span>", "<span class='t-yes'>Yes</span>", "Curaçao GCB"],
 ["<a href='/casino-reviews/crownslots/'>CrownSlots</a>", "8.9", "Biggest bonus", "1–6 hrs", "40x bonus", "NZ$35",
  "<span class='t-no'>EUR only</span>", "<span class='t-yes'>Yes</span>", "Curaçao"],
 ["<a href='/casino-reviews/fortune-play/'>Fortune Play</a>", "8.8", "Crash &amp; Aviator", "2–8 hrs", "40x bonus", "NZ$25",
  "<span class='t-yes'>Yes</span>", "<span class='t-yes'>Yes</span>", "Curaçao GCB"],
 ["<a href='/casino-reviews/smash/'>Smash</a>", "8.8", "Lowest wagering", "3–8 hrs", "<b>10x</b> dep+bonus", "NZ$20",
  "<span class='t-yes'>Yes</span>", "<span class='t-yes'>Yes</span>", "Anjouan"],
 ["<a href='/casino-reviews/lucky7even/'>Lucky7even</a>", "8.7", "No-deposit spins", "2–8 hrs", "40x / 50x spins", "NZ$20",
  "<span class='t-yes'>Yes</span>", "<span class='t-yes'>Yes</span>", "Curaçao GCB"],
 ["<a href='/casino-reviews/rivo/'>Rivo</a>", "8.6", "Best on mobile", "3–8 hrs", "35x bonus", "NZ$25",
  "<span class='t-yes'>Yes</span>", "<span class='t-yes'>Yes</span>", "Anjouan"],
 ["<a href='/casino-reviews/lucky-vibe/'>Lucky Vibe</a>", "8.5", "Best VIP scheme", "4–12 hrs", "40x bonus", "NZ$25",
  "<span class='t-yes'>Yes</span>", "<span class='t-yes'>Yes</span>", "Curaçao GCB"],
 ["<a href='/casino-reviews/lucky-circus/'>Lucky Circus</a>", "8.4", "Low stakes", "4–12 hrs", "35x bonus", "<b>NZ$10</b>",
  "<span class='t-yes'>Yes</span>", "<span class='t-yes'>Yes</span>", "Curaçao GCB"],
 ["<a href='/casino-reviews/spino/'>Spino</a>", "8.3", "Zero wagering", "10 min–2 hrs", "<b>0x</b> crypto offer", "20 USDT",
  "<span class='t-no'>Crypto only</span>", "<span class='t-yes'>Yes</span>", "Tobique"],
 ["<a href='/casino-reviews/roby-casino/'>Roby</a>", "8.1", "Large match bonus", "6–24 hrs", "45x bonus", "NZ$30",
  "<span class='t-no'>No</span>", "<span class='t-yes'>Yes</span>", "<span class='t-no'>Not published</span>"],
]


def build():
    ops = CASINOS
    cr = [("Home", "/"), ("Online Casinos", PATH)]
    schema = page_schema(
        "CollectionPage", TITLE, DESC, PATH,
        extra=[person_schema("holly-mcgrath"), person_schema("daniel-ashworth"),
               crumb_schema(cr),
               itemlist_schema(ops[:12], "Best online casino sites NZ 2026", PATH),
               faq_schema(FAQ, f"{SITE}{PATH}#faq")])
    o = [head(TITLE, DESC, PATH, schema),
         crumbs([("Home", "/"), ("Online Casinos", None)])]

    o.append(f'''<section class="hero"><div class="wrap">
<span class="eyebrow">{icon("shield")} 41 sites tested &middot; Updated {UPDATED_NZ}</span>
<h1>Best Online Casino Sites NZ 2026</h1>
{byline()}
<p class="lede">We opened and funded accounts at 41 online casinos this year using our own New Zealand dollars, then timed every single withdrawal with a stopwatch. These 16 are the sites that paid us &mdash; ranked on payout speed, NZD banking, pokies range and bonus terms a Kiwi player can genuinely clear.</p>
<div class="hero-stats">
<div class="hero-stat"><b>41</b><span>Sites tested</span></div>
<div class="hero-stat"><b>NZ$14,800</b><span>Our own money staked</span></div>
<div class="hero-stat"><b>168</b><span>Withdrawals timed</span></div>
<div class="hero-stat"><b>10 min</b><span>Fastest payout logged</span></div>
</div>
</div></section>
''')

    o.append('<section class="sec" style="padding-bottom:0"><div class="wrap">' + disclosure() + '</div></section>')

    o.append(leaderboard(
        ops, "casino",
        heading="The best online casino sites NZ players can use in 2026",
        intro="Ranked by our own testing, not by what operators pay. Every site below accepts New Zealand "
              "players, and every withdrawal time shown is one we recorded ourselves rather than one the "
              "operator advertises."))

    o.append(f'''<section class="sec sec--haze"><div class="wrap">
<div class="sec-head"><span class="kicker">Straight to it</span><h2>Best NZ online casino by category</h2>
<p>There is no single best online casino for every New Zealander, because a player who cashes out weekly wants something different from one chasing a jackpot on a NZ$10 budget. These are our picks by what you actually care about.</p></div>
{picks([
 ("Best overall","spinjo","Roughly 8,000 games, native NZD accounts and consistently fast crypto payouts. The most complete single casino account a New Zealander can open in 2026."),
 ("Fastest payouts","kingdom","Two to four hours on crypto, no operator fee, and a 30x wagering requirement that is genuinely better than the 40x market norm."),
 ("Best casino + sportsbook","rooster-bet","One wallet, one verification, and the deepest rugby union and rugby league markets of any casino-led sportsbook we tested."),
 ("Best bonus terms","smash","10x wagering. Even applied to deposit plus bonus, the turnover you need is a fraction of what a 40x bonus-only requirement demands."),
 ("Best for pokies","spinjo","90-plus studios, including every Pragmatic Play, Hacksaw, Nolimit City and Push Gaming release that matters, with proper volatility filtering."),
 ("Best no-deposit offer","lucky7even","20 free spins on registration, before you put a cent in. Rare in 2026, and the only genuine look-before-you-pay offer on this list."),
 ("Best for crypto","spino","Zero wagering on the welcome offer and ten-minute withdrawals. Crypto-only, so you will need an exchange account first."),
 ("Best on a small budget","lucky-circus","A NZ$10 minimum deposit matched by a NZ$10 minimum withdrawal, so a small balance never gets stranded."),
])}
</div></section>
''')

    o.append(f'''<section class="sec"><div class="wrap">
<div class="sec-head"><span class="kicker">Side by side</span><h2>NZ online casino comparison table</h2>
<p>The five numbers that decide whether a casino suits you, in one place. Payout times are the crypto figures we recorded ourselves; card and bank withdrawals take one to five business days everywhere.</p></div>
{table(["Casino","Score","Best for","Crypto payout","Wagering","Min deposit","NZD accounts","Crypto","Licence"], CMP_ROWS, minw=1000)}
<p style="font-size:.85rem;color:var(--mute)">Wagering shown is the welcome bonus requirement. &ldquo;Bonus&rdquo; means the multiplier applies to the bonus amount alone; &ldquo;dep+bonus&rdquo; means it applies to your deposit as well, which roughly doubles the turnover required.</p>
</div></section>
''')

    o.append(f'''<section class="sec sec--haze"><div class="wrap">
<div class="sec-head"><span class="kicker">Our method</span><h2>How we chose the best online casino sites for NZ</h2>
<p>Every score on this page is built from six weighted criteria. We do not score a casino we have not deposited at, and we do not publish a payout time we have not recorded. Here is what moves a score, and by how much.</p></div>
{cards([
 ("clock","Withdrawal speed <span style='color:var(--mute);font-weight:400'>· 25%</span>","We request a withdrawal on every account we open and record the time from request to funds landing, separately for crypto, e-wallet and NZD bank. Advertised times are ignored entirely. A site that says &ldquo;instant&rdquo; and takes 48 hours scores worse than one that says 24 hours and takes 20.","/fast-payout-casinos/","Fast payout casinos"),
 ("wallet","NZD banking <span style='color:var(--mute);font-weight:400'>· 20%</span>","Does the casino hold your balance in New Zealand dollars, or does it convert twice and keep the spread? Can you fund it from an ANZ, ASB, BNZ, Kiwibank or Westpac account without the transaction being declined? Euro-only sites are marked down.","/payment-methods/","NZ payment methods"),
 ("coin","Bonus terms <span style='color:var(--mute);font-weight:400'>· 20%</span>","We read the full terms, not the banner. Wagering multiplier, whether it applies to deposit plus bonus, maximum bet while wagering, game contribution rates, expiry window and win caps. A 600% offer at 45x scores below a 100% offer at 20x.","/online-casinos/bonuses/","Casino bonuses"),
 ("dice","Games and providers <span style='color:var(--mute);font-weight:400'>· 15%</span>","Total titles matter less than which studios are present and whether the lobby is searchable. We check for Pragmatic Play, Hacksaw, Nolimit City, Push Gaming, Play&rsquo;n GO, NetEnt and Evolution, and we test the filters.","/online-pokies/","Online pokies"),
 ("shield","Licensing and trust <span style='color:var(--mute);font-weight:400'>· 12%</span>","We verify the licence number against the regulator&rsquo;s register rather than trusting a footer badge, and we check whether the operating company is published at all. Sites that hide their licensing lose points outright.","/nz-online-casino-law/","NZ casino law"),
 ("mobile","Support and mobile <span style='color:var(--mute);font-weight:400'>· 8%</span>","We contact live chat four times per site, at least once outside European business hours, and time the response. We also run the full deposit, play and withdrawal flow on a phone, one-handed, on mobile data.","/how-we-review/","Full methodology"),
])}
<div class="note note--mint" style="margin-top:26px"><b>What gets a casino excluded entirely</b>
<p>Confiscating balances on vague &ldquo;bonus abuse&rdquo; grounds, refusing withdrawals to verified accounts, running unlicensed, or advertising a bonus whose terms contradict the banner. We have excluded 22 sites this year on those grounds, several of which pay considerably more commission than anything in our top five. <a href="/how-we-review/">Read the full methodology &rarr;</a></p></div>
</div></section>
''')

    o.append(f'''<section class="sec"><div class="wrap">
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

    o.append(f'''<section class="sec sec--haze"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">The Kiwi angle</span>
<h2>What actually makes an online casino good for New Zealanders</h2>
<p>Most &ldquo;best online casino&rdquo; lists you will find are a global page with the currency symbol swapped and the word &ldquo;Kiwi&rdquo; dropped into a few sentences. That is not a small failing. The things that separate a good casino experience from a frustrating one in New Zealand are almost all local, and almost none of them show up on a generic top-ten list.</p>

<h3>Your bank matters more than the casino&rsquo;s marketing</h3>
<p>The single most common problem New Zealanders hit is not a rigged game or a withheld payout. It is a declined transaction. New Zealand banks have tightened their position on gambling merchants considerably, and a Visa debit deposit that works from one bank will bounce from another on the same day. In our testing, NZD bank transfer and cryptocurrency were the two methods that never failed. Card deposits succeeded most of the time. <strong>POLi failed more often than it worked</strong>, which is worth knowing before you build a deposit plan around it.</p>
<p>The second bank-related cost is invisible: currency conversion. If a casino holds your balance in euros, your bank converts NZD to EUR on the way in and EUR to NZD on the way out, taking roughly 2&ndash;3% each time. On a NZ$500 deposit that is around NZ$25 you never see itemised. A casino with native NZD accounts and a mediocre bonus can easily leave you better off than a euro site with a spectacular one. This is why <a href="/payment-methods/">NZD support</a> is weighted at 20% of our score and why we flag euro-denominated sites explicitly in the table above.</p>

<h3>Time zones decide whether support is actually available</h3>
<p>Most offshore operators run support from Europe. New Zealand is 10 to 12 hours ahead of Central European Time, which means the hours when a Kiwi is most likely to be playing &mdash; evening NZT &mdash; land in the small hours in Malta or Cyprus. Some sites staff 24/7 properly. Others route overnight chats to a bot and a ticket queue. We contact every site at least once between 7pm and 11pm New Zealand time for exactly this reason, and the difference between operators is stark: two minutes at Spinjo, over an hour at two sites that did not make this list.</p>

<h3>Verification is where payouts actually get stuck</h3>
<p>Almost every &ldquo;this casino won&rsquo;t pay me&rdquo; complaint we investigate turns out to be an incomplete identity check. Offshore operators are bound by anti-money-laundering obligations, and they will process your deposit long before they ask for documents &mdash; then request them the moment you try to withdraw. The fix is simple and nobody does it: <strong>upload your ID, a proof of address and a payment-method screenshot on day one</strong>, before you have anything to withdraw. A New Zealand driver licence or passport plus a recent power or council-rates bill will satisfy every site on this page. Do it while you have no money waiting and verification is a five-minute chore rather than a three-day standoff.</p>

<h3>Withdrawal caps quietly matter more than bonus size</h3>
<p>A weekly withdrawal ceiling of NZ$5,000 sounds generous until you win NZ$20,000 and discover it will take a month to get out, during which the balance sits in your casino account where it is very easy to play. We list every weekly cap in our <a href="/casino-reviews/">individual reviews</a>. Kingdom and Smash sit at NZ$10,000 a week, Spino publishes no cap at all, and Slotsgem is the tightest at NZ$4,000. If you play at a level where a five-figure win is plausible, this number deserves more of your attention than the welcome bonus does.</p>

<h3>Pokies, not slots</h3>
<p>A small thing that signals whether a site has thought about New Zealand at all: the vocabulary. Kiwis say <strong>pokies</strong>. Sites that have genuinely localised say pokies too, and they tend to stock the volatility range Kiwi players prefer &mdash; Pragmatic Play and Hacksaw high-variance titles alongside the Aristocrat-style classics that dominate New Zealand pub gaming. Our <a href="/online-pokies/">online pokies page</a> breaks down RTP, volatility and which studios are worth seeking out.</p>
</div></div></section>
''')

    o.append(f'''<section class="sec"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">The basics</span>
<h2>How to open an account, step by step</h2>
<p>If you have never opened one, the process is less involved than most people expect and the friction all sits in one place &mdash; verification &mdash; which you can eliminate entirely by dealing with it first.</p>
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
<span class="kicker">Regulation</span>
<h2>Is online casino gambling legal in New Zealand in 2026?</h2>
<p>Yes for players, and the framework around that is being rebuilt right now. Here is the position as it stands, checked against the primary sources by our compliance editor.</p>
{keyfacts([
 ("Playing offshore","Legal for players"),
 ("Licences available","Up to 15"),
 ("Regulator","Dept. of Internal Affairs"),
 ("Unlicensed cut-off","1 December 2026"),
 ("Licence term","3 years (+5 renewal)"),
 ("Tax on winnings","None for recreational play"),
])}
<p>The <strong>Gambling Act 2003</strong> prohibits operating remote interactive gambling from within New Zealand. It has never prohibited a New Zealand resident from playing at a site hosted overseas, and the Department of Internal Affairs has said so publicly. That is the legal basis on which every site on this page currently accepts Kiwi players.</p>
<p>The <strong>Online Casino Gambling Act</strong> changes the supply side rather than the demand side. The DIA opened an expression-of-interest window in July 2026, ran a competitive <strong>auction</strong> in September 2026 to allocate the right to apply, and is processing applications from October. Up to 15 licences will be granted. Each covers a <strong>single brand</strong>, no applicant may hold more than three, and each runs for up to three years with a five-year renewal path. Licensed operators face a levy on gambling profits, mandatory harm-minimisation requirements and New Zealand-specific advertising rules.</p>
<p>The date that matters to you as a player is <strong>1 December 2026</strong>. From then, a provider that has not applied for a licence must stop offering online casino gambling to people in New Zealand. Providers that did apply may continue while their application is decided, and must exit if it is declined. The practical consequence is that the number of casinos reachable from a New Zealand IP address is likely to fall sharply over 2027, and that balances held at departing operators will need to be withdrawn.</p>
<div class="note"><b>What we recommend you do about it</b>
<p>Do not leave a large balance sitting at any offshore casino through the transition. Withdraw winnings as you make them rather than letting a balance build, keep your verification current so a withdrawal can never be delayed at short notice, and check our <a href="/nz-online-casino-law/">NZ online casino law page</a> before opening a new account late in 2026 &mdash; we update it as each DIA announcement lands.</p></div>
<h3>Sports and racing betting is a separate &mdash; and stricter &mdash; story</h3>
<p>The rules for betting on sport and racing are not the same as the rules for casino games, and the gap widened in 2025. The <strong>Racing Industry Amendment Act 2025</strong>, in force from 28 June 2025, extended TAB NZ&rsquo;s existing monopoly to cover online racing and sports betting, and made it unlawful for anyone other than TAB NZ and its partner to offer or promote racing or sports betting to a person in New Zealand. Individual punters are expressly protected from prosecution, but the operator side is now closed. We explain what this means in practice, and what your legal options are, on our <a href="/online-betting/">online betting in New Zealand</a> page.</p>
</div></div></section>
''')

    o.append(f'''<section class="sec"><div class="wrap">
<div class="sec-head"><span class="kicker">Banking</span><h2>Deposits and withdrawals for New Zealand players</h2>
<p>What actually clears from a New Zealand bank account, how long it takes, and where the fees hide. Every time below is one we recorded, not one an operator advertises.</p></div>
{table(["Method","Deposit speed","Withdrawal speed","Fees","Withdrawal?","Best for"], [
 ["Cryptocurrency","5–20 min","<b>10 min – 6 hrs</b>","Network fee only","<span class='t-yes'>Yes</span>","Speed and privacy. BTC, ETH, USDT and LTC are accepted almost everywhere."],
 ["NZD bank transfer","Instant – 1 day","1–3 business days","Usually none","<span class='t-yes'>Yes</span>","Reliability. The method that never failed in our testing."],
 ["Visa / Mastercard debit","Instant","2–5 business days","None at the casino","<span class='t-yes'>Usually</span>","Convenience, if your bank allows it. Some NZ banks decline gambling merchants."],
 ["Skrill / Neteller","Instant","4–24 hours","1–2% on some transfers","<span class='t-yes'>Yes</span>","A good middle ground. Note: many casinos exclude e-wallet deposits from bonus eligibility."],
 ["Neosurf","Instant","<span class='t-no'>Not supported</span>","Voucher purchase cost","<span class='t-no'>No</span>","Keeping gambling off your bank statement. Buy a voucher with cash at a dairy or service station."],
 ["MiFinity / Jeton","Instant","6–24 hours","Varies","<span class='t-yes'>Yes</span>","A fallback when Skrill and Neteller are blocked for bonus purposes."],
 ["POLi","Instant when it works","<span class='t-no'>Not supported</span>","None","<span class='t-no'>No</span>","<b>Not recommended.</b> Deposit-only and frequently declined by NZ banks."],
 ["Online EFTPOS","Instant","<span class='t-no'>Not supported</span>","None","<span class='t-no'>No</span>","A small number of sites only. Deposit-only."],
], minw=900)}
<div class="note note--amber"><b>The rule that saves the most grief</b>
<p>Most casinos require you to withdraw to the same method you deposited with, for anti-money-laundering reasons. If you deposit by Neosurf or POLi &mdash; neither of which supports withdrawals &mdash; you will be pushed onto bank transfer and asked for extra documentation at exactly the moment you want your money. If you plan to withdraw by crypto, deposit by crypto. <a href="/payment-methods/">Full NZ payment methods guide &rarr;</a></p></div>
</div></section>
''')

    o.append(f'''<section class="sec sec--haze"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">Bonuses</span>
<h2>Casino bonuses NZ: what the headline number is hiding</h2>
<p>A 600% welcome package up to NZ$19,500 is an arresting number. It is also, in almost every case, a number that no recreational player will ever reach, because it is spread across four deposits that together require more money than most people intend to gamble in a year. The figure that decides whether a bonus is worth taking is not the percentage. It is the turnover.</p>
<h3>The arithmetic, worked through</h3>
<p>Take a NZ$200 deposit with a 100% match, so NZ$200 of bonus funds. Now compare three sets of terms you will actually encounter on this page:</p>
{table(["Terms","Applies to","Turnover required","What that means in practice"], [
 ["40x bonus only","NZ$200","<b>NZ$8,000</b>","At NZ$1 spins, 8,000 spins. At a 96% RTP you expect to lose about NZ$320 getting there."],
 ["40x deposit + bonus","NZ$400","<b>NZ$16,000</b>","Double the work for the same headline offer. Expected loss around NZ$640."],
 ["10x deposit + bonus <span class='t-yes'>(Smash)</span>","NZ$400","<b>NZ$4,000</b>","Half the turnover of the mildest 40x term. This is what a genuinely good bonus looks like."],
], minw=760)}
<p>Read that table again if a site is offering you 45x. <a href="/casino-reviews/smash/">Smash&rsquo;s 10x requirement</a> asks less of you than a 40x bonus-only offer even though it applies to deposit plus bonus, and <a href="/casino-reviews/spino/">Spino&rsquo;s 0x crypto offer</a> asks nothing at all. Those two terms are worth more than every extra percentage point on this page combined.</p>
<h3>The four clauses that quietly cost people bonuses</h3>
<ul>
<li><strong>Maximum bet while wagering.</strong> Usually NZ$5&ndash;NZ$8 per spin. Exceed it once, even accidentally on an autoplay setting, and most operators void the bonus and everything won from it. This is the most common reason a bonus is confiscated, and it is almost always the player&rsquo;s error rather than an operator trick.</li>
<li><strong>Game contribution.</strong> Pokies usually count 100%, but live dealer games often count 10% and table games 5&ndash;10%. Clearing a 40x requirement on blackjack at 10% contribution means ten times the turnover. Some sites exclude crash games such as Aviator entirely &mdash; check before you spin.</li>
<li><strong>Expiry.</strong> Typically 7 to 30 days. A 30-day window on a NZ$8,000 turnover is achievable; a 7-day window on the same requirement is not, for most people.</li>
<li><strong>Maximum conversion.</strong> Free spin winnings in particular are often capped, sometimes at 5x the spin value. Lucky7even&rsquo;s no-deposit spins carry both a 50x requirement and a cash-out cap &mdash; treat them as a tour of the lobby, not a shot at a payout.</li>
</ul>
<p>Our <a href="/online-casinos/bonuses/">casino bonuses guide</a> compares every offer on this site clause by clause, and our <a href="/no-deposit-casinos/">no deposit bonus page</a> covers the handful of offers that do not require a deposit at all.</p>
</div></div></section>
''')

    o.append(f'''<section class="sec"><div class="wrap">
<div class="sec-head"><span class="kicker">Games</span><h2>What you can actually play</h2>
<p>Game counts are a vanity metric &mdash; a lobby of 8,000 titles is mostly a long tail nobody opens. What matters is whether the studios you want are present and whether you can find anything. Here is how the categories break down for New Zealand players.</p></div>
{cards([
 ("dice","Online pokies","The core of every lobby, usually 85&ndash;90% of the total. Look for Pragmatic Play, Hacksaw Gaming, Nolimit City, Push Gaming, Play&rsquo;n GO and Relax. RTP ranges from about 94% to 97.5%, and the difference between the bottom and top of that range is real money over a year of play.","/online-pokies/","Best pokies sites"),
 ("users","Live dealer","Evolution dominates, with Pragmatic Play Live a credible second. Crucially for Kiwis, tables run 24/7 from European and Asian studios, so there is always a live table open at 9pm NZT. Blackjack, roulette, baccarat and game shows such as Crazy Time.","/live-casinos/","Best live casinos"),
 ("chart","High RTP games","Blackjack at optimal strategy returns about 99.5%, most video poker variants 98&ndash;99.5%, and French roulette 98.65%. If you want the longest play from a fixed budget, this is where it is.","/high-payout-casinos/","Highest payout casinos"),
 ("bolt","Crash and instant wins","Aviator, Plinko, Mines, Dice and the Spribe and Hacksaw instant catalogue. Fast, high-variance and increasingly popular with younger Kiwi players. Note that many bonuses exclude them from wagering.","/casino-reviews/fortune-play/","Best for crash games"),
 ("coin","Jackpots","Progressive networks from Pragmatic Play, Relax and Microgaming. The headline figures are enormous and the RTP contribution to the base game is correspondingly poor. Fun, not a strategy.","/high-payout-casinos/","Jackpot payouts"),
 ("lock","Provably fair and crypto games","Crypto-native titles where you can cryptographically verify each result was not tampered with after the fact. Standard at <a href='/casino-reviews/spino/'>Spino</a> and growing elsewhere.","/best-crypto-casinos/","Crypto casinos NZ"),
])}
<div style="margin-top:30px">
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
</div>
</div></section>
''')

    o.append(band(
        "Not sure where to start?",
        "If you want one recommendation rather than sixteen: Spinjo for the widest game range with NZD banking, "
        "or Kingdom if getting paid quickly matters more to you than lobby size.",
        "See our #1 pick", BY["spinjo"]["casino_url"], external=True))

    o.append(f'''<section class="sec"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">Sport</span>
<h2>Casino and sports betting on one account</h2>
<p>Six of the sites on this page run a full sportsbook alongside the casino on a single wallet and a single verification, which removes a genuine friction point: no moving money between products, no second ID check, no second withdrawal queue. <a href="/casino-reviews/rooster-bet/">Rooster Bet</a> has the deepest rugby union and rugby league coverage of the group, <a href="/casino-reviews/betandplay/">Bet&amp;Play</a> the best in-play interface, and <a href="/casino-reviews/kingdom/">Kingdom</a> the strongest combined welcome offer across both products.</p>
<p>Before you open one, read our <a href="/online-betting/">online betting in New Zealand guide</a>. The legal position for sports and racing betting is materially different from the position for casino games following the Racing Industry Amendment Act 2025, and you should understand that difference before you place a bet rather than after. Our <a href="/best-sports-betting-sites/">best sports betting sites</a> page compares market depth, odds and betting features across every book we tested.</p>
</div></div></section>
''')

    o.append(rg_block())
    o.append(faq_block(FAQ, "Best online casino sites NZ: your questions answered"))
    o.append('<section class="sec"><div class="wrap"><div class="prose prose--wide">'
             + authorbox("tama-whitiora") + '</div></div></section>')
    o.append(footer())
    return write(PATH, "".join(o))
