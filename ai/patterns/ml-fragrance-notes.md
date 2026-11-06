# Fragrance notes

**Template** `ml_fragrance_notes` (Library name "Fragrance notes") · Minimal Luxury pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `ML Fragrance notes` in `categories/minimal-luxury/ml-lab-3`.

For briefs like "the notes of the fragrance", "what is inside", "key ingredients", or a care list with three headings. Top, heart and base notes arrive one tier at a time, each with a gold rule that opens under it; the rules widen from tier to tier, so the three read as a pyramid. The product line comes last. 180 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Tier labels "TOP / HEART / BASE" (gold Regular 26 px, tracking 1.6, y 290 / 470 / 650) | 10, 38, 66 | opacity in 36 f; tracking 1.60 → 1.64 over the hold | Tier 1 opaque **f41** |
| Notes (ivory Regular 40 px, 56 px under the label) | label + 8 | up 12 px over 40 f (decelerate), then a 0.3% H drift | **0% overshoot**; Notes 1 opaque **f49**, Notes 3 **f105** |
| Rules (gold 2 px, 116 px under the label; 160 / 280 / 400 px wide) | | open from the centre, label + 18 for 40 f, S curve cubic-bezier(0.333, 0, 0.667, 1), the curve arriving at the key | Rule 3 settles **f120** |
| Product "No. 7 · EAU DE PARFUM" (muted Regular 26 px, tracking 1.4, y 880) | 100 | opacity in 36 f | opaque **f131** |

Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 21 pairs, closest 30.6 px (Tier 1 / Notes 1).

## Steps
1. New notes: edit `NOTES` (label, notes, rule width) in `ai/scripts/motion/minimal_luxury_lab3.py` and rebuild, or edit the texts after placing. Keep each tier to one line of two or three notes (the longest here, "Bergamot · Pink pepper", measures 441 px at 40 px).
2. For an ingredient or care list, rename the labels (for example KEY INGREDIENTS / TEXTURE / RITUAL) and keep the order: what matters most first.

## Pitfalls
- The tiers are 180 px apart; a fourth tier does not fit above the product line. Use two templates or drop the product line.
- 26 px is the smallest size in the pack: Rethink Sans at 28 px is about 20 px tall and lint's floor is 18 px ([KI-143](../references/known-issues.md#ki-143)). Do not go smaller for the labels.

Inspiration: fragrance note pyramids on perfume cards. No external text or code was used.
