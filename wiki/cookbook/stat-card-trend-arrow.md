---
id: cookbook/stat-card-trend-arrow
title: Build a stat card with a trend arrow
section: cookbook
tags: [stat card, kpi, metric, trend, delta, up arrow, down arrow, dashboard, chip, triangle]
styles: [saas-ui, data-viz, corporate-brand]
topics: [data, ui, shapes]
related: [cookbook/count-a-number-up, genres/data-stories, design/contrast, accessibility/readability]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/animation-usability/]
---

# Build a stat card with a trend arrow

**Goal.** A dashboard card: a label, a big value, and a coloured chip with an up (or down) triangle and the
change, entering in that order.

## Steps

1. Card: rectangle 640 × 380 px, `borderRadius` 28, with **`Card lift`**.
2. Label (34 px Medium, muted) 4 f later; value (120 px Bold) 6 f after the card, rising 24 px, expo, 14 f.
3. Chip 16 f after the card: a rectangle 190 × 62 px, `borderRadius` 16, in the trend colour at 18% opacity; a
   3-sided **Polygon** (30 px) as the triangle; the change as text (40 px Bold). `Pop - gentle` on each.
4. Point the triangle with **`rotate`**: **`"-90deg"`** points it up, **`"90deg"`** down (a 3-sided
   polygon's corner points right at 0°; rotate is clockwise, the 0.1.6 note had +90° up and −90° down).
5. Use a light tint of the trend colour for the change text, not the saturated colour: it sits on a dark
   tint of itself.

## Measured in Carvercat 0.1.6

Comp `K Stat card` in [cookbook lab 6](../labs/README.md#cookbook-lab-6carverproj): an "up" card from f4 and a
"down" card from f10; `inspect curves`, `inspect lint` and `carvercat_render` at f60:

| Triangle | Rotation | Top row width | Bottom row width | Height |
|---|---|---|---|---|
| Up (green) | +90° | 2 px | 25 px | 22 px |
| Down (red) | −90° | 26 px | 2 px | 22 px |

- `Card lift`: opaque by f11, still (position and scale) from **f16**, 12 f after it starts. Value settled
  f19; chip and triangle `Pop - gentle` 4.4% over, settled f38.
- First version, change text 36 px in the saturated green and red: `inspect lint contrast:true` gave 2
  `low_contrast` warnings (**2.99:1** and **2.53:1**, wanted 3) and 2 `text_too_small`. With 40 px in light
  tints (#7FE0A0, #FF8A80): **0 errors, 0 warnings**, 8 notes.

## Traps

- A polygon's old `angle` does not rotate it (use `rotate`): [KI-150](../../ai/references/known-issues.md#ki-150).
- `inspect curves` reads a second move on the same lane as overshoot:
  [KI-152](../../ai/references/known-issues.md#ki-152).
- Small `Regular` text under 34 px escapes the contrast check, so small chips need a look too:
  [KI-142](../../ai/references/known-issues.md#ki-142).

## In Carvercat

- Library: `KPI tile` ([su-kpi-tile](../../ai/patterns/su-kpi-tile.md)), `Stat card`, `Three stats`
  ([cb-three-stats](../../ai/patterns/cb-three-stats.md)), `Card lift`, `Pop - gentle`.
- Background: [count a number up](count-a-number-up.md), [contrast](../design/contrast.md).
