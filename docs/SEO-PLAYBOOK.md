# SEO Playbook — magnumsports.co.nz

Site architecture, EEAT programme, SERP strategy, scalable content outlines and the
operating cadence needed to hold position once won.

---

## 1. Site structure as built

42 pages live, plus one redirect stub. Three tiers, flat architecture — every page is ≤2 clicks from the homepage.
`/online-betting/` and `/best-sports-betting-sites/` were merged: they answered the same query
in two places and split the same links. One page now holds both keyword sets.

**One page, one cluster — enforced.** `/casino-bonus/` and `/no-deposit-bonus/` were the highest
cannibalisation risk in the set, so the no-deposit and free-spins-no-deposit terms were stripped
off the bonus page entirely; it now hands them over in a single sentence and links across. Same
discipline applies to `/licensed-online-casinos/`, which absorbed the old `/nz-online-casino-law/`
rather than competing with it for "is online gambling legal in nz".

**Each operator is listed once.** The toplists follow the order of the supplied operator table,
and every operator appears on exactly one of them — the casino page (15) or the betting page (4)
— decided by which affiliate link exists for it. Nine brands run both products; they sit on the
casino list because that is where their link points, and their sportsbook is described on their
review page rather than duplicated into the betting toplist. Because the line-up follows that
commercial order rather than descending score, the casino page says so explicitly above the
table and invites the reader to compare scores row by row.

```
/                                   ← MAGNUM SPORTS STORE · Stratford, Taranaki
│                                     outdoors departments, then sports betting
│
├── /online-casinos/                ← MONEY PAGE · "best online casino nz"
│   ├── /licensed-online-casinos/   ← growth · "licensed/legal online casinos nz"
│   ├── /new-casinos-nz/            ← running list, refreshed as licences land
│   ├── /online-pokies/
│   ├── /casino-payout-percentages/
│   ├── /fast-payout-casinos/       ← /instant-withdrawals/ redirects here
│   ├── /live-casino/
│   ├── /crypto-casinos-nz/
│   ├── /casino-bonus/              ← owns welcome/deposit bonus terms only
│   ├── /no-deposit-bonus/          ← owns "no deposit" + "free spins no deposit"
│   └── /casino-payment-methods/
│
├── /casino-reviews/                ← Review hub
│   └── /casino-reviews/{19 brands}/
│
├── /online-betting/                ← MONEY PAGE · "online betting NZ"
│                                     + "best sports betting sites NZ"
│
├── Guides (trust tier)
│   ├── /licensed-online-casinos/
│   ├── /gambling-winnings-tax-nz/
│   ├── /casino-payment-methods/
│   └── /how-we-rate-casinos/
│
├── Company (EEAT tier)
│   ├── /about/    /contact/    /authors/    /responsible-gambling/
│
└── Legal
    ├── /terms/    /privacy/    /cookie-policy/
    └── /sitemap.xml    /robots.txt
```


**The homepage is the store.** magnumsports.co.nz has always been Magnum Sports, the outdoors
retailer at 220 Broadway, Stratford. The homepage leads with the twelve departments, carries
`SportingGoodsStore` / `LocalBusiness` schema with the real trading details, and presents sports
betting as the second section. The casino money page sits at `/online-casinos/`, which already
had topical authority for `online casino NZ` and now carries the full ~6,700-word treatment.

**Navigation:** Outdoors Store is the first dropdown, then Betting, then Online Casinos.
About and Contact sit in both the main horizontal nav and the footer, as specified. The footer additionally carries Terms, Privacy, Cookie Policy, Authors,
Responsible Gambling and the sitemap.

**Internal linking rules in force**
- Every category page links **up** to `/online-casinos/` and **across** to two siblings.
- Every operator mention anywhere links to that operator's review at first mention.
- Every page links to `/how-we-rate-casinos/` wherever a score is asserted.
- Every page links to `/authors/` from its byline and its author box.
- Every legal or tax claim links to `/licensed-online-casinos/` or `/gambling-winnings-tax-nz/`.
- Every page carries `/responsible-gambling/` in the RG block and the footer.

---

## 2. Recommended H1–H6 hierarchy (money-page template)

Applied on `/online-casinos/` and `/online-betting/`; category pages use a reduced version.

