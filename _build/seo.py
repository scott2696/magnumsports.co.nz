"""Search copy for the catalogue: which keyword group each product belongs to,
and the titles, descriptions and blurbs written from it.

Keyword groups come from the NZ keyword research of 2026-09-29 (DataForSEO,
Google NZ). Only keywords that honestly describe the product are used: other
brands' names (Mechanix, Harris, Atlas, Backlanz, 5.11 ...) and searches for
things we do not sell (merino, leather, heated, horse-riding helmets) are left
out, so no page claims to be something it is not.

Every product fact in the copy comes from the supplier listing (name, specs);
the group text is general to the kind of product. Nothing here invents a
certification, a material or a feature.
"""
import html
import re

from pixels import px, LIMIT as TITLE_PX

esc = lambda s: html.escape(str(s), quote=True)

# ------------------------------------------------------------------ groups
# key: label (plural heading), noun (singular), kw (primary search term),
#      title (for <title>), keywords (research terms we can honestly use),
#      intro (what it is and who it is for), uses, notes, section (the short
#      text above the group on its department page).
GROUPS = {
 "tactical-gloves": dict(
    label="Tactical gloves", noun="tactical gloves", kw="tactical gloves", title="Tactical Gloves NZ",
    keywords=["tactical gloves", "tactical gloves nz", "fingerless tactical gloves", "lightweight tactical gloves",
              "shooting tactical gloves"],
    intro="Tactical gloves are built for grip and dexterity first: a close fit, reinforced palms and fingers "
          "you can still work a zip, a buckle or a phone with. They suit hunting, airsoft, range days, "
          "tramping and any outdoor work where bare hands take a beating.",
    uses=["Hunting and shooting", "Airsoft and paintball", "Tramping and climbing", "Outdoor work and DIY"],
    notes="Tactical gloves are sized to fit snugly, so a glove that feels a little tight at first usually "
          "settles in after a few wears. Put your hand measurement in the notes box at checkout if you are "
          "between sizes.",
    section="Full-finger tactical gloves for grip, dexterity and protection, from lightweight shooting "
            "gloves to hard-knuckle models. Tactical gloves in NZ, delivered in 7 to 10 days."),
 "motorcycle-gloves": dict(
    label="Motorcycle riding gloves", noun="riding gloves", kw="motorcycle gloves", title="Motorcycle Gloves NZ",
    keywords=["motorcycle gloves", "motorcycle gloves nz", "gloves motorcycle", "winter motorcycle gloves"],
    intro="These riding gloves are cut for the bike: pre-curved fingers for the bars, padded or hard-shell "
          "knuckles and an anti-slip palm. Riders use them for commuting, trail and off-road riding, "
          "and they double as tough outdoor and tactical gloves off the bike.",
    uses=["Motorcycle and scooter commuting", "Trail and off-road riding", "Mountain biking", "Outdoor and tactical use"],
    notes="Unless the listing says otherwise these are not certified motorcycle protective equipment "
          "(EN 13594), so for road riding pair them with the protection you would normally wear.",
    section="Riding gloves for motorcycles, scooters and trail bikes, with knuckle protection and anti-slip "
            "palms. Motorcycle gloves in NZ with free delivery."),
 "cycling-gloves": dict(
    label="Cycling gloves", noun="cycling gloves", kw="cycling gloves", title="Cycling Gloves NZ",
    keywords=["cycling gloves", "cycling gloves nz", "bike cycling gloves", "winter cycling gloves",
              "cycling gloves fingerless"],
    intro="Cycling gloves cushion your palms on the bars, keep your grip when your hands sweat and take "
          "the sting out of a fall. These are light and breathable enough for summer riding and tough "
          "enough for mountain biking, climbing and gym work.",
    uses=["Road and mountain biking", "Climbing and bouldering", "Gym and fitness training", "Tramping"],
    notes="For cycling, choose a snug fit: loose fingers bunch on the bars. Wash in cool water and let "
          "them air-dry away from direct heat.",
    section="Breathable cycling gloves for road, mountain bike and gym, many with touchscreen fingertips. "
            "Cycling gloves in NZ, delivered free."),
 "fingerless-gloves": dict(
    label="Fingerless gloves", noun="fingerless gloves", kw="fingerless gloves", title="Fingerless Gloves NZ",
    keywords=["fingerless gloves", "fingerless gloves nz", "fingerless gloves new zealand", "gloves fingerless",
              "fingerless tactical gloves", "cycling gloves fingerless"],
    intro="Fingerless (half-finger) gloves protect your palm and knuckles while leaving your fingertips "
          "free for triggers, reels, knots, phones and fine work. They are the glove of choice for "
          "shooting, cycling and warm-weather outdoor work in New Zealand.",
    uses=["Shooting and hunting", "Cycling and fitness", "Fishing and rope work", "Driving and everyday wear"],
    notes="Half-finger gloves should sit snugly at the base of each finger. Measure around your palm below "
          "the knuckles and put it in the notes box at checkout if you are unsure of the size.",
    section="Half-finger gloves that keep your fingertips free for triggers, phones and fine work. "
            "Fingerless gloves in NZ, delivered in 7 to 10 days."),
 "winter-gloves": dict(
    label="Winter gloves", noun="winter gloves", kw="winter gloves", title="Winter Gloves NZ",
    keywords=["winter gloves", "winter gloves nz", "gloves for winter", "winter bike gloves"],
    intro="Winter gloves for cold mornings on the hill, the bike or the farm: thicker shells, many windproof, "
          "that keep your hands working when the temperature drops, without the bulk of a ski mitt.",
    uses=["Winter hunting and tramping", "Cold-weather cycling and riding", "Farm and outdoor work", "Skiing and snow days"],
    notes="Winter gloves should have a little room at the fingertips: trapped air is what keeps you warm.",
    section="Warmer, windproof gloves for the New Zealand winter on the hill, the bike or the farm. "
            "Winter gloves in NZ with free delivery."),
 "work-gloves": dict(
    label="Work gloves", noun="work gloves", kw="work gloves", title="Work Gloves NZ",
    keywords=["work gloves", "work gloves nz", "winter work gloves"],
    intro="Hard-wearing work gloves that still let you feel what you are doing: reinforced palms for "
          "grip and abrasion, with the dexterity of a tactical glove for tools, fencing, firewood and "
          "general outdoor jobs.",
    uses=["Fencing, firewood and farm work", "DIY and building sites", "Hunting and outdoor work", "Driving and handling gear"],
    notes="Unless the listing says otherwise these are general work gloves, not certified cut or "
          "chemical-resistant PPE.",
    section="Tough, dexterous work gloves for the farm, the section and the workshop. Work gloves in NZ, "
            "delivered in 7 to 10 days."),
 "tactical-belt": dict(
    label="Tactical belts", noun="tactical belt", kw="tactical belt", title="Tactical Belts NZ",
    keywords=["tactical belt", "tactical belt nz", "tactical hunting belt", "tactical military belt"],
    intro="A tactical belt carries weight without sagging: stiff webbing, a secure buckle and room for "
          "MOLLE pouches, a knife sheath or a torch. It works as a hunting belt, a duty belt or a heavy "
          "everyday belt.",
    uses=["Hunting and bush trips", "Security and duty use", "Airsoft and training", "Carrying tools and pouches"],
    notes="Measure around your waist over the clothes you will wear it with, and allow for pouches.",
    section="Stiff, load-bearing tactical belts for pouches, tools and holsters. Tactical belts in NZ."),
 "duty-belt": dict(
    label="Duty belt sets", noun="duty belt set", kw="duty belt", title="Duty Belts NZ",
    keywords=["duty belt", "heavy duty work belt"],
    intro="A duty belt set gives you the belt and the pouches together, so security, patrol and "
          "training kit is carried in one organised, balanced rig.",
    uses=["Security and patrol work", "Training and airsoft", "Event and outdoor staff"],
    notes="Check your waist size against the belt length before you order.",
    section="Complete duty belt sets for security, patrol and training."),
 "tactical-vest": dict(
    label="Tactical vest accessories", noun="tactical vest insert", kw="tactical vest", title="Tactical Vest Gear NZ",
    keywords=["tactical vest", "tactical vest nz"],
    intro="Accessories that make a tactical vest or plate carrier more comfortable to wear for long days, "
          "for airsoft, training and outdoor use.",
    uses=["Airsoft and paintball", "Training", "Comfort under load"],
    notes="Foam inserts are for comfort and shape only: they are not ballistic or stab protection.",
    section="Comfort inserts and accessories for tactical vests and plate carriers. Not ballistic protection."),
 "baton-holster": dict(
    label="Baton holders", noun="baton holder", kw="expandable baton holder", title="Baton Holders NZ",
    keywords=["expandable baton holder", "baton holster"],
    intro="A rigid holder that keeps an expandable baton secure on a duty belt, with a rotating clip so it "
          "sits at the angle you draw from.",
    uses=["Security and duty belts", "Training kit"],
    notes="This is the holder only. Carrying a baton in public in New Zealand needs a lawful reason.",
    section="Rotating holders for expandable batons on duty belts. Holders only."),
 "molle-accessories": dict(
    label="MOLLE accessories", noun="MOLLE accessory", kw="molle accessories", title="MOLLE Accessories NZ",
    keywords=["molle accessories", "molle backpack attachments", "molle bag attachments"],
    intro="MOLLE (Modular Lightweight Load-carrying Equipment) webbing lets you attach gear anywhere on a "
          "pack, belt or vest. These clips, straps and mounts add the small fixings that make a MOLLE "
          "set-up work.",
    uses=["Customising backpacks and vests", "Mounting pouches and tools", "Hunting and camping kit", "Airsoft loadouts"],
    notes="MOLLE fits standard 1-inch (25 mm) webbing rows spaced 1 inch apart.",
    section="Clips, straps and mounts for MOLLE webbing on packs, belts and vests."),
 "molle-pouch": dict(
    label="MOLLE pouches", noun="MOLLE pouch", kw="molle pouch", title="MOLLE Pouches NZ",
    keywords=["molle pouch", "molle zip pouch", "molle glove pouch", "what is a molle pouch", "how to attach molle pouch"],
    intro="A MOLLE pouch weaves onto the webbing of a pack, belt, vest or seat back, so you can carry "
          "exactly what you need where you can reach it. These pouches suit hunting, camping, vehicle "
          "storage and airsoft loadouts.",
    uses=["Backpacks and chest rigs", "Belts and plate carriers", "Vehicle seat backs", "Hunting and camping kit"],
    notes="To attach a MOLLE pouch, thread its straps alternately through the webbing on the pouch and "
          "your pack, then snap the strap closed at the bottom.",
    section="Pouches that weave onto MOLLE webbing on packs, belts, vests and seat backs. MOLLE pouches in NZ."),
 "molle-utility-pouch": dict(
    label="MOLLE utility pouches", noun="MOLLE utility pouch", kw="molle utility pouch", title="MOLLE Utility Pouches NZ",
    keywords=["molle utility pouch", "molle utility pouch small"],
    intro="General-purpose MOLLE utility pouches for the odds and ends: snacks, a multi-tool, cordage, "
          "batteries or a first aid kit, mounted on a belt or pack.",
    uses=["Belts and packs", "Everyday carry", "Camping and hunting"],
    notes="Utility pouches are the most useful first pouch on a new pack.",
    section="General-purpose utility pouches for belts and packs."),
 "magazine-pouch": dict(
    label="Magazine pouches", noun="magazine pouch", kw="magazine pouch", title="Magazine Pouches NZ",
    keywords=["magazine pouch", "molle magazine pouch", "magazine pouch belt", "7.62 magazine pouch"],
    intro="Magazine pouches hold mags securely on a belt, chest rig or plate carrier and release them fast "
          "when you need them. They suit airsoft, range and training loadouts, and double as handy "
          "pouches for a phone, torch or multi-tool.",
    uses=["Airsoft and paintball loadouts", "Range and training kit", "Chest rigs and plate carriers", "Holding torches or tools"],
    notes="Check the calibre and size in the name (9mm, 5.56, 7.62) against the magazines you use.",
    section="Single, double and triple mag pouches in 9mm, 5.56 and 7.62 sizes, for belts, rigs and "
            "plate carriers. Magazine pouches in NZ."),
 "shotgun-shell-pouch": dict(
    label="Shotgun shell pouches", noun="shotgun shell pouch", kw="shotgun shell pouch", title="Shotgun Shell Pouches NZ",
    keywords=["shotgun shell pouch", "ammo pouch nz", "molle ammo pouch"],
    intro="Shell pouches keep 12 gauge cartridges in individual loops, so you can reload quickly and "
          "quietly in the maimai, the paddock or at the clay range.",
    uses=["Duck and game bird hunting", "Clay target shooting", "Rabbiting and pest control"],
    notes="Loops are sized for 12 gauge shells.",
    section="12 gauge shell pouches for duck hunting and clay shooting. Ammo pouches in NZ."),
 "first-aid-pouch": dict(
    label="First aid pouches", noun="first aid pouch", kw="first aid pouch", title="First Aid Pouches NZ",
    keywords=["first aid pouch", "first aid kit pouch", "mini first aid pouch", "molle pouch first aid kit",
              "first aid belt pouch"],
    intro="A first aid pouch keeps your kit together and in reach: on a belt, a pack or in the ute. "
          "Build your own trauma or tramping kit inside, from plasters and bandages to a tourniquet.",
    uses=["Tramping and hunting first aid kits", "Vehicle and boat kits", "Sports and event medics",
          "Airsoft and training"],
    notes="Pouches are sold empty: fill them with a first aid kit that suits what you do.",
    section="Pouches for your first aid and medical kit, on a belt, pack or in the vehicle. Sold empty."),
 "tourniquet-holder": dict(
    label="Tourniquet holders", noun="tourniquet holder", kw="tourniquet holder", title="Tourniquet Holders NZ",
    keywords=["tourniquet holder", "cat tourniquet holder"],
    intro="A tourniquet holder keeps a windlass tourniquet (such as a CAT-style tourniquet) and trauma "
          "shears where you can reach them one-handed, on a belt, pack strap or vest.",
    uses=["Hunting and bush first aid", "Range safety kits", "Vehicle and boat kits"],
    notes="Holders are sold empty. Check the fit against the tourniquet you carry.",
    section="Holders that keep a tourniquet and shears in one-handed reach. Sold empty."),
 "water-bottle-pouch": dict(
    label="Water bottle pouches", noun="water bottle pouch", kw="water bottle pouch", title="Water Bottle Pouches NZ",
    keywords=["water bottle pouch", "molle pouch for water bottle", "water bottle carry pouch",
              "backpack water bottle pouch"],
    intro="A water bottle pouch puts a drink on your belt or pack strap instead of buried inside your pack, "
          "so you actually drink on the hill.",
    uses=["Tramping and hunting", "Day walks and dog walks", "Cycling and running", "Camping"],
    notes="Measure your bottle: most pouches suit standard 500 ml to 1 litre bottles.",
    section="Bottle carriers for belts and packs, so a drink is always in reach."),
 "drop-leg-pouch": dict(
    label="Drop leg pouches and platforms", noun="drop leg pouch", kw="drop leg pouch", title="Drop Leg Pouches NZ",
    keywords=["drop leg pouch", "leg pouch", "thigh pouch", "drop leg medical pouch"],
    intro="Drop leg pouches and platforms move weight off your belt and onto your thigh, where it is easy "
          "to reach when you are wearing a pack or sitting in a vehicle.",
    uses=["Hunting and bush work", "Airsoft loadouts", "Tools and first aid on the move", "Riding and driving"],
    notes="Adjust the leg straps so the pouch sits firmly without restricting your stride.",
    section="Thigh-mounted pouches and platforms that carry gear below your belt."),
 "radio-pouch": dict(
    label="Radio pouches", noun="radio pouch", kw="radio pouch", title="Radio Pouches NZ",
    keywords=["radio pouch", "radio pouch nz", "molle radio pouch", "handheld radio pouch"],
    intro="Radio pouches hold a handheld radio, PLB or power bank upright on a chest rig, belt or pack "
          "strap, with the antenna free and the controls in reach.",
    uses=["Hunting parties and deer stalking", "Search and rescue training", "Airsoft teams", "Farm and event work"],
    notes="Check your radio's dimensions against the pouch before ordering.",
    section="Pouches for handheld radios, PLBs and power banks. Radio pouches in NZ."),
 "edc-pouch": dict(
    label="EDC pouches", noun="EDC pouch", kw="edc pouch", title="EDC Pouches NZ",
    keywords=["edc pouch", "edc pouch nz", "edc zip pouch", "edc knife pouch"],
    intro="An EDC (everyday carry) pouch keeps the small things you always carry together: multi-tool, "
          "torch, keys, lighter, cards and cables, on your belt, in a bag or clipped to MOLLE.",
    uses=["Everyday carry", "Travel and commuting", "Camping and hunting", "Vehicle glovebox kits"],
    notes="Most EDC pouches have MOLLE straps on the back as well as a carry loop.",
    section="Everyday-carry organisers for tools, torch, keys and cards. EDC pouches in NZ."),
 "flashlight-pouch": dict(
    label="Flashlight pouches", noun="flashlight pouch", kw="flashlight pouch", title="Flashlight Pouches NZ",
    keywords=["flashlight pouch", "molle flashlight pouch", "torch holder"],
    intro="A flashlight pouch holds a torch where you can grab it in the dark: on your belt, pack strap "
          "or vest, with a secure closure so it stays put.",
    uses=["Night hunting and spotlighting", "Camping and tramping", "Security work", "Vehicle kits"],
    notes="Measure your torch's body diameter and length against the pouch.",
    section="Torch holders for belts, packs and vests."),
 "molle-phone-pouch": dict(
    label="Phone pouches", noun="MOLLE phone pouch", kw="molle phone pouch", title="MOLLE Phone Pouches NZ",
    keywords=["molle phone pouch", "molle pouch phone"],
    intro="A MOLLE phone pouch keeps your phone protected and reachable on a pack strap, belt or chest rig "
          "rather than in a pocket.",
    uses=["Hunting and navigation apps", "Tramping", "Cycling and riding", "Work sites"],
    notes="Check your phone's screen size (with case) against the pouch size in the name.",
    section="Phone pouches for pack straps, belts and chest rigs."),
 "tactical-waist-bag": dict(
    label="Tactical waist bags", noun="tactical waist bag", kw="tactical waist bag", title="Tactical Waist Bags NZ",
    keywords=["tactical waist bag", "waist bag tactical", "tactical fanny pack", "tactical waist pack"],
    intro="A tactical waist bag carries the essentials on your hips: phone, wallet, keys and a few tools, "
          "with MOLLE webbing to add pouches. Hands-free and light, for day walks, travel and outdoor work.",
    uses=["Day walks and dog walks", "Travel and festivals", "Hunting and fishing", "Everyday carry"],
    notes="Most waist bags can also be worn crossbody by lengthening the strap.",
    section="Hip and waist packs for the essentials, many with MOLLE webbing. Tactical waist bags in NZ."),
 "tactical-sling-bag": dict(
    label="Tactical sling bags", noun="tactical sling bag", kw="tactical sling bag", title="Tactical Sling Bags NZ",
    keywords=["tactical sling bag", "tactical crossbody bag", "tactical chest bag"],
    intro="A tactical sling bag rides across your chest or back and swings round when you need it: more "
          "room than a waist bag, less than a backpack, for day trips, travel and everyday carry.",
    uses=["Day trips and travel", "Everyday carry", "Hunting and fishing", "Cycling and commuting"],
    notes="Sling bags can usually be worn left or right shoulder.",
    section="Crossbody and chest sling bags with MOLLE webbing. Tactical sling bags in NZ."),
 "tactical-backpack": dict(
    label="Tactical backpacks", noun="tactical backpack", kw="tactical backpack", title="Tactical Backpacks NZ",
    keywords=["tactical backpack", "tactical backpack nz", "black tactical backpack", "tactical backpack for travel"],
    intro="A tactical backpack is built tougher than a school bag: heavy fabric, strong zips and MOLLE "
          "webbing all over for extra pouches. It works as a day pack, hunting pack, go bag or travel bag.",
    uses=["Day walks and hunting", "Travel and carry-on", "Emergency go bag", "Gym and work"],
    notes="Load heavy items close to your back and use the chest strap on the hill.",
    section="MOLLE backpacks for hunting, travel and everyday use. Tactical backpacks in NZ."),
 "helmet-bag": dict(
    label="Helmet bags and pouches", noun="helmet bag", kw="helmet bag", title="Helmet Bags NZ",
    keywords=["helmet bag", "helmet bag nz", "motorcycle helmet bag"],
    intro="Padded helmet bags and helmet pouches protect a helmet in transport and add storage to it, for "
          "airsoft, riding and outdoor use.",
    uses=["Carrying and storing helmets", "Airsoft and training", "Motorcycle and bike helmets"],
    notes="Check your helmet size against the bag before ordering.",
    section="Bags and pouches for carrying, protecting and adding storage to helmets."),
 "helmet-cover": dict(
    label="Helmet covers", noun="helmet cover", kw="helmet cover", title="Helmet Covers NZ",
    keywords=["helmet cover", "tactical helmet cover"],
    intro="A fabric helmet cover protects a tactical or airsoft helmet from scratches and adds camouflage.",
    uses=["Airsoft and paintball", "Training", "Camouflage"],
    notes="Covers are made for a specific helmet shape: check the model in the name.",
    section="Fabric covers for tactical and airsoft helmets."),
 "knife-sheath": dict(
    label="Knife sheaths", noun="knife sheath", kw="knife sheath", title="Knife Sheaths NZ",
    keywords=["knife sheath", "knife sheath hunting and fishing", "sheath knife"],
    intro="A good knife sheath keeps a hunting or fishing knife safe on your belt and quick to draw, and "
          "protects the edge between uses.",
    uses=["Hunting and butchering", "Fishing", "Camping and bushcraft", "Farm work"],
    notes="Sheaths are sold without a knife. Measure your blade and handle against the sheath.",
    section="Belt sheaths for hunting, fishing and bushcraft knives. Knife not included."),
 "tool-pouch": dict(
    label="Tool pouches", noun="tool pouch", kw="tool pouch", title="Tool Pouches NZ",
    keywords=["tool pouch", "tool pouch nz", "tool belt pouch", "belt tool pouch", "small tool pouch"],
    intro="A tool pouch keeps hand tools organised on your belt or pack: pliers, screwdrivers, a knife, "
          "a torch and fixings each in their own slot.",
    uses=["Trades and building sites", "Farm and fencing work", "Hunting and camping", "Vehicle kits"],
    notes="Slots are sized for common hand tools. Tools are not included.",
    section="Belt tool pouches with slots for hand tools. Tool pouches in NZ."),
 "dump-pouch": dict(
    label="Dump pouches", noun="dump pouch", kw="dump pouch", title="Dump Pouches NZ",
    keywords=["dump pouch", "molle dump pouch"],
    intro="A dump pouch is a fold-away bag on your belt or pack for anything you need to stash fast: empty "
          "mags, rubbish, foraged food, shells or gloves. It rolls flat when you do not need it.",
    uses=["Airsoft and range days", "Collecting spent shells", "Foraging and hunting", "General stash bag"],
    notes="Dump pouches fold or roll up small when empty.",
    section="Fold-away stash bags for your belt or pack."),
 "grenade-pouch": dict(
    label="Grenade pouches", noun="grenade pouch", kw="molle grenade pouch", title="MOLLE Grenade Pouches NZ",
    keywords=["molle grenade pouch", "grenade pouch"],
    intro="Small, round-bottomed MOLLE pouches originally sized for grenades, now used for airsoft "
          "grenades, smoke, a compass or small items on a vest.",
    uses=["Airsoft loadouts", "Small items on a vest or belt"],
    notes="For airsoft and storage use.",
    section="Small MOLLE pouches for airsoft grenades and small items."),
 "shooting-rest": dict(
    label="Shooting rests", noun="shooting rest bag", kw="shooting rest", title="Shooting Rests NZ",
    keywords=["shooting rest", "shooting rest nz", "shooting rest bags", "bench rest shooting"],
    intro="A shooting rest bag steadies a rifle on a bench, bonnet or rock for accurate, repeatable shots "
          "when sighting in or shooting at range.",
    uses=["Sighting in at the range", "Bench rest shooting", "Hunting from a vehicle or rock"],
    notes="Fill with sand or plastic pellets to the firmness you like.",
    section="Bags and rests that steady a rifle for sighting in and range work."),
 "rifle-sling": dict(
    label="Rifle slings", noun="rifle sling", kw="rifle sling", title="Rifle Slings NZ",
    keywords=["rifle sling", "rifle sling nz", "hands free rifle sling nz", "3 point rifle sling"],
    intro="A rifle sling carries the weight on your shoulder on the walk in and steadies your aim when you "
          "take a shot. An adjustable two-point sling is the most versatile choice for hunting.",
    uses=["Deer and goat hunting", "Long walks in", "Range days"],
    notes="Check the swivel or clip type against the mounts on your rifle.",
    section="Adjustable rifle slings for the walk in. Rifle slings in NZ."),
 "rifle-cheek-rest": dict(
    label="Cheek rests", noun="rifle cheek rest", kw="rifle cheek rest", title="Rifle Cheek Rests NZ",
    keywords=["rifle cheek rest", "cheek rest pouch", "buttstock cheek rest"],
    intro="A cheek rest raises your eye to line up with the scope, and its pouch carries spare "
          "cartridges on the stock where you can reach them.",
    uses=["Scoped hunting rifles", "Range shooting"],
    notes="Adjustable straps fit most buttstocks.",
    section="Cheek rests and buttstock pouches for scoped rifles."),
 "rifle-bipod": dict(
    label="Rifle bipods", noun="rifle bipod", kw="rifle bipod", title="Rifle Bipods NZ",
    keywords=["rifle bipod", "bipod nz", "hunting bipod", "shooting bipod", "adjustable bipod"],
    intro="A rifle bipod turns any rest into a steady shooting position. Pick the height by how you shoot: "
          "6 to 9 inches for prone, 9 to 13 inches for sitting behind a log, and taller for sitting upright.",
    uses=["Prone shooting at the range", "Hunting from a ridge or log", "Varmint and pest control", "Sighting in"],
    notes="Check the mount (sling swivel stud, Picatinny or M-Lok) against your rifle before ordering.",
    section="Adjustable rifle bipods from 6 to 27 inches, for prone and sitting shots. Rifle bipods in NZ."),
 "carbon-bipod": dict(
    label="Carbon fibre bipods", noun="carbon fibre bipod", kw="carbon fiber bipod", title="Carbon Fibre Bipods NZ",
    keywords=["carbon fiber bipod", "carbon bipod nz", "bipod carbon fiber"],
    intro="A carbon fibre bipod gives you the steadiness of a bipod at a fraction of the weight, the "
          "choice for mountain hunting where every gram counts.",
    uses=["Mountain and alpine hunting", "Lightweight rifle set-ups", "Prone shooting"],
    notes="Check the mount against your rifle before ordering.",
    section="Lightweight carbon bipods for mountain hunting."),
 "mlok-bipod": dict(
    label="M-Lok bipods", noun="M-Lok bipod", kw="m-lok bipod", title="M-Lok Bipods NZ",
    keywords=["m-lok bipod", "mlok bipod", "rifle bipod", "bipod nz"],
    intro="An M-Lok bipod bolts straight to an M-Lok handguard, with no adaptor, for a low, solid mount.",
    uses=["M-Lok rifles and chassis", "Prone shooting", "Hunting"],
    notes="Fits M-Lok slots only.",
    section="Bipods that mount directly to M-Lok handguards."),
 "shemagh": dict(
    label="Shemaghs", noun="shemagh", kw="shemagh", title="Shemagh NZ",
    keywords=["shemagh", "shemagh nz", "shemagh scarf", "shemagh cotton", "how to tie a shemagh",
              "shemagh vs keffiyeh"],
    intro="A shemagh is a large square cotton scarf worn as a neck wrap, face cover or head wrap. It keeps "
          "sun, wind, dust and sandflies off, and doubles as a sweat rag, sling or pot holder.",
    uses=["Sun and wind protection", "Hunting and tramping", "Dusty tracks and dirt bikes", "Camping"],
    notes="To tie a shemagh as a neck scarf, fold it corner to corner into a triangle, place the point "
          "at the front and wrap the ends around your neck. A shemagh and a keffiyeh are the same kind "
          "of scarf; shemagh is the name most used in outdoor and military gear.",
    section="Large cotton shemagh scarves for sun, wind and dust."),
}

