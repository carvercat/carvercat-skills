# Collection index

**Template** `ml_collection_index` (Library name "Collection index") · Minimal Luxury pack · **Verified 0.1.8.1 (rev 1127)**, comp `ML Collection index` in `categories/minimal-luxury/ml-lab-3`.

For briefs like "the looks in this collection", "lookbook contents", "chapters of the film". An INDEX heading with a short rule, five numbered looks (roman numerals) that settle one by one, then the others step back and one look turns gold: the one the next scene is about. 210 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Heading "INDEX" (gold Regular 28 px, tracking 1.8) | 0 | Slow fade in; tracking 1.80 → 1.84 | opacity **f31**, size **f27** |
| Rule (160 px, y 282) | 0 | opens from its centre, f12–52, S curve cubic-bezier(0.333, 0, 0.667, 1), the curve arriving at the key | |
| Numerals (gold Regular 28 px, right edge x 790, no tracking) | 24 + 12 per row | up 10 px over 40 f (decelerate); opacity in 36 f | Numeral 5 lands **f102** |
| Looks (ivory Regular 40 px, left edge x 850, rows 90 px apart from y 370) | numeral + 4 | the same | Look 1 lands **f58**, Look 5 **f106** |
| Choice | 150 | the other rows 1 → 0.4 opacity, f150–180, S curve; Look 3's colour ivory → gold | colour settles **f177** |

Lint 0 errors, 0 warnings, 8 notes (`repeated_key_value`: opacity held at 1 between the entrance and the dim, intended). Placed into a fresh comp: lint 0/0/0. Text-gap audit: 55 pairs, closest 52.2 px (Look 2 / Look 3). The widest look ("Silk Evening Dress", 320 px) ends at x 1170.

## Steps
1. New looks: edit `LOOKS` (and `ROMAN` for more rows) in `ai/scripts/motion/minimal_luxury_lab3.py`; `pick` chooses the look that turns gold, `dim` the frame.
2. Six rows or more: lower the row pitch to 80 px and start at y 340, or the last row crosses y 800.

## Pitfalls
- `inspect curves` reports **150% "overshoot"** on the dimmed rows: 1 → 0.4 is measured against the last key. It is the dim, not a spring ([data-viz round 3, pitfall 4](data-viz.md#round-3-pitfalls)).
- Do not track roman numerals: at tracking 1.3 "III" read as three separate letters in the first build.
- The rows need 25 opaque frames before the dim (lint reading time); with five rows 12 f apart the dim cannot start before about f135.

Inspiration: contents pages of fashion lookbooks. No external text or code was used.
