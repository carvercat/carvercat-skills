---
id: techniques/trails-and-echoes
title: Trails and echoes
section: techniques
tags: [trail, echo, ghost, smear, speed lines, delay, copies, onion]
styles: [funky, sports, retro, cartoon-bounce, kinetic-typography]
topics: [speed, stylisation]
related: [techniques/motion-blur, principles/follow-through-and-overlap, techniques/stagger-systems, principles/exaggeration]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.lollypop.design/blog/2019/march/the-forgotten-art-of-spacing/, https://lesterbanks.com/?p=35455]
---

# Trails and echoes

An echo trail is a row of fading copies that follow a moving object a few frames behind, like a long camera
exposure or the ghost images in cartoons and sports graphics. Unlike motion blur it is a deliberate style:
the copies stay distinct and draw the path of the move.

## The idea

- Copies of the object play the same move, each delayed a fixed number of frames and fainter than the one in
  front.
- Delay sets the spacing of the ghosts (more delay, wider gaps); opacity steps set how long the trail looks.
- Echoes show path and speed at once: dense where the object was slow, spread where it was fast.
- Typography echoes (a word repeated behind itself) are a classic kinetic-type move.

## Rules of thumb

- 3–5 copies; delay 1–3 f each; opacity falling roughly by half per copy (1.0, 0.7, 0.45, 0.25, 0.12).
- Use on the hero move only, and let the trail catch up (all copies land on the target).
- Echo copies sit **behind** the leader in the track order.
- Prefer motion blur for realism, echoes for style ([motion blur](motion-blur.md)).

## Measured in Carvercat

A leader dot and four copies on the same move (1300 px over 20 f, smooth `cubic-bezier(0.65, 0, 0.35, 1)`), each
copy delayed 2 f more and fainter (opacities 1.0, 0.7, 0.45, 0.25, 0.12). `carvercat_inspect mode:timing`:

| Object | Starts moving | Settles |
|---|---|---|
| Leader | f6 | f25 |
| Echo 1 | f8 | f27 |
| Echo 2 | f10 | f29 |
| Echo 3 | f12 | f31 |
| Echo 4 | f14 | f33 |

The trail is 8 f long and fully collapses onto the leader 8 f after it lands. In `carvercat_look` at f15 the
ghosts still near the start were bunched together and the gaps widened towards the leader, which was in
the fast middle of its move: the trail draws the easing.

## Do and don't

- Do build the leader first, then duplicate and offset keys by a fixed step.
- Do let the trail finish; a trail frozen mid-way looks like a mistake.
- Don't echo text that must be read until it has landed.
- Don't use more than one trail at a time.

## Checklist

- [ ] Fixed delay step and falling opacity.
- [ ] Copies behind the leader; trail collapses after the landing.
- [ ] `inspect timing` shows the even cascade of settle frames.

## In Carvercat

- Curve names on this page (smooth) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Copies: new clips with the same keys (in the project file, give each a new id), set
  `opacity`, and shift the copies' keys (`key.box` over MCP, or `+ i × step` frames in
  the file). Put the leader on the top track.
- For text echoes, use separate text clips, one per ghost.
- Lab: comp `M Trails` in [the measurement lab 2](../labs/README.md).
