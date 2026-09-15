# Department photos

Drop a photo here named after the department slug and rebuild — the homepage
card picks it up automatically. No markup or CSS changes needed.

    images/departments/<slug>.jpg      (or .webp / .png)

| Slug | Department |
|---|---|
| `airguns` | Airguns |
| `ammunition` | Ammunition |
| `apparel` | Apparel |
| `bags` | Bags |
| `firearms-and-accessories` | Firearms and Accessories |
| `fishing` | Fishing |
| `footwear` | Footwear |
| `hunting-accessories` | Hunting Accessories |
| `outdoor-leisure` | Outdoor Leisure |
| `reloading` | Reloading |
| `sporting-goods` | Sporting Goods |
| `clearance` | Clearance |

Until a file exists, the card renders a dark brand-gradient tile with the
department icon. That is the deliberate fallback, not a placeholder to be
embarrassed about — the cards look finished either way, and photos are a pure
swap.

## Specs

- **800 x 450** (16:9). The card crops with `object-fit: cover`, so anything
  wider than 16:9 loses the sides and anything taller loses top and bottom —
  keep the subject centred.
- **JPEG, quality 82-88**, under about 120 KB each. They are lazy-loaded and
  below the fold, but twelve of them adds up.
- Shoot or crop **landscape**. Portrait product shots crop badly here.

## What actually works in these cards

Shoot the shop. Photos of your own stock on your own shelves will beat any
stock library for this page, for three reasons: they are unmistakably yours,
they carry local signals that help the Google Business Profile, and a customer
recognises the aisle when they walk in. A phone camera near the window on an
overcast day is genuinely enough — no flash, shoot along the shelf rather than
straight at it, and leave headroom for the crop.

If you want stock instead, **Unsplash and Pexels** both have strong outdoor,
hunting and fishing photography under licences that permit commercial use
without attribution. Both need a free API key. Hand one over and the fetch can
be scripted against the slug list above.

## Sources that were checked and rejected

- **Openverse (CC0/public domain filter)** — no results at all for airguns,
  firearms, reloading or hunting accessories. "Ammunition" returned WW2
  Wehrmacht photographs; "fly fishing" returned a railway viaduct; "sporting
  goods" returned clipart.
- **Wikimedia Commons** — better coverage, but almost everything relevant is
  CC BY-SA (attribution plus share-alike, awkward on a commercial site) and
  the register is archival or museum-catalogue rather than retail. Think
  1970s fishing publicity shots and object photography on white.

Neither is worth shipping. The fallback tile looks better than a bad photo.
