#!/usr/bin/env python3
"""Generate the favicons and the social sharing card for magnumsports.co.nz."""
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


def og_card():
    """1200x630 sharing card: the store, not any one page."""
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), (12, 11, 16))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    for r in range(340, 0, -4):
        a = int(40 * (1 - r / 340))
        gd.ellipse([1000 - r, 110 - r, 1000 + r, 110 + r], fill=(245, 165, 36, a))
    im = Image.alpha_composite(im.convert("RGBA"), glow).convert("RGB")
    d = ImageDraw.Draw(im)
    im.paste(mark(96).convert("RGB"), (80, 76))
    d.text((196, 88), "MAGNUM", font=font(40), fill=(242, 239, 233))
    d.text((196, 134), "OUTDOOR GEAR ONLINE", font=font(17), fill=(157, 152, 168))
    d.text((80, 236), "Outdoor Gear,", font=font(78), fill=(242, 239, 233))
    d.text((80, 322), "Delivered NZ-Wide", font=font(78), fill=(245, 165, 36))
    d.text((80, 438), "Gloves, clothing, pouches, packs and bipods.", font=font(30), fill=(200, 196, 208))
    d.text((80, 480), "Order online, delivered in 7 to 10 days.", font=font(30), fill=(200, 196, 208))
    d.rounded_rectangle([80, 546, 300, 592], radius=10, fill=(245, 165, 36))
    d.text((100, 559), "06 765 7248", font=font(21), fill=(26, 18, 4))
    im.save(os.path.join(ROOT, "images", "og-magnum.jpg"), quality=88)


if __name__ == "__main__":
    write_favicons()
    og_card()
    print("images generated")
