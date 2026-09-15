# -*- coding: utf-8 -*-
"""Company, legal and support pages."""
from lib import *


def simple(title, desc, path, crumb, h1, lede, body, author="tama-whitiora",
           eyebrow=None, kind="WebPage", extra=None, faq=None, noindex=False, show_author=True):
    ex = [crumb_schema([("Home", "/")] + crumb)]
    if not faq and paa_items(path):
        ex.append(faq_schema(paa_items(path), f"{SITE}{path}#faq"))
    if faq:
        ex.append(faq_schema(faq + paa_items(path), f"{SITE}{path}#faq"))
    if extra:
        ex += extra
    schema = page_schema(kind, title, desc, path, author=author, extra=ex)
    o = [head(title, desc, path, schema, robots="noindex,follow" if noindex else None),
         crumbs([("Home", "/")] + [(c[0], None if i == len(crumb) - 1 else c[1])
                                   for i, c in enumerate(crumb)])]
    eb = f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else ""
    o.append(f'''<section class="hero"><div class="wrap">{eb}<h1>{h1}</h1>
{byline(author) if show_author else ''}
<p class="lede">{lede}</p></div></section>
''')
    o.append(body)
    if faq:
        o.append(faq_block(faq))
    o.append(paa_for(path, haze=not faq))
    o.append(footer())
    return write(path, "".join(o))


# ================================================================ ABOUT
def about():
    _tc = []
    for _s, _a in AUTHORS.items():
        _tc.append(
            '<div class="card"><img src="{i}" srcset="{i} 1x, {i2} 2x" alt="{n}" width="64" height="64" '
            'loading="lazy" style="border-radius:50%;margin-bottom:12px"><h3>{n}</h3>'
            '<p style="font-family:var(--mono);font-size:.7rem;letter-spacing:.07em;text-transform:uppercase;'
            'color:var(--red);margin-bottom:8px">{r}</p><p>{d}</p>'
            '<p><a href="/authors/#{s}">Full profile &rarr;</a></p></div>'.format(
                i=_a["img"], i2=_a["img"].replace(".jpg", "@2x.jpg"), n=esc(_a["name"]),
                r=esc(_a["role"]), d=esc(_a["short"]), s=_s))
    team_cards = "".join(_tc)
    body = f'''<section class="sec"><div class="wrap"><div class="prose prose--wide">
<h2>Why this site exists</h2>
<p>There is no shortage of &ldquo;best online casino NZ&rdquo; pages. There is a serious shortage of ones written by anybody who has opened an account, deposited New Zealand dollars and tried to get them back out again.</p>
<p>Most of what ranks for these searches is a global template with the currency symbol swapped, a few uses of the word &ldquo;Kiwi&rdquo;, and a ranking order that correlates suspiciously well with commission rates. The payout times are copied from operator marketing. The bonus terms are transcribed from the banner rather than the terms document. The legal section is usually wrong, sometimes badly &mdash; we have lost count of the pages still describing New Zealand sports betting law as it stood before June 2025.</p>
<p>Magnum Sports started in early 2026 because that gap is large, and because the information a New Zealander actually needs &mdash; whether a deposit will clear from an ASB account, whether a casino holds NZD or quietly converts twice, how long a withdrawal really takes at nine at night in Auckland &mdash; is not available anywhere else in one place.</p>

<h2>What we do differently</h2>
{cards([
 ("wallet","We use our own money","Every operator we publish has taken a real deposit from us and paid a real withdrawal back. Around NZ$14,800 of our own funds in 2026 across 41 sites. We do not use operator-supplied test accounts, because a test account tells you nothing about how a withdrawal is handled."),
 ("clock","We time everything","168 withdrawals timed with a stopwatch from request to funds available, recorded separately by method. When we say Kingdom pays out in two to four hours, that is a number we measured, not one we were given."),
 ("book","We read the actual terms","Not the promotion banner — the full terms document. Wagering base, maximum bet, contribution tables, expiry, conversion caps. Where the terms contradict the advertised offer, we say so."),
 ("scale","We check the law at source","Every legal claim on this site is checked against the Act, the DIA notice or the regulator's own register. Not against another comparison site, which is where most of the errors in this industry come from."),
 ("flag","We say what is wrong","Roby does not publish a licence number or an operating company. We say that on every page it appears on, including the pages that link to it. A comparison site that never criticises anything is an advertisement."),
 ("users","We put our names on it","Three named people with published areas of responsibility, a byline on every page and a fact-checker on every claim. No anonymous content, no AI-generated reviews of casinos nobody has visited."),
])}

<h2>How we are funded, in plain terms</h2>
<p>We earn a commission when a reader opens an account through a link on this site. That is the entire business model and we would rather state it in the first paragraph than bury it in a footer.</p>
<p>Here is what that does and does not mean. It does not cost you anything and it does not change the offer you receive. It does not buy a ranking &mdash; commission rates across the operators we list range from 20% to 50%, and our top-rated casino is not the highest payer. We have excluded 22 operators this year, several paying well above average, for refusing withdrawals, hiding licensing or publishing terms that contradict their own advertising.</p>
<p>What it does mean is that we have a commercial interest in you opening an account. The honest way to manage that is to make the methodology public and the scoring mechanical, so that any deviation would be visible to you. That is what our <a href="/how-we-review/">review methodology page</a> is for, and we would encourage you to read it sceptically.</p>

<h2>What we will not do</h2>
<ul>
<li><strong>Sell a ranking position.</strong> No paid placements, no purchased &ldquo;editor&rsquo;s choice&rdquo; badges, no sponsored rows in a comparison table. We have declined these offers.</li>
<li><strong>Let an operator see a review before publication.</strong> No pre-approval, and no post-publication edits except to correct a factual error we can verify.</li>
<li><strong>Publish an offer we have not checked.</strong> Our <a href="/no-deposit-casinos/">no deposit page</a> lists one offer because one is what we could verify as live. Pages listing thirty are not checking.</li>
<li><strong>Pretend gambling is a way to make money.</strong> Every game we cover has a house edge. We write about how to lose more slowly and enjoy it more, not about how to win.</li>
<li><strong>Market to people who should not be gambling.</strong> Strictly 18+, responsible gambling information on every page, and no content designed to appeal to under-18s.</li>
</ul>

<h2>Editorial standards</h2>
<ul>
<li>Every page carries a named author, a named fact-checker and a last-reviewed date.</li>
<li>Legal and regulatory claims are sourced to legislation or to official guidance, not to other websites.</li>
<li>Operator data is re-tested quarterly; bonus terms are re-checked monthly because they change without notice.</li>
<li>Corrections are made in place with a note, not quietly.</li>
<li>Reader reports of non-payment trigger an immediate re-test of the operator concerned.</li>
</ul>

<h2>Who we are</h2>
<p>Three people, based in New Zealand, with backgrounds in gambling media, retail banking and sports analytics. Full profiles, areas of responsibility and contact details are on our <a href="/authors/">authors page</a>.</p>
<div class="grid grid--3" style="margin-top:22px">
{team_cards}
</div>

<h2>Talk to us</h2>
<p>We read everything that comes in. Corrections, disputes about something we have written, reports of an operator behaving badly, or a question we have not answered anywhere on the site &mdash; all of it is useful, and player reports are the single most valuable input we get.</p>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> or use the <a href="/contact/">contact form</a>. Expect a reply within two working days.</p>
<div class="note note--amber"><b>If you are worried about your gambling</b>
<p>We are a comparison site, not a support service, and we would rather point you somewhere useful than keep you here. The Gambling Helpline is free, confidential and available 24 hours a day on <a href="tel:0800654655">0800 654 655</a>. The Problem Gambling Foundation offers free counselling nationwide. Our <a href="/responsible-gambling/">responsible gambling page</a> lists every New Zealand service we know of.</p></div>
</div></div></section>
'''
    return simple(
        "About Magnum Sports | Independent NZ Casino &amp; Betting Reviews",
        "Who we are, how we test online casinos with our own money, how affiliate commission is handled, and "
        "what we will not do. Independent casino and betting reviews for New Zealanders.",
        "/about/", [("About Us", "/about/")], "About Magnum Sports",
        "We are a small New Zealand team that opens real accounts, deposits real New Zealand dollars and times "
        "every withdrawal. This page explains who we are, how the site is funded, and why you should read "
        "anything written by a commission-funded publisher &mdash; including this one &mdash; with your eyes "
        "open.",
        body, eyebrow=icon("users") + " Established 2026",
        extra=[person_schema("holly-mcgrath"), person_schema("daniel-ashworth"),
               {"@type": "AboutPage", "@id": f"{SITE}/about/#aboutpage",
                "mainEntity": {"@id": f"{SITE}/#organization"}}])


