# Progress rings

**Template** `dv_progress_rings` · Data Viz pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `DV Progress rings` in `categories/data-viz/dv-lab-2`.

Three 300 px rings (26 px stroke, round caps) on dark tracks, filling clockwise from 12 o'clock to 82%, 64% and 45%, with the value in the centre and a label below. 90 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Track 1–3 | 0 | opacity in, 3 f apart | |
| Ring 1–3 (rotation 90°) | 0 | Trim Stroke start 1 → 1 − value, 30 f, Custom expo, from f6, 12, 18; opacity Hold 0 → 1 on the start frame | Ring 1 settles **f25**, Ring 3 **f37** |
| Value 1–3 (Bold 64 px) | 0 | opacity in from ring start + 16 | |
| Label 1–3 (Medium 30 px) | 0 | opacity in | |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place and apply. For a new value v, set the ring's trim start end key to 1 − v and edit the centre text.

## Pitfalls
- The rings use the donut's geometry rule ([data-viz.md](data-viz.md#measured-geometry-facts-016)): rotate +90° and trim from 1 − b to 1 − a for a clockwise share.
- A round cap draws a dot even at zero length, so each ring is hidden (Hold 0) until its sweep starts.

Inspiration: activity and KPI rings in product dashboards. No external text or code was used.
