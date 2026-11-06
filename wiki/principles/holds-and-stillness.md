---
id: principles/holds-and-stillness
title: Holds and stillness
section: principles
tags: [hold, stillness, still frame, ambient motion, push, drift, freeze, never static, breathing]
styles: [all]
topics: [timing, pacing]
related: [principles/timing-and-spacing, principles/rhythm, design/negative-space, sound-and-timing/reading-time, techniques/camera-moves-2d]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://fluent2.microsoft.design/motion, https://www.nngroup.com/articles/animation-duration/]
---

# Holds and stillness

A hold is a moment where the main elements stop: the title lands and is read, the product sits in the frame.
Holds are where communication happens. But a completely frozen frame in a video can look like a playback
fault, so most motion styles keep a small amount of life going during a hold.

## The idea

- **The moving hold**: the composition is still, but something subtle continues: a slow push or drift, a
  breathing tracking, a gently moving background, a particle or light sweep.
- **The true still**: a deliberate, short freeze for emphasis (a stop before the punchline), or a graphic style
  that wants calm. Keep it short or motivate it.
- **Read first, decorate second**: ambient motion must never compete with text being read.

## Rules of thumb

- Slow push during a hold: 2–6% scale over 3–5 s, `linear`.
- Drift: 0.5–1% of the frame over 3–5 s.
- Text breathing: tracking +0.04–0.06 over the hold.
- True stills: under about 1.5 s unless the piece is deliberately contemplative.

## Measured in Carvercat

Four 4 s comps with a card and a 96 px title: frozen, and with the card pushing 1%, 3% and 6% over the 4 s
(`linear`). `carvercat_inspect {mode:"qc"}` at its default 96 px analysis width and at 480 px:

| Comp | qc result (both widths) |
|---|---|
| Frozen | `freeze` from f0 to f119, 3.97 s |
| Push 1% | `freeze`, 3.97 s |
| Push 3% | `freeze`, 3.97 s |
| Push 6% (1.5% a second) | `freeze`, 3.97 s |

- qc's freeze check (holds of 2 s or more) does not see slow ambient motion: a 6% push over 4 s is reported as
  frozen. Treat `freeze` findings on intended moving holds as expected, and confirm the motion with
  `carvercat_inspect {mode:"timing"}` (it lists the moving object) or a look at the start and end of the hold.
- So "is this hold alive?" is a design judgment you check by eye; qc only tells you where the long holds are.

## Do and don't

- Do give every hold over about 2 s a subtle ambient motion, unless stillness is the point.
- Do keep ambient motion slower than anything the viewer must follow.
- Don't start ambient motion with an ease that draws attention; `linear` or very soft.
- Don't read qc `freeze` as an error on a moving hold.

## Checklist

- [ ] Every long hold has ambient motion or a reason to be still.
- [ ] Ambient motion does not move text being read.
- [ ] qc `freeze` findings reviewed against intended holds.

## In Carvercat

- Ready-made ambient motion: `Photo push - 5 s` ([Corporate Brand](../../ai/patterns/corporate-brand.md)),
  `Drift up - 4 s` and the tracking breathe ([Minimal Luxury](../../ai/patterns/minimal-luxury.md)),
  `Focus pull` ([kt-focus-pull](../../ai/patterns/kt-focus-pull.md)).
- The recipes note the same qc behaviour for held end cards ([recipes](../../ai/recipes/README.md)).
- Lab: comps `Q Frozen`, `Q Push 1pct`, `Q Push 3pct`, `Q Push 6pct` in [the measurement lab 4](../labs/README.md).
