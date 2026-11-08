# Donut - fill

**Template** `dv_donut` · Data Viz pack · **Verified 0.1.8.4 (rev 1130)**, comp `DV Donut`.

A 420 px ring with a 56 px stroke. Three segments sweep clockwise from 12 o'clock: 46% cyan, 28% amber, 18% green (92% in total; the last 8% stays track grey). The centre reads "92%" over "of goal".

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Track | 0–8 | opacity 0 → 1 | |
| Segment 1 / 2 / 3 | 6–22 / 20–36 / 32–48 | Trim Stroke start swept (end held), Custom expo | segment 1 settles **f16**, segment 3 **f42** (segment 2 uses the same 16 f curve; not measured separately) |
| Centre value / label | 30–40 / 34–44 | opacity | |

## How the clockwise sweep is made (measured)
An ellipse's stroke starts at 3 o'clock and runs counter-clockwise. Each segment ellipse is rotated **+90°** (counter-clockwise), so its path starts at 12 o'clock. A clockwise share [a, b] is then native [1 − b, 1 − a]:
- set Trim **end** = 1 − a;
- key Trim **start** from 1 − a to 1 − b.

The stroke cap is **butt**, so neighbouring segments meet cleanly.

## Steps
Place and apply. For other shares, change each segment's held end and its start's target value (1 − cumulative share). Keep the segments' start frames about 14 f apart.
