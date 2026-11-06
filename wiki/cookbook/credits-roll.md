---
id: cookbook/credits-roll
title: Roll end credits up the screen
section: cookbook
tags: [credits, end credits, roll, scroll, crawl, closing titles, fade edges, gradient]
styles: [corporate-brand, minimal-luxury, kinetic-typography]
topics: [text, timing]
related: [cookbook/end-cleanly, sound-and-timing/reading-time, techniques/gradients-in-motion, genres/title-sequences]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Closing_credits]
---

# Roll end credits up the screen

**Goal.** A block of credits scrolls up at a steady speed, entering below the frame and leaving above it,
with soft fades at the top and bottom edges.

## Steps

1. All credits in **one text** (one line per row, empty lines between groups), centred, 44 px Medium.
   Measure its height with `carvercat_authoring geometry`.
2. Key `y` **`linear`**: 1080 on f0 (the block's top edge just below the frame), and −height (the block just above) on
   the comp's last frame + 1. Linear keeps the speed constant, which is what makes a roll readable.
3. Speed = (1080 + height) / frames. Check that each line stays on screen long enough to read
   (1080 / speed frames).
4. Two 160 px bands in the background colour on top: a gradient fill, alpha 1 → 0 down from the top edge,
   and 0 → 1 down to the bottom edge. As a CSS gradient: `fill: "linear-gradient(180deg, #101418 0%, #10141800 100%)"` (180deg runs top to bottom;
   y is down). The bottom band is the same with `0deg`.

## Measured in Carvercat 0.1.6

Comp `K Credits` in [cookbook lab 5](../labs/README.md#cookbook-lab-5carverproj): 15 rows, 360 f;
`inspect probe` and `carvercat_render`:

- Measured block height **857.4 px**. Centre y 1528.5 at f0, 539.8 at f180, −443.4 at f359 (`y` = centre − 428.7): **5.49 px per
  frame** on every frame (5.5 between f0 and f1). Each line is on screen about 197 f (6.6 s).
- Rendered at f200 down the centre column, text pixels under the top band: grey 60 at y 10, 161 at y 70,
  183 at y 90; unfaded text is 242. The bands fade the letters, not the background.
- `inspect lint`: **0 errors, 0 warnings, 0 notes**.

## Traps

- The old `json_author/cc.py` `gradient()` converted its endpoints as comp coordinates with y up, so a top band
  written with it faded the wrong way (text at y 4 stayed full white):
  [KI-155](../../ai/references/known-issues.md#ki-155). The CSS gradient angle has no such flip.
- An eased roll (ease in/out) changes speed and is harder to read; keep it linear and fade it in instead.
- Lint does not judge scroll speed; check the time on screen yourself
  ([reading time](../sound-and-timing/reading-time.md)).

## In Carvercat

- Library: `Kinetic quote`, `Slow quote`; the opening-credits pattern
  [kt-opening-credits](../../ai/patterns/kt-opening-credits.md) and the long scroll
  [kt-manifesto-scroll](../../ai/patterns/kt-manifesto-scroll.md).
- Background: [end cleanly](end-cleanly.md), [gradients in motion](../techniques/gradients-in-motion.md).
