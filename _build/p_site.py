# -*- coding: utf-8 -*-
"""Company and legal pages."""
from lib import *


def simple(title, desc, path, crumb, h1, lede, body, eyebrow=None, kind="WebPage", extra=None,
           faq=None, noindex=False):
    ex = [crumb_schema([("Home", "/")] + crumb)]
    if faq:
        ex.append(faq_schema(faq, f"{SITE}{path}#faq"))
    if extra:
        ex += extra
    schema = page_schema(kind, title, desc, path, extra=ex)
    o = [head(title, desc, path, schema, robots="noindex,follow" if noindex else None),
         crumbs([("Home", "/")] + [(c[0], None if i == len(crumb) - 1 else c[1])
                                   for i, c in enumerate(crumb)])]
    eb = f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else ""
    o.append(f'''<section class="hero"><div class="wrap">{eb}<h1>{h1}</h1>
<p class="lede">{lede}</p></div></section>
''')
    o.append(body)
    if faq:
        o.append(faq_block(faq))
    o.append(footer())
    return write(path, "".join(o))


TEL = f'<a href="tel:{STORE["phone_tel"]}">{esc(STORE["phone_display"])}</a>'
ADDR = f'{esc(STORE["street"])}, {esc(STORE["suburb"])}, {esc(STORE["region"])} {esc(STORE["postcode"])}'


# ================================================================ ABOUT
def about():
    depts = by_dept()
    online = sum(len(d[4]) for d in depts)
    body = f'''<section class="sec"><div class="wrap"><div class="prose prose--wide">
<h2>Outdoor gear, delivered</h2>
<p>{esc(STORE["name"])} is a New Zealand online store for outdoor gear: gloves and clothing, pouches, packs and storage, bipods and hunting accessories. We deliver anywhere in New Zealand.</p>

<h2>What we sell</h2>
<p>{online} products across {len(depts)} departments:</p>
{cards([(ic, esc(n), b, f"/shop/{slug}/", f"Shop {len(items)} products") for n, slug, ic, b, items in depts])}

<h2>How ordering works</h2>
<p>Add what you want to your cart and send us the order. We reply to confirm stock and how to pay before anything is charged, and deliver in 7 to 10 days. Every price includes delivery anywhere in New Zealand and GST. {PAY_HOW}</p>
<p>The details are in our <a href="/terms/">terms</a>, and the answers to common questions are on the <a href="/#faq">homepage</a> and each department page.</p>

<h2>Get in touch</h2>
{keyfacts([("Phone", TEL), ("Email", f'<a href="mailto:{EMAIL}">{EMAIL}</a>'),
           ("Business address", ADDR), ("Online shop", '<a href="/shop/">Shop now</a>')])}
</div></div></section>
'''
    return simple(*META["/about/"], "/about/", [("About Us", "/about/")], f"About {esc(STORE['name'])}",
                  "A New Zealand online store for outdoor gear: clothing, gloves, bags and hunting accessories, "
                  "delivered NZ-wide.",
                  body, eyebrow=icon("cart") + " Outdoor gear online",
                  extra=[store_schema(),
                         {"@type": "AboutPage", "@id": f"{SITE}/about/#aboutpage",
                          "mainEntity": {"@id": f"{SITE}/#store"}}])


