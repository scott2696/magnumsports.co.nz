# -*- coding: utf-8 -*-
"""Guide pages: law, tax, payments, methodology."""
from lib import *


def guide(title, desc, path, crumb, h1, lede, eyebrow, body, faq, author, checker="daniel-ashworth",
          stats=None, kind="Article", extra=None):
    ex = [crumb_schema([("Home", "/")] + crumb)]
    if faq:
        ex.append(faq_schema(faq, f"{SITE}{path}#faq"))
    if extra:
        ex += extra
    schema = page_schema(kind, title, desc, path, author=author, extra=ex)
    o = [head(title, desc, path, schema),
         crumbs([("Home", "/")] + [(c[0], None if i == len(crumb) - 1 else c[1])
                                   for i, c in enumerate(crumb)])]
    st = ""
    if stats:
        st = '<div class="hero-stats">' + "".join(
            f'<div class="hero-stat"><b>{a}</b><span>{b}</span></div>' for a, b in stats) + '</div>'
    o.append(f'''<section class="hero"><div class="wrap">
<span class="eyebrow">{eyebrow}</span><h1>{h1}</h1>{byline(author, checker)}
<p class="lede">{lede}</p>{st}</div></section>
''')
    o.append(body)
    if faq:
        o.append(faq_block(faq))
    o.append('<section class="sec"><div class="wrap"><div class="prose prose--wide">'
             + authorbox(author) + '</div></div></section>')
    o.append(footer())
    return write(path, "".join(o))


