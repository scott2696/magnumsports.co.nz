#!/usr/bin/env python3
"""Turn a "Quote request" email into a Stripe invoice, with delivery added.

    1. Copy the whole quote request email (Cmd+A, Cmd+C in the email).
    2. python3 _build/tools/invoice.py 25            preview: delivery NZ$25
    3. python3 _build/tools/invoice.py 25 --send     create it and email it

Stripe emails the customer an invoice from "Magnum Sports" with a Pay button
(card, Apple Pay, Google Pay, PayPal ...). You get Stripe's usual email when
it is paid. Options:
    --days 3        days until the invoice is due (default 3)
    --file q.txt    read the email from a file instead of the clipboard

Prices are taken from the live catalogue by SKU, not from the email text, so
an edited request cannot change what the customer is charged.

The Stripe key is read from the macOS Keychain (service
"magnumsports-stripe-invoices"). Store it once, after copying the key:
    security add-generic-password -U -s magnumsports-stripe-invoices -a stripe -w "$(pbpaste)"
It needs a restricted key with Customers: Write and Invoices: Write.
"""
import argparse
import json
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

CATALOGUE = "https://magnumsports.co.nz/assets/js/search.json"
SITE = "https://magnumsports.co.nz"
KEYCHAIN = "magnumsports-stripe-invoices"


def die(msg):
    print(f"\n  ✗ {msg}\n")
    sys.exit(1)


# ------------------------------------------------------------ the email
def parse(text):
    """Customer and items from the Worker's quote request email."""
    field = lambda k: (re.search(rf"^\s*{k}:\s*(.+)$", text, re.M) or [None, ""])[1].strip()
    items = []
    for m in re.finditer(r"^\s*(\d+)\s*x\s+(.+?)\s+\[([a-z0-9-]+)\]\s*$", text, re.M):
        # The name and price come from the catalogue by SKU; only the quantity is read here.
        items.append({"sku": m.group(3), "qty": int(m.group(1)), "opt": ""})
    return {"name": field("Name"), "email": field("Email"), "phone": field("Phone"),
            "address": field("Deliver"), "items": items}


def clipboard():
    return subprocess.run(["pbpaste"], capture_output=True, text=True).stdout


# ------------------------------------------------------------ Stripe
def stripe_key():
    r = subprocess.run(["security", "find-generic-password", "-s", KEYCHAIN, "-w"],
                       capture_output=True, text=True)
    key = r.stdout.strip()
    if not key:
        die("No Stripe key in the Keychain yet. Copy your restricted key, then run:\n"
            f'    security add-generic-password -U -s {KEYCHAIN} -a stripe -w "$(pbpaste)"')
    return key


def api(key, method, path, data=None):
    body = urllib.parse.urlencode(data or {}, doseq=True).encode() if data else None
    url = f"https://api.stripe.com/v1/{path}"
    if method == "GET" and data:
        url, body = url + "?" + urllib.parse.urlencode(data), None
    req = urllib.request.Request(url, data=body, method=method,
                                 headers={"Authorization": f"Bearer {key}"})
    try:
        return json.load(urllib.request.urlopen(req, timeout=30))
    except urllib.error.HTTPError as e:
        err = json.load(e).get("error", {})
        hint = " (the key needs Customers: Write and Invoices: Write)" if e.code in (401, 403) else ""
        die(f"Stripe said: {err.get('message', e)}{hint}")


