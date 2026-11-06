---
id: cookbook/slow-motion-hold
title: Fake a slow-motion hold (speed ramp)
section: cookbook
tags: [slow motion, speed ramp, hold, drift, fly through, time ramp, bullet time, title]
styles: [kinetic-typography, sports, social-short-form, glitch]
topics: [timing, easing]
related: [principles/holds-and-stillness, principles/slow-in-slow-out, principles/timing-and-spacing, techniques/nested-comps-and-time]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Slow_motion]
---

# Fake a slow-motion hold (speed ramp)

**Goal.** A title rockets in, nearly stops and drifts slowly through the middle for two seconds as if time
slowed, then rockets out: a speed ramp done with keys.

## Steps

1. Four position keys: off-screen left → just left of centre (fast, 14 f) → just right of centre (slow,
   60 f) → off-screen right (fast, 14 f).
2. The middle segment `linear`: here 200 px in 60 f, **3.3 px a frame**. That steady creep is the "slow
   motion".
3. The entry segment eases out **into the drift speed**, not to a stop, and the exit eases in **from** it.
   With a custom curve the end slope can match: entry `(0.2, 0.6, 0.5, 0.985)`, exit
   `(0.5, 0.015, 0.8, 0.4)` (end slope = drift × segment frames / segment distance = 0.03).
4. Make the fast parts many times the drift speed (here about 90×), so the change of speed is the effect.

## Measured in Carvercat 0.1.6

Comp `K Speed ramp` in [cookbook lab 6](../labs/README.md#cookbook-lab-6carverproj): "SLOW MOTION" 120 px,
keys f0 / f14 / f74 / f88; the matched curves against plain quad out / quad in; `inspect probe`, pixels
moved from each frame to the next:

| From frame | 0 | 6 | 11 | 12 | 13 | 14 | 40 | 73 | 74 | 75 | 80 | 86 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Matched curves | 302.8 | 96.4 | 26.0 | 16.2 | 7.5 | 3.3 | 3.3 | 3.3 | 7.5 | 16.2 | 78.4 | 248.8 |
| quad out / quad in | 214.9 | 119.4 | 39.8 | 23.8 | 8.0 | 3.3 | 3.3 | 3.3 | 8.0 | 23.8 | 103.5 | 199.0 |

- The drift is a constant **3.3 px a frame** (3.4 on some frames); the fast ends move up to **303 px a
  frame**, about 90× faster.
- At 30 fps both curve choices step 7.5–8.0 px into the drift: the zero-speed instant of a plain ease out
  falls between frames and doesn't show. The matched curves make the approach steeper earlier (302.8 vs
  214.9 px on the first frame), which reads as a harder "brake".
- `inspect lint`: 0 errors, 0 warnings, 2 notes (`speed_jump` at the ends, where the title leaves the frame).

## Traps

- This slows **keyed motion** only. Carvercat has no time remap: a nested comp or a video clip can be offset
  (`sourceIn`) but not slowed down or sped up: [FR-043](../../ai/references/known-issues.md#fr-043).

## In Carvercat

- Curve names on this page (quad out, quad in) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Drift up - 4 s` (minimal luxury), `Zoom past`, `Replay stinger` ([sp-replay-stinger](../../ai/patterns/sp-replay-stinger.md)).
- Background: [holds and stillness](../principles/holds-and-stillness.md), [timing and spacing](../principles/timing-and-spacing.md),
  [nested comps and time](../techniques/nested-comps-and-time.md).
