---
id: history/flat-design-and-ui-motion
title: Flat design and UI motion
section: history
tags: [flat design, material design, ui motion, design systems, easing tokens, skeuomorphism, 2010s, saas]
styles: [saas-ui, explainer, corporate-brand, data-viz]
topics: [history, ui, easing]
related: [history/swiss-international-style, genres/ui-ux-demos, principles/slow-in-slow-out, principles/timing-and-spacing, accessibility/motion-sensitivity]
verified: no (theory only)
source_inspiration: [https://en.wikipedia.org/wiki/Flat_design, https://m1.material.io/motion/duration-easing.html, https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md, https://carbondesignsystem.com/elements/motion/overview/, https://fluent2.microsoft.design/motion, https://blog.adobe.com/en/publish/2016/11/08/redesigning-the-12-principles-of-animation-for-motion-design]
---

# Flat design and UI motion

In the early 2010s interface design dropped imitation textures (leather, glass, paper) for flat colour,
simple icons and clean type, rooted in Swiss and Bauhaus ideas. Without visual depth cues, **motion** took
over the job of explaining interfaces: where a panel came from, what is on top, what changed. Design
systems then wrote that motion down as rules and tokens, and SaaS marketing video adopted the same look.

## What defined it

- Flat colour fields, sans-serif type, simple line or solid icons, generous space.
- A backlash against weak affordances led to "flat plus": subtle shadows, layers and depth returned within
  a few years, with motion to show hierarchy.
- **Motion as meaning**: elements enter from where they belong, scale from what was tapped, and leave
  towards where they go. Continuity replaces decoration.
- **Tokens**: design systems published fixed duration ladders (roughly 50–1000 ms) and named easing
  curves (standard, decelerate for entering, accelerate for leaving, emphasised variants), so every team
  moves the same way.
- **Productive vs expressive**: short subtle motion for everyday tasks, larger expressive motion for rare
  moments.

## Why it matters for motion

- It produced the clearest public guidance on durations and easing; the curves used throughout this wiki
  (standard, emphasised decelerate and accelerate, expo-like arrivals) come from that world.
- SaaS promo and UI demo styles are its direct descendants.
- It brought reduced-motion settings and motion accessibility into mainstream practice.

## Using the influence well

- Interface parts move with interface timing (about 150–400 ms); the "film" around them can be slower.
- Enter decelerating, leave accelerating, move on screen with a standard curve.
- Let motion explain spatial relationships: things grow from their trigger and return to it.
- Add subtle depth (one shadow style) where layers overlap.

## In Carvercat

- Curve names on this page (decelerate, accelerate) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
No measurements on this page; the curves are measured in [slow in and slow out](../principles/slow-in-slow-out.md).

- Design-system curves as `cubic-bezier(...)` (old `customEase`): standard `0.2, 0, 0, 1`, emphasised decelerate `0.05, 0.7, 0.1, 1`,
  emphasised accelerate `0.3, 0, 0.8, 0.15` ([custom curves](../../ai/patterns/custom-curves.md)).
- The [SaaS UI pack](../../ai/patterns/saas-ui.md) and [UI demo genre](../genres/ui-ux-demos.md).
