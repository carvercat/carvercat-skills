# Standings table

**Template** `sp_standings` (Library name "Standings table") · Sports pack · **Verified 0.1.8.1 (rev 1127)**, comp `SP Standings` in `categories/sports/sp-lab-2`.

"LEAGUE TABLE" and five slanted rows (rank, team, points in yellow; ExtraBold 40 px), with row 3 on a red highlight. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Table title | 0 | Slash in | |
| Row 1, 2, 4, 5 panels and all cells | 8, 12, 16, 20, 24 (+2 for cells) | Slash in | last row settles **f33** |
| Row highlight (red, row 3's panel) | 50 | scale X 0 → 1 from its left edge, 10 f, expo | settles **f57** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Edit the cells. To highlight another row, move the Row highlight to that row's y (400 + row × 84) and give the old highlighted row its navy panel back (the lab script skips the panel of the highlighted row).

Inspiration: league-table graphics. No external text or code was used.
