---
id: cookbook/tile-grid-stagger
title: Stagger a grid of tiles from the centre
section: cookbook
tags: [grid, tiles, stagger, radial, ripple stagger, icons, mosaic, pop]
styles: [saas-ui, explainer, funky, futuristic-hud, data-viz]
topics: [stagger, layout]
related: [techniques/stagger-systems, design/grids-and-layout, cookbook/pop-in, cookbook/bullet-list]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/animation-duration/, https://idl.uw.edu/papers/animated-transitions]
---

# Stagger a grid of tiles from the centre

**Goal.** A grid of tiles (icons, photos, cells) that pops in as a wave spreading out from the middle.

## Steps

1. Lay the tiles out on a grid (7 × 4, 180 px pitch, 150 px tiles here).
2. For each tile, its **delay** = base + round(distance from the grid centre, in cells, × 3 f).
3. Each tile pops: scale 0 → 1, back out, 12 f, starting at its delay.
4. Stagger Text works on text only; for shapes, write each tile's keys (a short script or the project
   file does this in one go).

## Measured in Carvercat 0.1.6

Comp `K Tile grid` in [cookbook lab 4](../labs/README.md#cookbook-lab-4carverproj): 28 tiles, base f8,
3 f per cell of distance; `inspect curves` on all 28:

- Start frames ran **f10** (the four centre tiles, 0.5 cells out) to **f18** (the corners, 3.35 cells out).
- Every tile overshot **9.8%** and settled 11 f after its start: the first at f21, the corners at **f29**.
- The whole grid took 19 f (0.63 s) from first motion to the last settle.
- `inspect lint`: **0 errors, 0 warnings, 0 notes**.

## Traps

- Stagger Text cannot drive shapes or scaleX/scaleY: [KI-134](../../ai/references/known-issues.md#ki-134).
- `preset.apply` takes one `id` at a time, so presets on 28 tiles are 28 calls:
  [KI-113](../../ai/references/known-issues.md#ki-113); writing keys in the project file is faster
  ([JSON authoring](../../ai/references/app/json-authoring.md)).

## In Carvercat

- Curve names on this page (back out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Icon grid` ([ex-icon-grid](../../ai/patterns/ex-icon-grid.md)), `Waffle chart`
  ([dv-waffle-chart](../../ai/patterns/dv-waffle-chart.md)), `Hex grid` ([fh-hex-grid](../../ai/patterns/fh-hex-grid.md)).
- Background: [stagger systems](../techniques/stagger-systems.md) (orders forward, reverse, centre, edges,
  random for text), [grids and layout](../design/grids-and-layout.md).