# ============================================================== CONTACT
def contact():
    body = f'''<section class="sec"><div class="wrap">
<div class="grid grid--2">
<div>
<h2>Send us a message</h2>
<p>Stock checks, questions about an order or delivery, or advice on gear. For anything urgent, ring the shop.</p>
<form class="form" id="contact-form" action="mailto:{EMAIL}" method="post" enctype="text/plain" data-send="{esc(MESSAGE_URL)}">
<div class="hp" aria-hidden="true"><label for="c-website">Leave this empty</label><input id="c-website" name="website" tabindex="-1" autocomplete="off"></div>
<div class="field"><label for="cname">Your name</label><input id="cname" name="name" type="text" autocomplete="name" required></div>
<div class="field"><label for="cemail">Email address</label><input id="cemail" name="email" type="email" autocomplete="email" required><span class="hint">We only use this to reply to you. See our <a href="/privacy/">privacy policy</a>.</span></div>
<div class="field"><label for="ctopic">What is this about?</label>
<select id="ctopic" name="topic">
<option>Checking stock</option>
<option>An online order</option>
<option>Delivery</option>
<option>Advice on gear</option>
<option>Returns or a faulty item</option>
<option>Privacy or data request</option>
<option>Something else</option>
</select></div>
<div class="field"><label for="cmsg">Message</label><textarea id="cmsg" name="message" required></textarea>
<span class="hint">For an order, include the name you ordered under and roughly when.</span></div>
<button class="btn" type="submit">Send message</button>
</form>
<div id="contact-done" class="note note--ok" hidden tabindex="-1"><b>Thank you: your message is on its way</b>
<p>We reply by email, usually the same working day. Anything urgent? Call {TEL}.</p></div>
</div>
<div>
<h2>Other ways to reach us</h2>
<div class="card" style="margin-bottom:16px"><div class="card-ic">{icon("chat")}</div>
<h3>Phone the shop</h3><p>{TEL}</p>
<p style="font-size:.86rem;color:var(--mute);margin-bottom:0">The quickest way to check stock or ask about an order.</p></div>
<div class="card" style="margin-bottom:16px"><div class="card-ic">{icon("mail")}</div>
<h3>Email</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p style="font-size:.86rem;color:var(--mute);margin-bottom:0">Orders, delivery and general questions.</p></div>
<div class="card"><div class="card-ic">{icon("flag")}</div>
<h3>Business address</h3><p>{esc(STORE["legal"])}<br>{ADDR}</p>
<p style="font-size:.86rem;color:var(--mute);margin-bottom:0">We are an online store; orders are delivered, not collected.</p></div>
</div>
</div>
</div></section>
'''
    return simple(*META["/contact/"], "/contact/", [("Contact Us", "/contact/")], "Contact Us",
                  f"Phone {esc(STORE['phone_display'])} or email us about an order, delivery, stock or a product.",
                  body, eyebrow=icon("mail") + " Stock checks, orders and advice", kind="ContactPage",
                  extra=[store_schema(),
                         {"@type": "ContactPage", "@id": f"{SITE}/contact/#contactpage",
                          "mainEntity": {"@id": f"{SITE}/#store"}}])


