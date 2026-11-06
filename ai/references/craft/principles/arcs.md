# Arcs

**What it does:** living things move along curves, not straight lines. Arcs make jumps, throws, swings and big moves feel natural.

## What Carvercat does with position keys (measured)
**Position travels in a straight line between two keys, whatever the easing.** Measured on 0.1.6 (rev 1105), 2026-10-28, headless: a dot keyed (200, 800) → (960, 300) → (1720, 800) and sampled every 5 f stayed on the two straight segments to within 0.05 px, with linear and with ease-in-out. Easing changes the **speed** along the segment, not its **path**. So:
- **Offsetting the middle key does not make a curve; it makes a corner** (a "^" with two straight legs). With an ease-in-out or ease on that key the object slows into the corner and speeds out of it.
- Earlier versions of this page and of [../motion-principles.md](../motion-principles.md) said "offset the mid key" for a curved diagonal. That was wrong and is corrected here (2026-10-28).

## Three ways to get a real arc
1. **Bake the curve to keys** (simplest). Sample the curve you want and key the position every 2 f with linear joins. Measured: a parabola keyed every 2 f over 40 f stayed within **1.25 px** of the true curve at the in-between frames. Script it (the lab helpers in `ai/scripts/motion/` build key lists this way, e.g. `bake()` in `curves.py`).
2. **Separate the axes with a nest** (a real curve with only a few keys). Put the object in a comp where it moves only vertically (ease-out up to the peak, ease-in down), nest that comp, and move the nest horizontally in the master, linearly. Each axis eases on its own, so the path is a smooth arc. Verified with a look (9 frames, f0–40); master lint 0 / 0 / 0. This is also how you get constant horizontal speed in a jump ([../../../patterns/cartoon-bounce.md](../../../patterns/cartoon-bounce.md) pitfall 2).
3. **Rotate about a pivot** (swings, limbs, orbits). Parent the part to a visible pivot (a nail, a hub, a joint; `parent.assign`) and rotate the pivot: every point travels on a circle. In the project file a child's position is an offset from the comp centre ([../../app/json-authoring.md](../../app/json-authoring.md), [../../drawing/rigging.md](../../drawing/rigging.md)).

## The verified examples, measured honestly
| Template | Path | Numbers |
|---|---|---|
| Hanging sign ([ct-hanging-sign.md](../../../patterns/ct-hanging-sign.md)) | true arcs: the whole sign rotates about the nail | 28° first swing, still from f42 |
| Orbit end card ([fk-orbit-end.md](../../../patterns/fk-orbit-end.md)) | true circles: satellites parented to a turning hub | 120° over 132 f |
| Character hop ([ct-character-hop.md](../../../patterns/ct-character-hop.md)) | **two straight legs** (take-off → peak → landing), eased: it reads as a hop because of the squash, stretch and easing, not because the path curves | peak f29, lands f40 |
| Bouncing ball ([ct-bouncing-ball.md](../../../patterns/ct-bouncing-ball.md)) | straight legs between contacts and peaks, eased | contacts f18, 44, 62, 72 |

For a true parabola in the hop or the ball, use method 1 or 2.

## Traps
- A child of a parent whose `transformOrigin` (stored anchor) is off-centre drifts when the parent rotates; use a pivot with a centred `transformOrigin` "50% 50%" ([../../drawing/rigging.md](../../drawing/rigging.md)).
- Baked keys every 2 f make the curve but also fix the timing: re-bake rather than hand-editing a few of them.