# ============================================================== CONTACT
def contact():
    body = f'''<section class="sec"><div class="wrap">
<div class="grid grid--2">
<div>
<h2>Get in touch</h2>
<p>We read every message. Corrections and reports about operator behaviour are the most useful things you can send us and they go straight to the relevant editor.</p>
<form class="form" action="mailto:{EMAIL}" method="post" enctype="text/plain">
<div class="field"><label for="cname">Your name</label><input id="cname" name="name" type="text" autocomplete="name" required></div>
<div class="field"><label for="cemail">Email address</label><input id="cemail" name="email" type="email" autocomplete="email" required><span class="hint">We only use this to reply to you. See our <a href="/privacy/">privacy policy</a>.</span></div>
<div class="field"><label for="ctopic">What is this about?</label>
<select id="ctopic" name="topic">
<option>A correction or factual error</option>
<option>A problem with an operator you recommend</option>
<option>A question about something on the site</option>
<option>Partnership or commercial enquiry</option>
<option>Press or media</option>
<option>Privacy, data or cookies request</option>
<option>Something else</option>
</select></div>
<div class="field"><label for="cmsg">Message</label><textarea id="cmsg" name="message" required></textarea>
<span class="hint">If you are reporting an operator problem, please include the site name, the date, and what happened. It helps us re-test quickly.</span></div>
<button class="btn" type="submit">Send message</button>
<p style="font-size:.79rem;color:var(--mute);margin-top:6px">By sending this you confirm you are 18 or over.</p>
</form>
</div>
<div>
<h2>Direct contacts</h2>
<div class="card" style="margin-bottom:16px"><div class="card-ic">{icon("mail")}</div>
<h3>General enquiries</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p style="font-size:.86rem;color:var(--mute);margin-bottom:0">Replies within two working days, New Zealand time.</p></div>
<div class="card" style="margin-bottom:16px"><div class="card-ic">{icon("flag")}</div>
<h3>Corrections and disputes</h3><p><a href="mailto:corrections@magnumsports.co.nz">corrections@magnumsports.co.nz</a></p>
<p style="font-size:.86rem;color:var(--mute);margin-bottom:0">Goes directly to our fact-checking editor. Include a link to the page and what you believe is wrong. We correct in place with a note.</p></div>
<div class="card" style="margin-bottom:16px"><div class="card-ic">{icon("lock")}</div>
<h3>Privacy and data requests</h3><p><a href="mailto:privacy@magnumsports.co.nz">privacy@magnumsports.co.nz</a></p>
<p style="font-size:.86rem;color:var(--mute);margin-bottom:0">Access, correction or deletion requests under the Privacy Act 2020. We respond within 20 working days as required.</p></div>
<div class="card"><div class="card-ic">{icon("chart")}</div>
<h3>Commercial enquiries</h3><p><a href="mailto:partnerships@magnumsports.co.nz">partnerships@magnumsports.co.nz</a></p>
<p style="font-size:.86rem;color:var(--mute);margin-bottom:0">Please note before writing: we do not sell ranking positions, sponsored placements or editorial. See <a href="/how-we-review/">our methodology</a>.</p></div>
</div>
</div>
</div></section>

<section class="sec sec--haze"><div class="wrap"><div class="prose prose--wide">
<h2>Before you write to us</h2>
<p>A few things we are asked regularly, answered here to save you the email.</p>
<h3>We cannot recover your money from an operator</h3>
<p>We are a comparison site, not a regulator or an ombudsman. We have no authority over any casino or bookmaker and no ability to release a withheld balance. What we <em>can</em> do is re-test the operator immediately, raise it with our contact there where one exists, and remove them from the site if the pattern holds. That is genuinely worth reporting &mdash; it protects the next reader &mdash; but please do not wait on us instead of pursuing the operator&rsquo;s own complaints process and its licensing body.</p>
<h3>If your withdrawal is stuck, check this first</h3>
<p>In our experience the overwhelming majority of stalled withdrawals are an incomplete identity check. Log in, open the verification section, and confirm every document has been accepted rather than merely uploaded. Also check that no active bonus is holding the balance, and that you have not hit a weekly withdrawal cap. Our <a href="/fast-payout-casinos/">payouts page</a> covers all of this.</p>
<h3>We do not accept guest posts or link insertions</h3>
<p>We are asked most days. The answer is no, including for &ldquo;relevant, high-quality content&rdquo;. Nothing published here is written by anyone outside our team.</p>
<h3>If you need help with gambling, please contact a service rather than us</h3>
<p>The <strong>Gambling Helpline</strong> is free, confidential and available 24 hours a day on <a href="tel:0800654655">0800 654 655</a>, with text support on 8006 and live chat at <a href="https://www.gamblinghelpline.co.nz/" rel="nofollow noopener" target="_blank">gamblinghelpline.co.nz</a>. The <strong>Problem Gambling Foundation</strong> offers free face-to-face and online counselling nationwide. Both are staffed by people trained to help; we are not. Our <a href="/responsible-gambling/">responsible gambling page</a> has the full list.</p>
</div></div></section>

<section class="sec"><div class="wrap"><div class="prose prose--wide">
<h2>Publisher details</h2>
{keyfacts([("Site", "magnumsports.co.nz"), ("Editorial contact", EMAIL),
           ("Region served", "New Zealand"), ("Language", "English (NZ)"),
           ("Established", "2026"), ("Audience", "18 years and over")])}
<p>Magnum Sports is an independent comparison and review publisher. We are not a gambling operator, we do not accept wagers, and we do not hold or handle player funds at any point. All gambling activity takes place with third-party operators under their own terms and their own licensing.</p>
</div></div></section>
'''
    return simple(
        "Contact Magnum Sports | NZ Casino &amp; Betting Guide",
        "Contact the Magnum Sports team. Corrections, operator complaints, privacy requests and commercial "
        "enquiries — with the right address for each and a two-working-day reply.",
        "/contact/", [("Contact Us", "/contact/")], "Contact Us",
        "Corrections, reports about an operator, questions we have not answered, or a privacy request &mdash; "
        "here is how to reach the right person. We reply within two working days.",
        body, eyebrow=icon("mail") + " We read everything", kind="ContactPage", show_author=False,
        extra=[{"@type": "ContactPage", "@id": f"{SITE}/contact/#contactpage",
                "mainEntity": {"@id": f"{SITE}/#organization"}}])


