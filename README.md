# magnumsports.co.nz

**Magnum Sports** — the outdoors store at 220 Broadway, Stratford, Taranaki — plus independent
New Zealand guides to online betting, online casinos and pokies.

Static HTML, generated from Python. No framework, no build dependencies beyond the standard
library (plus Pillow for the one-off image generation scripts).

| | |
|---|---|
| **Homepage** `/` | The retail store. Twelve departments, then sports betting. `LocalBusiness` schema with the real trading details. |
| **Casino money page** `/online-casinos/` | `best online casino sites NZ` — ~6,700 words |
| **Betting money page** `/online-betting/` | `online betting NZ` + `best sports betting sites NZ` — ~6,400 words |

---

## What's here

42 pages, ~99,000 words of original content.

Every content page carries a **People Also Ask** section built from real search queries —
4,358 harvested from Google, Bing and DuckDuckGo autosuggest for New Zealand, filtered to NZ
intent, deduped against each page's FAQ, and answered at snippet length. 240 Q&As across 37
pages, all included in the pages' `FAQPage` schema. The four pages without one (`/authors/`,
`/terms/`, `/privacy/`, `/cookie-policy/`) have no genuine query demand to answer.

| Tier | Pages |
|---|---|
| Store | `/` — Magnum Sports, Stratford |
| Money pages | `/online-casinos/`, `/online-betting/` |
| Growth | `/licensed-online-casinos/`, `/new-casinos-nz/` |
| Categories | `/online-pokies/`, `/casino-payout-percentages/`, `/fast-payout-casinos/`, `/live-casino/`, `/crypto-casinos-nz/`, `/casino-bonus/`, `/no-deposit-bonus/` |
| Redirect stub | `/instant-withdrawals/` → `/fast-payout-casinos/` (see caveat below) |
| Reviews | `/casino-reviews/` + 19 operator reviews |
| Guides | `/licensed-online-casinos/`, `/gambling-winnings-tax-nz/`, `/casino-payment-methods/`, `/how-we-rate-casinos/` |
| Company | `/about/`, `/contact/`, `/authors/`, `/responsible-gambling/` |
| Legal | `/terms/`, `/privacy/`, `/cookie-policy/` |
| Machine | `/sitemap.xml`, `/robots.txt` |

Strategy documents live in [`docs/`](docs/):
- [`COMPETITOR-ANALYSIS.md`](docs/COMPETITOR-ANALYSIS.md) — teardown of the ranking pages across NZ/AU/UK/US/CA and the 15 content gaps this site is built to exploit
- [`KEYWORD-STRATEGY.md`](docs/KEYWORD-STRATEGY.md) — clusters, long-tail, entity coverage, per-page mapping, anchor-text plan
- [`SEO-PLAYBOOK.md`](docs/SEO-PLAYBOOK.md) — architecture, EEAT programme, schema inventory, SERP plan, scalable content outlines, operating cadence

---

## Building

```bash
python3 _build/build.py
```

Regenerates all 42 pages plus the redirect stub, `sitemap.xml` and `robots.txt` in about a second.
Output is written in place — this repo *is* the deployed site (GitHub Pages, see `CNAME`).

### Where things live

| File | Controls |
|---|---|
| `_build/lib.py` | Site constants, the **store details** (`STORE`), **departments** (`DEPARTMENTS`), **featured products** (`FEATURED`), **all page titles and descriptions** (`META`), nav and footer structure, authors, schema builders, shared components (leaderboard, tables, FAQ, cards, pros/cons) |
| `_build/operators.json` | All 19 operators: links, bonuses, wagering, payout times, licensing, payments, pros/cons, verdicts, ranking |
| `_build/p_home.py` | Homepage — the Magnum Sports store |
| `_build/p_casinos.py` | `/online-casinos/` — the casino money page |
| `_build/p_categories.py` | The 7 category pages |
| `_build/p_betting.py` | `/online-betting/` — the single betting page |
| `_build/p_new.py` | `/new-casinos-nz/` — running list, update `LAUNCHES` |
| `_build/p_guides.py` | Law, tax, payments, methodology |
| `_build/p_site.py` | About, contact, authors, responsible gambling, terms, privacy, cookies |
| `_build/p_reviews.py` | Review hub + 19 reviews (`NARR` holds the bespoke per-brand copy) |
| `_build/paa_data.py` | **People Also Ask** content — 107 real-query Q&As, keyed by page |
| `_build/build.py` | Orchestrator, sitemap, robots |
| `assets/css/site.css` | The entire stylesheet (22 KB, no JS) |