# ================================================================ TERMS
def terms():
    body = f'''<section class="sec"><div class="wrap"><div class="prose">
<p><strong>Last updated:</strong> {UPDATED_NZ}</p>
<h2>1. About these terms</h2>
<p>These terms apply to your use of magnumsports.co.nz (&ldquo;this site&rdquo;) and to orders placed through our online shop. The site is run by {esc(STORE["legal"])}, {ADDR} (&ldquo;we&rdquo;, &ldquo;us&rdquo;). By using the site or placing an order you agree to them.</p>

<h2>2. Orders</h2>
{"<p>If you pay by card at checkout, your payment is an offer to buy at the price shown. We check stock and dispatch; if an item is unavailable we tell you and refund it in full within five working days.</p>" if CHECKOUT_URL else ""}
<p>Sending an order request from the cart is an offer to buy. It is not a contract until we reply to confirm stock and how to pay. We may decline or cancel an order &mdash; for example if an item is out of stock or a price is shown in error &mdash; and if you have already paid we will refund you in full.</p>

<h2>3. Prices</h2>
<p>Prices are in New Zealand dollars and include GST and delivery anywhere in New Zealand; there is no separate freight charge. We may change prices at any time, but the price you pay is the one we confirm to you.</p>

<h2>4. Payment</h2>
<p>We take payment only through Stripe. {PAY_HOW} The full list of methods is in our <a href="/#faq">FAQ</a>. Stripe processes every payment on its own secure page; we never see or store your card number, and we never ask for payment details by email or phone. Goods are dispatched once payment has cleared.</p>

<h2>5. Delivery</h2>
<p>We deliver within New Zealand. Delivery takes <strong>7 to 10 days</strong> from when we confirm your order. Risk in the goods passes to you on delivery.</p>

<h2>6. Returns and your consumer rights</h2>
<p>Nothing in these terms limits your rights under the <strong>Consumer Guarantees Act 1993</strong> or the <strong>Fair Trading Act 1986</strong>. If something you buy from us is faulty or not as described, contact us on {TEL} or <a href="mailto:{EMAIL}">{EMAIL}</a> and we will put it right as those Acts require. If you have simply changed your mind, get in touch and we will tell you what we can do.</p>

<h2>7. Product information</h2>
<p>We take care to describe products accurately. Photos are for illustration, and colours on screen can differ from the item. Product specifications come from the manufacturer; if a detail matters to you, ask us before you order.</p>

<h2>8. Use of this site</h2>
<p>Content on this site &mdash; text, photographs, design and code &mdash; is owned by us or used under licence. You may view and share links to it for personal use, but not copy or republish it without our permission. Product names and trade marks belong to their owners.</p>

<h2>9. Liability</h2>
<p>To the extent the law allows, we are not liable for indirect or consequential loss arising from your use of this site. This does not affect your rights under the Consumer Guarantees Act or Fair Trading Act.</p>

<h2>10. Privacy and cookies</h2>
<p>How we handle personal information is set out in our <a href="/privacy/">Privacy Policy</a>, and our use of cookies and browser storage in our <a href="/cookie-policy/">Cookie Policy</a>.</p>

<h2>11. Changes and governing law</h2>
<p>We may update these terms; the date above shows when they last changed, and the terms that apply to an order are the ones in place when we confirmed it. These terms are governed by New Zealand law.</p>

<h2>12. Contact</h2>
<p>{TEL} &middot; <a href="mailto:{EMAIL}">{EMAIL}</a> &middot; {ADDR}</p>
</div></div></section>
'''
    return simple(*META["/terms/"], "/terms/", [("Terms and Conditions", "/terms/")], "Terms and Conditions",
                  "The terms for using this site and for ordering from our online shop: orders, prices, payment, "
                  "delivery and your consumer rights.", body)


# ============================================================== PRIVACY
def privacy():
    body = f'''<section class="sec"><div class="wrap"><div class="prose">
<p><strong>Last updated:</strong> {UPDATED_NZ}</p>
<p>This policy explains how {esc(STORE["legal"])} collects, uses, stores and discloses personal information. We comply with the <strong>Privacy Act 2020</strong> and its information privacy principles.</p>

<h2>1. What we collect</h2>
<ul>
<li><strong>Orders.</strong> When you send an order request: your name, email address, phone number, delivery address, the items you want and any notes. These reach us by email, delivered through our website host, Cloudflare.</li>
<li><strong>Messages.</strong> When you contact us: your name, email address and what you tell us.</li>
<li><strong>Payments.</strong> Every payment is made through Stripe on its own secure page. Stripe tells us the order is paid; your card or wallet details go to Stripe, not to us (see <a href="https://stripe.com/privacy" rel="nofollow noopener" target="_blank">Stripe&rsquo;s privacy policy</a>).</li>
<li><strong>Your cart.</strong> Kept in your own browser until you send the order or clear it. We do not see it until you send us the order.</li>
<li><strong>Server logs.</strong> Our host records IP addresses and pages requested, for security and diagnostics.</li>
</ul>

<h2>2. How we use it</h2>
<p>To process and deliver your order, take payment, answer your questions, and meet our legal obligations, including keeping records for tax. We do not sell or rent personal information, and we do not use it for advertising.</p>

<h2>3. Who we share it with</h2>
<ul>
<li><strong>Couriers</strong>, who need your name, address and phone number to deliver your order.</li>
<li><strong>Stripe</strong>, which processes every payment.</li>
<li><strong>Our hosting and email providers</strong>, which run the site and carry our email. Some are overseas; where that is the case we take reasonable steps to ensure comparable safeguards, consistent with information privacy principle 12.</li>
<li><strong>Authorities</strong>, where the law requires it.</li>
</ul>

<h2>4. How long we keep it</h2>
<p>Order and payment records are kept for seven years, as New Zealand tax law requires. Other messages are kept for up to two years, then deleted.</p>

<h2>5. Security</h2>
<p>The site is served over HTTPS. Access to order information is limited to the people in the business who need it.</p>

<h2>6. Your rights</h2>
<p>You may ask to see the personal information we hold about you and ask us to correct it. Email <a href="mailto:{EMAIL}">{EMAIL}</a> or ring {TEL}. We respond within 20 working days, as the Privacy Act requires. If you are not satisfied with our response, you may complain to the <strong>Office of the Privacy Commissioner</strong> at <a href="https://www.privacy.org.nz/" rel="nofollow noopener" target="_blank">privacy.org.nz</a>.</p>

<h2>7. Changes</h2>
<p>We may update this policy; the date at the top shows when it last changed.</p>
</div></div></section>
'''
    return simple(*META["/privacy/"], "/privacy/", [("Privacy Policy", "/privacy/")], "Privacy Policy",
                  "What we collect when you order or contact us, why, who we share it with, and how to see or "
                  "correct it. We comply with the Privacy Act 2020.", body)


