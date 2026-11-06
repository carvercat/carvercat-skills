---
id: cookbook/photo-grid-diagonal-reveal
title: Reveal a photo grid in a diagonal sweep
section: cookbook
tags: [photo grid, gallery, grid reveal, stagger, diagonal, tiles, portfolio, mosaic]
styles: [social-short-form, minimal-luxury, corporate-brand, saas-ui]
topics: [stagger, layout, stills]
related: [cookbook/tile-grid-stagger, cookbook/pop-in, techniques/stagger-systems, design/grids-and-layout, principles/rhythm]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/animation-duration/]
---

# Reveal a photo grid in a diagonal sweep

**Goal.** A 4 × 3 grid of photos that appear in a wave from the top-left to the bottom-right, each tile growing
from its own centre without overshoot.

## Steps

1. Tiles 400 × 300 px (`borderRadius` 12), gap 20 px: the grid is 1660 × 940, left edge 130, top edge 70, centred. Centres
   at x 330, 750, 1170, 1590 and y 220, 540, 860.
2. **Delay by diagonal**: tile at column *c*, row *r* (from 0) starts at f **3 × (r + c)**: 0 for the corner, 15 for
   the opposite corner.
3. Each tile scales 0 → 1 over 14 f with expo out (decelerate). No overshoot, so a tile never touches its
   neighbour ([tile grid stagger](tile-grid-stagger.md) pops from the centre with back out).
4. Keys are per tile (12 tiles, 12 scale lanes); write them with a short script or the project file.

## Measured in Carvercat 0.1.6

Comp `K Photo grid` (90 f) in [cookbook lab 9](../labs/README.md#cookbook-lab-9carverproj); tile widths by `inspect probe`:

| Tile | starts | visible | 98% wide | settles (0.5%) |
|---|---|---|---|---|
| 1.1 (corner) | f0 | f1 | f8 | f9 |
| 2.1 | f3 | f4 | f11 | |
| 1.4 | f9 | f10 | f17 | |
| 2.4 | f12 | f13 | f20 | |
| 3.4 (far corner) | f15 | f16 | f23 | f24 |

- Tile 1.1 is 251.2 px wide at +2 f, 380.5 at +6 f and 400.0 at +14 f; the other tiles are the same, shifted.
- The whole grid takes **24 f (0.8 s)** from first motion to the last settle; overshoot 0.0 on every tile.
- At rest the centres are exactly 420 px apart across and 320 px apart down.
- `inspect lint`: **0 errors, 0 warnings, 0 notes**.

## Traps

- A 3 f step is a quick wave (0.8 s). 6 f feels like a slow reveal, but the last tile then lands at f39.
- A back out pop grows a 400 px tile by about 39 px at its peak (9.8%), 19.6 px each side: nearly all of the 20 px gap. Use a decelerate in tight grids.
- Photos need their own clip per tile; put the picture inside the tile with a mask
  ([rounded image card](rounded-image-card.md)).

## In Carvercat

- Curve names on this page (expo out, back out, decelerate) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Photo stack`, `Icon grid`, `Pop - gentle`, `Pop - on twos`.
- Background: [tile grid stagger](tile-grid-stagger.md), [stagger systems](../techniques/stagger-systems.md),
  [grids and layout](../design/grids-and-layout.md).