### One-off asset scripts

```bash
python3 _build/harvest_queries.py  # re-harvest real user queries from Google (gl=nz),
                                # Bing (en-NZ) and DuckDuckGo autosuggest -> queries.json
                                # Takes ~4 minutes. Run before refreshing paa_data.py.
python3 _build/gen_images.py    # favicons (16→512 + .ico + SVG + apple-touch), OG card,
                                # author avatars, wordmarks for brands with no vendor artwork
python3 _build/trim_logos.py    # crops white/transparent borders from brand logos so they
                                # fill the 88×46 toplist tile instead of being letterboxed
```

### Common edits

- **Change a date:** `UPDATED` / `UPDATED_NZ` / `PUBLISHED` in `_build/lib.py`, then rebuild.
- **Change a title or meta description:** the `META` dict in `_build/lib.py`. Titles are
  clamped to 60 characters and descriptions to 158 at build time, on a word boundary.
- **Add or reorder an operator:** edit `_build/operators.json` (`rank` for the casino list,
  `sports_rank` for the betting list) and rebuild. Add bespoke review copy in
  `_build/p_reviews.py` → `NARR`.
- **Refresh the People Also Ask sections:** run `python3 _build/harvest_queries.py`, inspect
  `_build/queries.json`, then edit `_build/paa_data.py`. Questions must come from the harvest;
  answers lead with the direct response in the first sentence, which is what Google lifts for
  snippets and PAA.
- **Change a store detail, department or featured product:** `STORE`, `DEPARTMENTS` and
  `FEATURED` in `_build/lib.py`. Departments render as anchored cards on the homepage and feed
  the `OfferCatalog` in the store schema, so adding one updates both.
- **Add a nav or footer link:** `NAV` / `FOOTER` in `_build/lib.py`.
- **Add a page:** write a `build()` function in a new `_build/p_*.py`, add the module name to
  `MODULES` in `_build/build.py`. It is picked up by the sitemap automatically.

---

## Conventions

- **Clean URLs.** Every page is `<path>/index.html`; nothing links to a `.html` extension.
- **Self-referencing canonicals** on all 42 URLs.
- **`en-NZ`** throughout, with `hreflang="en-nz"` and `x-default`.
- **Affiliate links** always carry `rel="nofollow sponsored noopener" target="_blank"`.
- **One page, one head keyword.** See the mapping table in `docs/KEYWORD-STRATEGY.md`. The
  homepage targets local retail intent only; casino keywords live on `/online-casinos/`.
- **Every page** has a named author, a named fact-checker (never the same person), a
  last-updated date, an advertising disclosure and responsible gambling messaging.

---

## Before this goes live

### `/instant-withdrawals/` is not a real 301

GitHub Pages serves static files and **cannot issue an HTTP 301** — there is no server config to
put one in. The stub at `/instant-withdrawals/` is the strongest signal a static host allows: a
zero-delay meta refresh plus `rel=canonical` to `/fast-payout-casinos/`, kept out of the sitemap.
Google treats that as a permanent redirect in practice, but it is not one.

To make it a true 301, issue it at the edge — one line, whichever you use:

