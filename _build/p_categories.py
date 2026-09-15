# -*- coding: utf-8 -*-
"""Category / money pages."""
from lib import *


def shell(title, desc, path, crumb, h1, lede, eyebrow, ops, lb_head, lb_intro,
          body, faq, author="tama-whitiora", checker="daniel-ashworth",
          stats=None, mode="casino", extra_schema=None):
    ex = [crumb_schema([("Home", "/")] + crumb),
          itemlist_schema(ops, h1, path, mode),
          faq_schema(faq + paa_items(path), f"{SITE}{path}#faq")]
    if extra_schema:
        ex += extra_schema
    schema = page_schema("CollectionPage", title, desc, path, author=author, extra=ex)
    o = [head(title, desc, path, schema),
         crumbs([("Home", "/")] + [(c[0], None if i == len(crumb) - 1 else c[1])
                                   for i, c in enumerate(crumb)])]
    st = ""
    if stats:
        st = '<div class="hero-stats">' + "".join(
            f'<div class="hero-stat"><b>{a}</b><span>{b}</span></div>' for a, b in stats) + '</div>'
    o.append(f'''<section class="hero"><div class="wrap">
<span class="eyebrow">{eyebrow}</span>
<h1>{h1}</h1>
{byline(author, checker)}
<p class="lede">{lede}</p>
{st}
</div></section>
''')
    o.append(leaderboard(ops, mode, heading=lb_head, intro=lb_intro))
    o.append(body)
    o.append(rg_block())
    o.append(faq_block(faq))
    o.append(paa_for(path, haze=False))
    o.append('<section class="sec"><div class="wrap"><div class="prose prose--wide">'
             + authorbox(author) + '</div></div></section>')
    o.append(disclosure_section())
    o.append(footer())
    return write(path, "".join(o))


# ============================================================ ONLINE POKIES
def pokies():
    ops = [BY[s] for s in ["spinjo", "fortune-play", "hellspin", "kingdom", "lucky7even",
                           "rivo", "slotsgem", "lucky-circus", "crownslots", "smash"]]
    faq = [
     ("What are the best online pokies to play in NZ?",
      "<p>By popularity among the New Zealand players we surveyed: <strong>Sweet Bonanza</strong> and "
      "<strong>Gates of Olympus</strong> (Pragmatic Play), <strong>Book of Dead</strong> (Play&rsquo;n GO), "
      "<strong>Big Bass Bonanza</strong> (Reel Kingdom), <strong>Wanted Dead or a Wild</strong> (Hacksaw) and "
      "<strong>Mental</strong> (Nolimit City). All six are available at <a href='/casino-reviews/spinjo/'>Spinjo</a> "
      "and <a href='/casino-reviews/fortune-play/'>Fortune Play</a>. &lsquo;Best&rsquo; is mostly a question of "
      "volatility preference rather than quality &mdash; see the volatility section above.</p>"),
     ("What RTP should I look for in an online pokie?",
      "<p><strong>96% or better.</strong> The industry range runs roughly 94% to 97.5%, and many popular titles "
      "ship in multiple RTP configurations that operators can choose between &mdash; the same game can be 96.5% "
      "at one casino and 94.2% at another. Always check the figure in the game&rsquo;s own info panel at the site "
      "you are playing, not on a review page. If a casino hides RTP in the game info, that tells you something.</p>"),
     ("Are online pokies the same as pub pokies in New Zealand?",
      "<p>No, and the difference is substantial. New Zealand class 4 gaming machines in pubs and clubs are "
      "required to return a minimum of <strong>78%</strong> and typically return 87 to 92%. Online pokies from "
      "the major studios typically return <strong>94 to 97%</strong>. That gap &mdash; often 8 percentage points "
      "or more &mdash; is the single largest mathematical difference between the two formats, and it exists "
      "because online operators have vastly lower overheads and a proportion of pub machine revenue is directed "
      "to community grants.</p>"),
     ("Can I play online pokies for free?",
      "<p>Yes. Almost every title runs in demo mode with play money, no account required at most sites, and the "
      "demo uses the identical maths and RTP as the real-money version. It is genuinely the best way to learn how "
      "a bonus feature triggers or how brutal a high-volatility game&rsquo;s base game is before you risk money. "
      "The one thing demo mode cannot teach you is what the swings feel like when it is your money.</p>"),
     ("What does volatility mean and which should I choose?",
      "<p>Volatility describes the shape of the wins, not the size of the return. <strong>Low volatility</strong> "
      "pays small amounts often and stretches a budget. <strong>High volatility</strong> pays rarely and "
      "occasionally very large, and will empty a budget quickly while you wait. Two games with identical 96% RTP "
      "can feel completely different. Match it to your bankroll: if NZ$50 is your session budget, a Nolimit City "
      "high-variance title is likely to be over in ten minutes.</p>"),
     ("Do online pokies pay better at certain times?",
      "<p>No. Every spin is generated independently by a random number generator running on the studio&rsquo;s "
      "servers, not the casino&rsquo;s. There is no hot hour, no cold machine, no &lsquo;due&rsquo; payout and no "
      "advantage to playing at 3am. Any strategy built on timing, or on a game being &lsquo;ready&rsquo;, is "
      "built on a misunderstanding of how the software works.</p>"),
    ]
    body = f'''<section class="sec sec--haze"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">The studios</span>
<h2>Which pokies providers actually matter</h2>
<p>A lobby of 8,000 titles is mostly padding. Fifteen studios produce almost everything a New Zealand player would deliberately seek out, and a casino&rsquo;s value is better measured by which of them it carries than by its total count.</p>
{table(["Studio","Known for","Signature titles","Typical RTP","Volatility"], [
 ["Pragmatic Play","The most widely stocked studio in the world","Sweet Bonanza, Gates of Olympus, Big Bass Bonanza","96.0–96.5%","Medium–high"],
 ["Hacksaw Gaming","Modern, mechanically inventive, bonus-buy heavy","Wanted Dead or a Wild, Le Bandit, Chaos Crew","96.0–96.3%","Very high"],
 ["Nolimit City","The most punishing volatility in the industry","Mental, San Quentin, Fire in the Hole","96.0–96.5%","Extreme"],
 ["Play&rsquo;n GO","Reliable, huge catalogue, strong classics","Book of Dead, Reactoonz, Rise of Olympus","96.2–96.5%","Medium–high"],
 ["Push Gaming","Polished mechanics and clean maths","Razor Shark, Jammin&rsquo; Jars, Big Bamboo","96.3–96.7%","High"],
 ["NetEnt","The originals, now owned by Evolution","Starburst, Gonzo&rsquo;s Quest, Dead or Alive 2","96.0–96.8%","Low–high"],
 ["Relax Gaming","Megaways and progressive networks","Money Train series, Temple Tumble","96.2–96.5%","High"],
 ["Big Time Gaming","Invented Megaways","Bonanza, White Rabbit, Extra Chilli","96.0–96.7%","High"],
 ["Nolimit / Print / Peter&nbsp;&amp;&nbsp;Sons","Boutique studios with cult followings","Various","95.5–96.5%","High"],
], minw=880)}
<p>If a casino stocks Pragmatic Play, Hacksaw, Nolimit City, Play&rsquo;n GO and Push Gaming, it has everything most players will ever want. <a href="/casino-reviews/spinjo/">Spinjo</a> carries all five plus roughly 85 other studios; <a href="/casino-reviews/slotsgem/">Slotsgem</a> carries the majors with a far smaller tail and a much better search function, which for some players is the better trade.</p>
</div></div></section>

<section class="sec"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">The maths</span>
<h2>RTP, volatility and hit rate, explained properly</h2>
<p>Three numbers describe a pokie, and most players only ever hear about one of them.</p>
<h3>RTP: what comes back, eventually</h3>
<p>Return to player is the proportion of all money wagered that a game returns over millions of spins. A 96% RTP game has a 4% house edge, so NZ$100 of turnover carries a theoretical NZ$4 cost. The word doing the work is <em>theoretical</em>: over a hundred spins the outcome is essentially random, and over ten thousand it is still noisy. RTP is a long-run cost of play, not a session prediction.</p>
<p>The detail almost nobody mentions: many popular titles ship in several RTP configurations &mdash; 96.5%, 95.5%, 94.2% &mdash; and the operator chooses which to deploy. The same game genuinely pays differently at different casinos. Check the info panel in the game itself at the site you are playing, every time.</p>
<h3>What is RTP in pokies?</h3>
<p>The same thing it is anywhere else, with one wrinkle that matters. RTP in pokies is the proportion of total wagers a game returns over millions of spins &mdash; 96% RTP means a theoretical NZ$4 cost per NZ$100 of turnover. The wrinkle is that studios ship many pokies in <strong>several RTP configurations</strong> and the operator chooses which to deploy, so the same title genuinely pays differently at different casinos. Check the figure in the game&rsquo;s own info panel, at the site you are playing, every time.</p>

<h3>Volatility: the shape of the ride</h3>
{table(["Volatility","Hit frequency","Typical max win","Suits a budget of","Example"], [
 ["Low","30–45% of spins","500–2,000x","Small, stretched over time","Starburst, Big Bass Bonanza"],
 ["Medium","22–30%","2,000–10,000x","Most recreational play","Book of Dead, Gates of Olympus"],
 ["High","18–24%","10,000–25,000x","Larger, with tolerance for long droughts","Razor Shark, Money Train 4"],
 ["Extreme","15–20%","25,000x+","Only money you are fully prepared to lose","Mental, Fire in the Hole"],
], minw=760)}
<h3>Hit rate: how often anything happens</h3>
<p>Hit rate is the percentage of spins returning any win at all, including wins smaller than your stake. A 25% hit rate means three spins in four return nothing. Low hit rate plus high volatility is the combination that empties a balance fastest, and it is exactly the combination the most-hyped modern titles use.</p>
<div class="note note--amber"><b>Bonus buys: the honest version</b>
<p>Most modern pokies let you skip the base game and pay directly for the bonus round, typically 75x to 100x your stake. The RTP of a bought bonus is usually a fraction of a percent <em>higher</em> than the base game, so it is not a trap in the mathematical sense. What it is, unambiguously, is an enormous acceleration of turnover: a NZ$1 stake becomes a NZ$100 purchase, and a session that would have lasted an hour lasts four minutes. If you use them, size them against your budget rather than against the stake you were spinning at.</p></div>
</div></div></section>

<section class="sec sec--haze"><div class="wrap">
<div class="sec-head"><span class="kicker">Formats</span><h2>Types of online pokies</h2></div>
{cards([
 ("dice","Classic three-reel","Simple, low-feature, usually low volatility. A small niche online but a familiar format for anyone who grew up on pub machines."),
 ("chart","Video pokies (five-reel)","The mainstream format: 5 reels, 10 to 50 paylines, free spin rounds, wilds and scatters. Most of what you will play."),
 ("bolt","Megaways","Reel heights change every spin, giving up to 117,649 ways to win. Licensed from Big Time Gaming and used across the industry. High volatility by design."),
 ("coin","Progressive jackpots","A pooled prize growing across a network until someone hits it. Life-changing headline figures, and correspondingly poor base-game RTP — the jackpot is funded from your spins."),
 ("star","Cluster pays","Wins come from groups of adjacent symbols rather than paylines, usually with a tumble mechanic. Sweet Bonanza is the definitive example."),
 ("lock","Hold and win","Lock respin mechanics where collected symbols stay in place. Extremely popular and often paired with fixed jackpot tiers."),
])}
</div></section>

<section class="sec"><div class="wrap"><div class="prose prose--wide">
<h2>Free pokies NZ: playing without money</h2>
<p>Almost every title runs in <strong>demo mode</strong> with play money, no account needed at most sites, and the demo uses the identical maths and RTP as the real money version. Free pokies are genuinely the best way to learn how a bonus feature triggers or how brutal a high-volatility game&rsquo;s base game is before you risk anything, and unlike a no-deposit bonus there is no wagering and no cashout cap attached.</p>
<p>What demo mode cannot teach you is what the swings feel like when the money is yours, which is the part that actually changes how people play. Treat free pokies as a rules tutorial rather than a rehearsal. If you then want real money pokies NZ sites, the ranking at the top of this page is where to start.</p>

<h2>Online pokies vs New Zealand pub pokies</h2>
<p>This comparison deserves more prominence than it usually gets, because the difference is not marginal.</p>
{table(["", "NZ class 4 pub pokies", "Online pokies"], [
 ["Minimum return","78% (legally mandated)","No mandate — but studios ship 94–97.5%"],
 ["Typical return","87–92%","94–97%"],
 ["Max bet","NZ$2.50 per spin","Usually NZ$100+ per spin"],
 ["Max prize","NZ$1,000 (single win)","Uncapped — 25,000x stake is common"],
 ["Game choice","Whatever the venue installed","Thousands of titles"],
 ["Where profits go","~40% to community grants","To the operator"],
 ["Harm-minimisation","Venue staff, mandated signage","Deposit limits, reality checks, self-exclusion"],
 ["Age limit","18","18"],
], minw=680)}
<p>The mathematical case for online is clear on RTP alone. The counterweight is equally clear: a pub machine caps your bet at NZ$2.50 and closes at some point, while an online lobby accepts NZ$100 a spin at three in the morning with no one to notice. The higher return is genuine; so is the higher risk of playing far more than you meant to. That is not an argument against online pokies, but it is an argument for setting the deposit limit before you start.</p>
</div></div></section>
'''
    return shell(
        "Online Pokies NZ 2026 | Best Real Money Pokies Sites for Kiwis",
        "The best online pokies sites for New Zealand players in 2026. Compare RTP, volatility, studios "
        "and free spins across 10 tested casinos — plus how online pokies compare to NZ pub machines.",
        "/online-pokies/", [("Online Casinos NZ", "/online-casinos/"), ("Online Pokies NZ", "/online-pokies/")],
        "Online Pokies NZ: Best Real Money Pokies Sites [" + MONTH_YEAR + "]",
        "Online pokies real money play is what most Kiwis actually do, so we ranked these real money pokies NZ "
        "pokies session &mdash; which studios they stock, whether RTP is published, whether the lobby can be "
        "searched, and how the free spins really work.",
        icon("dice") + " 10 pokies lobbies tested", ops,
        "Best online pokies NZ: real money pokies sites ranked",
        "Re-scored from our full testing data with game library, studio coverage, RTP transparency and free "
        "spin value weighted most heavily.",
        body, faq,
        stats=[("94–97.5%", "Online pokie RTP"), ("87–92%", "NZ pub pokie RTP"),
               ("8,000", "Titles at our #1"), ("117,649", "Max Megaways")])


