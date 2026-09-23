# Checkout Worker (Stripe)

A Cloudflare Worker that turns the cart into a Stripe Checkout page. The site is
static and public, so the Stripe key lives only here, as a Cloudflare secret.

- The browser sends SKUs and quantities only. The Worker prices them from the
  site's published catalogue (`CATALOGUE_URL`), so a price edited in a browser
  never reaches Stripe.
- Stripe collects the delivery address (NZ only), phone and card; emails the
  receipt; and creates an invoice for every order.
- After paying, the customer lands on `/shop/thanks/`, which empties their cart.

## Set up (once)

1. In Stripe: **Developers → API keys → Create restricted key**. Give it
   **Checkout Sessions: Write** and nothing else. Do this in **test mode** first.
2. From this folder, in your own terminal:
   ```
   npx wrangler login                          # opens Cloudflare in the browser
   npx wrangler secret put STRIPE_SECRET_KEY   # paste the key at the prompt
   npx wrangler deploy                         # prints the Worker's address
   ```
3. Put that address plus `/checkout` in `CHECKOUT_URL` in `_build/lib.py`, and
   rebuild. The "Pay now by card" button and the pay-now wording appear.
4. Test with card `4242 4242 4242 4242`, any future date, any CVC.
5. Go live: create the same restricted key in **live mode**, run
   `npx wrangler secret put STRIPE_SECRET_KEY` again with it. Nothing else changes.

If Stripe refuses with a permissions error, `npx wrangler tail` shows which
permission the key is missing.

**Never** put the key in this repository, in `wrangler.toml`, or in chat.
`.dev.vars` (for local testing) is git-ignored.
