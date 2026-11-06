# Calendar heatmap

**Template** `dv_heatmap` (Library name "Calendar heatmap") · Data Viz pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `DV Heatmap` in `categories/data-viz/dv-lab-3`.

For briefs like "a year of activity", "habit / streak", "daily usage". 140 day squares (20 weeks × 7 days, 44 px, Monday on top) in five levels of active minutes (sample data, made by a seeded generator with a week off and a training block), a Less → More legend, and the best week outlined with its total. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Day and month labels (28 px) | 0–10 | opacity in | |
| Day squares | 6 + week + day ÷ 3 (Mon–Wed +0, Thu–Sat +1, Sun +2) | scale 0.5 → 1, 8 f, expo; opacity in 4 f | first settles **f11**, last **f32** |
| Legend | 40–45 | opacity in | |
| Best-week outline (4 px stroke) | 52 | Trim end 0 → 1, 16 f, S curve cubic-bezier(0.333, 0, 0.667, 1) | settles **f67** |
| Best-week note ("Best week: 6 h 44 min") | 66 | 16 px from above | settles **f74** |

Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (closest 18.2 px, "May" / a square). 161 objects.

## Steps
1. Real data: replace `heat_minutes()` in `ai/scripts/motion/data_viz_lab3.py` with the daily values (Monday first); the levels, the best week and its total are computed.
2. A full year is 53 columns: cut the square to about 20 px and accept that the labels go above, not beside, or show one quarter per scene.

## Pitfalls
- Level 0 is a dark square, not empty: a missing day and a zero day look different, and the grid stays readable.
- A simple modulo "random" made stripes along the rows; a seeded generator looks like real behaviour.

Inspiration: calendar heatmaps in fitness and developer-activity apps. No external text or code was used.
