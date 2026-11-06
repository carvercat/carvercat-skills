# Data table

**Template** `dv_data_table` · Data Viz pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `DV Data table` in `categories/data-viz/dv-lab-2`.

A four-column table (Team, Q1, Q2, Change) with a header rule, four rows 90 px apart, green/pink change values, and a highlight bar that sweeps behind the last row. 120 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Header rule and headers (SemiBold 28 px, muted) | 0 | opacity in, 2 f apart | |
| Row 1–4 cells (34 px; team and change Bold) | 8, 14, 20, 26 | 16 px from above, 12 f, expo; fade 6 f | last row settles **f34** |
| Row highlight (1140×76 px, `#1B2B3F`, anchor at the left edge) | 56 | scale X 0 → 1, f56–70, expo | settles **f65** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place and apply. Edit the cells; numbers are right-aligned so digits line up.
2. Highlight another row: move the Row highlight to that row's y (400 + row × 90).

## Pitfalls
- The highlight is created before the cells, so it sits under them.

Inspiration: results tables in quarterly-review videos. No external text or code was used.
