---
id: cookbook/glint-sweep
title: Sweep a glint across a logo
section: cookbook
tags: [glint, shine, sheen, light sweep, gleam, logo, premium, mask]
styles: [minimal-luxury, corporate-brand, sports, retro]
topics: [masking, light]
related: [techniques/gradients-in-motion, techniques/masking, cookbook/logo-sting, cookbook/reveal-image-through-text]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://blog.frame.io/2018/02/12/animated-masks-after-effects/, https://www.framer.com/marketplace/components/advanced-text-reveal/]
---

# Sweep a glint across a logo

**Goal.** A band of light slides across a logo or word, only on the letters, once.

## Steps

1. The logo text as usual.
2. The **sheen**: a tall narrow rectangle (90 × 500 px), white at `opacity` 0.8, `rotate` `"20deg"` (clockwise; the 0.1.6 note said −20°).
3. A **copy** of the logo text on top of the sheen, as its matte: on the sheen `property.set {key: "mask", value: "<copy>"}` (the copy is the mask, and text can be one), then
   `parent.clear {ids: ["<copy>"]}`.
4. Key the sheen's `x` (its left edge: the centre minus 45 px) from **fully left of the first letter to fully right of the last** (allow half the
   sheen's slanted width, about 135 px here, on each side), 30 f, S-curve.
5. Once per appearance. A glint every few seconds becomes a tic.

## Measured in Carvercat 0.1.6

Comp `K Glint` in [cookbook lab 3](../labs/README.md#cookbook-lab-3carverproj): "NORTHWIND" 200 px
ExtraBold #F2B03C, sheen centre 200 → 1720 over f10–f40 (`x` 155 → 1675).

- `carvercat_inspect composite`: the sheen shows on the letters **f15–f34** and nowhere else; 0 pixels
  before and after.
- `carvercat_render` f25: under the sheen the letters are (242, 230, 217); the rest of the letters
  (242, 176, 60); the background around them unchanged (16, 20, 24) at every sample.
- First try, sheen centre 360 → 1560: it sat on the "N" at f10 and was still on the "D" at f40: start and end
  must be off the letters.
- `inspect lint`: 0 errors, 1 warning: `text_overlap` between the logo and its matte copy. Expected, the
  matte is not drawn.

## Traps

- Lint ignores masks: [KI-133](../../ai/references/known-issues.md#ki-133).
- The old gradient offset and angle controls don't render, so a gradient-sheen version can't be moved by offset; move the
  shape: [KI-111](../../ai/references/known-issues.md#ki-111).
- The old rectangle `angle` is not drawn; `rotate` turns it:
  [KI-057](../../ai/references/known-issues.md#ki-057).

## In Carvercat

- Curve names on this page (S-curve) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Light sweep` ([ml-light-sweep](../../ai/patterns/ml-light-sweep.md)), `Chrome title`
  ([rt-chrome-title](../../ai/patterns/rt-chrome-title.md)).
- Background: [gradients in motion](../techniques/gradients-in-motion.md), [masking](../techniques/masking.md).