# ------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("delivery", type=float, help="delivery charge in NZ$, e.g. 25 (0 for none)")
    ap.add_argument("--send", action="store_true", help="create the invoice and email it")
    ap.add_argument("--days", type=int, default=3, help="days until due (default 3)")
    ap.add_argument("--file", help="read the email from this file instead of the clipboard")
    a = ap.parse_args()

    text = open(a.file, encoding="utf-8").read() if a.file else clipboard()
    if "ITEMS" not in text or "Email:" not in text:
        die("The clipboard doesn't hold a quote request email. Open the email, press Cmd+A then Cmd+C, and try again.")
    q = parse(text)
    if not q["items"]:
        die("No items found in the email.")
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", q["email"]):
        die(f"The email has no valid customer address ({q['email']!r}).")
    if a.delivery < 0:
        die("Delivery can't be negative.")

    # The site turns away Python's default user agent, so name ours.
    req = urllib.request.Request(CATALOGUE, headers={"User-Agent": "MagnumSports-invoice/1.0"})
    try:
        cat = {p["s"]: p for p in json.load(urllib.request.urlopen(req, timeout=30))}
    except Exception as e:
        die(f"Could not load the live catalogue ({e}). Check your internet connection.")
    lines, total, kgx = [], 0, 0.0
    for it in q["items"]:
        p = cat.get(it["sku"])
        if not p or not p.get("p"):
            die(f"{it['sku']} is not in the live catalogue (or has no price). Check it before invoicing.")
        cents = round(float(p["p"]) * 100)
        desc = p["n"] + (f" (pack of {p['k']})" if p.get("k") else "") + (f" ({it['opt']})" if it["opt"] else "")
        lines.append((desc, it["qty"], cents, it["sku"]))
        if p.get("x"):
            kgx += float(p.get("w") or 0) * it["qty"]
        total += cents * it["qty"]
    deliv = round(a.delivery * 100)
    total += deliv

    print(f"\n  Invoice for {q['name']} <{q['email']}>")
    if q["phone"]:
        print(f"  Phone:    {q['phone']}")
    print(f"  Deliver:  {q['address']}\n")
    for desc, qty, cents, sku in lines:
        print(f"  {qty:>3} x {desc[:60]:<60} NZ${cents * qty / 100:>10,.2f}")
    print(f"        {'Delivery':<60}   NZ${deliv / 100:>10,.2f}")
    print(f"        {'TOTAL (incl. GST)':<60}   NZ${total / 100:>10,.2f}")
    if kgx:
        import math
        whole = max(1, math.ceil(round(kgx, 3)))
        print(f"\n  Note: {kgx:.2f} kg of these items are charged by weight: rate card NZ${30.11 + 22.19 * (whole - 1):.2f} "
              f"({whole} kg). Add the pack delivery on top of that for your delivery figure.")
    print(f"\n  Due in {a.days} day{'s' if a.days != 1 else ''}.")
    if not a.send:
        print("  Preview only. Add --send to create the invoice and email it to the customer.\n")
        return

    key = stripe_key()
    found = api(key, "GET", "customers", {"email": q["email"], "limit": 1})["data"]
    cust = found[0]["id"] if found else api(key, "POST", "customers", {
        "name": q["name"], "email": q["email"], "phone": q["phone"],
        "shipping[name]": q["name"], "shipping[address][line1]": q["address"][:200],
        "shipping[address][country]": "NZ",
        "metadata[source]": "magnumsports.co.nz quote request"})["id"]
    inv = api(key, "POST", "invoices", {
        "customer": cust, "currency": "nzd", "collection_method": "send_invoice",
        "days_until_due": a.days, "pending_invoice_items_behavior": "exclude",
        "description": "Your Magnum Sports order, including delivery. Prices include GST.",
        "footer": f"Delivery to: {q['address'][:300]}. Questions? {SITE}/contact/",
        "metadata[source]": "quote request"})
    for desc, qty, cents, sku in lines:
        api(key, "POST", "invoiceitems", {
            "customer": cust, "invoice": inv["id"], "currency": "nzd",
            "amount": cents * qty, "description": f"{qty} x {desc}"[:500], "metadata[sku]": sku})
    if deliv:
        api(key, "POST", "invoiceitems", {
            "customer": cust, "invoice": inv["id"], "currency": "nzd",
            "amount": deliv, "description": "Delivery within New Zealand"})
    api(key, "POST", f"invoices/{inv['id']}/finalize", {"auto_advance": "false"})
    sent = api(key, "POST", f"invoices/{inv['id']}/send")
    if sent.get("amount_due") != total:
        print(f"  ! Stripe's total NZ${sent.get('amount_due', 0) / 100:,.2f} differs from ours "
              f"NZ${total / 100:,.2f}: check the invoice in the dashboard.")
    print(f"\n  ✓ Invoice {sent.get('number') or inv['id']} emailed to {q['email']} "
          f"for NZ${sent.get('amount_due', total) / 100:,.2f}.")
    print(f"    Customer's pay page: {sent.get('hosted_invoice_url')}\n")


if __name__ == "__main__":
    main()