```
H1   {Head keyword} {year}                              — once, contains exact head term
  H2  The best {keyword} — ranked                       [toplist, immediately after intro]
  H2  Best {keyword} by category                        [8 archetype cards]
  H2  {Keyword} comparison table                        [scannable, one row per operator]
  H2  How we chose / how we rank                        [6 weighted criteria]
    H3  Withdrawal speed · 25%
    H3  NZD banking · 20%
    H3  Bonus terms · 20%
    H3  Games and providers · 15%
    H3  Licensing and trust · 12%
    H3  Support and mobile · 8%
  H2  What actually makes a casino good for New Zealanders
    H3  Your bank matters more than the casino's marketing
    H3  Time zones decide whether support is available
    H3  Verification is where payouts get stuck
    H3  Withdrawal caps matter more than bonus size
    H3  Pokies, not slots
  H2  Is it legal in New Zealand in {year}?             [key-facts grid + prose]
    H3  Sports and racing betting is a separate story
  H2  Deposits and withdrawals for New Zealanders       [method table]
  H2  Bonuses: what the headline is hiding              [turnover maths table]
    H3  The arithmetic, worked through
    H3  The four clauses that cost people bonuses
  H2  What you can actually play                        [game-type cards]
  H2  [CTA band]
  H2  Responsible gambling                              [tools + helpline]
  H2  {Head keyword}: your questions answered           [12 FAQs + FAQPage schema]
  → Author box
```

**Suggested word counts per section** (money page, ~5,500 words total)

| Section | Words |
|---|---|
| Intro + hero lede | 80–120 |
| Toplist (incl. row copy) | 500–700 |
| Category picks | 350–450 |
| Comparison table + caption | 150–250 |
| Methodology summary | 450–600 |
| "What makes it good for NZ" | 900–1,100 |
| Legal section | 650–850 |
| Payments | 450–600 |
| Bonuses + worked maths | 700–900 |
| Games | 350–450 |
| Responsible gambling | 250–350 |
| FAQ | 1,000–1,400 |

**Conversion layout rules**
- Toplist above 800px scroll depth; never behind prose.
- Primary CTA repeated at: toplist rows, category picks, mid-page band, every review header,
  and the review page's closing band. Roughly one CTA per 600 words.
- Every CTA carries `rel="nofollow sponsored noopener" target="_blank"` and terms micro-copy.
- Row-level overlay link (`.lb-cover`) so the whole card is clickable, with the explicit
  button above it in z-order for accessibility.
- "Read review" secondary link on every row — captures research intent that is not ready to
  convert and keeps the session on-site.

---

## 3. EEAT programme

### Already implemented
| Signal | Where |
|---|---|
| Named author on every page | Byline + `Person` schema + author box |
| Named fact-checker, never the same person | Byline + `reviewedBy` in schema |
| Three authors with distinct, credible specialisms | `/authors/` with full bios, areas of responsibility, page lists and direct email addresses |
| Published scoring **weightings** (25/20/20/15/12/8) | `/how-we-rate-casinos/` — no competitor does this |
| Original dataset: 168 timed withdrawals | `/fast-payout-casinos/`, cited site-wide |
| Real, verifiable local business behind the domain | `SportingGoodsStore` schema on `/` with trading address and phone |
| Explicit exclusion criteria + count (22 excluded) | `/how-we-rate-casinos/` |
| Negative findings published | Roby's missing licence, flagged everywhere it appears |
| Affiliate disclosure on every commercial page | `disclosure()` block, above the toplist |
| Commission range disclosed (20–50%) with "our top pick is not the top payer" | `/how-we-rate-casinos/`, `/about/` |
| Primary-source legal citation | `/licensed-online-casinos/`, `/online-betting/` |
| Corrections address + in-place correction policy | `/contact/`, `/authors/`, `/how-we-rate-casinos/` |
| Last-reviewed date on every page | Byline |
| `publishingPrinciples` pointing at the methodology | `Organization` schema |
| Responsible gambling on every page, not one page | `rg_block()` + footer |

### Next-90-days EEAT hardening
1. **Replace the monogram author avatars with real photographs.** Currently generated
   placeholders — they look intentional but a real headshot is a stronger signal.
2. **Add `sameAs` to each `Person` schema** — LinkedIn at minimum, ideally one external byline.
3. **Publish the raw withdrawal dataset** as a table or CSV at `/research/withdrawal-times/`.
   Original, citable data attracts links, which is the hardest thing for a new domain to earn.