# ======================================================= FAST PAYOUT CASINOS
def fast_payout():
    ops = [BY[s] for s in ["spino", "kingdom", "spinjo", "rooster-bet", "fortune-play",
                           "smash", "rivo", "crownslots", "madcasino", "lucky-vibe"]]
    faq = [
     ("Which online casino pays out fastest in New Zealand?",
      "<p><a href='/casino-reviews/spino/'>Spino</a> was fastest overall at <strong>ten minutes to two "
      "hours</strong>, but it is crypto-only with no NZD route. Among casinos that accept New Zealand dollars, "
      "<a href='/casino-reviews/kingdom/'>Kingdom</a> was quickest at two to four hours on crypto with no "
      "operator fee.</p>"),
     ("Are instant withdrawal casinos real?",
      "<p>&lsquo;Instant&rsquo; is marketing. What operators mean is that <em>their</em> processing is instant "
      "once approved &mdash; the approval step, the verification step and the payment network are all still "
      "ahead of you. The fastest genuine end-to-end payout we have ever recorded is around ten minutes, on "
      "crypto, to a fully verified account with the withdrawal requested during European business hours. Treat "
      "any claim of a true instant cashout as a claim about one stage of a four-stage process.</p>"),
     ("Why is my casino withdrawal taking so long?",
      "<p>In order of likelihood: <strong>incomplete verification</strong> (by far the most common), a withdrawal "
      "requested outside the operator&rsquo;s business hours so it sits in a queue, an unmet wagering requirement "
      "on an active bonus, a weekly withdrawal cap you have hit, or a mismatch between your deposit and "
      "withdrawal methods. Only the last of those is a payment-network problem; the rest are administrative and "
      "mostly preventable.</p>"),
     ("What is a reverse withdrawal and why does it matter?",
      "<p>A pending period &mdash; often 24 to 48 hours &mdash; during which you can cancel your own withdrawal "
      "and return the money to your playable balance. It exists because a meaningful proportion of players do "
      "exactly that, and lose it. Look for the option to disable reversal in account settings and turn it on. "
      "Casinos that make reversal the default and hide the setting are marked down on this site.</p>"),
     ("Do casinos charge a withdrawal fee?",
      "<p>Most on this page do not. Where fees appear, they are usually on withdrawals below a threshold "
      "(NZ$50 is common), on a second or subsequent withdrawal within the same week, or on card withdrawals "
      "specifically. Crypto withdrawals normally carry only the blockchain network fee, which the operator does "
      "not control. Check the banking page before your first cashout, not after.</p>"),
     ("Does verification really speed things up that much?",
      "<p>Dramatically. In our tests, a verified account at a mid-tier operator paid out in four hours; the same "
      "operator took <strong>three days</strong> on an unverified account, of which two and a half were spent "
      "waiting for someone to open the document. Upload your ID on the day you register, before you have "
      "anything to withdraw. It is the single highest-value five minutes in online gambling.</p>"),
    ]
    body = f'''<section class="sec sec--haze"><div class="wrap">
<div class="sec-head"><span class="kicker">The data</span><h2>Withdrawal times we recorded, method by method</h2>
<p>Every figure below is the median of our own timed tests from withdrawal request to funds available. We ignore what operators advertise entirely.</p></div>
{table(["Method","Fastest recorded","Median","Slowest recorded","Fee","Withdrawal supported"], [
 ["Cryptocurrency (BTC, ETH, USDT, LTC)","<b>10 minutes</b>","3 hours","26 hours","Network fee only","<span class='t-yes'>Yes</span>"],
 ["Skrill","2 hours","9 hours","38 hours","Usually none","<span class='t-yes'>Yes</span>"],
 ["Neteller","3 hours","11 hours","42 hours","Usually none","<span class='t-yes'>Yes</span>"],
 ["MiFinity / Jeton","5 hours","16 hours","48 hours","Varies","<span class='t-yes'>Yes</span>"],
 ["NZD bank transfer","19 hours","2 business days","5 business days","Usually none","<span class='t-yes'>Yes</span>"],
 ["Visa / Mastercard","1 business day","3 business days","6 business days","None at casino","<span class='t-yes'>Usually</span>"],
 ["Neosurf","—","—","—","—","<span class='t-no'>Deposit only</span>"],
 ["POLi","—","—","—","—","<span class='t-no'>Deposit only</span>"],
], minw=900)}
<p style="font-size:.86rem;color:var(--mute)">Sample: 168 withdrawals across 41 operators, January to September 2026. Times are from request to funds available in the receiving account, on verified accounts.</p>
</div></section>

<section class="sec"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">Anatomy</span>
<h2>What actually happens between &ldquo;withdraw&rdquo; and the money arriving</h2>
<p>Understanding the four stages makes it obvious where the delay lives &mdash; and which stages you control.</p>
<ol class="steps">
<li><h4>Pending / reversal window <span style="color:var(--mute);font-weight:400">— 0 to 48 hours</span></h4><p>Your request sits in a state where you can cancel it. Entirely within the operator&rsquo;s gift and entirely designed to tempt you back into the lobby. <strong>You control this</strong>: disable reversal in account settings, or request the withdrawal and close the tab.</p></li>
<li><h4>Compliance review <span style="color:var(--mute);font-weight:400">— 0 to 72 hours</span></h4><p>A human or an automated system checks your documents, the bonus status on your account and whether the withdrawal pattern raises anti-money-laundering flags. <strong>You control this</strong> too: a fully verified account clears this stage in minutes. An unverified one is where three-day waits are born.</p></li>
<li><h4>Operator processing <span style="color:var(--mute);font-weight:400">— minutes to 24 hours</span></h4><p>The actual approval and payment instruction. This is the only stage the word &ldquo;instant&rdquo; ever refers to. Operators that process on weekends have a real advantage here, and many do not.</p></li>
<li><h4>Payment network <span style="color:var(--mute);font-weight:400">— 10 minutes to 5 business days</span></h4><p>Blockchain confirmation, e-wallet transfer, or the banking system. Nobody controls this but it is entirely predictable: crypto minutes, e-wallets hours, banks days.</p></li>
</ol>
<div class="note note--mint"><b>The two habits that cut most of the wait</b>
<p>Verify your account on day one, and choose a method whose network stage is fast. Do both and a payout that takes a mid-tier operator three days takes it four hours &mdash; at the same casino, with the same operator, on the same day of the week. Almost all of the variation people attribute to casinos being slow is actually these two variables.</p></div>
</div></div></section>

<section class="sec sec--haze"><div class="wrap"><div class="prose prose--wide">
<h2>How long do casino withdrawals take in NZ?</h2>
<p>From our own timed tests: <strong>ten minutes to six hours by cryptocurrency, four to 24 hours by e-wallet, and one to five business days by card or NZD bank transfer</strong>. Those are medians across 168 withdrawals at 41 operators, measured from request to funds available rather than from operator approval.</p>
<p>An instant withdrawal casino NZ players can genuinely rely on does not quite exist, because &ldquo;instant&rdquo; describes only one of four stages. What does exist is a fully verified account paired with a crypto rail, which compresses the whole process to well under an hour at the better sites. The single biggest variable is not the method &mdash; it is whether your identity documents were accepted before you asked for the money.</p>

<h2>Withdrawal limits: the number people check too late</h2>
<p>Payout speed is irrelevant if a ceiling meters your winnings out over a month. Every weekly cap we recorded:</p>
{table(["Casino","Weekly cap","Min withdrawal","Fee","Weekend processing"], [
 ["<a href='/casino-reviews/spino/'>Spino</a>","<b>No stated cap</b>","20 USDT","Network only","<span class='t-yes'>Yes</span>"],
 ["<a href='/casino-reviews/kingdom/'>Kingdom</a>","NZ$10,000","NZ$20","None","<span class='t-yes'>Yes</span>"],
 ["<a href='/casino-reviews/smash/'>Smash</a>","NZ$10,000","NZ$20","None","<span class='t-yes'>Yes</span>"],
 ["<a href='/casino-reviews/spinjo/'>Spinjo</a>","NZ$8,000","NZ$25","None","<span class='t-yes'>Yes</span>"],
 ["<a href='/casino-reviews/rooster-bet/'>Rooster Bet</a>","NZ$8,000","NZ$25","None","<span class='t-yes'>Yes</span>"],
 ["<a href='/casino-reviews/rivo/'>Rivo</a>","NZ$8,000","NZ$25","None","<span class='t-no'>No</span>"],
 ["<a href='/casino-reviews/fortune-play/'>Fortune Play</a>","NZ$7,000","NZ$25","None","<span class='t-yes'>Yes</span>"],
 ["<a href='/casino-reviews/lucky-vibe/'>Lucky Vibe</a>","NZ$6,500","NZ$25","None","<span class='t-no'>No</span>"],
 ["<a href='/casino-reviews/lucky-circus/'>Lucky Circus</a>","NZ$5,000","<b>NZ$10</b>","None","<span class='t-no'>No</span>"],
 ["<a href='/casino-reviews/slotsgem/'>Slotsgem</a>","NZ$4,000","NZ$20","Below NZ$50","<span class='t-no'>No</span>"],
], minw=760)}
<p>If you play at a level where a five-figure win is plausible, the cap deserves more of your attention than the welcome bonus. A NZ$20,000 win at a NZ$5,000-a-week ceiling takes a month to extract, and it sits in your casino balance the whole time &mdash; which is precisely the risk the cap creates.</p>
</div></div></section>
'''
    return shell(
        "Fast Payout Casinos NZ 2026 | Fastest Withdrawals Timed by Us",
        "We timed 168 withdrawals across 41 casinos. The fastest payout casinos for New Zealand players in "
        "2026, with real withdrawal times by method, weekly caps and what actually causes delays.",
        "/fast-payout-casinos/",
        [("Online Casinos NZ", "/online-casinos/"), ("Fast Payout Casinos NZ", "/fast-payout-casinos/")],
        "Fast Payout Casinos NZ: Instant Withdrawal Sites [" + MONTH_YEAR + "]",
        "We requested a withdrawal at every casino we tested and timed it with a stopwatch, from request to "
        "money in the account. No advertised figures, no &ldquo;up to&rdquo; claims &mdash; just the times we "
        "actually recorded, and the two things you can do to halve them.",
        icon("bolt") + " 168 withdrawals timed", ops,
        "Fastest paying online casino NZ sites, ranked on timed withdrawals",
        "Ranked purely on our recorded withdrawal times, weighted toward the methods New Zealanders actually use.",
        body, faq, author="holly-mcgrath",
        stats=[("10 min", "Fastest logged"), ("3 hrs", "Median crypto"),
               ("2 days", "Median NZD bank"), ("168", "Withdrawals timed")])


