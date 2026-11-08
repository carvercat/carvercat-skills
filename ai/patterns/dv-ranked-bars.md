# Ranked bars

**Template** `dv_ranked_bars` · Data Viz pack · **Verified 0.1.8.4 (rev 1130)**, comp `DV Ranked bars`.

Five rows, 120 px apart: Design 92, Engineering 78, Marketing 64, Sales 51, Support 37. Labels are right-aligned at x 520, bars start at x 560 (56 px tall, 8 px radius, 1000 px = 100), and values sit 20 px past the bar ends. The top row is cyan with an ink label; the others are slate with muted labels.

| Part | Frames (row *i* = 0…4) | Motion | Measured |
|---|---|---|---|
| Label | 3*i* to 3*i* + 8 | opacity | |
| Bar | from 6 + 4*i* | **Bar grow across - spring** (transformOrigin "0% 50%", anchor [−1, 0]) | 4.4% overshoot, settles 18 f after its start |
| Value | from 24 + 4*i* | slides 12 px from the left (expo, 10 f), fades in over 6 f | settles 7 f after its start |

## Steps
Place and apply. A new value means a new bar width (value × 10 px) with its centre at 560 + width / 2, and the value text moved to 580 + width. Keep the highlight on one row only.
