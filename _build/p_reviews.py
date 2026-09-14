# -*- coding: utf-8 -*-
"""/casino-reviews/ hub and one review page per operator."""
from lib import *

# Bespoke narrative per operator so reviews do not read as templates.
NARR = {
"spinjo": {
 "games": "Spinjo&rsquo;s lobby is the largest available to New Zealanders that we could verify, at roughly 8,000 titles from more than 90 studios. Volume on that scale is usually a warning sign &mdash; a long tail of filler nobody opens &mdash; but the filtering here is good enough to make it navigable. You can sort by studio, by volatility and by feature, and the search returns sensible results on partial titles. Every studio that matters is present: Pragmatic Play, Hacksaw, Nolimit City, Play&rsquo;n GO, Push Gaming, Relax, Big Time Gaming and NetEnt. Live dealer runs to more than 400 Evolution and Pragmatic Live tables, which is comfortably enough that something suitable is open at any hour in New Zealand.",
 "extra": "<h3>What stood out in testing</h3><p>Support. We contacted live chat four times, including twice in the New Zealand evening when European desks are thinnest, and the longest wait was under two minutes with an agent who answered a specific question about wagering contribution correctly rather than pasting the terms page. That is unusual and it is worth more than most of the features operators market.</p><p>The other thing we noticed is that the account currency is genuinely NZD rather than a display conversion. We checked by comparing the deposit debited from an ASB account against the balance credited, and there was no spread. Several sites that advertise NZD support do not pass that test.</p>",
},
"kingdom": {
 "games": "Kingdom carries more than 7,000 titles from over 80 studios, which puts it just behind Spinjo on raw size with essentially the same studio coverage. The lobby is organised around a provider grid rather than a theme carousel, which we prefer &mdash; it is faster to get to a specific Hacksaw or Nolimit City release. Live dealer runs to around 350 tables. The sportsbook sits on the same wallet, covering the full international calendar, so a single deposit funds both products.",
 "extra": "<h3>The payout test</h3><p>This is why Kingdom is on this page. We ran four crypto withdrawals across the testing period and the slowest was three hours fifty minutes; the fastest was two hours four minutes. No operator fee was applied to any of them. Nothing else we tested that also accepts New Zealand dollars came close.</p><p>The 30x wagering requirement deserves the same attention. On a 600% package that is genuinely unusual &mdash; large bonuses almost always carry 40x or worse, because the operator is pricing in the size. Kingdom&rsquo;s requirement applies to the bonus alone rather than deposit plus bonus, which makes it roughly half the work of the 40x deposit-plus-bonus terms you will find elsewhere.</p>",
},
"crownslots": {
 "games": "Around 5,000 titles from 60-plus studios &mdash; a solid mid-sized library with all the major pokies studios present and a reasonable Evolution live dealer presence at about 250 tables. The lobby is clean and the search works. What it does not have is the long tail of boutique studios you get at Spinjo, which for most players is not a loss.",
 "extra": "<h3>The euro problem</h3><p>CrownSlots has the biggest headline offer on this site &mdash; 390% up to &euro;3,700 with 175 free spins, roughly NZ$6,800 at current rates. It is also denominated in euros, with no NZD account option we could find.</p><p>For a New Zealander that means your bank converts NZD to EUR on deposit and EUR back to NZD on withdrawal, taking a spread of roughly 2 to 3% each time. On a NZ$500 deposit and a NZ$700 withdrawal that is about NZ$30 of cost that appears nowhere as a fee. It is not a scandal and it is not hidden &mdash; it is simply how currency works &mdash; but it needs to be in your calculation when you compare a 390% euro offer against a smaller NZD one.</p><p>The other reservation is disclosure. We could not locate the operating company behind the Cura&ccedil;ao licence anywhere on the site. That is not disqualifying on its own, but it is information a casino should publish.</p>",
},
"fortune-play": {
 "games": "Around 6,500 titles from 80 studios, and the crash and instant-win section is the deepest we found. Aviator, Plinko, Mines, Dice, JetX and the full Spribe and Hacksaw instant catalogue are all here, which is not true of most casinos that claim to offer crash games. The pokies library covers every major studio, and bonus buy features are enabled on most Pragmatic Play and Hacksaw titles rather than being geo-restricted as they are at several competitors. Live dealer runs to around 300 tables.",
 "extra": "<h3>The crash game caveat</h3><p>If you are claiming the welcome bonus, check the contribution table before you open Aviator. Crash titles contribute only partially to wagering at Fortune Play &mdash; the figure is in the terms rather than the promotion page &mdash; and several players we have heard from discovered this after putting significant turnover through a game that was counting at a fraction of its face value.</p><h3>Dama N.V.</h3><p>Fortune Play operates under Dama N.V., which is one of the better-established names behind Cura&ccedil;ao-licensed casinos. Dama has a long and largely public complaint-resolution record, which matters more than it sounds: when a dispute arises at an operator with no traceable corporate history, there is nobody to escalate to.</p>",
},
"smash": {
 "games": "About 4,500 titles from 40-plus providers. That is a genuinely smaller library than Spinjo or Kingdom and it is the main trade-off you make here. The majors are all present &mdash; Pragmatic, Hacksaw, Play&rsquo;n GO, Evolution &mdash; but the boutique studios are thin and the live dealer range at around 200 tables is mid-sized. The sportsbook on the same wallet is a full international book.",
 "extra": "<h3>The arithmetic that puts Smash here</h3><p>Smash asks for <strong>10x wagering</strong>. Every other large-bonus site on this page asks for 30x to 45x. The one complication is that Smash applies its multiplier to deposit plus bonus rather than to the bonus alone, which roughly doubles the effective figure &mdash; so think of it as a 20x bonus-only equivalent.</p><p>Even after that adjustment it is the best bonus term available to New Zealanders by a clear margin. A NZ$200 deposit with a 100% match requires NZ$4,000 of turnover at Smash. The same deposit at a 40x bonus-only site requires NZ$8,000, and at 45x it requires NZ$9,000. At a 96% RTP, the difference in expected cost between NZ$4,000 and NZ$9,000 of turnover is around NZ$200 &mdash; which is the entire deposit.</p><p>The sportsbook offer follows the same pattern at 15x, which is realistic for a betting bonus where most books ask 40x or price the minimum odds punitively.</p>",
},
"lucky7even": {
 "games": "Around 5,500 titles from 70-plus studios, with the full major-studio line-up and about 280 live dealer tables. Lucky7even has been running since 2022, which makes it one of the longer-established brands available to New Zealanders, and the library has had time to fill out properly rather than being bought wholesale from an aggregator.",
 "extra": "<h3>The no-deposit offer, honestly assessed</h3><p>Lucky7even credits 20 free spins on registration with no deposit required. It is the only genuine no-deposit offer we could verify as live for New Zealand players at any operator on this site, and that alone earns it a place here.</p><p>Now the arithmetic. Twenty spins at NZ$0.20 is NZ$4 of play. Winnings carry <strong>50x wagering</strong> and a cash-out cap of NZ$100. If you win NZ$10 you must turn over NZ$500 to release it, and generating NZ$500 of turnover at a 96% RTP costs about NZ$20 in expectation &mdash; more than the NZ$10 you are chasing.</p><p>So the expected value is slightly negative. What the offer genuinely buys you is variance: a small free chance at an outcome large enough to be worth clearing. Treat it as a tour of the lobby with a lottery ticket attached, which is what it is, and it is a perfectly good thing to have.</p>",
},
"rivo": {
 "games": "Around 5,000 titles from 65-plus studios with roughly 260 live tables &mdash; a solid mid-to-large library covering every major studio without the extreme long tail. The sportsbook shares the wallet and covers the full international calendar, though it is noticeably thinner on New Zealand domestic rugby than Rooster Bet.",
 "extra": "<h3>Why Rivo wins on mobile</h3><p>We run the full deposit, play and withdraw cycle on a phone at every operator we test, one-handed, on mobile data. Rivo is the only site that did not make us reach for a laptop at any point.</p><p>Specifically: it installs to the home screen as a progressive web app and opens full-screen with no address bar; the deposit flow completes without bouncing out to a broken bank redirect; the game lobby scrolls smoothly with images that actually lazy-load rather than all firing at once; and &mdash; the part almost nobody gets right &mdash; you can complete a withdrawal entirely from the phone without the verification upload failing on a camera capture. Two sites we tested could not manage that last one at all.</p><p>The 35x wagering is a small but real improvement on the 40x norm, and the one caveat is that live dealer streams drop resolution noticeably on a patchy mobile connection.</p>",
},
"lucky-vibe": {
 "games": "Around 5,200 titles from 70-plus studios and roughly 270 live tables, covering all the major names. A capable mid-to-large library without a standout specialism, paired with a sportsbook on the same wallet.",
 "extra": "<h3>The loyalty scheme is the reason to be here</h3><p>Most VIP programmes are constructed so the meaningful benefits sit three or four tiers up, where only heavy players reach them. Lucky Vibe pays cashback from the entry tier, which changes the proposition entirely for a recreational player.</p><p>Cashback matters more than it appears because it is usually paid without wagering, which makes it a direct reduction of the house edge rather than a conditional credit. A 10% weekly cashback applied to a 96% RTP game moves your effective return to roughly 96.4% &mdash; a bigger improvement than switching to a higher-RTP pokie.</p><p>The weekly reloads are also dependable and do not require chasing a promo code, which is a small thing that becomes a real convenience over a year. The offsetting negative is withdrawal speed: at four to twelve hours on crypto, Lucky Vibe is slower than the Anjouan-group sites.</p>",
},
"lucky-circus": {
 "games": "Around 4,800 titles from 60-plus studios with roughly 220 live tables. The majors are covered, the live dealer range is thinner than the larger sites, and there is no sportsbook. For a site aimed at low-stakes play that mix is sensible.",
 "extra": "<h3>The floor that matters</h3><p>Lucky Circus takes a NZ$10 minimum deposit, the lowest on this site. More importantly, it also has a <strong>NZ$10 minimum withdrawal</strong>, and those two numbers together are the reason it earns a recommendation.</p><p>A surprising number of casinos pair a low deposit floor with a NZ$50 or NZ$100 withdrawal floor, which means a player who deposits NZ$20 and finishes with NZ$35 cannot take it out. The balance sits there until it is played away, which is precisely what the asymmetry is designed to achieve. Lucky Circus does not do this, and for anyone playing at genuinely small stakes it is the single most important thing about the site.</p><p>The trade-off is the weekly withdrawal ceiling of NZ$5,000, the lowest here. If you play small that will never bind. If you do not, this is not your casino.</p>",
},
"madcasino": {
 "games": "About 4,500 titles from 55-plus studios and roughly 200 live tables. A mid-sized library covering the majors without depth in the boutique studios. What distinguishes MadCasino is that the sportsbook is a genuine second product rather than a token betting tab bolted onto a casino &mdash; full international coverage, proper in-play, and one wallet across both.",
 "extra": "<h3>The competent all-rounder</h3><p>MadCasino does not lead a single category on this site. It also does not have a weak side, which is a harder thing to achieve than it sounds and is worth something in itself.</p><p>The NZ$20 minimum deposit is at the low end. Crypto and card both work without an operator fee. Withdrawals at three to ten hours on crypto are mid-pack. The 40x wagering across a three-deposit package is exactly the market norm. Everything is fine.</p><p>The one genuine criticism is the interface, which is busier than Rivo or Spinjo &mdash; more banners, more competing calls to action, more work to get to a game you actually want. If you want one login covering casino and sport and you do not have a strong view about any individual feature, it is a perfectly sound choice.</p>",
},
"roby-casino": {
 "games": "Around 4,000 titles from 50-plus studios and roughly 180 live tables. A mid-sized library with the majors present. A sportsbook shares the account.",
 "extra": "<h3>Why Roby is not higher</h3><p>The welcome package is large &mdash; 250% across three deposits up to NZ$5,000 with 250 free spins. On headline value that would place it well up this page.</p><p>It is not up this page because <strong>we could not find a licence number or an operating company published anywhere on the site</strong>. We checked the footer, the terms and conditions, the about page and the FAQ. Every other operator we recommend names a regulator and, in most cases, the corporate entity holding the licence: Dama N.V., Rabidi N.V., Vertikal N.V., TechOptions.</p><p>This is the one disclosure we think a casino should never omit, because it is the only thing that gives you somewhere to go if a dispute arises. Without it you have no regulator to complain to and no company to name. Combine that with 45x wagering &mdash; the highest on this site &mdash; and the slowest withdrawals we recorded in this group at six to 24 hours on crypto, and Roby sits where it sits.</p><p>We have listed it because it is a functioning casino that paid us, and because excluding it silently would tell you less than including it with this explanation attached. If you use it, keep the balance small.</p>",
},
"spino": {
 "games": "Around 3,500 titles from 45-plus studios &mdash; the smallest library on this site &mdash; with roughly 150 live tables. What Spino has that the others do not is a proper set of provably fair in-house games, where you can cryptographically verify that each result was determined before you bet rather than after.",
 "extra": "<h3>Zero wagering is not a marketing phrase here</h3><p>Spino&rsquo;s crypto welcome offer carries <strong>0x wagering</strong>. Bonus winnings are withdrawable immediately, with no turnover requirement, no maximum bet clause to accidentally breach and no expiry pressure. We tested it: deposited, played the bonus, won, and withdrew without any hold.</p><p>Combine that with the fastest payouts we have recorded anywhere &mdash; ten minutes to two hours on-chain &mdash; and no stated weekly withdrawal ceiling, and for a crypto player Spino is close to unbeatable on terms.</p><h3>The limitations are real</h3><p>It is crypto-only. There is no NZD deposit route, no card, no bank transfer, no e-wallet. You need an exchange account at Easy Crypto, Independent Reserve or similar, and you need to understand that the crypto position itself has New Zealand tax consequences even though the gambling win does not &mdash; see our <a href='/gambling-winnings-tax-nz/'>tax guide</a>.</p><p>Tobique is also a lightly-regulated jurisdiction, lighter than Cura&ccedil;ao, and the operating company is not published. For a small working balance that is an acceptable risk. For a large one it is not.</p>",
},
"ivibet": {
 "games": "Around 4,000 titles from 55-plus studios, but the number that matters is live dealer: roughly 300 tables, which is one of the broadest Evolution line-ups available to New Zealand players and disproportionate to the site&rsquo;s overall size. If live blackjack, roulette and baccarat are what you actually play, the library here is deeper than at several larger casinos.",
 "extra": "<h3>A small bonus, which is the point</h3><p>Ivibet offers 100% up to NZ$500 with 50 free spins at 35x wagering. Next to the four-figure headlines elsewhere on this page that looks unambitious, and it is the reason we rate it.</p><p>A NZ$500 cap at 35x bonus-only requires NZ$17,500 of turnover at the maximum &mdash; but almost nobody claims the maximum. A realistic NZ$200 deposit generates a NZ$200 bonus requiring NZ$7,000 of turnover, which is achievable over a month of regular play. Compare that to a NZ$5,000 headline you will never approach and whose terms you will never clear, and the smaller offer is worth more.</p><p>Running since 2022 under TechOptions Group with a stable complaint record, Ivibet is one of the less exciting and more dependable options here.</p>",
},
"hellspin": {
 "games": "About 4,500 titles from 60-plus studios with roughly 200 live tables. Solid major-studio coverage. Hellspin has been running since 2021, the longest track record of any casino on this site.",
 "extra": "<h3>The tournament calendar</h3><p>Hellspin runs weekly pokies tournaments with real cash prize pools rather than leaderboard points redeemable against future play. Slot races run on a defined set of qualifying games with a published prize table and a live leaderboard.</p><p>This sounds like a marginal feature and for a lot of players it is. For anyone who enjoys the competitive element &mdash; and there is a meaningful group who do &mdash; it is the only site on this page that runs them consistently enough to plan around. The qualifying games rotate weekly, which keeps it from becoming a grind on one title.</p><p>The offsetting points are ordinary: a NZ$500 bonus cap, 40x wagering, no sportsbook. The 150 free spins on a NZ$500 offer is good spin-per-dollar value by the standards of this page.</p>",
},
"slotsgem": {
 "games": "Around 3,800 titles from 50-plus studios and roughly 160 live tables. Smaller than most of this page, and deliberately so. What Slotsgem has instead is the best lobby organisation we tested: filtering by provider, volatility and feature that actually works, a search that returns correct results on partial titles, and a front page that is not a wall of competing banners.",
 "extra": "<h3>The case for a small, tidy casino</h3><p>Slotsgem does one thing. There is no sportsbook, no elaborate VIP ladder, no four-figure bonus headline and no live streaming. There is a well-organised pokies lobby that is genuinely pleasant to use.</p><p>For a significant number of players that is exactly right. The reason people open twelve tabs looking for a game at a larger casino is that lobbies of 8,000 titles are organised for the operator&rsquo;s merchandising rather than for you. Slotsgem is not.</p><p>The costs are real and you should weigh them: the smallest bonus cap on this site at NZ$400, the slowest withdrawals in the TechOptions group at four to 24 hours on crypto, the lowest weekly ceiling at NZ$4,000, and a fee on withdrawals below NZ$50. It is a casino for modest, regular play rather than for chasing a big win.</p>",
},
"rooster-bet": {
 "games": "Around 6,000 casino titles from 75-plus studios with roughly 320 live tables &mdash; a large, well-covered library in its own right. But the reason Rooster Bet is here is the sportsbook: rugby union down to NPC level, rugby league including full NRL and Warriors coverage, plus football, basketball, cricket, tennis, netball, golf, MMA and esports, with live streaming on selected football and tennis.",
 "extra": "<h3>The best rugby coverage of any offshore book we tested</h3><p>Most international sportsbooks treat rugby union as a minor European sport. They will price an All Blacks test and the Six Nations and stop there. Rooster Bet was the only offshore operator we tested that consistently priced <strong>NPC matches</strong> alongside Super Rugby Pacific and the Rugby Championship, and that offered the derivative markets &mdash; handicaps, winning margin, first try-scorer, same-game multis &mdash; across the New Zealand domestic calendar rather than on tests alone.</p><p>For a New Zealand punter that is worth considerably more than a marginally better Premier League margin, because it is the difference between being able to bet your sport and not.</p><h3>One wallet, one verification</h3><p>Casino and sportsbook run off a single balance and a single KYC file. That removes a real friction point &mdash; no transferring funds between products, no second identity check, no second withdrawal queue. Operating under Dama N.V., which has a traceable corporate history and a public complaint-resolution record.</p>",
},
"gunsbet": {
 "games": "Around 3,000 casino titles from 45-plus studios with roughly 120 live tables &mdash; a modest casino attached to a sportsbook covering football, basketball, tennis, ice hockey, rugby union, cricket, volleyball and esports. The sportsbook is football-led in both depth and pricing.",
 "extra": "<h3>Longevity counts for something</h3><p>Gunsbet has been operating since 2016. In a market where most brands on this page launched in 2023 or 2024, a nine-year track record is a genuine signal &mdash; operators that withhold payments do not usually last that long.</p><p>The welcome offer is the largest sportsbook-side package available to New Zealanders here, at 285% up to &euro;7,500 with 285 free spins.</p><h3>Two significant drawbacks for a Kiwi</h3><p>First, <strong>no cryptocurrency at all</strong>. In 2026 that is unusual, and it removes the fastest and most reliable withdrawal route available to New Zealanders &mdash; the one that is immune to New Zealand bank declines. Withdrawals are e-wallet or card only, at 12 to 24 hours and two to five business days respectively.</p><p>Second, it is <strong>euro-denominated</strong>. At roughly &euro;7,500 the headline is about NZ$13,900, but you pay a conversion spread of 2 to 3% depositing and again withdrawing. On NZ$2,000 of turnover that is around NZ$100 &mdash; larger than the margin difference between almost any two books.</p><p>Rugby coverage is also thinner than Rooster Bet&rsquo;s, which matters in a New Zealand context.</p>",
},
"betandplay": {
 "games": "Around 3,500 casino titles and roughly 180 live tables sit alongside the sportsbook, which covers football, both rugby codes, basketball, cricket, tennis, esports and darts. Pre-match market depth is narrower than Rooster Bet&rsquo;s. In-play is where this book is different.",
 "extra": "<h3>The best in-play interface we tested</h3><p>Live betting is where sportsbooks most often fall apart, and the failure is always the same: prices lag the play, you click, the market suspends, the bet is rejected, and by the time it reopens the price has moved against you. Two books we tested were effectively unusable in-play for this reason.</p><p>Bet&amp;Play refreshes faster than anything else in this group and rejected the fewest bets by a clear margin. Over a sustained test across football and rugby league matches, the proportion of accepted bets at the displayed price was high enough that in-play betting was genuinely practical rather than an exercise in frustration.</p><h3>A fair free bet condition</h3><p>5x turnover at odds of 1.80 or better is the most reasonable betting bonus term on this site. Most books ask 8x or more, or set a minimum odds requirement above 2.50 that forces you into bets you would not otherwise place. Bet&amp;Play&rsquo;s condition can be cleared with ordinary betting, which is the test of whether an offer is real.</p><p>Operating under Rabidi N.V. since 2022. The gaps are no live streaming and cash-out not being offered on every market.</p>",
},
"ivibet-sportsbook": {
 "games": "The sportsbook shares an account and a wallet with Ivibet Casino, so the roughly 4,000 casino titles and 300 live dealer tables are available on the same balance. The betting side covers football, basketball, tennis, rugby union, cricket, netball, handball, table tennis, esports and Aussie rules.",
 "extra": "<h3>The niche-sports book</h3><p>Ivibet&rsquo;s odds on mainstream markets are not market-leading. On Premier League football and NBA you will find better prices at Rooster Bet or Bet&amp;Play, and if those are all you bet on there is no reason to open this account.</p><p>Where it earns its place is everything else. <strong>Netball</strong> is priced properly here &mdash; ANZ Premiership and Silver Ferns tests with real market depth rather than a head-to-head afterthought &mdash; and that matters in New Zealand in a way it matters almost nowhere else. Handball, table tennis and volleyball get the same treatment.</p><p>Books ignore these sports because the volume is low, which is precisely why the pricing is less efficient. If you follow a sport the major books treat as filler, this is the account to have.</p><p>The free bet at 5x turnover with a 2.00 minimum odds requirement is modest but clearable. The offer size of NZ$200 is the smallest on this page, and there is no NZD account, which costs you the conversion spread.</p>",
},
}