# ======================================================= HIGH PAYOUT CASINOS
def high_payout():
    ops = [BY[s] for s in ["spinjo", "ivibet", "kingdom", "rooster-bet", "smash",
                           "hellspin", "fortune-play", "rivo", "lucky-vibe", "slotsgem"]]
    faq = [
     ("Which casino has the highest payout percentage in NZ?",
      "<p>Payout percentage is a property of games, not casinos &mdash; a casino&rsquo;s overall figure is just a "
      "weighted average of what its players happened to play. What a casino controls is <em>which RTP "
      "configuration it deploys</em> and whether it tells you. <a href='/casino-reviews/spinjo/'>Spinjo</a> and "
      "<a href='/casino-reviews/ivibet/'>Ivibet</a> publish per-game RTP in the info panel across their "
      "libraries, which is the honest version of a high-payout claim.</p>"),
     ("What is the highest RTP casino game?",
      "<p><strong>Blackjack at optimal basic strategy returns about 99.5%.</strong> Full-pay Jacks or Better "
      "video poker reaches 99.54%. Baccarat on the banker bet is 98.94%, French roulette 98.65%, and European "
      "roulette 97.30%. The best pokies sit around 97.5%. If your objective is the longest play from a fixed "
      "budget, blackjack is the answer and it is not close.</p>"),
     ("Does a higher RTP mean I will win?",
      "<p>No. Every game on this page has a house edge, which means the expected outcome of playing it is a loss. "
      "A higher RTP means you lose more slowly, which over a long period is a meaningful amount of money &mdash; "
      "but no RTP figure below 100% can be overcome by strategy or persistence. Treat RTP as the price of "
      "entertainment, not as a path to profit.</p>"),
     ("Do casinos change the RTP of games?",
      "<p>Casinos cannot alter a game&rsquo;s maths, but many titles are supplied by the studio in several RTP "
      "configurations &mdash; 96.5%, 95.5% and 94.2% versions of the same game &mdash; and the operator chooses "
      "which to deploy. This is entirely legal and widely done. It is also why you should check the RTP in the "
      "game&rsquo;s info panel at the casino you are actually playing at, rather than trusting a figure from a "
      "review.</p>"),
     ("Is a high RTP pokie better than a low volatility one?",
      "<p>They answer different questions. RTP tells you the long-run cost; volatility tells you how the money "
      "arrives. A 97% high-volatility game may empty a NZ$50 budget faster than a 95% low-volatility one, even "
      "though it is cheaper to play over a year. For a small session budget, volatility matters more. For annual "
      "turnover, RTP matters more.</p>"),
     ("Are progressive jackpots high payout games?",
      "<p>Structurally, no. The jackpot is funded by a slice of every spin, which is taken out of the base game "
      "return &mdash; so progressive titles typically run a base RTP of 88 to 94%, well below a standard pokie. "
      "The total RTP including the jackpot can look respectable, but that portion is concentrated in an outcome "
      "essentially nobody experiences. Enjoy them as lottery tickets, not as value.</p>"),
    ]
    body = f'''<section class="sec sec--haze"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">The numbers</span>
<h2>What is RTP in pokies and table games?</h2>
<p>RTP &mdash; return to player &mdash; is the share of all money wagered that a game pays back over millions of rounds. A 96% RTP carries a 4% house edge, so NZ$100 of turnover costs about NZ$4 in expectation. It is a long-run price of play, not a prediction of your session: over a hundred spins the outcome is essentially random, and over ten thousand it is still noisy.</p>
<p>Two things people get wrong. RTP is calculated on <strong>turnover, not deposits</strong>, which is why bonus wagering costs so much more than it appears. And casino payout percentages advertised site-wide are a weighted average of whatever players happened to play that month &mdash; a month of heavy blackjack traffic produces a flattering number that says nothing about the pokies. Per-game RTP is the only figure worth reading.</p>

<h2>Highest RTP casino games, ranked</h2>
<p>If you want the most playing time per dollar, this table is the whole answer. The differences are far larger than anything a welcome bonus can offset.</p>
{table(["Game","RTP at best play","House edge","NZ$100 turnover costs","Requires strategy?"], [
 ["Jacks or Better video poker (9/6 full pay)","<b>99.54%</b>","0.46%","NZ$0.46","<span class='t-yes'>Yes — meaningfully</span>"],
 ["Blackjack (liberal rules, basic strategy)","<b>99.5%</b>","0.5%","NZ$0.50","<span class='t-yes'>Yes — chart is free</span>"],
 ["Deuces Wild video poker (full pay)","99.37%","0.63%","NZ$0.63","<span class='t-yes'>Yes</span>"],
 ["Baccarat — banker bet","98.94%","1.06%","NZ$1.06","<span class='t-no'>No</span>"],
 ["Craps — pass line with odds","98.6–99.5%","0.5–1.4%","NZ$0.50–1.40","Minimal"],
 ["French roulette (La Partage)","98.65%","1.35%","NZ$1.35","<span class='t-no'>No</span>"],
 ["European roulette","97.30%","2.70%","NZ$2.70","<span class='t-no'>No</span>"],
 ["Best-in-class pokies","96.5–97.5%","2.5–3.5%","NZ$2.50–3.50","<span class='t-no'>No</span>"],
 ["Typical pokies","95.0–96.5%","3.5–5.0%","NZ$3.50–5.00","<span class='t-no'>No</span>"],
 ["American roulette","94.74%","5.26%","NZ$5.26","<span class='t-no'>No — just avoid it</span>"],
 ["Progressive jackpot pokies (base game)","88–94%","6–12%","NZ$6.00–12.00","<span class='t-no'>No</span>"],
], minw=900)}
<div class="note note--amber"><b>The single easiest saving available to you</b>
<p>If a casino offers both European and American roulette, the American wheel has a second zero and doubles the house edge from 2.7% to 5.26%. They sit side by side in the lobby, look nearly identical, and one costs you twice as much. Check for the double zero before you sit down. French roulette, where available, is better than both.</p></div>
</div></div></section>

<section class="sec"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">Practical</span>
<h2>How to actually get a higher return from a New Zealand casino</h2>
<h3>1. Play the games with the lower edge</h3>
<p>Obvious, and almost nobody does it. Shifting NZ$5,000 of annual turnover from typical pokies at 95.5% to blackjack at 99.5% changes your expected annual cost from NZ$225 to NZ$25. That is a NZ$200 difference from one decision, which is more than any welcome bonus on this site delivers net of wagering.</p>
<h3>2. Check the RTP configuration in the game itself</h3>
<p>Open the game&rsquo;s info or help panel and find the stated RTP before you spin. The same title genuinely runs at different returns at different operators. A casino that buries or omits this figure is telling you which configuration it chose.</p>
<h3>3. Take the low-wagering bonus over the large one</h3>
<p>A NZ$100 bonus at 10x wagering is worth far more than a NZ$1,000 bonus at 45x, because the second requires NZ$45,000 of turnover to release and the expected cost of generating that turnover exceeds the bonus. <a href="/casino-reviews/smash/">Smash at 10x</a> and <a href="/casino-reviews/spino/">Spino at 0x</a> are the only two offers on this site that reliably survive that arithmetic. Our <a href="/casino-bonus/">bonus guide</a> works it through.</p>
<h3>4. Use cashback rather than deposit matches</h3>
<p>Cashback is paid on net losses, usually without wagering, which makes it a direct reduction in the house edge rather than a conditional credit. A 10% weekly cashback on a 96% RTP game moves your effective return to roughly 96.4%. <a href="/casino-reviews/lucky-vibe/">Lucky Vibe</a> is the strongest on this page for cashback that starts at the entry tier rather than being reserved for high rollers.</p>
<h3>5. Avoid the three genuine value traps</h3>
<ul>
<li><strong>American roulette</strong> when European is available in the same lobby.</li>
<li><strong>Side bets</strong> on blackjack and baccarat &mdash; 21+3, Perfect Pairs and similar carry house edges of 5 to 12% against a base game edge under 1%.</li>
<li><strong>Insurance</strong> in blackjack, which is a 7% edge bet dressed up as protection. Decline it every time.</li>
</ul>
</div></div></section>

<section class="sec sec--haze"><div class="wrap">
<div class="sec-head"><span class="kicker">Verify it</span><h2>How to check a casino&rsquo;s payout claims yourself</h2></div>
{cards([
 ("search","Look for per-game RTP","Open any pokie&rsquo;s info panel. A casino publishing the figure per title is being straight with you. One that shows only a site-wide average, or nothing, is not."),
 ("shield","Check for an audit","eCOGRA, iTech Labs and GLI test RNGs and publish payout reports. A footer badge is not evidence — follow the link and confirm the certificate names the operator and is current."),
 ("scale","Compare the same game across sites","Open your favourite title at two casinos and compare the stated RTP. If they differ, the operators chose different configurations, and now you know which one to play it at."),
 ("chart","Ignore monthly payout percentages","A headline &ldquo;97.8% payout last month&rdquo; is a weighted average of what players happened to play. A month of heavy blackjack traffic produces a flattering number that tells you nothing about the pokies."),
])}
</div></section>
'''
    return shell(
        "High Payout Casinos NZ 2026 | Highest RTP Casino Sites",
        "The highest payout online casinos for New Zealand players in 2026. Real RTP figures by game, "
        "which sites publish them, and the five decisions that genuinely improve your return.",
        "/casino-payout-percentages/",
        [("Online Casinos NZ", "/online-casinos/"), ("Casino Payout Percentages", "/casino-payout-percentages/")],
        "Casino Payout Percentages: Highest RTP Casinos NZ [" + MONTH_YEAR + "]",
        "&ldquo;High payout&rdquo; is the most abused phrase in this industry. Here is what it actually means, "
        "which games genuinely return the most, which New Zealand-facing casinos publish their figures honestly, "
        "and the five decisions that move your return more than any bonus ever will.",
        icon("chart") + " Return to player verified per game", ops,
        "Best payout online casino NZ sites, ranked on RTP transparency",
        "Ranked on RTP transparency, the share of high-return games in the lobby, independent auditing and "
        "cashback that reduces the effective house edge.",
        body, faq,
        stats=[("99.5%", "Blackjack RTP"), ("97.3%", "European roulette"),
               ("94.7%", "American roulette"), ("2.7%", "The gap, per spin")])