# ============================================================== AUTHORS
def authors():
    blocks = []
    detail = {
     "tama-whitiora": {
      "since": "2017", "reviews": "41 operators tested in 2026",
      "cover": ["Casino reviews and scoring", "Online pokies and game libraries",
                "Bonus terms analysis", "Withdrawal testing"],
      "extra": "<p>He grew up in Rotorua and came to this work after a decade in hospitality venues "
               "running class 4 gaming machines &mdash; an education in what problem gambling actually "
               "looks like, and the reason this site is written the way it is.</p>"
               "<p>He is responsible for the scoring model, for every casino review on the site, and for the "
               "decision to exclude an operator. He personally opened and funded all 41 accounts tested in "
               "2026 and logged all 168 withdrawal times.</p>",
      "pages": [("Best Online Casino Sites NZ", "/"), ("Online Casinos NZ", "/online-casinos/"),
                ("Online Pokies NZ", "/online-pokies/"), ("High Payout Casinos", "/high-payout-casinos/"),
                ("Live Casinos NZ", "/live-casinos/"), ("Casino Bonuses NZ", "/online-casinos/bonuses/"),
                ("No Deposit Casinos", "/no-deposit-casinos/"), ("How We Review", "/how-we-review/")]},
     "holly-mcgrath": {
      "since": "2021", "reviews": "5 NZ banks tested across 41 operators",
      "cover": ["NZD deposits and withdrawals", "Bank declines and payment friction",
                "Cryptocurrency payments", "Verification and KYC"],
      "extra": "<p>Holly spent nine years in retail banking operations in Auckland, including four in a "
               "financial crime team, before moving into gambling media in 2021. That background is the "
               "reason this site covers things most casino guides do not &mdash; why a deposit gets declined "
               "at one New Zealand bank and clears at another, what anti-money-laundering obligations actually "
               "require of an operator, and where the currency conversion spread on a euro-denominated account "
               "goes.</p>"
               "<p>She runs all payment testing, maintains the withdrawal timing dataset, and writes the "
               "banking and crypto coverage.</p>",
      "pages": [("NZ Payment Methods", "/payment-methods/"), ("Fast Payout Casinos", "/fast-payout-casinos/"),
                ("Best Crypto Casinos NZ", "/best-crypto-casinos/")]},
     "daniel-ashworth": {
      "since": "2019", "reviews": "Every legal claim on this site",
      "cover": ["New Zealand gambling legislation", "Sports betting and odds analysis",
                "Fact-checking and corrections", "Responsible gambling policy"],
      "extra": "<p>Daniel has priced sports markets professionally and follows New Zealand gambling "
               "legislation closely enough to have read the Racing Industry Amendment Act rather than a "
               "summary of it. He fact-checks every legal, regulatory and statistical claim published on this "
               "site against the primary source &mdash; the Act itself, the Department of Internal Affairs "
               "notice, or the regulator&rsquo;s own licence register.</p>"
               "<p>He is the reason a number of claims that appear on competing New Zealand casino sites do "
               "not appear on this one, and the reason our betting pages say plainly that the punter commits "
               "no offence &mdash; a point most coverage of the 2025 law change has blurred.</p>",
      "pages": [("NZ Online Casino Law", "/nz-online-casino-law/"),
                ("Tax on Gambling Winnings NZ", "/gambling-winnings-tax-nz/"),
                ("Online Betting NZ", "/online-betting/"),
                ("Responsible Gambling", "/responsible-gambling/")]},
    }
    for slug, a in AUTHORS.items():
        d = detail[slug]
        cover_chips = "".join('<li><span class="chip chip--on">%s</span></li>' % esc(c) for c in d["cover"])
        knows_chips = "".join('<li><span class="chip">%s</span></li>' % esc(k) for k in a["knows"])
        page_links = "".join('<li><a href="%s">%s</a></li>' % (u, esc(t)) for t, u in d["pages"])
        blocks.append(f'''<div id="{slug}" class="card" style="margin-bottom:24px;scroll-margin-top:90px">
<div style="display:flex;gap:20px;flex-wrap:wrap;align-items:flex-start">
<img src="{a["img"]}" srcset="{a["img"]} 1x, {a["img"].replace(".jpg","@2x.jpg")} 2x" alt="{esc(a["name"])}" width="96" height="96" loading="lazy" style="border-radius:50%;flex:0 0 auto">
<div style="flex:1 1 300px">
<h2 style="margin-bottom:4px;font-size:1.4rem">{esc(a["name"])}</h2>
<p style="font-family:var(--mono);font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--red);margin-bottom:12px">{esc(a["role"])} &middot; Writing about gambling since {d["since"]}</p>
<p>{esc(a["bio"])}</p>
{d["extra"]}
<h3 style="font-size:1rem;margin-top:1.4em">Areas of responsibility</h3>
<ul class="chips">{cover_chips}</ul>
<h3 style="font-size:1rem">Also knows about</h3>
<ul class="chips">{knows_chips}</ul>
<h3 style="font-size:1rem">Pages by {esc(a["name"].split()[0])}</h3>
<ul>{page_links}</ul>
<p style="margin-bottom:0"><strong>Contact:</strong> <a href="mailto:{slug.split("-")[0]}@magnumsports.co.nz">{slug.split("-")[0]}@magnumsports.co.nz</a> &middot; <a href="/contact/">via the contact form</a></p>
</div></div></div>''')

    blocks_html = "".join(blocks)
    body = f'''<section class="sec"><div class="wrap"><div class="prose prose--wide">
<h2>Who writes Magnum Sports</h2>
<p>Three named people, each responsible for a defined area, with a byline on every page they write and a colleague fact-checking every claim. We do not publish anonymous content, we do not use contributed or guest posts, and we do not generate reviews of casinos nobody on the team has opened an account at.</p>
<p>That should not be remarkable. In this industry it is, which is why the page exists and why every author here is contactable directly.</p>
</div>
<div style="max-width:880px;margin-top:28px">
{blocks_html}
</div>
<div class="prose prose--wide" style="margin-top:8px">
<h2>How we work together</h2>
<p>Every page on this site has an <strong>author</strong> and a <strong>fact-checker</strong>, and they are never the same person. Tama writes the casino and pokies coverage and Daniel checks it. Daniel writes the legal, tax and betting coverage and Tama or Holly checks it. Holly writes the payments and crypto coverage and Tama checks it.</p>
<p>Factual claims about the law are checked against the legislation or the Department of Internal Affairs notice. Claims about an operator are checked against the operator&rsquo;s own published terms and against our testing data. Numbers in our tables come from the testing dataset, not from operator marketing. Where we cannot verify something, we either leave it out or say explicitly that it is unverified &mdash; which is why our <a href="/no-deposit-casinos/">no deposit page</a> lists one offer rather than thirty.</p>
<h2>Corrections</h2>
<p>We get things wrong. Bonus terms change without notice, operators alter payment methods quietly, and legislation moves. When we find an error, or you tell us about one, we correct it in place and note the change rather than editing silently.</p>
<p>Email <a href="mailto:corrections@magnumsports.co.nz">corrections@magnumsports.co.nz</a> with a link to the page and what you believe is wrong. It goes straight to Daniel. Read our full <a href="/how-we-review/">methodology and editorial standards</a>.</p>
</div>
</div></section>
'''
    return simple(
        "Our Authors | Who Writes Magnum Sports",
        "Meet the three people who write Magnum Sports: their backgrounds, areas of responsibility, the pages "
        "they write and how to contact them directly. No anonymous content.",
        "/authors/", [("Our Authors", "/authors/")], "Our Authors",
        "Every page on this site carries a named author and a named fact-checker, and they are never the same "
        "person. Here is who they are, what each is responsible for, and how to reach them.",
        body, eyebrow=icon("users") + " Named, contactable, accountable", show_author=False,
        kind="ProfilePage",
        extra=[person_schema("holly-mcgrath"), person_schema("daniel-ashworth")])


