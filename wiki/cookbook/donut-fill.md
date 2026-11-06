---
id: cookbook/donut-fill
title: Fill a donut or ring to a percentage
section: cookbook
tags: [donut, ring, pie, percentage, gauge, progress ring, trim, clockwise]
styles: [data-viz, saas-ui, corporate-brand, explainer, futuristic-hud]
topics: [data, stroke]
related: [genres/data-stories, techniques/line-drawing, cookbook/progress-bar, cookbook/chart-bars-to-values]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.geckoboard.com/blog/to-animate-or-not-to-animate/, https://blog.nobledesktop.com/learn/after-effects/stroke-animation]
---

# Fill a donut or ring to a percentage

**Goal.** A ring that sweeps clockwise from 12 o'clock to a value (68%), over a dim track.

## Steps

1. **Track**: an ellipse, fill `none`, a thick stroke (36 px on a 400 px ring) in a dim colour.
2. **Arc**: the same ellipse on top in the accent colour, stroke cap `butt` (round caps run past the value).
3. An ellipse's stroke **starts at 3 o'clock and runs counter-clockwise**. For the usual clockwise sweep
   from 12 o'clock: `rotate` the arc **`"-90deg"`** (rotate is clockwise, so this moves the 3 o'clock start to 12 o'clock), leave `trimEnd` at
   `"100%"` and key **`trimStart` from `"100%"` to 100% − value** (`"100%"` → `"32%"` for 68%; `anim.set` with `trimStart` keys it by name).
4. For a counter-clockwise sweep from 3 o'clock, leave `rotate` at 0 and key `trimEnd` `"0%"` → `"68%"`.
5. Fade the value in as the arc lands, centred in the ring.

## Measured in Carvercat 0.1.6

Comps `K Donut` and `K Donut clockwise` in [cookbook lab 3](../labs/README.md#cookbook-lab-3carverproj),
rendered at f45 with `carvercat_render` and sampled every 15° round the ring (angles counter-clockwise
from 3 o'clock):

| Comp | Keys | Arc colour found at |
|---|---|---|
| `K Donut` | `rotate` 0, `trimEnd` `"0%"` → `"68%"`, f10 → f40 expo | 15° to 240° (from 3 o'clock, counter-clockwise past 12 and 9) |
| `K Donut clockwise` | `rotate` `"-90deg"`, `trimStart` `"100%"` → `"32%"`, f10 → f40 expo | 210° to 345° and 0° to 75° (from 12 o'clock, clockwise past 3 and 6) |

- 0.68 × 360° = 245°: both arcs cover that span, ending about 205° (clockwise) from their start.
- Both settle **f29** (`inspect curves`); `inspect lint` **0 errors, 0 warnings, 0 notes**.

## Traps

- `rotate` is positive **clockwise**. The old stored rotation was positive counter-clockwise, which is why the 0.1.6 measurements say +90° (data-viz measured geometry,
  [data viz pack](../../ai/patterns/data-viz.md#measured-geometry-facts-016)).
- Dash and gap don't animate; segmented rings need one arc per segment:
  [KI-147](../../ai/references/known-issues.md#ki-147).
- Shapes larger than the comp are cropped: [KI-137](../../ai/references/known-issues.md#ki-137).

## In Carvercat

- Library: `Donut - fill` ([dv-donut](../../ai/patterns/dv-donut.md)), `Gauge` ([dv-gauge](../../ai/patterns/dv-gauge.md)),
  `Progress rings` ([dv-progress-rings](../../ai/patterns/dv-progress-rings.md)).
- Keys `trimStart`, `trimEnd`, `trimOffset` (%, old `trim.start`/`trim.end`/`trim.offset` as 0 to 1): [stroke and trim](../../ai/references/effects/stroke-and-trim.md).
- Background: [data stories](../genres/data-stories.md), [line drawing](../techniques/line-drawing.md).
