#!/usr/bin/env python3
import os, sys, importlib, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import ROOT, SITE, UPDATED

MODULES = ["p_home", "p_casinos", "p_categories", "p_betting", "p_guides", "p_site", "p_reviews"]

PRIORITY = {"/": "1.0", "/online-casinos/": "1.0", "/online-betting/": "0.9",
            "/online-pokies/": "0.9"}


def main():
    built = []
    for m in MODULES:
        try:
            mod = importlib.import_module(m)
        except ModuleNotFoundError:
            print(f"  (skip {m} — not written yet)")
            continue
        r = mod.build()
        built += r if isinstance(r, list) else [r]
    built = sorted(set(built))

    # sitemap.xml
    urls = []
    for p in built:
        pr = PRIORITY.get(p, "0.8" if p.count("/") <= 2 else "0.7")
        if p in ("/terms/", "/privacy/", "/cookie-policy/"):
            pr = "0.3"
        urls.append(f"  <url>\n    <loc>{SITE}{p}</loc>\n    <lastmod>{UPDATED}</lastmod>\n"
                    f"    <changefreq>{'daily' if pr=='1.0' else 'weekly' if float(pr)>=0.8 else 'monthly'}</changefreq>\n"
                    f"    <priority>{pr}</priority>\n  </url>")
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls) + "\n</urlset>\n")

    # robots.txt
    blocked = ["AhrefsBot", "SemrushBot", "MJ12bot", "DotBot", "Rogerbot", "serpstatbot", "SistrixBot"]
    r = ["# robots.txt — magnumsports.co.nz", "",
         "# SEO crawlers we do not want indexing or profiling this site"]
    for b in blocked:
        r += ["", f"User-agent: {b}", "Disallow: /"]
    r += ["", "# Everyone else", "User-agent: *", "Allow: /",
          "Disallow: /_build/", "Disallow: /go/", "Disallow: /*?",
          "Crawl-delay: 1", "",
          f"Sitemap: {SITE}/sitemap.xml", ""]
    open(os.path.join(ROOT, "robots.txt"), "w").write("\n".join(r))

    print(f"\n✓ {len(built)} pages built")
    print("✓ sitemap.xml, robots.txt")
    return built


if __name__ == "__main__":
    main()