# Which group each product is in. Glove families match on the model code in
# the SKU (petram-b33-blk, -rgg ... all tactical gloves); other lines by SKU.
FAMILIES = {
 "tactical-gloves": "a26 a28 b80 b62 b33 b10 b60 b61 b28 a27 n31 b7 b26 b39 b31 b99 n33 c60 b85",
 "motorcycle-gloves": "n32 b22 a17 n28 a72 n10 n19 n77 b79",
 "cycling-gloves": "a30 l26 a9 n15 b55 n11 n38 b8 c5 a20 n21 b66",
 "fingerless-gloves": "comp n9 b56 b58 n50",
 "winter-gloves": "a50 a24 002 001",
 "work-gloves": "b36-f a6 a2",
}
SKUS = {
 "motorcycle-gloves": "blackhawk-snd blackhawk-blk hawk-rgg",
 "baton-holster": "aa-044-bk aa-019-bk",
 "tactical-belt": "custom-wfogpc custom-pzytkl custom-hzsgyx",
 "duty-belt": "lb-10-piece-set",
 "tactical-vest": "eva-pad",
 "molle-accessories": "custom-hzcgfa custom-iohfvl qt-030 gb-acc-08 custom-dfnfzw aa-244 gj-001",
 "shotgun-shell-pouch": "dj-028 custom-pdjtdt custom-vwnaca",
 "tactical-waist-bag": "custom-iohamr custom-tdcaif lb-23-wfntwk custom-hdygtw lb-01 custom-szsfwo "
                       "custom-lwntit lb-07 lm-10 rb-21 custom-cwnafg",
 "tourniquet-holder": "custom-zdhgwj qls19-22 aa-311 qls19-22-zfstsd custom-tojfoa custom-zojadg",
 "water-bottle-pouch": "custom-rostbf custom-ddwavq custom-idkfno custom-rdfgiw",
 "first-aid-pouch": "custom-szwghy custom-dzvfcy custom-bfsfrt br-yb01 lb-121 custom-afcamf custom-fdcaxc "
                    "custom-wfstpz custom-gwjfqx lb-58 lb-122 custom-jdntbv",
 "molle-pouch": "custom-wzjtaz custom-udjfcw custom-afyads custom-boytxt custom-pwwgci zh-095-a br-134 dj-101",
 "magazine-pouch": "br-135 mg-f-15 mg-f-01 mg-f-02 custom-jozamf mg-116 br-d1 custom-kwygzv custom-tdwgjv mg-35 "
                   "ve-75-acc-14 ve-75-acc-15 custom-izkfqi mg-34 mg-115 lb mg-49 mg-48 ve-74-acc-02 "
                   "ve-74-acc-03 mg-74 custom-jfstvw lb-triple-combo-pouch br-136 mg-f-04 mg-114 mg-f-06",
 "drop-leg-pouch": "custom custom-ufyfwz lb-tornado custom-sdcgtm so-185 qt-250 gb-acc-01",
 "helmet-bag": "tk-acc-01 tk-035",
 "helmet-cover": "tk-036",
 "knife-sheath": "custom-eznfcs lb-28 custom-udkgjj",
 "flashlight-pouch": "lb-132 custom-kfyfvl custom-jzsanh custom-hdyank custom-pwcaty custom-fwcamg",
 "radio-pouch": "custom-nwctso custom-doctws custom-sfjtqc custom-hocagw lb-small-radio-pouch custom-xzctng",
 "edc-pouch": "lb-39 custom-tznamk lb-23 lb-03 lb-09 lb-130 lb-41",
 "rifle-sling": "custom-wzjaqu",
 "molle-phone-pouch": "custom-pdwtla custom-roytdg d-1 d-2",
 "rifle-cheek-rest": "zp-6-2-combination-tactical-cheek-rest-cover 8-holes-cheek-rest-pouch",
 "tactical-backpack": "lm201",
 "molle-utility-pouch": "custom-vfcavx qt-206",
 "shooting-rest": "zp-bb-sand-bag",
 "grenade-pouch": "gp-10 gp-08",
 "dump-pouch": "custom-tzsfqd lb-small-dump-pouch",
 "tactical-sling-bag": "lb-06 lm-06 lb-124 lb-37",
 "tool-pouch": "custom-sdnfhw custom-rdyaxw",
 "rifle-bipod": "13inb 27inb bt-07 6in11mmb 9inb bt-11 v8-b v8-t sr-5-b sr-5-t v9-ft-tan v9-ft",
 "carbon-bipod": "bt-09",
 "mlok-bipod": "pt-mag933-fde-atkrwv pt-mag933-fde",
 "shemagh": "wj-001",
}
_BY_SKU = {f"petram-{s}": g for g, ss in SKUS.items() for s in ss.split()}
_FAMILY = [(f"petram-{c}-", g) for g, cs in FAMILIES.items() for c in cs.split()]
# Fallback when a new product has not been mapped yet: the department's main group.
_DEPT_DEFAULT = {"Apparel": "tactical-gloves", "Bags": "molle-pouch", "Hunting Accessories": "molle-accessories"}


