---
id: cookbook/before-after-slider
title: Slide a before/after divider across two images
section: cookbook
tags: [before after, comparison, slider, divider, reveal, wipe, mask, makeover, product demo]
styles: [saas-ui, explainer, social-short-form, data-viz]
topics: [masking, layout]
related: [techniques/masking, cookbook/split-screen, cookbook/wipe-transition, genres/product-launches]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Wipe_(transition)]
---

# Slide a before/after divider across two images

**Goal.** "Before" on the left, "after" on the right, split by a vertical line with a handle that sweeps
across, revealing more of one or the other.

## Steps

1. Both scenes as comps, placed full-frame: **Before** below, **After** above.
2. A full-frame window rectangle (1920 × 1080) over the After instance, anchored on its **right edge**
   (`transformOrigin` `"100% 50%"`). `property.set {id: "<After>", key: "mask", value: "<window>"}`, then `parent.clear {ids: ["<window>"]}`.
3. Pick the divider positions as fractions *v* of the width. Key the window's `scale` `[1 − v, 1]` (it then
   covers [1920 *v*, 1920]) and the divider's centre to 1920 *v* (`x` = 1920 *v* − 3 for the 6 px line), on the **same frames with the same ease**
   (here S-curve). Scale and position interpolate the same way, so they stay locked.
4. The divider: a 6 px white rectangle the height of the frame; a 72 px white circle as the handle, keyed
   the same as the divider.
5. Labels inside each scene (top-left "BEFORE", top-right "AFTER") so they are revealed with it.

## Measured in Carvercat 0.1.6

Comp `K Before after` in [cookbook lab 5](../labs/README.md#cookbook-lab-5carverproj): *v* = 0.5 (f0–f20),
0.85 (f50), 0.15 (f80), 0.5 (f110); rendered with `carvercat_render`, scanning the ground row (y 900):

| Frame | 0 | 35 | 50 | 65 | 80 | 95 |
|---|---|---|---|---|---|---|
| Divider centre x (`inspect probe`) | 960 | 1296 | 1632 | 960 | 288 | 624 |
| First "after" pixel x | 964 | 1300 | 1636 | 964 | 292 | 628 |

- The first After pixel was **4 px right of the divider's centre at every frame**: right at the edge of the
  6 px line. The seam never showed beside the line, moving or still.
- `inspect lint`: 0 errors, 0 warnings, 3 notes (repeated key values on the hold).

## Traps

- One window masks one track: [masking](../techniques/masking.md); lint ignores masks
  ([KI-133](../../ai/references/known-issues.md#ki-133)).
- The old `mask.invert` did not change the render ([KI-146](../../ai/references/known-issues.md#ki-146)); `mask: {ref, invert: true}` does, see [soft and inverted masks](../techniques/soft-and-inverted-masks.md).
- A shape larger than the comp is cropped before its scale, so keep the window at frame size and scale it
  down, never up past 1: [KI-137](../../ai/references/known-issues.md#ki-137).

## In Carvercat

- Curve names on this page (S-curve) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Before and after` (1:1 scene), `Before after split (9:16)` ([ss-before-after](../../ai/patterns/ss-before-after.md)),
  `Comparison bars` ([dv-before-after](../../ai/patterns/dv-before-after.md)), `Split screen`.
- Background: [masking](../techniques/masking.md), [split-screen](split-screen.md).