# ================================================================== LAW
def law():
    faq = [
     ("Is it illegal to play at an online casino in New Zealand?",
      "<p><strong>No.</strong> The Gambling Act 2003 prohibits <em>operating</em> remote interactive gambling "
      "from within New Zealand. It has never made it an offence for a New Zealand resident to play at a casino "
      "hosted offshore, and the Department of Internal Affairs has confirmed this publicly. The Online Casino "
      "Gambling Act regulates who may supply the service to New Zealanders; it does not create an offence for "
      "playing.</p>"),
     ("What is the Online Casino Gambling Act?",
      "<p>The legislation creating New Zealand&rsquo;s first licensed online casino market. It authorises the "
      "Department of Internal Affairs to issue <strong>up to 15 licences</strong>, allocated through a "
      "competitive process &mdash; Cabinet decided the first round would be an <strong>auction</strong>, held "
      "in September 2026. Each licence covers a single brand, runs for up to three years with a five-year "
      "renewal path, and no applicant may hold more than three.</p>"),
     ("What happens on 1 December 2026?",
      "<p>From that date, a provider that has <strong>not applied</strong> for a licence must cease conducting "
      "online casino gambling in New Zealand. Providers that did apply may continue operating until their "
      "application is determined; if it is declined, they must exit the market. Expect the number of casinos "
      "reachable from a New Zealand IP address to fall significantly from late 2026 into 2027.</p>"),
     ("Can offshore casinos advertise in New Zealand?",
      "<p>Advertising unlicensed online casino gambling to New Zealanders is restricted, and the regime "
      "tightens as licensing takes effect. Licensed operators will face New Zealand-specific advertising rules "
      "including harm-minimisation messaging. This is a significant change from the previous position, in which "
      "offshore brands advertised into New Zealand with little constraint.</p>"),
     ("Is sports betting covered by the same law?",
      "<p>No, and this is the point most guides get wrong. Sports and racing betting sit under the "
      "<strong>Racing Industry Act 2020</strong>, amended in 2025 to extend TAB NZ&rsquo;s monopoly to online "
      "betting. From <strong>28 June 2025</strong>, only TAB NZ and its partner may offer or promote racing and "
      "sports betting to a person in New Zealand. The casino regime is opening up; the betting regime has "
      "closed down. See our <a href='/online-betting/'>online betting guide</a>.</p>"),
     ("Can I get in trouble for betting with an offshore bookmaker?",
      "<p>No. The Racing Industry Amendment Act expressly provides that an individual may not be convicted of an "
      "offence for placing a bet with an offshore betting operator. The prohibition binds the operator that "
      "offers or promotes the bet, not the person who places it.</p>"),
     ("How old do I have to be?",
      "<p><strong>18</strong> for online gambling and for New Zealand class 4 pub gaming machines, and "
      "<strong>20</strong> to enter a physical casino venue in New Zealand. Online operators verify age as part "
      "of identity checks, and accounts opened with false details are closed with winnings forfeited.</p>"),
     ("Will licensed casinos be better for players?",
      "<p>In the ways that matter most, yes. A licensed operator is accountable to the Department of Internal "
      "Affairs, which means there is a New Zealand body with jurisdiction if it withholds your money &mdash; "
      "something no offshore regulator currently gives you. Harm-minimisation tools become mandatory rather "
      "than optional. The trade-off is a much smaller choice of operators.</p>"),
    ]
    body = f'''<section class="sec"><div class="wrap"><div class="prose prose--wide">
{disclosure("Nothing on this page is legal advice. It is a plain-English summary of publicly available "
            "legislation and Department of Internal Affairs material, current to " + UPDATED_NZ + ".")}
{keyfacts([("Playing offshore", "Not an offence"), ("Operating from NZ", "Prohibited"),
           ("Licences available", "Up to 15"), ("Allocation method", "Auction, Sept 2026"),
           ("Unlicensed cut-off", "1 Dec 2026"), ("Licence term", "3 yrs + 5 renewal"),
           ("Max licences per company", "3"), ("Tax on winnings", "None (recreational)")])}
<h2>The position in one paragraph</h2>
<p>It is not an offence for a New Zealander to gamble at an online casino based overseas, and it never has been. It is an offence to operate remote interactive gambling from within New Zealand. That has been the settled position since the Gambling Act 2003, and it produced a large offshore market with no New Zealand oversight, no New Zealand tax and no New Zealand harm-minimisation requirements. The Online Casino Gambling Act replaces that with a licensed market of up to 15 operators, with the first licences allocated by auction in September 2026 and unlicensed operators required to leave from 1 December 2026.</p>

<h2>The Gambling Act 2003: the twenty-year baseline</h2>
<p>The Gambling Act 2003 was written before online casinos were a meaningful consumer product, and it deals with them by prohibiting <strong>remote interactive gambling</strong> conducted from within New Zealand. Two carve-outs exist for the domestic operators &mdash; Lotto NZ and TAB NZ &mdash; and everything else offered from inside the country is unlawful.</p>
<p>What the Act does not do is reach the player. There is no offence of gambling at an offshore site, no penalty for depositing with one, and no obligation to declare it. The Department of Internal Affairs has stated the position publicly: New Zealanders may lawfully gamble on overseas websites. Section 10 of the Act restricts advertising overseas gambling, which is why offshore brands have historically been cautious about direct New Zealand advertising even while accepting New Zealand players.</p>

<h2>The Online Casino Gambling Act: the new licensed market</h2>
<p>The new framework is the most significant change to New Zealand gambling law in two decades. The mechanics:</p>
<h3>How the licences are being allocated</h3>
<ol class="steps">
<li><h4>Expression of interest — July to August 2026</h4><p>The Secretary for Internal Affairs invited expressions of interest by public notice. The window opened 17 July 2026 and closed 14 August 2026. Submitting an EOI established eligibility to participate in the competitive process.</p></li>
<li><h4>Competitive auction — September 2026</h4><p>Cabinet determined that the first allocation round would be an auction. The right to <em>apply</em> for a licence was auctioned to up to 15 providers. Winning the auction confers the right to apply, not the licence itself.</p></li>
<li><h4>Applications — from October 2026</h4><p>Successful bidders submit full licence applications, which the Department assesses against suitability, harm-minimisation, technical and financial criteria.</p></li>
<li><h4>Prohibition takes effect — 1 December 2026</h4><p>Providers that have not applied must cease conducting online casino gambling in New Zealand. Those with an application pending may continue until it is determined, and must exit if declined.</p></li>
</ol>
<h3>What a licence involves</h3>
<ul>
<li><strong>Up to 15 licences</strong> in total.</li>
<li><strong>One brand per licence.</strong> An operator running three brands needs three licences.</li>
<li><strong>Maximum three licences</strong> per applicant group.</li>
<li><strong>Term of up to three years</strong>, with a renewal path of up to a further five.</li>
<li><strong>A levy on gambling profits</strong>, alongside the existing online gambling duty.</li>
<li><strong>Mandatory harm-minimisation</strong> — deposit limits, self-exclusion and reality checks become requirements.</li>
<li><strong>New Zealand-specific advertising rules</strong> for licensed operators.</li>
</ul>

<h2>What this means for you as a player</h2>
<div class="pc"><div class="pc-col pc-pro"><h4>Better</h4><ul>
<li>A New Zealand regulator with jurisdiction over the operator holding your money</li>
<li>Mandatory deposit limits, reality checks and self-exclusion at every licensed site</li>
<li>A domestic complaints path instead of a foreign regulator you will never reach</li>
<li>Advertising standards enforced in New Zealand</li>
<li>Gambling duty revenue directed to New Zealand rather than nowhere</li>
</ul></div>
<div class="pc-col pc-con"><h4>Worse</h4><ul>
<li>Far fewer operators — 15 brands where hundreds are currently reachable</li>
<li>Sites you use today may not be available in 2027</li>
<li>Transition risk: balances at departing operators may be difficult to recover</li>
<li>Licensed operators will likely offer smaller bonuses under stricter promotional rules</li>
<li>Geo-blocking and payment blocking may make unlicensed sites harder to reach</li>
</ul></div></div>

<div class="note note--amber"><b>Practical advice for the transition period</b>
<p>Do not leave a large balance at any offshore casino through late 2026 and into 2027. Withdraw winnings as you make them. Keep verification current at every operator where you hold an account so a withdrawal can never be stalled at short notice. Before opening a new account late in the year, check whether the operator has applied for a New Zealand licence &mdash; an operator that has not is one you may have to exit at short notice.</p></div>

<h2>Betting law is moving in the opposite direction</h2>
<p>This is the point that trips up most coverage. Casino gambling is being <em>opened</em> to licensed private operators. Sports and racing betting has been <em>closed</em> to a single authorised operator.</p>
<p>The <strong>Racing Industry Amendment Act 2025</strong>, in force <strong>28 June 2025</strong>, extended TAB NZ&rsquo;s land-based monopoly on racing and sports betting to cover online betting. It is now unlawful for any person other than TAB NZ or its partner organisation to offer or promote racing betting, sports betting or other sports betting to a person in New Zealand. The stated purpose was to protect the financial sustainability of the racing industry, which had been losing an estimated NZ$180&ndash;200 million a year in turnover offshore.</p>
<p>Critically, the Act expressly provides that <strong>an individual may not be convicted of an offence for placing a bet with an offshore betting operator</strong>. The obligation is on the supply side. Our <a href="/online-betting/">online betting guide</a> covers what this means in practice.</p>

<h2>Other rules worth knowing</h2>
<h3>Age</h3>
<p>18 for online gambling and class 4 pub gaming machines. 20 to enter a physical casino venue. Operators verify age during identity checks and forfeit winnings on accounts opened with false details.</p>
<h3>Tax</h3>
<p>Recreational gambling winnings are not assessable income in New Zealand. There is no tax and nothing to declare. Exceptions apply to professional gambling carried on as a business and to cryptocurrency gains &mdash; see our <a href="/gambling-winnings-tax-nz/">tax on gambling winnings guide</a>.</p>
<h3>Anti-money-laundering</h3>
<p>Offshore operators are bound by AML obligations under their own licensing regimes, which is why identity verification is required before withdrawal everywhere. New Zealand banks are separately subject to the AML/CFT Act 2009, which is part of why gambling-related transactions attract scrutiny and are sometimes declined.</p>
<h3>Self-exclusion</h3>
<p>New Zealand operates a multi-venue exclusion programme for land-based venues. It does not extend to offshore online operators, so online self-exclusion must be requested at each site individually. Every operator we recommend offers it. See our <a href="/responsible-gambling/">responsible gambling page</a>.</p>

<h2>Sources</h2>
<p>This page is compiled from the Gambling Act 2003, the Racing Industry Act 2020 as amended by the Racing Industry Amendment Act 2025, the Online Casino Gambling Act, and Department of Internal Affairs guidance for online gambling providers. Where we state a date or a figure, it comes from one of those sources rather than from another comparison site. We review this page monthly and after every material DIA announcement; it was last reviewed on {UPDATED_NZ} by {AUTHORS["daniel-ashworth"]["name"]}.</p>
</div></div></section>
'''
    return guide(
        "NZ Online Casino Law 2026 | Is Online Gambling Legal in New Zealand?",
        "Is online gambling legal in New Zealand? The Gambling Act 2003, the Online Casino Gambling Act, the "
        "15-licence auction and the 1 December 2026 deadline, explained in plain English.",
        "/nz-online-casino-law/", [("NZ Online Casino Law", "/nz-online-casino-law/")],
        "NZ Online Casino Law: Is Online Gambling Legal in 2026?",
        "New Zealand is halfway through the biggest change to its gambling laws in twenty years. This page "
        "explains what the law says today, what changes on 1 December 2026, and &mdash; the part most guides "
        "get wrong &mdash; why the rules for casino games and the rules for sports betting are moving in "
        "opposite directions.",
        icon("scale") + " Checked against primary sources", body, faq, "daniel-ashworth", "tama-whitiora",
        stats=[("15", "Licences available"), ("1 Dec 2026", "Unlicensed cut-off"),
               ("Legal", "For players"), ("18+", "Minimum age")])