def group_of(p):
    g = _BY_SKU.get(p["sku"])
    if not g:
        g = next((g for pre, g in _FAMILY if p["sku"].startswith(pre)), None)
    return g


# ------------------------------------------------------------------ facts
COLOURS = {"Black", "Grey", "Navy", "Red", "Blue", "White", "Sand", "Ranger Green", "Multicam", "Tan",
           "Coyote", "Coyote Brown", "OD Green", "Flat Dark Earth", "Dark Earth", "Camo", "Wolf Grey", "Orange",
           "Green"}
# Words in the supplier's product name -> the feature we can state.
FEATURES = [
    (r"touch ?screen", "touchscreen fingertips"),
    (r"half-finger|fingerless", "a half-finger cut"),
    (r"full-finger|full finger", "full-finger cover"),
    (r"hard shell|hard-shell", "hard-shell knuckles"),
    (r"anti-?cut", "cut-resistant palms"),
    (r"windproof", "windproof"),
    (r"waterproof", "waterproof"),
    (r"shock ?(absorb|proof)", "shock-absorbing pads"),
    (r"anti-?(slip|skid)", "anti-slip grip"),
    (r"anti-?fall", "impact protection"),
    (r"wear[- ]resistant|durable|tough|sturdy|heavy duty|strong", "hard-wearing"),
    (r"breathable", "breathable"),
    (r"\bwarm\b|winter|thick", "extra warmth"),
    (r"camo|camouflage|tiger stripe", "a camo pattern"),
    (r"molle", "MOLLE-compatible"),
    (r"quick (release|detach|draw)|quick drain", "quick-release access"),
    (r"elastic", "elastic retention"),
    (r"hook and loop", "hook-and-loop fastening"),
    (r"adjustable", "adjustable fit"),
    (r"retractable", "retractable legs"),
    (r"360|rotat|pivot|tilt|swivel", "a rotating mount"),
    (r"alumin", "aluminium alloy"),
    (r"carbon fib", "carbon fibre"),
    (r"lightweight|\blight\b", "lightweight"),
    (r"foldable|collapsible", "a fold-flat design"),
    (r"molle expandable", "expandable sides"),
]


