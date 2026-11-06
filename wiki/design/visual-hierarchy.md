---
id: design/visual-hierarchy
title: Visual hierarchy
section: design
tags: [hierarchy, emphasis, scale, weight, order, focal point, importance, levels]
styles: [all]
topics: [composition, attention]
related: [principles/staging, design/contrast, design/visual-flow, design/typography-pairing, design/grids-and-layout, design/negative-space]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/principles-visual-design/, https://xd.adobe.com/ideas/process/information-architecture/visual-hierarchy-principles-examples, https://artworkflowhq.com/resources/10-principles-of-visual-hierarchy-for-designers, https://carbondesignsystem.com/elements/motion/choreography/]
---

# Visual hierarchy

Hierarchy is the order in which the viewer notices things. In a still layout it comes from size, contrast,
colour, position and space. In motion there is a fifth lever, stronger than all of them: **what moves, and
when**. A good frame tells the eye "first this, then this, then that" without a word.

## The idea

- **Levels**: hero (one), support (one to three), detail (the rest). Three levels are usually enough.
- **Levers, strongest first in motion**: movement, then contrast, then size, then colour, then position,
  then space.
- **Order of appearance is hierarchy**: what arrives first is read as most important. Arrival order should
  match importance, then reading order.
- **Weight budget**: every lever you pull on a minor element steals attention from the hero.

## Rules of thumb

- Size steps of about 2× between levels (headline 84 px, subline 38 px; name 76 px, role 36 px).
- The hero gets the accent colour and the highest contrast; supporting text is muted (lower contrast,
  never below the [contrast](contrast.md) minimum).
- The hero moves first or most; support follows 3–6 f later with a quieter move
  ([stagger systems](../techniques/stagger-systems.md)).
- At most one element animating hard at a time.
- Put the hero at a thirds intersection or the optical centre (slightly above the true centre).

## Measured in Carvercat: how muted can the lower levels be?

A three-level stack on a near-black ground (#101418): hero "Hero" 96 px Bold in #ECECEE, support "Support" 40 px
Regular and label "Label" 28 px Bold in six greys. `carvercat_inspect {mode:"lint", contrast:true}`:

| Grey | Nominal ratio on #101418 | Support (40 px Regular, wants 3:1) | Label (28 px Bold, wants 4.5:1) |
|---|---|---|---|
| #4A5260 | 2.35 | warning, measured 2.18 | error, measured 2.18 |
| #5A6372 | 3.05 | warning, 2.79 | warning, 2.79 |
| #6B7480 | 3.91 | passes | warning, 3.16 |
| #7C8592 | 4.96 | passes | warning, 4.43 |
| #8C96A6 | 6.19 | passes | passes |
| #A0A8B4 | 7.71 | passes | passes |

- On this ground, supporting text can be muted down to about #6B7480; small labels need about #8C96A6 or lighter.
- Lint measures the rendered ink, so a grey must be roughly 1.2–1.4× above the nominal threshold to pass
  ([contrast](contrast.md)).
- Measured ink heights of the three levels (`carvercat_authoring geometry`): hero 68 px, support 37 px (with a
  descender), label 20 px: about a 2× step per level, as the rule of thumb asks.

## Do and don't

- Do decide the three levels for each scene before choosing fonts or colours.
- Do let the hero arrive first and leave last.
- Don't make everything bold, big or accented.
- Don't use motion on detail-level items during the hero's moment.

## Checklist

- [ ] Each scene has one hero, named in the plan.
- [ ] Size, contrast and arrival order all agree on the hero.
- [ ] Supporting text is muted but passes contrast.
- [ ] A greyscale, paused frame still shows the hierarchy.

## In Carvercat

- Sizes used in the verified packs (hero 150–300 px, headline 72–96 px, support 26–40 px, labels 28–34 px)
  and lint's minimum text size: [typography craft](../../ai/references/craft/typography.md).
- Hero vs support entrances per style (hero gets the signature move, support the plain one 4–12 f later):
  [timing by style](../../ai/references/craft/timing-by-style.md).
- Dimming and blurring the background, and lint's contrast check: [staging](../principles/staging.md),
  [contrast](contrast.md).
- Lab: comp `H Hierarchy` in [the hierarchy lab](../labs/README.md).
- Arrival order: `carvercat_inspect {mode:"timing"}` lists when each object enters; `expect` checks such as
  `"Title" before "Subtitle"` lock the order.
