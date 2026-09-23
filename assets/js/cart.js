/* Magnum Sports cart. Built from _build/cart.js by p_shop.py — edit that file,
   not assets/js/cart.js, which is overwritten on every build.

   The cart lives in this browser only (localStorage). Checkout does not take
   payment: it composes an order request and hands it to the customer's email
   app, and the shop replies to confirm stock and payment. Prices and
   names always come from the catalogue baked in below, never from storage. */
(function () {
  "use strict";
  var CAT = {"hunters-pack-4pc":{"name":"4 Piece Hunters Pack","price":"109.99"},"track-pant-5to9":{"name":"5 TO 9 Track Pant","price":"109.99"},"wide-brim-hat-360":{"name":"360° Wide Brim Hat","price":"49.99"},"wide-brim-hat-360-heavy":{"name":"360° Wide Brim Hat — Heavy","price":"59.99"},"petram-pt-mag933-fde":{"name":"M-Lok Bipod M-Lok Mount Foldable Adjustable 6061 Aluminum — Flat Dark Earth","price":"296.94"},"petram-pt-mag933-fde-atkrwv":{"name":"M-Lok Bipod M-Lok Mount Foldable Adjustable 6061 Aluminum — Flat Dark Earth (PT-MAG933-FDE)","price":"296.94"},"petram-ve-75-acc-15":{"name":"Tactical Built-in Triple 7.62 Mag Pouch Molle Pouch","price":"50.22"},"petram-ve-75-acc-14":{"name":"Tactical Built-in Triple 5.56 Mag Pouch Molle Pouch","price":"50.22"},"petram-mg-116":{"name":"Lightweight Mag Pouch Elastic Triple Magazine Pouch 5.56 7.62","price":"78.60"},"petram-mg-115":{"name":"Tactical Mag Pouch Lightweight Elastic Double 5.56/7.62 Mag","price":"58.95"},"petram-mg-114":{"name":"Lightweight Elastic Camo 5.56 Tactical Molle Pouch","price":"39.30"},"petram-mg-74":{"name":"Tactical Multifunctional Full Size Mag Pouch Tiger Stripe","price":"98.25"},"petram-mg-f-01":{"name":"Fast Tactical Multifunctional Single 9mm Mag Pouch Molle Pouch","price":"50.22"},"petram-mg-f-15":{"name":"Fast Tactical Low Profile Single 7.62 Mag Pouch Molle 762","price":"52.40"},"petram-mg-f-04":{"name":"Fast Tactical Double 9mm Molle Expandable Multifunctional Pouch","price":"52.40"},"petram-mg-f-02":{"name":"Fast Tactical Single 9mm Magazine Pouch Quick Drain Molle Pouch","price":"41.48"},"petram-gp-08":{"name":"Tactical Multifunctional Grenade Pouch","price":"48.04"},"petram-gp-10":{"name":"Tactical Grenade Pouch Multifunctional Camo Grenade Carrier","price":"43.67"},"petram-mg-f-06":{"name":"Tactical Low Profile 9mm 5.56 Combo Molle Quick Release Pouch","price":"89.52"},"petram-mg-49":{"name":"Tactical Multi-Functional 5.56 Mag Pouch Tiger Stripe Molle","price":"52.40"},"petram-ve-74-acc-02":{"name":"Tactical Multifunctional 4-Mag Pouch Mk4 Chest Rig Insert — VE-74-ACC-02","price":"37.12"},"petram-mg-48":{"name":"Tactical Multi-Functional 9mm Single Molle Tiger Stripe","price":"28.38"},"petram-tk-acc-01":{"name":"Fast Helmet Counterweight Pouch","price":"37.12"},"petram-dj-101":{"name":"Tactical Triple Quick Draw Functional Pouch Short Tiger Style","price":"51.09"},"petram-aa-044-bk":{"name":"360 Degree Rotatable Tactical Expandable Baton Holder","price":"26.20"},"petram-dj-028":{"name":"18 Rounds 12gauge Shell Pouch Tactical Outdoor Hunting","price":"24.02"},"petram-mg-34":{"name":"Tactical Mag Pouch 5.56 7.62 Nylon Soft Shell Molle Elastic","price":"34.93"},"petram-aa-019-bk":{"name":"360° Rotatable Tactical Expandable Stick Pouch ABS Material","price":"21.83"},"petram-ve-74-acc-03":{"name":"Tactical Multifunctional 4-Mag Pouch Mk4 Chest Rig Insert — VE-74-ACC-03","price":"37.12"},"petram-qt-030":{"name":"Tactical Mls15/18 Black Nylon Quick Release Mounting Plate Set","price":"56.77"},"petram-lb-small-radio-pouch":{"name":"Tactical Multi Function Molle Radio Pouch Outdoor EDC Tool Bag","price":"13.10"},"petram-br-134":{"name":"Tactical Single Pouch Outdoor Vest Molle Accessory Pouch CS","price":"13.10"},"petram-zp-bb-sand-bag":{"name":"Tactical Fix Support Bracket Shooting Rest Sand Bag Bb Sand Bag","price":"15.28"},"petram-zp-6-2-combination-tactical-cheek-rest-cover":{"name":"Tactical 6+2 Combination Cheek Rest Cover 8 Holes Universal","price":"19.65"},"petram-8-holes-cheek-rest-pouch":{"name":"Tactical Multi Function Cheek Rest Pouch 8 Holes Wrist Storage","price":"15.28"},"petram-eva-pad":{"name":"Tactical Vest Inner Liner Foam Shock Absorbing Plate Outdoor","price":"15.28"},"petram-gj-001":{"name":"Tactical Plastic Multi Hole Connector Adapter Outdoor","price":"39.30"},"petram-mg-35":{"name":"Tactical 9mm Magazine Pouch Soft Shell Elastic Mag Holder Molle","price":"32.23"},"petram-wj-001":{"name":"Tactical Shemagh Scarf 110X110cm Cotton Outdoor Large Square","price":"30.22"},"petram-lb-23":{"name":"Tactical Molle Mini Utility Pouch EDC Cigarette Card Tool","price":"14.15"},"petram-lm-06":{"name":"Tactical Molle Crossbody Bag Outdoor Sports Multifunctional","price":"40.35"},"petram-lb-122":{"name":"Tactical Molle First Aid Pouch Outdoor Medical Storage","price":"40.35"},"petram-lm-10":{"name":"Tactical Molle Waist Bag Outdoor Multifunctional Camo Fanny","price":"38.25"},"petram-lb-03":{"name":"Tactical Molle Pouch Outdoor Multifunctional EDC Tool Pouch","price":"26.20"},"petram-lb-58":{"name":"Tactical Molle EMT Medical Pouch Detachable Insert Outdoor","price":"38.25"},"petram-lb-124":{"name":"Tactical Molle Crossbody Pouch Outdoor Multifunctional EDC Cell","price":"40.35"},"petram-lb-41":{"name":"Tactical Molle Utility Pouch Outdoor Multifunctional EDC Tool","price":"24.19"},"petram-lb-06":{"name":"Tactical Molle Crossbody Bag Outdoor Multifunctional EDC Cell","price":"40.35"},"petram-br-d1":{"name":"Molle Mag Pouch 1000d Nylon 9mm Mag Holder Tactical Accessory","price":"19.65"},"petram-lb-triple-combo-pouch":{"name":"Triple Mag Pouch Set Magazine Pouch Molle Vest Accessory Bag","price":"43.67"},"petram-lb-132":{"name":"Flashlight Pouch 1000d Nylon Pouch Torch Holder Outdoor","price":"17.47"},"petram-lb-10-piece-set":{"name":"10 Piece Tactical Duty Belt Set Security Patrol Training","price":"78.60"},"petram-lb":{"name":"Tactical Mag Pouch Single Molle Storage Magazine Pouch Outdoor","price":"21.83"},"petram-lb-28":{"name":"Knife Sheath Tactical Pouch Lighter Holder 600d Polyester Molle","price":"15.28"},"petram-lb-39":{"name":"Multifunctional EDC Tool Bag Pouch 600d Polyester Large Storage","price":"28.38"},"petram-br-yb01":{"name":"First Aid Kit Small EMT Medical Pouch Molle Outdoor Emergency","price":"21.83"},"petram-lb-tornado":{"name":"Leg Pouch Adjustable Thigh Carrier Quick Release Camouflage","price":"30.57"},"petram-lb-121":{"name":"Medical Pouch First Aid Kit Pouch","price":"39.74"},"petram-br-135":{"name":"Double Tactical Mag Pouch Molle Vest Accessory Bag CS Outdoor","price":"17.47"},"petram-br-136":{"name":"Triple Tactical Mag Pouch Molle Vest Accessory Bag Outdoor","price":"24.02"},"petram-lb-130":{"name":"Tactical Molle Utility Pouch Outdoor Multifunctional EDC First","price":"24.19"},"petram-lb-09":{"name":"Tactical Molle Utility Pouch Outdoor Multifunctional EDC","price":"30.22"},"petram-lb-07":{"name":"Tactical Molle Attachment Pouch Outdoor EDC Storage Waist Bag","price":"20.17"},"petram-lm201":{"name":"Tactical 3p Backpack Camouflage Outdoor Multifunctional Travel","price":"72.58"},"petram-lb-37":{"name":"Tactical Outdoor Sling Chest Bag Multifunctional Crossbody","price":"48.38"},"petram-rb-21":{"name":"Tactical Multifunctional Waist Bag","price":"44.37"},"petram-lb-01":{"name":"Tactical Camouflage Utility Waist Pouch Multifunctional Molle","price":"16.16"},"petram-d-2":{"name":"Tactical 6 Inch Molle Phone Pouch Multifunctional Outdoor","price":"12.05"},"petram-d-1":{"name":"Tactical 5 Inch Molle Phone Pouch Multifunctional Outdoor","price":"11.09"},"petram-v8-b":{"name":"V8 Bipod 360 Degrees Tilt Hunting Bipod 6-9 Inches Shooting — V8-B","price":"100.44"},"petram-v8-t":{"name":"V8 Bipod 360 Degrees Tilt Hunting Bipod 6-9 Inches Shooting — V8-T","price":"100.44"},"petram-6in11mmb":{"name":"6-9 Inches Bipod Aluminum Alloy Hunting Bipod Retractable Metal","price":"78.60"},"petram-27inb":{"name":"21-27 Inches Retractable All Metal Aluminum Alloy Bipod","price":"191.27"},"petram-bt-09":{"name":"Carbon Fiber 6-9 Inch Bipod","price":"116.86"},"petram-bt-07":{"name":"6-9 Inch Bipod","price":"137.12"},"petram-sr-5-b":{"name":"V9 Bipod Hunting Bipod 6-9 Inches Shooting Bipod Adjustable — SR-5-B","price":"100.44"},"petram-sr-5-t":{"name":"V9 Bipod Hunting Bipod 6-9 Inches Shooting Bipod Adjustable — SR-5-T","price":"100.44"},"petram-bt-11":{"name":"9-13 Inches Retractable All Metal Aluminum Alloy Bipod","price":"155.02"},"petram-13inb":{"name":"13-21 Inches Retractable All Metal Aluminum Alloy Bipod","price":"157.21"},"petram-9inb":{"name":"9-13 Inches Pivot Retractable Rotating Bipod","price":"155.02"},"petram-a2-blk":{"name":"Full-Finger Touchscreen Outdoor Tactical Work Hiking Gloves A2 — Black","price":"66.38"},"petram-001-blk":{"name":"Thick Full-Finger Winter Cycling and Ski Outdoor Gloves Touch — Black","price":"21.83"},"petram-001-gry":{"name":"Thick Full-Finger Winter Cycling and Ski Outdoor Gloves Touch — Grey","price":"21.83"},"petram-001-nvb":{"name":"Thick Full-Finger Winter Cycling and Ski Outdoor Gloves Touch — Navy","price":"21.83"},"petram-002-blk":{"name":"Outdoor Winter Windproof Waterproof Anti-Slip Sports Gloves — Black","price":"26.20"},"petram-002-rgg":{"name":"Outdoor Winter Windproof Waterproof Anti-Slip Sports Gloves — Ranger Green","price":"26.20"},"petram-002-mtc":{"name":"Outdoor Winter Windproof Waterproof Anti-Slip Sports Gloves — Multicam","price":"26.20"},"petram-a2-rgg":{"name":"Full-Finger Touchscreen Outdoor Tactical Work Hiking Gloves A2 — Ranger Green","price":"66.38"},"petram-a2-snd":{"name":"Full-Finger Touchscreen Outdoor Tactical Work Hiking Gloves A2 — Sand","price":"66.38"},"petram-a6-blk":{"name":"Full-Finger Anti-Scratch Touchscreen Outdoor Tactical Work — Black","price":"39.30"},"petram-a6-rgg":{"name":"Full-Finger Anti-Scratch Touchscreen Outdoor Tactical Work — Ranger Green","price":"39.30"},"petram-a6-snd":{"name":"Full-Finger Anti-Scratch Touchscreen Outdoor Tactical Work — Sand","price":"39.30"},"petram-a9-blk":{"name":"Outdoor Cycling Climbing Gloves Multi-Functional Tactical — Black","price":"43.67"},"petram-a9-rgg":{"name":"Outdoor Cycling Climbing Gloves Multi-Functional Tactical — Ranger Green","price":"43.67"},"petram-a9-cmb":{"name":"Outdoor Cycling Climbing Gloves Multi-Functional Tactical — A9-CMB","price":"43.67"},"petram-a9-cmg":{"name":"Outdoor Cycling Climbing Gloves Multi-Functional Tactical — A9-CMG","price":"43.67"},"petram-a9-cmgn":{"name":"Outdoor Cycling Climbing Gloves Multi-Functional Tactical — A9-CMGN","price":"43.67"},"petram-a9-cmr":{"name":"Outdoor Cycling Climbing Gloves Multi-Functional Tactical — A9-CMR","price":"43.67"},"petram-a9-mtc":{"name":"Outdoor Cycling Climbing Gloves Multi-Functional Tactical — Multicam","price":"43.67"},"petram-a9-wfg":{"name":"Outdoor Cycling Climbing Gloves Multi-Functional Tactical — A9-WFG","price":"43.67"},"petram-a17-blk":{"name":"Outdoor Motorcycle Gloves Climbing Gloves Anti-Slip Tool — Black","price":"61.14"},"petram-a17-rgg":{"name":"Outdoor Motorcycle Gloves Climbing Gloves Anti-Slip Tool — Ranger Green","price":"61.14"},"petram-a17-wfb":{"name":"Outdoor Motorcycle Gloves Climbing Gloves Anti-Slip Tool — A17-WFB","price":"61.14"},"petram-a17-lcf":{"name":"Outdoor Motorcycle Gloves Climbing Gloves Anti-Slip Tool — A17-LCF","price":"61.14"},"petram-a17-dcf":{"name":"Outdoor Motorcycle Gloves Climbing Gloves Anti-Slip Tool — A17-DCF","price":"61.14"},"petram-a17-jcf":{"name":"Outdoor Motorcycle Gloves Climbing Gloves Anti-Slip Tool — A17-JCF","price":"61.14"},"petram-a20-blk":{"name":"Tactical Gloves Anti-Slip Outdoor Cycling Fitness Protection — Black","price":"52.40"},"petram-a20-snd":{"name":"Tactical Gloves Anti-Slip Outdoor Cycling Fitness Protection — Sand","price":"52.40"},"petram-a20-rgg":{"name":"Tactical Gloves Anti-Slip Outdoor Cycling Fitness Protection — Ranger Green","price":"52.40"},"petram-a24-blk":{"name":"Outdoor Tactical Warm Gloves Windproof Waterproof Anti-Slip — Black","price":"69.87"},"petram-a24-snd":{"name":"Outdoor Tactical Warm Gloves Windproof Waterproof Anti-Slip — Sand","price":"69.87"},"petram-a24-rgg":{"name":"Outdoor Tactical Warm Gloves Windproof Waterproof Anti-Slip — Ranger Green","price":"69.87"},"petram-a24-mtc":{"name":"Outdoor Tactical Warm Gloves Windproof Waterproof Anti-Slip — Multicam","price":"69.87"},"petram-a26-blk":{"name":"Breathable Full-Finger Adult Gloves — Black","price":"84.72"},"petram-a26-snd":{"name":"Breathable Full-Finger Adult Gloves — Sand","price":"84.72"},"petram-a26-rgg":{"name":"Breathable Full-Finger Adult Gloves — Ranger Green","price":"84.72"},"petram-a27-blk":{"name":"Outdoor Tactical Gloves Full-Finger Touchscreen Gloves — Black","price":"72.49"},"petram-a27-snd":{"name":"Outdoor Tactical Gloves Full-Finger Touchscreen Gloves — Sand","price":"72.49"},"petram-a27-rgg":{"name":"Outdoor Tactical Gloves Full-Finger Touchscreen Gloves — Ranger Green","price":"72.49"},"petram-a27-gry":{"name":"Outdoor Tactical Gloves Full-Finger Touchscreen Gloves — Grey","price":"72.49"},"petram-a27-mtc":{"name":"Outdoor Tactical Gloves Full-Finger Touchscreen Gloves — Multicam","price":"72.49"},"petram-a28-blk":{"name":"Breathable Full-Finger Uni-Sex Gloves — Black","price":"84.72"},"petram-a28-snd":{"name":"Breathable Full-Finger Uni-Sex Gloves — Sand","price":"84.72"},"petram-a28-rgg":{"name":"Breathable Full-Finger Uni-Sex Gloves — Ranger Green","price":"84.72"},"petram-a30-blk":{"name":"Outdoor Camo Sports Tactical Gloves Cycling Anti-Slip — Black","price":"72.49"},"petram-a30-snd":{"name":"Outdoor Camo Sports Tactical Gloves Cycling Anti-Slip — Sand","price":"72.49"},"petram-a30-rgg":{"name":"Outdoor Camo Sports Tactical Gloves Cycling Anti-Slip — Ranger Green","price":"72.49"},"petram-a30-lcf":{"name":"Outdoor Camo Sports Tactical Gloves Cycling Anti-Slip — A30-LCF","price":"72.49"},"petram-a30-dcf":{"name":"Outdoor Camo Sports Tactical Gloves Cycling Anti-Slip — A30-DCF","price":"72.49"},"petram-a30-jcf":{"name":"Outdoor Camo Sports Tactical Gloves Cycling Anti-Slip — A30-JCF","price":"72.49"},"petram-a50-blk":{"name":"Autumn Winter Tactical Gloves Shockproof Shooting Gloves — Black","price":"78.60"},"petram-a50-snd":{"name":"Autumn Winter Tactical Gloves Shockproof Shooting Gloves — Sand","price":"78.60"},"petram-a50-rgg":{"name":"Autumn Winter Tactical Gloves Shockproof Shooting Gloves — Ranger Green","price":"78.60"},"petram-a72-blk":{"name":"Outdoor off-Road Motorcycle Gloves Hard Shell Anti-Fall — Black","price":"62.45"},"petram-a72-nog":{"name":"Outdoor off-Road Motorcycle Gloves Hard Shell Anti-Fall — A72-NOG","price":"62.45"},"petram-a72-red":{"name":"Outdoor off-Road Motorcycle Gloves Hard Shell Anti-Fall — Red","price":"62.45"},"petram-b7-blk":{"name":"Rubber Full-Finger Sports Gloves — Black","price":"26.20"},"petram-b7-snd":{"name":"Rubber Full-Finger Sports Gloves — Sand","price":"26.20"},"petram-b7-rgg":{"name":"Rubber Full-Finger Sports Gloves — Ranger Green","price":"26.20"},"petram-b8-blk":{"name":"Summer Outdoor Sports Cycling Tactical Gloves Mountaineering — Black","price":"61.14"},"petram-b8-snd":{"name":"Summer Outdoor Sports Cycling Tactical Gloves Mountaineering — Sand","price":"61.14"},"petram-b8-rgg":{"name":"Summer Outdoor Sports Cycling Tactical Gloves Mountaineering — Ranger Green","price":"61.14"},"petram-b10-blk":{"name":"Outdoor Full-Finger Touchscreen Tactical Gloves — Black","price":"61.14"},"petram-b10-snd":{"name":"Outdoor Full-Finger Touchscreen Tactical Gloves — Sand","price":"61.14"},"petram-b10-rgg":{"name":"Outdoor Full-Finger Touchscreen Tactical Gloves — Ranger Green","price":"61.14"},"petram-b22-blk":{"name":"Outdoor Motorcycle Bike Gloves — Black","price":"96.07"},"petram-b22-snd":{"name":"Outdoor Motorcycle Bike Gloves — Sand","price":"96.07"},"petram-b22-rgg":{"name":"Outdoor Motorcycle Bike Gloves — Ranger Green","price":"96.07"},"petram-b26-blk":{"name":"Special Forces Tactical Gloves Anti-Slip Touchscreen Compatible — Black","price":"74.24"},"petram-b26-snd":{"name":"Special Forces Tactical Gloves Anti-Slip Touchscreen Compatible — Sand","price":"74.24"},"petram-b26-rgg":{"name":"Special Forces Tactical Gloves Anti-Slip Touchscreen Compatible — Ranger Green","price":"74.24"},"petram-b26-lcf":{"name":"Special Forces Tactical Gloves Anti-Slip Touchscreen Compatible — B26-LCF","price":"74.24"},"petram-b26-dcf":{"name":"Special Forces Tactical Gloves Anti-Slip Touchscreen Compatible — B26-DCF","price":"74.24"},"petram-b26-jcf":{"name":"Special Forces Tactical Gloves Anti-Slip Touchscreen Compatible — B26-JCF","price":"74.24"},"petram-b28-blk":{"name":"Outdoor Sports Tactical Gloves Hard Shell Full-Finger — Black","price":"82.97"},"petram-b28-snd":{"name":"Outdoor Sports Tactical Gloves Hard Shell Full-Finger — Sand","price":"82.97"},"petram-b28-rgg":{"name":"Outdoor Sports Tactical Gloves Hard Shell Full-Finger — Ranger Green","price":"82.97"},"petram-b31-blk":{"name":"Sports Gloves — Black","price":"78.60"},"petram-b31-snd":{"name":"Sports Gloves — Sand","price":"78.60"},"petram-b31-rgg":{"name":"Sports Gloves — Ranger Green","price":"78.60"},"petram-b31-lcf":{"name":"Sports Gloves — B31-LCF","price":"78.60"},"petram-b31-dcf":{"name":"Sports Gloves — B31-DCF","price":"78.60"},"petram-b33-blk":{"name":"Full-Finger Sports Protective Gloves — Black","price":"78.60"},"petram-b33-snd":{"name":"Full-Finger Sports Protective Gloves — Sand","price":"78.60"},"petram-b33-rgg":{"name":"Full-Finger Sports Protective Gloves — Ranger Green","price":"78.60"},"petram-b33-lcf":{"name":"Full-Finger Sports Protective Gloves — B33-LCF","price":"78.60"},"petram-b33-dcf":{"name":"Full-Finger Sports Protective Gloves — B33-DCF","price":"78.60"},"petram-b33-gry":{"name":"Full-Finger Sports Protective Gloves — Grey","price":"78.60"},"petram-b33-jcf":{"name":"Full-Finger Sports Protective Gloves — B33-JCF","price":"78.60"},"petram-b36-f-blk":{"name":"Anti-Cut Tactical Gloves — Black","price":"117.90"},"petram-b36-f-snd":{"name":"Anti-Cut Tactical Gloves — Sand","price":"117.90"},"petram-b36-f-rgg":{"name":"Anti-Cut Tactical Gloves — Ranger Green","price":"117.90"},"petram-b36-f-mtc":{"name":"Anti-Cut Tactical Gloves — Multicam","price":"117.90"},"petram-b39-blk":{"name":"Sports Full-Finger Protective Gloves — Black","price":"82.97"},"petram-b39-snd":{"name":"Sports Full-Finger Protective Gloves — Sand","price":"82.97"},"petram-b39-rgg":{"name":"Sports Full-Finger Protective Gloves — Ranger Green","price":"82.97"},"petram-b39-mtc":{"name":"Sports Full-Finger Protective Gloves — Multicam","price":"82.97"},"petram-b55-blk":{"name":"Outdoor Cycling Gloves Mountain Climbing Sports Protective Gear — Black","price":"50.22"},"petram-b55-snd":{"name":"Outdoor Cycling Gloves Mountain Climbing Sports Protective Gear — Sand","price":"50.22"},"petram-b55-rgg":{"name":"Outdoor Cycling Gloves Mountain Climbing Sports Protective Gear — Ranger Green","price":"50.22"},"petram-b55-dcf":{"name":"Outdoor Cycling Gloves Mountain Climbing Sports Protective Gear — B55-DCF","price":"50.22"},"petram-b55-jcf":{"name":"Outdoor Cycling Gloves Mountain Climbing Sports Protective Gear — B55-JCF","price":"50.22"},"petram-b56-blk":{"name":"Half-Finger Tactical Gloves — Black","price":"78.60"},"petram-b56-snd":{"name":"Half-Finger Tactical Gloves — Sand","price":"78.60"},"petram-b56-rgg":{"name":"Half-Finger Tactical Gloves — Ranger Green","price":"78.60"},"petram-b56-mtc":{"name":"Half-Finger Tactical Gloves — Multicam","price":"78.60"},"petram-b58-blk":{"name":"Half-Finger Tactical Gloves Hard Shell Sports Outdoor Anti-Slip — Black","price":"78.60"},"petram-b58-rgg":{"name":"Half-Finger Tactical Gloves Hard Shell Sports Outdoor Anti-Slip — Ranger Green","price":"78.60"},"petram-b58-mtc":{"name":"Half-Finger Tactical Gloves Hard Shell Sports Outdoor Anti-Slip — Multicam","price":"78.60"},"petram-b60-blk":{"name":"Outdoor Sports Camouflage Tactical Gloves — Black","price":"75.11"},"petram-b60-snd":{"name":"Outdoor Sports Camouflage Tactical Gloves — Sand","price":"75.11"},"petram-b60-rgg":{"name":"Outdoor Sports Camouflage Tactical Gloves — Ranger Green","price":"75.11"},"petram-b60-mtc":{"name":"Outdoor Sports Camouflage Tactical Gloves — Multicam","price":"75.11"},"petram-b61-blk":{"name":"Outdoor Sports Gloves — Black","price":"87.34"},"petram-b61-snd":{"name":"Outdoor Sports Gloves — Sand","price":"87.34"},"petram-b61-rgg":{"name":"Outdoor Sports Gloves — Ranger Green","price":"87.34"},"petram-b62-blk":{"name":"Full-Finger Gloves — Black","price":"96.07"},"petram-b62-snd":{"name":"Full-Finger Gloves — Sand","price":"96.07"},"petram-b62-rgg":{"name":"Full-Finger Gloves — Ranger Green","price":"96.07"},"petram-b62-mtc":{"name":"Full-Finger Gloves — Multicam","price":"96.07"},"petram-b66-blk":{"name":"Tactical Gloves Outdoor Anti-Slip Touchscreen Cycling Sports — Black","price":"100.44"},"petram-b66-snd":{"name":"Tactical Gloves Outdoor Anti-Slip Touchscreen Cycling Sports — Sand","price":"100.44"},"petram-b66-rgg":{"name":"Tactical Gloves Outdoor Anti-Slip Touchscreen Cycling Sports — Ranger Green","price":"100.44"},"petram-b66-mtc":{"name":"Tactical Gloves Outdoor Anti-Slip Touchscreen Cycling Sports — Multicam","price":"100.44"},"petram-b79-blk":{"name":"Touchscreen Tactical Riding Gloves — Black","price":"98.69"},"petram-b79-snd":{"name":"Touchscreen Tactical Riding Gloves — Sand","price":"98.69"},"petram-b79-rgg":{"name":"Touchscreen Tactical Riding Gloves — Ranger Green","price":"98.69"},"petram-b79-mtc":{"name":"Touchscreen Tactical Riding Gloves — Multicam","price":"98.69"},"petram-b80-blk":{"name":"Breathable Wear-Resistant Anti-Slip Multi-Functional Outdoor — Black","price":"98.69"},"petram-b80-snd":{"name":"Breathable Wear-Resistant Anti-Slip Multi-Functional Outdoor — Sand","price":"98.69"},"petram-b80-rgg":{"name":"Breathable Wear-Resistant Anti-Slip Multi-Functional Outdoor — Ranger Green","price":"98.69"},"petram-b80-mtc":{"name":"Breathable Wear-Resistant Anti-Slip Multi-Functional Outdoor — Multicam","price":"98.69"},"petram-b85-blk":{"name":"Tactical Protective Gloves — Black","price":"98.69"},"petram-b85-snd":{"name":"Tactical Protective Gloves — Sand","price":"98.69"},"petram-b85-rgg":{"name":"Tactical Protective Gloves — Ranger Green","price":"98.69"},"petram-b85-mtc":{"name":"Tactical Protective Gloves — Multicam","price":"98.69"},"petram-b99-blk":{"name":"Super Tech Tactical Gloves Anti-Slip Touchscreen Tactical — Black","price":"113.54"},"petram-b99-snd":{"name":"Super Tech Tactical Gloves Anti-Slip Touchscreen Tactical — Sand","price":"113.54"},"petram-b99-rgg":{"name":"Super Tech Tactical Gloves Anti-Slip Touchscreen Tactical — Ranger Green","price":"113.54"},"petram-blackhawk-blk":{"name":"Tactical Hawk Motorcycle Riding Gloves — Black","price":"47.16"},"petram-blackhawk-snd":{"name":"Tactical B-Hawk Motorcycle Riding Gloves","price":"47.16"},"petram-hawk-rgg":{"name":"Tactical Hawk Motorcycle Riding Gloves — Ranger Green","price":"47.16"},"petram-c5-blk":{"name":"Super Tech Tactical Gloves Cycling Gloves Outdoor Anti-Slip — Black","price":"74.24"},"petram-c5-snd":{"name":"Super Tech Tactical Gloves Cycling Gloves Outdoor Anti-Slip — Sand","price":"74.24"},"petram-c5-rgg":{"name":"Super Tech Tactical Gloves Cycling Gloves Outdoor Anti-Slip — Ranger Green","price":"74.24"},"petram-c5-mtc":{"name":"Super Tech Tactical Gloves Cycling Gloves Outdoor Anti-Slip — Multicam","price":"74.24"},"petram-c60-blk":{"name":"Tactical Gloves Adult Full-Finger Protective Anti-Fall — Black","price":"80.79"},"petram-c60-snd":{"name":"Tactical Gloves Adult Full-Finger Protective Anti-Fall — Sand","price":"80.79"},"petram-c60-rgg":{"name":"Tactical Gloves Adult Full-Finger Protective Anti-Fall — Ranger Green","price":"80.79"},"petram-c60-red":{"name":"Tactical Gloves Adult Full-Finger Protective Anti-Fall — Red","price":"80.79"},"petram-comp-blk":{"name":"Comprehensive Outdoor Half-Finger Adult Tactical Gloves — Black","price":"50.22"},"petram-comp-snd":{"name":"Comprehensive Outdoor Half-Finger Adult Tactical Gloves — Sand","price":"50.22"},"petram-comp-rgg":{"name":"Comprehensive Outdoor Half-Finger Adult Tactical Gloves — Ranger Green","price":"50.22"},"petram-l26-blk":{"name":"Outdoor Cycling Anti-Slip Hard Shell Touchscreen Gloves Durable — Black","price":"74.24"},"petram-l26-snd":{"name":"Outdoor Cycling Anti-Slip Hard Shell Touchscreen Gloves Durable — Sand","price":"74.24"},"petram-l26-rgg":{"name":"Outdoor Cycling Anti-Slip Hard Shell Touchscreen Gloves Durable — Ranger Green","price":"74.24"},"petram-n9-blk":{"name":"Half-Finger Cycling Gloves Outdoor Sports Shock Absorption — Black","price":"30.57"},"petram-n9-gry":{"name":"Half-Finger Cycling Gloves Outdoor Sports Shock Absorption — Grey","price":"30.57"},"petram-n9-red":{"name":"Half-Finger Cycling Gloves Outdoor Sports Shock Absorption — Red","price":"30.57"},"petram-n9-blu":{"name":"Half-Finger Cycling Gloves Outdoor Sports Shock Absorption — Blue","price":"30.57"},"petram-n10-blk":{"name":"Super Technician Full-Finger Sports Outdoor Motorcycle Tactical — Black","price":"69.87"},"petram-n10-snd":{"name":"Super Technician Full-Finger Sports Outdoor Motorcycle Tactical — Sand","price":"69.87"},"petram-n10-rgg":{"name":"Super Technician Full-Finger Sports Outdoor Motorcycle Tactical — Ranger Green","price":"69.87"},"petram-n10-mtc":{"name":"Super Technician Full-Finger Sports Outdoor Motorcycle Tactical — Multicam","price":"69.87"},"petram-n11-wht":{"name":"Outdoor Cycling Gloves Touchscreen Anti-Slip Breathable — White","price":"26.20"},"petram-n11-blu":{"name":"Outdoor Cycling Gloves Touchscreen Anti-Slip Breathable — Blue","price":"26.20"},"petram-n11-red":{"name":"Outdoor Cycling Gloves Touchscreen Anti-Slip Breathable — Red","price":"26.20"},"petram-n15-wht":{"name":"Outdoor Cycling Gloves Breathable Anti-Slip Shock-Absorbing — White","price":"26.20"},"petram-n15-blu":{"name":"Outdoor Cycling Gloves Breathable Anti-Slip Shock-Absorbing — Blue","price":"26.20"},"petram-n15-red":{"name":"Outdoor Cycling Gloves Breathable Anti-Slip Shock-Absorbing — Red","price":"26.20"},"petram-n19-blk":{"name":"Tactical Gloves 5.0 Riding Gloves Breathable Anti-Slip — Black","price":"96.07"},"petram-n19-snd":{"name":"Tactical Gloves 5.0 Riding Gloves Breathable Anti-Slip — Sand","price":"96.07"},"petram-n19-rgg":{"name":"Tactical Gloves 5.0 Riding Gloves Breathable Anti-Slip — Ranger Green","price":"96.07"},"petram-n21-blk":{"name":"Tactical Gloves Full Finger Touchscreen Outdoor Cycling Gloves — Black","price":"96.07"},"petram-n21-snd":{"name":"Tactical Gloves Full Finger Touchscreen Outdoor Cycling Gloves — Sand","price":"96.07"},"petram-n21-rgg":{"name":"Tactical Gloves Full Finger Touchscreen Outdoor Cycling Gloves — Ranger Green","price":"96.07"},"petram-n28-blk":{"name":"Outdoor Motorcycle Riding Gloves Anti-Slip Touchscreen Gloves — Black","price":"52.40"},"petram-n28-snd":{"name":"Outdoor Motorcycle Riding Gloves Anti-Slip Touchscreen Gloves — Sand","price":"52.40"},"petram-n28-rgg":{"name":"Outdoor Motorcycle Riding Gloves Anti-Slip Touchscreen Gloves — Ranger Green","price":"52.40"},"petram-n28-red":{"name":"Outdoor Motorcycle Riding Gloves Anti-Slip Touchscreen Gloves — Red","price":"52.40"},"petram-n28-wht":{"name":"Outdoor Motorcycle Riding Gloves Anti-Slip Touchscreen Gloves — White","price":"52.40"},"petram-n31-blk":{"name":"Protective Wear-Resistant Anti-Slip Tactical Gloves — Black","price":"87.34"},"petram-n31-snd":{"name":"Protective Wear-Resistant Anti-Slip Tactical Gloves — Sand","price":"87.34"},"petram-n31-rgg":{"name":"Protective Wear-Resistant Anti-Slip Tactical Gloves — Ranger Green","price":"87.34"},"petram-n32-blk":{"name":"Motorcycle Gloves Racing Bike Riders Anti-Fall Anti-Slip — Black","price":"48.04"},"petram-n32-gry":{"name":"Motorcycle Gloves Racing Bike Riders Anti-Fall Anti-Slip — Grey","price":"48.04"},"petram-n32-red":{"name":"Motorcycle Gloves Racing Bike Riders Anti-Fall Anti-Slip — Red","price":"48.04"},"petram-n32-snd":{"name":"Motorcycle Gloves Racing Bike Riders Anti-Fall Anti-Slip — Sand","price":"48.04"},"petram-n33-blk":{"name":"Super Technician Glove Man Tactical Gloves Spring and Autumn — Black","price":"78.60"},"petram-n33-snd":{"name":"Super Technician Glove Man Tactical Gloves Spring and Autumn — Sand","price":"78.60"},"petram-n33-rgg":{"name":"Super Technician Glove Man Tactical Gloves Spring and Autumn — Ranger Green","price":"78.60"},"petram-n33-wht":{"name":"Super Technician Glove Man Tactical Gloves Spring and Autumn — White","price":"78.60"},"petram-v9-ft":{"name":"V9 Split Bipod Hunting Bipod 6-8 Inches Adjustable Retractable — Black","price":"96.07"},"petram-v9-ft-tan":{"name":"V9 Split Bipod Hunting Bipod 6-8 Inches Adjustable Retractable — Tan","price":"96.07"},"petram-n38-blk":{"name":"Outdoor Sports Gloves Tactical Gloves Cycling Field Training — Black","price":"78.60"},"petram-n38-snd":{"name":"Outdoor Sports Gloves Tactical Gloves Cycling Field Training — Sand","price":"78.60"},"petram-n38-rgg":{"name":"Outdoor Sports Gloves Tactical Gloves Cycling Field Training — Ranger Green","price":"78.60"},"petram-n38-mtc":{"name":"Outdoor Sports Gloves Tactical Gloves Cycling Field Training — Multicam","price":"78.60"},"petram-n50-blk":{"name":"Tactical Gloves Half-Finger Sports Cycling Hiking Anti-Slip — Black","price":"65.50"},"petram-n50-snd":{"name":"Tactical Gloves Half-Finger Sports Cycling Hiking Anti-Slip — Sand","price":"65.50"},"petram-n50-rgg":{"name":"Tactical Gloves Half-Finger Sports Cycling Hiking Anti-Slip — Ranger Green","price":"65.50"},"petram-n77-blk":{"name":"Tactical Gloves Skeleton Style Motorcycle Riding Gloves — Black","price":"113.54"},"petram-n77-snd":{"name":"Tactical Gloves Skeleton Style Motorcycle Riding Gloves — Sand","price":"113.54"},"petram-n77-rgg":{"name":"Tactical Gloves Skeleton Style Motorcycle Riding Gloves — Ranger Green","price":"113.54"},"petram-n77-mtc":{"name":"Tactical Gloves Skeleton Style Motorcycle Riding Gloves — Multicam","price":"113.54"},"petram-custom":{"name":"Combined Outdoor Leg and Waist Carry Tool Pouch","price":"45.41"},"petram-custom-bfsfrt":{"name":"Eagle Model Outdoor Multi Function First Aid Storage Bag","price":"30.57"},"petram-custom-afyads":{"name":"Multi Functional 14-Hole Hook Loop Storage Patch","price":"21.83"},"petram-custom-tdcaif":{"name":"Compact Portable General Key Storage Waist Hanging Bag","price":"13.10"},"petram-custom-pzytkl":{"name":"Breathable Molle Back Support Waist Belt","price":"28.38"},"petram-custom-sdcgtm":{"name":"Slim Hidden Adjustable Universal Leg Sleeve Tool Pouch","price":"17.03"},"petram-custom-wfogpc":{"name":"Adjustable 30-Hole Camouflage Waist Strap Belt","price":"19.65"},"petram-custom-afcamf":{"name":"Portable Handheld Outdoor First Aid Survival Storage Bag","price":"30.57"},"petram-custom-wzjtaz":{"name":"Collapsible Foldable Sundry Storage Hanging Pouch","price":"11.35"},"petram-custom-pdjtdt":{"name":"Durable 25-Hole Hunting Special 12g Gear Storage Pouch","price":"22.71"},"petram-custom-cwnafg":{"name":"Versatile Multi Way Single Shoulder Crossbody Waist Carry Bag","price":"21.83"},"petram-custom-roytdg":{"name":"Stylish Camouflage EDC Coin Phone Waist Storage Pouch","price":"11.00"},"petram-custom-iohfvl":{"name":"Mini Simulated Molle Beer Bottle Protective Cover Vest","price":"22.71"},"petram-custom-ddwavq":{"name":"Elastic Adjustable Nylon Webbing Water Bottle Holder Pouch","price":"26.20"},"petram-custom-udjfcw":{"name":"Heavy Duty Tactical 18-Hole Storage Pouch","price":"21.83"},"petram-custom-doctws":{"name":"Single Radio Battery Power Bank Hanging Storage Bag","price":"13.10"},"petram-custom-jzsanh":{"name":"Mini Dual 9mm Flashlight Molle Vest Mounted Accessory Pouch","price":"13.10"},"petram-custom-nwctso":{"name":"Lightweight Wireless Radio Molle Storage Carry Pouch","price":"10.04"},"petram-custom-wzjaqu":{"name":"Solid Adjustable Dual Point Mission Carry Sling Strap Rope","price":"11.35"},"petram-custom-ufyfwz":{"name":"Ergonomic Adjustable Outdoor Leg Storage Carry Pouch","price":"48.04"},"petram-custom-jdntbv":{"name":"Waterproof Portable Molle Outdoor Medical Storage Bag","price":"30.57"},"petram-custom-fdcaxc":{"name":"Professional EMT First Aid Supply Molle Waist Accessory Bag","price":"22.71"},"petram-custom-dzvfcy":{"name":"Convenient Daily Medical Supply Waist Storage Pouch","price":"22.71"},"petram-lb-23-wfntwk":{"name":"Fashion Camouflage EDC Molle Sundry Storage Waist Pouch","price":"13.10"},"petram-custom-udkgjj":{"name":"Spacious Large Size Survival Knife Protective Sheath Tool Bag","price":"19.65"},"petram-custom-eznfcs":{"name":"Compact Small Size Survival Knife Protective Sheath Tool Bag","price":"17.03"},"petram-custom-szwghy":{"name":"Camouflage Waterproof Molle Medical Supply Storage Pouch","price":"19.65"},"petram-custom-rdyaxw":{"name":"Tough Tactical 9-Hole Multi Function Hunting Tool Storage Bag","price":"15.28"},"petram-custom-zdhgwj":{"name":"All Purpose Outdoor EDC Flashlight Medical Scissor Tourniquet","price":"11.35"},"petram-custom-tojfoa":{"name":"Reliable EMT Tourniquet Storage Sleeve Medical Scissor Hanging","price":"13.10"},"petram-custom-jozamf":{"name":"Innovative Style M4 Pullable Tactical Magazine Carrier Pouch","price":"17.03"},"petram-custom-kwygzv":{"name":"Special Revolver Molle Double Magazine Loader Pouch","price":"10.04"},"petram-custom-pdwtla":{"name":"Spacious Dual Large Screen 6 Inch Phone Waist Crossbody Carry","price":"26.20"},"petram-custom-rostbf":{"name":"Breathable Practical 095 Water Bottle Carrier Holder Pouch","price":"21.83"},"petram-custom-wfstpz":{"name":"Strong Nylon Multi Function Outdoor Tool Medical Scissor Pouch","price":"15.28"},"petram-custom-hzcgfa":{"name":"Flexible Rotatable 360 Degree Molle Webbing D Shape Buckle Hook","price":"5.68"},"petram-custom-boytxt":{"name":"Sturdy Wear Resistant 12-Hole Molle Accessory Waist Storage","price":"19.65"},"petram-custom-iohamr":{"name":"Adjustable Nylon Multi Functional Molle Waist Tool Carry Bag","price":"30.57"},"petram-custom-vwnaca":{"name":"Durable Waterproof 10-Hole Multi Purpose 12g Storage Pouch","price":"15.28"},"petram-custom-kfyfvl":{"name":"Lightweight Portable EDC Flashlight Waist Tool Storage Pouch","price":"13.10"},"petram-custom-fwcamg":{"name":"Tactical Waterproof EDC Key Flashlight Pouch","price":"11.35"},"petram-custom-pwwgci":{"name":"Tactical 12-Slot Molle Pouch","price":"19.65"},"petram-custom-xzctng":{"name":"Tactical Universal Radio Water Pouch","price":"11.35"},"petram-custom-sdnfhw":{"name":"Tactical Camo 16-Slot Tool Pouch","price":"21.83"},"petram-custom-lwntit":{"name":"Tactical Mini EDC Cigarette Waist Pack","price":"17.03"},"petram-custom-izkfqi":{"name":"Tactical Double Mag Pouch","price":"28.38"},"petram-custom-vfcavx":{"name":"Tactical 4-Hole Utility Pouch","price":"4.80"},"petram-custom-hocagw":{"name":"Tactical Molle Radio Pouch","price":"15.28"},"petram-custom-zojadg":{"name":"Tactical Tourniquet Scissors Pouch","price":"13.10"},"petram-custom-szsfwo":{"name":"Tactical EDC Wrist Waist Pack","price":"26.20"},"petram-custom-rdfgiw":{"name":"Tactical Molle Water Bottle Pouch","price":"11.35"},"petram-custom-hzsgyx":{"name":"Tactical 27-Hole Utility Belt","price":"13.10"},"petram-custom-tznamk":{"name":"Tactical EDC Cigarette Pouch","price":"11.35"},"petram-custom-gwjfqx":{"name":"Tactical Medical Utility Pouch","price":"11.35"},"petram-custom-sfjtqc":{"name":"Tactical Camo Molle Radio Pouch","price":"10.48"},"petram-custom-pwcaty":{"name":"Tactical M5 Small Flashlight Pouch","price":"10.48"},"petram-custom-dfnfzw":{"name":"Tactical Molle Webbing Hook Clip","price":"3.49"},"petram-custom-jfstvw":{"name":"Tactical P90 Double Mag Pouch","price":"26.20"},"petram-custom-hdyank":{"name":"Tactical 360 Rotating Flashlight Pouch","price":"17.03"},"petram-custom-tdwgjv":{"name":"Tactical 5.56 Single Mag Pouch","price":"21.83"},"petram-custom-idkfno":{"name":"Tactical Camo Molle Water Bottle Pouch","price":"11.35"},"petram-custom-tzsfqd":{"name":"Tactical Large Molle Dump Pouch","price":"15.28"},"petram-custom-hdygtw":{"name":"Tactical 600d Molle Camo Waist Pack","price":"10.48"},"petram-lb-small-dump-pouch":{"name":"Tactical Small 1000d Nylon Molle Utility Dump Pouch, Drawstring","price":"19.65"},"petram-tk-036":{"name":"Tactical Multifunctional Mich 2000 Helmet Cover Outdoor Helmet","price":"19.65"},"petram-aa-244":{"name":"Tactical 4-Pack Nylon Molle Attachment Straps Snap Closure","price":"17.47"},"petram-qls19-22":{"name":"Elastic Tourniquet Holder Panel Hook and Loop Mount Nylon","price":"13.10"},"petram-qls19-22-zfstsd":{"name":"Elastic Tourniquet Storage Panel Hook and Loop Mount Nylon","price":"26.20"},"petram-aa-311":{"name":"Elastic Tourniquet Holder Pouch Hook and Loop Belt Bag Outdoor","price":"4.37"},"petram-so-185":{"name":"Tactical Adjustable Molle Drop Leg Platform","price":"28.38"},"petram-qt-250":{"name":"Tactical Nylon Drop Leg Mounting Platform Non Slip Elastic","price":"56.77"},"petram-gb-acc-01":{"name":"Universal Adjustable Elastic Nylon Thigh Strap","price":"18.56"},"petram-gb-acc-08":{"name":"Tactical Molle Quick Detach Mounting Plate","price":"19.65"},"petram-qt-206":{"name":"Tactical Soft Shell Adjustable Belt Attachment Box Pouch","price":"15.28"},"petram-tk-035":{"name":"Outdoor Multifunctional Fast Mich Helmet Pouch Helmet Bag","price":"72.05"},"petram-zh-095-a":{"name":"Tactical Multifunctional Seat Back Storage Bag Hanger","price":"218.34"}};
  var TO = "editor@magnumsports.co.nz";
  var KEY = "ms-cart-v1";

  function load() {
    try {
      var raw = JSON.parse(localStorage.getItem(KEY) || "[]");
      // Drop anything no longer sold, or with an option that has gone.
      return raw.filter(function (l) {
        var p = CAT[l.sku];
        return p && l.qty > 0 &&
          (p.options ? p.options.indexOf(l.opt) > -1 : !l.opt);
      });
    } catch (e) { return []; }
  }
  function save(lines) {
    try { localStorage.setItem(KEY, JSON.stringify(lines)); } catch (e) {}
  }
  function cents(s) { return Math.round(parseFloat(s) * 100); }
  function money(c) {
    return "NZ$" + (c / 100).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  }
  function count(lines) {
    return lines.reduce(function (n, l) { return n + l.qty; }, 0);
  }
  function total(lines) {
    return lines.reduce(function (n, l) { return n + cents(CAT[l.sku].price) * l.qty; }, 0);
  }
  function label(l) {
    return CAT[l.sku].name + (l.opt ? " (" + l.opt + ")" : "");
  }
  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }
  function announce(msg) {
    var live = document.getElementById("cart-live");
    if (live) { live.textContent = ""; setTimeout(function () { live.textContent = msg; }, 50); }
  }

  var lines = load();

  function badge() {
    var n = count(lines);
    document.querySelectorAll("[data-cart-count]").forEach(function (b) {
      b.textContent = n > 99 ? "99+" : String(n);
      b.hidden = n === 0;
    });
    document.querySelectorAll(".nav-cart").forEach(function (a) {
      a.setAttribute("aria-label", n ? "Cart, " + n + " item" + (n === 1 ? "" : "s") : "Cart, empty");
    });
  }

  function update(nextLines, msg) {
    lines = nextLines;
    save(lines);
    badge();
    render();
    document.dispatchEvent(new Event("cart:change"));
    if (msg) announce(msg);
  }

  function add(sku, opt) {
    var found = false;
    var next = lines.map(function (l) {
      if (l.sku === sku && (l.opt || "") === (opt || "")) {
        found = true;
        return { sku: l.sku, opt: l.opt, qty: Math.min(l.qty + 1, 99) };
      }
      return l;
    });
    if (!found) next.push(opt ? { sku: sku, opt: opt, qty: 1 } : { sku: sku, qty: 1 });
    update(next, CAT[sku].name + " added to cart");
  }

  function setQty(i, q) {
    var name = label(lines[i]);
    var next = lines.slice();
    if (q < 1) next.splice(i, 1); else next[i] = { sku: next[i].sku, opt: next[i].opt, qty: Math.min(q, 99) };
    update(next, q < 1 ? name + " removed" : name + ", quantity " + q);
  }

  // ------------------------------------------------------------ cart view
  function render() {
    var box = document.getElementById("cart-lines");
    if (!box) return;
    var form = document.getElementById("order-form");
    box.textContent = "";
    if (!lines.length) {
      box.appendChild(el("p", "cart-empty", "Your cart is empty. Add something from the shelves above."));
      if (form) form.hidden = true;
      return;
    }
    if (form) form.hidden = false;
    var ul = el("ul", "cart-list");
    lines.forEach(function (l, i) {
      var p = CAT[l.sku];
      var li = el("li", "cart-line");
      var info = el("div", "cart-info");
      info.appendChild(el("b", null, p.name));
      if (l.opt) info.appendChild(el("span", "cart-opt", l.opt));
      info.appendChild(el("span", "cart-each", money(cents(p.price)) + " each"));
      var qty = el("div", "cart-qty");
      var minus = el("button", "cart-step", "−");
      minus.type = "button";
      minus.setAttribute("aria-label", "One fewer " + label(l));
      minus.onclick = function () { setQty(i, l.qty - 1); };
      var n = el("span", "cart-n", String(l.qty));
      var plus = el("button", "cart-step", "+");
      plus.type = "button";
      plus.setAttribute("aria-label", "One more " + label(l));
      plus.onclick = function () { setQty(i, l.qty + 1); };
      qty.append(minus, n, plus);
      var sum = el("span", "cart-sum", money(cents(p.price) * l.qty));
      var rm = el("button", "cart-rm", "Remove");
      rm.type = "button";
      rm.setAttribute("aria-label", "Remove " + label(l));
      rm.onclick = function () { setQty(i, 0); };
      li.append(info, qty, sum, rm);
      ul.appendChild(li);
    });
    box.appendChild(ul);
    var t = el("div", "cart-total");
    t.append(el("span", null, "Total (" + count(lines) + " item" + (count(lines) === 1 ? "" : "s") + ")"),
             el("b", null, money(total(lines))));
    box.appendChild(t);
    box.appendChild(el("p", "cart-fine", "Free delivery anywhere in New Zealand, 7 to 10 days. Prices are in New Zealand dollars and include GST and delivery."));
  }

  // ------------------------------------------------------------ checkout
  function orderText(f) {
    var get = function (n) { return (f.elements[n] && f.elements[n].value || "").trim(); };
    var out = ["ORDER REQUEST — " + location.hostname, ""];
    lines.forEach(function (l) {
      out.push(l.qty + " x " + label(l) + "  @ " + money(cents(CAT[l.sku].price)) +
               "  = " + money(cents(CAT[l.sku].price) * l.qty) + "   [" + l.sku + "]");
    });
    out.push("", "Total: " + money(total(lines)) + " (includes GST and delivery)", "",
             "Name: " + get("name"), "Email: " + get("email"), "Phone: " + get("phone"),
             "Deliver to: " + get("address").replace(/\s*\n\s*/g, ", "));
    var pay = f.querySelector("input[name=payment]:checked");
    if (pay) out.push("Payment: " + pay.value);
    if (get("notes")) out.push("", "Notes: " + get("notes"));
    return out.join("\n");
  }

  // Pay now: send SKUs and quantities to the checkout Worker, which prices them
  // from the site's catalogue and returns a Stripe Checkout address.
  function wirePayNow() {
    var btn = document.getElementById("pay-now");
    if (!btn) return;
    var wrap = document.getElementById("pay-now-wrap");
    var err = document.getElementById("pay-now-error");
    var sync = function () { wrap.hidden = !lines.length; };
    sync();
    document.addEventListener("cart:change", sync);
    btn.addEventListener("click", function () {
      if (!lines.length) return;
      var label = btn.innerHTML;
      btn.disabled = true;
      btn.textContent = "Opening secure checkout\u2026";
      err.hidden = true;
      fetch(btn.getAttribute("data-checkout"), {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ items: lines.map(function (l) { return { sku: l.sku, qty: l.qty, opt: l.opt || "" }; }) })
      }).then(function (r) { return r.json().then(function (d) { return { ok: r.ok, d: d }; }); })
        .then(function (x) {
          if (x.ok && x.d.url) { location.href = x.d.url; return; }
          throw new Error(x.d.error || "Payment could not be started.");
        })
        .catch(function (e) {
          err.textContent = (e && e.message) || "Payment could not be started. Please try again.";
          err.hidden = false;
          btn.disabled = false;
          btn.innerHTML = label;
        });
    });
  }

  function wireCheckout() {
    var f = document.getElementById("order-form");
    if (!f) return;
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!lines.length) return;
      var text = orderText(f);
      var subject = "Order request — " + f.elements.name.value.trim();
      var sent = document.getElementById("order-sent");
      document.getElementById("order-copy").value = text;
      sent.hidden = false;
      sent.scrollIntoView({ behavior: "smooth", block: "start" });
      location.href = "mailto:" + TO + "?subject=" + encodeURIComponent(subject) +
                      "&body=" + encodeURIComponent(text);
    });
    var clear = document.getElementById("order-clear");
    if (clear) clear.onclick = function () {
      update([], "Cart cleared");
      document.getElementById("order-sent").hidden = true;
      f.reset();
    };
    var copy = document.getElementById("order-copy-btn");
    if (copy) copy.onclick = function () {
      var ta = document.getElementById("order-copy");
      ta.select();
      var done = function () { copy.textContent = "Copied"; setTimeout(function () { copy.textContent = "Copy order"; }, 1600); };
      if (navigator.clipboard) navigator.clipboard.writeText(ta.value).then(done, function () {});
      else { try { document.execCommand("copy"); done(); } catch (e2) {} }
    };
  }

  // -------------------------------------------------------- add buttons
  document.addEventListener("click", function (e) {
    var btn = e.target.closest && e.target.closest("[data-add]");
    if (!btn) return;
    var sku = btn.getAttribute("data-add");
    var p = CAT[sku];
    if (!p) return;
    var opt = "";
    if (p.options) {
      var card = btn.closest("[data-sku]");
      var sel = card && card.querySelector("select[data-opt]");
      opt = sel ? sel.value : "";
      if (!opt) {
        if (sel) { sel.focus(); sel.setAttribute("aria-invalid", "true"); }
        announce("Choose an option for " + p.name + " first");
        return;
      }
      sel.removeAttribute("aria-invalid");
    }
    add(sku, opt);
    if (btn._was == null) btn._was = btn.innerHTML;
    btn.textContent = "Added ✓";
    btn.classList.add("is-added");
    clearTimeout(btn._t);
    btn._t = setTimeout(function () {
      btn.innerHTML = btn._was; btn._was = null; btn.classList.remove("is-added");
    }, 1400);
  });

  // Another tab changed the cart: follow it.
  window.addEventListener("storage", function (e) {
    if (e.key === KEY) { lines = load(); badge(); render(); }
  });

  function init() {
    if (!document.getElementById("cart-live")) {
      var live = el("div", "sr-only");
      live.id = "cart-live";
      live.setAttribute("aria-live", "polite");
      document.body.appendChild(live);
    }
    // Back from a paid Stripe checkout: the order is placed, so empty the cart.
    if (document.querySelector("[data-clear-cart]") && lines.length) {
      lines = [];
      save(lines);
    }
    badge();
    render();
    wireCheckout();
    wirePayNow();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
