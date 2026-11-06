---
id: cookbook/gradient-background-drift
title: Drift a gradient background in a loop
section: cookbook
tags: [gradient, animated gradient, background, mesh, colour drift, loop, ambient, gradientStart]
styles: [saas-ui, minimal-luxury, social-short-form, corporate-brand]
topics: [colour, looping]
related: [cookbook/background-drift, techniques/gradients-in-motion, cookbook/seamless-loop, design/colour-transitions]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/animation-usability/]
---

# Drift a gradient background in a loop

**Goal.** A full-frame three-colour gradient whose direction slowly turns, so the colours travel around the
corners and the loop point can't be found.

## Steps

1. A full-frame rectangle with a linear gradient, three stops (deep blue, violet, coral).
2. A static gradient is `fill: "linear-gradient(60deg, ...)"`, but the gradient's start and end have no design key yet and `fill` refuses a gradient inside a key ("not a colour"), so this page keeps the stored keys: key `shape.fill.gradientStart` and `gradientEnd` (object-local fractions, y down) round the corners, the end
   always opposite the start: start (0, 0) → (1, 0) → (1, 1) → (0, 1) → (0, 0), end the reverse diagonal,
   one corner every 30 f, **S-curve**.
3. The last keys on f120 equal the first: a 120 f loop (4 s).
4. White title on top; check its contrast over the lightest moment.

## Measured in Carvercat 0.1.6

Comp `K Gradient drift` in [cookbook lab 7](../labs/README.md#cookbook-lab-7carverproj), 120 f; rendered
corner pixels with `carvercat_render` (top-left, top-right, bottom-right, bottom-left):

| Frame | Top-left | Top-right | Bottom-right | Bottom-left |
|---|---|---|---|---|
| 0 | blue 31, 42, 108 | violet 107, 62, 153 | coral 222, 107, 118 | violet 106, 61, 154 |
| 30 | violet | blue | violet | coral |
| 60 | coral | violet | blue | violet |
| 90 | violet | coral | violet | blue |
| 119 | blue 30, 42, 108 | violet 108, 62, 153 | coral 222, 107, 117 | violet 106, 61, 153 |

- The blue corner steps clockwise one corner every 30 f; f119 is within 1 level of f0 in every corner.
- `inspect qc`: `loops_cleanly: true`, seam difference **0.0**. `inspect lint contrast:true`: **0 errors,
  0 warnings, 0 notes**.

## Traps

- Stored gradient endpoints are object-local, y down; the old `cc.py` helper wrote comp y-up:
  [KI-155](../../ai/references/known-issues.md#ki-155).
- Gradient angle, offset and size controls aren't read by the renderer; move start and end instead:
  [KI-111](../../ai/references/known-issues.md#ki-111).
- The qc seam check is brightness only: [KI-140](../../ai/references/known-issues.md#ki-140).

## In Carvercat

- Curve names on this page (S-curve) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Pattern drift` ([fk-pattern-drift](../../ai/patterns/fk-pattern-drift.md)), `Rainbow stripes`, `Light sweep`.
- Background: [background drift](background-drift.md) (blurred blobs), [gradients in motion](../techniques/gradients-in-motion.md).
