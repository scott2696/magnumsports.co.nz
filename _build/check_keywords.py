#!/usr/bin/env python3
"""Build-time guard: every Tier 1 term must appear on its page, and no short
phrase may exceed 2.5% of a page (the keyword-stuffing tripwire)."""
import html, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TIER1 = {
 "/online-casinos/": ["online casinos nz", "best online casino nz", "online casino new zealand",
   "nz online casinos", "online casino real money nz", "best online casinos nz 2026",
   "top online casinos nz", "real money casino nz", "nz casino sites", "casino online nz"],
 "/licensed-online-casinos/": ["licensed online casinos nz", "legal online casinos nz",
   "is online gambling legal in nz", "are online casinos legal in new zealand",
   "online gambling laws new zealand"],
 "/casino-bonus/": ["casino bonus nz", "best casino bonuses nz", "casino sign up bonus nz",
   "$1 deposit casino nz"],
 "/no-deposit-bonus/": ["no deposit bonus nz", "free spins no deposit nz",
   "no deposit bonus codes nz", "no deposit casino nz"],
 "/casino-payout-percentages/": ["casino payout percentage", "best payout online casino nz",
   "highest rtp casinos nz", "what is rtp in pokies"],
 "/fast-payout-casinos/": ["fast payout casinos nz", "instant withdrawal casino nz",
   "fastest paying online casino nz", "how long do casino withdrawals take"],
 "/casino-payment-methods/": ["casino payment methods nz", "paysafecard", "poli", "paypal",
   "neosurf", "skrill"],
 "/online-pokies/": ["online pokies nz", "online pokies real money", "best online pokies nz",
   "free pokies", "real money pokies nz"],
 "/live-casino/": ["live casino nz", "live dealer casino nz", "best live casino nz",
   "live roulette", "live blackjack"],
 "/crypto-casinos-nz/": ["crypto casino nz", "bitcoin casino nz", "crypto casinos new zealand",
   "best crypto casino nz", "bitcoin gambling"],
 "/new-casinos-nz/": ["new online casinos nz", "new casinos nz", "newest online casinos nz",
   "new casino sites nz"],
}
WATCH = ["online casino", "online pokies", "casino bonus", "no deposit", "crypto casino",
         "live casino", "fast payout", "payment methods"]
LIMIT = 2.5  # % of page words; "no deposit" on its own page is the known exception


def main():
    missing, dense = [], []
    for path, terms in TIER1.items():
        f = os.path.join(ROOT, path.strip("/"), "index.html")
        raw = open(f, encoding="utf-8").read()
        body = re.sub(r"(?s)<(script|style|header|footer|nav).*?</\1>", "", raw)
        text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", body))).lower()
        words = max(len(text.split()), 1)
        for t in terms:
            if t not in text:
                missing.append(f"{path}: Tier 1 term absent — '{t}'")
        for kw in WATCH:
            pct = text.count(kw) * len(kw.split()) / words * 100
            if pct > LIMIT and not (path == "/no-deposit-bonus/" and kw == "no deposit"):
                dense.append(f"{path}: '{kw}' at {pct:.1f}% of page (limit {LIMIT}%)")
    for m in missing:
        print("  ✗", m)
    for d in dense:
        print("  ! ", d)
    print(f"keyword check: {len(missing)} missing, {len(dense)} density warnings")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