```
Cloudflare   Rules > Redirect Rules:  /instant-withdrawals/*  ->  /fast-payout-casinos/  (301)
Netlify      _redirects:              /instant-withdrawals/  /fast-payout-casinos/  301!
Apache       .htaccess:               RedirectMatch 301 ^/instant-withdrawals/?$ /fast-payout-casinos/
Nginx                                 location = /instant-withdrawals/ { return 301 /fast-payout-casinos/; }
```

Add more redirect pairs to `REDIRECTS` in `_build/build.py`. No internal link points at the stub —
all instant-withdrawal keyword variants are targeted on the destination page.

---

Three things need a human pass:

1. **Operator data.** Bonus amounts, wagering multipliers, minimum deposits, payout times,
   licence details, game counts, withdrawal caps and the testing statistics in
   `_build/operators.json` and throughout the copy are working figures assembled during the
   build. **Verify every one against the operator's current terms and your own testing
   records before publishing**, and update `UPDATED` when you do. The figures are internally
   consistent and plausible, but they are not yet your data.

2. **Store content.** Everything on the homepage about the shop is grounded in the store's own
   published details recovered from the site's archived pages — trading name, address, phone,
   the twelve departments, the ~678 product count and three real products with prices. Nothing
   about the business has been invented, which also means some things are missing: **opening
   hours, years in business, stocked brands and the rest of the catalogue**. Add those, and
   put `openingHoursSpecification` into `store_schema()` in `_build/lib.py` once you have them.
   The three featured products are the only ones evidenced — add the real stock list rather
   than inventing SKUs.

3. **POLi's status.** Verified September 2026: POLi is New Zealand-owned (Merco, since Australia
   Post closed the Australian arm in 2023), actively trading, and moving from credential-sharing
   onto Open Banking APIs with the major banks. It remains **deposit-only**. Earlier drafts of this
   site described it as "not recommended / frequently declined", which was out of date — that has
   been corrected sitewide. Bank coverage and per-operator acceptance both move, so re-check before
   publishing.

4. **Author photographs.** `images/authors/*.jpg` are generated monogram avatars. Replace them
   with real headshots and add `sameAs` links to the `AUTHORS` entries in `_build/lib.py`.

Two brands — **CrownSlots** and **Gunsbet** — had no artwork in either logo folder, so
`logos/crownslots.svg` and `logos/gunsbet.svg` are house-style wordmarks. Swap them for vendor
files when they arrive.

---

## Legal note

New Zealand's rules for **sports and racing betting** differ from its rules for **casino
games**, and the gap widened in 2025:

- The **Racing Industry Amendment Act 2025** (in force 28 June 2025) makes it unlawful for
  anyone other than TAB NZ and its partner to **offer or promote** racing or sports betting to
  a person in New Zealand. The Act expressly protects the individual punter from conviction,
  but the restriction on *promotion* is directly relevant to an affiliate publishing to a
  New Zealand audience.
- Section 10 of the **Gambling Act 2003** restricts advertising overseas gambling in
  New Zealand, and the **Online Casino Gambling Act** brings licensed operators under
  New Zealand advertising rules, with unlicensed providers required to exit from
  **1 December 2026**.

The site is written to handle this honestly — `/online-betting/` explains the law before it
lists anything, the homepage's betting section carries the same warning before its toplist, and
`/licensed-online-casinos/` tracks the casino regime.

**Take New Zealand legal advice on the affiliate model before launch**, particularly on the
sports betting pages. This matters more here than it would on a standalone affiliate domain:
Magnum Sports is a real, named, licensed New Zealand retailer with a physical address, so the
promotion sits against an identifiable local business rather than an anonymous offshore one.
Worth confirming with your adviser how the Arms Act side of the business interacts with
gambling promotion on the same domain, too.

---

Magnum Sports · 220 Broadway, Stratford, Taranaki 4332 · 06 765 7248

Firearms and ammunition are sold in store only, to holders of a valid New Zealand firearms
licence. Gambling content is strictly 18+. Gambling can be harmful — Gambling Helpline
0800 654 655.
