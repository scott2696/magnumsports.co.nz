# -*- coding: utf-8 -*-
"""People Also Ask content.

Questions are real: harvested from Google (gl=nz), Bing (en-NZ) and DuckDuckGo
(nz-en) autosuggest by _build/harvest_queries.py, filtered to New Zealand
intent and deduped against each page's existing FAQ. Raw set in queries.json.

Answers are written to snippet length — the direct response lands in the first
sentence, which is the shape Google lifts for featured snippets and PAA.
"""

PAA = {

# ------------------------------------------------------------------ home
"/": ("What people ask us about the shop",
      "Pulled from what New Zealanders actually search for around Magnum Sports, hunting, "
      "fishing and firearms. If your question is not here, ring the shop &mdash; it is faster "
      "than any website.",
 [("Where is Magnum Sports?",
   "<p>Magnum Sports is at <strong>220 Broadway, Stratford, Taranaki 4332</strong>, on the main "
   "road through town. Phone <a href='tel:+6467657248'>06 765 7248</a>. Stratford is about 40 "
   "minutes south of New Plymouth and an hour north of H&#257;wera, which makes us a practical stop "
   "on the way to the ranges or the coast.</p>"),
  ("Do I need a licence to buy a firearm or ammunition in New Zealand?",
   "<p><strong>Yes.</strong> You need a valid New Zealand firearms licence to buy or possess a "
   "firearm or ammunition, and for some items an endorsement and a permit to procure as well. "
   "Licences are issued by Te Tari P&#363;reke &mdash; Firearms Safety Authority. Every firearm and "
   "ammunition sale we make is completed in store with the paperwork done properly. We do not sell "
   "or ship either online.</p>"),
  ("Can I buy from Magnum Sports online?",
   "<p>Not at the moment &mdash; our online shop is being rebuilt. For now, "
   "<a href='tel:+6467657248'>phone 06 765 7248</a> or <a href='/contact/'>send us a message</a> "
   "and we will check stock, put an item aside or arrange freight on non-restricted gear. It is "
   "usually quicker than a shopping cart, and you get an actual answer to the question you have.</p>"),
  ("What is a magnum cartridge?",
   "<p>A magnum cartridge is a higher-powered version of a standard cartridge in the same "
   "calibre &mdash; more propellant, higher velocity, more recoil and more noise. The .22 WMR "
   "against the .22 LR is the common example. Whether you need one depends entirely on what you "
   "are shooting and at what range, and it is worth a conversation rather than a guess. Ask us in "
   "store.</p>"),
  ("Can you hunt in New Zealand?",
   "<p>Yes, and on public conservation land it is generally free. Deer, pig, goat, tahr and chamois "
   "are introduced species that the Department of Conservation actively wants reduced, so no game "
   "licence is required for them &mdash; though a DOC hunting permit is, and it is free to apply "
   "for. Game bird hunting is different and does require a licence from Fish &amp; Game. You still "
   "need a firearms licence for the rifle.</p>"),
  ("Is the fishing good in Taranaki?",
   "<p>Very. The region has more than 300 kilometres of fishable rivers and streams running off the "
   "maunga, with brown and rainbow trout through the season, plus a west coast that fishes well for "
   "snapper, kahawai and kingfish. A Fish &amp; Game licence is required for freshwater. Come in and "
   "we will tell you what is working where &mdash; that is the part a website cannot do.</p>"),
 ]),

# --------------------------------------------------------- online casinos
"/online-casinos/": ("What New Zealanders are actually asking",
      "These are real searches, not questions we invented. Some of them have uncomfortable "
      "answers, and we have given those straight.",
 [("What is the most trusted online casino in New Zealand?",
   "<p>Trust and &lsquo;best&rsquo; are not the same question. On trust specifically &mdash; a "
   "verifiable licence, a named operating company, and a withdrawal record we tested ourselves "
   "&mdash; <a href='/casino-reviews/spinjo/'>Spinjo</a> and "
   "<a href='/casino-reviews/rooster-bet/'>Rooster Bet</a> (Rabidi N.V. and Dama N.V. respectively) "
   "rate highest. The clearest negative signal is the opposite: "
   "<a href='/casino-reviews/roby-casino/'>Roby</a> publishes neither a licence number nor an "
   "operating company, and we say so on every page it appears on.</p>"),
  ("Are there casinos in New Zealand, and how many?",
   "<p>There are <strong>six licensed land-based casinos</strong> in New Zealand: SkyCity Auckland, "
   "SkyCity Hamilton, two in Queenstown, Christchurch Casino and Grand Casino Dunedin. The Gambling "
   "Act 2003 froze the number &mdash; no new casino licence can be issued. That cap is a large part "
   "of why online play grew the way it did, and why the "
   "<a href='/licensed-online-casinos/'>new online licensing regime</a> matters.</p>"),
  ("Do online casinos pay real money?",
   "<p>Yes &mdash; the good ones do, and we test exactly that. We requested and timed 168 "
   "withdrawals across 41 operators using our own New Zealand dollars. The ones that paid are on "
   "this page; the 22 that did not, or that made it unreasonably difficult, are not. The relevant "
   "question is never &ldquo;do they pay&rdquo; in the abstract but &ldquo;does <em>this one</em> "
   "pay&rdquo;, which is why <a href='/fast-payout-casinos/'>payout behaviour</a> is 25% of our "
   "score.</p>"),
  ("How do you win real money at an online casino?",
   "<p>By getting lucky, and there is no second method. Every game here has a published house edge "
   "&mdash; 2.5&ndash;6% on pokies, around 0.5% on blackjack at correct strategy &mdash; which means "
   "the expected result of playing is a loss. Individual sessions win often; the long run does not. "
   "What you can control is <em>how fast</em> you lose: play higher-RTP games, take low-wagering "
   "bonuses, and use cashback. Anyone selling a system is selling you something.</p>"),
  ("Are casinos a waste of money?",
   "<p>If you are treating it as an investment, yes, unambiguously &mdash; the maths guarantees a "
   "loss over time. If you are treating it as paid entertainment, that is a personal call, the same "
   "one you make about a concert ticket. The useful test is whether you set a budget beforehand and "
   "stuck to it. If the answer is no, or if you are chasing losses, the "
   "<a href='/responsible-gambling/'>Gambling Helpline is free on 0800 654 655</a>.</p>"),
  ("Which NZ online casino has the best welcome bonus?",
   "<p>On headline size, <a href='/casino-reviews/crownslots/'>CrownSlots</a> at 390% up to &euro;3,700 "
   "with 175 free spins. On actual value, <a href='/casino-reviews/smash/'>Smash</a> &mdash; its 10x "
   "wagering requires roughly NZ$4,000 of turnover on a NZ$200 deposit where a 40x bonus-only offer "
   "requires NZ$8,000 and a 45x one NZ$9,000. The biggest number and the best offer are almost never "
   "the same thing. Our <a href='/casino-bonus/'>bonus guide</a> shows the arithmetic.</p>"),
  ("Which NZ online casino is best for pokies?",
   "<p><a href='/casino-reviews/spinjo/'>Spinjo</a>, on library depth &mdash; roughly 8,000 titles "
   "from 90-plus studios, with every Pragmatic Play, Hacksaw, Nolimit City, Play&rsquo;n GO and Push "
   "Gaming release that matters, and filtering that actually works. If you would rather have a small "
   "tidy lobby than a huge one, <a href='/casino-reviews/slotsgem/'>Slotsgem</a> is the better "
   "experience. Full breakdown on our <a href='/online-pokies/'>online pokies page</a>.</p>"),
  ("Is there a $1 deposit online casino in NZ?",
   "<p>A handful advertise one, but almost none are worth taking. The catch is rarely the deposit "
   "&mdash; it is the <strong>withdrawal floor</strong>, often NZ$50 or NZ$100, which strands a small "
   "balance until it is played away. The lowest genuinely usable entry on this page is "
   "<a href='/casino-reviews/lucky-circus/'>Lucky Circus</a> at <strong>NZ$10 in and NZ$10 "
   "out</strong>. Always check both numbers, not just the one in the advert.</p>"),
 ]),

# ----------------------------------------------------------- online pokies
"/online-pokies/": ("What Kiwis ask about pokies",
      "The most-searched pokies questions in New Zealand, including the two everybody asks and "
      "nobody answers honestly.",
 [("Are online pokies legal in NZ?",
   "<p>Yes, for players. The Gambling Act 2003 bans <em>operating</em> remote gambling from inside "
   "New Zealand but has never made it an offence to play at a site hosted overseas. From "
   "<strong>1 December 2026</strong>, operators without a New Zealand licence application must stop "
   "serving New Zealanders &mdash; a change to who may supply the game, not to whether you may play "
   "it. See our <a href='/licensed-online-casinos/'>law page</a>.</p>"),
  ("How do you win on pokies in New Zealand?",
   "<p>You cannot, reliably, and anyone telling you otherwise is wrong or selling something. Every "
   "spin is generated independently by a random number generator on the studio&rsquo;s servers. There "
   "is no hot machine, no cold machine, no &lsquo;due&rsquo; payout, no advantage to a particular "
   "time of day, and no betting pattern that changes the maths. The only real decisions are which "
   "game (RTP), what stake, and when to stop.</p>"),
  ("How much do pokies pay out?",
   "<p>It depends enormously on where you play. New Zealand class 4 pub and club machines are "
   "required to return at least <strong>78%</strong> and typically return 87&ndash;92%. Online pokies "
   "from the major studios typically return <strong>94&ndash;97%</strong>. That gap &mdash; often 8 "
   "percentage points or more &mdash; is the single largest mathematical difference between the two "
   "formats.</p>"),
  ("How old do you have to be to play pokies in NZ?",
   "<p><strong>18</strong> for online pokies and for class 4 machines in pubs and clubs. "
   "<strong>20</strong> to enter one of New Zealand&rsquo;s six licensed casino venues. Online "
   "operators verify age as part of identity checks before they will process a withdrawal, and an "
   "account opened with false details is closed with the winnings forfeited.</p>"),
  ("Are online pokies safe?",
   "<p>The games themselves are, at a licensed operator running titles from established studios. The "
   "casino does not run the games &mdash; Pragmatic Play, Evolution, Play&rsquo;n GO and the rest do, "
   "on their own servers, with independently audited random number generators. The risk is not rigged "
   "reels; it is an operator that will not pay you. That is why we weight "
   "<a href='/fast-payout-casinos/'>withdrawal behaviour</a> at 25% and game fairness at almost "
   "nothing.</p>"),
  ("What is the best online pokie site for New Zealanders?",
   "<p><a href='/casino-reviews/spinjo/'>Spinjo</a> for range &mdash; around 8,000 titles across 90-plus "
   "studios with volatility and provider filters that work. "
   "<a href='/casino-reviews/fortune-play/'>Fortune Play</a> if you want crash games and bonus buys, "
   "<a href='/casino-reviews/hellspin/'>Hellspin</a> for weekly slot tournaments, and "
   "<a href='/casino-reviews/lucky-circus/'>Lucky Circus</a> if you play at NZ$10 stakes. The ranking "
   "above compares all of them.</p>"),
  ("When do pokies close in New Zealand?",
   "<p>Pub and club gaming rooms follow their venue&rsquo;s licensed hours, so they close when the "
   "venue does &mdash; and class 4 venues are required to run a mandatory break in play each day. "
   "Online pokies have no closing time at all, which is precisely the risk. A "
   "<a href='/responsible-gambling/'>session limit or reality check</a> is the substitute for last "
   "orders, and it is worth setting one before you start rather than after.</p>"),
 ]),

# ------------------------------------------------------ high payout / RTP
"/casino-payout-percentages/": ("Everything people ask about RTP",
      "RTP is the most-searched and least-understood number in online gambling. These are the "
      "questions New Zealanders actually type.",
 [("How does casino RTP work?",
   "<p>Return to player is the percentage of all money wagered that a game returns over millions of "
   "spins. A 96% RTP game has a <strong>4% house edge</strong>, so NZ$100 of turnover carries a "
   "theoretical NZ$4 cost. The word doing the work is <em>theoretical</em>: over a hundred spins the "
   "result is essentially random, and over ten thousand it is still noisy. RTP is a long-run price of "
   "play, not a session prediction.</p>"),
  ("Can casinos change the RTP on slots?",
   "<p>They cannot alter a game&rsquo;s maths, but they can choose which version to deploy &mdash; and "
   "most players have no idea. Studios ship many popular titles in several RTP configurations, "
   "commonly 96.5%, 95.5% and 94.2%, and the operator picks one. <strong>The same game genuinely pays "
   "differently at different casinos.</strong> Always read the figure in the game&rsquo;s own info "
   "panel at the site you are actually playing at.</p>"),
  ("How do you find the RTP of a slot?",
   "<p>Open the game and look in its <strong>info, help or paytable</strong> panel &mdash; the RTP is "
   "stated there, usually at the bottom of the rules. If a casino has hidden or removed it, that "
   "tells you which configuration it chose. Do not rely on a figure quoted on a review site, "
   "including ours: check it in the game, at that casino, on the day.</p>"),
  ("Which casino game has the best RTP?",
   "<p><strong>Video poker and blackjack.</strong> Full-pay Jacks or Better returns about 99.54% and "
   "blackjack at correct basic strategy about 99.5%. Then baccarat on the banker bet at 98.94%, French "
   "roulette at 98.65% and European roulette at 97.30%. The best pokies reach roughly 97.5%. If your "
   "goal is the most playing time per dollar, blackjack is the answer and it is not close.</p>"),
  ("How do you calculate the house edge from RTP?",
   "<p>Subtract the RTP from 100%. A 96% RTP is a 4% house edge; 97.3% is 2.7%. To turn that into "
   "dollars, multiply by your <strong>total turnover</strong>, not your deposit &mdash; which is why "
   "bonus wagering matters so much. NZ$8,000 of turnover to clear a 40x bonus at 96% RTP carries about "
   "NZ$320 of expected cost, whatever your deposit was.</p>"),
  ("Can you win at high RTP slots?",
   "<p>In a session, often. Over time, no &mdash; 97% RTP still means a 3% edge against you, and no "
   "stake pattern, time of day or game selection turns a number below 100 into a number above it. What "
   "a higher RTP genuinely buys is <strong>slower losses and longer play</strong> for the same budget. "
   "Shifting NZ$5,000 of annual turnover from 95.5% to 99.5% changes expected cost from about NZ$225 "
   "to about NZ$25.</p>"),
 ]),

# ---------------------------------------------------------- fast payouts
"/fast-payout-casinos/": ("Withdrawal questions New Zealanders search",
      "Every one of these comes from real autosuggest data. Two of them have answers the industry "
      "would rather you did not read.",
 [("Which online casino pays out the fastest?",
   "<p><a href='/casino-reviews/spino/'>Spino</a> was fastest overall in our testing at <strong>ten "
   "minutes to two hours</strong> on crypto, but it is crypto-only. Among casinos that take New "
   "Zealand dollars, <a href='/casino-reviews/kingdom/'>Kingdom</a> is quickest at two to four hours "
   "on crypto with no operator fee. Those are medians from withdrawals we requested and timed "
   "ourselves, not figures from an operator&rsquo;s marketing page.</p>"),
  ("How do you withdraw money from an online casino?",
   "<p>Open the cashier, choose Withdraw, pick your method, enter the amount and confirm &mdash; then "
   "<strong>leave it alone</strong>. Most operators require the same method you deposited with, up to "
   "the value of the deposit. Your account must be verified, any active bonus wagering must be "
   "finished, and you must be above the minimum withdrawal. The whole process is four stages; we break "
   "them down above.</p>"),
  ("Is there an instant withdrawal casino with no verification?",
   "<p>No, and you should be suspicious of anything advertising one. Every licensed operator is bound "
   "by anti-money-laundering obligations and will verify your identity before releasing a meaningful "
   "withdrawal &mdash; if not at the first, then at the point the amounts matter. A site genuinely "
   "willing to pay out large sums with no checks is a site with a compliance problem, which is not a "
   "feature when it is <em>your</em> balance sitting there.</p>"),
  ("Can you withdraw a casino bonus?",
   "<p>Not the bonus credit itself &mdash; you withdraw what is left after the wagering requirement is "
   "cleared, at which point the remaining balance converts to cash. Cancel a bonus part-way and you "
   "typically forfeit the bonus and anything won with it, and at operators that pool deposit and bonus "
   "funds you may forfeit more. Check which model a casino uses <em>before</em> you accept the "
   "offer.</p>"),
  ("Do casinos pay out more on certain days?",
   "<p>No. Outcomes come from random number generators running on the game studio&rsquo;s servers, not "
   "the casino&rsquo;s, and they have no concept of the calendar. What genuinely does vary by day is "
   "<strong>withdrawal processing</strong>: several operators do not process on weekends, so a Friday "
   "night request can sit until Monday. We record which ones process seven days a week.</p>"),
  ("Why is my casino withdrawal taking so long?",
   "<p>In order of likelihood: <strong>incomplete verification</strong> by a wide margin, then a "
   "request made outside the operator&rsquo;s processing hours, unfinished bonus wagering, a weekly "
   "withdrawal cap you have hit, or a mismatch between your deposit and withdrawal methods. Only the "
   "last is a payment-network issue. In our tests the same operator paid a verified account in four "
   "hours and an unverified one in three days.</p>"),
 ]),

# ------------------------------------------------------------ live casino
"/live-casino/": ("Live dealer questions people search",
      "Mostly about whether any of it is real. It is &mdash; here is how it works.",
 [("Are online casino dealers real people?",
   "<p><strong>Yes.</strong> Live dealer games are filmed in purpose-built studios with real dealers, "
   "real cards and real wheels, streamed to you in real time. Evolution runs studios in Latvia, Malta, "
   "Georgia, Canada and the Philippines; Pragmatic Play Live operates from Bucharest. You are watching "
   "an actual person deal an actual shoe &mdash; which is exactly why many players prefer it to "
   "software games.</p>"),
  ("Is live blackjack rigged?",
   "<p>No &mdash; and live dealer is the one format where you can satisfy yourself of that with your "
   "own eyes rather than by trusting a certificate. The cards are physically dealt on camera from a "
   "shoe you can see. Software games are genuinely random too, with independently audited RNGs, but "
   "they ask you to take that on trust. For players whose hesitation is fundamentally about trust, "
   "live solves a psychological problem that was never a mathematical one.</p>"),
  ("What are the table limits in New Zealand dollars?",
   "<p>Typically <strong>NZ$1 to NZ$5,000</strong> per hand on standard blackjack and roulette, with "
   "dedicated low-stakes tables from NZ$0.50 and VIP tables running to NZ$50,000. For most players the "
   "binding constraint is not the table limit but the casino&rsquo;s "
   "<a href='/fast-payout-casinos/'>weekly withdrawal cap</a>, which is the number worth checking "
   "first.</p>"),
  ("Can you play live casino from New Zealand at a reasonable hour?",
   "<p>Yes, comfortably. Evolution and Pragmatic Live run studios across Europe, Georgia and the "
   "Philippines on a 24-hour rotation, so 9pm in Auckland is mid-morning in Europe and late evening in "
   "Manila. There is no hour of the New Zealand day without open blackjack, roulette and baccarat "
   "tables &mdash; though the very high-limit tables are thinner in our early morning.</p>"),
  ("Do live casino games count towards wagering requirements?",
   "<p>Usually only partially, and this catches people out. Pokies typically contribute 100% toward a "
   "wagering requirement while live dealer games contribute <strong>10%</strong>, and some operators "
   "exclude live blackjack entirely. Clearing 40x at 10% contribution means 400x of real turnover, "
   "which is not a realistic proposition. If live dealer is what you play, consider declining the "
   "bonus.</p>"),
  ("How much data does live casino use?",
   "<p>Roughly <strong>0.5 to 1.5 GB per hour</strong> at full HD, dropping to about 200 MB at the "
   "lowest quality setting. That matters more in New Zealand than in most markets, where rural mobile "
   "coverage is uneven and data caps are tighter. Every major provider lets you drop the stream quality "
   "manually &mdash; do it before you start a session on mobile data, not after.</p>"),
 ]),

# ---------------------------------------------------------- crypto casinos
"/crypto-casinos-nz/": ("Crypto questions Kiwis search",
      "Crypto gambling raises a set of New Zealand-specific questions that generic guides skip "
      "entirely &mdash; particularly the tax one.",
 [("Is cryptocurrency legal in New Zealand?",
   "<p><strong>Yes.</strong> Cryptocurrency is legal to buy, hold and trade in New Zealand. Inland "
   "Revenue treats it as <strong>property</strong> rather than currency, which is the detail that "
   "matters for gambling: the win itself is not taxable, but a gain in the crypto&rsquo;s NZD value "
   "between acquiring and disposing of it can be. Our "
   "<a href='/gambling-winnings-tax-nz/'>tax guide</a> works through a six-step example.</p>"),
  ("How do you buy Bitcoin in New Zealand?",
   "<p>Through a New Zealand-serving exchange that accepts NZD bank transfer &mdash; Easy Crypto, "
   "Independent Reserve, Swyftx NZ and Binance all do. Expect to complete identity verification; "
   "exchanges are registered financial service providers here and it is not optional. For casino play "
   "specifically, buy <strong>USDT on the Tron network</strong> rather than Bitcoin: it settles in "
   "seconds, costs under a dollar to move, and does not move in value while you play.</p>"),
  ("What is a crypto casino?",
   "<p>An online casino that takes deposits and pays withdrawals in cryptocurrency rather than through "
   "banks. The games are usually the same Pragmatic Play and Hacksaw titles you would find anywhere "
   "&mdash; crypto changes the payment rail, not the maths. What is genuinely different is speed (ten "
   "minutes to six hours against one to five business days), immunity to New Zealand bank declines, "
   "and access to provably fair in-house games.</p>"),
  ("Do you pay tax on crypto gambling winnings in NZ?",
   "<p>Not on the win. Possibly on the coin. The gambling winnings are not assessable income, but "
   "because IRD treats crypto as property, a rise in its NZD value between when you acquired it and "
   "when you convert back can be taxable. <strong>Using a stablecoin removes most of this</strong>, "
   "since USDT and USDC are pegged and barely move. Keep records of the NZD value at both ends, and "
   "get advice if the position is meaningful.</p>"),
  ("Are crypto casinos anonymous?",
   "<p>Largely not, in 2026. Anti-money-laundering obligations apply regardless of the payment rail, "
   "and most operators will request identification before a significant withdrawal even where "
   "registration asked for nothing. A handful of crypto-native sites still allow small play "
   "unverified. Assume you will be asked and verify early &mdash; it is the difference between a "
   "four-hour payout and a three-day one.</p>"),
  ("Is there a crypto casino with a no deposit bonus for NZ?",
   "<p>Rare, and usually not what it appears. Far better value sits in the "
   "<strong>zero-wagering</strong> crypto welcome offers: "
   "<a href='/casino-reviews/spino/'>Spino&rsquo;s 0x requirement</a> means bonus winnings are "
   "withdrawable immediately, with no turnover, no maximum-bet clause to breach and no expiry. That is "
   "worth more than any no-deposit offer currently advertised to New Zealanders.</p>"),
 ]),

# --------------------------------------------------------- casino bonuses
"/casino-bonus/": ("Bonus questions people actually search",
      "Wagering requirements generate more confused searching than any other topic in online "
      "gambling. Here is the plain version.",
 [("How do wagering requirements work?",
   "<p>You must bet the bonus a set number of times before any of it can be withdrawn. A NZ$100 bonus "
   "at 40x requires <strong>NZ$4,000 of turnover</strong> &mdash; and if the multiplier applies to "
   "deposit <em>plus</em> bonus rather than the bonus alone, NZ$8,000. Turnover is not loss: you are "
   "recycling the same money through the games, losing roughly the house edge on each pass, which is "
   "about 4% of everything you put through.</p>"),
  ("How do casino bonuses work?",
   "<p>The casino credits bonus funds matched to your deposit, your balance is locked until the "
   "wagering is cleared, then whatever remains converts to withdrawable cash. Four clauses decide "
   "whether it is worth taking: the <strong>multiplier</strong>, what it <strong>applies to</strong>, "
   "the <strong>maximum bet</strong> while wagering (breach it once and the bonus is usually void), "
   "and the <strong>expiry</strong>. Bonuses are opt-in almost everywhere &mdash; declining one is a "
   "legitimate choice.</p>"),
  ("Do free spins have wagering requirements?",
   "<p>Almost always, and often higher than the deposit bonus &mdash; 50x on free spin winnings is "
   "common where the cash bonus is 40x. Free spins usually carry a <strong>maximum conversion "
   "cap</strong> as well, sometimes as low as NZ$100 no matter how much you win. Check the per-spin "
   "value while you are there: 300 free spins at NZ$0.20 is NZ$60 of play, not NZ$300.</p>"),
  ("How do you beat wagering requirements?",
   "<p>You do not beat them; you choose ones worth attempting. Take low multipliers over large "
   "headlines, play games that contribute 100% (pokies, not live dealer at 10%), stay under the "
   "maximum bet, and finish inside the expiry window. On this page "
   "<a href='/casino-reviews/smash/'>Smash at 10x</a> and "
   "<a href='/casino-reviews/spino/'>Spino at 0x</a> are the only two offers that survive the "
   "arithmetic comfortably.</p>"),
  ("What is a good $10 or $20 deposit bonus in NZ?",
   "<p>At small deposits the multiplier matters more than the match percentage, because the turnover "
   "scales with the bonus. A 100% match on NZ$20 at 10x is NZ$400 of turnover &mdash; achievable. The "
   "same NZ$20 at 45x is NZ$1,800, which will take most of the balance to clear. Check the "
   "<strong>minimum qualifying deposit</strong> too: several headline offers require NZ$25 or NZ$30 "
   "before the match triggers at all.</p>"),
  ("Can you withdraw your deposit if you do not finish the wagering?",
   "<p>It depends on the operator&rsquo;s wallet model. Where deposit and bonus funds sit in "
   "<strong>separate wallets</strong>, you can usually cancel the bonus and withdraw your own deposit, "
   "forfeiting the bonus and anything won with it. Where they are <strong>combined</strong> &mdash; "
   "increasingly common &mdash; cancelling may forfeit everything above your original deposit, or at "
   "the worst operators the lot. Check before accepting.</p>"),
 ]),

# ------------------------------------------------------ no deposit bonuses
"/no-deposit-bonus/": ("No deposit questions, answered honestly",
      "The search volume around free bonuses is enormous and most of what it returns is out of "
      "date or untrue. These answers are not flattering, but they are accurate.",
 [("What is a no deposit bonus?",
   "<p>Bonus funds or free spins credited when you register, before you put any money in. They are "
   "genuinely free to claim, and they are genuinely constrained: high wagering (40&ndash;60x), a low "
   "<strong>maximum conversion cap</strong>, a requirement to make a deposit before withdrawing, and a "
   "short expiry. All four are in the terms and none is hidden &mdash; the mistake is treating the "
   "offer as a shot at real money rather than a free look around.</p>"),
  ("How do you get free spins with no deposit?",
   "<p>By registering at an operator that still offers them, which in New Zealand in 2026 is almost "
   "none. We checked every no-deposit offer advertised to Kiwi players and could verify exactly "
   "<strong>one</strong> as live: <a href='/casino-reviews/lucky7even/'>Lucky7even&rsquo;s 20 spins on "
   "registration</a>. Pages listing twenty or thirty such offers are not checking them.</p>"),
  ("Is there a $20 or $100 no deposit bonus in NZ?",
   "<p>We could not verify a single one, and we would treat any page advertising NZ$100 free on "
   "registration as a reason to distrust the whole page. The economics do not work: a casino&rsquo;s "
   "cost to acquire a player does not stretch to a three-figure unconditional giveaway. Where large "
   "no-deposit figures do appear, the conversion cap almost always reduces the real maximum to a "
   "fraction of the headline.</p>"),
  ("Are $1 deposit casinos with free spins worth it?",
   "<p>Rarely, and the deposit is not the problem &mdash; the <strong>withdrawal floor</strong> is. "
   "Plenty of sites accept NZ$1 in and then require NZ$50 or NZ$100 out, which strands any small "
   "balance until it is played away. That asymmetry is the product. "
   "<a href='/casino-reviews/lucky-circus/'>Lucky Circus at NZ$10 in and NZ$10 out</a> is the only "
   "genuinely low-stakes entry we recommend.</p>"),
  ("Can you actually withdraw no deposit bonus winnings?",
   "<p>In principle yes; in practice rarely at a meaningful amount, by design. Lucky7even&rsquo;s "
   "spins carry <strong>50x wagering and a NZ$100 cap</strong>. Win NZ$400 and you may keep NZ$100 of "
   "it, after turning over 50x. Worth doing because it costs nothing, not worth planning around. If "
   "you simply want to try a casino, demo mode uses identical maths with no wagering and no cap.</p>"),
 ]),

# ---------------------------------------------------------- online betting
"/online-betting/": ("Betting questions New Zealanders search",
      "Search interest in whether betting is still legal here spiked after the 2025 law change, and "
      "most of what ranks for it is out of date. These answers are current.",
 [("Is sports betting banned in New Zealand?",
   "<p>Not for you. Since <strong>28 June 2025</strong> the Racing Industry Amendment Act has made it "
   "unlawful for anyone other than TAB NZ and its partner to <em>offer or promote</em> racing and "
   "sports betting to a person in New Zealand &mdash; but the Act expressly provides that an "
   "individual <strong>may not be convicted</strong> for placing a bet with an offshore operator. The "
   "prohibition binds the supplier, not the punter.</p>"),
  ("Can you get in trouble for betting with an offshore bookmaker?",
   "<p>No. The legislation protects the individual explicitly. What you do lose is recourse: an "
   "operator not authorised here is not accountable to the Department of Internal Affairs, so a "
   "withheld balance leaves you with only that operator&rsquo;s own licensing body &mdash; usually "
   "Cura&ccedil;ao or Anjouan. That is a real risk, and the reason we say keep balances small and "
   "withdraw often.</p>"),
  ("Is Bet365 legal in New Zealand?",
   "<p>Bet365 does not actively serve New Zealand customers. It was one of several large "
   "European-licensed bookmakers that withdrew rather than operate against the 2025 Act. If a guide "
   "still lists it as a New Zealand option, that guide has not been updated since mid-2025 &mdash; "
   "which is worth knowing about the rest of its content too.</p>"),
  ("What betting sites can I actually use in NZ?",
   "<p><strong>TAB NZ</strong> is the only authorised operator, in partnership with Entain, with "
   "Betcha under the same framework. Beyond that, a smaller group of offshore books still accepts New "
   "Zealand registrations &mdash; the four we tested and rate are listed "
   "<a href='#sites'>above</a>. Using one is not an offence on your part; it does mean no New Zealand "
   "regulator stands behind it.</p>"),
  ("Are there sports betting apps that work in NZ?",
   "<p>TAB NZ has a New Zealand App Store and Google Play app. Offshore books almost never do, because "
   "both platforms restrict real-money gambling apps here. What they build instead is a "
   "<strong>progressive web app</strong>: open the site in Safari or Chrome, use the share menu and "
   "choose Add to Home Screen. It opens full-screen, behaves like a native app, and needs no app store "
   "account.</p>"),
  ("How do you use TAB bonus bets?",
   "<p>Bonus bets are selected at the bet slip rather than applied automatically &mdash; choose your "
   "selection, then toggle the bonus bet option before confirming. As with offshore free bets, the "
   "<strong>stake is not returned</strong> with your winnings: a NZ$50 bonus bet at odds of 2.00 "
   "returns NZ$50, not NZ$100. Check the minimum odds and the expiry, which is often short.</p>"),
  ("Is online betting safe?",
   "<p>At TAB NZ, as safe as gambling gets here &mdash; domestic regulation and a local complaints "
   "path. At an offshore book it depends entirely on the operator, and you carry the diligence "
   "yourself: verify the licence number on the regulator&rsquo;s public register, confirm a named "
   "operating company exists, read the withdrawal terms, complete verification on day one and test "
   "with a small withdrawal early. We run all five checks &mdash; see <a href='#trust'>above</a>.</p>"),
 ]),

# ------------------------------------------------------------------- law
"/licensed-online-casinos/": ("Legality questions, answered directly",
      "&ldquo;Is online gambling legal in New Zealand&rdquo; and its variants are the most-searched "
      "gambling questions in the country. Here is each one, answered without hedging.",
 [("Is online gambling illegal in New Zealand?",
   "<p><strong>No.</strong> It is not an offence for a New Zealand resident to gamble at an online "
   "casino based overseas, and it never has been. What the Gambling Act 2003 prohibits is "
   "<em>operating</em> remote interactive gambling from within New Zealand. The Department of Internal "
   "Affairs has stated the position publicly. The new licensing regime regulates who may supply the "
   "service to you, not whether you may use it.</p>"),
  ("Can you get in trouble for online gambling in NZ?",
   "<p>No. There is no offence of playing, no penalty for depositing, and nothing to declare. The "
   "obligations in both the Gambling Act 2003 and the Racing Industry Amendment Act 2025 sit on "
   "operators and promoters. For betting specifically, the 2025 Act goes further and states expressly "
   "that an individual may not be convicted for placing a bet with an offshore operator.</p>"),
  ("Is online poker legal in New Zealand?",
   "<p>Yes, on the same basis as casino games: you may play at a site hosted overseas, and it is "
   "unlawful to run one from inside New Zealand. Poker sits within the online casino gambling "
   "framework rather than under the betting rules, so it is affected by the "
   "<strong>1 December 2026</strong> licensing cut-off rather than by TAB NZ&rsquo;s betting "
   "monopoly.</p>"),
  ("What is the gambling age in New Zealand?",
   "<p><strong>18</strong> for online gambling, sports betting and class 4 pub gaming machines. "
   "<strong>20</strong> to enter a licensed casino venue. Lotto is 18. Operators verify age during "
   "identity checks before processing a withdrawal, and accounts opened with false details are closed "
   "with the winnings forfeited &mdash; enforced far more consistently than people expect.</p>"),
  ("What does the Gambling Act 2003 actually say?",
   "<p>It is the framework statute for all New Zealand gambling. For online play the operative parts "
   "are the prohibition on conducting remote interactive gambling from within New Zealand, carve-outs "
   "for Lotto NZ and TAB NZ, a cap on land-based casino licences at the existing six, and "
   "<strong>section 10</strong>, which restricts advertising overseas gambling here. It predates "
   "consumer online casinos, which is exactly why the new Act exists.</p>"),
  ("Can offshore casinos advertise in New Zealand?",
   "<p>Advertising unlicensed online casino gambling to New Zealanders is restricted under section 10 "
   "of the Gambling Act 2003, and the regime tightens as licensing takes effect &mdash; licensed "
   "operators will face New Zealand-specific advertising rules including mandatory harm-minimisation "
   "messaging. For sports and racing betting, promotion by anyone other than TAB NZ has been "
   "prohibited outright since June 2025.</p>"),
  ("When will online gambling be licensed in New Zealand?",
   "<p>It already is being. The DIA ran an expression-of-interest window in July&ndash;August 2026 and "
   "a competitive <strong>auction in September 2026</strong> for the right to apply, with applications "
   "processed from October. Up to <strong>15 licences</strong> will be issued, each covering one brand, "
   "with no applicant holding more than three. From <strong>1 December 2026</strong>, providers that "
   "have not applied must stop serving New Zealanders.</p>"),
 ]),

# ------------------------------------------------------------------- tax
"/gambling-winnings-tax-nz/": ("Tax questions New Zealanders search",
      "Tax on winnings generates more search volume than almost any other New Zealand gambling "
      "topic, and the short answer is the same for nearly everyone.",
 [("Do you pay tax on casino winnings in NZ?",
   "<p><strong>No.</strong> Inland Revenue does not treat recreational gambling winnings as assessable "
   "income, so there is no income tax and no GST on a pokies win, a blackjack session or a jackpot. "
   "There is no threshold above which it changes, and nothing to enter on an IR3. The money is yours "
   "in full the moment it lands.</p>"),
  ("Are lottery winnings taxable in New Zealand?",
   "<p>No. A Lotto, Powerball or Instant Kiwi win is treated exactly like any other gambling win "
   "&mdash; a windfall, outside the income tax net, with nothing to declare. What <em>is</em> taxable "
   "is what the money subsequently earns: interest on a term deposit, dividends on shares, rent from "
   "a property. The win arrives tax-free and then enters the ordinary tax system like any other "
   "capital.</p>"),
  ("Why does New Zealand not tax gambling winnings?",
   "<p>Because income tax applies to income from employment, business or investment, and a "
   "recreational gambling win is none of those &mdash; it is a windfall. The corollary is the part "
   "people forget: because winnings are not income, <strong>losses are not deductible</strong> either. "
   "The treatment is symmetrical. Revenue is collected from operators through gambling duty instead of "
   "from players.</p>"),
  ("Are gambling winnings taxed differently for professionals?",
   "<p>Yes. Where gambling amounts to carrying on a <strong>business</strong>, the proceeds can be "
   "assessable income. IRD weighs organisation and system, a genuine intention to profit, scale and "
   "regularity, reliance on it as income, and whether real skill is involved. It is a demanding test "
   "&mdash; not met by playing often, or by one large win. If you might be near the line, get advice "
   "before you file, not after.</p>"),
  ("Do you have to declare casino winnings to IRD?",
   "<p>No, if you are gambling recreationally. There is no declaration requirement and no field for it "
   "on the IR3. Your <em>bank</em> may ask about the source of a large deposit under anti-money-"
   "laundering rules &mdash; that is a bank compliance question, not a tax one. Keep the withdrawal "
   "confirmation and the operator name so you can answer it in a sentence.</p>"),
  ("Is crypto gambling taxed in New Zealand?",
   "<p>This is the exception that catches people. The <strong>win is not taxable</strong>, but IRD "
   "treats cryptocurrency as property, so a rise in its NZD value between acquiring it and converting "
   "back can be taxable income &mdash; even though the gambling itself is not. Using a stablecoin such "
   "as USDT removes most of the exposure. Keep records of the NZD value at both ends, and get advice "
   "if the sums are meaningful.</p>"),
 ]),

# -------------------------------------------------------------- payments
"/casino-payment-methods/": ("Deposit and banking questions people search",
      "Most of the search volume here is about minimum deposits and whether particular methods still "
      "work from a New Zealand bank. Both answers have changed recently.",
 [("What is the minimum deposit at an NZ online casino?",
   "<p><strong>NZ$10 to NZ$35</strong> across the sites we recommend, with "
   "<a href='/casino-reviews/lucky-circus/'>Lucky Circus lowest at NZ$10</a>. The more important "
   "number is the <strong>minimum withdrawal</strong>, which many sites set far higher than the "
   "deposit floor &mdash; NZ$50 or NZ$100 is common, and it strands small balances. Lucky Circus "
   "matches NZ$10 both ways, which is rarer than it should be.</p>"),
  ("Is there a $1 deposit casino in New Zealand?",
   "<p>Some advertise one, and the deposit is almost never the catch. Check three things before you "
   "bother: the <strong>withdrawal floor</strong> (often NZ$50+), the <strong>minimum qualifying "
   "deposit for the bonus</strong> (frequently NZ$20 or more, so a NZ$1 deposit earns nothing), and "
   "whether the offer is live for New Zealand at all. In practice a NZ$10 site with matching "
   "withdrawal terms serves a small budget better.</p>"),
  ("Can you use PayPal at an online casino in NZ?",
   "<p>No. PayPal is not available for gambling deposits at the casinos that accept New Zealand "
   "players. If you want an e-wallet, <strong>Skrill</strong> and <strong>Neteller</strong> are the "
   "supported equivalents and clear withdrawals in four to 24 hours &mdash; but check whether e-wallet "
   "deposits qualify for the welcome bonus, because at several operators they are excluded.</p>"),
  ("Why do New Zealand banks decline casino deposits?",
   "<p>Because they can block transactions to gambling merchant category codes, and policies differ "
   "between ANZ, ASB, BNZ, Kiwibank and Westpac &mdash; sometimes between products at the same bank. "
   "It is not a fault at the casino&rsquo;s end and retrying will not help. Switch to an "
   "<strong>NZD bank transfer</strong> or cryptocurrency, the two methods that never failed across our "
   "testing. Some banks also offer a deliberate gambling block you may have enabled.</p>"),
  ("Can you use Paysafecard or Neosurf in NZ?",
   "<p><strong>Neosurf</strong> yes, and it is the best option if you want gambling kept off your bank "
   "statement &mdash; a cash voucher from a dairy or service station. Paysafecard is accepted at fewer "
   "New Zealand-facing sites. Both are <strong>deposit-only</strong>, so plan a separate withdrawal "
   "route from the start, usually bank transfer, which will need full verification.</p>"),
  ("What is the fastest way to get money out of an online casino?",
   "<p>Cryptocurrency, by a wide margin &mdash; ten minutes to six hours against one to five business "
   "days for a card or bank withdrawal. <strong>USDT on the Tron network</strong> is the practical "
   "choice: seconds to confirm, under a dollar to move, and pegged so it does not lose value while you "
   "play. The bigger variable is verification: verify on day one and you remove the stage where most "
   "delays actually happen.</p>"),
 ]),

# --------------------------------------------------- responsible gambling
"/responsible-gambling/": ("Questions people search when it stops being fun",
      "These come from real search data. If you are typing any of them, the Gambling Helpline is "
      "free, confidential and answers 24 hours a day on <a href='tel:0800654655'>0800 654 655</a>.",
 [("How do I get help for gambling in New Zealand?",
   "<p>Call the <strong>Gambling Helpline on <a href='tel:0800654655'>0800 654 655</a></strong> "
   "&mdash; free, confidential, 24 hours a day, every day. Text <strong>8006</strong> if you would "
   "rather not speak. The Problem Gambling Foundation offers free face-to-face and online counselling "
   "nationwide on <a href='tel:0800664262'>0800 664 262</a>. No referral is needed and nothing costs "
   "anything. You do not have to be in crisis to call, and most people who do are not.</p>"),
  ("Can a gambling addiction be cured?",
   "<p>It can be treated, and a great many people recover fully. Clinicians generally describe it as "
   "manageable rather than cured &mdash; more like a condition you learn to live around than an "
   "infection that clears. Cognitive behavioural therapy has the strongest evidence base, and it is "
   "<strong>free through New Zealand&rsquo;s publicly funded services</strong>. The single best "
   "predictor of a good outcome is asking earlier rather than later.</p>"),
  ("How do you deal with a gambling addiction?",
   "<p>Three things, roughly in order. <strong>Put barriers up</strong> &mdash; self-exclude at every "
   "operator, install BetBlocker (free) or Gamban, and turn on your bank&rsquo;s gambling block. "
   "<strong>Tell someone</strong>, because concealment is what lets it grow. <strong>Get "
   "professional support</strong> &mdash; the Helpline will refer you. Willpower alone has the worst "
   "track record of any approach; technical barriers plus support has the best.</p>"),
  ("Can a doctor help with gambling addiction?",
   "<p>Yes. Your GP can refer you into publicly funded problem gambling services, and can help with "
   "the anxiety, depression or sleep problems that frequently travel with it. Many people find it "
   "easier to raise with a GP than with family. You can also self-refer &mdash; no GP visit is "
   "required to access Gambling Helpline or Problem Gambling Foundation services.</p>"),
  ("What are the signs of a gambling problem?",
   "<p>Gambling more or longer than you intended; chasing losses; borrowing or using money meant for "
   "bills; hiding it from people close to you; gambling to escape stress or low mood; being unable to "
   "stop once you have decided to; lying about how much you have lost; and it affecting work, sleep, "
   "study or relationships. <strong>Any one of these is enough to warrant a phone call.</strong></p>"),
  ("How do I block gambling sites on my phone?",
   "<p>Use two layers, because one is easy to undo. <strong>BetBlocker</strong> is free, blocks "
   "thousands of gambling sites and apps across devices, and cannot be uninstalled during a period you "
   "set; <strong>Gamban</strong> is the paid alternative with broader coverage. Then turn on your "
   "<strong>bank&rsquo;s gambling block</strong> &mdash; ASB, ANZ, BNZ, Kiwibank and Westpac all offer "
   "one from the app, and several impose a cooling-off period before it can be removed.</p>"),
 ]),

# -------------------------------------------------------- casino reviews
"/casino-reviews/": ("What people ask before they open an account",
      "Trust questions dominate the search data around casino reviews. These are the ones Kiwis "
      "type most often.",
 [("Are online casino games legit?",
   "<p>At licensed operators running titles from established studios, yes &mdash; and the reason is "
   "structural rather than a matter of faith. The casino does not run the games. Pragmatic Play, "
   "Evolution, Play&rsquo;n GO and the rest do, on their own servers, with random number generators "
   "audited by independent labs. An operator can no more adjust a Pragmatic Play title&rsquo;s RTP "
   "than a pub can adjust a Sky broadcast.</p>"),
  ("What is the most legit online casino in NZ?",
   "<p>Judge it on three checkable things rather than a badge: a <strong>licence number you can "
   "verify</strong> on the regulator&rsquo;s public register, a <strong>named operating company</strong>, "
   "and a payout record someone has actually tested. On those, "
   "<a href='/casino-reviews/spinjo/'>Spinjo</a> (Rabidi N.V.) and "
   "<a href='/casino-reviews/rooster-bet/'>Rooster Bet</a> (Dama N.V.) rate highest here. "
   "<a href='/casino-reviews/roby-casino/'>Roby</a> publishes neither, which is why it sits where it "
   "does.</p>"),
  ("How do you tell if an online casino is safe?",
   "<p>Five minutes of checking answers it. Find the licence number in the footer and verify it "
   "against the regulator&rsquo;s register &mdash; a badge image proves nothing. Confirm a named legal "
   "entity and registered address appear in the terms. Read the withdrawal ceilings and fees. Complete "
   "verification on day one. Then test with a small withdrawal in the first week, which buys you "
   "information about how the operator behaves when it owes you money.</p>"),
  ("Are online casino apps legit?",
   "<p>Be careful here. Apple and Google restrict real-money gambling apps in New Zealand, so almost "
   "no offshore operator ships one to the local stores &mdash; which means an app claiming to be one "
   "deserves scrutiny. The legitimate route is the operator&rsquo;s <strong>mobile web app</strong>: "
   "open the site in Safari or Chrome and use Add to Home Screen. Full-screen, app-like, no store "
   "account, nothing to install.</p>"),
  ("Can you trust casino reviews on the internet?",
   "<p>Treat any review site as an interested party until it shows you otherwise, this one included. "
   "The questions worth asking: does it publish its <strong>scoring weightings</strong>? Does it say "
   "what disqualifies an operator? Does it ever <strong>criticise</strong> a site it links to? Does it "
   "disclose commission plainly? Our answers are on the "
   "<a href='/how-we-rate-casinos/'>methodology page</a>, and we would rather you read it sceptically than "
   "not at all.</p>"),
  ("Is SkyCity online legit?",
   "<p>SkyCity is a New Zealand-listed company operating the country&rsquo;s largest land-based "
   "casinos, and it runs a licensed online casino in a jurisdiction where it holds a licence. It is a "
   "different kind of proposition from the offshore operators we review here &mdash; more local "
   "accountability, generally smaller bonuses. We do not have a commercial relationship with SkyCity "
   "and do not review it, which is also why we can say that plainly.</p>"),
 ]),

# ------------------------------------------------------------------ about
"/about/": ("What people ask about us",
      "Fair questions about a site that reviews gambling operators for commission.",
 [("Is Magnum Sports a real business?",
   "<p>Yes. Magnum Sports is an outdoors and sporting goods store at <strong>220 Broadway, Stratford, "
   "Taranaki</strong> &mdash; hunting, fishing, camping, clothing and firearms, twelve departments on "
   "the floor. Phone <a href='tel:+6467657248'>06 765 7248</a> and someone will answer. The betting "
   "and casino guides are published by the same business, by a "
   "<a href='/authors/'>named team</a>, and kept separate from the shop.</p>"),
  ("Who writes the casino and betting reviews?",
   "<p>Three named people, each with a defined area and a published contact address: Tama Whitiora "
   "(casino reviews and scoring), Holly McGrath (payments and banking) and Daniel Ashworth (law, tax "
   "and betting). Every page carries an author <em>and</em> a fact-checker, and they are never the "
   "same person. Full profiles on the <a href='/authors/'>authors page</a>.</p>"),
  ("How does this site make money?",
   "<p>Affiliate commission &mdash; operators pay us when a reader opens an account through one of our "
   "links. It costs you nothing and changes nothing about the offer. What it does not do is buy a "
   "ranking: commission rates across the operators we list run from 20% to 50%, our top-rated casino "
   "is not the highest payer, and we excluded 22 operators this year on editorial grounds, several "
   "paying well above average.</p>"),
  ("Do you accept guest posts or paid links?",
   "<p>No, and we are asked most days. No guest posts, no link insertions, no sponsored placements, no "
   "purchased &lsquo;editor&rsquo;s choice&rsquo; badges, and no paid ranking positions. Nothing "
   "published here is written by anyone outside our team, and no operator sees a review before it goes "
   "live.</p>"),
 ]),

# ------------------------------------------------------------ methodology
"/how-we-rate-casinos/": ("What people ask about review sites",
      "Reasonable scepticism about commission-funded reviews, including this one. We would rather "
      "answer it than have you assume.",
 [("How do casino review sites make money?",
   "<p>Affiliate commission, almost universally &mdash; the operator pays a share of its revenue from "
   "players who sign up through the site&rsquo;s links. Anyone claiming otherwise while linking to "
   "casinos is being less than straight with you. The questions worth asking are not <em>whether</em> "
   "a site earns commission but whether it publishes its scoring method, whether it ever criticises "
   "what it links to, and whether it excludes operators on editorial grounds.</p>"),
  ("Can you trust online casino reviews?",
   "<p>Apply four tests. Does the site publish its <strong>scoring weightings</strong>, not just a "
   "list of criteria? Does it say what <strong>disqualifies</strong> an operator, and how many it "
   "excluded? Does it ever <strong>criticise</strong> a site it earns from? Does it claim to have "
   "tested things it plainly has not &mdash; copied payout times are the usual tell. Most sites fail "
   "at least two. Ours are answered on this page, and we would rather you checked.</p>"),
  ("Do casinos pay for good reviews?",
   "<p>They offer to, regularly. We do not sell ranking positions, &lsquo;editor&rsquo;s choice&rsquo; "
   "badges, sponsored table rows or link insertions, and no operator sees a review before it goes "
   "live. The commission rates available to us range from 20% to 50% &mdash; our top-rated casino "
   "pays 45%, and two of the highest payers sit outside our top five, with one excluded "
   "entirely.</p>"),
  ("How often are casino reviews updated?",
   "<p>Ours: every operator re-tested at least <strong>quarterly</strong>, bonus terms re-checked "
   "<strong>monthly</strong> because they change without notice, legal pages reviewed monthly and "
   "after every DIA announcement, and an immediate re-test whenever a reader reports a payment "
   "problem. Every page carries the date it was last reviewed. A page with no date, or a date more "
   "than a year old, is telling you something.</p>"),
  ("How do you actually test an online casino?",
   "<p>We open a real account, complete verification, deposit our own New Zealand dollars, read the "
   "full terms document rather than the promotional banner, play across the lobby, contact live chat "
   "four times including once in the New Zealand evening, request a withdrawal and time it, then run "
   "the whole cycle again on a phone. In 2026 that came to 41 operators, about NZ$14,800 of our own "
   "money and 168 timed withdrawals.</p>"),
 ]),

# ---------------------------------------------------------------- contact
"/contact/": ("Questions we get asked most",
      "Before you write, these are the four things people ask us most often.",
 [("What is the Magnum Sports phone number?",
   "<p><strong><a href='tel:+6467657248'>06 765 7248</a></strong>, for the shop at 220 Broadway, "
   "Stratford. That is the fastest route for stock checks, holds, advice and anything involving "
   "firearms or ammunition, which we handle in store rather than online. For editorial matters, "
   "<a href='mailto:editor@magnumsports.co.nz'>editor@magnumsports.co.nz</a>.</p>"),
  ("How do I report a problem with an operator you recommend?",
   "<p>Email <a href='mailto:corrections@magnumsports.co.nz'>corrections@magnumsports.co.nz</a> with "
   "the site name, the date and what happened. It goes straight to our fact-checking editor and "
   "triggers an <strong>immediate re-test</strong> of that operator. Reader reports of non-payment "
   "are the single most valuable input we get &mdash; several of the 22 operators we excluded this "
   "year were flagged that way first.</p>"),
  ("Can you get my money back from a casino?",
   "<p>No. We are a comparison site, not a regulator or an ombudsman, with no authority over any "
   "operator and no ability to release a withheld balance. What we can do is re-test them, raise it "
   "where we have a contact, and remove them. Pursue the operator&rsquo;s own complaints process and "
   "then its licensing body in parallel &mdash; and check first that your "
   "<a href='/fast-payout-casinos/'>verification is complete</a>, which is what most stuck "
   "withdrawals turn out to be.</p>"),
  ("How quickly do you reply?",
   "<p>Within <strong>two working days</strong>, New Zealand time, on every address on this page. "
   "Privacy requests under the Privacy Act 2020 are answered within 20 working days as the Act "
   "requires, and usually much sooner. If you are writing about gambling harm rather than about the "
   "site, please contact the <a href='/responsible-gambling/'>Gambling Helpline on 0800 654 655</a> "
   "instead &mdash; they are trained for it and available right now.</p>"),
 ]),

# ------------------------------------------------------- new casinos nz
"/new-casinos-nz/": ("What people ask about new casino sites",
      "New brands attract a specific set of searches &mdash; mostly about whether they can be "
      "trusted, which is the right instinct.",
 [("Are new online casinos safe in NZ?",
   "<p>Some are. A 2024 launch is not automatically worse than a 2019 one &mdash; several of the "
   "strongest sites we rate are new. What a new casino site lacks is a complaint history, and there "
   "is no substitute for that, only proxies: a verifiable licence number, a named operating company, "
   "withdrawal terms without unlimited operator discretion, and a small test withdrawal in week "
   "one.</p>"),
  ("Which are the best new casino sites NZ 2026?",
   "<p>On our testing, <a href='/casino-reviews/kingdom/'>Kingdom</a> for payout speed, "
   "<a href='/casino-reviews/smash/'>Smash</a> for the 10x wagering, "
   "<a href='/casino-reviews/rivo/'>Rivo</a> for mobile and "
   "<a href='/casino-reviews/crownslots/'>CrownSlots</a> for the largest welcome package. All four "
   "launched within the last two years. <a href='/casino-reviews/roby-casino/'>Roby</a> is the new "
   "brand we would avoid &mdash; it publishes neither a licence number nor an operating "
   "company.</p>"),
  ("Do new online casinos have no deposit bonuses in NZ?",
   "<p>Almost never. New operators put their acquisition spend into large matched deposits rather "
   "than unconditional giveaways, because a deposit filters for genuine intent. Across every new "
   "casino site we checked, none had a verified no deposit offer &mdash; the only one live in this "
   "market sits at a 2022 brand. See our <a href='/no-deposit-bonus/'>no deposit bonus page</a>.</p>"),
  ("When do new licensed casinos launch in New Zealand?",
   "<p>From <strong>December 2026 onwards</strong>. The DIA auction ran in September 2026 and "
   "applications are processed from October, so the first licence holders are determined after that. "
   "Up to 15 brands will go live under New Zealand supervision. We add each one to this page with "
   "the date as it launches, and track the licences themselves on our "
   "<a href='/licensed-online-casinos/'>licensed online casinos page</a>.</p>"),
  ("Are there new crypto casinos for NZ players?",
   "<p>Yes &mdash; crypto is where most recent launches concentrate, because it sidesteps the bank "
   "declines that make card deposits unreliable here. <a href='/casino-reviews/spino/'>Spino</a> is "
   "the clearest example: crypto-only, launched 2024, with a zero-wagering welcome offer and "
   "ten-minute withdrawals. Our <a href='/crypto-casinos-nz/'>crypto casinos NZ page</a> covers the "
   "coins and the tax position.</p>"),
  ("Do new NZ casinos accept NZD?",
   "<p>Most of the recent launches do &mdash; Kingdom, Smash, Rivo and MadCasino all hold New Zealand "
   "dollar balances. The exceptions matter: <a href='/casino-reviews/crownslots/'>CrownSlots</a> is "
   "euro-denominated and <a href='/casino-reviews/spino/'>Spino</a> is crypto-only. A non-NZD account "
   "costs you roughly 2&ndash;3% in conversion each way, which on a NZ$500 deposit is about NZ$25 "
   "that never appears as a fee.</p>"),
 ]),
}
