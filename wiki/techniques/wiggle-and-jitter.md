---
id: techniques/wiggle-and-jitter
title: Wiggle, shake and jitter
section: techniques
tags: [wiggle, shake, jitter, noise, random, camera shake, hand-held, boil, lint]
styles: [glitch, cartoon-bounce, funky, sports, retro]
topics: [motion, noise]
related: [principles/straight-ahead-and-pose-to-pose, techniques/camera-moves-2d, principles/weight, accessibility/motion-sensitivity]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://blog.cg-wire.com/camera-work-in-animation/, https://wavemotioncannon.com/2016/12/31/an-introduction-to-framerate-modulation/]
---

# Wiggle, shake and jitter

Small random motion adds life or tension: a camera shake on impact, a hand-drawn "boil" on a cartoon line, a
nervous glitch, a sticker that never quite sits still. The difference between intended wiggle and accidental
jitter is amplitude and timing: deliberate noise is visible and has a rhythm; accidental jitter is a pixel
of wobble that just looks broken.

## The idea

- **Shake** (impact): large, fast, decaying; a few frames only.
- **Wiggle** (life): small, slow, continuous; new random target every few frames, eased between them.
- **Boil** (hand-made): tiny, stepped (Hold keys) every 2–3 frames, like redrawn lines.
- **Jitter** (error): sub-pixel back-and-forth every frame. Avoid it.

## Rules of thumb

| Use | Amplitude | New value every | Easing |
|---|---|---|---|
| Impact shake | 8–20 px, decaying to 0 | 1–2 f, for 6–10 f | `linear` or `hold` |
| Life wiggle | 2–8 px, 1–3° | 6–12 f | S-curve |
| Boil | 1–2 px | 2–3 f | `hold` |
| Glitch | 10–40 px | 1–2 f, in bursts under 0.5 s | `hold` |

- Generate the random keys with a fixed seed so revisions are repeatable.
- Shake the camera null, not each element ([camera moves](camera-moves-2d.md)).

## Measured in Carvercat

Eight dots with random position keys (seeded), checked with `carvercat_inspect {mode:"lint"}`:

| Amplitude | New value every | Lint |
|---|---|---|
| ±1 px | 1 f (`linear`) | **warning `jitter`**: "23 sub-pixel reversals" |
| ±2 px | 1 f | nothing |
| ±4 px | 1 f | info `speed_jump` |
| ±8 px | 1 f | info `speed_jump` |
| ±8, ±20, ±40 px | 3–6 f (S-curve) | nothing |

- Lint's `jitter` check catches the accidental kind: tiny reversals every frame. Deliberate shakes of a few
  pixels or more pass, with at most an info note about speed jumps.
- A ±1 px wiggle is not visible as motion anyway; if lint calls it jitter, either make it bigger and slower or
  remove it.

## Do and don't

- Do decay impact shakes quickly; a shake that does not decay reads as an earthquake.
- Do keep life wiggles slow and small on anything with text.
- Don't wiggle every element; one wiggling thing per frame is plenty.
- Don't shake full-frame for long (motion sickness, [motion sensitivity](../accessibility/motion-sensitivity.md)).

## Checklist

- [ ] Amplitude and interval chosen from the table.
- [ ] Random keys generated from a fixed seed.
- [ ] `inspect lint` shows no `jitter` warning.

## In Carvercat

- Curve names on this page (S-curve) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Generate keys in a script (seeded random values on `x` and `y` or `rotate`) and write them
  into the project file; Carvercat has no expression-driven wiggle.
- Ready-made: `Slide in - wiggle` ([Funky](../../ai/patterns/funky.md)), stepped glitches ([Glitch](../../ai/patterns/glitch.md)),
  on-twos boil ([Retro](../../ai/patterns/retro.md)).
- Lab: comp `W Wiggle` in [the measurement lab 4](../labs/README.md).
