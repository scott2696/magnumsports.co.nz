# -*- coding: utf-8 -*-
"""Frequently asked questions: the shop-wide set for the homepage and one set
per department page.

The questions are the ones people actually search for. They come from Google
(gl=nz), Bing (en-NZ) and DuckDuckGo (nz-en) autosuggest for the product types
on sale, harvested 23 September 2026 and reworded only where the search was
too terse to read as a question. Answers lead with the direct response in the
first sentence. Keep them true to the shop: ordering, payment and delivery
facts come from lib.py (PAY_HOW, PAYMENT) and the terms page.
"""
from lib import PAY_HOW, STORE, EMAIL

TEL = f"<a href='tel:{STORE['phone_tel']}'>{STORE['phone_display']}</a>"

HOME = [
 ("How does ordering online work?",
  "<p>Add what you want to the cart and send us an order request with your delivery address. "
  "We reply, usually the same working day, to confirm stock and how to pay. "
  "Nothing is charged until we have confirmed your order with you.</p>"),
 ("How long does delivery take?",
  "<p><strong>7 to 10 days</strong> from when we confirm your order, anywhere in New Zealand.</p>"),
 ("How much is delivery?",
  "<p>Nothing extra. Every price already includes delivery anywhere in New Zealand, so the price "
  "you see is the price you pay.</p>"),
 ("Do you ship overseas?",
  "<p>No. We deliver within New Zealand only.</p>"),
 ("How do I pay?",
  f"<p>{PAY_HOW} We never ask for card details by email, and our bank account number only ever "
  "comes in our reply to your order.</p>"),
 ("Are your prices in New Zealand dollars?",
  "<p>Yes. Every price is in NZ dollars and includes GST and delivery.</p>"),
 ("How do I know what size to order?",
  "<p>Sizing varies by maker, so put your usual size, and for gloves your hand measurement, in "
  "the order notes. We check it against the product and confirm the fit with you before you pay. "
  "See the <a href='/shop/apparel/'>Apparel</a> questions for how to measure a hand.</p>"),
 ("Can I return something?",
  "<p>If an item is faulty or not as described, we put it right as the Consumer Guarantees Act "
  f"requires. Ring {TEL} or email <a href='mailto:{EMAIL}'>{EMAIL}</a>. If you have simply "
  "changed your mind, get in touch and we will tell you what we can do.</p>"),
 ("What is tactical gear?",
  "<p>Outdoor equipment built the way military and emergency-service gear is: tough nylon, "
  "reinforced stitching, and modular attachment such as MOLLE, so you can carry exactly what a "
  "day needs. Hunters, trampers, cyclists, tradespeople and anyone who is hard on their kit use "
  "it for the same reason: it lasts.</p>"),
]

