# Walk cycle (rigged)

**Template** `ct_walk_cycle` (Library name "Walk cycle (rigged)") · Cartoon Bounce pack · **verified 0.1.8.1 (rev 1127; headless, isolated folders, pack added to a scratch user Library)**, comp `CT Walk cycle` in `categories/cartoon-bounce/ct-lab-3`.

For briefs like "the mascot walks in", "a character strolls across", "arrives at the shop". A blob character walks 976 px to the right in eight steps, stops with a settle on its hips and blinks. 150 f.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Shorts (the pivot: a visible red rectangle at the hips, centred anchor) | f10–106 | position baked every 2 f: x linear at 10.2 px/f, y = ground − 150 × cos(leg angle), so the hips dip 13 px when the legs spread and rise at the passing pose | position settles **f106** (50 keys) |
| | f106–119 | stop: 106 × 94%, 97 × 103%, 100% (S curve cubic-bezier(0.333, 0, 0.667, 1)) | scale settles **f119**; x·y 0.996–0.999 |
| Leg front / Leg back (ink capsules, anchor at the top = the hip) | f10–106 | ±24°, Linear between extremes (half step, 7 full steps of 12 f, half step); the back leg mirrors the front | rotation settles **f106**; 0% overshoot |
| | each swing | the swinging leg tucks to 108 × 88% mid-swing, so its foot clears the ground | x·y **0.95** |
| Arm front / Arm back (anchor at the shoulder) | f10–106 | ±19° against the legs, S curve between extremes | settles **f106** |
| Body, Eye 1–2 | — | parented to Shorts; eyes blink f126–132 | |
| Walk shadow | f10–106 | slides with the hips, linear | |

Lint 0 errors, 0 warnings, 30 notes (`speed_jump` at f10 where the walk starts at full speed, `repeated_key_value` on the f0–10 hold). Placed into a fresh comp: lint 0/0/0; the rig survives placement. Text-gap audit: no text. Full-frame looks of the placed comp at f106 and f149: nothing cut.

## How the feet stay planted
- The stride is `2 × L × sin(θ)` = 2 × 150 × sin 24° = **122 px**; the hips move one stride per 12 f step, and the leg turns Linear, so the stance foot sweeps back exactly as fast as the hips move forward.
- Both legs share `|θ|`, so the hip height `ground − L cos θ` keeps both soles on the ground line; the tuck (scale y 88%) lifts the swinging foot about 18 px.
- The hips are baked every 2 f ([arcs, method 1](../references/craft/principles/arcs.md)): two keys per step would make a straight "^" path and a ping-pong.

## Steps
1. Change `L`, `th` or `step` in `walk_cycle()` and rebuild; the stride and the hip speed follow. More steps: lengthen `keysA`.
2. Recolour Body, Shorts and arms; keep the legs as one ink colour so the crossing reads.

## Pitfalls
- Easing the leg rotation (S curve) makes the planted foot slide; keep it Linear and put the ease in the arms.
- The walk starts and stops at full speed (lint notes `speed_jump`); the settle squash on the hips hides the stop.
- Rotation is positive counter-clockwise, so +θ moves a hanging leg's foot forward (to the right).

Inspiration: the classic walk cycle (contact, passing, planted foot). No external text or code was used.
