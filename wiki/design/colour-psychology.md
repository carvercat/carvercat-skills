---
id: design/colour-psychology
title: Colour psychology and palettes
section: design
tags: [colour, color, palette, psychology, meaning, 60-30-10, accent, harmony, linear light, hex]
styles: [all]
topics: [colour, brand]
related: [design/contrast, design/visual-hierarchy, principles/solid-drawing-2d, techniques/faux-3d]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Color_psychology, https://www.adobe.com/in/creativecloud/roc/blog/design/colour-meaning-design.html, https://lottiefiles.com/blog/tips-and-tutorials/color-theory-for-motion-design.md, https://www.schoolofmotion.com/blog/color-theory-after-effects]
---

# Colour psychology and palettes

Colour sets mood before a single word is read. But colour "meanings" are learned, not universal: they
change with culture, context, saturation and the colours around them. Use them as a starting vocabulary
and test with the actual audience in mind.

## The idea

| Family | Common associations (Western-leaning) | Watch out |
|---|---|---|
| Red | energy, urgency, appetite, danger, sale | aggression; in finance "down"; in some cultures luck and celebration |
| Orange | warmth, friendliness, creativity, value | can read cheap if saturated everywhere |
| Yellow | optimism, attention, caution | legibility on white; jealousy in some cultures |
| Green | growth, health, money, go, nature | "up" in finance; overused for eco |
| Blue | trust, calm, technology, corporate | cold; the default of every bank and SaaS |
| Purple | luxury, imagination, spirituality | mourning in some cultures |
| Black / near-black | premium, power, night, cinema | heavy on long pieces |
| White / off-white | clean, minimal, medical, space | sterile without warm accents |

- **Saturation and value change meaning more than hue**: a dusty red is calm, a neon red is alarm.
- **Context wins**: red in a sports package reads as energy; in a dashboard it reads as a problem.
- **The 60-30-10 split**: about 60% dominant (background), 30% secondary (panels, shapes), 10% accent
  (the call to action, the hero word).

## Rules of thumb

- One accent colour per frame, used for the one thing that matters.
- Build the palette in roles (background, surface, text, muted text, accent, positive, negative) before
  choosing hues ([colour craft](../../ai/references/craft/colour.md)).
- Check values in greyscale; similar values "buzz" at edges, so shift one by 10–40% brightness.
- Gradients: neighbouring hues (analogous) look smooth; opposite hues through grey look muddy.
- Data colours: one hue for the subject, grey for the context; never rely on red/green alone.

## Measured in Carvercat: colour values are linear light

The project file stores colours as **linear** RGB, and the renderer converts them back for display with the
**BT.709** transfer curve. Patches rendered with `carvercat_render` and read back pixel by pixel:

| Stored value | Rendered pixel |
|---|---|
| `[0.5, 0.5, 0.5]` | 180, 180, 180 |
| #808080 converted with the sRGB curve (0.2158) | **115**, 115, 115 (not 128) |
| #F2B03C converted with the sRGB curve | 240, 167, 44 (#F0A72C, not #F2B03C) |
| #F2B03C divided by 255 (not converted) | 248, 212, 121 (washed out) |
| white at `opacity` 0.5 over black | 180, 180, 180 |

**In design units you do not convert**: `fill: "#F2B03C"` (or `"rgb(242 176 60)"`, `"orange"`) is a colour *as displayed*, and the app converts it for you.
Checked on a headless Carvercat 0.1.8 build: `fill` `"#808080"` rendered (128, 128, 128), `"#F2B03C"` rendered (242, 176, 60), a white rectangle at
`opacity` 0.5 over black rendered (180, 180, 180). Only a raw `[r, g, b]` array is still linear light. The rows above are what the stored arrays do, and what
an old script has to avoid: (1) hex must be converted to linear before writing a raw array, (2) the conversion must be the BT.709 one the
renderer uses (`linear = v/4.5` below 0.081, else `((v + 0.099)/1.099)^(1/0.45)`), as `cc_scene.linear_hex`
does. The sRGB formula in `json_author/cc.py`'s `lin()` renders mid-tones about 13 levels (10%) darker in 8-bit
([KI-141](../../ai/references/known-issues.md#ki-141)). Also, 50% opacity of white over black is the
same 180 grey as a stored 0.5: blending happens in linear light, so fades look lighter in the middle than a
designer used to sRGB blending expects.

## Do and don't

- Do define the palette as hex in one place and write it as a CSS colour string; the app does the BT.709 conversion.
- Do test the accent in context (on the real background, next to the real text).
- Don't trust a single "meaning" table for a global audience.
- Don't use more than one saturated accent per frame.

## Checklist

- [ ] Palette defined in roles; accent used once per frame.
- [ ] All text/background pairs meet [contrast](contrast.md) minimums.
- [ ] Colours written as CSS strings (raw arrays converted with BT.709), verified with a rendered frame if exact brand colour matters.
- [ ] Greyscale check passes.

## In Carvercat

- Colour keys: `fill` (shape or text) and `stroke` (shape stroke or text outline) take `#rgb`, `#rrggbb`, `#rrggbbaa`, `rgb()`, `hsl()`, a name, `none`, or a CSS gradient
  (`"linear-gradient(90deg, #ff7a00 0%, #1b1b1b 100%)"`); wide-gamut colours are refused (`wide-gamut`). Old names, accepted for one release: `shape.fill.color`, `shape.stroke.color`,
  `text.fill.color`, `text.outline.color` (RGBA, **linear**), the `fill` and `stroke` effects' `Colour`; gradients in `shape.fill.gradient` with stops.
- Hex through the toolkit: `cc_scene` accepts hex and converts with BT.709 ([creative controls](../../ai/references/app/creative-controls.md)); not needed for CSS strings.
- Verify a brand colour: `carvercat_render {dir, from, to}` writes PNG frames; compare the pixel with the
  brand hex.
- Palettes per style: [style families](../../ai/references/craft/style-families.md).
- Lab: comp `C Colour` in [the accessibility lab](../labs/README.md).
