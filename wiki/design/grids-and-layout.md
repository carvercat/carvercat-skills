---
id: design/grids-and-layout
title: Grids, safe areas and layout
section: design
tags: [grid, columns, gutters, margins, safe area, rule of thirds, layout, alignment, title safe, action safe]
styles: [all]
topics: [layout, composition]
related: [design/visual-hierarchy, design/negative-space, design/visual-flow, design/gestalt, accessibility/readability]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Josef_M%C3%BCller-Brockmann, https://madegooddesigns.com/grid-systems/, https://uxdesign.cc/the-anatomy-of-a-grid-c955d5355fae, https://www.nngroup.com/articles/principles-visual-design/]
---

# Grids, safe areas and layout

A grid is a set of invisible lines that everything snaps to. It makes a sequence of frames feel like one
designed system, keeps text where screens will not crop it, and makes motion paths purposeful: things
travel along grid lines and land on them.

## The idea

- **Margins** keep content away from the edge; **columns** and **rows** divide the space; **gutters** separate
  columns. Modules are the cells where rows and columns cross.
- **Safe areas**: televisions and platforms crop or cover the edges. Action-safe keeps important action in;
  graphics-safe (title-safe) keeps text in.
- **Rule of thirds**: the four intersections of the thirds lines are strong places for a focal point.
- **Motion on the grid**: start and end poses sit on grid lines; moves travel along rows or columns, not
  random diagonals.
- A grid used across all scenes is what makes a film look like a system rather than a collage.

## Rules of thumb (1920 × 1080)

| Element | Value |
|---|---|
| Graphics-safe margin | 5%: 96 px left/right, 54 px top/bottom |
| Action-safe margin | about 3.5% |
| Columns | 12 columns for UI-like layouts, 6 for big type; gutters 24–48 px |
| Baseline rhythm | an 8 px unit for spacing; larger steps 16, 24, 32, 48, 64 |
| Vertical 9:16 (1080 × 1920) | keep text out of the top ~14% and bottom ~35% where platform UI sits ([vertical and safe areas](../../ai/references/craft/vertical-and-safe-areas.md)) |

- Align to edges, not to centres, when items have different widths (left edges line up visibly).
- Keep one alignment per frame: left-aligned or centred, not both.

## Measured in Carvercat

- **Lint's safe box** is `[96, 54, 1824, 1026]` on a 1920 × 1080 comp: 5% in from every edge (EBU R95
  graphics safe). Text whose ink crosses it gets an `outside_graphics_safe` note. Bold 40 px text placed at
  x 20 and x 60 was flagged; at x 96 and beyond it was not. Text whose top was at y 20 was flagged; at 54 and
  below it was not.
- **`carvercat_look {overlay:["safe"]}`** draws two boxes: an outer one at about 3.5% (action safe) and the
  inner 5% graphics-safe box lint uses.
- **`carvercat_look {overlay:["grid"]}`** draws a 6 × 6 grid: lines every 320 px across and 180 px down at
  1920 × 1080. Every second line is a thirds line, so the overlay doubles as a rule-of-thirds guide.

## Do and don't

- Do set margins and columns before placing anything, and reuse them in every scene.
- Do land moves on grid lines; let the grid choose the travel distance.
- Don't put text in the outer 5% of a 16:9 frame or the platform zones of a 9:16 frame.
- Don't centre everything; centred layouts are calm but static.

## Checklist

- [ ] Margins and grid defined once and used everywhere.
- [ ] `inspect lint` shows no `outside_graphics_safe` notes for text.
- [ ] `carvercat_look {overlay:["grid","safe"]}` shows key poses on grid lines.
- [ ] One alignment per frame.

## In Carvercat

- Measure placement with `carvercat_authoring {mode:"validate", checks:[{type:"bounds_inside", id, box:[96,54,1728,972]}]}`
  (box is x, y, width, height in comp pixels) and keep pairs apart with `no_overlap`.
- Place by bounds: `authoring.place_bounds` in a batch (give a `frame` for objects that start later).
- Align and distribute: `align.apply` ([mcp essentials](../../ai/references/app/mcp-essentials.md)).
- Composition rules and safe areas in depth: [composition and layout](../../ai/references/craft/composition-and-layout.md).
- Lab: comp `C Safe` in [the accessibility lab](../labs/README.md).
