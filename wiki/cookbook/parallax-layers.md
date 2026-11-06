---
id: cookbook/parallax-layers
title: Pan across three parallax layers
section: cookbook
tags: [parallax, depth, layers, pan, landscape, background, side scroll, camera move]
styles: [explainer, retro, minimal-luxury, cartoon-bounce]
topics: [depth, composition]
related: [techniques/parallax, techniques/camera-moves-2d, techniques/faux-3d, cookbook/background-drift]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Parallax_scrolling]
---

# Pan across three parallax layers

**Goal.** A sideways camera move over a landscape where far hills crawl, middle hills move faster and the
near ground moves fastest, which reads as depth.

## Steps

1. A static sky (and sun): the infinitely far layer doesn't move.
2. Three layers of filled paths, far to near, each moving left `linear` over the whole shot by **1 : 2 : 4**
   (here 60, 120 and 240 px in 90 f).
3. Each layer must still cover the frame at its last position: build it 240 px wider than the frame, **out
   of pieces no wider than the comp** (here two pieces per layer, overlapping 4 px).
4. Darker, more saturated near layers and lighter far layers add to the depth.

## Measured in Carvercat 0.1.6

Comps `K Parallax` (two pieces per layer) and `K Parallax wide` (one 2400 px piece per layer) in
[cookbook lab 7](../labs/README.md#cookbook-lab-7carverproj); `inspect probe` and `carvercat_render` at f89:

| Layer | Speed (px/frame) | Right edge at f89, pieces | Right edge at f89, one 2400 px piece |
|---|---|---|---|
| Far hills | 0.666 | hill (201, 143, 122) | sky (242, 201, 160) |
| Mid hills | 1.334 | hill (140, 90, 96) | sky |
| Near ground | 2.666 | ground (61, 43, 58) | sky |

- The speeds are exactly 1 : 2 : 4.
- The single wide pieces were **cut to a comp-sized box**: the right edge showed sky on every row from f30, and
  by f89 the last 59 px of the frame (x 1861–1919) were sky, the far layer's 60 px of travel; the faster
  layers had pulled back further behind it. The two-piece layers still reached the edge at f89.
- `inspect lint`: 0 errors, 0 warnings, 0 notes for both; lint does not see the gap.

## Traps

- A shape larger than the comp is cropped to a comp-sized box: paths too, not only ellipses:
  [KI-137](../../ai/references/known-issues.md#ki-137).
- Parenting all layers to one moving null won't give parallax; each layer needs its own speed.
- Nested instances ignore a parent's transform: [KI-119](../../ai/references/known-issues.md#ki-119).

## In Carvercat

- Library: `Synthwave sun` ([rt-synthwave](../../ai/patterns/rt-synthwave.md)), `Pattern drift`, `Hex grid`.
- Background: [parallax](../techniques/parallax.md), [2D camera moves](../techniques/camera-moves-2d.md).
