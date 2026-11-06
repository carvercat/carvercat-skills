---
id: cookbook/vignette
title: Add a vignette
section: cookbook
tags: [vignette, darken edges, radial gradient, focus, film look, frame, mood]
styles: [minimal-luxury, retro, corporate-brand]
topics: [colour, composition]
related: [techniques/gradients-in-motion, design/visual-flow, cookbook/title-over-footage, cookbook/background-drift]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Vignetting]
---

# Add a vignette

**Goal.** Darken the corners and edges of the frame softly so the eye goes to the middle.

## Steps

1. A full-frame rectangle on top of everything, black.
2. `fill` a **radial** CSS gradient with alpha stops: 0 at 0%, 0 at 55%, 0.65 (`a6`) at 100%. The lab comp's fill, as `scene.get` reads
   it: `"radial-gradient(ellipse 1357.645px at 50% 50%, #00000000 0%, #00000000 55%, #000000a6 100%)"`.
3. The centre is `at 50% 50%` and the radius runs to a corner, so the gradient's full radius reaches the corners.
4. Leave it static. A gradient cannot be keyed by design name yet; if it must move, key the stored `gradientStart` / `gradientEnd`.

## Measured in Carvercat 0.1.6

Comp `K Vignette` in [cookbook lab 7](../labs/README.md#cookbook-lab-7carverproj): a #E8DCC8 background,
rendered with `carvercat_render`:

| Pixel | (960, 300) | (1500, 540) | (1900, 540) | (960, 1070) | (240, 135) | (10, 10) |
|---|---|---|---|---|---|---|
| RGB | 232, 220, 200 | 232, 220, 200 | 206, 196, 178 | 206, 195, 177 | 195, 185, 168 | 139, 132, 119 |

- The middle is untouched; the corner is 40% darker.
- The right edge (940 px from the centre) and the bottom edge (530 px from it) darken the same: the radial
  gradient is measured in the rectangle's own 0–1 space, so it is an **ellipse with the frame's aspect**,
  not a circle.
- `inspect lint contrast:true`: **0 errors, 0 warnings, 0 notes**.

## Traps

- Stored gradient endpoints are object-local with y down; the old `cc.py` `gradient()` helper wrote them as comp
  coordinates: [KI-155](../../ai/references/known-issues.md#ki-155).
- The old gradient angle, size and type controls aren't read by the renderer; set the mode in the gradient and
  key start/end: [KI-111](../../ai/references/known-issues.md#ki-111).
- Because the ellipse follows the rectangle, a rounder vignette needs a less wide rectangle; don't make it
  larger than the comp, as such shapes are cropped: [KI-137](../../ai/references/known-issues.md#ki-137).

## In Carvercat

- Library: `VHS overlay` ([rt-vhs-overlay](../../ai/patterns/rt-vhs-overlay.md)), `Light sweep`.
- Background: [gradients in motion](../techniques/gradients-in-motion.md), [visual flow](../design/visual-flow.md).