def split_name(p):
    """('Base name', 'Black') for 'Base name — Black'; variant may be a model."""
    base, _, var = p["name"].partition(" — ")
    return base.strip(), var.strip()


def code(p):
    """The maker's model code without the colour suffix: 'B56' from 'B56-BLK'."""
    m = (p.get("model") or "").strip()
    if not m or m.lower() == "custom":
        return ""
    c = m.rsplit("-", 1)[0] if re.search(r"-[A-Z]{2,4}$", m) else m
    return c if len(c) <= 14 else ""


def colour(p):
    _, var = split_name(p)
    if var in COLOURS:
        return var
    c = dict(p.get("specs") or []).get("Color", "")
    return c if c and "/" not in c else ""


def colours_available(p):
    c = dict(p.get("specs") or []).get("Color", "")
    return [x.strip() for x in c.split("/") if x.strip()] if "/" in c else []


def features(p):
    name = split_name(p)[0].lower()
    out = []
    for rx, f in FEATURES:
        if re.search(rx, name) and f not in out:
            out.append(f)
    return out


def spec(p, key):
    return dict(p.get("specs") or []).get(key, "")


def _join(xs):
    xs = list(xs)
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1] if xs else ""


# ------------------------------------------------------------------ copy
def G(p):
    return GROUPS[p["group"]]


