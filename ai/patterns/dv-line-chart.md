# Line chart - draw

**Template** `dv_line_chart` · Data Viz pack · **Verified 0.1.8.4 (rev 1130)**, comp `DV Line chart` in `categories/data-viz/dv-lab`.

A 1200×560 px plot (x 360–1560, y 260–820) with five gridlines (0, 25, 50, 75, 100) and right-aligned 28 px axis labels. A 6 px cyan line through six values (32, 45, 41, 58, 66, 84) draws itself, data points pop as it reaches them, and the last value appears above the final point.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Gridline and label *i* | 2*i* to 2*i* + 8 | opacity 0 → 1 | |
| Line | 10–55 | Trim Stroke end 0 → 1, Custom S-curve (0.65, 0, 0.35, 1) | settles **f51** |
| Points 1–6 (20 px, 4 px ground-coloured ring) | clip starts 10, 27, 31, 34, 38, 55 | **Data point pop** | 16.2% overshoot, settles 11 f after each start |
| End value ("84%", Bold 40 px) | 55–67 | rises 16 px (expo), fades in over 6 f | settles **f63** |

## Steps
1. Place and apply. To change values, edit the Line's path nodes and move each Point to its node.
2. The points' start frames come from the line's arc length and the inverse of its ease. Regenerate them with `line_chart()` in `data_viz_lab.py` when the values change, or start each point's clip on the frame the look shows the line reaching it.
