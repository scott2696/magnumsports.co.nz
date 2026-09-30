"""China sizes -> New Zealand sizes.

NZ reference: Lowes Menswear size chart (lowesmenswear.co.nz/size-chart,
read 30 Sep 2026). Tops (tees, shirts, polos, knitwear and jackets), chest cm:
S 108, M 114, L 120, XL 126, 2XL 132, 3XL 138, 4XL 144. Shoes: EU 37-47 =
NZ/AU/UK 3-13 (EU 35-36 continue the same steps: NZ 1-2).

China jacket chart (from the supplier, garment measurements in cm, +/- 2-4):
the NZ size given is the Lowes size whose chest is closest. The two charts step
differently (4 cm vs 6 cm), so neighbouring China sizes can share an NZ size:
each option also carries the China size and the chest, so the choice is clear.

Only the men's jackets and vests use the jacket chart. T-shirts, shirts,
trousers and women's jackets keep their China sizes until the supplier sends
their own charts: a jacket chart would mislabel them.
"""

LOWES_TOPS = [("S", 108), ("M", 114), ("L", 120), ("XL", 126), ("2XL", 132), ("3XL", 138), ("4XL", 144)]

# China size: chest ("Bra"), coat length, shoulder width, sleeve length, collar, hem
JACKET_CN = {
    "S":   dict(chest=118, length=68, shoulder=47, sleeve=60,   collar=49,   hem=116),
    "M":   dict(chest=122, length=70, shoulder=49, sleeve=61.5, collar=50.5, hem=120),
    "L":   dict(chest=126, length=72, shoulder=51, sleeve=63,   collar=52,   hem=124),
    "XL":  dict(chest=130, length=74, shoulder=53, sleeve=64.5, collar=53.5, hem=128),
    "2XL": dict(chest=134, length=76, shoulder=55, sleeve=66,   collar=55,   hem=132),
    "3XL": dict(chest=138, length=78, shoulder=57, sleeve=67.5, collar=56.5, hem=136),
}
# Not on the supplier's chart: extended one chart step either way (chest 4, length 2,
# shoulder 2, sleeve 1.5 cm), shown with "≈".
JACKET_EST = {"XS": 114, "4XL": 142}
JACKET_EST_ROW = {
    "XS":  dict(chest=114, length=66, shoulder=45, sleeve=58.5),
    "4XL": dict(chest=142, length=80, shoulder=59, sleeve=69),
}
SHOE_US = {35: "2", 36: "3", 37: "4", 38: "5", 39: "6", 40: "7", 41: "8", 42: "9", 43: "10", 44: "11", 45: "12", 46: "13", 47: "14"}
JACKET_GROUPS = {"softshell-jacket", "fleece-jacket", "rain-jacket"}

# Shoes: Lowes EU -> NZ/AU/UK; kids' EU sizes by the usual UK children's conversion.
SHOE_NZ = {35: "1", 36: "2", 37: "3", 38: "4", 39: "5", 40: "6", 41: "7", 42: "8", 43: "9", 44: "10", 45: "11", 46: "12", 47: "13"}
KIDS_NZ = {29: "11", 30: "12", 31: "12.5", 32: "13.5", 33: "1", 34: "2", 35: "2.5", 36: "3.5"}


ORDER = ["XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL"]


def nz_top(chest):
    return min(LOWES_TOPS, key=lambda s: (abs(s[1] - chest), s[1]))[0]


def uses_jacket_chart(p):
    return p.get("group") in JACKET_GROUPS and not p["name"].startswith("Women's")


def label(p, size):
    """The NZ size shown to the customer. Customers never see the China size;
    china_for() gives it back for ordering from the supplier.

    Jackets: measured against the Lowes chart these come up one size large, so each
    China size is sold as the next NZ size up (China S = NZ M ... China 3XL = NZ 4XL),
    a one-to-one match within about 6 cm of chest. Boots: EU -> NZ/AU/UK."""
    if size.startswith("EU "):
        eu = int(size[3:])
        if "Kids" in p["name"]:
            return f"Kids {KIDS_NZ[eu]}" if eu in KIDS_NZ else size
        return SHOE_NZ.get(eu, size)
    if uses_jacket_chart(p) and size in ORDER[:-1]:
        return ORDER[ORDER.index(size) + 1]
    return size          # no NZ chart for this line yet: the supplier's size letters