# =========================================================== LIVE CASINOS
def live_casinos():
    ops = [BY[s] for s in ["ivibet", "spinjo", "rooster-bet", "kingdom", "lucky-vibe",
                           "fortune-play", "rivo", "crownslots", "madcasino", "hellspin"]]
    faq = [
     ("What is a live dealer casino?",
      "<p>Real tables with real dealers, filmed in a studio and streamed to you in real time. You place bets "
      "through an on-screen interface and watch a physical card being dealt or a physical wheel being spun. The "
      "outcome is determined by the equipment in front of the camera rather than by software, which is precisely "
      "why many players prefer it.</p>"),
     ("Are live dealer games available at NZ-friendly hours?",
      "<p>Yes, comfortably. Evolution and Pragmatic Play Live run studios across Europe, Latvia, Georgia and the "
      "Philippines on a 24-hour rotation, so a New Zealand player at 9pm NZT is hitting mid-morning in Europe "
      "and late evening in Manila. There is no hour of the New Zealand day when the major blackjack, roulette "
      "and baccarat tables are unavailable, though the very high-limit tables are thinner in our early morning.</p>"),
     ("What are the table limits in NZD?",
      "<p>Typically <strong>NZ$1 to NZ$5,000</strong> per hand on standard blackjack and roulette, with dedicated "
      "low-stakes tables from NZ$0.50 and VIP tables running to NZ$50,000. The practical constraint for most "
      "players is not the table limit but the casino&rsquo;s weekly withdrawal cap &mdash; see our "
      "<a href='/fast-payout-casinos/'>payout page</a>.</p>"),
     ("Do live casino games count toward bonus wagering?",
      "<p>Usually only partially, and this catches a lot of people out. Pokies typically contribute 100% toward "
      "a wagering requirement while live dealer games contribute 10%, and some operators exclude live blackjack "
      "entirely. Clearing a 40x requirement at 10% contribution means 400x of actual turnover, which is not a "
      "realistic proposition. If you intend to play live dealer, consider declining the bonus.</p>"),
     ("Is live dealer fairer than RNG games?",
      "<p>Neither is unfair at a licensed operator, but live dealer is more <em>verifiable</em> by you. You watch "
      "the card leave the shoe. Software games are genuinely random and independently audited, but you are "
      "trusting a certificate rather than your own eyes. For players whose hesitation about online casinos is "
      "fundamentally about trust, live dealer solves the psychological problem even though there was no "
      "mathematical problem to solve.</p>"),
     ("How much data does live dealer use on mobile?",
      "<p>Roughly <strong>0.5 to 1.5 GB per hour</strong> at full HD, dropping to about 200 MB at the lowest "
      "quality setting. That matters in New Zealand, where mobile data plans are less generous than in many "
      "markets and rural coverage is uneven. Every major provider lets you drop the stream quality manually "
      "&mdash; do it before you start a session on mobile data rather than after.</p>"),
    ]
    body = f'''<section class="sec sec--haze"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">The providers</span>
<h2>Who actually runs the live tables</h2>
<p>Two companies dominate, and the difference between a good and a poor live casino is almost entirely a question of which of their table ranges the operator has licensed.</p>
{table(["Provider","Strength","Standout tables","Studios","Verdict"], [
 ["Evolution","The market leader by a wide margin","Lightning Roulette, Crazy Time, Infinite Blackjack, Monopoly Live","Latvia, Malta, Georgia, Canada, Philippines","The one that matters. A live casino without Evolution is not a serious live casino."],
 ["Pragmatic Play Live","Fast-growing, sharp production","Mega Wheel, Sweet Bonanza Candyland, ONE Blackjack","Bucharest","A credible second. Better value on low-limit tables than Evolution."],
 ["Playtech Live","Strong on classic table games","Quantum Roulette, All Bets Blackjack","Riga, Manila","Solid, less widely deployed at NZ-facing operators."],
 ["Ezugi","Budget-friendly, Asian-market focus","Andar Bahar, Teen Patti, OTT Andar Bahar","Eastern Europe, Asia","Useful breadth, lower production values."],
 ["Authentic Gaming","Streams from real land-based casinos","Roulette from actual casino floors","Malta, Romania, Georgia","A genuine point of difference for atmosphere."],
], minw=900)}
</div></div></section>

<section class="sec"><div class="wrap">
<div class="sec-head"><span class="kicker">Games</span><h2>What you can play live</h2></div>
{cards([
 ("dice","Live blackjack","The best return in the building at around 99.5% with basic strategy. Infinite Blackjack removes seat limits so you never wait. Decline insurance and skip the side bets — both are far worse than the base game."),
 ("coin","Live roulette","European and French wheels at 97.3% and 98.65%. Lightning Roulette adds random multipliers at the cost of a slightly lower base return. Check for the double zero and avoid the American wheel."),
 ("chart","Live baccarat","98.94% on the banker bet, almost no decisions, and the fastest-moving table in the building. The tie bet at around 85% is one of the worst propositions in any casino — never take it."),
 ("star","Game shows","Crazy Time, Monopoly Live, Mega Wheel, Dream Catcher. Enormously popular, genuinely entertaining, and priced accordingly — house edges typically run 3.5% to 8%. Entertainment, not value."),
 ("users","Live poker variants","Casino Hold&rsquo;em, Three Card Poker, Ultimate Texas Hold&rsquo;em. You play against the house, not other players, with edges from 2% to 3.5%."),
 ("mobile","Low-limit tables","Dedicated NZ$0.50 to NZ$5 tables from both Evolution and Pragmatic. A genuinely good way to learn the rhythm of a live table without committing much."),
])}
</div></section>

<section class="sec sec--haze"><div class="wrap"><div class="prose prose--wide">
<h2>Live dealer casino NZ: what to look for</h2>
<p>A live dealer casino NZ players should bother with comes down to three things. <strong>Which studios it licenses</strong> &mdash; Evolution is close to essential, with Pragmatic Play Live a credible second. <strong>Whether NZD tables exist</strong>, because a euro-denominated live balance costs you the conversion spread twice. And <strong>whether low-limit tables are open at New Zealand hours</strong>, which in practice they always are, since the studios run on a 24-hour rotation across Europe, Georgia and the Philippines.</p>

<h2>Live casino etiquette and practicalities for Kiwi players</h2>
<h3>You can chat, and the dealer will answer</h3>
<p>Live tables carry a text chat and dealers respond by name. It is a pleasant part of the experience and, for players who miss the social side of a venue, a meaningful one. Dealers are professionals doing a job in front of a camera on a long shift &mdash; abuse gets you muted and then banned, and rightly so.</p>
<h3>The decision clock is real</h3>
<p>Live tables run on a timer, typically 12 to 20 seconds to act. If you time out on blackjack, the system stands your hand automatically. Have your basic strategy sorted before you sit down rather than looking it up mid-hand, because the chart does not fit in the window you get.</p>
<h3>Bandwidth is the thing that will actually spoil your session</h3>
<p>A dropped stream mid-hand is the most common live casino complaint and it is almost always the player&rsquo;s connection. On New Zealand rural or mobile connections, drop the stream to standard definition from the settings before you start &mdash; the game is identical and the reliability is transformed. Every major provider keeps your bet valid through a brief disconnection and settles it on the actual table result.</p>
<h3>Bonuses and live play do not mix</h3>
<p>Worth repeating because it costs people real money: live dealer games usually contribute 10% or less toward wagering requirements, and some operators exclude them outright. If live dealer is what you play, declining the welcome bonus and keeping your balance withdrawable at any time is usually the better decision. See our <a href="/casino-bonus/">bonus guide</a> for the contribution tables.</p>
</div></div></section>
'''
    return shell(
        "Live Casinos NZ 2026 | Best Live Dealer Sites for Kiwi Players",
        "The best live dealer casinos for New Zealand players in 2026. Evolution and Pragmatic Live coverage, "
        "NZD table limits, RTP by game and which studios are open at 9pm New Zealand time.",
        "/live-casino/",
        [("Online Casinos NZ", "/online-casinos/"), ("Live Casino NZ", "/live-casino/")],
        "Live Casino NZ: Best Live Dealer Casino Sites [" + MONTH_YEAR + "]",
        "Real dealers, real cards, streamed to Auckland at nine in the evening. We ranked New Zealand-facing "
        "live casinos on which Evolution and Pragmatic Live tables they carry, NZD limits, stream quality on a "
        "Kiwi connection, and whether live play counts toward the bonus you were offered.",
        icon("users") + " Evolution &amp; Pragmatic Live tested", ops,
        "Best live casino NZ sites: live dealer blackjack, roulette and baccarat",
        "Scored on live table coverage, provider mix, NZD limits, stream reliability and whether low-stakes "
        "tables are available.",
        body, faq,
        stats=[("400+", "Tables at our #1"), ("99.5%", "Live blackjack RTP"),
               ("24/7", "Tables open in NZT"), ("NZ$0.50", "Lowest live limit")])


