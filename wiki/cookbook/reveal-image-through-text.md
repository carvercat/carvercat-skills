---
id: cookbook/reveal-image-through-text
title: Reveal an image through text
section: cookbook
tags: [text mask, matte, image in text, knockout, video in text, title, mask]
styles: [kinetic-typography, minimal-luxury, corporate-brand, social-short-form]
topics: [masking, text]
related: [techniques/masking, techniques/soft-and-inverted-masks, techniques/kinetic-type, cookbook/split-screen]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://blog.frame.io/2018/02/12/animated-masks-after-effects/, https://www.framer.com/marketplace/components/text-video-reveal/]
---

# Reveal an image through text

**Goal.** A big word whose letters are windows onto a picture or footage that keeps moving inside them.

## Steps

1. Put the picture in its **own comp** and place it as a nested instance a little larger than the frame
   (scale 1.15 here), so it can drift without showing an edge.
2. Make the word: one text object, heavy weight, very large (380 px ExtraBold here). Its fill colour does
   not matter; it becomes the matte.
3. On the picture instance `property.set {key: "mask", value: "<text>"}` (text can be a mask), then `parent.clear {ids: ["<text>"]}`, so the picture can
   move on its own behind the letters.
4. Animate both, gently: the picture drifts (x +100 → −100 px over the shot, `linear`), the word settles
   from 112% to 100% (expo, 40 f).

## Measured in Carvercat 0.1.6

Comp `K Text reveal` in [cookbook lab 2](../labs/README.md#cookbook-lab-2carverproj): "OCEAN" over a
three-stop gradient with dark wave shapes, rendered with `carvercat_render` at f60 and read back:

- Outside the letters: the background colour (16, 20, 24), so nothing of the picture leaks.
- Across the first "O" at y 540: gradient teal (64, 153, 166) to (69, 162, 175) inside the stroke, the
  background again in the counter at x 720.
- Word scale settles **f25** (curves). `carvercat_look` at f0, f45, f89 shows the gradient sliding through
  the letters.
- `inspect lint`: **0 errors, 0 warnings, 0 notes**.

## Traps

- The inverse (text cut out of a plate) did not render with the old `mask.invert`:
  [KI-146](../../ai/references/known-issues.md#ki-146). `mask: {ref, invert: true}` renders for a shape mask ([soft and inverted masks](../techniques/soft-and-inverted-masks.md)); not measured with text.
- Lint ignores masks: [KI-133](../../ai/references/known-issues.md#ki-133).
- Shapes larger than the comp are cropped before scaling; build the picture comp at frame size and scale
  the instance: [KI-137](../../ai/references/known-issues.md#ki-137).
- Text needs an installed font: [KI-136](../../ai/references/known-issues.md#ki-136).

## In Carvercat

- `mask` on the object to cut (`value`: the mask's id), then `parent.clear`; old: `mask.make {ids:[mask, target]}`, the first id is the mask. Detail:
  [compositing and masks](../../ai/references/effects/compositing-and-masks.md).
- Library: `Feather wipe reveal` ([ml-feather-wipe](../../ai/patterns/ml-feather-wipe.md)) for a soft-edged
  reveal of a headline.
- Background: [masking](../techniques/masking.md), [soft and inverted masks](../techniques/soft-and-inverted-masks.md).
