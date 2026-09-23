#!/usr/bin/env python3
"""Download the product photo for every line on sale (sell = yes) into
images/products/<sku>.webp. Already-downloaded images are skipped, so run it
again after reprice.py switches new lines on.

Each supplier's settings come from suppliers.json: photo_top_band is the share
of the photo's height to trim off the top (Petram's photos carry its logo and a
marketplace badge there; Ultra Safety's are clean), and photo_referer is sent
with the download. The photo is re-centred on white, 600px square. Needs Pillow.
"""
import csv, glob, io, json, os, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(ROOT, "images", "products")
SIZE = 600
SUPPLIERS = json.load(open(os.path.join(HERE, "suppliers.json"), encoding="utf-8"))
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128 Safari/537.36"


def clean(data, band):
    im = Image.open(io.BytesIO(data)).convert("RGB")
    w, h = im.size
    im = im.crop((0, int(h * band), w, h))
    side = max(im.size)
    sq = Image.new("RGB", (side, side), "white")
    sq.paste(im, ((side - im.width) // 2, (side - im.height) // 2))
    return sq.resize((SIZE, SIZE), Image.LANCZOS)


def fetch(row):
    dest = os.path.join(OUT, row["sku"] + ".webp")
    if os.path.exists(dest):
        return "skip"
    for attempt in range(3):
        try:
            info = SUPPLIERS[row["supplier"]]
            req = urllib.request.Request(row["supplier_image"], headers={
                "User-Agent": UA, "Referer": info["photo_referer"]})
            data = urllib.request.urlopen(req, timeout=30).read()
            clean(data, info["photo_top_band"]).save(dest, "WEBP", quality=78, method=6)
            return "ok"
        except Exception as e:
            err = e
            time.sleep(3 * (attempt + 1))
    print("  failed:", row["sku"], err, file=sys.stderr)
    return "fail"


os.makedirs(OUT, exist_ok=True)
rows = []
for path in sorted(glob.glob(os.path.join(HERE, "*.csv"))):
    rows += [r for r in csv.DictReader(open(path, encoding="utf-8-sig"))
             if r.get("sell", "").strip().lower() in ("y", "yes", "1", "true") and r.get("supplier_image")]
with ThreadPoolExecutor(4) as ex:
    res = list(ex.map(fetch, rows))
print({k: res.count(k) for k in set(res)}, f"-> {OUT}")