# Features that read as adjectives ("lightweight magazine pouch"); the rest
# follow "with" ("... with elastic retention").
ADJ = {"windproof", "waterproof", "breathable", "hard-wearing", "lightweight", "MOLLE-compatible",
       "adjustable fit", "aluminium alloy", "carbon fibre"}


def _phrase(p, n_with=2):
    """'Lightweight MOLLE-compatible magazine pouch with elastic retention'."""
    g, fs = G(p), features(p)
    adj = [f.replace(" fit", "") for f in fs if f in ADJ][:2]
    rest = [f for f in fs if f not in ADJ][:n_with]
    s = " ".join(adj + [g["noun"]]) + (" with " + _join(rest) if rest else "")
    return s


def blurb(p):
    """One or two lines for cards and search results."""
    s = _phrase(p)
    s = s[0].upper() + s[1:]
    mat = spec(p, "Material")
    tail = [x for x in (mat, colour(p).lower() if colour(p) else "") if x]
    return s + "." + (" " + ", ".join(tail).capitalize() + "." if tail else "")


def title(p, brand):
    """'<name> – <colour> | <Keyword> NZ', fitted to the width Google shows.
    The name is shortened first; the colour stays so variants stay distinct."""
    g = G(p)
    base, var = split_name(p)
    words = base.split()
    mc = code(p)
    if mc and (mc.lower() in base.lower() or var.lower().startswith(mc.lower())):
        mc = ""
    kw = f" | {g['title']}"
    v = f" – {var}" if var else ""
    # Keep, in order of importance: keyword, colour, model code, then as much name as fits.
    for tail in ((f" {mc}" if mc else "") + v + kw, v + kw, kw):
        ws = list(words)
        while px(" ".join(ws) + tail) > TITLE_PX - 5 and len(ws) > 1:
            ws.pop()
        t = " ".join(ws) + tail
        # One word of name is enough when a model code or variant follows it.
        if px(t) <= TITLE_PX - 5 and (len(ws) >= 2 or tail != kw):
            return t
    return t


