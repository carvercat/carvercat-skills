---
id: cookbook/zoom-through-transition
title: Zoom through from one scene into the next
section: cookbook
tags: [zoom transition, zoom through, push in, scale transition, nested comp, motion blur, scene change]
styles: [kinetic-typography, social-short-form, sports, futuristic-hud]
topics: [transitions, structure]
related: [cookbook/wipe-transition, cookbook/iris-wipe, techniques/nested-comps-and-time, techniques/motion-blur]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Wipe_(transition)]
---

# Zoom through from one scene into the next

**Goal.** The camera seems to rush into scene A, and scene B arrives out of the rush, still moving
forward, then settles.

## Steps

1. Both scenes as comps, placed as instances: A below, B above, B's clip starting where A is at about
   2× scale.
2. A: scale 1 → 4, **accelerate**, 14 f, then on to 6 (`linear`) for as long as B is still growing. Keep A
   opaque: it fills the edges behind B.
3. B: scale 0.5 → 1, **expo out**, 16 f; opacity 0 → 1 over its first 4 f.
4. `motionblur` (shutter 180) on both instances sells the speed.
5. End A's clip once B is full-frame.

## Measured in Carvercat 0.1.6

Comp `K Zoom through` in [cookbook lab 7](../labs/README.md#cookbook-lab-7carverproj): A f10–f36, B from f20;
`inspect probe` (instance width) and `carvercat_render`:

| Frame | 14 | 18 | 20 | 22 | 24 | 28 | 32 | 36 |
|---|---|---|---|---|---|---|---|---|
| A width (px) | 2188 | 3121 | 3979 | 5307 | 7680 | 8960 | 10240 | – |
| B width (px) | – | – | 960 | 1514 | 1753 | 1893 | 1918 | 1920 |
| B opacity | – | – | 0 | 0.5 | 1 | 1 | 1 | 1 |

- Rendered edge pixels at f22 and f26 show scene A's zoomed colour, never black: A behind B covers the
  border while B is smaller than the frame. B fills the frame from **f36**.
- `inspect qc`: no flash findings. `inspect lint`: **0 errors, 0 warnings, 0 notes**.

## Traps

- If A fades out while B is still smaller than the frame, the comp background shows as a black border
  around B (seen in this lab's first version).
- Instances ignore a parent's transform, so key the instances, not a camera null:
  [KI-119](../../ai/references/known-issues.md#ki-119).
- Instance scale is about the master's centre for a frame-sized inner comp
  ([nested comps and time](../techniques/nested-comps-and-time.md)).

## In Carvercat

- Curve names on this page (expo out, accelerate) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Exit zoom through`, `Zoom past`, `Zoom settle`; the zoom-through pattern
  [tr-zoom-through](../../ai/patterns/tr-zoom-through.md) and [kt-zoom-through](../../ai/patterns/kt-zoom-through.md).
- Background: [motion blur](../techniques/motion-blur.md), [wipe transition](wipe-transition.md).