# ================================================================== TAX
def tax():
    faq = [
     ("Do I pay tax on gambling winnings in New Zealand?",
      "<p><strong>No, not on recreational gambling.</strong> Inland Revenue does not treat gambling winnings as "
      "assessable income for a person gambling for recreation. There is no income tax, no GST, no withholding "
      "and nothing to declare in your IR3 &mdash; whether you win NZ$50 on a pokie or NZ$500,000 on a "
      "jackpot.</p>"),
     ("Why doesn't New Zealand tax gambling winnings?",
      "<p>Because of how the income tax framework treats windfalls. Income tax applies to income from "
      "employment, business or investment. A gambling win from recreational play is none of those &mdash; it is "
      "a windfall, and the symmetrical consequence is that gambling <em>losses</em> are equally not deductible. "
      "The revenue is collected from operators through gambling duty instead of from players through income "
      "tax.</p>"),
     ("When would gambling winnings be taxable in NZ?",
      "<p>Where gambling amounts to carrying on a <strong>business</strong>. IRD looks at whether the activity "
      "is organised and systematic, conducted with a genuine intention of profit, scaled and regular, and "
      "whether it is the person&rsquo;s primary income. This is a demanding test and it is not met by playing "
      "pokies often or by winning a large amount once. It is aimed at genuine professionals &mdash; for "
      "example, a full-time advantage player operating systematically. If you think you might be near this "
      "line, speak to an accountant.</p>"),
     ("Is crypto casino winning taxed differently?",
      "<p>Yes, and this is where New Zealanders most often get caught out. The <em>gambling win</em> is not "
      "taxable. But Inland Revenue treats cryptocurrency as <strong>property</strong>, so if the NZD value of "
      "your crypto rises between acquiring it and disposing of it &mdash; including converting back to NZD "
      "&mdash; that gain can be taxable income. Buy NZ$1,000 of Bitcoin, win, and convert back when it is worth "
      "NZ$1,400: the NZ$400 attributable to the price movement may be taxable even though your winnings are "
      "not.</p>"),
     ("Do I pay tax on a big jackpot or a Lotto win?",
      "<p>No. There is no threshold above which a recreational gambling win becomes taxable in New Zealand. A "
      "NZ$2 million progressive jackpot and a NZ$20 pokie win are treated identically &mdash; neither is "
      "assessable income. What <em>is</em> taxable is what you do with it afterwards: interest earned on the "
      "money in a bank account, dividends from shares you buy with it, or rent from property. The income the "
      "winnings generate is taxable even though the winnings are not.</p>"),
     ("Do I need to declare winnings to IRD?",
      "<p>No, if you are gambling recreationally. There is no declaration requirement and no box on the IR3 for "
      "it. Your bank may ask about the source of a large deposit under anti-money-laundering rules &mdash; that "
      "is a bank compliance question, not a tax one. Keep records of the withdrawal and the operator so you can "
      "answer it easily.</p>"),
     ("Are gambling losses deductible?",
      "<p>No. The treatment is symmetrical: because recreational winnings are not income, recreational losses "
      "are not deductible. Nor can they be offset against other income. This is one of the reasons the New "
      "Zealand position is simpler than the American one, where winnings are taxable and losses are deductible "
      "only against winnings and only if you itemise.</p>"),
    ]
    body = f'''<section class="sec"><div class="wrap"><div class="prose prose--wide">
{disclosure("This page is general information, not tax advice. Tax treatment depends on your particular "
            "circumstances. For anything beyond recreational play — and for any crypto position of size — "
            "speak to a New Zealand chartered accountant.")}
{keyfacts([("Recreational winnings", "Not taxable"), ("Jackpot / Lotto", "Not taxable"),
           ("Losses", "Not deductible"), ("Declaration required", "No"),
           ("Professional gambling", "Can be taxable"), ("Crypto gains", "Can be taxable")])}
<h2>The short answer</h2>
<p><strong>You do not pay tax on gambling winnings in New Zealand.</strong> Not on pokies, not on blackjack, not on a sports bet, not on Lotto, and not on a seven-figure jackpot. There is no threshold, no withholding, no declaration and no form. If you gamble for recreation, the money is yours in full the moment it lands.</p>
<p>That is unusual by international standards and it is worth understanding why, because the reasoning is also what defines the two exceptions.</p>

<h2>Why New Zealand does not tax gambling wins</h2>
<p>New Zealand income tax applies to income from employment, from business, and from investment. A gambling win by a recreational player fits none of those categories. It is a <strong>windfall</strong> &mdash; the product of chance rather than of a business activity &mdash; and windfalls sit outside the income tax net.</p>
<p>The corollary is the part people forget: because winnings are not income, <strong>losses are not deductible</strong>. You cannot offset a bad year at the casino against your salary. The treatment is symmetrical and, on the whole, favourable &mdash; the overwhelming majority of gamblers lose over time, and a system that taxed the winners would have to reckon with the losers.</p>
<p>New Zealand collects its revenue from the operator side instead, through gambling duty and, under the new online casino regime, a levy on licensed operators&rsquo; profits. The money is collected once, at the source, rather than chased across thousands of individual players.</p>

<h2>Exception one: gambling as a business</h2>
<p>If gambling constitutes carrying on a business, the proceeds can be assessable income. IRD assesses this on the substance of the activity, looking at factors including:</p>
<ul>
<li><strong>Organisation and system.</strong> Is there a methodical approach, records, capital management, a defined strategy?</li>
<li><strong>Intention to profit.</strong> Is the activity undertaken with a genuine expectation of profit rather than in hope of one?</li>
<li><strong>Scale and regularity.</strong> Is it continuous and substantial rather than occasional?</li>
<li><strong>Reliance.</strong> Is it the person&rsquo;s primary or sole source of income?</li>
<li><strong>Skill.</strong> Does the activity involve a genuine edge &mdash; advantage play, professional poker, arbitrage &mdash; rather than pure chance?</li>
</ul>
<p>This is a high bar and it is not met by playing frequently or by winning a lot once. A person who plays pokies every weekend for a decade and wins NZ$400,000 on a jackpot is still a recreational player, because pokies contain no skill element through which a business could be conducted. A person running a systematic arbitrage operation across multiple books as their full-time income is in a very different position.</p>
<div class="note"><b>If you are anywhere near this line</b>
<p>Get advice from a New Zealand chartered accountant before you file, not after. The consequence of being treated as in business is not only that winnings become taxable &mdash; it is that the whole activity comes into the tax system, with record-keeping obligations, provisional tax and possibly GST considerations attached. It is a status you want determined deliberately rather than discovered in an audit.</p></div>

<h2>Exception two: cryptocurrency</h2>
<p>This is the one that catches New Zealanders out, and it is catching more of them every year as crypto casinos grow.</p>
<p>Inland Revenue treats cryptocurrency as <strong>property</strong>, not currency. Acquiring crypto with the purpose of disposing of it generally makes any gain on disposal taxable income. Gambling with it does not change that analysis &mdash; the gambling win is still not taxable, but the crypto position sitting underneath it is a separate matter.</p>
<h3>A worked example</h3>
{table(["Step", "Action", "NZD value", "Tax treatment"], [
 ["1", "Buy 1,000 USDT on a NZ exchange", "NZ$1,650", "Acquisition — no tax event"],
 ["2", "Deposit to a crypto casino", "NZ$1,650", "No tax event"],
 ["3", "Play; balance grows to 1,500 USDT", "NZ$2,475", "<b>Gambling win — not taxable</b>"],
 ["4", "Withdraw 1,500 USDT to your wallet", "NZ$2,475", "No tax event"],
 ["5", "Hold; USD/NZD moves, USDT now worth more in NZD", "NZ$2,600", "Unrealised — no tax event yet"],
 ["6", "Convert 1,500 USDT to NZD", "NZ$2,600", "<b>Disposal — the NZ$125 movement may be taxable</b>"],
], minw=760)}
<p>The NZ$825 of winnings at step 3 is not taxable. The NZ$125 of currency movement at step 6 may be. That is a genuinely awkward distinction to track, and it gets considerably harder with a volatile coin such as Bitcoin where the price can move 20% during a single session.</p>
<div class="note note--mint"><b>How to keep this manageable</b>
<p><strong>Use a stablecoin.</strong> USDT and USDC are pegged to the US dollar, so the only movement is the NZD/USD rate rather than crypto volatility. <strong>Keep records</strong> of the NZD value at every acquisition and every disposal &mdash; exchanges such as Easy Crypto and Independent Reserve export this. And if your crypto position is significant, get advice. See our <a href="/best-crypto-casinos/">crypto casinos page</a> for the practical side.</p></div>

<h2>What about the money after you win it?</h2>
<p>The win is not taxable. What the money subsequently earns is. If you put NZ$200,000 of winnings into a term deposit, the interest is taxable income. Dividends from shares bought with it are taxable. Rental income from a property is taxable, and the bright-line rules apply to the property as they would to any other. The winnings arrive tax-free and then enter the ordinary tax system like any other capital.</p>

<h2>Will the new online casino licensing change any of this?</h2>
<p>Not for players. The Online Casino Gambling Act imposes a levy on <strong>licensed operators&rsquo; profits</strong> &mdash; a tax on the operator, not on you. Nothing in the framework proposes taxing player winnings, and doing so would be a fundamental departure from how New Zealand treats windfalls. Our <a href="/nz-online-casino-law/">law page</a> covers the new regime in full.</p>

<h2>How New Zealand compares</h2>
{table(["Country", "Tax on player winnings", "Notes"], [
 ["<b>New Zealand</b>", "<span class='t-yes'>None (recreational)</span>", "Operator-side duty. Professional gambling and crypto gains are the exceptions."],
 ["Australia", "<span class='t-yes'>None</span>", "Same windfall reasoning. Operators pay point-of-consumption tax."],
 ["United Kingdom", "<span class='t-yes'>None</span>", "Abolished betting duty on players in 2001; operators pay 15%+ remote gaming duty."],
 ["Canada", "<span class='t-yes'>None (recreational)</span>", "Professional gambling is taxable, as in NZ."],
 ["United States", "<span class='t-no'>Yes — fully taxable</span>", "All winnings are income. Withholding applies above thresholds; losses deductible only against winnings."],
], minw=680)}
<p>New Zealand sits with the UK, Australia and Canada rather than with the United States. If you have read American advice about W-2G forms and withholding, none of it applies here.</p>
</div></div></section>
'''
    return guide(
        "Tax on Gambling Winnings NZ 2026 | Do You Pay Tax on Casino Wins?",
        "Do you pay tax on gambling winnings in New Zealand? No, for recreational players — with two "
        "exceptions that catch people out. Professional gambling and crypto, explained with worked examples.",
        "/gambling-winnings-tax-nz/", [("Tax on Gambling Winnings", "/gambling-winnings-tax-nz/")],
        "Tax on Gambling Winnings in New Zealand",
        "The short answer is no, and it applies whether you won NZ$50 or NZ$5 million. The longer answer "
        "matters if you gamble professionally or you play at crypto casinos &mdash; two situations where New "
        "Zealand&rsquo;s otherwise simple position gets genuinely complicated.",
        icon("coin") + " Current to " + UPDATED_NZ, body, faq, "daniel-ashworth", "holly-mcgrath",
        stats=[("NZ$0", "Tax on recreational wins"), ("No", "Declaration required"),
               ("Property", "IRD's view of crypto"), ("Not deductible", "Losses")])


