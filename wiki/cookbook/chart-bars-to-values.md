---
id: cookbook/chart-bars-to-values
title: Animate chart bars to their values
section: cookbook
tags: [bar chart, column chart, data, grow, baseline, stagger, values, overshoot]
styles: [data-viz, corporate-brand, explainer, saas-ui]
topics: [data, easing, stagger]
related: [genres/data-stories, genres/infographics, principles/exaggeration, cookbook/progress-bar, cookbook/count-a-number-up]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.geckoboard.com/blog/to-animate-or-not-to-animate/, https://idl.uw.edu/papers/animated-transitions]
---

# Animate chart bars to their values

**Goal.** Columns that grow up from a fixed baseline to heights that match their values, one after
another, with labels that appear as each bar lands.

## Steps

1. Draw each bar at its **full-scale** height (the axis maximum, 600 px for 1000 here) with its bottom on
   the baseline, then anchor it at the **bottom edge**: `transformOrigin` `"50% 100%"`.
2. Key scale `[1, 0]` → `[1, value / max]`. The height is then proportional to the value by construction.
3. Stagger the bars 4 f apart, 16 f each, back out (0.34, 1.56, 0.64, 1) for a small overshoot or expo out
   for none. Data purists use no overshoot: a bar briefly showing a wrong value.
4. Fade each value label in over the last frames of its bar (from +12 f), placed above the final height.

## Measured in Carvercat 0.1.6

Comp `K Chart bars` in [cookbook lab 2](../labs/README.md#cookbook-lab-2carverproj): five 140 px bars,
values 350, 600, 800, 500, 950 of 1000, baseline y 860, `carvercat_inspect` `curves` and `probe`:

| Bar | Keys | Settles | Final height | Bottom edge |
|---|---|---|---|---|
| 1 (350) | f10 → f26 | f25 | 210 px | 860 |
| 2 (600) | f14 → f30 | f29 | 360 px | 860 |
| 3 (800) | f18 → f34 | f33 | 480 px | 860 |
| 4 (500) | f22 → f38 | f37 | 300 px | 860 |
| 5 (950) | f26 → f42 | f41 | 570 px | 860 |

- Every bar overshot **9.8%** of its own height with back out: bar 5 reached 580.8 px at f40 before settling
  on 570.
- The bottom edge stayed at 860 px at every probed frame.
- `inspect lint`: 0 errors, 0 warnings, 5 notes (`speed_jump` as each bar starts from zero).

## Traps

- A shape's origin (the old `anchor` in the project file) does not move its position; the bar is drawn at full height and
  scaled about its bottom edge ([JSON authoring](../../ai/references/app/json-authoring.md#units-and-semantics-verified)).
- `scaleX`/`scaleY` cannot be staggered by the Stagger Text card, so stagger bars by their own keys:
  [KI-134](../../ai/references/known-issues.md#ki-134).
- Labels can't count up with text keys: [KI-051](../../ai/references/known-issues.md#ki-051); see
  [count a number up](count-a-number-up.md).

## In Carvercat

- Curve names on this page (expo out, back out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Column chart` ([dv-column-chart](../../ai/patterns/dv-column-chart.md)), `Bar chart`
  (Carvercat Essentials), `Ranked bars` ([dv-ranked-bars](../../ai/patterns/dv-ranked-bars.md)),
  `Stacked bar` ([dv-stacked-bar](../../ai/patterns/dv-stacked-bar.md)), preset `Grow up (Y)`.
- Background: [data stories](../genres/data-stories.md), [infographics](../genres/infographics.md),
  [exaggeration](../principles/exaggeration.md).
