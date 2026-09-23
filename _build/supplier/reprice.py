#!/usr/bin/env python3
"""Choose and price the supplier lines that go live, for every supplier in
suppliers.json (each has its own sheet, e.g. petram.csv, ultra-safety.csv).

A row is sold when:
  - it has no flag other than "Department is a guess" (so no other brand's
    name, no legal or safety concern, nothing the owner has ruled out);
  - its origin says China;
  - it has a supplier price in supplier_fob_usd (Ultra Safety does not publish
    prices: its rows stay off until quoted prices are entered);
  - its department is sold online, and its SKU is not in exclude.txt.
Every other row is switched off.

    retail_nzd = top of the supplier's USD price (range) x MARKUP x USD->NZD

    python3 _build/supplier/reprice.py            # fetches today's rate
    python3 _build/supplier/reprice.py 1.7467     # or pass one
then rebuild with python3 _build/build.py.
"""
import csv, json, os, re, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
SUPPLIERS = json.load(open(os.path.join(HERE, "suppliers.json"), encoding="utf-8"))
MARKUP = 5
HARMLESS = {"", "Department is a guess - check"}
# The shop is online only; nothing in these departments is sold.
OFFLINE = {"Firearms and Accessories", "Ammunition", "Reloading", "Airguns"}

# SKUs kept off sale for good, whatever the sheet says (see the reasons there).
EXCLUDE = set()
_ex = os.path.join(HERE, "exclude.txt")
if os.path.exists(_ex):
    EXCLUDE = {l.split("#")[0].strip() for l in open(_ex)} - {""}

CODES = {"BLK": "Black", "BK": "Black", "TAN": "Tan", "GRY": "Grey", "GY": "Grey", "BLU": "Blue",
         "RED": "Red", "WHT": "White", "GRN": "Green", "GR": "Green", "OD": "OD Green",
         "ODG": "OD Green", "NVB": "Navy", "NVY": "Navy", "FDE": "Flat Dark Earth", "DE": "Dark Earth",
         "SND": "Sand", "CB": "Coyote Brown", "CYT": "Coyote", "RGG": "Ranger Green",
         "MTC": "Multicam", "MC": "Multicam", "CAM": "Camo", "WG": "Wolf Grey", "ORG": "Orange"}


def usd_nzd():
    if len(sys.argv) > 1:
        return float(sys.argv[1]), "given"
    d = json.load(urllib.request.urlopen("https://open.er-api.com/v6/latest/USD", timeout=20))
    return float(d["rates"]["NZD"]), d.get("time_last_update_utc", "")


def variant(r, group, prefix):
    """What tells this row apart from the others with the same name."""
    code = r["model"].rsplit("-", 1)[-1].upper() if "-" in r["model"] else ""
    colour = re.search(r"color: ([^|]+)", r["key_specs"], re.I)
    colours = {(re.search(r"color: ([^|]+)", g["key_specs"], re.I) or [None, ""])[1] for g in group}
    if colour and len(colours) == len(group):
        return colour.group(1).strip()
    if code in CODES:
        return CODES[code]
    return r["model"] or r["sku"].replace(prefix, "")


def reprice(info, rate):
    sheet = os.path.join(HERE, info["sheet"])
    rows = list(csv.DictReader(open(sheet, encoding="utf-8-sig")))
    fields = list(rows[0])
    live = []
    for r in rows:
        fob = [float(x) for x in re.findall(r"[\d.]+", r.get("supplier_fob_usd", ""))]
        ok = (r["flags"].strip() in HARMLESS and "china" in r["origin"].lower() and fob
              and r["sku"] not in EXCLUDE and r["dept"] not in OFFLINE)
        r["sell"] = "yes" if ok else ""
        r["retail_nzd"] = f"{max(fob) * MARKUP * rate:.2f}" if ok else ""
        if ok:
            live.append(r)
    # Same name twice (usually colourways) -> add the colour so the cards differ.
    names = {}
    for r in live:
        names.setdefault(r["name"], []).append(r)
    for name, group in names.items():
        if len(group) < 2:
            continue
        for r in group:
            v = variant(r, group, info["sku_prefix"])
            if not name.endswith(f" — {v}"):          # safe to run more than once
                r["name"] = f"{name} — {v}"
    # Anything still doubled is the same item listed twice: tell them apart by model.
    seen = {}
    for r in live:
        seen.setdefault(r["name"], []).append(r)
    for group in seen.values():
        for r in group[1:] if len(group) > 1 else []:
            r["name"] = f'{r["name"]} ({r["model"] or r["sku"].replace(info["sku_prefix"], "")})'
    with open(sheet, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    waiting = sum(1 for r in rows if r["flags"].strip() in HARMLESS and r["sku"] not in EXCLUDE
                  and r["dept"] not in OFFLINE and not r.get("supplier_fob_usd", "").strip())
    note = f"; {waiting} eligible but awaiting a supplier price" if waiting else ""
    print(f"  {info['name']}: {len(live)} of {len(rows)} lines set to sell{note}")


if __name__ == "__main__":
    rate, when = usd_nzd()
    print(f"USD->NZD {rate} ({when}); x{MARKUP} on the top of each supplier price")
    for info in SUPPLIERS.values():
        reprice(info, rate)