DEPT = {
 "Apparel": [
  ("What are touchscreen gloves?",
   "<p>Gloves with conductive fibres or pads in the fingertips, usually the thumb and index "
   "finger, so a phone screen registers your touch without taking the glove off. Every glove "
   "with &ldquo;Touchscreen&rdquo; in its name here has them.</p>"),
  ("Do touchscreen gloves actually work?",
   "<p>Yes, on the phones and tablets almost everyone uses, which sense the small electrical "
   "charge of a finger through the conductive tips. They work best when the glove fits snugly at "
   "the fingertip; a loose tip, or a tip soaked through, makes taps less reliable.</p>"),
  ("Why wear fingerless or half-finger gloves?",
   "<p>For dexterity. With the fingertips free you can tie knots, work a zip, load a camera or "
   "handle small parts, while the palm and knuckles stay protected. The trade-off is less warmth, "
   "so for cold mornings choose full-finger.</p>"),
  ("What are hard-knuckle gloves for?",
   "<p>The moulded shell over the knuckles takes knocks and scrapes: scrambling over rock, "
   "clearing scrub, working on machinery. They are protective work and outdoor gloves; unless a "
   "product says otherwise, they are not certified motorcycle protective equipment.</p>"),
  ("How do I measure my hand for gloves?",
   "<p>Wrap a tape measure around your dominant hand at the widest part of the palm, just below "
   "the knuckles, without the thumb. That number in centimetres is your glove measurement. Put it "
   "in your order notes and we will match it to the glove's sizing before you pay.</p>"),
  ("Can you wash these gloves?",
   "<p>Yes. For synthetic and mixed-fabric gloves, hand wash in cool water with a little mild "
   "soap, rinse, press out the water and dry flat away from direct heat. Leather panels should be "
   "cleaned rather than soaked, then left to dry naturally. Never tumble dry.</p>"),
  ("Are tactical vests bulletproof?",
   "<p>No. The vests, chest rigs and vest liners we sell carry gear. None of them is body "
   "armour, and none is rated to stop a projectile. The foam liners are padding for comfort.</p>"),
  ("What is a chest rig?",
   "<p>A lightweight harness that sits on your chest and holds pouches for the things you reach "
   "for most: phone, radio, knife, torch, first aid. Everything stays in front of you, and nothing "
   "is buried in a pack.</p>"),
  ("How should a duty belt fit?",
   "<p>Snug enough not to slide or sag when it is loaded, but not so tight it digs in when you "
   "sit or bend. Try it with everything you plan to hang on it: weight on the belt is what makes a "
   "loose one sag.</p>"),
 ],
 "Bags": [
  ("What is MOLLE?",
   "<p>A way of attaching pouches to packs, vests and belts. The gear carries rows of strong "
   "nylon webbing, 25 mm wide and spaced 25 mm apart (called PALS webbing). A pouch's straps weave "
   "through those rows, so it sits firmly and can be moved wherever you want it.</p>"),
  ("How does the MOLLE system work?",
   "<p>Line the pouch up against the webbing, then weave its strap down alternately through the "
   "webbing on the pack and the webbing on the pouch, row by row, and snap it closed at the "
   "bottom. Because every MOLLE item uses the same spacing, pouches fit packs, vests and belts "
   "from other makers too.</p>"),
  ("What is a dump pouch used for?",
   "<p>A quick place to stash things you need to put away in a hurry: rubbish, gloves, a beanie, "
   "empty containers, finds on a walk. It folds flat when you do not need it and opens into a "
   "large bag when you do.</p>"),
  ("What is an admin pouch?",
   "<p>An organiser for the small things you keep reaching for: notebook, pens, map, torch, "
   "phone, spare batteries. Mounted on a vest or pack, it opens like a book so everything is in "
   "sight.</p>"),
  ("What is an IFAK pouch?",
   "<p>IFAK stands for Individual First Aid Kit: a pouch sized to carry one person's first aid "
   "gear where it can be reached fast. The pouches here come empty, so fill them with a first aid "
   "kit and, ideally, the training to use it.</p>"),
  ("Are sling bags good for hiking?",
   "<p>For short walks and day trips, yes: they swing round to the front so you can reach your "
   "phone, snacks or keys without stopping. For long days or heavier loads, a backpack is kinder, "
   "because it spreads the weight over both shoulders.</p>"),
  ("How big is a 3-day assault pack?",
   "<p>Usually around 30 to 45 litres: enough for a few days' clothing, food and kit. Check the "
   "capacity listed in each pack's specifications.</p>"),
  ("Can you wash a tactical backpack?",
   "<p>Yes, by hand. Empty it, brush out the dirt, then wash with cool water and mild soap and a "
   "soft brush. Rinse well and hang it upside down to dry in the shade. Skip the washing machine, "
   "the dryer and bleach: they damage the coatings and the webbing.</p>"),
 ],
 "Hunting Accessories": [
  ("What is a bipod?",
   "<p>A two-legged folding rest that attaches to the fore-end of a rifle and steadies it "
   "when you are shooting from the ground or a bench. The legs fold away along the fore-end when "
   "you are walking.</p>"),
  ("Which bipod height do I need?",
   "<p>It depends on how you shoot. <strong>6 to 9 inches</strong> suits lying prone on flat "
   "ground. <strong>9 to 13 inches</strong> clears grass and uneven ground when prone. "
   "<strong>13 to 27 inches</strong> is for sitting or kneeling. Every bipod here lists its height "
   "range in the name and specifications.</p>"),
  ("How does a bipod attach?",
   "<p>Through one of three mounts: a sling swivel stud (standard on most hunting rifles), a "
   "Picatinny rail, or an M-LOK slot. Check the mount type in the product's specifications "
   "against your rifle before you order.</p>"),
  ("Do I need a firearms licence to buy a bipod?",
   "<p>No. A bipod, shooting rest or bag is not a firearm or a controlled part under the Arms Act "
   "1983, so no licence is needed to buy one.</p>"),
  ("How do you use a rear shooting bag?",
   "<p>Set the bag under the rear of the stock, just below where your cheek rests. Squeeze the bag "
   "to raise the rifle's aim a touch, or relax your grip to lower it, while the front rests on a "
   "bipod or front bag. Check a bag's specifications to see whether it comes filled; empty bags "
   "are filled with sand, rice or plastic pellets.</p>"),
 ],
}
