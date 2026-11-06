---
id: cookbook/outline-to-fill-text
title: Reveal text from outline to fill
section: cookbook
tags: [outline text, stroke text, fill, hollow text, text reveal, title, typography]
styles: [kinetic-typography, minimal-luxury, sports, social-short-form]
topics: [text, reveal]
related: [techniques/text-outlines, techniques/kinetic-type, cookbook/focus-in, cookbook/headline-word-by-word]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://fonts.google.com/knowledge]
---

# Reveal text from outline to fill

**Goal.** A title appears as a thin outline, then fills in solid, as if the letters were inked.

## Steps

1. One text ("BOLD MOVE", 220 px Rethink Sans Bold, white). Turn on its outline: `text.outline` paint
   `solid`, colour = the fill colour.
2. **Outline in**: key `text.outline` **Thickness** 0 → 0.012 (4.4 px at 220 px; no design key yet, so the stored fraction: px = thickness × fontSize ÷ 0.597 for Rethink Sans) from f0 to f12 (decelerate). Its colour is `stroke`.
3. **Fill in**: key the text `fill` through its alpha: `"#ffffff00"` (f0) → `"#ffffff00"` (f20) → `"#ffffff"` (f36, S-curve). Verified on a headless build from master: a static `"#ffffff80"` rendered (180, 180, 180) on black and `"#ffffff00"` rendered nothing. (Old: `text.fill` **Opacity** 0 → 0 → 1 with the fill paint left `solid`:
   paint is not keyframeable, opacity is.
4. Optionally key the outline thickness back to 0 after the fill lands, for a clean solid title.

## Measured in Carvercat 0.1.6

Comp `K Outline fill` in [cookbook lab 8](../labs/README.md#cookbook-lab-8carverproj); two pixels on the centre
row of the "B": one on the letter's outer edge (x 349) and one inside the stem (x 389). RGB from rendered
frames, background (16, 20, 24):

| Frame | 0 | 6 | 12 | 20 | 24 | 28 | 32 | 36 | 40 |
|---|---|---|---|---|---|---|---|---|---|
| Edge pixel | 16 | 242 | 242 | 242 | 242 | 242 | 242 | 242 | 242 |
| Inside pixel | 16 | 16 | 16 | 16 | 95 | 172 | 223 | 242 | 242 |

- The outline is drawn from f6 while the inside stays background until f20: a true hollow title for 14 frames.
- The fill reaches full white on f36, the last key.
- `inspect lint contrast:true`: 0 errors, 0 warnings, 1 note (`repeated_key_value`, the hold key at f20).

## Traps

- `fill: "none"` is refused on a text ("not a colour name, hex, rgb() or hsl()"), and the old `text.fill` paint (`none`/`solid`) could not be keyed; fade the colour's **alpha**, as here.
- There is no trim (draw-on) for text outlines; for a drawn-on outline, trace the word as paths and use
  [draw a line along a path](draw-a-line-along-a-path.md).
- The outline adds to the letter's ink, so an outline colour different from the fill shows as a rim after the
  fill lands.

## In Carvercat

- Curve names on this page (S-curve, decelerate) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Outlined` text (outline only, fill paint `none`, thickness 0.014 = 5.2 px at 220 px) and `Dashed outline`.
- Controls: `stroke` (outline colour) and `fill` (text colour) are design keys; outline thickness, opacity and offset and the fill's opacity and paint have none yet and stay `text.outline.*` and `text.fill.*`.
- Background: [text outlines](../techniques/text-outlines.md), [kinetic type](../techniques/kinetic-type.md).
