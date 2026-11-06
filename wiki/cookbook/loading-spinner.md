---
id: cookbook/loading-spinner
title: Make a looping loading spinner
section: cookbook
tags: [loading, spinner, loader, throbber, progress, arc, trim, loop, busy indicator]
styles: [saas-ui, futuristic-hud, explainer]
topics: [looping, shapes, ui]
related: [cookbook/seamless-loop, cookbook/donut-fill, techniques/looping, techniques/line-drawing]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://m3.material.io/components/progress-indicators/overview, https://www.nngroup.com/articles/progress-indicators/, https://en.wikipedia.org/wiki/Throbber]
---

# Make a looping loading spinner

**Goal.** A ring spinner that loops forever: a steady arc turning, or a "breathing" arc whose head runs
ahead and whose tail catches up, both seamless at the loop point.

## Steps

**Steady arc.**

1. A circle (200 px) with no fill and a 14 px round-capped stroke, over a dim track circle.
2. `trimEnd` `"25%"` (a quarter ring; the first write adds the Trim Stroke).
3. Comp 60 f; `rotate` `"0deg"` → `"360deg"` **`linear`** from f0 to f60 (one frame past the last), so the step across
   the loop equals every other step ([seamless loop](seamless-loop.md)).

**Breathing arc.**

1. The same circle, mirrored with scale `[-1, 1]` so the trim runs clockwise (starting at 9 o'clock).
2. `trimEnd` `"5%"` → `"80%"`, S-curve, f0–f30; `trimStart` `"0%"` → `"75%"`, S-curve, f30–f60 (both keyed by name in one `anim.set`). The arc grows,
   then shrinks to the same 5% length, now sitting 75% of a turn further on.
3. Rotation must carry the arc the remaining quarter turn (plus whole turns) by the loop point: `"0deg"` → **`"450deg"`**
   `linear`, f0–f60 ((1 − 0.75) + 1 turns, clockwise).

## Measured in Carvercat 0.1.6

Comp `K Spinner` in [cookbook lab 5](../labs/README.md#cookbook-lab-5carverproj), 60 f; arcs found in frames
rendered with `carvercat_render` (angles counter-clockwise from 3 o'clock, sampled every 2 px):

| Frame | 58 | 59 | 0 | 1 | 15 | 30 | 45 |
|---|---|---|---|---|---|---|---|
| Steady arc, tail angle | 9.1° | 3.4° | 356.5° | 350.5° | 266.4° | 176.5° | 86.5° |
| Breathing arc, tail angle | 173.0° | 166.0° | 158.0° | 149.8° | 271.1° | 23.5° | 271.1° |
| Breathing arc, span | 28.4° | 25.6° | 25.5° | 25.7° | 160.4° | 294.9° | 160.1° |

- The steady arc spans 97° (90° plus the round caps) and moves about 6° clockwise a frame, across the loop
  point too (f59 → f0: 6.9° within the 2 px sampling).
- The breathing arc's tail stepped −8.0° from f59 to f0 and −8.2° from f0 to f1, and its length at f59
  (25.6°) matches f0 (25.5°): no jump at the seam.
- `inspect qc`: `loops_cleanly: true`, mean luma difference **0.0**.
- `inspect lint`: 1 **error**, `never_visible` "off frame for its whole clip" on the mirrored arc, which is
  on screen in every render.

## Traps

- A mirrored shape (negative scale) reports a negative width and `on_screen` 0, and lint calls it
  `never_visible`: [KI-154](../../ai/references/known-issues.md#ki-154).
- The qc seam check compares brightness only, so check the arc's position at the seam yourself:
  [KI-140](../../ai/references/known-issues.md#ki-140).
- An unmirrored stroke's trim starts at 3 o'clock and runs counter-clockwise ([donut fill](donut-fill.md)).

## In Carvercat

- Curve names on this page (S-curve) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Segment loader` ([fh-loader](../../ai/patterns/fh-loader.md)), `Progress rings`
  ([dv-progress-rings](../../ai/patterns/dv-progress-rings.md)), `Progress`.
- Background: [looping](../techniques/looping.md), [line drawing](../techniques/line-drawing.md).
