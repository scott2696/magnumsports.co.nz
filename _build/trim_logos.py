#!/usr/bin/env python3
"""Crop near-white / transparent borders from raster brand logos so they fill
the 88x46 toplist tile instead of being letterboxed by object-fit:contain."""
import os, glob
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGOS = os.path.join(ROOT, "logos")


def content_bbox(im, thresh=244):
    """Bounding box of pixels that are neither transparent nor near-white."""
    im = im.convert("RGBA")
    w, h = im.size
    px = im.load()
    x0, y0, x1, y1 = w, h, -1, -1
    step = max(1, min(w, h) // 400)
    for y in range(0, h, step):
        for x in range(0, w, step):
            r, g, b, a = px[x, y]
            if a < 24:
                continue
            if r > thresh and g > thresh and b > thresh:
                continue
            if x < x0: x0 = x
            if y < y0: y0 = y
            if x > x1: x1 = x
            if y > y1: y1 = y
    if x1 < 0:
        return None
    return (x0, y0, x1 + 1, y1 + 1)


def main():
    for f in sorted(glob.glob(os.path.join(LOGOS, "*.png")) + glob.glob(os.path.join(LOGOS, "*.jpg"))):
        im = Image.open(f)
        bb = content_bbox(im)
        if not bb:
            print(f"  skip {os.path.basename(f)} (no content found)")
            continue
        w, h = im.size
        cw, ch = bb[2] - bb[0], bb[3] - bb[1]
        if cw > w * 0.94 and ch > h * 0.94:
            print(f"  ok   {os.path.basename(f)} (already tight)")
            continue
        pad = int(max(cw, ch) * 0.03)
        box = (max(0, bb[0] - pad), max(0, bb[1] - pad),
               min(w, bb[2] + pad), min(h, bb[3] + pad))
        out = im.convert("RGBA").crop(box)
        # cap the long edge so files stay small; the tile is 88x46 @2x = 176x92
        out.thumbnail((440, 440), Image.LANCZOS)
        dest = os.path.splitext(f)[0] + ".png"
        out.save(dest)
        if dest != f:
            os.remove(f)
        print(f"  trim {os.path.basename(f)} {w}x{h} -> {out.size[0]}x{out.size[1]}  ({dest.split('/')[-1]})")


if __name__ == "__main__":
    main()