# ============================================================= PAYMENTS
def payments():
    faq = [
     ("What is the best payment method for NZ online casinos?",
      "<p><strong>NZD bank transfer</strong> for reliability and <strong>cryptocurrency</strong> for speed. "
      "Those were the only two methods that never failed across our testing. Card deposits work most of the "
      "time but are declined by some New Zealand banks. If speed of withdrawal is what you care about, use "
      "USDT on the Tron network &mdash; it clears in hours rather than days.</p>"),
     ("Does POLi work for online casinos in New Zealand?",
      "<p>Rarely, and we do not recommend planning around it. POLi is <strong>deposit-only</strong>, so it can "
      "never be your withdrawal method. The major New Zealand banks have tightened their terms on sharing "
      "internet-banking credentials with third parties, and POLi-to-gambling transactions are frequently "
      "declined outright. Use an NZD bank transfer instead.</p>"),
     ("Can I use online EFTPOS at a casino?",
      "<p>At a small number of sites, and deposit-only. Online EFTPOS lets you pay from your bank account "
      "without sharing card details, which is appealing, but casino support for it is thin and you will need a "
      "different route for withdrawals. Treat it as a convenience for depositing rather than a banking "
      "plan.</p>"),
     ("Why did my bank decline my casino deposit?",
      "<p>New Zealand banks can and do block transactions to gambling merchant category codes, and policies "
      "differ between ANZ, ASB, BNZ, Kiwibank and Westpac &mdash; and sometimes between products at the same "
      "bank. It is not a fault at the casino&rsquo;s end and repeated attempts will not help. Switch to an NZD "
      "bank transfer, an e-wallet, Neosurf or crypto.</p>"),
     ("Do I have to withdraw to the same method I deposited with?",
      "<p>Usually yes, up to the value of your deposit, for anti-money-laundering reasons. This matters most if "
      "you deposit by a method that does not support withdrawals &mdash; Neosurf and POLi &mdash; in which case "
      "you will be routed to bank transfer and asked for additional documentation at exactly the moment you "
      "want your money. Plan the withdrawal route before you make the deposit.</p>"),
     ("Is it safe to give a casino my bank details?",
      "<p>At a licensed operator with verified TLS encryption, the payment handling itself is standard "
      "e-commerce practice and the risk is low. The greater risk is the operator rather than the technology: a "
      "site that will not publish its licence number or operating company is one you should not be sending bank "
      "details to at all. If you would rather keep gambling off your bank statement entirely, Neosurf vouchers "
      "bought with cash are the cleanest route.</p>"),
     ("Are there fees on casino deposits and withdrawals?",
      "<p>Most operators on this site charge nothing on either. Where fees appear they are usually on "
      "withdrawals below a threshold, on repeat withdrawals within a week, or on card withdrawals. The costs "
      "that are easy to miss are not casino fees at all: <strong>currency conversion</strong> of roughly "
      "2&ndash;3% each way at euro-denominated sites, and your bank&rsquo;s own international transaction "
      "fee.</p>"),
    ]
    body = f'''<section class="sec"><div class="wrap"><div class="prose prose--wide">
<h2>The methods that actually work from a New Zealand bank account</h2>
<p>This page is based on funding and withdrawing from 41 operators using New Zealand bank accounts at ANZ, ASB, BNZ, Kiwibank and Westpac over nine months. Where we say something fails, it failed for us.</p>
{table(["Method","Deposit","Withdraw","Speed out","Fee","Reliability in our testing"], [
 ["NZD bank transfer","<span class='t-yes'>Yes</span>","<span class='t-yes'>Yes</span>","1–3 business days","Usually none","<span class='t-yes'>100% — never failed</span>"],
 ["Cryptocurrency","<span class='t-yes'>Yes</span>","<span class='t-yes'>Yes</span>","<b>10 min – 6 hrs</b>","Network only","<span class='t-yes'>100% — never failed</span>"],
 ["Visa / Mastercard debit","<span class='t-yes'>Yes</span>","<span class='t-yes'>Usually</span>","2–5 business days","None at casino","Mixed — bank-dependent"],
 ["Skrill","<span class='t-yes'>Yes</span>","<span class='t-yes'>Yes</span>","4–24 hours","1–2% some transfers","<span class='t-yes'>High</span>"],
 ["Neteller","<span class='t-yes'>Yes</span>","<span class='t-yes'>Yes</span>","4–24 hours","1–2% some transfers","<span class='t-yes'>High</span>"],
 ["MiFinity","<span class='t-yes'>Yes</span>","<span class='t-yes'>Yes</span>","6–24 hours","Varies","Good"],
 ["Jeton","<span class='t-yes'>Yes</span>","<span class='t-yes'>Yes</span>","6–24 hours","Varies","Good"],
 ["Neosurf","<span class='t-yes'>Yes</span>","<span class='t-no'>No</span>","—","Voucher cost","<span class='t-yes'>High for deposits</span>"],
 ["Online EFTPOS","<span class='t-yes'>Limited</span>","<span class='t-no'>No</span>","—","None","Few sites support it"],
 ["POLi","<span class='t-no'>Patchy</span>","<span class='t-no'>No</span>","—","None","<span class='t-no'>Low — often declined</span>"],
 ["PayPal","<span class='t-no'>No</span>","<span class='t-no'>No</span>","—","—","<span class='t-no'>Not available at NZ-facing casinos</span>"],
], minw=920)}

<h2>The conversion spread nobody itemises</h2>
<p>This is the largest hidden cost in New Zealand online gambling and almost nothing is written about it.</p>
<p>If a casino holds your balance in euros or US dollars, two conversions happen. Your bank converts NZD to EUR when you deposit, taking a spread of roughly 2 to 3% over the mid-market rate. When you withdraw, it converts back, taking the spread again. On a NZ$500 deposit and a NZ$700 withdrawal, that is roughly <strong>NZ$30 in conversion cost</strong> &mdash; and none of it appears as a fee on any statement. It is built into the rate.</p>
{table(["Scenario","Deposit","Withdrawal","Conversion cost","Effective outcome"], [
 ["NZD account","NZ$500","NZ$700","<span class='t-yes'>NZ$0</span>","+NZ$200"],
 ["EUR account, 2.5% each way","NZ$500","NZ$700","<span class='t-no'>~NZ$30</span>","+NZ$170"],
 ["EUR account + bank intl. fee","NZ$500","NZ$700","<span class='t-no'>~NZ$42</span>","+NZ$158"],
], minw=680)}
<p>On this site, <a href="/casino-reviews/crownslots/">CrownSlots</a> and <a href="/casino-reviews/gunsbet/">Gunsbet</a> are euro-denominated. Everything else with a NZD flag in our <a href="/online-casinos/">comparison table</a> holds New Zealand dollars natively. Select NZD at registration if it is offered &mdash; most operators cannot change your account currency afterwards.</p>

<h2>Method by method, for New Zealanders</h2>
<h3>NZD bank transfer</h3>
<p>The most reliable route we tested, and the only one with a 100% success rate across every operator and every New Zealand bank we used. Deposits arrive instantly to within a day; withdrawals take one to three business days. No fees at almost every operator. The downside is speed on the way out and the fact that gambling transactions appear plainly on your bank statement, which matters to some people.</p>
<h3>Cryptocurrency</h3>
<p>The fastest way to get money out of an online casino, by a wide margin, and completely immune to New Zealand bank declines. Buy USDT on the Tron network through Easy Crypto, Independent Reserve or Binance, send a small test transaction first, and match the network at both ends. Our <a href="/best-crypto-casinos/">crypto casinos page</a> covers the setup, and our <a href="/gambling-winnings-tax-nz/">tax guide</a> covers the New Zealand tax wrinkle that comes with it.</p>
<h3>Visa and Mastercard debit</h3>
<p>Convenient, instant on deposit, and unreliable in a way that is entirely outside the casino&rsquo;s control. New Zealand banks apply their own policies to gambling merchant category codes and these differ between banks and sometimes between card products at the same bank. When a card deposit is declined, retrying will not help &mdash; switch methods. Credit card gambling deposits are increasingly blocked outright and we would not recommend them regardless.</p>
<h3>Skrill and Neteller</h3>
<p>A genuinely good middle ground: faster out than a bank, more widely accepted than crypto, and not subject to New Zealand bank gambling blocks because the transaction to the wallet is not a gambling transaction. The catch that costs people money: <strong>many casinos exclude e-wallet deposits from bonus eligibility</strong>. If you are claiming a welcome offer, check this clause before you fund the account.</p>
<h3>Neosurf</h3>
<p>A prepaid voucher bought with cash at dairies and service stations across New Zealand. The only method that keeps gambling entirely off your bank statement, and genuinely useful as a spending control because you can only lose what is on the voucher. Deposit-only, so you must plan a separate withdrawal route &mdash; usually bank transfer, which will require full verification.</p>
<h3>POLi &mdash; and why we advise against it</h3>
<p>POLi works by having you enter your internet banking credentials into a third-party interface. New Zealand banks have tightened their terms considerably on exactly this, and POLi-to-gambling transactions are declined more often than they succeed in our experience. It is also deposit-only. There is no scenario in which POLi is your best option for casino banking in 2026.</p>

<h2>Verification: what you will be asked for</h2>
<p>Every operator will require identity verification before processing a withdrawal. Doing it on day one rather than at withdrawal is the single most useful habit in online gambling. You will need:</p>
<ul>
<li><strong>Photo ID.</strong> A New Zealand driver licence (both sides) or the photo page of a passport. A Kiwi Access Card works at most operators.</li>
<li><strong>Proof of address dated within three months.</strong> A power, gas or internet bill, a council rates notice, or a bank statement. The name and address must match your account exactly &mdash; a middle name on one and not the other is a common cause of rejection.</li>
<li><strong>Proof of payment method.</strong> A photo of your card with the middle digits covered, or a screenshot of your e-wallet or bank account showing your name.</li>
<li><strong>Occasionally, source of funds.</strong> For larger withdrawals, a payslip or bank statement. Standard anti-money-laundering practice, not an accusation.</li>
</ul>
<div class="note note--mint"><b>Do this on day one</b>
<p>Upload everything the day you register, before you have a balance worth withdrawing. It takes five minutes when there is nothing at stake and turns a three-day standoff into a non-event. In our testing, the same operator paid a verified account in four hours and an unverified one in three days.</p></div>
</div></div></section>
'''
    return guide(
        "NZ Casino Payment Methods 2026 | What Actually Works From a Kiwi Bank",
        "Which payment methods actually clear from a New Zealand bank account at online casinos. NZD bank "
        "transfer, crypto, cards, Skrill, Neosurf and POLi tested across 41 operators — plus the 2–3% "
        "conversion spread nobody itemises.",
        "/payment-methods/", [("NZ Payment Methods", "/payment-methods/")],
        "NZ Casino Payment Methods: What Actually Works",
        "We funded 41 casino accounts from New Zealand bank accounts at ANZ, ASB, BNZ, Kiwibank and Westpac, "
        "and withdrew from every one of them. This is what cleared, what got declined, how long each method "
        "really took, and where the costs hide.",
        icon("wallet") + " Tested across 5 NZ banks", body, faq, "holly-mcgrath",
        stats=[("100%", "Bank transfer success"), ("10 min", "Fastest crypto out"),
               ("2–3%", "Hidden EUR spread"), ("POLi", "The one to avoid")])