def meta_description(p, price_text, limit=158):
    """Keyword phrase, colour or model, price, delivery; payment if it fits."""
    base, var = split_name(p)
    c = colour(p)
    ph = _phrase(p)
    mc = code(p)
    which = (f", in {c.lower()}" if c else (f", model {var}" if var else "")) + (f" ({mc})" if mc and c else "")
    lead = ph[0].upper() + ph[1:] + which
    if not c:
        # No colour to tell listings apart: lead with the product's own name.
        short = " ".join(base.split()[:7])
        lead = f"{short}: {ph}{which}"
    s = f"{lead}. {price_text}Free NZ delivery in 7 to 10 days."
    for extra in (" Pay by card, Apple Pay, Google Pay or PayPal.", " Pay by card or PayPal."):
        if len(s + extra) <= limit:
            return s + extra
    if len(s) > limit:
        s = f"{lead}. {price_text}Free NZ delivery."
    return s


def description_html(p, pack_text=""):
    g, fs = G(p), features(p)
    base, var = split_name(p)
    c = colour(p)
    ph = _phrase(p, 3)
    art = "a pair of" if g["noun"].endswith("gloves") else ("an" if ph[0] in "aeiouAEIOU" else "a")
    lead = (f"<p>The <strong>{esc(base)}</strong>{' in ' + esc(c.lower()) if c else ''} is "
            f"{art} {esc(ph)}. {esc(g['intro'])}</p>")
    facts = [f[0].upper() + f[1:] for f in fs]
    for k, label in (("Material", "Material"), ("Nylon Type", "Fabric"), ("Dimensions", "Size"),
                     ("Size", "Size"), ("Weight", "Weight"), ("Capacity", "Capacity"),
                     ("Feature", "Also"), ("Function", "Use")):
        v = spec(p, k)
        if v and not (k == "Size" and spec(p, "Dimensions")):
            facts.append(f"{label}: {v}")
    if colours_available(p):
        facts.append("Available in " + _join(colours_available(p)).lower() + " (see the photo for this listing)")
    if var and var not in COLOURS:
        facts.append(f"Model: {var}")
    out = [lead]
    if facts:
        out.append("<h3>Features</h3><ul>" + "".join(f"<li>{esc(f)}</li>" for f in facts) + "</ul>")
    out.append("<h3>Good for</h3><ul>" + "".join(f"<li>{esc(u)}</li>" for u in g["uses"]) + "</ul>")
    out.append(f"<p>{esc(g['notes'])}</p>")
    if pack_text:
        out.append(f"<p>{pack_text}</p>")
    return "".join(out)


