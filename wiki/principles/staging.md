---
id: principles/staging
title: Staging
section: principles
tags: [staging, focus, focal point, hierarchy, depth of field, blur, dimming, clarity]
styles: [all]
topics: [attention, composition]
related: [design/visual-hierarchy, design/visual-flow, principles/secondary-action, principles/appeal, accessibility/readability]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation, https://blog.adobe.com/en/publish/2016/11/08/redesigning-the-12-principles-of-animation-for-motion-design, https://atlassian.design/foundations/motion, https://www.nngroup.com/articles/principles-visual-design/]
---

# Staging

Staging is presenting one idea so clearly that it cannot be missed. Where is the viewer looking right
now, and is that where the story is? In motion graphics, staging is layout, contrast, timing and
"who moves" working together.

## The idea

- **One focal point per beat.** Everything else is quieter: smaller, dimmer, softer, or still.
- **Movement is the strongest attractor.** The eye goes to what moves, then to contrast, then to size.
  So only the thing that matters should move at the moment it matters.
- **Silhouette test**: if the frame were a flat shape, would the main action still read?
- **Paused-frame test**: any frame, including frame 0, should look intentional.

## Rules of thumb

- Push supporting elements back with 30–60% opacity, a small blur, or a darker value; never all three at
  full strength.
- Give the hero at least 2× the visual weight of the next thing (size, contrast or both).
- At most one or two things move together; background motion is slow and continuous.
- Reveal in order of importance, then reading order: container, headline, support, call to action.
- Leave space around the hero ([negative space](../design/negative-space.md)).

## Measured in Carvercat

A staging lab comp: four background cards at opacity 0.45 with `blur: "6.9px"` (the old Blur `Size` 6), a light hero
card with a 96 px headline, and a 32 px caption in a dark slate (#3A4552) on the near-black ground (#101418).
`carvercat_inspect {mode:"lint", contrast:true}` measured the caption at **1.57:1** and raised a
`low_contrast` error (it wants 3:1 for text that size). The blurred, dimmed cards read clearly as
background in `carvercat_look`; the caption had been pushed back too far and became unreadable. Dimming is
for shapes and images; text that must be read keeps its contrast (see [contrast](../design/contrast.md)).

## Do and don't

- Do decide the focal point of every beat before animating.
- Do use motion to hand attention from one element to the next (the next thing starts as the last settles).
- Don't animate two unrelated things at once.
- Don't push readable text below contrast minimums to "stage" it; shrink or remove it instead.

## Checklist

- [ ] One focal point per beat, named in the plan.
- [ ] The focal point moves or changes; competitors are still or slow.
- [ ] Supporting shapes are dimmed or softened; supporting text still passes `lint contrast:true`.
- [ ] A paused frame at entrance, hold and exit reads on its own (`carvercat_look`).

## In Carvercat

- Template examples with measured numbers and lint traps for this principle: [craft principle page](../../ai/references/craft/principles/staging.md).
- Dimming: `opacity` 0.3–0.6 on supporting objects.
- Softening: `blur` `"4.6px"` to `"9.2px"` (the old Blur `Size` 4–8; a blur added with `effect.add` starts at the old size 10, 11.5 px, which is very soft;
  [blur](../../ai/references/effects/blur.md)).
- Focus pull between elements: key `blur` on both (`anim.set` with `blur`, by name), one going to `"0px"` as the other goes to 4.6–9.2 px; the
  `Focus pull` template does this for text ([kt-focus-pull](../../ai/patterns/kt-focus-pull.md)).
- Check: `carvercat_inspect {mode:"lint", contrast:true}` for text contrast; `carvercat_look` with
  `overlay:["safe"]` for placement; `carvercat_inspect {mode:"timing"}` to confirm only one thing moves per beat.
- Composition rules and safe areas: [composition and layout](../../ai/references/craft/composition-and-layout.md).
- Lab: comp `W Staging` in [the principles lab](../labs/README.md).