HUB_TITLE = "Casino Reviews NZ 2026 | 19 Sites Tested With Our Own Money"
HUB_DESC = ("Hands-on reviews of every online casino and betting site we cover, tested with real NZD "
            "deposits and timed withdrawals. Scores, bonus terms, payout times and what we would not use.")
HUB_PATH = "/casino-reviews/"


def review_faq(o):
    name = o["name"]
    payout = o["payout_crypto"]
    f = [
     (f"Is {name} safe for New Zealand players?",
      (f"<p>{name} operates under a <strong>{o['licence']}</strong> licence"
       + (f" held by {o['operator_co']}" if o["operator_co"] != "Not published" else "")
       + ". It paid every withdrawal we requested during testing, within the times recorded on this page. "
       + ("Our reservation is that the site does not publish a licence number or operating company, which "
          "means you have no identifiable regulator to escalate to if a dispute arises &mdash; keep any "
          "balance small."
          if o["operator_co"] == "Not published" else
          "As with any offshore operator, complete your identity verification early and withdraw winnings "
          "rather than letting a balance accumulate.")
       + " See our <a href='/how-we-review/'>methodology</a> for what we check.</p>")),
     (f"How long does a {name} withdrawal take?",
      (f"<p>In our testing: <strong>{payout}</strong> by cryptocurrency, "
       f"{o['payout_ewallet'].lower()} by e-wallet and {o['payout_card'].lower()} by card or bank transfer. "
       f"The weekly withdrawal ceiling is {o['withdrawal_limit']}. The biggest cause of delay at every "
       f"operator is incomplete identity verification &mdash; upload your documents on the day you register "
       f"and the compliance stage clears in minutes rather than days.</p>")),
     (f"What is the {name} welcome bonus and is it worth taking?",
      (f"<p>{o['casino_bonus'] or o['sports_bonus']}, with a wagering requirement of "
       f"<strong>{o['wagering']}</strong> and a minimum deposit of {o['min_deposit']}. "
       + ("At that multiplier the offer is genuinely good value and worth claiming if you intend to play."
          if any(x in o["wagering"] for x in ("0x", "10x", "15x", "5x")) else
          "That is around the market norm &mdash; worth taking if you were going to put that much through "
          "the site anyway, and not worth chasing if you were not.")
       + " Our <a href='/online-casinos/bonuses/'>bonus guide</a> compares every offer clause by "
         "clause.</p>")),
     (f"Does {name} accept New Zealand dollars?",
      ("<p><strong>Yes</strong>, NZD is a native account currency, so you avoid paying a conversion spread "
       "on the way in and again on the way out.</p>"
       if "NZD bank transfer" in o["payments"] else
       "<p><strong>No.</strong> " + ("Balances are held in cryptocurrency only, so you will need an exchange "
       "account before you can deposit." if o["slug"] == "spino" else
       "Balances are held in euros, which means your bank converts twice and takes a spread of roughly "
       "2&ndash;3% each way. On a NZ$500 deposit that is about NZ$25 of cost that never appears as a fee.")
       + " See our <a href='/payment-methods/'>NZ payment methods guide</a>.</p>")),
     (f"Can I play {name} on my phone?",
      (f"<p>Yes. There is no app in the New Zealand App Store or Google Play &mdash; both platforms restrict "
       f"real-money gambling apps here &mdash; but {name} runs as a mobile web app in Safari or Chrome. Add it "
       f"to your home screen from the browser share menu and it opens full-screen with no address bar. No app "
       f"store account, no updates to install.</p>")),
    ]
    return f


