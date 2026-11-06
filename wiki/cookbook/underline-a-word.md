---
id: cookbook/underline-a-word
title: Underline a word as it is said
section: cookbook
tags: [underline, emphasis, line, trim, draw on, round cap, text]
styles: [kinetic-typography, explainer, minimal-luxury, corporate-brand, funky]
topics: [text, stroke, emphasis]
related: [techniques/line-drawing, techniques/stroke-dashes, cookbook/highlight-a-word, cookbook/draw-a-line-along-a-path]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://pixelbakery.com/recipes/trim-paths-animate-text, https://blog.nobledesktop.com/learn/after-effects/stroke-animation]
---

# Underline a word as it is said

**Goal.** A line that draws itself under a word, exactly as wide as the word.

## Steps

1. Measure the word with `carvercat_authoring mode:geometry detail:"bounds"` (x, width, bottom).
2. Draw a **2-point path** 14 px below the bottom of the letters, stroke 8 px, fill none.
3. **Round caps add half the stroke width at each end.** With round caps, inset each end by half the
   stroke (4 px for 8 px); with butt caps use the word's edges as they are.
4. `trimEnd` `"0%"` → `"100%"` over 10–12 f, expo out, starting on the word's spoken frame.

## Measured in Carvercat 0.1.6

Comp `K Underline` in [cookbook lab 3](../labs/README.md#cookbook-lab-3carverproj): "underline this", 96 px
Bold, bounds x 678.3–1241.6; two 8 px underlines, rendered at f40 and scanned for ink:

| Line | Path endpoints | Inked from → to |
|---|---|---|
| Round cap | 682.3 → 1237.6 (inset 4 px) | **678 → 1241** |
| Butt cap | 678.3 → 1241.6 | **678 → 1241** |

- Both lines match the word's width once the round line is inset by half its stroke.
- Draw-on f14 → f26 expo: first ink f15, 98% drawn **f21**.
- `inspect lint`: **0 errors, 0 warnings, 0 notes**.

## Traps

- Geometry bounds stop at the last glyph, so measure the word alone, without a trailing space:
  [KI-149](../../ai/references/known-issues.md#ki-149).
- Dash length and gap can't be keyed: [KI-147](../../ai/references/known-issues.md#ki-147).

## In Carvercat

- `trimEnd` keys by design name: `anim.set {id, keyframes: [{at, trimEnd: "0%", ease}, {at, trimEnd: "100%"}]}`, `ease` on the key that leaves (checked: `wiki/tools/verify_keyed_pages.py`, case draw-a-line-along-a-path). A static `trimEnd` is one call. The older stored key `trim.end` (0 to 1) still works.
- Curve names on this page (expo out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Underline` and `Scribble circle` stickers (Carvercat Essentials), `Squiggle underline`
  ([fk-squiggle-underline](../../ai/patterns/fk-squiggle-underline.md)), `Impact stack`
  ([kt-impact-stack](../../ai/patterns/kt-impact-stack.md)).
- Background: [line drawing](../techniques/line-drawing.md), [stroke dashes](../techniques/stroke-dashes.md).