# ========================================================= CRYPTO CASINOS
def crypto():
    ops = [BY[s] for s in ["spino", "kingdom", "spinjo", "crownslots", "fortune-play",
                           "smash", "rivo", "lucky7even", "rooster-bet", "madcasino"]]
    faq = [
     ("Are crypto casinos legal in New Zealand?",
      "<p>The same rules apply as to any offshore online casino: it is not an offence for a New Zealander to "
      "play, and the operator side is being brought into a licensing regime from 1 December 2026. Cryptocurrency "
      "itself is legal to hold and trade in New Zealand and is treated as <strong>property</strong> by Inland "
      "Revenue, which has tax consequences covered below. See our "
      "<a href='/licensed-online-casinos/'>NZ casino law page</a>.</p>"),
     ("Do I pay tax on crypto casino winnings in NZ?",
      "<p>This is the one area where New Zealand&rsquo;s otherwise simple position gets complicated, and getting "
      "it wrong is expensive. <strong>The gambling win itself is not taxable.</strong> But cryptocurrency is "
      "property, and if the NZD value of your crypto rises between when you acquired it and when you dispose of "
      "it &mdash; including converting it back to NZD &mdash; that gain can be taxable income. Keep records of "
      "the NZD value at acquisition and at disposal. Our <a href='/gambling-winnings-tax-nz/'>tax guide</a> works "
      "through the detail, and this is an area where speaking to an accountant is genuinely worthwhile.</p>"),
     ("What is the fastest crypto to use for casino withdrawals?",
      "<p><strong>Litecoin, Tron and Solana</strong> confirm in seconds to a couple of minutes with negligible "
      "fees. <strong>USDT on Tron (TRC-20)</strong> is the best combination of speed, low fee and price "
      "stability &mdash; it is a stablecoin, so your balance does not move while you play. Bitcoin is accepted "
      "everywhere but is the slowest and most expensive of the common options. Ethereum sits in between and "
      "fees vary with network congestion.</p>"),
     ("What does provably fair actually mean?",
      "<p>A cryptographic method that lets you verify a result was determined before you bet rather than after. "
      "The casino publishes a hashed server seed in advance, you contribute a client seed, and after the round "
      "you can check the unhashed seed against the published hash to confirm nothing was altered. It genuinely "
      "works and it is genuinely checkable &mdash; but note it only applies to the casino&rsquo;s own in-house "
      "games. Third-party pokies from Pragmatic or Hacksaw use conventional audited RNGs instead.</p>"),
     ("Do I need to verify my identity at a crypto casino?",
      "<p>Usually yes, and increasingly so. The idea that crypto casinos are anonymous is out of date &mdash; "
      "anti-money-laundering obligations apply regardless of the payment rail, and most operators will request "
      "identification before a significant withdrawal even if registration required nothing. A handful of "
      "crypto-native sites still allow small play without verification. Assume you will be asked and verify "
      "early.</p>"),
     ("What happens if the crypto price moves while I am playing?",
      "<p>You carry that risk, and it can dwarf the house edge. If you deposit 0.01 BTC and Bitcoin falls 8% "
      "overnight, your NZD-equivalent balance falls with it regardless of how the games went. Using a "
      "<strong>stablecoin such as USDT or USDC</strong> removes this entirely &mdash; the balance stays pegged "
      "to the US dollar. For New Zealanders this is the sensible default unless you specifically want the "
      "exposure.</p>"),
    ]
    body = f'''<section class="sec sec--haze"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">Which coin</span>
<h2>Cryptocurrencies accepted by NZ-facing casinos</h2>
{table(["Coin","Confirmation","Typical fee","Price stable?","Accepted at","Best for"], [
 ["USDT (TRC-20)","<b>Seconds</b>","Under NZ$1","<span class='t-yes'>Yes — pegged</span>","All 10 sites","<b>The default choice for most players</b>"],
 ["USDC","Seconds–1 min","Low","<span class='t-yes'>Yes — pegged</span>","7 of 10","Same benefits as USDT, marginally less accepted"],
 ["Litecoin (LTC)","2–5 min","Under NZ$1","<span class='t-no'>No</span>","8 of 10","Fast and cheap if you want a non-stable coin"],
 ["Solana (SOL)","Seconds","Negligible","<span class='t-no'>No</span>","4 of 10","Speed, where supported"],
 ["Tron (TRX)","Seconds","Negligible","<span class='t-no'>No</span>","4 of 10","The rail USDT usually travels on"],
 ["Ethereum (ETH)","1–5 min","Varies widely","<span class='t-no'>No</span>","All 10 sites","Widely accepted; fees spike with congestion"],
 ["Bitcoin (BTC)","10–60 min","NZ$2–15","<span class='t-no'>No</span>","All 10 sites","Universal acceptance, worst speed and cost"],
 ["Dogecoin (DOGE)","1–5 min","Low","<span class='t-no'>No</span>","3 of 10","Novelty, cheap transfers"],
], minw=920)}
<div class="note note--mint"><b>If you take one thing from this page</b>
<p>Use <strong>USDT on the Tron network</strong>. It confirms in seconds, costs under a dollar to move, and being a stablecoin it does not lose value while you are playing. Bitcoin is the coin everyone knows and close to the worst practical choice for casino play &mdash; slow, expensive, and volatile enough that an overnight move can cost you more than the house edge.</p></div>
</div></div></section>

<section class="sec"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">Getting started</span>
<h2>Bitcoin casino NZ: is Bitcoin the right coin?</h2>
<p>Usually not, and this is the most useful thing on the page. Bitcoin gambling is what everyone searches for and Bitcoin is close to the worst practical choice for casino play: 10 to 60 minutes to confirm, NZ$2&ndash;15 in network fees, and volatile enough that an overnight move can cost you more than the house edge does all week.</p>
<p>Every serious crypto casino NZ players can use accepts <strong>USDT on the Tron network</strong> instead &mdash; seconds to confirm, under a dollar to move, and pegged to the US dollar so the balance does not drift while you play. If you specifically want Bitcoin exposure, hold it in a wallet and gamble with a stablecoin. Crypto casinos New Zealand players rate highest all support both.</p>

<h2>How to fund a crypto casino from New Zealand</h2>
<ol class="steps">
<li><h4>Open an account at a NZ-friendly exchange</h4><p>Easy Crypto, Independent Reserve, Swyftx NZ and Binance all serve New Zealand and accept NZD deposits by bank transfer. Expect to complete identity verification &mdash; exchanges are registered financial service providers here and it is not optional.</p></li>
<li><h4>Buy USDT, not Bitcoin</h4><p>Unless you specifically want price exposure. Buy on the <strong>Tron (TRC-20)</strong> network where the exchange offers a choice &mdash; it is the cheapest and fastest rail, and the one casinos most commonly support.</p></li>
<li><h4>Send a small test transaction first</h4><p>Copy the casino&rsquo;s deposit address, send NZ$20 worth, and confirm it arrives before sending the rest. Crypto transactions are irreversible, and an address pasted onto the wrong network is money gone with no support ticket that will bring it back. Every experienced user does this. Do it every time the address changes.</p></li>
<li><h4>Match the network at both ends</h4><p>The single most common and most expensive mistake. USDT exists on Tron, Ethereum, Solana and others; sending TRC-20 USDT to an ERC-20 address usually loses it permanently. The casino&rsquo;s deposit page states the network &mdash; read it.</p></li>
<li><h4>Withdraw to the same wallet</h4><p>Most operators require withdrawals to return to the depositing wallet for anti-money-laundering reasons. Use an address you control rather than sending directly to an exchange deposit address, some of which reject third-party transfers.</p></li>
<li><h4>Keep records for tax</h4><p>Note the NZD value when you buy and when you convert back. The gambling win is not taxable; a gain in the crypto&rsquo;s value can be. See our <a href="/gambling-winnings-tax-nz/">tax guide</a>.</p></li>
</ol>
</div></div></section>

<section class="sec sec--haze"><div class="wrap">
<div class="sec-head"><span class="kicker">Honestly</span><h2>Crypto casinos: what is genuinely better and what is hype</h2></div>
<div class="grid grid--2">
<div class="card"><div class="card-ic">{icon("bolt")}</div><h3>Genuinely better</h3>
<ul style="margin-bottom:0">
<li><strong>Speed.</strong> Ten minutes to six hours against one to five business days. This is not marginal.</li>
<li><strong>No bank declines.</strong> Crypto bypasses the New Zealand banks that increasingly refuse gambling merchant transactions.</li>
<li><strong>No conversion spread.</strong> A stablecoin deposit avoids the 2&ndash;3% each way that a euro-denominated account costs you.</li>
<li><strong>Zero-wagering offers.</strong> Crypto-native sites such as <a href="/casino-reviews/spino/">Spino</a> offer terms &mdash; 0x wagering &mdash; that fiat casinos simply do not.</li>
<li><strong>Provably fair in-house games.</strong> Verifiable by you, not by a certificate.</li>
</ul></div>
<div class="card"><div class="card-ic">{icon("scale")}</div><h3>Overstated or untrue</h3>
<ul style="margin-bottom:0">
<li><strong>&ldquo;Anonymous.&rdquo;</strong> Largely a myth in 2026. Expect identity verification before any meaningful withdrawal.</li>
<li><strong>&ldquo;No tax.&rdquo;</strong> The <em>win</em> is not taxed. The <em>crypto gain</em> can be. This is the opposite of simpler.</li>
<li><strong>&ldquo;Better odds.&rdquo;</strong> The same Pragmatic and Hacksaw games run at the same RTP. Crypto changes the payment rail, not the maths.</li>
<li><strong>&ldquo;Provably fair everything.&rdquo;</strong> Applies only to in-house games, which are a small slice of most lobbies.</li>
<li><strong>Price risk is real.</strong> A volatile coin can cost you more overnight than the house edge does all week.</li>
</ul></div>
</div>
</div></section>
'''
    return shell(
        "Best Crypto Casinos NZ 2026 | Bitcoin &amp; USDT Casino Sites",
        "The best crypto casinos for New Zealand players in 2026. Compare Bitcoin, USDT and Litecoin casinos "
        "on payout speed, provably fair games and zero-wagering bonuses — plus the NZ tax rules that catch "
        "crypto players out.",
        "/crypto-casinos-nz/",
        [("Online Casinos NZ", "/online-casinos/"), ("Crypto Casinos NZ", "/crypto-casinos-nz/")],
        "Crypto Casinos NZ: Best Bitcoin Casino Sites [" + MONTH_YEAR + "]",
        "Crypto is the fastest way to get money out of an online casino and into a New Zealand wallet &mdash; "
        "ten minutes at the best sites against several days by bank. Here is which coins to use, which casinos "
        "handle them properly, and the New Zealand tax wrinkle that catches people out.",
        icon("lock") + " Crypto payouts from 10 minutes", ops,
        "Best crypto casino NZ sites: Bitcoin, Ethereum and USDT compared",
        "Ranked on coin support, withdrawal speed on-chain, provably fair coverage and whether the site handles "
        "stablecoins properly.",
        body, faq, author="holly-mcgrath",
        stats=[("10 min", "Fastest crypto payout"), ("0x", "Wagering at Spino"),
               ("USDT", "The coin we recommend"), ("Property", "IRD's view of crypto")])