# ================================================ RESPONSIBLE GAMBLING
def responsible():
    faq = [
     ("Where can I get free help for gambling in New Zealand?",
      "<p>The <strong>Gambling Helpline</strong> is free, confidential and available 24 hours a day on "
      "<a href='tel:0800654655'>0800 654 655</a>, with text support on 8006 and live chat online. The "
      "<strong>Problem Gambling Foundation of New Zealand</strong> offers free face-to-face and online "
      "counselling nationwide, including services for family and wh&#257;nau. <strong>Salvation Army Oasis</strong> "
      "provides free counselling in several centres. None of these services costs anything and none requires a "
      "referral.</p>"),
     ("How do I self-exclude from an online casino?",
      "<p>Every operator we recommend offers self-exclusion from the account settings, usually under "
      "&lsquo;Responsible Gambling&rsquo; or &lsquo;Account Limits&rsquo;. Periods typically run from six "
      "months to permanent. A self-exclusion cannot be reversed on request during the period &mdash; that is "
      "the point of it. Note that online self-exclusion applies to <em>that operator only</em>; New "
      "Zealand&rsquo;s multi-venue exclusion programme covers land-based venues and does not extend to offshore "
      "online sites, so you must request it at each site individually.</p>"),
     ("What is a reality check and should I use one?",
      "<p>A pop-up at an interval you choose &mdash; 15, 30 or 60 minutes &mdash; telling you how long you have "
      "been playing and, at better operators, how much you are up or down. It sounds trivial and it is one of "
      "the most effective tools available, because losing track of time is a central mechanism of gambling "
      "harm. Yes, use one. Sixty minutes is a sensible default.</p>"),
     ("Can I set a deposit limit?",
      "<p>Yes, at every operator on this site, from the account settings. Daily, weekly or monthly. "
      "<strong>Reductions take effect immediately; increases are deliberately delayed</strong>, usually by 24 "
      "to 72 hours, so a limit cannot be raised in the moment you most want to raise it. Set one before your "
      "first deposit rather than after a bad night.</p>"),
     ("What are the warning signs of a gambling problem?",
      "<p>Gambling more than you intended or can afford; chasing losses; borrowing to gamble; hiding it from "
      "people close to you; gambling to escape stress or low mood; being unable to stop after deciding to; "
      "gambling affecting work, sleep, study or relationships. Any one of these warrants a conversation with "
      "the Helpline. You do not need to be in crisis to call, and most people who do are not.</p>"),
     ("Can I block gambling sites on my devices?",
      "<p>Yes, and blocking software is more effective than willpower. <strong>Gamban</strong> and "
      "<strong>BetBlocker</strong> both block thousands of gambling sites and apps across devices; BetBlocker "
      "is free. Most New Zealand banks now offer a <strong>gambling block</strong> on debit and credit cards "
      "from the banking app &mdash; ASB, ANZ, BNZ, Kiwibank and Westpac all provide some form of it, and it "
      "takes about a minute to turn on. Combining a card block with site blocking is considerably more "
      "effective than either alone.</p>"),
     ("Is it normal to lose?",
      "<p>Yes. Every game we cover has a built-in mathematical advantage for the operator, published and "
      "unchanging, which means the expected outcome of playing is a loss. Winning sessions happen and are the "
      "reason people play, but they do not change the long-run arithmetic. Anyone presenting gambling as a way "
      "to make money &mdash; a system, a strategy, a tipster service &mdash; is either mistaken or selling "
      "you something.</p>"),
    ]
    body = f'''<section class="sec"><div class="wrap"><div class="prose prose--wide">
<div class="note note--amber"><b>Free help, right now</b>
<p><strong>Gambling Helpline: <a href="tel:0800654655">0800 654 655</a></strong> &mdash; free, confidential, 24 hours a day, every day. Text <strong>8006</strong>. Live chat at <a href="https://www.gamblinghelpline.co.nz/" rel="nofollow noopener" target="_blank">gamblinghelpline.co.nz</a>. You do not need to be in crisis to call, and you do not need a referral.</p></div>

<h2>The maths, stated plainly</h2>
<p>Every game on every site we review has a house edge. It is published, it does not move, and it means the expected outcome of playing is a loss. A 96% RTP pokie returns NZ$96 for every NZ$100 wagered, over the long run. Blackjack at optimal strategy returns about NZ$99.50. Both numbers are below NZ$100, and no strategy, system, staking plan or amount of persistence changes that.</p>
<p>We write about how to lose more slowly &mdash; better RTP, better bonus terms, lower margins &mdash; and how to enjoy it. We do not write about how to win, because over any meaningful period nobody does. If that framing makes the whole exercise less appealing, that is a reasonable response and a good reason to spend the money on something else.</p>

<h2>The tools, and how to actually use them</h2>
{cards([
 ("wallet","Deposit limits","Daily, weekly or monthly caps set in account settings. Reductions apply immediately; increases are delayed 24–72 hours at every reputable operator. <b>Set one before your first deposit</b>, when the decision costs you nothing."),
 ("clock","Reality checks","A pop-up every 15, 30 or 60 minutes showing how long you have played. The single most effective tool most operators offer, because losing track of time is central to how harm develops."),
 ("chart","Loss limits","A cap on net losses over a period, rather than on deposits. More precisely targeted than a deposit limit and available at most of the operators we list."),
 ("clock","Session limits","An automatic logout after a set period. Blunt, and effective for exactly that reason."),
 ("lock","Time-out","A short cooling-off period, from 24 hours to six weeks, during which you cannot log in. Reversible when it ends. A good first step if you are unsure."),
 ("shield","Self-exclusion","Six months to permanent, and not reversible on request. The strongest tool an operator offers. Applies to that operator only, so repeat it at every site where you hold an account."),
])}

<h2>New Zealand support services</h2>
{table(["Service","What it offers","Contact","Cost"], [
 ["<b>Gambling Helpline Aotearoa</b>","24/7 phone, text and live chat counselling; referral to face-to-face services; support for family and wh&#257;nau","<a href='tel:0800654655'>0800 654 655</a> &middot; text 8006 &middot; <a href='https://www.gamblinghelpline.co.nz/' rel='nofollow noopener' target='_blank'>gamblinghelpline.co.nz</a>","<span class='t-yes'>Free</span>"],
 ["<b>Problem Gambling Foundation NZ</b>","Free face-to-face and online counselling nationwide; wh&#257;nau support; Asian, Pacific and M&#257;ori services","<a href='tel:0800664262'>0800 664 262</a> &middot; <a href='https://www.pgf.nz/' rel='nofollow noopener' target='_blank'>pgf.nz</a>","<span class='t-yes'>Free</span>"],
 ["<b>Salvation Army Oasis</b>","Free counselling and support in Auckland, Hamilton, Tauranga, Wellington and Christchurch","<a href='tel:0800530000'>0800 53 00 00</a>","<span class='t-yes'>Free</span>"],
 ["<b>Te Whatu Ora gambling services</b>","Publicly funded treatment services and referrals","Via your GP or the Helpline","<span class='t-yes'>Free</span>"],
 ["<b>Gamblers Anonymous NZ</b>","Peer support meetings nationwide and online","<a href='https://www.gamblersanonymous.org.nz/' rel='nofollow noopener' target='_blank'>gamblersanonymous.org.nz</a>","<span class='t-yes'>Free</span>"],
 ["<b>Need to Talk?</b>","General mental health support, 24/7","<a href='tel:1737'>Call or text 1737</a>","<span class='t-yes'>Free</span>"],
 ["<b>Lifeline Aotearoa</b>","24/7 crisis support","<a href='tel:0800543354'>0800 543 354</a>","<span class='t-yes'>Free</span>"],
], minw=800)}

<h2>Blocking software and bank blocks</h2>
<p>Technical barriers work better than intention. Two layers are far more effective than one.</p>
<ul>
<li><strong>BetBlocker</strong> &mdash; free, blocks thousands of gambling sites and apps across devices, and cannot be uninstalled during a period you set. Funded by a UK charity and available worldwide including New Zealand.</li>
<li><strong>Gamban</strong> &mdash; paid, broader coverage, works across Windows, macOS, iOS and Android.</li>
<li><strong>Your bank&rsquo;s gambling block.</strong> ASB, ANZ, BNZ, Kiwibank and Westpac all offer some form of card-level gambling block, toggled from the banking app. It blocks transactions to gambling merchant codes at the source. Some banks impose a cooling-off period before it can be removed, which is the feature rather than a flaw.</li>
</ul>
<p>Used together &mdash; site blocking plus a bank block &mdash; these make impulsive gambling genuinely difficult rather than merely discouraged.</p>

<h2>Recognising the signs</h2>
<p>Gambling harm develops gradually, and the people experiencing it are usually the last to name it. These are the signs clinicians and the New Zealand support services consistently identify:</p>
<div class="pc">
<div class="pc-col pc-con"><h4>Warning signs</h4><ul>
<li>Gambling more, or for longer, than you intended</li>
<li>Chasing losses &mdash; betting more to recover what you have lost</li>
<li>Borrowing money, selling things, or using money meant for bills</li>
<li>Hiding gambling from partners, family or friends</li>
<li>Gambling to escape stress, boredom, loneliness or low mood</li>
<li>Restlessness or irritability when you try to cut down</li>
<li>Lying about how much you have lost</li>
<li>Gambling affecting work, study, sleep or relationships</li>
<li>Feeling you must keep going until you win it back</li>
</ul></div>
<div class="pc-col pc-pro"><h4>Habits that keep it safe</h4><ul>
<li>Set a deposit limit before your first deposit</li>
<li>Decide the amount before you start, and treat it as spent</li>
<li>Never gamble with money needed for rent, bills, food or debt</li>
<li>Never borrow to gamble, from anyone or anything</li>
<li>Use a reality check and pay attention to it</li>
<li>Take real breaks &mdash; leave the device, not just the tab</li>
<li>Do not gamble when upset, drinking or unable to sleep</li>
<li>Accept losses as the cost of the entertainment rather than a debt to recover</li>
<li>Talk to someone if it stops being fun</li>
</ul></div></div>

<h2>If you are worried about someone else</h2>
<p>Gambling harm affects families as much as the person gambling, and every service listed above supports family and wh&#257;nau directly &mdash; you do not need the person gambling to be involved or even to know you have called.</p>
<p>What helps: raise it calmly and specifically rather than in an argument; focus on behaviour you have observed rather than on character; offer to help them contact a service rather than issuing an ultimatum; and protect your own financial position, which is not disloyal but sensible. What does not help: paying off gambling debts, which reliably enables further gambling; policing and monitoring, which produces concealment; and waiting for them to hit bottom, which is a myth.</p>
<p>The Gambling Helpline takes calls from family members every day on <a href="tel:0800654655">0800 654 655</a>.</p>

<h2>Our commitments</h2>
<ul>
<li>We publish responsible gambling information on <strong>every page</strong> of this site, not only this one.</li>
<li>We display 18+ messaging and the Helpline number in the footer of every page.</li>
<li>We do not list operators that fail to provide deposit limits, time-outs and self-exclusion.</li>
<li>We do not present gambling as a way to make money, and we state the house edge in plain terms.</li>
<li>We do not create content designed to appeal to people under 18.</li>
<li>We do not use urgency, scarcity or loss-chasing language in our promotional copy.</li>
<li>We will remove an operator that obstructs self-exclusion or markets to excluded players.</li>
</ul>
<p>If you think we have fallen short of any of these, tell us at <a href="mailto:{EMAIL}">{EMAIL}</a>. We take it seriously.</p>
</div></div></section>
'''
    return simple(
        "Responsible Gambling NZ | Free Help, Tools and Support",
        "Free, confidential gambling help in New Zealand. Gambling Helpline 0800 654 655, deposit limits, "
        "self-exclusion, blocking software and bank gambling blocks — plus how to help someone else.",
        "/responsible-gambling/", [("Responsible Gambling", "/responsible-gambling/")],
        "Responsible Gambling in New Zealand",
        "Every game we write about has a house edge, which means the expected outcome of playing is a loss. "
        "This page is about keeping it that way &mdash; a cost you chose &mdash; rather than something worse. "
        "Free help is available 24 hours a day on <strong>0800 654 655</strong>.",
        body, author="daniel-ashworth", eyebrow=icon("shield") + " Free help &middot; 0800 654 655",
        faq=faq)


