# Timeline

**Template** `dv_timeline` · Data Viz pack · **Verified 0.1.8.4 (rev 1130)**, comp `DV Timeline` in `categories/data-viz/dv-lab-2`.

A 1400 px axis that draws left to right with five milestones: a dot, a year above (Bold 40 px) and a caption below (Medium 28 px). The last milestone is cyan. 120 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Axis (4 px line) | 0 | Trim Stroke end 0 → 1, f6–60, Custom S-curve (0.65, 0, 0.35, 1) | settles **f55** |
| Milestone 1–5 (28 px dot, 6 px slate ring) | the frame the line reaches it | Data point pop | **16.2% overshoot**; Milestone 5 settles **f71** |
| Year 1–5 | dot + 2 | 16 px from above, 12 f, expo | |
| Caption 1–5 | dot + 5 | 16 px from below, 12 f, expo | Caption 5 settles **f73** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place and apply. Edit years and captions; milestones are 350 px apart, so check long captions with a look.
2. Uneven spacing: rebuild with `ai/scripts/motion/data_viz_lab2.py`. Each dot's start frame comes from `t_for_progress`, the inverse of the axis ease.

Inspiration: company-history and roadmap timelines. No external text or code was used.