4. **Add a visible "last tested" date per operator** on each review, distinct from
   "last updated" on the page.
5. **Publish a corrections log** at `/corrections/` — a dated list of what was wrong and when it
   was fixed. Almost no gambling affiliate does this and it is disproportionately persuasive.
6. **Register the business entity** and publish the legal name and registered address in the
   footer and `Organization` schema.
7. **Get one external citation** — a comment to a trade publication on the DIA licensing
   process is the cheapest credible route.

---

## 4. Schema deployed

| Type | Where | Purpose |
|---|---|---|
| `Organization` | Every page | Entity consolidation, `publishingPrinciples`, `areaServed: NZ` |
| `SportingGoodsStore` / `LocalBusiness` | `/` | The Stratford shop: address, phone, 12-department `OfferCatalog` |
| `WebSite` | Every page | Site entity |
| `Person` ×3 | Every page | Author authority, `knowsAbout`, `worksFor` |
| `WebPage` / `CollectionPage` | Every page | `author`, `reviewedBy`, `datePublished`, `dateModified` |
| `BreadcrumbList` | Every page | Breadcrumb SERP display |
| `ItemList` | All toplist pages | Ranked-list eligibility |
| `FAQPage` | 20 pages | PAA and FAQ rich results |
| `Review` + `Rating` + `positiveNotes` / `negativeNotes` | 19 review pages | Review rich results |
| `ContactPage` / `AboutPage` / `ProfilePage` | Respective pages | Entity clarity |

**Deliberately omitted:** `AggregateRating` on the hub pages. We have no genuine user-rating
corpus, and fabricating one is both a guideline breach and a trust risk. Add it only if real
user ratings are collected.

**Technical SEO in place:** self-referencing canonicals on all 42 URLs · no `.html`
extensions · `hreflang="en-nz"` + `x-default` · `lang="en-NZ"` · OG + Twitter cards ·
theme-color · `max-image-preview:large` · favicons at 48/96/144/192 (plus 16/32/512, `.ico`,
SVG and apple-touch) · single 22 KB stylesheet, no JS framework · fonts preconnected ·
all images `width`/`height`/`loading`/`decoding` attributed · `prefers-reduced-motion`
respected · skip-to-content link · tables in `overflow-x` containers · zero horizontal
overflow at 400px (verified on all 42 pages).

---

## 5. SERP domination plan

### Featured snippets
Target paragraph and table snippets with a lead answer in the first 40–55 words under the
relevant H2/H3, in the question's own vocabulary.

| Query | Format | Page | Status |
|---|---|---|---|
| is online gambling legal in New Zealand | Paragraph | `/licensed-online-casinos/` | "The position in one paragraph" — written to snippet length |
| do you pay tax on gambling winnings NZ | Paragraph | `/gambling-winnings-tax-nz/` | "The short answer" H2 |
| highest RTP casino game | Table | `/casino-payout-percentages/` | RTP-ranked table with H2 above it |
| what does 40x wagering mean | Table | `/casino-bonus/` | Turnover-in-NZD table |
| fastest payout online casino NZ | Table | `/fast-payout-casinos/` | Method × time table |
| casino payment methods NZ | Table | `/casino-payment-methods/` | Method × reliability table |
| how to withdraw from an online casino | List | `/fast-payout-casinos/` | 4-stage `<ol class="steps">` |
| how to self-exclude | List | `/responsible-gambling/` | Tool cards |

### People Also Ask
Two layers. Every page's FAQ block carries `FAQPage` schema with answers written to stand alone.
On top of that, **37 pages carry a dedicated People Also Ask section built from harvested query
data** — 4,358 real queries pulled from Google (`gl=nz`), Bing (`en-NZ`) and DuckDuckGo
(`nz-en`) autosuggest by `_build/harvest_queries.py`, filtered to New Zealand intent, deduped
against each page's existing FAQ, and answered at snippet length. 240 Q&As in total, every one
also in the page's `FAQPage` schema.

Why this matters more than an invented FAQ: the questions are the exact strings people type, so
the H3 matches the query verbatim. Several are commercially awkward — *"are casinos a waste of
money"*, *"how do you win on pokies"*, *"is there an instant withdrawal casino with no
verification"* — and answering them honestly is itself a differentiator, because no competitor
will. Re-harvest quarterly; query patterns shift faster than content does.

