#!/usr/bin/env python3
"""Measure SERP title width in pixels, not characters.

Google renders desktop result titles in Arial at 20px and truncates on width,
so a 55-character title of capitals can overflow while a 62-character one of
lowercase fits. Widths below are Arial advance widths in 1/1000 em, the values
from the font's own metrics, scaled to 20px.
"""

# Arial advance widths, units per em = 1000
W = {
 " ": 278, "!": 278, '"': 355, "#": 556, "$": 556, "%": 889, "&": 667, "'": 191,
 "(": 333, ")": 333, "*": 389, "+": 584, ",": 278, "-": 333, ".": 278, "/": 278,
 ":": 278, ";": 278, "<": 584, "=": 584, ">": 584, "?": 556, "@": 1015,
 "[": 278, "\\": 278, "]": 278, "^": 469, "_": 556, "`": 333,
 "{": 334, "|": 260, "}": 334, "~": 584,
 "A": 667, "B": 667, "C": 722, "D": 722, "E": 667, "F": 611, "G": 778, "H": 722,
 "I": 278, "J": 500, "K": 667, "L": 556, "M": 833, "N": 722, "O": 778, "P": 667,
 "Q": 778, "R": 722, "S": 667, "T": 611, "U": 722, "V": 667, "W": 944, "X": 667,
 "Y": 667, "Z": 611,
 "a": 556, "b": 556, "c": 500, "d": 556, "e": 556, "f": 278, "g": 556, "h": 556,
 "i": 222, "j": 222, "k": 500, "l": 222, "m": 833, "n": 556, "o": 556, "p": 556,
 "q": 556, "r": 333, "s": 500, "t": 278, "u": 556, "v": 500, "w": 722, "x": 500,
 "y": 500, "z": 500,
 "–": 556, "—": 1000, "’": 191, "‘": 191,
 "“": 333, "”": 333, "ç": 500, "é": 556,
}
DIGIT = 556
FONT_PX = 20
DEFAULT = 556
LIMIT = 580


def px(text, size=FONT_PX):
    """Rendered width of `text` in pixels at Google's desktop title size."""
    total = 0
    for ch in text:
        if ch.isdigit():
            total += DIGIT
        else:
            total += W.get(ch, DEFAULT)
    return round(total / 1000 * size)


def fits(text, limit=LIMIT):
    return px(text) <= limit


def trim_to_px(text, limit=LIMIT):
    """Trim on a word boundary until it fits the pixel budget."""
    if px(text) <= limit:
        return text
    words = text.split()
    while words and px(" ".join(words)) > limit:
        words.pop()
    return " ".join(words)


if __name__ == "__main__":
    # sanity-check against the competitor titles measured live
    for t in [
        "Best Online Casino NZ | Top Real Money Casino Sites in 2026",
        "Best Online Casinos NZ 2026 | Top 20 NZ Casino Sites Reviewed",
        "Best Online Casinos NZ 2026 | Top 10 Real Money Casino Sites",
        "Best Online Casinos in NZ (2026)- Tested with Real Money",
        "Online Casinos New Zealand - Top NZ Casino Sites Of 2026",
    ]:
        flag = "OK " if fits(t) else "OVER"
        print(f"  {flag} {px(t):>4}px  [{len(t):>2} chars]  {t}")