def china_for(p, nz):
    """The supplier size behind an NZ label (for the order emails and Stripe)."""
    for cn, lab in zip(p.get("options_cn") or [], p.get("options") or []):
        if lab == nz:
            return cn
    return ""


def jacket_chest(size):
    return JACKET_CN[size]["chest"] if size in JACKET_CN else JACKET_EST.get(size)


def note(p):
    """Short sizing line for the product page."""
    if not p.get("options"):
        return ""
    if (p.get("options_cn") or p["options"])[0].startswith("EU "):
        return "Sizes are NZ/AU/UK shoe sizes. If you are between sizes, go up one."
    if uses_jacket_chart(p):
        return ("Sizes are NZ sizes. Check the chest measurement in the size guide against a jacket that fits you: "
                "lay it flat, measure across the chest under the arms and double it.")
    return ("Not sure which size? Ask us on live chat and we will send you the garment measurements before "
            "you order.")


def _jacket_rows(p):
    rows = []
    for c in p.get("options_cn") or []:
        if c in JACKET_CN:
            m, est = JACKET_CN[c], False
        elif c in JACKET_EST_ROW:
            m, est = JACKET_EST_ROW[c], True
        else:
            continue
        a = "≈" if est else ""
        rows.append((label(p, c), f"{a}{m['chest']}", f"{a}{m['length']}", f"{a}{m['shoulder']}", f"{a}{m['sleeve']}"))
    return rows


def _table(head, rows):
    h = "".join(f"<th scope='col'>{x}</th>" for x in head)
    b = "".join("<tr><th scope='row'>" + r[0] + "</th>" + "".join(f"<td>{x}</td>" for x in r[1:]) + "</tr>" for r in rows)
    return f"<div class='tw'><table class='specs'><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>"


def table_html(p, esc):
    """Size guide on the product page (jackets)."""
    rows = _jacket_rows(p) if uses_jacket_chart(p) else []
    if not rows:
        return ""
    return ("<h3 id='size-guide'>Size guide (cm, garment measurements)</h3>"
            + _table(("Size", "Chest", "Length", "Shoulder", "Sleeve"), rows)
            + "<p class='pdp-fine'>Measured flat and doubled; allow 2 to 4 cm either way. &asymp; = estimated "
              "from the neighbouring size.</p>")


def dialog_html(p, esc):
    """'Measurements' pop-up next to the size menu: every size this product comes in."""
    if not p.get("options"):
        return ""
    did = f"sg-{p['sku']}"
    cn = p.get("options_cn") or p["options"]
    if cn and cn[0].startswith("EU "):
        rows = []
        for c in cn:
            eu = int(c[3:])
            if "Kids" in p["name"]:
                rows.append((label(p, c), str(eu), "&ndash;"))
            else:
                rows.append((label(p, c), str(eu), SHOE_US.get(eu, "&ndash;")))
        body = (_table(("NZ / AU / UK", "EU", "US"), rows)
                + "<p class='pdp-fine'>If you are between sizes, go up one. Measure your foot from heel to longest toe "
                  "standing, and compare with a shoe that fits well.</p>")
    elif uses_jacket_chart(p) and _jacket_rows(p):
        body = (_table(("Size", "Chest", "Length", "Shoulder", "Sleeve"), _jacket_rows(p))
                + "<p class='pdp-fine'>Garment measurements in cm, measured flat and doubled; allow 2 to 4 cm. "
                  "&asymp; = estimated. How to check: lay a jacket that fits you flat, measure across the chest just "
                  "under the arms and double it, then pick the size with the nearest chest.</p>")
    else:
        body = ("<p>Sizes available: <strong>" + ", ".join(esc(o) for o in p["options"]) + "</strong>.</p>"
                "<p class='pdp-fine'>We don't have a measurement chart for this line yet. Ask us on live chat or "
                "the <a href='/contact/'>contact form</a> and we will send you the chest, waist and length for each "
                "size before you order.</p>")
    return (f"<dialog class='size-dialog' id='{did}' aria-labelledby='{did}-h'>"
            f"<div class='size-dialog-head'><h2 id='{did}-h'>Measurements: {esc(p['name'].split(' — ')[0])}</h2>"
            "<button type='button' class='size-dialog-x' data-close aria-label='Close'>&times;</button></div>"
            f"{body}</dialog>")
