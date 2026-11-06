---
id: techniques/blend-modes
title: Blend modes (measured, linear light)
section: techniques
tags: [blend modes, compositing, screen, multiply, overlay, add, linear light, gamma, after effects]
styles: [all]
topics: [compositing, colour]
related: [design/colour-psychology, design/colour-transitions, techniques/masking, techniques/gradients-in-motion]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://helpx.adobe.com/uk/after-effects/desktop/work-with-transparency-and-compositing/work-with-track-mattes-and-traveling-mattes/track-mattes-and-traveling-mattes.html, https://www.schoolofmotion.com/blog/color-theory-after-effects]
---

# Blend modes (measured, linear light)

A blend mode decides how an object's colour combines with what is beneath it: Screen lightens, Multiply
darkens, Overlay adds contrast, Difference inverts. Carvercat offers 16 modes, and it computes **all of them
in linear light**. That matters: the same mode in a tool that blends encoded (gamma) values gives a visibly
different result, especially in the mid-tones.

## The idea

| Family | Modes | Typical use |
|---|---|---|
| Darken | Multiply, Darken, Color Burn | shadows, ink, paper texture, tinting |
| Lighten | Screen, Lighten, Color Dodge | light leaks, glows, flares, highlights |
| Contrast | Overlay, Soft Light, Hard Light | texture and grain over images, punchy colour |
| Inversion | Difference, Exclusion | glitch, graphic inversions, alignment checks |
| Component | Hue, Saturation, Color, Luminosity | recolouring, tinting while keeping detail |

## Rules of thumb

- Use Screen for light, Multiply for shadow, Overlay or Soft Light for texture at low opacity (10–40%).
- Linear blending makes Screen and Overlay results darker in the mid-tones than gamma blending, and Multiply
  slightly darker too; re-judge looks copied from another tool.
- Blend modes are not keyframeable in Carvercat; switch looks by crossfading two layers.

## Measured in Carvercat

**Every mode blends in linear light.** A base patch (linear `[0.2, 0.3, 0.6]`, displayed (111, 138, 197)) under a
top patch (linear `[0.8, 0.4, 0.1]`, displayed (228, 160, 74)), rendered with `carvercat_render` and compared with
the standard formulas computed both ways:

| Mode | Rendered | Formula in linear light | Formula on encoded values |
|---|---|---|---|
| Normal | 228, 160, 74 | 228, 160, 74 | 228, 160, 74 |
| Screen | 234, 194, 204 | **234, 194, 204** | 240, 211, 214 |
| Multiply | 98, 83, 54 | **98, 83, 54** | 99, 87, 57 |
| Overlay | 143, 122, 133 | **143, 122, 133** | 198, 168, 173 |
| Soft Light | 149, 127, 162 | **149, 127, 162** (W3C formula) | 156, 151, 179 |
| Hard Light | 210, 122, 83 | **210, 122, 83** | 225, 168, 115 |
| Color Dodge | 255, 180, 208 | **255, 180, 208** | 255, 255, 255 |
| Color Burn | 0, 0, 0 | **0, 0, 0** | 94, 69, 57 |
| Darken | 111, 138, 74 | 111, 138, 74 | 111, 138, 74 |
| Lighten | 228, 160, 197 | 228, 160, 197 | 228, 160, 197 |
| Difference | 197, 74, 180 | **197, 74, 180** | 118, 23, 123 |
| Exclusion | 210, 172, 194 | **210, 172, 194** | 141, 125, 157 |
| Hue | 176, 126, 66 | 177, 126, 66 | 168, 130, 81 |
| Saturation | 84, 137, 231 | **84, 137, 231** | 91, 139, 245 |
| Color | 188, 121, 0 | 189, 121, 0 | 193, 125, 39 |
| Luminosity | 157, 177, 226 | **157, 177, 226** | 146, 173, 232 |

The component modes (Hue, Saturation, Color, Luminosity) match the W3C formulas with luma weights 0.3, 0.59,
0.11 applied to linear values, within one level.

**Mid-grey example** (for converting looks to or from a tool that blends encoded values, such as a default
8- or 16-bit After Effects project). Base linear 0.18 (displays 104), top linear 0.5 (displays 180):

| Mode | Carvercat (linear) | Same mode on encoded values would give |
|---|---|---|
| Multiply | **70** (0.18 × 0.5 = 0.09 linear) | 73 |
| Screen | **196** (1 − 0.82 × 0.5 = 0.59 linear) | 211 |
| Overlay | **104** (2 × 0.18 × 0.5 = 0.18 linear) | 147 |
| Soft Light | **104** | 128 |
| Difference | **143** (0.32 linear) | 76 |

Display values use the BT.709 curve Carvercat renders with ([colour](../design/colour-psychology.md#measured-in-carvercat-colour-values-are-linear-light)).
To reproduce a Carvercat blend in an encoded-value compositor, blend in a linear working space (for example a
linearised 32-bit project) or convert values with BT.709 before and after.

## Do and don't

- Do judge blends on rendered frames; mid-tones move most.
- Do lower opacity rather than stacking several blend layers.
- Don't expect Overlay at 50% grey to be neutral: in linear light the neutral value is linear 0.5 (displays 180),
  not display 128.
- Don't use Color Dodge or Color Burn near saturated colours; they clip quickly (Burn went to black here).

## Checklist

- [ ] Blends checked on a render, at the frames where the base is darkest and brightest.
- [ ] Looks ported from or to another tool re-matched with linear vs encoded in mind.

## In Carvercat

- Parameter: `mixBlendMode` with options Normal, Screen, Multiply, Overlay, Soft Light, Hard Light,
  Color Dodge, Color Burn, Darken, Lighten, Difference, Exclusion, Hue, Saturation, Color, Luminosity (not
  keyframeable). `transform.compositing.combine` reports "no active compositing reader" in 0.1.6.
- Masks and other compositing: [compositing and masks](../../ai/references/effects/compositing-and-masks.md).
- Labs: comps `B Blend` and `B Mid grey` in [the measurement lab 3](../labs/README.md).
