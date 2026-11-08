# Gauge

**Template** `dv_gauge` · Data Viz pack · **Verified 0.1.8.4 (rev 1130)**, comp `DV Gauge`.

A 600 px half-circle meter centred at (960, 660) with a 40 px butt-capped stroke. The cyan fill and a 250 px needle sweep together from 0 to 72%. The value "72" (Bold 96 px) and the label "Health score" sit below the hub.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Track | static | Trim Stroke 0 → 0.5 (the top half, 3 → 12 → 9 o'clock) | |
| Fill | 8–40 | Trim start 0.5 → 0.5 − 0.5 × 0.72 (end held at 0.5), Custom (0.34, 1.15, 0.64, 1) | **0.6% overshoot, settles f29** |
| Needle (transformOrigin "0% 50%", anchor [−1, 0], drawn pointing right) | 8–40 | rotation 180° → 180° − 180° × 0.72 = 50.4°, same curve | **0.6% overshoot, settles f29** |
| Value | 30–40 | opacity | |

## Steps
For another value *v* (0–1): set the fill's start target to 0.5 − 0.5*v* and the needle's target to 180 − 180*v*, and keep both on the same curve and frames so the needle sits on the fill's edge. Rotation is positive counter-clockwise.