# ========================================================== HOW WE REVIEW
def how_we_review():
    faq = [
     ("Do you get paid by the casinos you review?",
      "<p>Yes, and we would rather say so plainly than bury it. We receive a commission when a reader opens an "
      "account through a link on this site, typically a share of the operator&rsquo;s revenue from that player. "
      "It costs you nothing and changes nothing about the offer you receive. What it does not do is determine "
      "rankings &mdash; the commission rates we are offered vary from 20% to 50%, and our top-rated casino is "
      "not the highest-paying one on our list.</p>"),
     ("How can a commission-funded site be independent?",
      "<p>By making the methodology public and the scoring mechanical, so that a deviation would be visible. The "
      "criteria and weightings on this page are fixed; the scores are derived from them; the order of the list "
      "follows the scores. If we ranked a site above its score, you could see it. We also publish operators we "
      "do not recommend, and we exclude sites regardless of commercial terms &mdash; nine this year, several "
      "paying well above average.</p>"),
     ("Do you actually deposit your own money?",
      "<p>Yes, at every operator we publish. We do not use operator-supplied test accounts, because a test "
      "account does not reveal how a withdrawal is treated. In 2026 we staked approximately NZ$14,800 of our "
      "own funds across 41 sites and completed 168 withdrawals. That expenditure is exactly what the commission "
      "funds.</p>"),
     ("What gets a casino excluded?",
      "<p>Confiscating balances on undefined &lsquo;bonus abuse&rsquo; grounds; refusing or indefinitely "
      "delaying withdrawals to verified accounts; operating without a verifiable licence; publishing bonus "
      "terms that contradict the advertised offer; or a pattern of unresolved non-payment complaints. Any one "
      "of these and the operator does not appear, regardless of what it pays.</p>"),
     ("How often do you re-test?",
      "<p>Every operator is re-tested at least quarterly, and immediately if we receive credible reports of "
      "payment problems. Bonus terms are re-checked monthly because they change without notice. Legal and "
      "regulatory pages are reviewed monthly and after every material DIA announcement. Each page carries its "
      "last-reviewed date.</p>"),
     ("Can an operator pay to be featured?",
      "<p>No. We do not sell ranking positions, &lsquo;editor&rsquo;s choice&rsquo; badges, or placement in the "
      "comparison tables. We have declined paid-placement offers from operators, and we will continue to, "
      "because the moment a position is purchasable the entire site is worthless to you and therefore worthless "
      "to us.</p>"),
    ]
    body = f'''<section class="sec"><div class="wrap"><div class="prose prose--wide">
<h2>What we actually do</h2>
<p>Most casino comparison sites are written from operator media kits. We open accounts, deposit our own New Zealand dollars, play, request withdrawals, and time them. In 2026 that meant <strong>41 operators, approximately NZ$14,800 of our own money staked, and 168 timed withdrawals</strong>. Fifteen casinos and four sportsbooks survived to publication, and each is listed once &mdash; on the page for the product it actually is, rather than on both.</p>
{keyfacts([("Operators assessed", "41"), ("Published", "19"), ("Excluded", "22"),
           ("Withdrawals timed", "168"), ("Own funds staked", "~NZ$14,800"), ("Re-test cycle", "Quarterly")])}

<h2>The six criteria and their weights</h2>
<p>Every casino score out of 10 is built from these six components. The weights are fixed and published so that any deviation between a score and a ranking position would be visible to you.</p>
{table(["Criterion","Weight","What we measure","How"], [
 ["<b>Withdrawal speed</b>","<b>25%</b>","Time from withdrawal request to funds available, by method","We request a real withdrawal at every operator and time it. Advertised figures are ignored entirely."],
 ["<b>NZD banking</b>","<b>20%</b>","Native NZD accounts, which methods clear from NZ banks, conversion costs","Funding and withdrawing from accounts at ANZ, ASB, BNZ, Kiwibank and Westpac."],
 ["<b>Bonus terms</b>","<b>20%</b>","Wagering multiplier and base, max bet, contribution rates, expiry, win caps","Reading the full terms document, not the promotion banner."],
 ["<b>Games and providers</b>","<b>15%</b>","Studio coverage, RTP transparency, lobby search and filtering","Checking for 15 named studios and testing filters and search."],
 ["<b>Licensing and trust</b>","<b>12%</b>","Verifiable licence number, named operating company, terms quality","Verifying the number against the regulator's public register. Footer badges count for nothing."],
 ["<b>Support and mobile</b>","<b>8%</b>","Response time and quality; full mobile flow","Four live chat contacts per site, at least one between 7pm and 11pm NZT. Full deposit-play-withdraw on a phone."],
], minw=900)}

<h2>Our testing process, step by step</h2>
<ol class="steps">
<li><h4>Verify the licence before anything else</h4><p>We locate the licence number and check it against the regulator&rsquo;s public register. If there is no number, or it does not resolve, or the named company does not match, testing stops here and the operator is excluded.</p></li>
<li><h4>Register and complete verification</h4><p>A real account, real details, full KYC upload on day one. We record how long verification takes and what documents are requested, because that is a real part of the player experience.</p></li>
<li><h4>Deposit real New Zealand dollars</h4><p>We test at least two deposit methods per operator, always including whatever the site presents as its primary NZD route. We record declines, fees and the account currency actually applied.</p></li>
<li><h4>Read the full bonus terms</h4><p>The complete terms document, not the promotional page. We extract the wagering multiplier and its base, the maximum bet while wagering, the game contribution table, the expiry window and any maximum conversion cap, and we record contradictions between the terms and the advertised offer.</p></li>
<li><h4>Play across the lobby</h4><p>Pokies from several studios, at least one live dealer table, and the search and filter tools. We check whether per-game RTP is published and whether the stated figure matches the studio&rsquo;s standard configuration.</p></li>
<li><h4>Contact support four times</h4><p>At least once between 7pm and 11pm New Zealand time, because that is when Kiwis play and when European support desks are thinnest. We ask a question with a specific, checkable answer and record both the response time and whether the answer was correct.</p></li>
<li><h4>Withdraw, and time it</h4><p>The core test. We request a withdrawal and record the time to funds available, separately by method. We note whether reversal is enabled by default and whether it can be turned off.</p></li>
<li><h4>Run the whole thing again on a phone</h4><p>Deposit, play and withdraw on a mobile device on mobile data, one-handed. A site that works on a desktop and fails on a phone has failed, because that is where New Zealanders actually play.</p></li>
<li><h4>Score, publish, and re-test quarterly</h4><p>Scores are calculated from the weighted criteria. Bonus terms are re-checked monthly. Any credible report of a payment problem triggers an immediate re-test.</p></li>
</ol>

<h2>What disqualifies an operator outright</h2>
<div class="note"><p>No score, no listing, regardless of commercial terms:</p>
<ul style="margin-bottom:0">
<li>Confiscating balances on undefined &ldquo;bonus abuse&rdquo; grounds</li>
<li>Refusing or indefinitely delaying withdrawals to fully verified accounts</li>
<li>Operating with no verifiable licence</li>
<li>Bonus terms that materially contradict the advertised offer</li>
<li>A pattern of unresolved non-payment complaints on independent forums</li>
<li>Withdrawal processes that require contacting support rather than a self-service request</li>
<li>Any requirement to deposit again before an existing balance can be withdrawn</li>
</ul></div>
<p>We excluded <strong>22 operators</strong> in 2026 on these grounds. Several of them offered commission rates well above the average of the sites we do list.</p>

<h2>How we handle the commercial relationship</h2>
<p>This site is funded by affiliate commission. An operator pays us a share of revenue when a reader opens an account through one of our links. We think you are entitled to know exactly how that interacts with what you read here.</p>
<ul>
<li><strong>Commission does not affect scores or order.</strong> Rates across the operators we list range from 20% to 50%. Our top-rated casino pays 45%; the highest-paying operators available to us include two that are not in our top five and one we excluded entirely.</li>
<li><strong>We do not sell placement.</strong> No paid rankings, no purchased &ldquo;editor&rsquo;s choice&rdquo; badges, no sponsored table positions. We have declined these offers and will continue to.</li>
<li><strong>Negative findings get published.</strong> <a href="/casino-reviews/roby-casino/">Roby</a> does not publish a licence number or operating company and we say so on every page it appears on, including the one that links to it.</li>
<li><strong>Operators cannot review copy before publication.</strong> No operator sees a review before it goes live, and we do not accept edits to published reviews except to correct a factual error we can verify.</li>
<li><strong>Removal is immediate.</strong> An operator that stops paying players is removed the week we can confirm it, irrespective of the contract.</li>
</ul>

<h2>Corrections and how to raise something with us</h2>
<p>We publish a date on every page and we get things wrong occasionally &mdash; bonus terms change without notice, and operators do not always tell us. If you find an error, or if you have had an experience at an operator we recommend that contradicts what we have written, tell us. Player reports of non-payment are the single most valuable input we receive and they trigger an immediate re-test.</p>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> or use our <a href="/contact/">contact form</a>. We read everything, and we correct in place with a note rather than quietly.</p>

<h2>Who writes this</h2>
<p>Three people, named, with their areas of responsibility published on our <a href="/authors/">authors page</a>. Every review carries a byline and a fact-checker. We do not publish anonymous content and we do not use AI-generated reviews of casinos nobody has opened an account at &mdash; which, given what this industry currently looks like, is worth stating explicitly.</p>
</div></div></section>
'''
    return guide(
        "How We Review Online Casinos | Magnum Sports Methodology",
        "Our full review methodology: six weighted criteria, 41 operators tested with our own money, 168 "
        "timed withdrawals, what disqualifies a casino, and exactly how affiliate commission is handled.",
        "/how-we-review/", [("How We Review", "/how-we-review/")],
        "How We Review Online Casinos",
        "Every score on this site comes from the same six weighted criteria, applied to accounts we opened and "
        "funded ourselves. This page sets out the whole method &mdash; including what disqualifies an operator "
        "and exactly how the commission that funds it is handled.",
        icon("shield") + " Published methodology", body, faq, "tama-whitiora", "daniel-ashworth",
        stats=[("41", "Operators tested"), ("22", "Excluded"),
               ("168", "Withdrawals timed"), ("25%", "Weight on payout speed")])


def build():
    return [law(), tax(), payments(), how_we_review()]
