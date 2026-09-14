# magnumsports.co.nz

Independent New Zealand comparison site for online casinos, online pokies and sports betting.
Static HTML, generated from Python. No framework, no build dependencies beyond the standard
library (plus Pillow for the one-off image generation scripts).

**Primary target:** `best online casino sites NZ`
**Secondary target:** `online betting NZ`

---

## What's here

42 pages, ~76,000 words of original content.

| Tier | Pages |
|---|---|
| Money pages | `/`, `/online-betting/` |
| Casino hub | `/online-casinos/` |
| Categories | `/online-pokies/`, `/high-payout-casinos/`, `/fast-payout-casinos/`, `/live-casinos/`, `/best-crypto-casinos/`, `/online-casinos/bonuses/`, `/no-deposit-casinos/` |
| Betting | `/best-sports-betting-sites/` |
| Reviews | `/casino-reviews/` + 19 operator reviews |
| Guides | `/nz-online-casino-law/`, `/gambling-winnings-tax-nz/`, `/payment-methods/`, `/how-we-review/` |
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

Regenerates all 42 pages plus `sitemap.xml` and `robots.txt` in about a second.
Output is written in place — this repo *is* the deployed site (GitHub Pages, see `CNAME`).

### Where things live

| File | Controls |
|---|---|
| `_build/lib.py` | Site constants, **all page titles and descriptions** (`META`), nav and footer structure, authors, schema builders, shared components (leaderboard, tables, FAQ, cards, pros/cons) |
| `_build/operators.json` | All 19 operators: links, bonuses, wagering, payout times, licensing, payments, pros/cons, verdicts, ranking |
| `_build/p_home.py` | Homepage |
| `_build/p_casinos.py` | `/online-casinos/` |
| `_build/p_categories.py` | The 7 category pages |
| `_build/p_betting.py` | `/online-betting/`, `/best-sports-betting-sites/` |
| `_build/p_guides.py` | Law, tax, payments, methodology |
| `_build/p_site.py` | About, contact, authors, responsible gambling, terms, privacy, cookies |
| `_build/p_reviews.py` | Review hub + 19 reviews (`NARR` holds the bespoke per-brand copy) |
| `_build/build.py` | Orchestrator, sitemap, robots |
| `assets/css/site.css` | The entire stylesheet (22 KB, no JS) |

### One-off asset scripts

```bash
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
- **Add a nav or footer link:** `NAV` / `FOOTER` in `_build/lib.py`.
- **Add a page:** write a `build()` function in a new `_build/p_*.py`, add the module name to
  `MODULES` in `_build/build.py`. It is picked up by the sitemap automatically.

---

## Conventions

- **Clean URLs.** Every page is `<path>/index.html`; nothing links to a `.html` extension.
- **Self-referencing canonicals** on all 42 URLs.
- **`en-NZ`** throughout, with `hreflang="en-nz"` and `x-default`.
- **Affiliate links** always carry `rel="nofollow sponsored noopener" target="_blank"`.
- **One page, one head keyword.** See the mapping table in `docs/KEYWORD-STRATEGY.md`.
- **Every page** has a named author, a named fact-checker (never the same person), a
  last-updated date, an advertising disclosure and responsible gambling messaging.

---

## Before this goes live

Two things need a human pass:

1. **Operator data.** Bonus amounts, wagering multipliers, minimum deposits, payout times,
   licence details, game counts, withdrawal caps and the testing statistics in
   `_build/operators.json` and throughout the copy are working figures assembled during the
   build. **Verify every one against the operator's current terms and your own testing
   records before publishing**, and update `UPDATED` when you do. The figures are internally
   consistent and plausible, but they are not yet your data.

2. **Author photographs.** `images/authors/*.jpg` are generated monogram avatars. Replace them
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
lists anything, and `/nz-online-casino-law/` tracks the casino regime. **Take New Zealand legal
advice on the affiliate model itself before launch**, particularly on the sports betting pages.

---

18+ only. Gambling can be harmful. Gambling Helpline: 0800 654 655.
