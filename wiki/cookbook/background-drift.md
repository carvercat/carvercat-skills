---
id: cookbook/background-drift
title: Keep a background alive with a slow drift
section: cookbook
tags: [background, drift, ambient, blobs, gradient, loop, blur, texture]
styles: [saas-ui, corporate-brand, minimal-luxury, social-short-form]
topics: [loops, colour, depth]
related: [techniques/gradients-in-motion, techniques/looping, principles/holds-and-stillness, cookbook/seamless-loop]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://motiondesign.school/blog/loopin-and-loopout/, https://www.schoolofmotion.com/blog/color-theory-after-effects]
---

# Keep a background alive with a slow drift

**Goal.** A background behind titles that moves just enough not to look frozen, loops, and never competes
with the text.

## Steps

1. A gradient base rectangle at frame size.
2. Two or three large soft **blobs**: ellipses (700–800 px), 55% opacity, with **Blur** (`blur: "69px"`; the old `blur.size` 60 is 69 px at 1920 wide).
3. Move each blob 150–200 px and back over the loop: keys at f0, f*N*/2, f*N*, S-curve, the last key
   equal to the first. Move blobs in different directions.
4. Keep the title's contrast against the brightest blob position (`inspect lint contrast:true`).

## Measured in Carvercat 0.1.6

Comp `K Background drift` in [cookbook lab 4](../labs/README.md#cookbook-lab-4carverproj): 120 f loop,
blob 1 moves 160 px right and 60 px down and back, blob 2 140 px left and 80 px up and back.

- `inspect probe`: blob 1 at (560, 380) on f0, (720, 440) on f60, (560.1, 380.0) on f119, the same as f1:
  a clean seam.
- `inspect qc`: `loops_cleanly: true`, mean luma difference **0.0**; frame luma 0.308–0.312 across the
  loop: the drift barely changes overall brightness.
- `inspect lint contrast:true`: 0 errors, 0 warnings, 1 note (`effect_clipped_by_frame`: blob 1's blur
  spreads **207 px** (3 × 69 px) and touches the frame edge, which is fine for a background).

## Traps

- The old gradient offset, angle, size and type controls are not rendered, so drift the shapes, not the gradient:
  [KI-111](../../ai/references/known-issues.md#ki-111).
- Shapes larger than the comp are cropped before scaling: [KI-137](../../ai/references/known-issues.md#ki-137).
- `softEdge` on a shape softens its paint permanently (and scales with the shape); use `blur` for blobs: [KI-058](../../ai/references/known-issues.md#ki-058).
- The qc seam check only compares brightness: [KI-140](../../ai/references/known-issues.md#ki-140).

## In Carvercat

- Curve names on this page (S-curve) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Pattern drift` ([fk-pattern-drift](../../ai/patterns/fk-pattern-drift.md)), `Hex grid`
  ([fh-hex-grid](../../ai/patterns/fh-hex-grid.md)), `Synthwave sun` ([rt-synthwave](../../ai/patterns/rt-synthwave.md)).
- Background: [gradients in motion](../techniques/gradients-in-motion.md), [holds and stillness](../principles/holds-and-stillness.md),
  [blur](../../ai/references/effects/blur.md).
