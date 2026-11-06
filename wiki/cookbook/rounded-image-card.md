---
id: cookbook/rounded-image-card
title: Slide in a rounded image card
section: cookbook
tags: [image card, rounded corners, photo, picture in picture, mask, card, slide in]
styles: [saas-ui, corporate-brand, minimal-luxury, social-short-form, funky]
topics: [masking, layout]
related: [techniques/masking, techniques/nested-comps-and-time, cookbook/split-screen, cookbook/reveal-image-through-text]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://blog.frame.io/2018/02/12/animated-masks-after-effects/, https://www.framer.com/marketplace/components/dynamic-video-mask/]
---

# Slide in a rounded image card

**Goal.** A picture inside a rounded-corner card that rises and fades in, with the corners staying round
all the way.

## Steps

1. Place the picture (an image, or a comp as a nested instance) and set its **cover scale** so it is
   larger than the card: 0.4 × 1920 × 1080 = 768 × 432 px covers a 720 × 400 card.
2. Draw the **card window**: a rectangle 720 × 400, `borderRadius` 32.
3. Move the playhead to a frame where the picture is **at rest**, then `property.set {id: "<picture>", key: "mask", value: "<window>"}`.
   Keep the link (no `parent.clear`): the window now follows the picture.
4. Animate only the picture: position from 60 px below to rest (expo, 18 f) and opacity in over 8 f.

## Measured in Carvercat 0.1.6

Comp `K Image card` in [cookbook lab 4](../labs/README.md#cookbook-lab-4carverproj): picture instance keys
y 600 → 540 over f6–f24; `inspect probe` and `carvercat_render` at f40.

| Frame | 6 | 10 | 14 | 24 |
|---|---|---|---|---|
| Picture centre y | 600 | 552.7 | 542.6 | 540 |
| Window centre y | 600 | 552.7 | 542.6 | 540 |

- The window moved with the picture at every frame.
- Render at f40: the card's corner pixel (602, 342) is background (244, 241, 234), 14 px further in
  (616, 356) is picture: the corner is round. The edge mid-point (606, 540) is picture, (594, 540) is
  background.
- **First attempt**, mask made at f0 while the picture still sat at its start (y 600): the window kept that
  60 px offset and the card came to rest at y **480** instead of 540.
- `inspect lint`: 0 errors, 0 warnings, 2 notes (`speed_jump`).

## Traps

- Setting `mask` links the two at the playhead (as `mask.make` did): the window keeps the offset it has at that frame.
- The old `cornerRadius` capped at a quarter of the short side ([KI-121](../../ai/references/known-issues.md#ki-121)); `borderRadius` runs to half the short side (`"50%"`).
- Lint ignores masks: [KI-133](../../ai/references/known-issues.md#ki-133).
- Nested instances ignore a parent: animate the instance itself: [KI-119](../../ai/references/known-issues.md#ki-119).

## In Carvercat

- Library: `Photo stack` ([fk-photo-stack](../../ai/patterns/fk-photo-stack.md)), `Product frame`
  ([ml-product-frame](../../ai/patterns/ml-product-frame.md)), preset `Card settle`.
- Mask rules: [compositing and masks](../../ai/references/effects/compositing-and-masks.md).
- Background: [masking](../techniques/masking.md), [nested comps](../techniques/nested-comps-and-time.md).