# ========================================================== COOKIE POLICY
def cookies():
    body = f'''<section class="sec"><div class="wrap"><div class="prose">
<p><strong>Last updated:</strong> {UPDATED_NZ}</p>
<h2>What this covers</h2>
<p>Cookies are small text files a website stores on your device; browser storage (&ldquo;local storage&rdquo;) does a similar job. This policy explains which of these the site uses.</p>

<h2>What this site stores</h2>
{table(["What", "What it does", "Set without asking?", "How long"], [
 ["<b>Shopping cart</b>", "Local storage in your browser holding the items in your cart. Set only when you add an item; never sent to us unless you send an order request", "<span class='t-yes'>Yes &mdash; you asked for it</span>", "Until you clear the cart"],
], minw=620)}
<p>That is the only thing the site itself stores. We do not use analytics, advertising or tracking cookies.</p>

<h2>Third parties</h2>
<p><strong>Google Fonts</strong> serves the typefaces on this site. It does not set advertising cookies. If you pay by card online, you do so on <strong>Stripe</strong>&rsquo;s own payment page, which sets its own cookies for security and fraud prevention under Stripe&rsquo;s policies, not ours. Links to other websites are governed by those sites&rsquo; own policies once you follow them.</p>

<h2>Clearing it</h2>
<p>Every browser lets you delete cookies and site data. Doing so for this site empties your cart; nothing else changes.</p>
<ul>
<li><strong>Chrome:</strong> Settings &rarr; Privacy and security &rarr; Site settings &rarr; View permissions and data stored across sites</li>
<li><strong>Safari:</strong> Settings &rarr; Safari &rarr; Advanced &rarr; Website Data (iOS) or Safari &rarr; Settings &rarr; Privacy &rarr; Manage Website Data (macOS)</li>
<li><strong>Firefox:</strong> Settings &rarr; Privacy &amp; Security &rarr; Cookies and Site Data</li>
<li><strong>Edge:</strong> Settings &rarr; Cookies and site permissions</li>
</ul>

<h2>Contact</h2>
<p>Questions: <a href="mailto:{EMAIL}">{EMAIL}</a>. See also our <a href="/privacy/">Privacy Policy</a> and <a href="/terms/">Terms and Conditions</a>.</p>
</div></div></section>
'''
    return simple(*META["/cookie-policy/"], "/cookie-policy/", [("Cookie Policy", "/cookie-policy/")],
                  "Cookie Policy", "What this site stores in your browser, and how to clear it. In short: your "
                  "cart, and nothing that tracks you.", body)


def build():
    return [about(), contact(), terms(), privacy(), cookies()]
