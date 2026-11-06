---
id: techniques/text-outlines
title: Text outlines (measured)
section: techniques
tags: [text outline, stroke, outline thickness, align, outside, centered, inside, outlined type]
styles: [funky, retro, kinetic-typography, sports, social-short-form]
topics: [text, paint]
related: [techniques/kinetic-type, design/contrast, techniques/faux-3d, design/typography-pairing]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://blog.nobledesktop.com/learn/after-effects/stroke-animation, https://www.fontshop.com/content/how-to-mix-type]
---

# Text outlines (measured)

An outline around text adds punch (sports, retro, funky), separates text from busy footage, or becomes the
whole letter in outline-only type. Getting it right means knowing how thick it really renders and on which side
of the letter edge it sits.

## The idea

- **Outline for legibility**: a dark outline 2–4 px around light text over footage.
- **Outline as style**: thick contrasting outlines (sticker, comic, retro), or outline-only letters with no fill.
- **Alignment**: outside keeps the letter shapes intact and grows them; centred eats half into the letter (but
  the fill, drawn on top, hides that half).

## Measured in Carvercat

The letter "I" in Rethink Sans Bold, white `fill`, black outline (`stroke`, opacity 1; the thickness is the stored fraction `text.outline.thickness`, which has no design name yet), rendered on mid grey and
measured across the stem (black pixels visible beyond the white stem, per side):

| Size (`fontSize`) | `Thickness` (stored) | `Align` outside | centered | inside |
|---|---|---|---|---|
| 100 px | 0.02 | 2 px | 1 px | 1 px |
| 100 px | 0.05 | 7 px | 3 px | 3 px |
| 100 px | 0.10 | 16 px | 7 px | 7 px |
| 200 px | 0.02 | 6 px | 3 px | 3 px |
| 200 px | 0.05 | 16 px | 8 px | 8 px |
| 200 px | 0.10 | 33 px | 16–19 px | 16–19 px |

- **Band width in px = `Thickness` × `fontSize` ÷ 0.597** for Rethink Sans (about 1.67 × thickness × font size). At `fontSize` 200,
  thickness 0.1 → 0.1 × 200 ÷ 0.597 = 33.5 px, measured 33 px outside. The same formula fits every row within about 1–2 px (the
  thickness column is 3.4, 8.4 and 16.8 px at 100 px type; 6.7, 16.8 and 33.5 px at 200 px). Read the lab back with `scene.get`: it gives `fontSize` 100 and 200, and the outline stays a stored fraction.
- **Outside**: the whole band sits outside the glyph. **Centered**: the band straddles the edge, half visible
  outside (the fill covers the inner half). The white stem kept its width (12 px at 100, 24 px at 200) in every
  case: the fill is drawn over the outline.
- **Inside renders exactly like centered** (same visible width in every row), although the control is listed as
  writable ([KI-148](../../ai/references/known-issues.md#ki-148)). Expect half the band to show outside the letter.

## Rules of thumb

- Legibility outline over footage: band 2–4 px at 1080p, outside, dark at 60–100% opacity.
- Style outlines: 4–10% of the font size; heavier on heavy weights only.
- For outline-only letters, make the `fill` transparent (`"#ffffff00"`; `"none"` is refused on a text; old: `text.fill.paint` none) and use centered or outside; thin weights look broken.

## Do and don't

- Do size outlines with the formula above, then check one rendered frame.
- Do prefer `outside` when letter shapes must stay intact.
- Don't rely on `inside` alignment in 0.1.6.
- Don't outline small body text heavily; counters fill in.

## Checklist

- [ ] Band width computed (thickness × size × comp width) and checked on a render.
- [ ] Alignment outside or centered, never relying on inside.

## In Carvercat

- Design keys: `stroke` (the outline colour on a text) and `fontSize` (px, a true em size). No design name yet, so these stay stored:
  `text.outline.paint` (none, solid, gradient), `opacity`, `thickness` (0–0.2, a fraction, keyframeable; px = thickness × fontSize ÷ 0.597 for Rethink Sans),
  `align` (inside, centered, outside), `corners`, `outsideOnly`. `strokeWidth` is refused on a text ("not a shape").
- More text paint: [text paint](../../ai/references/effects/text-paint.md); ready-made outlined type: `Offset shadow title`
  ([fk-offset-title](../../ai/patterns/fk-offset-title.md)).
- Lab: comp `P Outline` in [the measurement lab 5](../labs/README.md).
