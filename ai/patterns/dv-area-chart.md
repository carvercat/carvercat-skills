# Area chart

**Template** `dv_area_chart` · Data Viz pack · **Verified 0.1.8.4 (rev 1130)**, comp `DV Area chart` in `categories/data-viz/dv-lab-2`.

An 8-point line (6 px, cyan) over a filled area (cyan at 28% opacity), revealed left to right, with the end value. Plot 1200×520 px, baseline y 820. 90 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Baseline | 0 | opacity in | |
| Window (mask, anchor at the left edge) | 0 | scale X 0 → 1, f8–50, Custom S-curve | settles **f46** |
| Area (closed path, masked by Window) | 0 | none: the window reveals it | |
| Line | 0 | Trim Stroke end 0 → 1, f8–50, S curve cubic-bezier(0.333, 0, 0.667, 1) | settles **f46** |
| End value ("86", Bold 40 px) | 50 | 16 px from above, 12 f | settles **f58** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0. The mask survives extraction and placement.

## Steps
1. Place and apply. To change the data, rebuild with `area_chart()` in `ai/scripts/motion/data_viz_lab2.py`.

## Pitfalls
- Mask order: `property.set {id:<area>, key:"mask", value:{"ref":"<window id>"}}`, then `parent.clear {ids:[window, area]}` when the window must move independently.
- The window and the line share timing, but trim runs by path length and the window by x. On a steep segment the fill edge leads or trails the pen by a few pixels.
- Lint does not see masks ([KI-133](../references/known-issues.md#ki-133)); judge the reveal with a look.
- The 28% fill is mixed with whatever is underneath, so it looks darker over black than over the lab's slate.

Inspiration: area/trend charts in analytics products. No external text or code was used.
