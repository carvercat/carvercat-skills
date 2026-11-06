---
id: techniques/parallax
title: Parallax
section: techniques
tags: [parallax, depth, layers, 2.5d, foreground, background, drift, camera]
styles: [all]
topics: [depth, camera]
related: [techniques/camera-moves-2d, techniques/faux-3d, principles/solid-drawing-2d, accessibility/motion-sensitivity, techniques/looping]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://80.lv/articles/inside-the-making-of-2-5d-parallax-animation-for-music-artist, https://aejuice.com/blog/how-to-create-parallax-effect-in-after-effects, https://petapixel.com/2013/11/19/creating-motion-stills-animate-photo-post-parallax-effect, https://uxmag.com/articles/creating-usability-with-motion-the-ux-in-motion-manifesto]
---

# Parallax

When the viewpoint moves, near things slide past faster than far things. Giving flat layers different
speeds in the same direction creates depth from 2D artwork: the "2.5D" look of animated photos, layered
landscapes and premium product scenes.

## The idea

- Speed is proportional to nearness: background slow, middle medium, foreground fast.
- All layers move the same direction (opposite to the imagined camera move).
- Scale and blur agree with speed: near layers are larger and may be slightly soft; far layers are smaller
  and less saturated.
- A pure zoom on one flat image is not parallax; layers must move at different rates.

## Rules of thumb

- Three planes are enough: background 1×, middle 2×, foreground 3–4× (or 1 : 1.5 : 2 for subtle work).
- Keep background travel small: 1–3% of frame width per second for ambient holds.
- Use `linear` for continuous drifts inside a held scene; ease the whole move if the "camera" starts and
  stops inside the shot.
- Overscan: layers that travel need extra artwork beyond the frame edge (travel distance + 5%).
- For viewers sensitive to motion, keep parallax gentle and short (see [motion sensitivity](../accessibility/motion-sensitivity.md)).

## Measured in Carvercat

Three rows of cards, each row keyed by `x` and `y` over 90 f with `linear`:

| Plane | Card size | Travel in 90 f | Speed |
|---|---|---|---|
| Far | 80 px | 200 px | 2.2 px a frame |
| Mid | 140 px | 400 px | 4.4 px a frame |
| Near | 240 px | 800 px | 8.8 px a frame |

Speeds 1 : 2 : 4 with sizes 1 : 1.75 : 3 read as clear depth in `carvercat_look`.

## Do and don't

- Do decide plane speeds as ratios and keep them for the whole scene.
- Do darken, desaturate or soften far planes slightly.
- Don't use more than three or four speeds; extra planes look like noise.
- Don't let foreground elements cross the main subject while it is being read.

## Checklist

- [ ] All planes move in the same direction.
- [ ] Speed, size and contrast agree on depth.
- [ ] No plane runs out of artwork before the shot ends (`carvercat_look` at the last frame).
- [ ] Drift is slow enough to read text placed over it.

## In Carvercat

- Per layer: key `x` and `y` with `linear` (ambient drift) or S-curve (a move that
  starts and stops); or parent each plane's objects to a plane [null object](null-object.md) and key the nulls.
- One move for the whole scene: parent planes to a camera null and give each plane a different travel; see
  [camera moves in 2D](camera-moves-2d.md). Nested-comp instances ignore their parent
  ([KI-119](../../ai/references/known-issues.md#ki-119)): key them directly.
- Depth softness: `blur` `"2.3px"` to `"6.9px"` (the old Blur `Size` 2–6) on the near or far plane ([blur](../../ai/references/effects/blur.md)).
- Ambient drift presets: `Drift up - 4 s` ([Minimal Luxury](../../ai/patterns/minimal-luxury.md)),
  `Photo push - 5 s` ([Corporate Brand](../../ai/patterns/corporate-brand.md)).
- Lab: comp `T Parallax` in [the techniques lab](../labs/README.md).
