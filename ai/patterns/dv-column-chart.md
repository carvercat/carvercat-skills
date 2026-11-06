# Column chart

**Template** `dv_column_chart` · Data Viz pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `DV Column chart` in `categories/data-viz/dv-lab-2`.

Six monthly columns (96 px wide, plot 1000×480 px, baseline y 800) with gridlines at 0/50/100, axis labels, month labels, and the last column highlighted in cyan with its value above. 90 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Grid 0/50/100 and axis labels (28 px) | 0 | opacity in 8 f, 2 f apart | |
| Month labels (28 px) | 0 | opacity in, 2 f apart from f4 | |
| Column 1–6 (anchor on the baseline) | 8, 12 … 28 | Bar grow up - spring | **4.4% overshoot; Column 1 settles f26, Column 6 f46** |
| Peak value ("91", Bold 40 px) | 46 | settles 16 px from above, 12 f, expo; fades in 6 f | settles **f54** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place and apply. Set each column's height (value / 100 × 480 px) inside the comp; the anchor keeps it on the baseline.
2. Move the Peak value to the top of whichever column you highlight (column top − 44 px).

## Pitfalls
- The peak value waits for the last column's spring (start + 18 f). Earlier, the 4.4% overshoot runs the column into the label.

Inspiration: the standard column chart of business dashboards. No external text or code was used.