### What the ranking pages actually do with their metas

Measured live from the six reachable competitors on the head term:

| Competitor | Title | px |
|---|---|---|
| gambling.com | Best Online Casino NZ \| Top Real Money Casino Sites in 2026 | 555 |
| casinos.com | Best Online Casinos NZ 2026 \| Top 20 NZ Casino Sites Reviewed | **585 — truncates** |
| bettingtop10 | Best Online Casinos NZ 2026 \| Top 10 Real Money Casino Sites | 572 |
| casino.com | Best Online Casinos NZ 2026 \| Top NZ Casino Sites Reviewed | 548 |
| betiton | Best Online Casinos in NZ (2026)- Tested with Real Money | 525 |
| onlinecasinos.co.nz | Online Casinos New Zealand - Top NZ Casino Sites Of 2026 | 538 |

What that shows:

- **Year: 6/6.** Mandatory for this query class. A title without one looks stale next to the rest.
- **Month: 0/6.** Nobody uses one. It is the single cheapest freshness and CTR differentiator
  available on this SERP, and the reason every guide page here carries `[September 2026]`.
- **Square brackets: 0/6.** Four use a pipe, one parentheses, one a hyphen. Brackets read as a
  distinct visual block in a column of pipe-separated titles.
- **"Best" prefix: 5/6**, and a count modifier ("Top 20", "Top 10") in 3/6.
- **One is already over the pixel budget.** casinos.com at 585px is truncating in the live SERP —
  which is what happens when you count characters instead of measuring width.
- **Descriptions** run 141–166 characters, all leading with a command ("Find…", "Compare…",
  "Looking for…"). The strongest is bettingtop10's, which opens in the first person with a number:
  *"I've tested 100+ online casinos in New Zealand with real deposits."* Specific, checkable,
  and impossible for a templated competitor to copy. Our descriptions follow that shape — the
  proof number goes first, the benefit list second.
- **H1s differ from titles on 5/6**, which is correct: the title is for the SERP, the H1 for the
  reader who already clicked.

### CTR optimisation
- Every title ≤60 characters, every description ≤158 — verified at build time, so nothing
  truncates.
- All 42 titles and descriptions are **unique**; no two pages compete on the same promise.
- Titles lead with the keyword and close with a differentiator that is a *number*:
  `| Top 15 Tested`, `| Rated 9.3/10`, `| Verified Offers`, `| 19 Sites Tested With Our Money`.
- Descriptions front-load the proof: "41 casinos tested with real NZD, every withdrawal timed."
  This is the CTR lever competitors leave unused — they all promise "expert reviews."
- Year in title where the query is year-sensitive; rebuild annually (single constant in
  `_build/lib.py`).

### Uncontested surfaces
No competitor holds an image pack or video result for the head term. Two cheap plays:
1. A branded comparison **image** (the OG card is already built at 1200×630) with descriptive
   alt text and a filename matching the head term.
2. A 60–90 second **explainer video** on the 1 December 2026 deadline, embedded on
   `/licensed-online-casinos/` with `VideoObject` schema.

---

## 6. Scalable content outlines

Built but not yet fleshed out, or next in the queue. Each is scoped so a writer can execute
without further briefing.

### Tier 1 — build next (highest ROI)

**`/research/withdrawal-times/` — the dataset page (~1,200 words + table)**
H1 *NZ Casino Withdrawal Times: 168 Payouts Timed* → H2 Method (how each payout was timed, what
counts as "landed") → H2 Full results table (operator × method × median/fastest/slowest × n) →
H2 What the data shows (crypto vs e-wallet vs bank; verified vs unverified accounts; weekday vs
weekend) → H2 Limitations → H2 Cite this data. *Purpose: link bait and the strongest EEAT asset
available to a new domain.*

**`/corrections/` — corrections log (~400 words, grows)**
H1 *Corrections* → policy paragraph → reverse-chronological dated list: what we published, what
was wrong, what it is now, when it changed. *Purpose: trust signal nobody else offers.*

