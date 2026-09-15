#!/usr/bin/env python3
"""Harvest real user queries from search autosuggest, the AnswerThePublic way.

Seeds x (question prefixes + a-z + prepositions) across Google (gl=nz),
Bing (en-NZ) and DuckDuckGo. Results are what people actually type, not what
we imagine they type. Writes _build/queries.json.
"""
import json, os, re, string, time, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/125.0 Safari/537.36")

QWORDS = ["how", "what", "why", "when", "where", "which", "who", "is", "are",
          "can", "do", "does", "should", "will", "did"]
PREPS = ["for", "with", "without", "vs", "near me", "in nz", "that", "like"]

SEEDS = {
 "/online-casinos/": ["online casino nz", "best online casino nz", "online casino new zealand",
                      "real money casino nz"],
 "/online-pokies/": ["online pokies nz", "pokies nz", "real money pokies nz"],
 "/casino-payout-percentages/": ["highest payout online casino nz", "casino rtp", "best payout casino nz"],
 "/fast-payout-casinos/": ["fast payout casino nz", "casino withdrawal nz", "instant withdrawal casino nz"],
 "/live-casino/": ["live casino nz", "live dealer casino nz"],
 "/crypto-casinos-nz/": ["crypto casino nz", "bitcoin casino nz"],
 "/casino-bonus/": ["casino bonus nz", "wagering requirements", "welcome bonus casino nz"],
 "/no-deposit-bonus/": ["no deposit bonus nz", "free spins no deposit nz"],
 "/online-betting/": ["online betting nz", "betting sites nz", "sports betting nz", "tab nz betting"],
 "/licensed-online-casinos/": ["is online gambling legal in new zealand", "nz online gambling law",
                            "online casino legal nz"],
 "/gambling-winnings-tax-nz/": ["gambling winnings tax nz", "do you pay tax on gambling winnings nz",
                                "casino winnings tax new zealand"],
 "/casino-payment-methods/": ["casino payment methods nz", "poli casino", "casino deposit nz"],
 "/responsible-gambling/": ["gambling help nz", "problem gambling nz", "gambling addiction help"],
 "/casino-reviews/": ["casino review nz", "is online casino legit"],
 "/": ["magnum sports", "outdoors store nz", "hunting and fishing nz", "gun shop taranaki"],
}


def fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA,
                                                   "Accept": "application/json, text/plain, */*"})
        with urllib.request.urlopen(req, timeout=12) as r:
            return r.read().decode("utf-8", "ignore")
    except Exception:
        return ""


def suggestions(q):
    """Union of suggestions from three engines for one query string."""
    e = urllib.parse.quote_plus(q)
    out = []
    g = fetch(f"https://suggestqueries.google.com/complete/search?client=firefox&gl=nz&hl=en&q={e}")
    if g:
        try:
            out += json.loads(g)[1]
        except Exception:
            pass
    b = fetch(f"https://api.bing.com/osjson.aspx?query={e}&market=en-NZ")
    if b:
        try:
            out += json.loads(b)[1]
        except Exception:
            pass
    d = fetch(f"https://duckduckgo.com/ac/?q={e}&kl=nz-en")
    if d:
        try:
            out += [x.get("phrase", "") for x in json.loads(d)]
        except Exception:
            pass
    return out


SPAM = re.compile(r"\.(com|net|info|org|co|xyz|click|site)\b|casinorankboard|truejackpotguide"
                  r"|igamblingstar|brainal|\bgcash\b|\bph\b", re.I)


def harvest_seed(seed):
    queries = [seed]
    queries += [f"{seed} {c}" for c in string.ascii_lowercase]
    queries += [f"{w} {seed}" for w in QWORDS]
    queries += [f"{seed} {p}" for p in PREPS]
    found = set()
    for q in queries:
        for s in suggestions(q):
            s = s.strip().lower()
            if 8 < len(s) < 90 and not SPAM.search(s):
                found.add(s)
        time.sleep(0.05)
    return seed, found


def main():
    result = {}
    allseeds = [(p, s) for p, ss in SEEDS.items() for s in ss]
    print(f"harvesting {len(allseeds)} seeds across 3 engines...")
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(harvest_seed, s): (p, s) for p, s in allseeds}
        for f in futs:
            pass
        for f, (p, s) in futs.items():
            seed, found = f.result()
            result.setdefault(p, set()).update(found)
            print(f"  {s:<42} {len(found):>4} queries")
    out = {p: sorted(v) for p, v in result.items()}
    json.dump(out, open(os.path.join(ROOT, "_build", "queries.json"), "w"),
              ensure_ascii=False, indent=1)
    print(f"\ntotal unique queries: {sum(len(v) for v in out.values())}")
    print("written to _build/queries.json")


if __name__ == "__main__":
    main()