# ================================================================ TERMS
def terms():
    body = f'''<section class="sec"><div class="wrap"><div class="prose">
<p><strong>Last updated:</strong> {UPDATED_NZ}</p>
<h2>1. About these terms</h2>
<p>These terms govern your use of magnumsports.co.nz (&ldquo;this site&rdquo;, &ldquo;we&rdquo;, &ldquo;us&rdquo;). By accessing the site you agree to them. If you do not agree, please do not use the site.</p>
<p>Magnum Sports is an independent information and comparison publisher. <strong>We are not a gambling operator.</strong> We do not accept wagers, we do not operate games, and we never hold, handle or have access to player funds. All gambling activity takes place with third-party operators under their terms and their licensing.</p>

<h2>2. Age restriction</h2>
<p>This site is intended for people aged <strong>18 years or over</strong>. By using it you confirm you are 18 or over. Content on this site is not directed at minors and we take reasonable steps to avoid material that would appeal to them. If you are under 18, leave this site.</p>

<h2>3. Information, not advice</h2>
<p>Everything on this site is general information. It is not legal advice, financial advice, tax advice or gambling advice, and it does not take account of your circumstances. Before acting on anything here &mdash; particularly on matters of law or tax &mdash; obtain advice from an appropriately qualified New Zealand professional.</p>
<p>We make reasonable efforts to keep information accurate and current, including quarterly re-testing of operators and monthly checks of bonus terms. Despite that, operator terms, bonuses, payment methods and availability change without notice, and legislation changes. <strong>Always read the operator&rsquo;s own current terms before depositing.</strong> Where our information conflicts with an operator&rsquo;s published terms, the operator&rsquo;s terms prevail.</p>

<h2>4. Affiliate relationships</h2>
<p>We earn commission when a reader opens an account with an operator through a link on this site. This does not cost you anything and does not alter the offer available to you.</p>
<p>Commission does not determine our rankings. Scores are calculated from the weighted criteria published in our <a href="/how-we-review/">review methodology</a>, and operators are excluded on editorial grounds regardless of commercial terms. We do not sell ranking positions, badges or placement. Our commercial relationships are disclosed on every page carrying affiliate links.</p>

<h2>5. Third-party sites</h2>
<p>This site links to third-party websites, including gambling operators. We do not control those sites and we are not responsible for their content, terms, privacy practices, security or conduct. Following a link means leaving this site and entering into a relationship governed entirely by that operator&rsquo;s terms.</p>
<p>We are not a party to any agreement between you and an operator, and <strong>we cannot resolve disputes with operators, recover funds, or intervene in your account</strong>. If you have a dispute, use the operator&rsquo;s complaints process and then its licensing authority. We are grateful to hear about it &mdash; it informs our testing and may result in an operator being removed &mdash; but we have no authority to act on your behalf.</p>

<h2>6. Your responsibilities</h2>
<ul>
<li>Ensure gambling is lawful for you in your jurisdiction and that you meet the age requirement.</li>
<li>Read and understand an operator&rsquo;s terms before depositing.</li>
<li>Gamble only with money you can afford to lose.</li>
<li>Use the site lawfully and not in a way that damages, overloads or interferes with it.</li>
<li>Not scrape, republish or systematically extract our content without written permission.</li>
</ul>

<h2>7. Intellectual property</h2>
<p>All content on this site &mdash; text, review scores, testing data, comparison tables, design, code and graphics &mdash; is owned by Magnum Sports or used under licence, and is protected by copyright. You may read, print and share links for personal, non-commercial use. You may not reproduce, republish, redistribute or create derivative works from it without our prior written permission.</p>
<p>Operator names, logos and trade marks are the property of their respective owners and appear here for identification purposes under fair dealing.</p>

<h2>8. Availability</h2>
<p>We aim to keep the site available but do not guarantee uninterrupted access. We may modify, suspend or discontinue any part of it at any time without notice.</p>

<h2>9. Limitation of liability</h2>
<p>To the maximum extent permitted by law, we exclude all warranties, express or implied, as to the accuracy, completeness or fitness for purpose of anything on this site, and we are not liable for any loss or damage arising from your use of it or of any third-party site accessed through it. This includes, without limitation, <strong>gambling losses</strong>, losses arising from reliance on our information, and losses arising from an operator&rsquo;s conduct.</p>
<p>Nothing in these terms limits rights you have under the Consumer Guarantees Act 1993 or the Fair Trading Act 1986 that cannot lawfully be excluded.</p>

<h2>10. Responsible gambling</h2>
<p>Gambling can be harmful. If it is causing you difficulty, free and confidential help is available 24 hours a day from the Gambling Helpline on <a href="tel:0800654655">0800 654 655</a>. See our <a href="/responsible-gambling/">responsible gambling page</a> for the full list of New Zealand services.</p>

<h2>11. Privacy and cookies</h2>
<p>Our handling of personal information is set out in our <a href="/privacy/">Privacy Policy</a> and our use of cookies in our <a href="/cookie-policy/">Cookie Policy</a>. Both form part of these terms.</p>

<h2>12. Changes</h2>
<p>We may amend these terms at any time. The version published here is the current one and the date at the top shows when it last changed. Continued use after a change constitutes acceptance.</p>

<h2>13. Governing law</h2>
<p>These terms are governed by New Zealand law, and the New Zealand courts have exclusive jurisdiction over any dispute arising from them or from your use of this site.</p>

<h2>14. Contact</h2>
<p>Questions about these terms: <a href="mailto:{EMAIL}">{EMAIL}</a> or via our <a href="/contact/">contact page</a>.</p>
</div></div></section>
'''
    return simple("Terms and Conditions | Magnum Sports",
                  "Terms and conditions for using magnumsports.co.nz — age restriction, affiliate disclosure, "
                  "third-party operators, liability and governing law.",
                  "/terms/", [("Terms and Conditions", "/terms/")], "Terms and Conditions",
                  "The terms on which you may use this site, our affiliate relationships, and the limits of "
                  "what we are responsible for.", body, show_author=False)


