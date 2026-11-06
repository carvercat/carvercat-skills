---
id: cookbook/safe-area-guides
title: Set safe-area guides for 4:5 and 1:1
section: cookbook
tags: [safe area, safe zone, guides, 4:5, 1:1, square, portrait, feed post, margins, graphics safe]
styles: [social-short-form, corporate-brand, saas-ui]
topics: [layout, delivery]
related: [design/grids-and-layout, cookbook/vertical-captions, workflow/delivery, workflow/lint-and-qc-audit]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://tech.ebu.ch/publications/r095]
---

# Set safe-area guides for 4:5 and 1:1

**Goal.** Guides on a 4:5 (1080 × 1350) and a 1:1 (1080 × 1080) comp that show where text is safe, matching
what Carvercat's lint checks, and never appearing in the render.

## Steps

1. Make the comp at its size (`comp.format {width:1080, height:1350}` for 4:5, 1080 × 1080 for 1:1).
2. **Graphics-safe box, 5% in from every edge** (the margin lint uses):
   `guide.add {axis:"x", position:54}`, `{axis:"x", position:1026}`, and on y 5% and 95% of the height:
   67.5 and 1282.5 for 4:5, 54 and 1026 for 1:1. `axis:"x"` is a vertical line at that x; positions are comp
   pixels, y down.
3. **4:5 that must also survive a square centre crop**: two more guides at y = (1350 − 1080) / 2 = **135** and
   **1215**; keep titles and logos between them.
4. `guide.lock {on:true}` when the layout is set, so a drag cannot move them; `guide.snap` makes dragged
   objects snap to them.
5. Check with `inspect lint`: any text outside the 5% box raises `outside_graphics_safe`.

## Measured in Carvercat 0.1.6

Comps `S 4:5 safe` and `S 1:1 safe` in [cookbook lab 8](../labs/README.md#cookbook-lab-8carverproj), guides
added with the commands above; texts placed with their left edge 2%, 6% and 11% in from the left.

- `carvercat_state` reads the guides back exactly: 4:5 x 54, 1026, y 67.5, 1282.5, 135, 1215; 1:1 x 54, 1026,
  y 54, 1026; `visible:true`, `locked:false`, `snap:true` by default.
- The render has **no guide lines**: the pixel on the x = 54 guide is the background (16, 20, 24) in both comps.
- `inspect lint` reports the text at 2% as `outside_graphics_safe` with the safe box
  **[54, 67.5, 1026, 1282.5]** (4:5) and **[54, 54, 1026, 1026]** (1:1), "keep text 5% in from every edge (EBU
  R95 graphics safe)". The texts at 6% and 11% raise nothing. So the 5% guides are exactly lint's box.
- `outside_graphics_safe` is a note (severity info), not a warning.

## Traps

- Guides are a view aid stored with the comp; they do not mask or crop anything.
- Lint knows no platform overlays (buttons, captions, profile crops); those zones are
  [FR-040](../../ai/references/known-issues.md#fr-040) for 9:16, and the same applies here.
- Lint's minimum text size is fixed at 18 px whatever the comp size
  ([KI-143](../../ai/references/known-issues.md#ki-143)).

## In Carvercat

- Commands: `guide.add`, `guide.move`, `guide.remove`, `guide.clear`, `guide.lock`, `guide.visible`,
  `guide.snap`, `view.rulers`; the list is in `carvercat_state` under `guides.items`.
- Background: [grids and layout](../design/grids-and-layout.md), [vertical captions](vertical-captions.md),
  [delivery](../workflow/delivery.md).