# Department pages: title, heading, meta description and intro, led by the
# searches each department answers.
DEPTS = {
 "Apparel": dict(
    title="Tactical Gloves NZ: Motorcycle, Cycling & Work Gloves",
    h1="Tactical, Motorcycle & Cycling Gloves",
    desc="Tactical gloves, motorcycle gloves, cycling gloves, fingerless and winter gloves, plus tactical "
         "belts. Shop online in NZ with free delivery in 7 to 10 days.",
    lede="Gloves for every job: <strong>tactical gloves</strong> for grip and dexterity, "
         "<strong>motorcycle gloves</strong> with knuckle protection, breathable <strong>cycling gloves</strong>, "
         "<strong>fingerless gloves</strong> for shooting and fine work, and warmer <strong>winter gloves</strong>. "
         "Most come in several colours, many with touchscreen fingertips. Free delivery anywhere in New Zealand."),
 "Bags": dict(
    title="MOLLE Pouches & Tactical Bags NZ",
    h1="MOLLE Pouches, Tactical Bags & Waist Packs",
    desc="MOLLE pouches, magazine pouches, first aid pouches, radio and EDC pouches, tactical waist bags, "
         "sling bags and backpacks. Free NZ delivery in 7 to 10 days.",
    lede="Build your loadout: <strong>MOLLE pouches</strong> for packs, belts and vests, "
         "<strong>magazine pouches</strong>, <strong>first aid pouches</strong>, <strong>radio pouches</strong> and "
         "<strong>EDC pouches</strong>, plus <strong>tactical waist bags</strong>, sling bags and a "
         "<strong>tactical backpack</strong>. For hunting, tramping, airsoft and everyday carry, delivered free "
         "across New Zealand."),
 "Hunting Accessories": dict(
    title="Rifle Bipods & Hunting Accessories NZ",
    h1="Rifle Bipods & Hunting Accessories",
    desc="Rifle bipods from 6 to 27 inches, carbon and M-Lok bipods, drop leg platforms, shemaghs and "
         "hunting accessories. Free NZ delivery in 7 to 10 days.",
    lede="Steady your shot with a <strong>rifle bipod</strong>: aluminium models from 6 to 27 inches, a "
         "lightweight <strong>carbon fibre bipod</strong> and an <strong>M-Lok bipod</strong>. Plus drop leg "
         "platforms, helmet covers, MOLLE connectors and a cotton <strong>shemagh</strong>. Hunting accessories "
         "delivered free anywhere in New Zealand."),
}


def families(products):
    """{sku: family id} for products sold in more than one colour."""
    fam = {}
    for p in products:
        fam.setdefault((split_name(p)[0], p["group"]), []).append(p)
    out = {}
    for (base, grp), ps in fam.items():
        if len(ps) > 1 and all(colour(x) for x in ps):
            fid = code(ps[0]) or re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-")[:40]
            for x in ps:
                out[x["sku"]] = (fid, base, [y["sku"] for y in ps])
    return out


def alt(p):
    return f"{p['name']} – {G(p)['kw']}"


def check(products):
    """Every product needs a group; say which do not."""
    missing = [p["sku"] for p in products if not p.get("group")]
    if missing:
        print(f"  ! {len(missing)} products have no keyword group (department default used): "
              + ", ".join(missing[:10]))
