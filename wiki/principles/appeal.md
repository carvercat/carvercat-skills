---
id: principles/appeal
title: Appeal
section: principles
tags: [appeal, charisma, polish, clarity, silhouette, personality, craft]
styles: [all]
topics: [quality, personality]
related: [principles/staging, principles/exaggeration, principles/solid-drawing-2d, design/visual-hierarchy, workflow/review]
verified: no (theory only)
source_inspiration: [https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation, https://dribbble.com/stories/2020/07/27/disney-principles-of-animation-ui-interactions, https://fluent2.microsoft.design/motion, https://blog.adobe.com/en/publish/2019/06/19/designing-animation-six-principles-using-animation-ux]
---

# Appeal

Appeal is the quality that makes people want to keep watching. It is not cuteness: a villain, a stock
chart or a bank logo can all have appeal. In motion graphics it comes from clarity, confident timing, a
consistent personality and the absence of small mistakes.

## The idea

- **Clarity**: every pose and every frame is readable; nothing is ambiguous or cluttered.
- **Personality**: the motion has a point of view (crisp, bouncy, calm, aggressive) and keeps it.
- **Polish**: no jitter, no pops, no misaligned edges, no one-frame flashes, no text appearing a frame
  early. Viewers cannot name these errors but they feel them.
- **Purpose**: every move has a reason. Unmotivated spins and zooms subtract appeal.

## Rules of thumb

- Choose one personality per film and write it in three words ("calm, precise, warm"). Check each move
  against them.
- Clean silhouettes at every key pose: nothing tangent, nothing just touching an edge.
- The accent colour appears once per frame.
- Reduce before adding: remove the weakest animated element in each scene and see if it got better.
- Ease everything that starts or stops; overshoot only what has personality.

## Do and don't

- Do watch the film at full speed, muted, with fresh eyes, before calling it done.
- Do borrow appeal from good proportions and spacing (see [design](../design/README.md)), not from effects.
- Don't stack effects (glow + blur + shadow + gradient) to make something "pop".
- Don't animate everything; stillness gives the moving parts their charm.

## Checklist

- [ ] The film's personality fits in three words, and every scene matches it.
- [ ] No jitter, no one-frame flashes, no tangents (`lint` and `qc` are clean).
- [ ] Every move has a reason you can say out loud.
- [ ] One accent colour moment per frame.

## In Carvercat

- Template examples with measured numbers and lint traps for this principle: [craft principle page](../../ai/references/craft/principles/appeal.md).
- Appeal is judged, not measured, but the tools catch what spoils it:
  - `carvercat_inspect {mode:"lint"}` finds jitter, speed jumps, text too small or too brief, overlaps and
    keys outside clips.
  - `carvercat_inspect {mode:"qc"}` finds black frames, flashes and freezes.
  - `carvercat_look {sample:"keys"}` shows every keyframe, entry, settle and exit, where silhouettes and
    tangents are easiest to judge.
- Style packs with a consistent personality to start from: [style families](../../ai/references/craft/style-families.md)
  and the per-style review lists in [review by style](../../ai/references/craft/review-by-style.md).
- The final pass: [review checklist](../../ai/references/craft/review-checklist.md).
