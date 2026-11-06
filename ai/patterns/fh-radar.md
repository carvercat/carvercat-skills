# Radar sweep

**Template** `fh_radar` · Futuristic HUD pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FH Radar`.

A 600 px radar: three grid rings and two axes in `#0F2A36`, a cyan pie-slice sweep at 28% opacity, a glowing beam line, and three amber blips.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Sweep wedge (ellipse 300 px, stroke 300 px butt-capped, Trim 0 → 0.07) and beam (anchor at the centre end) | 0–120 | rotate 0 → 720° clockwise, linear (stored −720°): one clockwise turn per 60 f | 6° per frame |
| Blips (math angles 300°, 200°, 40°) | appear at f10, f27, f53 | scale 0 → 1 in 6 f (back), then opacity 1 → 0.35 over 50 f | **8.7% overshoot**, settle 6 f after appearing |

Lint 0/0/0; qc found no flashes. To move a blip, compute its frame from its angle: ((360 − θ) mod 360) / 360 × 60.