# ============================================================== PRIVACY
def privacy():
    body = f'''<section class="sec"><div class="wrap"><div class="prose">
<p><strong>Last updated:</strong> {UPDATED_NZ}</p>
<p>This policy explains how Magnum Sports collects, uses, stores and discloses personal information. We comply with the <strong>Privacy Act 2020</strong> and its information privacy principles. Where visitors are in the EU or UK, we also seek to meet GDPR standards.</p>

<h2>1. Who we are</h2>
<p>Magnum Sports operates magnumsports.co.nz, an independent comparison site for online casinos and betting sites serving New Zealand. For the purposes of this policy we are the agency (and, under GDPR, the controller) responsible for the personal information described below.</p>
<p><strong>Privacy contact:</strong> <a href="mailto:privacy@magnumsports.co.nz">privacy@magnumsports.co.nz</a></p>

<h2>2. What we collect</h2>
<h3>Information you give us</h3>
<ul>
<li><strong>Contact form and email.</strong> Your name, email address, chosen topic and the content of your message. We use this only to respond to you and to investigate anything you report.</li>
</ul>
<h3>Information collected automatically</h3>
<ul>
<li><strong>Analytics data.</strong> Pages viewed, time on page, approximate location (country or region, derived from IP), referring site, device type, browser and operating system. This is aggregated and we do not use it to identify individuals.</li>
<li><strong>Affiliate tracking.</strong> When you click a link to an operator, a tracking parameter records that the click came from this site so commission can be attributed. This is handled by the operator&rsquo;s affiliate platform, not by us.</li>
<li><strong>Server logs.</strong> IP address, timestamp and requested URL, retained briefly for security and diagnostics.</li>
</ul>
<h3>What we do not collect</h3>
<p>We do not collect or have access to your gambling account details, your deposits, withdrawals, balances, play history, or any financial information. Those sit entirely with the operator. We do not knowingly collect information from anyone under 18.</p>

<h2>3. Why we collect it, and our lawful basis</h2>
{table(["Purpose","Information used","Basis"], [
 ["Responding to your enquiry","Name, email, message","Your request / legitimate interest"],
 ["Understanding which content is useful","Aggregated analytics","Consent (analytics cookies) / legitimate interest"],
 ["Attributing affiliate commission","Click referral data","Consent (marketing cookies) / legitimate interest"],
 ["Keeping the site secure","Server logs, IP","Legitimate interest"],
 ["Meeting legal obligations","As required","Legal obligation"],
], minw=620)}

<h2>4. Cookies</h2>
<p>We use cookies and similar technologies. Essential cookies keep the site working; analytics and affiliate cookies are set only where you consent. Full detail, including how to refuse or delete them, is in our <a href="/cookie-policy/">Cookie Policy</a>.</p>

<h2>5. Who we share information with</h2>
<p>We do not sell personal information. We do not trade or rent it. We share limited information with:</p>
<ul>
<li><strong>Analytics providers</strong>, which process aggregated usage data on our behalf.</li>
<li><strong>Affiliate networks and operators</strong>, which receive click referral data when you follow an outbound link.</li>
<li><strong>Our hosting and email providers</strong>, as processors, to run the site and deliver messages.</li>
<li><strong>Law enforcement or regulators</strong>, where we are legally required to.</li>
</ul>
<p>Some of these providers are overseas, which means your information may be stored or processed outside New Zealand. Where that happens we take reasonable steps to ensure comparable safeguards, consistent with information privacy principle 12.</p>

<h2>6. How long we keep it</h2>
<ul>
<li><strong>Contact enquiries:</strong> up to 24 months, then deleted.</li>
<li><strong>Analytics:</strong> aggregated and retained up to 26 months.</li>
<li><strong>Server logs:</strong> up to 90 days.</li>
</ul>

<h2>7. Security</h2>
<p>The site is served over HTTPS with TLS encryption. Access to enquiry data is limited to team members who need it. No system is perfectly secure, but we take reasonable steps appropriate to the limited and low-risk information we hold.</p>

<h2>8. Your rights</h2>
<p>Under the Privacy Act 2020 you may:</p>
<ul>
<li><strong>Access</strong> the personal information we hold about you;</li>
<li><strong>Request correction</strong> of anything inaccurate;</li>
<li><strong>Complain</strong> to us, and then to the Office of the Privacy Commissioner if you are not satisfied.</li>
</ul>
<p>Where GDPR applies to you, you additionally have rights to erasure, restriction, portability and objection, and may withdraw consent at any time.</p>
<p>To exercise any of these, email <a href="mailto:privacy@magnumsports.co.nz">privacy@magnumsports.co.nz</a>. We respond within <strong>20 working days</strong> as the Privacy Act requires, and usually much sooner. We may need to verify your identity first.</p>

<h2>9. Complaints</h2>
<p>If you are unhappy with how we have handled your information, contact us first at <a href="mailto:privacy@magnumsports.co.nz">privacy@magnumsports.co.nz</a>. If we cannot resolve it, you may complain to the <strong>Office of the Privacy Commissioner</strong> at <a href="https://www.privacy.org.nz/" rel="nofollow noopener" target="_blank">privacy.org.nz</a> or on 0800 803 909.</p>

<h2>10. Children</h2>
<p>This site is for people aged 18 and over. We do not knowingly collect information from anyone under 18. If you believe we have, contact us and we will delete it.</p>

<h2>11. Changes</h2>
<p>We may update this policy. The date at the top shows when it last changed. Material changes will be flagged on the site.</p>

<h2>12. Contact</h2>
<p><a href="mailto:privacy@magnumsports.co.nz">privacy@magnumsports.co.nz</a> &middot; <a href="/contact/">Contact form</a></p>
</div></div></section>
'''
    return simple("Privacy Policy | Magnum Sports",
                  "How Magnum Sports collects, uses and protects personal information under the Privacy Act "
                  "2020 — what we collect, who we share it with, how long we keep it and your rights.",
                  "/privacy/", [("Privacy Policy", "/privacy/")], "Privacy Policy",
                  "What we collect, why, who we share it with, and how to access, correct or delete it. "
                  "We comply with the Privacy Act 2020.", body, show_author=False)


