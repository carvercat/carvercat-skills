# Office location card

**Template** `cb_office_card` (Library name "Office location card") · Corporate Brand pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `CB Office card` in `categories/corporate-brand/cb-lab-3`.

For briefs like "we're opening a new office", "visit us at", "our locations". A map stand-in on the left half (pale panel and white streets) with a teal pin that sends one pulse, and the city, address and opening date on the right. The light background is part of the template. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Map panel (960 × 1080 px), six streets (white 18 px) | 0, 2–12 | opacity in 16 f, 2 f apart | panel **f15**, last street **f27** |
| Pin (teal 64 px), pin dot (white 22 px) | 18, 22 | Card settle (as keys) | pin **f33**, dot **f34** |
| Pin pulse (teal 3 px ring) | 34 | scale 1 → 2.2, decelerate; opacity 0.9 → 0 | scale **f57**, gone **f64** |
| Kicker "NEW OFFICE", city (SemiBold 96 px) | 10, 14 | Soft rise | city **f35** |
| Address (Regular 32 px, two lines) | 22 | Soft rise | **f43** |
| Rule (120 × 3 px), opening date (Medium 36 px) | 30, 34 | rule grows from the left; Soft rise | date **f55** |

**0% overshoot.** Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (closest 53.6 px, kicker / city). The pulse grows inside the placed instance; full-frame looks of the placed comp (f21–149) show nothing cut.

## Steps
1. Replace the map panel and streets with a map still (or a map built with `ai/scripts/maps/map_overlay.py`); keep the pin above it.
2. Move the pin to the address on the map. Keep it at least 70 px from the panel edge, so the pulse (141 px at full size) stays on the map.
3. Edit the city, address and date. An address of two lines fits; a third line moves the rule and date down by 40 px.

## Pitfalls
- One pulse is enough for a corporate card. A looping pulse reads as an alert, not a location.

Inspiration: location cards in company and real-estate films. No external text or code was used.
