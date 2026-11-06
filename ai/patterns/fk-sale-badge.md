# Sale badge

**Template** `fk_sale_badge` · Funky pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FK Sale badge` in `categories/funky/fk-lab-2`.

A 520 px pink 16-point starburst (inner radius 0.82, ink outline) with "50%" (white, 150 px, hard ink offset shadow) and "OFF TODAY" (ink, 48 px). 90 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Badge | 0 | Spin in; then turns 0 → 30° f20–90 (linear, one way) | size **4.4%**, settles **f18** |
| Badge big | 6 | Tilt pop | size **16.2%**, angle **30.9%**; settles **f22** |
| Badge small | 12 | Stamp, plus rotation −12° → 0 (back ease) | |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Pitfalls
- Tilt pop starts at size 0. On the 48 px line it failed lint `text_too_small` ("10.9 px tall"); Stamp starts large, and a small rotation key keeps the style's "rotation in every entrance".

Inspiration: retail starburst stickers. No external text or code was used.
