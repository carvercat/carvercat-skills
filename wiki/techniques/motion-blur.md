---
id: techniques/motion-blur
title: Motion blur
section: techniques
tags: [motion blur, shutter angle, smear, fast moves, strobing, samples]
styles: [sports, social-short-form, kinetic-typography, futuristic-hud]
topics: [rendering, speed]
related: [principles/squash-and-stretch, principles/timing-and-spacing, techniques/trails-and-echoes, techniques/camera-moves-2d]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation, https://www.masterclass.com/articles/how-frame-rates-affect-film-and-video]
---

# Motion blur

A camera exposes each frame for a fraction of a second, so fast objects smear. Without blur, fast moves in
graphics look like a series of sharp copies (strobing). With the right amount, they read as one smooth
motion, and the eye accepts larger jumps between frames.

## The idea

- **Shutter angle** is the exposure as a fraction of the frame: 180° = half a frame (the film look), 360° =
  the whole frame (heavy), 90° = a quarter (crisp, sporty).
- The smear length is the distance travelled during the exposure: speed × shutter ÷ 360.
- Blur belongs on fast moves only. Slow moves gain nothing; text being read must not smear.

## Rules of thumb

- Default 180° for anything moving faster than about 1/20 of the frame width a frame (about 100 px a frame
  at 1920).
- 90° for sport and action looks that should stay crisp; 270–360° for stylised whips and transitions.
- Pair with squash and stretch on cartoon moves; the two do the same job.

## Measured in Carvercat

Four 120 px squares slid 576 px in 8 f (quad out), with the `motionblur` effect at different shutter
angles. Rendered at frame 6, when the squares move about 120 px a frame, and measured across a pixel row:

| `Shutter angle` | Visible width | Fully solid core | Smear added |
|---|---|---|---|
| none (no effect) | 122 px | 120 px | 0 |
| 90° | 150 px | 100 px | 28 px |
| 180° | 179 px | 78 px | 57 px |
| 360° | 238 px | 34 px | 116 px |

- The added smear matches speed × shutter ÷ 360 (about 120 px × 0.25, 0.5 and 1.0).
- The smear extends both ahead of and behind the object (the visible span grew on both sides), so the
  object's centre stays where its keys put it.
- `inspect probe` positions and bounds were identical with and without blur: the blur is a rendering effect,
  so check it with `carvercat_look` or a render, not with probe.

## Do and don't

- Do add blur to the moving object itself (it follows the object's own keys).
- Do check the fastest frame with a look; that is where strobing or over-smearing shows.
- Don't blur text while it should be read.
- Don't use 360° on everything; heavy blur turns fast moves into mush.

## Checklist

- [ ] Every move faster than about 100 px a frame has blur (or a deliberate strobe style).
- [ ] Shutter angle consistent across the film.
- [ ] The fastest frame checked with `carvercat_look`.

## In Carvercat

- Curve names on this page (quad out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Effect: `motionblur` with `Shutter angle` (0–360, default 180) and `Samples` (2–64, default 16); add with
  `effect.add {cap:"motionblur"}`. It sees the object's own transform motion only: a child moved by its
  parent or content inside a moving nested comp may not blur ([motion blur effect page](../../ai/references/effects/motion-blur.md)).
- Lab: comp `M Blur` in [the measurement lab 2](../labs/README.md).
