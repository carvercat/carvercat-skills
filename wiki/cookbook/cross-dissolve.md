---
id: cookbook/cross-dissolve
title: Cross-dissolve between two scenes
section: cookbook
tags: [dissolve, cross fade, mix, transition, opacity, dip]
styles: [minimal-luxury, corporate-brand, explainer, all]
topics: [transitions, colour]
related: [design/colour-transitions, techniques/blend-modes, cookbook/wipe-transition, cookbook/end-cleanly]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.premiumbeat.com/blog/cut-to-the-beat-tip-for-editing-to-music-in-final-cut-pro-x/, https://blog.frame.io/2018/02/12/animated-masks-after-effects/]
---

# Cross-dissolve between two scenes

**Goal.** Scene A melts into scene B without the picture dipping darker half way.

## Steps

1. Overlap the clips by the dissolve length (15 f here): B starts 15 f before A ends, on a track **above** A.
2. Fade **only B in** (opacity 0 → 1, `linear`). Leave A at full opacity underneath; it ends when B is
   fully in.
3. Don't fade A out at the same time: two half-transparent layers over the background let it show through,
   and the frame dips.
4. Use 10–20 f for a soft scene change, longer (30 f+) for time passing.

## Measured in Carvercat 0.1.6

Comps `K Dissolve over` and `K Dissolve both` in [cookbook lab 3](../labs/README.md#cookbook-lab-3carverproj):
red #E5483B (scene A) to blue #4C7BD9 (scene B) over f30–f45 with nothing else in the comp; centre pixel from
`carvercat_render`:

| Frame | B fades in over A | A fades out, B fades in |
|---|---|---|
| f30 | (229, 72, 59) | (229, 72, 59) |
| f34 | (200, 88, 123) | (155, 74, 108) |
| f37 | (176, 99, 155) | **(116, 80, 132)** |
| f41 | (136, 112, 189) | (80, 96, 167) |
| f45 | (76, 123, 217) | (76, 123, 217) |

- `inspect qc` luma range: 0.41–0.48 for "B over A", **0.36**–0.47 for "both fade": the dip is measurable.
- Mixing is done in linear light, so even the clean version's mid frame is not the sRGB average of the two
  colours ([blend modes](../techniques/blend-modes.md)).

## Traps

- A clip that ends exactly where the next begins with no overlap is a cut, not a dissolve;
  `clip.move` overwrites what it lands on: [KI-032](../../ai/references/known-issues.md#ki-032).
- Nested-comp instances show nothing after their inner comp ends: keep the inner comp at least as long as
  the overlap ([nested comps](../techniques/nested-comps-and-time.md)).

## In Carvercat

- `opacity` on the incoming clip (or instance).
- Library: `Slow dip` for a dip through a colour ([ml-slow-dip](../../ai/patterns/ml-slow-dip.md)),
  `Dip to colour` ([tx-cover-transitions](../../ai/patterns/tx-cover-transitions.md)).
- Background: [colour transitions](../design/colour-transitions.md), [transitions craft](../../ai/references/craft/transitions.md).
