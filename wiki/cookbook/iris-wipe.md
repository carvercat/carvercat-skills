---
id: cookbook/iris-wipe
title: Open the next scene with an iris wipe
section: cookbook
tags: [iris, iris wipe, circle wipe, transition, reveal, mask, retro, chapter change]
styles: [retro, cartoon-bounce, funky, explainer]
topics: [transitions, masking]
related: [cookbook/wipe-transition, cookbook/cross-dissolve, techniques/masking, techniques/match-cuts]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Wipe_(transition)]
---

# Open the next scene with an iris wipe

**Goal.** Scene B opens out of a growing circle over scene A until it fills the frame.

## Steps

1. Scene A and scene B as full-frame instances, B on top.
2. A circle window **1000 px** wide at the iris centre. On B, `property.set {key: "mask", value: "<window>"}` at a frame where the
   window is open (`scale` > 0), then `parent.clear {ids: ["<window>"]}`.
3. Key the window's `scale` 0 → **2.3**, S-curve, 25 f. To cover the corners its diameter must reach the
   frame's diagonal, √(1920² + 1080²) = **2203 px** (for an iris at the centre): scale 2.203 for a 1000 px circle;
   2.3 leaves a margin.
4. Draw the circle at frame size or smaller and scale it up; don't draw a 2300 px circle.

## Measured in Carvercat 0.1.6

Comp `K Iris` in [cookbook lab 6](../labs/README.md#cookbook-lab-6carverproj): iris f15–f40 from the centre;
`inspect probe` on the window and `carvercat_render`, the four corner pixels:

| Frame | 20 | 25 | 30 | 34 | 36 | 37 | 40 |
|---|---|---|---|---|---|---|---|
| Iris diameter (px) | 239.2 | 809.6 | 1490.4 | 1966.1 | 2142.2 | **2208.6** | 2300.0 |
| Corners show | A | A | A | A | A | **B** | B |

- The corners turned to scene B on **f37**, the first frame the diameter passed 2203 px; the last 3 f of the
  25 f move only add margin.
- `inspect lint`: 0 errors, 1 warning (`cropped_at_rest` "only 39% on screen" on the window, which is a
  mask and never drawn), 0 notes.

## Traps

- A shape larger than the comp is cropped to a comp-sized box before its scale:
  [KI-137](../../ai/references/known-issues.md#ki-137).
- Lint treats a mask window that runs past the frame as drawn:
  [KI-151](../../ai/references/known-issues.md#ki-151), [KI-133](../../ai/references/known-issues.md#ki-133).
- The old `mask.invert` didn't render ([KI-146](../../ai/references/known-issues.md#ki-146)), so this page closes an iris by swapping B and A and keying the
  `scale` down. `mask: {ref, invert: true}` does render ([soft and inverted masks](../techniques/soft-and-inverted-masks.md)); not re-measured for an iris.

## In Carvercat

- Curve names on this page (S-curve) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Colour iris` ([tr-iris](../../ai/patterns/tr-iris.md)), `Bubble cover`, `Star cover`
  ([fk-star-cover](../../ai/patterns/fk-star-cover.md)), `TV switch-off`.
- Background: [wipe transition](wipe-transition.md), [masking](../techniques/masking.md).