# ========================================================== COOKIE POLICY
def cookies():
    body = f'''<section class="sec"><div class="wrap"><div class="prose">
<p><strong>Last updated:</strong> {UPDATED_NZ}</p>
<h2>What cookies are</h2>
<p>A cookie is a small text file a website stores on your device. It lets the site remember things between pages and visits &mdash; a preference you set, or the fact that you have already dismissed a banner. This policy also covers similar technologies such as local storage and tracking pixels.</p>

<h2>The cookies this site uses</h2>
{table(["Category","What it does","Set without consent?","Typical lifespan"], [
 ["<b>Strictly necessary</b>","Keeps the site working, remembers your cookie choice, and supports security","<span class='t-yes'>Yes — required</span>","Session to 12 months"],
 ["<b>Analytics</b>","Tells us which pages are read, how long for, and where readers arrive from, in aggregate","<span class='t-no'>No — consent only</span>","Up to 26 months"],
 ["<b>Affiliate / marketing</b>","Records that a click on an operator link came from this site, so commission can be attributed","<span class='t-no'>No — consent only</span>","Up to 12 months"],
 ["<b>Preference</b>","Remembers display choices you make","<span class='t-no'>No — consent only</span>","Up to 12 months"],
], minw=720)}

<h2>Third-party cookies</h2>
<p>Some cookies are set by third parties rather than by us:</p>
<ul>
<li><strong>Analytics providers</strong> set cookies to measure aggregated site usage.</li>
<li><strong>Affiliate networks and operators</strong> set cookies when you click through to their sites, to attribute the referral. These are governed by that party&rsquo;s own privacy and cookie policies, which we do not control.</li>
<li><strong>Google Fonts</strong> is used to serve typefaces. It does not set advertising cookies.</li>
</ul>
<p>Once you leave this site by following an outbound link, the destination operator&rsquo;s cookie practices apply, not ours.</p>

<h2>What we do not do</h2>
<ul>
<li>We do not use cookies to build advertising profiles for third parties.</li>
<li>We do not sell data collected through cookies.</li>
<li>We do not use cross-site behavioural advertising or retargeting pixels.</li>
<li>We do not use cookies to identify you personally.</li>
</ul>

<h2>Managing cookies</h2>
<h3>On this site</h3>
<p>You may accept or refuse non-essential cookies when you first visit, and you can change that choice at any time by clearing cookies for this domain in your browser and reloading the page.</p>
<h3>In your browser</h3>
<p>Every major browser lets you block or delete cookies. Note that blocking all cookies will break parts of most websites, including this one.</p>
<ul>
<li><strong>Chrome:</strong> Settings &rarr; Privacy and security &rarr; Third-party cookies</li>
<li><strong>Safari:</strong> Settings &rarr; Safari &rarr; Privacy &amp; Security (iOS) or Safari &rarr; Settings &rarr; Privacy (macOS)</li>
<li><strong>Firefox:</strong> Settings &rarr; Privacy &amp; Security &rarr; Cookies and Site Data</li>
<li><strong>Edge:</strong> Settings &rarr; Cookies and site permissions</li>
</ul>
<h3>Opting out of analytics</h3>
<p>Most analytics providers publish a browser opt-out. Enabling &ldquo;Do Not Track&rdquo; or a privacy-focused browser extension will also prevent most analytics cookies being set.</p>

<h2>Consequences of refusing</h2>
<p>Refusing analytics and affiliate cookies does not restrict your access to anything on this site. Every page remains fully readable. The practical effect is that we lose visibility of which content is useful, and that a referral may not be attributed &mdash; which affects our revenue, not your experience.</p>

<h2>Legal basis</h2>
<p>We set non-essential cookies on the basis of your consent, in line with the Privacy Act 2020 and, where applicable, the GDPR and the ePrivacy Directive. Strictly necessary cookies are set on the basis of legitimate interest, as the site cannot function without them.</p>

<h2>Changes and contact</h2>
<p>We may update this policy; the date above shows when it last changed. Questions: <a href="mailto:privacy@magnumsports.co.nz">privacy@magnumsports.co.nz</a>. See also our <a href="/privacy/">Privacy Policy</a> and <a href="/terms/">Terms and Conditions</a>.</p>
</div></div></section>
'''
    return simple("Cookie Policy | Magnum Sports",
                  "Which cookies magnumsports.co.nz uses, what each does, which require consent, and how to "
                  "refuse or delete them in any browser.",
                  "/cookie-policy/", [("Cookie Policy", "/cookie-policy/")], "Cookie Policy",
                  "Which cookies this site sets, what each one does, and how to turn off the ones you do not "
                  "want. Refusing them does not restrict anything you can read here.",
                  body, show_author=False)


def build():
    return [about(), contact(), authors(), responsible(), terms(), privacy(), cookies()]
