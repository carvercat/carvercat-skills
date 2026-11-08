# Blinking face

**Template** `ct_blink_face` · Cartoon Bounce pack · **verified 0.1.8.1 (rev 1127; headless, isolated folders, pack added to a scratch user Library)**, comp `CT Blink face`.

A 420 px yellow head with an 8 px ink outline, two 46 × 70 px eyes, and a smile drawn as the bottom arc of a 180 × 140 ellipse stroke.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Head | 0–28 | **Jelly in** | width 30.7% / height 16.2% overshoot, settles **f21** |
| Eyes | from 10 | **Pop - wobbly**; blinks at 44 and 80: scale [1.1, 0.1] in 2 f (accelerating arrival cubic-bezier(0.333, 0, 0.667, 0.333)), back in 3 f (decelerating arrival cubic-bezier(0.333, 0.667, 0.667, 1)) | |
| Smile | 18–30 | Trim Stroke start 0.75 → 0.55 and end 0.75 → 0.95 (grows out from 6 o'clock), Custom expo | settles **f26** |

Lint 0/0. The smile uses the measured ellipse path direction (it starts at 3 o'clock and runs counter-clockwise, so 0.75 is 6 o'clock; see [data-viz.md](data-viz.md)). Blink every 2–4 s, never on a regular beat.
