# magnumsports.co.nz

**Magnum Sports**: an online store for outdoor gear, delivered across New Zealand.

Static HTML, generated from Python. No framework and no build dependencies beyond the standard
library, plus Pillow for the image scripts.

| Page | What it is |
|---|---|
| `/` | Departments, five picks from each, favourites, how ordering works, FAQ |
| `/shop/` | Online shop front: department tiles, cart and order-request form |
| `/shop/<department>/` | Every product in one department, and that department's FAQ |
| `/shop/<department>/<sku>/` | One product: photo, description, full specifications, add to cart |
| `/search/?q=` | Product search results (not indexed, not in the sitemap) |
| `/about/`, `/contact/` | The business |
| `/terms/`, `/privacy/`, `/cookie-policy/` | Legal |

## Building

```bash
python3 _build/build.py
```

Regenerates every page, `assets/js/cart.js`, `sitemap.xml` and `robots.txt`. Output is written in
place: this repo *is* the deployed site (GitHub Pages, see `CNAME`). GitHub Pages does not serve
folders that start with `_`, so `_build/` stays off the live site. It is still visible to anyone who
can see the repository.

### Where things live

| File | Controls |
|---|---|
| `_build/lib.py` | Business details (`STORE`), departments (`DEPARTMENTS`; one appears only once it has products), the catalogue loader (`PRODUCTS`), order email (`ORDER_EMAIL`), payment methods (`PAYMENT`, `PAY_HOW`), page titles (`META`), nav, footer, schema and shared components |
| `_build/products.json` | The store's own products. One entry each: `sku`, `name`, `price`, `dept`, `blurb`, optional `options` (sizes etc.) and `featured` |
| `_build/supplier/` | Supplier price sheets and their scripts (below) |
| `_build/p_home.py` | Homepage |
| `_build/p_shop.py` | Shop front, department pages, product pages; writes `assets/js/cart.js` |
| `_build/p_site.py` | About, contact, terms, privacy, cookies |
| `_build/search.js` | Search: the header search box and `/search/`. Copied to `assets/js/search.js`; the build writes the index it searches to `assets/js/search.json` |
| `_build/cart.js` | Cart source. The build bakes the catalogue and `ORDER_EMAIL` into `assets/js/cart.js`, so edit this file, not the output |
| `_build/faq_data.py` | FAQs: the shop-wide set (`HOME`, on the homepage) and one set per department (`DEPT`). The questions come from real NZ search autosuggest; see the file's header |
| `_build/pixels.py`, `_build/check_titles.py` | Build check: no page title wider than Google shows before truncating |
| `_build/gen_images.py` | Favicons and the social sharing card (`images/og-magnum.jpg`) |
| `assets/css/site.css` | The stylesheet |

### The cart

The site has no server, so the cart does not take payment. It lives in the visitor's browser
(`localStorage`), and checkout opens their email app with the order written out, addressed to
`ORDER_EMAIL`. The shop replies to confirm stock and payment (prices include GST and NZ-wide delivery): bank transfer (account details
in that reply, never on the site) or Visa/Mastercard over the phone. The shop is online only:
nothing is sold for collection, and firearms, ammunition, reloading and airguns are not sold.

### Card checkout (Stripe)

`_build/stripe-worker/` is a Cloudflare Worker that holds the Stripe key and opens Stripe Checkout for
the cart; see its README. While `CHECKOUT_URL` in `lib.py` is empty, the site takes order requests
only (Stripe invoices, bank transfer, card by phone). Set it to the deployed Worker's address and
rebuild to add "Pay now by card". The Stripe key is never in this repository.

### Search

The site is static, so search runs in the browser. The build writes every product's name,
department, price, description, model and link to `assets/js/search.json`, fetched the first time
someone opens search. Every word typed must match; matches in the product name rank first.
Press `/` on any page to open the search box.

### Product photos

A product shows its photo when `images/products/<sku>.webp` (or `.jpg`/`.png`) exists; otherwise
its card shows the department icon. Drop a file in and rebuild.

### Suppliers

Every supplier is registered in `_build/supplier/suppliers.json`: name, company, website, its sheet,
its SKU prefix, how it prices, and its photo settings. Every row of every sheet and every product on
the site carries its `supplier` key, so any line can be traced back to who makes it. Customers do not
see it.

| Key | Supplier | Sheet | Prices |
|---|---|---|---|
| `petram` | Guangzhou PETRAM Technology Co., Ltd | `petram.csv` (1,018 lines) | Published USD ranges |
| `ultra-safety` | Kunshan New Rich Industry Co., Ltd (Ultra Safe, Vanda) | `ultra-safety.csv` (164 lines) | Quote only: none live until quoted |

A row goes live only when it has **`sell` = `yes`** and a **`retail_nzd`** price. `name`, `dept` and
`blurb` are drafts and can be edited. Read `flags` before selling a line: it marks titles using
another company's brand or product name, legal or safety concerns, and the owner's decisions (for
Ultra Safety: no body armour or bomb blankets, no police uniforms). The `supplier_*` columns are the
supplier's own data, for reference only.

- `python3 _build/supplier/reprice.py [rate]` goes through every supplier. It switches on each row
  with no flag (a department guess is fine), an origin of China, a supplier price and a department
  sold online, and prices it at the top of the supplier's USD price × 5, converted to NZD at today's
  rate or the one given. It overwrites `sell` and `retail_nzd`, so run it before hand-editing prices.
- `exclude.txt` lists SKUs kept off sale for good: photos showing another brand's marks, and a
  copied medical tourniquet.
- `python3 _build/supplier/price_request.py make <supplier>` writes a price request spreadsheet to
  `~/Documents` for a supplier that quotes; `... load <supplier> <file.xlsx>` reads the quoted prices
  back into its sheet.
- `python3 _build/supplier/fetch_images.py` downloads the photo for every line on sale, trimmed per
  the supplier's settings, as a 600px square. Check new photos by eye before they go live.

To add a supplier: give it an entry in `suppliers.json`, build its sheet in the same columns as the
others (the first column is `supplier`), then run the steps above and rebuild.

## lastmod

`sitemap.xml` `<lastmod>` and each page's `dateModified` come from a content hash kept in
`_build/lastmod.json`: a page's date changes only when its content does. Pages that are no longer
built are dropped from the file.