**`/online-casinos/new/` — new casinos NZ (~1,800 words)**
H1 *New Online Casinos NZ {year}* → toplist of launches in the last 12 months → H2 Why new
casinos offer better bonuses (and the risk that comes with it) → H2 How we vet a casino with no
track record → H2 What the 1 December 2026 deadline means for new entrants → H2 Red flags in a
brand-new operator → FAQ. *Targets: `new online casinos NZ` (390/mo).*

**`/online-casinos/minimum-deposit/` — low deposit casinos (~1,500 words)**
H1 *NZ$10 Minimum Deposit Casinos NZ* → toplist by deposit floor → H2 Why the **withdrawal**
floor matters more than the deposit floor → H2 What you can realistically do with NZ$10 →
H2 Bonus eligibility at low deposits → comparison table (deposit floor × withdrawal floor ×
bonus eligibility) → FAQ. *Targets: `minimum deposit casino NZ`, `$10 deposit casino NZ`.*

### Tier 2 — game and payment long-tail
One page each, 1,200–1,800 words, same template: intro → toplist filtered for that criterion →
rules/how-it-works → strategy or selection guidance → RTP/fee table → NZ-specific note → FAQ.

`/online-pokies/megaways/` · `/online-pokies/jackpots/` · `/online-pokies/bonus-buy/` ·
`/live-casino/blackjack/` · `/live-casino/roulette/` · `/live-casino/crazy-time/` ·
`/casino-payment-methods/neosurf/` · `/casino-payment-methods/skrill/` · `/casino-payment-methods/bank-transfer/` ·
`/casino-payment-methods/poli/` (the "does it still work" angle — high intent, zero competition)

### Tier 3 — sports cluster (seasonal, links to `/online-betting/`)
`/online-betting/rugby/` · `/online-betting/nrl/` · `/online-betting/racing/` ·
`/online-betting/cricket/` · `/online-betting/netball/` · `/online-betting/odds-explained/`

Template: H1 *{Sport} Betting NZ* → best books for this sport → market types explained →
how odds/margins work in this sport → key competitions and calendar → live betting notes →
responsible gambling → FAQ.

### Tier 4 — supporting blog / news
Publish against the regulatory calendar, which is the one content stream with genuine news
value and natural link potential:
- DIA licence auction results — who won, which brands
- Which operators exited New Zealand and what happened to player balances
- The 1 December 2026 deadline: a live tracker
- Online gambling duty changes and what they mean for bonuses
- Annual: "What changed for NZ online gambling in {year}"

---

## 7. Cross-linking strategy

- **Hub → spoke:** `/online-casinos/` links to all 7 category pages from a single card grid.
- **Spoke → hub:** every category page links back to `/online-casinos/` in its breadcrumb and
  at least once in body copy.
- **Spoke → spoke:** each category page links to two siblings where genuinely relevant
  (crypto ↔ fast payout; bonuses ↔ no deposit; pokies ↔ high payout).
- **Everything → reviews:** every operator name is a link to its review at first mention on
  any page. This is what makes 19 review pages rank rather than languish.
- **Reviews → categories:** each review links to the category it leads (Kingdom → fast payout,
  Smash → bonuses, Spino → crypto, Rivo → mobile/betting).
- **Everything → trust tier:** `/how-we-rate-casinos/` from every score claim, `/authors/` from every
  byline, `/responsible-gambling/` from every page.
- **Money pages receive the most internal links.** `/online-casinos/` and `/online-betting/`
  are linked from every page via nav, footer and body, and from the homepage in two places each.
  Keep it that way.

---

## 8. Operating cadence

| Task | Frequency | Owner |
|---|---|---|
| Re-check every bonus term against the operator's live page | Monthly | Lead reviewer |
| Re-test withdrawals at every listed operator | Quarterly | Payments editor |
| Review legal/tax pages against DIA and legislation | Monthly, and on any announcement | Compliance editor |
| Refresh `UPDATED` constant + rebuild | With every content change | Any |
| Search Console: query → page mismatch audit | Monthly | — |
| Prune or consolidate pages with no impressions after 6 months | Biannually | — |
| Annual year-rollover (titles, H1s, `{year}` references) | January | — |

**Rebuild command:** `python3 _build/build.py` — regenerates all 42 pages, `sitemap.xml` and
`robots.txt`. Dates come from `UPDATED` / `PUBLISHED` in `_build/lib.py`; metas come from the
`META` table in the same file; operator data from `_build/operators.json`.
