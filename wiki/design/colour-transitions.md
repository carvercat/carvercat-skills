---
id: design/colour-transitions
title: Colour transitions
section: design
tags: [colour animation, colour keys, interpolation, linear light, complementary, grey, gradient, blend]
styles: [all]
topics: [colour, animation]
related: [design/colour-psychology, techniques/gradients-in-motion, design/contrast, accessibility/colour-vision]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.schoolofmotion.com/blog/color-theory-after-effects, https://en.wikipedia.org/wiki/Color_psychology]
---

# Colour transitions

Animating from one colour to another seems trivial until the middle frames look wrong: a red-to-green change
that passes through a dirty yellow, or a blue-to-yellow one that goes grey. What you see in between depends
on how the software mixes colours, and Carvercat mixes in linear light.

## The idea

- A colour key interpolates each channel (red, green, blue) between the two values. The path between two
  colours is a straight line in that colour space, and the middle can be duller than either end.
- **Opposite (complementary) colours meet in grey** in the middle: blue and yellow, red and cyan, green and
  magenta.
- **Neighbouring colours stay vivid**: red to orange, blue to teal.
- Mixing in **linear light** (as Carvercat does) makes midpoints brighter than the same mix in sRGB.

## Rules of thumb

- Animate between neighbouring hues, or go through a deliberate third colour (blue → white → yellow) with an
  extra key.
- For opposite hues, crossfade two objects instead of keying one colour, or cut on a beat.
- Colour changes as emphasis: 6–10 f; mood shifts across a scene: 1–3 s.
- Keep text colour changes fast and readable at every frame (contrast at the midpoint too).

## Measured in Carvercat

Rectangles with `fill` keyed over 20 f (`linear`; the keys are CSS colours, mixed in linear light), rendered at frame 10 (the midpoint) and read
back as pixels:

| Keyed from → to | Midpoint pixel |
|---|---|
| red #FF0000 → green #00FF00 | (180, 180, 0): a bright olive-yellow |
| blue #0000FF → yellow #FFFF00 | (180, 180, 180): neutral grey |

A red → green gradient (`fill: "linear-gradient(90deg, #ff0000 0%, #00ff00 100%)"`; old: `shape.fill.paint` gradient) sampled at 0, 25, 50, 75 and 100% of its width gave
(255, 0, 0), (234, 98, 0), (180, 180, 0), (97, 234, 0), (0, 255, 0). The gradient `Interpolate` setting (rgb,
hls, hsv, lab) produced **identical** pixels: it is an unavailable control in 0.1.6
([gradients in motion](../techniques/gradients-in-motion.md)). Both colour keys and gradients mix in linear
light: a 50/50 mix of full red and full green is 0.5 linear in each channel, which displays as 180.

## Do and don't

- Do check the midpoint frame of every colour animation (`carvercat_look` at the middle).
- Do insert an intermediate key when the direct path turns grey or muddy.
- Don't key opposite hues on text; the grey midpoint can fail contrast.
- Don't rely on the gradient `Interpolate` control.

## Checklist

- [ ] Midpoint frames looked at.
- [ ] Opposite-hue changes go through a chosen third colour or are crossfades.
- [ ] Text keeps contrast through the change (`inspect lint contrast:true` at the midpoint).

## In Carvercat

- Colour parameters (linear RGBA): `fill`, `stroke`, `fill`,
  `text.outline.color`; keyframeable like any value. Design names: `fill` and `stroke` as CSS colours.
- Convert hex to linear with the BT.709 curve before writing keys ([colour psychology](colour-psychology.md#in-carvercat)).
- Lab: comp `M Colour` in [the measurement lab 2](../labs/README.md).
