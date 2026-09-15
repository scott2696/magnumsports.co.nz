#!/usr/bin/env python3
"""Generate favicons, author avatars and the OG card for magnumsports.co.nz."""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INK = (43, 40, 54, 255)      # graphite #2B2836
RED = (245, 165, 36, 255)    # sodium   #F5A524
AMBER = (242, 239, 233, 255) # chalk    #F2EFE9
WHITE = (255, 255, 255, 255)

FONTS = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    "/System/Library/Fonts/SFNSDisplay.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
]


def font(size):
    for p in FONTS:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()


def rounded(size, radius_ratio=0.22, fill=INK):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=int(size * radius_ratio), fill=fill)
    return im


def mark(size):
    """Graphite tile, sodium M, chalk underscore — one accent, per the system."""
    S = size * 8  # supersample
    im = rounded(S, fill=INK)
    d = ImageDraw.Draw(im)
    w = int(S * 0.115)
    pts = [(0.205, 0.735), (0.205, 0.265), (0.5, 0.585), (0.795, 0.265), (0.795, 0.735)]
    px = [(int(x * S), int(y * S)) for x, y in pts]
    d.line(px, fill=RED, width=w, joint="curve")
    for p in px:
        d.ellipse([p[0] - w // 2, p[1] - w // 2, p[0] + w // 2, p[1] + w // 2], fill=RED)
    # amber baseline accent
    d.rounded_rectangle(
        [int(0.205 * S), int(0.795 * S), int(0.795 * S), int(0.795 * S) + int(S * 0.055)],
        radius=int(S * 0.028), fill=AMBER)
    return im.resize((size, size), Image.LANCZOS)


def write_favicons():
    for s in (16, 32, 48, 96, 144, 192, 512):
        mark(s).save(os.path.join(ROOT, f"favicon-{s}x{s}.png"))
    mark(180).save(os.path.join(ROOT, "apple-touch-icon.png"))
    ico = mark(64)
    ico.save(os.path.join(ROOT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="Magnum Sports">
<rect width="100" height="100" rx="22" fill="#2B2836"/>
<path d="M20.5 73.5V26.5L50 58.5L79.5 26.5V73.5" fill="none" stroke="#F5A524" stroke-width="11.5" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="20.5" y="79.5" width="59" height="5.5" rx="2.75" fill="#F2EFE9"/>
</svg>"""
    open(os.path.join(ROOT, "favicon.svg"), "w").write(svg)


def wordmark(path, text, accent, sub=""):
    """House-style SVG wordmark used where no vendor artwork exists."""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 90" role="img" aria-label="{text}">
<style>.w{{font:700 40px 'Archivo','Helvetica Neue',Helvetica,Arial,sans-serif;fill:#101828}}
.a{{font:700 40px 'Archivo','Helvetica Neue',Helvetica,Arial,sans-serif;fill:{accent}}}
.s{{font:500 12px 'Helvetica Neue',Helvetica,Arial,sans-serif;fill:#6b7688;letter-spacing:3.2px}}</style>
<text x="10" y="50" class="w">{text.split(" ")[0]}<tspan class="a">{(" " + " ".join(text.split(" ")[1:])) if len(text.split(" ")) > 1 else ""}</tspan></text>
<text x="12" y="72" class="s">{sub}</text>
</svg>'''
    open(path, "w").write(svg)


def avatar(path, initials, c1, c2, size=168):
    S = size * 4
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for y in range(S):
        t = y / S
        d.line([(0, y), (S, y)], fill=(int(c1[0] + (c2[0] - c1[0]) * t),
                                       int(c1[1] + (c2[1] - c1[1]) * t),
                                       int(c1[2] + (c2[2] - c1[2]) * t), 255))
    mask = Image.new("L", (S, S), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, S - 1, S - 1], fill=255)
    im.putalpha(mask)
    f = font(int(S * 0.38))
    d = ImageDraw.Draw(im)
    bb = d.textbbox((0, 0), initials, font=f)
    d.text(((S - bb[2] + bb[0]) / 2 - bb[0], (S - bb[3] + bb[1]) / 2 - bb[1] - S * 0.02),
           initials, font=f, fill=WHITE)
    im.resize((size, size), Image.LANCZOS).convert("RGB").save(path, quality=92)
    im.resize((size * 2, size * 2), Image.LANCZOS).convert("RGB").save(
        path.replace(".jpg", "@2x.jpg"), quality=90)


def og_card():
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), (10, 16, 32))
    d = ImageDraw.Draw(im)
    for y in range(H):
        t = y / H
        d.line([(0, y), (W, y)], fill=(int(10 + 12 * t), int(16 + 19 * t), int(32 + 42 * t)))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    for r in range(320, 0, -4):
        a = int(46 * (1 - r / 320))
        gd.ellipse([1010 - r, 90 - r, 1010 + r, 90 + r], fill=(225, 29, 46, a))
    im = Image.alpha_composite(im.convert("RGBA"), glow).convert("RGB")
    d = ImageDraw.Draw(im)
    im.paste(mark(96).convert("RGB"), (80, 76))
    d.text((196, 88), "MAGNUM", font=font(40), fill=(255, 255, 255))
    d.text((196, 134), "NZ CASINO & BETTING GUIDE", font=font(17), fill=(141, 154, 181))
    d.text((80, 236), "Best Online Casino", font=font(78), fill=(255, 255, 255))
    d.text((80, 322), "Sites NZ 2026", font=font(78), fill=(225, 29, 46))
    d.text((80, 438), "Independently tested. Real NZD deposits.", font=font(30), fill=(200, 210, 228))
    d.text((80, 480), "Withdrawal times timed by us.", font=font(30), fill=(200, 210, 228))
    d.rounded_rectangle([80, 546, 292, 592], radius=10, fill=(255, 183, 3))
    d.text((100, 559), "18+  ·  T&Cs APPLY", font=font(19), fill=(10, 16, 32))
    im.save(os.path.join(ROOT, "images", "og-magnum.jpg"), quality=88)


if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "images", "authors"), exist_ok=True)
    write_favicons()
    wordmark(os.path.join(ROOT, "logos", "crownslots.svg"), "Crown Slots", "#c9a227", "CASINO")
    wordmark(os.path.join(ROOT, "logos", "gunsbet.svg"), "Guns Bet", "#e11d2e", "SPORTSBOOK")
    # Author headshots are supplied, not generated:
    #   headshot("<source>.png", "images/authors/angus-mclean.jpg")
    #   headshot("<source>.png", "images/authors/witi-king.jpg")
    og_card()
    print("images generated")


def headshot(src, dest, focus_y=0.42):
    """Square-crop a supplied headshot around the face and write 1x + 2x.

    Bylines and author boxes render the image as a circle, so the crop is
    centred horizontally and biased upward (faces sit above centre in most
    portraits) to keep the head inside the circle rather than the chin.
    """
    im = Image.open(src).convert("RGB")
    w, h = im.size
    side = min(w, h)
    left = (w - side) // 2
    top = int(max(0, min(h - side, focus_y * h - side / 2)))
    sq = im.crop((left, top, left + side, top + side))
    sq.resize((168, 168), Image.LANCZOS).save(dest, quality=92)
    sq.resize((336, 336), Image.LANCZOS).save(dest.replace(".jpg", "@2x.jpg"), quality=90)
    print(f"  {os.path.basename(src)} {w}x{h} -> {os.path.basename(dest)} (168 + 336)")
