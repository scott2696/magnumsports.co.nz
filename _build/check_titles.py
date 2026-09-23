#!/usr/bin/env python3
"""Build-time guard: no page title wider than Google renders before truncating
(measured in pixels, see pixels.py)."""
import glob, html, os, re, sys
from pixels import px, LIMIT as TITLE_PX

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def all_titles():
    """Every page title with its rendered pixel width."""
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, "**", "index.html"), recursive=True)):
        s = open(f, encoding="utf-8").read()
        m = re.search(r"<title>(.*?)</title>", s, re.S)
        if m:
            t = html.unescape(m.group(1)).strip()
            u = "/" + os.path.relpath(os.path.dirname(f), ROOT).replace(os.sep, "/") + "/"
            out.append((u.replace("/./", "/"), t, px(t)))
    return out


def main():
    titles = all_titles()
    over = [(u, t, w) for u, t, w in titles if w > TITLE_PX]
    for u, t, w in over:
        print(f"  ✗ {u}: title {w}px > {TITLE_PX}px — {t}")
    widest = max((w for _, _, w in titles), default=0)
    print(f"title width check: {len(over)} over {TITLE_PX}px, widest is {widest}px")
    return 1 if over else 0


if __name__ == "__main__":
    sys.exit(main())
