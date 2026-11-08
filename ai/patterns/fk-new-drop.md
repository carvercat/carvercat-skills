# New drop reveal

**Template** `fk_new_drop` (Library name "New drop reveal") · Funky pack · **verified 0.1.8.1 (rev 1127; headless, isolated folders, pack added to a scratch user Library)**, comp `FK New drop` in `categories/funky/fk-lab-3`.

For briefs like "new drop", "merch release", "collection 03 drops Friday". NEW and DROP slam in with hard ink shadows, a product panel stand-in slides in with a wiggle and then a purple slab steps out behind it, a black tape with the drop time grows across, and three sparks spin in. 120 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| "COLLECTION 03" (ExtraBold 40 px, purple, tracking 1.4) | 0 | fade 6 f | **f6** |
| "NEW" (ExtraBold 220 px, yellow, hard shadow 12 px) | 2 | stamp 1.15 → 1, 12° turn into +4°, 9 f | **9.7%**, **f11** |
| "DROP" (pink) | 12 | the same, turning from the other side | **9.7%**, **f21** |
| Product panel (560 × 660 px, teal, ink outline) and label | 10 | Slide in - wiggle as keys: from +620 px (expo, 14 f), angle 9° → −3° on the pop curve | lands **f19**; angle **15.8%**, **f27** |
| Panel slab (native Drop shadow, hard, purple) | 24 | offset 0 → 22 px right and down, expo | **f31** |
| Tape (ink) and "DROPS FRI 6 PM" (yellow 50 px) | 22, 26 | tape grows from the left, 10 f; text fades 4 f | **f29**, **f30** |
| Sparks 1–3 (4-point stars) | 32, 36, 40 | Spin in, then ±40° one way | size **9.8%**, **f45** (spark 1) and **f53** (spark 3) |

Lint 0/0/0 in the lab and placed. Text-gap audit: closest pair 24.6 px (NEW / DROP; the shadows sit in between). Full-frame looks of the placed instance at f14 (panel half outside the frame) and f119: nothing cut.

## Steps
1. Put the product still over the panel (560 × 660 px, 24 px corners) at the same −3° angle, or parent it to the panel.
2. Change the date on the tape; the tape is sized from the text in `funky_lab3.py`.

## Pitfalls
- The sparks' rotation lane reads **28.6%** "overshoot" in `curves` because it holds an entrance and a drift ([KI-152](../references/known-issues.md#ki-152)); the entrance alone is the 9.8% size pop.
- NEW / DROP first slammed from 1.6: the growing NEW covered COLLECTION 03 (`text_overlap` 100%). From 1.15 and with DROP starting after NEW lands, clean.

Inspiration: streetwear release posts and sneaker-drop countdowns. No external text or code was used.
