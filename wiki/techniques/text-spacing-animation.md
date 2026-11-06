---
id: techniques/text-spacing-animation
title: Animating tracking, word and line spacing
section: techniques
tags: [tracking, letter spacing, word spacing, line spacing, leading, text animation, breathe, expand]
styles: [minimal-luxury, kinetic-typography, corporate-brand]
topics: [text, typography]
related: [techniques/kinetic-type, design/typography-pairing, techniques/stagger-systems, sound-and-timing/reading-time]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://blog.typekit.com/2012/05/23/type-study-pairing-typefaces/, https://vimeo.com/305153408]
---

# Animating tracking, word and line spacing

Spacing animation is one of the quietest and most elegant text moves: a title that slowly opens its letter
spacing, a quote whose lines settle closer together, a word that tightens as it lands. It suits luxury,
brand and cinematic work, and keeps a held title alive without moving it.

## The idea

- **Tracking expand** (letters drift apart): calm, premium, "breathing". Often combined with a fade in.
- **Tracking collapse** (letters close in): focus, arrival, a word locking into place.
- **Line spacing settle**: lines start loose and settle to their final leading as a paragraph lands.
- Keep the text centred (or anchored to its alignment edge) so spacing is the only change.

## Rules of thumb

- Breathe during a hold: tracking +0.04 to +0.06 over the whole hold, `linear` or very soft.
- Expand or collapse as an entrance: about 0.3–0.6 tracking change over 20–40 f, S-curve or ease out.
- Wide tracking costs width fast; measure the final width before placing.
- Do not animate spacing on text being read quickly; it makes words jump.

## Measured in Carvercat

Three Bold texts keyed from f5 to f35 (S-curve), measured with `carvercat_authoring {mode:"geometry"}`:

| Text | Keyed | f5 | f20 | f35 |
|---|---|---|---|---|
| "MOTION DESIGN", 64 px, centred | `letterSpacing` `"0px"` → `"64.3px"` (old tracking 1.0 → 1.6) | x 719, width 482 | x 526, width 867 | x 333, width 1253 |
| "one two three", 64 px, centred | `text.font.wordSpacing` 1 → 3 (no design key) | width 386 | width 386 | width 386 |
| two lines, 56 px, centred | `lineHeight` `1.34` → `2.01` (old line spacing 1.0 → 1.5; 1.34 is normal for this font) | y 761, height 116 | y 752, height 135 | y 742, height 154 |

- **Letter spacing** grew the width by 771 px for 13 characters (12 gaps × 64.3 px; 1 em of the old tracking scale is the font size ÷ 0.597, so +0.1 of old tracking is 10.7 px at 64 px) and the text
  stayed centred: its centre held at x 960 at every frame.
- **Line spacing** grew the block symmetrically around its position (top moved up 19 px as height grew 38 px).
- **Word spacing did not change the render.** `carvercat_authoring {mode:"controls"}` reports it as "Resolve-only
  mapping; native text preview does not apply word spacing" ([KI-145](../../ai/references/known-issues.md#ki-145)). Use tracking, or separate
  words, to open gaps between words.

## Do and don't

- Do measure the widest frame of a tracking animation against the safe area.
- Do combine a tracking expand with a slow fade for luxury titles.
- Don't key word spacing; it has no effect in Carvercat's own render.
- Don't change line spacing on captions; it moves every line.

## Checklist

- [ ] Final width fits graphics-safe (`inspect lint` or `bounds_inside` at the last frame).
- [ ] Spacing changes slow enough to read through.
- [ ] No word-spacing keys.

## In Carvercat

- Curve names on this page (S-curve) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Parameters: `letterSpacing` in px, pt or em (`normal` is 0), `lineHeight` as a multiple of `fontSize` (`1.2`, `"120%"`) or a length (`"24px"`; `normal` is 1.34 for
  this font), both keyframeable and rendered; `wordSpacing` has no design key and `text.font.wordSpacing` is stored but not rendered natively in 0.1.6.
  Old names, accepted for one release: `text.font.tracking` (1 is normal, 0 to 5) and `text.font.lineSpacing` (1 is normal, 0 to 5).
- Ready-made: `Tracked title` ([ml-tracked-title](../../ai/patterns/ml-tracked-title.md)), `Focus pull`
  (letter spacing from 64 px at 64 px type, [kt-focus-pull](../../ai/patterns/kt-focus-pull.md)); measured static widths per tracking
  value: [typography craft](../../ai/references/craft/typography.md).
- Lab: comp `T Spacing` in [the measurement lab 3](../labs/README.md).