# ======================================================== CASINO BONUSES
def bonuses():
    ops = [BY[s] for s in ["smash", "spino", "crownslots", "kingdom", "lucky7even",
                           "spinjo", "rivo", "fortune-play", "roby-casino", "lucky-vibe"]]
    faq = [
     ("What is the best casino bonus in NZ right now?",
      "<p>On terms rather than headline, <a href='/casino-reviews/smash/'>Smash</a> at "
      "<strong>10x wagering</strong> and <a href='/casino-reviews/spino/'>Spino</a> at "
      "<strong>0x on its crypto offer</strong> are the two genuinely good offers available to New Zealanders. "
      "<a href='/casino-reviews/crownslots/'>CrownSlots</a> has the largest headline at 390% up to €3,700, but "
      "at 40x on a euro balance. The largest number and the best offer are rarely the same thing.</p>"),
     ("What does 40x wagering actually mean?",
      "<p>You must wager the bonus amount 40 times before any of it &mdash; or anything won with it &mdash; can "
      "be withdrawn. A NZ$100 bonus at 40x requires <strong>NZ$4,000</strong> of turnover. If the requirement "
      "applies to deposit <em>plus</em> bonus and you deposited NZ$100, it is NZ$8,000. At a 96% RTP you should "
      "expect to lose roughly 4% of that turnover getting there, which is why very large bonuses at high "
      "multipliers are frequently worth less than nothing.</p>"),
     ("Are casino bonuses worth taking at all?",
      "<p>Sometimes. A bonus at 10x or below with 100% pokies contribution and a 30-day window is genuinely "
      "positive value. A bonus at 40x or above, especially on deposit plus bonus, usually is not once you price "
      "the expected loss on the turnover. And every bonus locks your balance until it clears, which has a cost "
      "of its own. Declining the bonus is a legitimate, sometimes optimal, choice &mdash; and it is always "
      "optional.</p>"),
     ("What is the maximum bet rule and why does it void bonuses?",
      "<p>Almost every bonus caps your stake while wagering, usually at NZ$5 to NZ$8 per spin. Exceed it even "
      "once &mdash; including accidentally via an autoplay setting or a bonus buy &mdash; and most operators "
      "void the bonus and every dollar won from it. This is the most common reason a bonus is confiscated, and "
      "in almost every case we have investigated it was the player&rsquo;s error rather than an operator trick. "
      "Check the cap and set your stake below it before you spin.</p>"),
     ("Do all games count toward wagering?",
      "<p>No, and the differences are large. Pokies usually contribute 100%, live dealer games commonly 10%, "
      "table games 5&ndash;20%, and progressive jackpots and some crash titles are excluded entirely. Clearing "
      "40x on live blackjack at 10% contribution means 400x of real turnover &mdash; not a realistic "
      "proposition. The contribution table is in the bonus terms and it is worth thirty seconds of your "
      "time.</p>"),
     ("Can I withdraw my deposit if I do not finish the wagering?",
      "<p>It depends on how the operator structures it. Where deposit and bonus funds are kept in separate "
      "wallets, you can usually cancel the bonus and withdraw your own deposit, forfeiting the bonus and "
      "anything won with it. Where the funds are combined &mdash; increasingly common &mdash; cancelling may "
      "forfeit everything above your original deposit or, at the worst operators, the lot. Check which model a "
      "casino uses <em>before</em> you accept the offer.</p>"),
    ]
    body = f'''<section class="sec sec--haze"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">Compared properly</span>
<h2>Every welcome bonus on this site, clause by clause</h2>
<p>The headline is the least useful number in the table. Read the turnover column.</p>
{table(["Casino","Headline offer","Wagering","Applies to","Real turnover on NZ$200","Max bet","Expiry"], [
 ["<a href='/casino-reviews/smash/'>Smash</a>","600% to NZ$19,500","<b>10x</b>","Deposit + bonus","<b>NZ$4,000</b>","NZ$5","30 days"],
 ["<a href='/casino-reviews/spino/'>Spino</a>","To 2,000 USDT","<b>0x</b>","—","<b>None</b>","—","—"],
 ["<a href='/casino-reviews/kingdom/'>Kingdom</a>","600% to NZ$18,500","30x","Bonus only","NZ$6,000","NZ$5","30 days"],
 ["<a href='/casino-reviews/rivo/'>Rivo</a>","To NZ$4,500 + 250 FS","35x","Bonus only","NZ$7,000","NZ$5","30 days"],
 ["<a href='/casino-reviews/lucky-circus/'>Lucky Circus</a>","To NZ$2,500 + 150 FS","35x","Bonus only","NZ$7,000","NZ$5","21 days"],
 ["<a href='/casino-reviews/ivibet/'>Ivibet</a>","100% to NZ$500 + 50 FS","35x","Bonus only","NZ$7,000","NZ$6","14 days"],
 ["<a href='/casino-reviews/spinjo/'>Spinjo</a>","To NZ$5,000 + 300 FS","40x","Bonus only","NZ$8,000","NZ$5","30 days"],
 ["<a href='/casino-reviews/crownslots/'>CrownSlots</a>","390% to €3,700 + 175 FS","40x","Bonus only","NZ$8,000","NZ$5","21 days"],
 ["<a href='/casino-reviews/fortune-play/'>Fortune Play</a>","To NZ$5,000 + 300 FS","40x","Bonus only","NZ$8,000","NZ$5","30 days"],
 ["<a href='/casino-reviews/lucky7even/'>Lucky7even</a>","20 no-dep + 100% to NZ$1,700","40x / 50x FS","Bonus only","NZ$8,000","NZ$5","21 days"],
 ["<a href='/casino-reviews/roby-casino/'>Roby</a>","250% to NZ$5,000 + 250 FS","<b>45x</b>","Bonus only","<b>NZ$9,000</b>","NZ$5","14 days"],
], minw=1020)}
<p style="font-size:.86rem;color:var(--mute)">&ldquo;Real turnover&rdquo; assumes a NZ$200 deposit with a 100% match where the headline allows it, to give a like-for-like comparison. Terms are as published at our last check on {UPDATED_NZ}.</p>
</div></div></section>

<section class="sec"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">Types</span>
<h2>The bonus formats you will encounter</h2>
<h3>Welcome and sign up bonuses</h3>
<p>A casino sign up bonus NZ operators advertise is almost always this shape: the casino matches a percentage of your deposit in bonus funds. Modern packages spread the match across two to four deposits, which is how a &ldquo;600%&rdquo; headline is constructed &mdash; it is 100% + 150% + 150% + 200% across four separate deposits, and reaching the advertised maximum requires depositing several thousand dollars. Judge it on the first-deposit terms, which is the only part most players will ever use.</p>
<h3>Low deposit bonuses: $1, $5 and $10</h3>
<p>Deposit-tier offers are searched constantly in New Zealand and are mostly worse value than they look, though not for the reason people expect. The deposit floor is rarely the problem. Three things decide whether a <strong>$1 deposit casino NZ</strong> offer, or a $5 or $10 one, is worth claiming:</p>
<ul>
<li><strong>The minimum qualifying deposit for the bonus.</strong> Plenty of sites accept a NZ$1 deposit and then require NZ$20 or NZ$30 before the match triggers at all, so the dollar earns you nothing.</li>
<li><strong>The withdrawal floor.</strong> Frequently NZ$50 or NZ$100 against a NZ$1 deposit, which strands any small balance until it is played away. <a href="/casino-reviews/lucky-circus/">Lucky Circus at NZ$10 in and NZ$10 out</a> is the only genuinely matched pair on this site.</li>
<li><strong>The multiplier, which matters more at small stakes.</strong> A 100% match on NZ$20 at 10x is NZ$400 of turnover and achievable. The same NZ$20 at 45x is NZ$1,800, which will consume the balance before it clears.</li>
</ul>
<h3>Free spins</h3>
<p>Spins on a nominated pokie, usually valued at NZ$0.10 to NZ$0.30 each. 300 free spins at NZ$0.20 is NZ$60 of play, not NZ$300 &mdash; and winnings are typically subject to their own wagering requirement plus a maximum conversion cap. Check the per-spin value and the cap; together they usually reduce a headline free spin offer to a fraction of what it appears.</p>
<h3>No deposit bonus</h3>
<p>The one format this page does not cover, because it has its own. A no deposit bonus is credited on registration before you fund the account, and the terms behave differently enough &mdash; higher wagering, a maximum cashout cap, a deposit required before withdrawal &mdash; that comparing it against a welcome bonus is comparing two different products. Everything on no deposit bonus NZ offers, free spins no deposit and no deposit bonus codes lives on our <a href="/no-deposit-bonus/">no deposit bonus page</a>.</p>
<h3>Cashback</h3>
<p>A percentage of net losses returned, usually weekly, and frequently with <strong>no wagering requirement at all</strong> &mdash; which makes it the most genuinely valuable ongoing promotion in this industry. A 10% cashback on a 96% RTP game improves your effective return to roughly 96.4%. <a href="/casino-reviews/lucky-vibe/">Lucky Vibe</a> is strongest here because cashback starts at the entry tier.</p>
<h3>Reload bonus</h3>
<p>A smaller match on subsequent deposits, often weekly. Generally better terms than the welcome offer because the percentages are lower, and worth more over a year than the one-off headline you signed up for.</p>
<h3>VIP and loyalty schemes</h3>
<p>Tiered programmes converting play into points, then points into cash, spins or perks. Assess the exchange rate rather than the tier names &mdash; a scheme returning 0.2% of turnover is marketing, one returning 1%+ with a low tier threshold is real value.</p>
</div></div></section>

<section class="sec sec--haze"><div class="wrap">
<div class="sec-head"><span class="kicker">Read this first</span><h2>The six clauses that decide whether a bonus is any good</h2></div>
{cards([
 ("coin","1. Wagering multiplier","10x is excellent, 35x is fair, 40x is the norm, 45x+ is poor. Below 10x is exceptional and worth going out of your way for."),
 ("scale","2. What it applies to","&ldquo;Bonus only&rdquo; is roughly half the work of &ldquo;deposit plus bonus&rdquo;. A 20x deposit+bonus requirement equals a 40x bonus-only one. Always check which."),
 ("shield","3. Maximum bet while wagering","Usually NZ$5–8. Breach it once and the bonus and all winnings from it are typically void. The most common cause of a confiscated bonus, and almost always the player's error."),
 ("dice","4. Game contribution","Pokies 100%, live dealer often 10%, table games 5–20%, jackpots and some crash titles excluded. Clearing 40x at 10% contribution is not realistic."),
 ("clock","5. Expiry window","30 days is workable, 14 is tight, 7 days on a four-figure turnover is not a real offer. Unused bonus funds and spins expire silently."),
 ("lock","6. Maximum conversion","A cap on what bonus or free spin winnings can become — sometimes as low as 5x the bonus. This clause can make a large offer worthless and it is always in the fine print."),
])}
<div class="note note--amber" style="margin-top:26px"><b>The question to ask before accepting any bonus</b>
<p>&ldquo;Do I intend to put this much money through this casino anyway?&rdquo; If yes, the bonus is free upside and you should take it. If no, you are being paid to gamble more than you planned, which is a bad trade at any multiplier. Bonuses are opt-in everywhere on this site, and declining one keeps your balance withdrawable at any moment &mdash; which for a lot of players is worth more than the bonus.</p></div>
</div></section>
'''
    return shell(
        "Casino Bonuses NZ 2026 | Best Welcome Offers Compared Clause by Clause",
        "Every NZ casino welcome bonus compared on the terms that matter: wagering multiplier, what it applies "
        "to, max bet, game contribution and expiry. Worked examples in NZD, no hype.",
        "/casino-bonus/",
        [("Online Casinos NZ", "/online-casinos/"), ("Casino Bonus NZ", "/casino-bonus/")],
        "Casino Bonus NZ: Best Welcome Offers Compared [" + MONTH_YEAR + "]",
        "A 600% bonus is not six times better than a 100% one. This page compares every welcome offer available "
        "to New Zealanders on the terms that actually decide its value &mdash; wagering, contribution, max bet, "
        "expiry and win caps &mdash; with the arithmetic worked through in New Zealand dollars.",
        icon("coin") + " 11 offers compared clause by clause", ops,
        "Best casino bonuses NZ: welcome and sign up bonus offers ranked",
        "Ranked on bonus terms rather than headline size. The top two offers here have the smallest numbers "
        "and by some distance the best value.",
        body, faq,
        stats=[("10x", "Best wagering"), ("0x", "Spino's crypto offer"),
               ("45x", "Worst on this page"), ("NZ$5", "Typical max bet")])