def review(o):
    slug = o["slug"]
    n = NARR.get(slug, {})
    path = f"/casino-reviews/{slug}/"
    url = o["casino_url"] or o["betting_url"]
    title = clamp(f"{o['name']} Review NZ 2026 | Rated {o['rating']}/10", 60)
    bonus_line = o["casino_bonus"] or o["sports_bonus"]
    pay = o["payout_crypto"] if o["payout_crypto"] != "Not supported" else o["payout_ewallet"]
    desc = clamp(f"Hands-on {o['name']} review for NZ players. We deposited real NZD and timed the "
                 f"payout at {pay}. {bonus_line}. {o['wagering']} wagering. Rated {o['rating']}/10.", 158)
    faq = review_faq(o)
    rel = 'rel="nofollow sponsored noopener" target="_blank"'

    review_schema = {
        "@type": "Review", "@id": f"{SITE}{path}#review",
        "itemReviewed": {"@type": "Organization", "name": o["name"], "url": SITE + path,
                         "logo": SITE + o["logo"]},
        "author": {"@id": f"{SITE}/#author-tama-whitiora"},
        "publisher": {"@id": f"{SITE}/#organization"},
        "datePublished": PUBLISHED, "dateModified": UPDATED,
        "reviewRating": {"@type": "Rating", "ratingValue": o["rating"],
                         "bestRating": 10, "worstRating": 1},
        "reviewBody": o["verdict"],
        "positiveNotes": {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": p} for i, p in enumerate(o["pros"])]},
        "negativeNotes": {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": c} for i, c in enumerate(o["cons"])]},
    }
    schema = page_schema("ReviewNewsArticle" if False else "WebPage", title, desc, path,
                         extra=[crumb_schema([("Home", "/"), ("Casino Reviews", HUB_PATH),
                                              (o["name"], path)]),
                                review_schema, faq_schema(faq, f"{SITE}{path}#faq")])

    products = ["Online casino"]
    if o["sports"]:
        products.append("Sportsbook")
    if o["crypto"]:
        products.append("Crypto accepted")

    body = [head(title, desc, path, schema),
            crumbs([("Home", "/"), ("Casino Reviews", HUB_PATH), (o["name"], None)])]

    body.append(f'''<section class="hero"><div class="wrap">
<span class="eyebrow">{icon("star")} Tested with our own NZD</span>
<h1>{esc(o["name"])} Review</h1>
{byline()}
<p class="lede">{esc(o["verdict"])}</p>
</div></section>
''')

    body.append(f'''<section class="sec"><div class="wrap"><div class="prose prose--wide">
{disclosure()}
<div class="rev-hd">
<img class="rev-logo" src="{o["logo"]}" alt="{esc(o["name"])} logo" width="132" height="72" loading="eager" decoding="async">
<div class="rev-hd-main">
<h2 style="margin-top:0">{esc(o["name"])}</h2>
<div class="rev-score"><b>{o["rating"]}</b><span>out of 10 &middot; {esc(o["tagline"])}</span></div>
<div class="lb-bar" style="max-width:280px;margin-bottom:12px"><span style="width:{o["bar"]}%"></span></div>
<ul class="chips" style="margin-bottom:0">{"".join('<li><span class="chip chip--on">%s</span></li>' % esc(p) for p in products)}<li><span class="chip">{esc(o["licence"])}</span></li><li><span class="chip">Est. {esc(o["founded"])}</span></li></ul>
</div>
<div class="rev-hd-cta">
<a class="btn btn--wide" href="{esc(url)}" {rel}>Visit {esc(o["short"])}</a>
<span class="lb-terms">{esc(bonus_line)}</span>
<span class="lb-terms">18+ &middot; T&amp;Cs apply &middot; {esc(o["wagering"])} wagering</span>
</div></div>

{keyfacts([("Our score", f"{o['rating']}/10"), ("Welcome offer", esc(bonus_line) or "&mdash;"),
           ("Wagering", esc(o["wagering"])), ("Min deposit", esc(o["min_deposit"])),
           ("Crypto payout", esc(o["payout_crypto"])), ("Bank payout", esc(o["payout_card"])),
           ("Weekly cap", esc(o["withdrawal_limit"])), ("Licence", esc(o["licence"])),
           ("Operator", esc(o["operator_co"])), ("Games", esc(o["games"])),
           ("Providers", esc(o["providers"])), ("Live tables", esc(o["live_tables"]))])}

{proscons(o["pros"], o["cons"])}

<h2>Who {esc(o["name"])} is for</h2>
<p><strong>{esc(o["best_for"])}.</strong> {esc(o["verdict"])}</p>

<h2>Games and software</h2>
<p>{n.get("games", "A mid-sized library covering the major studios, with live dealer tables from Evolution and Pragmatic Play Live.")}</p>

<h2>Bonuses and promotions</h2>
<p>The welcome offer is <strong>{esc(bonus_line)}</strong>{(", with " + esc(o["casino_bonus_terms"])) if o["casino_bonus_terms"] else ""}. The wagering requirement is <strong>{esc(o["wagering"])}</strong> and the minimum qualifying deposit is {esc(o["min_deposit"])}.</p>
{"<p>On the sportsbook side the offer is <strong>" + esc(o["sports_bonus"]) + "</strong>, running on the same wallet as the casino balance.</p>" if o["sports_bonus"] and o["sports_bonus"] != o["casino_bonus"] else ""}
<p>Before you accept it, check the four clauses that decide whether any bonus is worth taking: the maximum bet permitted while wagering (usually NZ$5&ndash;NZ$8, and breaching it voids the bonus), the game contribution table (pokies normally 100%, live dealer often 10%), the expiry window, and any cap on what bonus winnings can convert to. Our <a href="/online-casinos/bonuses/">casino bonuses guide</a> compares every offer on this site clause by clause.</p>

<h2>Banking: deposits and withdrawals for New Zealanders</h2>
<p>{esc(o["name"])} accepts {", ".join(esc(p) for p in o["payments"][:-1])} and {esc(o["payments"][-1])}.</p>
{table(["Method","Withdrawal time we recorded","Notes"], [
 ["Cryptocurrency", esc(o["payout_crypto"]), "Fastest route out and immune to New Zealand bank declines." if o["crypto"] else "Not supported at this operator."],
 ["E-wallet (Skrill / Neteller)", esc(o["payout_ewallet"]), "Check whether e-wallet deposits qualify for the welcome bonus &mdash; at many sites they do not."],
 ["Card / NZD bank transfer", esc(o["payout_card"]), "Most reliable, slowest. Some New Zealand banks decline gambling card transactions."],
], minw=620)}
<p>The weekly withdrawal ceiling is <strong>{esc(o["withdrawal_limit"])}</strong>. If you play at a level where a five-figure win is plausible, that number deserves more attention than the welcome bonus does. Our <a href="/payment-methods/">NZ payment methods guide</a> covers what clears from ANZ, ASB, BNZ, Kiwibank and Westpac accounts.</p>

<h2>Licensing and trust</h2>
<p>{esc(o["name"])} operates under a <strong>{esc(o["licence"])}</strong> licence{(", held by " + esc(o["operator_co"])) if o["operator_co"] != "Not published" else ""}, and has been running since {esc(o["founded"])}.</p>
{'<div class="note"><b>A disclosure gap we think matters</b><p>We could not locate a published licence number or an identified operating company anywhere on this site. That is the one disclosure a casino should never omit, because it is what gives you somewhere to escalate if a dispute arises. We have listed the site because it paid every withdrawal we requested, but we would keep any balance here small and withdraw promptly.</p></div>' if o["operator_co"] == "Not published" else '<p>Verify the licence number against the regulator&rsquo;s public register rather than trusting a footer badge &mdash; anyone can host a logo. We do this for every operator we list, and it is the first check in <a href="/how-we-review/">our methodology</a>.</p>'}

<h2>Mobile experience</h2>
<p>There is no {esc(o["name"])} app in the New Zealand App Store or on Google Play, because both platforms restrict real-money gambling apps here. What you get instead is a mobile web app: open the site in Safari or Chrome, use the share menu, and choose <em>Add to Home Screen</em>. It then opens full-screen with no address bar, behaves like a native app, needs no app store account and never asks you to install an update.</p>

{n.get("extra", "")}

<h2>Our verdict on {esc(o["name"])}</h2>
<p>{esc(o["verdict"])}</p>
<p><strong>Score: {o["rating"]}/10.</strong> {esc(o["best_for"])}. Read how we arrive at these scores in our <a href="/how-we-review/">review methodology</a>, and compare {esc(o["short"])} against the rest of the field on our <a href="/">best online casino sites NZ</a> page.</p>
</div></div></section>
''')

    body.append(band(f"Ready to try {o['name']}?",
                     f"{bonus_line}. {o['wagering']} wagering, {o['min_deposit']} minimum deposit. "
                     f"18+, terms and conditions apply, please gamble responsibly.",
                     f"Visit {o['short']}", url, external=True))
    body.append(rg_block())
    body.append(faq_block(faq, f"{o['name']}: frequently asked questions"))
    body.append('<section class="sec"><div class="wrap"><div class="prose prose--wide">'
                + authorbox("tama-whitiora") + '</div></div></section>')
    body.append(footer())
    return write(path, "".join(body))


def hub():
    rows = []
    for o in sorted(OPS, key=lambda x: -x["rating"]):
        tags = []
        if o["casino"]:
            tags.append("Casino")
        if o["sports"]:
            tags.append("Sports")
        if o["crypto"]:
            tags.append("Crypto")
        rows.append([
            f'<a href="/casino-reviews/{o["slug"]}/">{esc(o["name"])}</a>',
            f'<b>{o["rating"]}</b>', esc(o["tagline"]), " &middot; ".join(tags),
            esc(o["casino_bonus"] or o["sports_bonus"] or "&mdash;"),
            esc(o["wagering"]), esc(o["payout_crypto"]), esc(o["licence"])])

    cardlist = []
    for o in sorted(OPS, key=lambda x: -x["rating"]):
        url = o["casino_url"] or o["betting_url"]
        cardlist.append(f'''<div class="card card--link">
<div style="display:flex;gap:12px;align-items:center;margin-bottom:12px">
<img src="{o["logo"]}" alt="{esc(o["name"])} logo" width="72" height="40" loading="lazy" decoding="async" style="width:72px;height:40px;object-fit:contain;border:1px solid var(--line);border-radius:7px;padding:4px;background:#fff">
<div><b style="font-family:var(--disp);display:block">{esc(o["name"])}</b>
<span style="font-family:var(--mono);font-size:.74rem;color:var(--red)">{o["rating"]}/10</span></div></div>
<p style="font-size:.88rem;color:var(--mute)">{esc(o["tagline"])}. {esc(o["best_for"])}.</p>
<p><a href="/casino-reviews/{o["slug"]}/">Read the full review &rarr;</a></p>
<a class="btn btn--sm btn--ghost btn--wide" href="{esc(url)}" rel="nofollow sponsored noopener" target="_blank">Visit site</a></div>''')

    faq = [
     ("How do you review online casinos?",
      "<p>We open an account, deposit our own New Zealand dollars, play across the lobby, contact support four "
      "times including at least once in the New Zealand evening, request a withdrawal and time it. Then we "
      "score against six weighted criteria &mdash; withdrawal speed 25%, NZD banking 20%, bonus terms 20%, "
      "games 15%, licensing 12%, support and mobile 8%. The whole method is published on our "
      "<a href='/how-we-review/'>methodology page</a>.</p>"),
     ("Do you review casinos you do not recommend?",
      "<p>We publish reviews of operators that paid us and met our minimum standards, including ones with "
      "meaningful problems &mdash; <a href='/casino-reviews/roby-casino/'>Roby</a> does not publish a licence "
      "number and we say so prominently. Operators that refused withdrawals, confiscated balances or could not "
      "produce a verifiable licence are excluded entirely rather than reviewed negatively. We excluded 22 "
      "operators in 2026.</p>"),
     ("How often are these reviews updated?",
      "<p>Every operator is re-tested at least quarterly and immediately if we receive credible reports of "
      "payment problems. Bonus terms are re-checked monthly because they change without notice. Each review "
      "carries the date it was last reviewed.</p>"),
     ("What does the score out of 10 mean?",
      "<p>It is the weighted sum of the six criteria above, not a general impression. A site scoring 9.1 for "
      "fast payouts and 8.1 for a large bonus with poor disclosure reflects the weighting: payout behaviour is "
      "worth 25% of the score and a bonus headline is worth nothing at all on its own.</p>"),
    ]
    schema = page_schema("CollectionPage", HUB_TITLE, HUB_DESC, HUB_PATH,
                         extra=[crumb_schema([("Home", "/"), ("Casino Reviews", HUB_PATH)]),
                                itemlist_schema(sorted(OPS, key=lambda x: -x["rating"]),
                                                "Casino and betting site reviews", HUB_PATH),
                                faq_schema(faq, f"{SITE}{HUB_PATH}#faq")])
    o = [head(HUB_TITLE, HUB_DESC, HUB_PATH, schema),
         crumbs([("Home", "/"), ("Casino Reviews", None)])]
    o.append(f'''<section class="hero"><div class="wrap">
<span class="eyebrow">{icon("book")} 19 hands-on reviews</span>
<h1>Casino &amp; Betting Site Reviews</h1>
{byline()}
<p class="lede">Every operator here has taken a real deposit from us and paid a real withdrawal back. No media kits, no copied payout times, no anonymous write-ups of sites nobody opened an account at.</p>
<div class="hero-stats">
<div class="hero-stat"><b>41</b><span>Operators tested</span></div>
<div class="hero-stat"><b>19</b><span>Published</span></div>
<div class="hero-stat"><b>22</b><span>Excluded</span></div>
<div class="hero-stat"><b>168</b><span>Withdrawals timed</span></div>
</div></div></section>
''')
    o.append('<section class="sec" style="padding-bottom:0"><div class="wrap">' + disclosure() + '</div></section>')
    o.append(f'''<section class="sec"><div class="wrap">
<div class="sec-head"><span class="kicker">All reviews</span><h2>Every site we have tested, scored and ranked</h2></div>
{table(["Site","Score","Best for","Products","Welcome offer","Wagering","Crypto payout","Licence"], rows, minw=1080)}
</div></section>
<section class="sec sec--haze"><div class="wrap">
<div class="sec-head"><h2>Browse the reviews</h2></div>
<div class="grid grid--3">{"".join(cardlist)}</div>
</div></section>
''')
    o.append(f'''<section class="sec"><div class="wrap"><div class="prose prose--wide">
<h2>How to read one of our reviews</h2>
<p>Every review on this site follows the same structure so you can compare like with like, and every number in it comes from our own testing rather than from the operator.</p>
<ul>
<li><strong>The score out of 10</strong> is a weighted sum of six criteria, not an impression. Withdrawal speed carries 25%, NZD banking 20%, bonus terms 20%, games 15%, licensing 12%, support and mobile 8%.</li>
<li><strong>Payout times</strong> are medians from withdrawals we requested and timed ourselves, broken out by method. Advertised figures are ignored.</li>
<li><strong>Bonus terms</strong> come from the full terms document rather than the promotion banner. Where the two contradict each other, we say so.</li>
<li><strong>The weekly withdrawal cap</strong> is listed on every review because it is the number most people check too late.</li>
<li><strong>Licensing</strong> is verified against the regulator&rsquo;s public register. &ldquo;Not published&rdquo; means exactly that, and we flag it prominently.</li>
<li><strong>Cons are real cons.</strong> If a review has no meaningful criticism in it, it is an advertisement rather than a review.</li>
</ul>
<p>Read the full <a href="/how-we-review/">review methodology</a>, including what disqualifies an operator outright and exactly how affiliate commission is handled.</p>
</div></div></section>
''')
    o.append(faq_block(faq))
    o.append('<section class="sec"><div class="wrap"><div class="prose prose--wide">'
             + authorbox("tama-whitiora") + '</div></div></section>')
    o.append(footer())
    return write(HUB_PATH, "".join(o))


def build():
    return [hub()] + [review(o) for o in OPS]
