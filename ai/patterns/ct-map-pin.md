# Bouncy map pin

**Template** `ct_map_pin` (Library name "Bouncy map pin") · Cartoon Bounce pack · **verified 0.1.8.1 (rev 1127; headless, isolated folders, pack added to a scratch user Library)**, comp `CT Map pin` in `categories/cartoon-bounce/ct-lab-3`.

For briefs like "find us here", "new store", "where the party is" in a playful film. A map stand-in fades in, a pin drops, squashes on its point, sends a ring and a label card pops out beside it. 120 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Map, Road 1–3, River (stand-ins) | 0 | opacity in f0–8 | |
| Pin tip (the pivot: a small ink oval at the point) | 0 | falls from y −40 to 680 (accelerating arrival cubic-bezier(0.333, 0, 0.667, 0.333)), stretched 86 × 116%; lands **f16**; squash 122 × 80% at f17, then 92 × 108%, 104 × 96%, 100% | position settles **f16**, scale **f29**; x·y 0.976–1.003 |
| Pin head (teardrop path), Pin dot | 0 | parented to Pin tip, so they squash about the point | |
| Pin shadow | 0 | grows 30 → 100% and darkens as the pin falls | |
| Landing ring | 16 | 60 → 190%, fades out (f16–36) | |
| Label card | 26 | pops 0 → 112 → 95 → 102 → 100% | scale settles **f41** |
| Place "Pip's Bakery" (ExtraBold 54 px) / Note "OPEN TILL 6" (ExtraBold 34 px) | 30 / 34 | pop from 60% | settle **f45** / **f49** |

Lint 0 errors, 0 warnings, 3 notes (`speed_jump` on the impact, intended). Placed into a fresh comp: lint 0/0/0. Text-gap audit: 5 pairs, closest 19 px (Place / Note). Full-frame looks of the placed comp at f17 and f119: nothing cut.

## Steps
1. Replace the map shapes with a still of the real map (keep it under the pin).
2. Move the pin by changing `tx, ty` in `map_pin()`; the card sits at `lx, ly`.

## Pitfalls
- The point is the pivot. Squashing the head with an anchor at its bottom would leave the white dot behind; parenting both to a visible tip makes them squash together ([rigging](../references/drawing/rigging.md)).
- Text that pops from 0 is read by lint at its first visible frame: the note first reported `text_too_small` (10.6 px). Text pops start at 60%.

Inspiration: map pins in playful location reveals. No external text or code was used.
