# 70s stripe lower third

**Template** `rt_stripe_lower_third` (Library name "70s stripe lower third") · Retro pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `RT Stripe lower third` in `categories/retro/rt-lab-2`.

A brown rounded name plate (620 × 116 px) with the name in cream (ExtraBold 54 px) and the role in mustard (28 px, tracked), above three 760 px rounded stripes (orange, mustard, teal). Everything moves on twos. 150 f (5 s) with its own exit.

| Part | Clip start | Motion |
|---|---|---|
| LT stripe 1–3 (anchor at the left edge) | 0 | scale X 0 → 1 on twos, 14 f, 4 f apart; back to 0 (accelerating, on twos) from f128–132 |
| LT plate, LT name, LT role | 6, 10, 14 | Rise - on twos; Exit down - on twos |

Lint 0 errors, 0 warnings; `inspect qc` (240 px) found no flashes. Placed into a fresh comp: lint 0/0/0. Gone by f146.

## Pitfalls
- The first exit timing let the last stripe finish on f150, so a stub was still visible on the last frame; the exits start 6 f earlier.
- **Fixed 2026-10-28 (overlap audit).** The role sat 6.6 px under the name (geometry at rest). The name moved up 6 px and the role down 8 px: a 20.6 px gap ([KI-138](../references/known-issues.md#ki-138)).

Inspiration: 70s TV supers with rainbow stripes. No external text or code was used.
