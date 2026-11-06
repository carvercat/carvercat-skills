---
id: styles/saas-ui
title: SaaS and product UI
section: styles
tags: [saas and product ui, style, hub, saas-ui]
styles: [saas-ui]
topics: [style, navigation]
related: [principles/slow-in-slow-out, principles/follow-through-and-overlap, principles/staging, principles/exaggeration, techniques/camera-moves-2d, techniques/masking, techniques/stagger-systems, genres/ui-ux-demos, genres/product-launches, genres/explainers, history/flat-design-and-ui-motion, history/swiss-international-style]
verified: no (theory only)
source_inspiration: [https://carbondesignsystem.com/elements/motion/overview/, https://screen.studio/guide/animations-motion]
---

# SaaS and product UI

A hub page: what the saas and product ui style is, which wiki pages matter most for it, and where its verified Carvercat pack and recipes are.

## The feel

Clean, confident, helpful. Interface pieces behave like real software; the film around them is a little slower and warmer.

## Principles that carry it

- [Slow in and slow out (easing)](../principles/slow-in-slow-out.md): expo-like arrivals, accelerating exits.
- [Follow-through and overlapping action](../principles/follow-through-and-overlap.md): cards land, content follows 2–5 f later.
- [Staging](../principles/staging.md): one UI action per beat, everything else dimmed.
- [Exaggeration and overshoot](../principles/exaggeration.md): overshoot 3–5% at most.

## Techniques it relies on

- [Camera-like moves in 2D](../techniques/camera-moves-2d.md): zoom to the active field, hold, pull back.
- [Masking and reveals](../techniques/masking.md): rolling counters and reveals inside cards.
- [Stagger systems](../techniques/stagger-systems.md): list rows and cards 3 f apart.

## Where it is used

- [UI and UX demo videos](../genres/ui-ux-demos.md)
- [Product launch films](../genres/product-launches.md)
- [Explainer videos](../genres/explainers.md)

## Roots

- [Flat design and UI motion](../history/flat-design-and-ui-motion.md)
- [Swiss International Typographic Style](../history/swiss-international-style.md)

## Watch out

- Interface timings (150–400 ms) for UI parts; do not let them bounce like cartoons.
- Mock UI text must still pass readability at delivery size.
- Masked counters trip lint (masks are invisible to it); judge with `mode:composite`.

## In Carvercat

This hub gives no new measurements; the pack and recipes are verified in their own docs.

- Pack: [saas-ui](../../ai/patterns/saas-ui.md); its row in [style families](../../ai/references/craft/style-families.md) (easing family, entrance and exit lengths, palette, signature pieces).
- Measured frame counts: [timing by style](../../ai/references/craft/timing-by-style.md); review list: [review by style](../../ai/references/craft/review-by-style.md).
- Recipe: [saas-feature-launch-30s](../../ai/recipes/saas-feature-launch-30s.md).
- From brief to build: [reading a brief](../../ai/references/craft/reading-a-brief.md).
