#!/usr/bin/env python3
import os, sys, importlib, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import ROOT, SITE, LASTMOD, save_manifest

MODULES = ["p_home", "p_casinos", "p_categories", "p_betting", "p_guides", "p_new",
           "p_site", "p_reviews"]


# Paths that exist only to redirect. Kept OUT of the sitemap deliberately.
#
# GitHub Pages serves static files and cannot issue a real 301 — there is no
# server config to write one into. What is generated below is the strongest
# signal available to a static host: a zero-delay meta refresh plus a
# rel=canonical pointing at the destination, which Google treats as a
# permanent redirect in practice. It is NOT an HTTP 301.
#
# To make it a true 301, the redirect must be issued at the edge:
#   Cloudflare  ->  Rules > Redirect Rules, /instant-withdrawals/* -> target, 301
#   Netlify     ->  a _redirects file:  /instant-withdrawals/ /fast-payout-casinos/ 301!
#   Apache      ->  RedirectMatch 301 ^/instant-withdrawals/?$ /fast-payout-casinos/
#   Nginx       ->  return 301 /fast-payout-casinos/;
REDIRECTS = {
    "/instant-withdrawals/": "/fast-payout-casinos/",
}


def write_redirects():
    for src, dest in REDIRECTS.items():
        url = SITE + dest
        html = f"""<!DOCTYPE html>
<html lang="en-NZ">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url={dest}">
<link rel="canonical" href="{url}">
<title>Redirecting to Fast Payout Casinos NZ</title>
<meta name="robots" content="noarchive">
<script>window.location.replace("{dest}");</script>
</head>
<body>
<p>This page has moved to <a href="{dest}">{url}</a>.</p>
</body>
</html>
"""
        d = os.path.join(ROOT, src.strip("/"))
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html)
    return list(REDIRECTS)


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
    redirects = write_redirects()

    # sitemap.xml
    # loc + lastmod only.
    #
    # Google has stated it ignores <changefreq> and <priority> outright, and
    # the values we were emitting were false anyway: "daily" on a store
    # homepage that changes a few times a year, "monthly" on terms that have
    # not moved since launch. A contradicted signal is worse than an absent
    # one, and lastmod is the field that still does something -- which is why
    # it is now derived from a content hash rather than the build clock.
    urls = []
    for p in built:
        urls.append(f"  <url>\n    <loc>{SITE}{p}</loc>\n"
                    f"    <lastmod>{LASTMOD.get(p, UPDATED_FALLBACK)}</lastmod>\n  </url>")
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
          "Disallow: /_fold.html",
          "Crawl-delay: 1", "",
          f"Sitemap: {SITE}/sitemap.xml", ""]
    open(os.path.join(ROOT, "robots.txt"), "w").write("\n".join(r))

    save_manifest()
    from collections import Counter
    spread = Counter(LASTMOD.get(p) for p in built)
    print("\n✓ lastmod: " + ", ".join(f"{d} ({n})" for d, n in sorted(spread.items())))
    print(f"✓ {len(built)} pages built")
    print(f"✓ {len(redirects)} redirect stub(s): {', '.join(redirects)} (meta-refresh + canonical, NOT a 301 — see REDIRECTS in build.py)")
    print("✓ sitemap.xml, robots.txt")
    try:
        import check_keywords
        check_keywords.main()
    except Exception as e:
        print(f"  (keyword check skipped: {e})")
    return built


if __name__ == "__main__":
    main()
