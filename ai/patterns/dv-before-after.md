# Comparison bars

**Template** `dv_before_after` (Library name "Comparison bars"; the essentials already have a "Before and after") · Data Viz pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `DV Before after` in `categories/data-viz/dv-lab-2`.

Two 200 px columns on a baseline (Before in grey at 30, After in cyan at 85, plot height 520 px), their values, and a green delta badge ("2.8x"). 90 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Bar Before, Bar After | 6, 16 | Bar grow up - spring | **4.4% overshoot; settle f24 / f34** |
| Value Before, Value After (Bold 40 px) | 24, 34 | settle 16 px from above, 12 f, expo | |
| Delta badge (200×76 px pill, green) | 40 | Pop - gentle | **4.4% overshoot, settles f58** |
| Delta ("2.8x", Bold 40 px, slate) | 42 | Zoom settle | settles **f58** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place and apply. Set the heights (value / 100 × 520 px), values and labels; recompute the delta (After / Before).

Inspiration: before/after result slides in case-study videos. No external text or code was used.
