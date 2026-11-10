---
id: techniques/film-grain
title: Film grain and noise (measured)
section: techniques
tags: [grain, film grain, noise, texture, cinematic, vhs, retro, adjustment layer, film look]
styles: [retro, minimal-luxury, glitch, futuristic-hud, social-short-form]
topics: [texture, effects, colour]
related: [techniques/directional-blur-and-speed, techniques/blend-modes, cookbook/film-look-grain-overlay, accessibility/photosensitivity]
verified: design/1 (Carvercat 0.1.10)
source_inspiration: [https://github.com/carvercat/carvercat-skills]
---

# Film grain and noise (measured)

Flat digital colour looks clean and cold. A little grain over it breaks up gradients, glues text and background into one
picture, and says "film", "tape" or "signal" without a single extra object. Too much says "damaged". The craft is the amount.

## The idea

- **Grain is a texture, not a layer of dots.** It is added to the picture itself, strongest in the mid-tones; pure black and
  pure white keep about 15 % of it, so shadows and highlights stay calm.
- **Amount is the whole look.** 0.05 to 0.12 is a quiet film finish you feel more than see; 0.2 to 0.3 is old print or tape;
  above 0.4 is distress, for glitch and found-footage looks.
- **Size says the medium.** A fine cell (1 to 2 px) is fine film or a sensor; 3 to 4 px is tape and low-light video; 6 px and up is a
  deliberate coarse stylisation.
- **Colour says the age.** Colour 0 is mono grain (film stock), 0.6 is chroma noise (tape, a cheap camera).

## Measured in Carvercat (design/1)

A flat `#808080` ground with an adjustment layer above it (verified: film-grain, `wiki/tools/verify_keyed_pages.py`); a 900 x 480 px
patch rendered at 1920 x 1080 and read per pixel. Std is the standard deviation of the green channel, as a share of 255.

| `grain` | Std | Lag-1 correlation (neighbour pixels) | Red/green correlation |
|---|---|---|---|
| `"0.25 1.5px"` (the default) | 0.050 | 0.47 | 0.75 |
| `"1 1.5px"` | 0.198 | 0.47 | 0.75 |
| `"0.5 6px"` (a coarse cell) | 0.100 | 0.91 | 0.75 |
| `"0.25 1.5px colour=0"` (mono) | 0.050 | 0.47 | 1.00 |
| `none` | 0.000 | | |

- Std at mid grey is 0.2 x amount; size changes the grain's reach (lag-1), not its strength; colour changes only the
  red/green correlation.
- The mean stays at 0.502: grain adds texture, it does not lighten or darken the ground.
- Animated (the default): frame 0 and frame 1 are different pixels. With `held` they are the same pixels; the same `seed` and frame
  always give the same pixels, so a render repeats.
- Resolve and After Effects: approximate (a Fusion Film Grain and an After Effects Add Grain, measured against these numbers by the
  app); the strength, size and character match, the pixels never will.

## Rules of thumb

- Put it on an **adjustment layer** at the top of the comp, so the whole picture shares one grain.
- 0.06 to 0.08 amount and 1.5 px for a film finish; 0.2 and 2.2 px for an old print; 0.14 to 0.22, 2.5 to 3.5 px and colour 0.5 to 0.6 for tape.
- The adjustment layer goes on the master comp; inside a placed template it reaches only the template's own objects ([KI-158](../../ai/references/known-issues.md#ki-158)).
- `held` for stills and freeze frames, so nothing shimmers.
- Fade it in with the first frames (key amount 0 to the resting value over 12 to 24 f) instead of starting hard.
- Keep text contrast up: at 0.3 and over, small light text on a dark ground loses its edge.
- Judge at 100 % size on an uncropped look; grain vanishes in a thumbnail.

## Checklist

- [ ] Grain amount chosen for the medium (film, tape or digital), not left at the default.
- [ ] One grain for the whole picture (an adjustment layer), not several layers each with their own.
- [ ] Text still passes `measure.contrast` and reads at 100 %.
- [ ] `carve.preflight` read: grain is `approximate` in Resolve and After Effects (the adjustment layer adds one expected `never_visible` lint warning).

## In Carvercat

- Design key `grain` (`"0.25 1.5px softness=0.3 colour=0.25 held seed=1"`), or `grain(...)` in `filter`; keyable by name;
  `effect.add {cap: "grain"}`. Full reference: [grain](../../ai/references/effects/grain.md).
- Library: the Retro pack's `Film countdown leader` (grain on its ground, [rt-film-leader](../../ai/patterns/rt-film-leader.md)); finishing grain on
  the masters of the [retro night promo](../../ai/recipes/retro-night-promo.md), [luxury product teaser](../../ai/recipes/luxury-product-teaser.md) and
  [glitch music teaser](../../ai/recipes/glitch-music-teaser.md) recipes.
- How-to: [a film look with a grain overlay](../cookbook/film-look-grain-overlay.md).
- Background: [styles: retro](../styles/retro.md), [minimal luxury](../styles/minimal-luxury.md), [glitch](../styles/glitch.md).