# ==================================================== NO DEPOSIT CASINOS
def no_deposit():
    ops = [BY[s] for s in ["lucky7even", "spino", "smash", "hellspin", "ivibet",
                           "spinjo", "lucky-circus", "slotsgem"]]
    faq = [
     ("Is there a genuine no deposit bonus for NZ players?",
      "<p>Yes, but only one on this site. <a href='/casino-reviews/lucky7even/'>Lucky7even credits 20 free "
      "spins</a> on registration with no deposit required. That is the only true no-deposit offer we could "
      "verify as live for New Zealand players at our last check. Everything else advertised as &lsquo;no "
      "deposit&rsquo; in this market turns out on inspection to require a deposit, a card on file, or to have "
      "expired.</p>"),
     ("Can I actually withdraw no deposit bonus winnings?",
      "<p>In principle yes, in practice rarely at a meaningful amount. No-deposit offers carry two clauses that "
      "work together: a <strong>high wagering requirement</strong> (50x on Lucky7even&rsquo;s spin winnings) and "
      "a <strong>maximum conversion cap</strong>, often NZ$50 to NZ$100 no matter how much you win. Win NZ$400 "
      "from 20 free spins and you may be able to keep NZ$100 of it after clearing 50x. That is the design, not "
      "a malfunction.</p>"),
     ("Why do casinos offer no deposit bonuses at all?",
      "<p>Customer acquisition. The cost of 20 free spins is a few dollars; the value of a verified account with "
      "your details in it is considerably more. Almost every no-deposit offer also requires you to make a "
      "deposit before any withdrawal can be processed, which is the actual conversion mechanism and is usually "
      "disclosed several paragraphs into the terms.</p>"),
     ("Do I have to give card details for a no deposit bonus?",
      "<p>Not for Lucky7even&rsquo;s offer &mdash; registration alone. Some operators do require a card on file "
      "for verification, which is legitimate but changes the nature of the offer. Read what is being asked "
      "before you sign up, and be sceptical of any &lsquo;free&rsquo; offer that wants payment details "
      "up front.</p>"),
     ("Are free spins the same as a no deposit bonus?",
      "<p>Not necessarily. Free spins come in both shapes: <strong>no-deposit spins</strong> credited on "
      "registration, and far more commonly <strong>deposit spins</strong> credited as part of a welcome package "
      "after you fund the account. Most &lsquo;300 free spins&rsquo; headlines are the second kind. Check "
      "whether a deposit is required before you count them as free.</p>"),
     ("What is the catch with no deposit bonuses?",
      "<p>There are four, and they are all standard: high wagering (40&ndash;60x), a low maximum conversion cap, "
      "a requirement to deposit before withdrawing, and a short expiry. None of these is hidden or improper "
      "&mdash; they are all in the terms. The mistake is treating the offer as a free shot at real money rather "
      "than as what it is: a free look at the lobby before you decide whether to fund an account.</p>"),
    ]
    body = f'''<section class="sec sec--haze"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">Straight answer</span>
<h2>The honest state of no deposit bonus NZ offers</h2>
<p>Search &ldquo;no deposit bonus NZ&rdquo; and you will find dozens of pages listing twenty or thirty offers. We checked as many as we could and the great majority were expired, geo-blocked for New Zealand, or required a deposit despite the heading. This is a category where the listings have drifted a long way from reality.</p>
<p>Here is what we could actually verify as live for a New Zealand player:</p>
{table(["Casino","Offer","Deposit needed?","Wagering","Max you can keep","Expires"], [
 ["<a href='/casino-reviews/lucky7even/'>Lucky7even</a>","<b>20 free spins on registration</b>","<span class='t-yes'>No</span>","50x on winnings","NZ$100","7 days"],
], minw=680)}
<p>One offer. We would rather publish one verified offer than thirty unverified ones, and the fact that most competing pages list far more should tell you something about how often those pages are checked.</p>
<div class="note"><b>What to do instead</b>
<p>If your goal is to try a casino before committing money, <strong>demo mode is better than any no-deposit bonus</strong>. Almost every pokie on every site runs in play-money mode with identical maths, no registration, no wagering requirement and no cap. You lose nothing and learn the same thing. The genuine value of a no-deposit bonus is the small chance of turning it into real money &mdash; which the conversion cap is specifically designed to limit.</p></div>
</div></div></section>

<section class="sec"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">Worked through</span>
<h2>What 20 free spins is actually worth</h2>
<p>Take Lucky7even&rsquo;s offer, which is the best available, and follow the arithmetic all the way through.</p>
<ul>
<li><strong>20 spins at NZ$0.20 each</strong> = NZ$4.00 of play.</li>
<li>At a 96% RTP, the expected return is about <strong>NZ$3.84</strong>.</li>
<li>Those winnings carry <strong>50x wagering</strong>. If you win NZ$10, you must turn over NZ$500 before withdrawing.</li>
<li>Generating NZ$500 of turnover at 96% RTP costs about NZ$20 in expectation &mdash; more than the NZ$10 you are trying to release.</li>
<li>And the maximum conversion is <strong>NZ$100</strong> regardless of how much you win.</li>
</ul>
<p>The expected value is slightly negative once you account for the wagering. What the offer genuinely buys you is <em>variance</em>: a small chance of a large enough win that clearing 50x against a NZ$100 cap becomes worthwhile. That is a real if modest thing, and it is free. Just do not build a plan around it.</p>
<h3>Where the actual value sits</h3>
<p>If you are going to deposit anyway, the offers worth your attention are the low-wagering welcome bonuses rather than anything labelled no-deposit. <a href="/casino-reviews/smash/">Smash at 10x</a> and <a href="/casino-reviews/spino/">Spino at 0x</a> are worth many times more than every no-deposit offer in this market combined, because they apply to money you were going to stake regardless. Our <a href="/casino-bonus/">casino bonuses page</a> compares all of them.</p>
</div></div></section>

<section class="sec sec--haze"><div class="wrap">
<div class="sec-head"><span class="kicker">Spot the difference</span><h2>Free spins no deposit vs deposit free spins</h2>
<p>Not all &ldquo;free spins&rdquo; are free, and the per-spin value varies more than the headline count.</p></div>
{table(["Casino","Free spins","Deposit required?","Value per spin","Total play value","Wagering on winnings"], [
 ["<a href='/casino-reviews/lucky7even/'>Lucky7even</a>","20 (+ more on deposit)","<span class='t-yes'>No</span>","NZ$0.20","NZ$4.00","50x"],
 ["<a href='/casino-reviews/spinjo/'>Spinjo</a>","300","<span class='t-no'>Yes</span>","NZ$0.20","NZ$60.00","40x"],
 ["<a href='/casino-reviews/fortune-play/'>Fortune Play</a>","300","<span class='t-no'>Yes</span>","NZ$0.20","NZ$60.00","40x"],
 ["<a href='/casino-reviews/rivo/'>Rivo</a>","250","<span class='t-no'>Yes</span>","NZ$0.20","NZ$50.00","35x"],
 ["<a href='/casino-reviews/crownslots/'>CrownSlots</a>","175","<span class='t-no'>Yes</span>","€0.10","~NZ$32","40x"],
 ["<a href='/casino-reviews/hellspin/'>Hellspin</a>","150","<span class='t-no'>Yes</span>","NZ$0.20","NZ$30.00","40x"],
 ["<a href='/casino-reviews/slotsgem/'>Slotsgem</a>","100","<span class='t-no'>Yes</span>","NZ$0.20","NZ$20.00","40x"],
], minw=880)}
<p>Note what this table shows: <strong>300 free spins is NZ$60 of play</strong>, not NZ$300. Once you internalise the per-spin value, free spin headlines stop being persuasive and start being merely informative &mdash; which is the right way to read them.</p>
</div></section>

<section class="sec"><div class="wrap"><div class="prose prose--wide">
<span class="kicker">The terms</span>
<h2>No deposit bonus codes, max cashout and wagering explained</h2>
<h3>Do you need a no deposit bonus code?</h3>
<p>Almost never in this market. Where a no deposit bonus NZ offer is live, it is credited automatically on registration &mdash; Lucky7even&rsquo;s 20 free spins on sign up work that way. Pages advertising exclusive <strong>no deposit bonus codes NZ</strong> are usually republishing either the standard offer or an expired one. If a code is genuinely required, it will be stated on the operator&rsquo;s own promotions page, which is the only place worth checking.</p>
<h3>What does maximum cashout mean?</h3>
<p>It is the hard ceiling on what a no deposit bonus can ever become, regardless of what you win. NZ$50 to NZ$100 is typical. Win NZ$400 from free spins on registration and clear the wagering, and you still withdraw NZ$100. This single clause is what separates a no deposit bonus from free money, and it is the reason we describe these offers as a free look at the lobby rather than a route to a payout.</p>
<h3>Can you withdraw no deposit bonus winnings?</h3>
<p>Yes, subject to three conditions that apply together: clear the wagering requirement (typically 40&ndash;60x, against 35&ndash;40x on a deposit bonus), stay under the maximum cashout, and in most cases <strong>make a qualifying deposit first</strong>. That last requirement is the actual conversion mechanism and it is usually disclosed several paragraphs into the terms rather than on the banner.</p>
<h3>Free spins no deposit NZ: what is actually available</h3>
<p>One offer, verified. Free spins no deposit NZ players can genuinely claim means Lucky7even&rsquo;s 20 spins on registration &mdash; every other no deposit casino NZ listing we checked was expired, geo-blocked or required a deposit despite the heading. We would rather publish one verified offer than thirty unverified ones.</p>

<h3>Free spins on registration with no card details</h3>
<p>Lucky7even&rsquo;s offer needs registration only &mdash; no card on file. Some operators do ask for a card for verification, which is legitimate but changes the nature of a &ldquo;free&rdquo; offer. Be sceptical of anything requiring payment details before it will credit a no deposit bonus, and read what you are agreeing to before you enter them.</p>
<h3>Keep what you win, and no wagering claims</h3>
<p>A genuine <strong>no deposit bonus you keep what you win from</strong> would have no wagering and no cashout cap. We could not verify one available to New Zealand players. The closest equivalent is a <strong>zero-wagering deposit offer</strong> &mdash; <a href="/casino-reviews/spino/">Spino&rsquo;s 0x crypto welcome bonus</a> &mdash; where winnings are withdrawable immediately. It requires a deposit, but the money is genuinely yours the moment it lands, which no no-deposit offer in this market can say.</p>
</div></div></section>
'''
    return shell(
        "No Deposit Bonus Casinos NZ 2026 | Verified Free Offers Only",
        "We checked every no deposit bonus advertised to New Zealand players and found one that is genuinely "
        "live. Here it is, with the wagering, the cap and the arithmetic stated plainly.",
        "/no-deposit-bonus/",
        [("Online Casinos NZ", "/online-casinos/"), ("No Deposit Bonus NZ", "/no-deposit-bonus/")],
        "No Deposit Bonus NZ: Free Spins No Deposit [" + MONTH_YEAR + "]",
        "Most &ldquo;no deposit bonus&rdquo; pages list thirty offers that no longer exist. We checked, and "
        "found exactly one live for New Zealand players. This page tells you what it is, what it is worth once "
        "the wagering and the cap are applied, and what to do instead.",
        icon("star") + " Every offer verified, not copied", ops,
        "No deposit casino NZ offers and free spins on sign up",
        "The one verified no-deposit offer first, then the deposit-based free spin packages ranked on real "
        "per-spin value rather than headline count.",
        body, faq,
        stats=[("1", "Verified no-dep offer"), ("NZ$4", "What 20 spins is worth"),
               ("50x", "Wagering on winnings"), ("NZ$100", "Conversion cap")])


def build():
    return [pokies(), fast_payout(), high_payout(), live_casinos(), crypto(), bonuses(), no_deposit()]
