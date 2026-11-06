---
id: techniques/match-cuts
title: Match cuts and graphic matches
section: techniques
tags: [match cut, graphic match, continuity, shape match, transition, cut, morph cut]
styles: [all]
topics: [transitions, continuity]
related: [techniques/morphing, techniques/masking, techniques/rhythm-editing, genres/title-sequences, genres/explainers]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.studiobinder.com/blog/match-cuts-creative-transitions-examples/, https://filmdaft.com/match-cut-definition/, https://carbondesignsystem.com/elements/motion/choreography/]
---

# Match cuts and graphic matches

A match cut joins two scenes through something they share: a shape, a colour, a position, a movement.
The eye stays on the same spot while the world changes around it. In motion graphics this is often
better than any wipe: a dot becomes the sun, a phone screen becomes the full frame, a logo's circle becomes
the next scene's planet.

## The idea

- **Graphic match**: same shape, size and position on both sides of the cut.
- **Match on action**: a movement that starts in scene A finishes in scene B (a swipe, a throw, a spin).
- **Colour match**: scene A ends on a full-frame colour that is scene B's background.
- The cut should happen at the moment of greatest similarity, usually when motion is fastest or the shape
  fills the frame.

## Rules of thumb

- Match position within a few pixels and size within about 5%; the eye forgives the rest.
- Keep the motion direction and speed continuous across the cut; ease the combined move as one curve.
- Hide the cut inside motion: cut at the peak of a scale-up or a whip, not on a still frame.
- One match cut per sequence is elegant; several in a row become a gimmick.

## Measured in Carvercat

Scene A (dark): a 120 px dot moves from (600, 700) to the centre and scales 1 → 3 over f0–f30
(S-curve). Scene B (light) starts at f30 with a 360 px "sun" at the centre that then rises. Checks:

- `carvercat_inspect {mode:"expect"}`: `"Scene A dot" at 960,540 within 2 at 29` and
  `"Scene B sun" at 960,540 within 2 at 30` both passed.
- Probe: the dot was 359 px wide at its centre at f29; the sun 360 px at f30. Size match 99.7%, position
  within 1 px.

In `carvercat_look` the dot appears to stay put while the background swaps from dark to light: the cut
reads as one object continuing. Writing the two `expect` sentences first, then building until they pass,
is the fastest way to land a graphic match.

## Do and don't

- Do plan both sides together; the last frame of A and the first of B are designed as a pair.
- Do let the shared object keep moving into scene B so the cut is carried by motion.
- Don't match cut between scenes that don't share meaning; the transition implies a connection.
- Don't add a cross-dissolve on top of a match; it blurs the trick.

## Checklist

- [ ] Shared element's position and size match across the cut (`expect` passes).
- [ ] Motion direction continues across the cut.
- [ ] The cut is on a moving frame.
- [ ] `carvercat_look` across the cut (3 frames either side) reads as one object.

## In Carvercat

- Curve names on this page (S-curve) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Build both sides in one comp on separate clips, or as two nested comps butted on one track; positions
  are comp pixels in `expect` and probe (y down).
- Scenes as nested comps: the cut is where one instance ends and the next starts; an instance shows nothing after
  its inner comp ends, so butt them exactly ([nested comps and time](nested-comps-and-time.md)).
- `expect` sentences: `"A" at X,Y within 2 at F` for the last frame of A and the first of B.
- Shared-element continuity across a whole promo: [promo assembly](../../ai/patterns/promo-assembly.md);
  transition choices and hand-offs: [transitions](../../ai/references/craft/transitions.md).
- Colour-field matches: `Dip to colour` and `Colour iris` ([Transitions](../../ai/patterns/transitions.md),
  [tr-iris](../../ai/patterns/tr-iris.md)).
- Lab: comp `T Match cut` in [the techniques lab](../labs/README.md).
