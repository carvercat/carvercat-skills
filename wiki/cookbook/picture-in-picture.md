---
id: cookbook/picture-in-picture
title: Put a picture-in-picture inset in a corner
section: cookbook
tags: [picture in picture, pip, inset, webcam, guest, corner window, nested comp, mask, rounded]
styles: [saas-ui, corporate-brand, social-short-form, sports]
topics: [masking, layout]
related: [techniques/nested-comps-and-time, techniques/masking, cookbook/rounded-image-card, cookbook/split-screen]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Picture-in-picture]
---

# Put a picture-in-picture inset in a corner

**Goal.** A second feed (a guest camera, a screen recording) in a rounded window in the bottom-right
corner, with a white border, sliding in from the right.

## Steps

1. Each feed is its own comp. Place the main feed full-frame, and the guest as a nested instance at **scale
   0.3** (1920 × 1080 → 576 × 324 px).
2. Put the inset 48 px from the right and bottom edges: centre (1920 − 48 − 288, 1080 − 48 − 162) =
   (1584, 870).
3. A rounded window rectangle of the same size (`borderRadius` 24) at the same centre. On the inset, `property.set {key: "mask", value: "<window>"}` **at a frame where the inset is at rest**, and keep the link (no `parent.clear`) so the window
   moves with it.
4. A border: a second rectangle, same size and radius, no fill, `strokeWidth` 6, white `stroke`, on top, with the same
   position keys as the inset.
5. Slide in: position from 700 px to the right, **expo out**, 18 f.

## Measured in Carvercat 0.1.6

Comp `K Picture in picture` in [cookbook lab 5](../labs/README.md#cookbook-lab-5carverproj): inset keyed
f10–f28, mask made at f40; `inspect probe` and `carvercat_render` at f40:

- Inset 576.0 × 324.0 px at (1584, 870): it fills 1296–1872 × 708–1032, 48 px from both edges.
- Window and border had the inset's x on every sampled frame (2284.0 at f10, 1732.4 at f14, 1596.5 at
  f20, 1584.0 from f28); the slide settles at **f22**.
- Rendered pixels: (1297, 709), just outside the rounded corner, is the main feed (39, 68, 86); (1320, 740)
  is the guest (201, 87, 127); (1296, 870) on the border is white (242, 242, 240).
- `inspect lint`: 0 errors, 0 warnings, 3 notes (`speed_jump` at the slide's start).

## Traps

- Make the mask at a rest frame; made while the inset is moving, the window is offset by the same amount
  ([rounded image card](rounded-image-card.md)).
- Lint ignores masks: [KI-133](../../ai/references/known-issues.md#ki-133).
- Nested instances ignore a parent's transform, so don't move the inset through a parent null:
  [KI-119](../../ai/references/known-issues.md#ki-119).

## In Carvercat

- Curve names on this page (expo out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Split screen` ([cb-split-screen](../../ai/patterns/cb-split-screen.md)), `Product frame`,
  `Photo stack`.
- Background: [nested comps and time](../techniques/nested-comps-and-time.md), [masking](../techniques/masking.md).
