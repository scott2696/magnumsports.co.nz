#!/usr/bin/env python3
import os, sys, importlib, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import ROOT, SITE, LASTMOD, save_manifest

MODULES = ["p_home", "p_shop", "p_site"]


UPDATED_FALLBACK = __import__("datetime").date.today().isoformat()


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
    # loc + lastmod only.
    #
    # Google has stated it ignores <changefreq> and <priority> outright, and
    # the values we were emitting were false anyway: "daily" on a store
    # homepage that changes a few times a year, "monthly" on terms that have
    # not moved since launch. A contradicted signal is worse than an absent
    # one, and lastmod is the field that still does something -- which is why
    # it is now derived from a content hash rather than the build clock.
    # Each product page also lists its photo (Google image sitemap extension).
    from lib import PRODUCTS, product_url, product_image
    photo = {product_url(p): product_image(p["sku"]) for p in PRODUCTS}
    urls = []
    for p in built:
        img = photo.get(p)
        img_xml = (f"\n    <image:image>\n      <image:loc>{SITE}{img}</image:loc>\n    </image:image>"
                   if img else "")
        urls.append(f"  <url>\n    <loc>{SITE}{p}</loc>\n"
                    f"    <lastmod>{LASTMOD.get(p, UPDATED_FALLBACK)}</lastmod>{img_xml}\n  </url>")
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
        + "\n".join(urls) + "\n</urlset>\n")

    # robots.txt
    blocked = ["AhrefsBot", "SemrushBot", "MJ12bot", "DotBot", "Rogerbot", "serpstatbot", "SistrixBot"]
    r = ["# robots.txt — magnumsports.co.nz", "",
         "# SEO crawlers we do not want indexing or profiling this site"]
    for b in blocked:
        r += ["", f"User-agent: {b}", "Disallow: /"]
    r += ["", "# Everyone else", "User-agent: *", "Allow: /",
          "Disallow: /_build/", "Disallow: /*?",
          "Crawl-delay: 1", "",
          f"Sitemap: {SITE}/sitemap.xml", ""]
    open(os.path.join(ROOT, "robots.txt"), "w").write("\n".join(r))

    save_manifest()
    from collections import Counter
    spread = Counter(LASTMOD.get(p) for p in built)
    print("\n✓ lastmod: " + ", ".join(f"{d} ({n})" for d, n in sorted(spread.items())))
    print(f"✓ {len(built)} pages built")
    print("✓ sitemap.xml, robots.txt")
    try:
        import check_titles
        check_titles.main()
    except Exception as e:
        print(f"  (title check skipped: {e})")
    return built


if __name__ == "__main__":
    main()
