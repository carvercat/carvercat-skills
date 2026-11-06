---
id: cookbook/countdown
title: Make a 3-2-1 countdown
section: cookbook
tags: [countdown, 3 2 1, timer, numbers, beat, ring, go]
styles: [social-short-form, sports, kinetic-typography, futuristic-hud]
topics: [text, timing, rhythm]
related: [sound-and-timing/reading-time, sound-and-timing/beat-sync, cookbook/hit-on-the-beat, cookbook/count-a-number-up]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.silvermansound.com/bpm-to-fps-calculator, https://www.ssw.com.au/rules/post-production-do-you-give-enough-time-to-read-texts-in-your-videos]
---

# Make a 3-2-1 countdown

**Goal.** "3, 2, 1, GO" on a steady beat, each number punching in, with a ring that runs round once per
number.

## Steps

1. One text clip per number, **back to back**, each one beat long. Use **25 f or more** per number at
   30 fps (72 BPM). Faster counts need sound to carry them, and lint flags them (see below).
2. Each number cuts in large and settles: scale 1.35 → 1.0 over 6 f, expo out.
3. A ring per number: an ellipse with stroke only, `trimEnd` `"0%"` → `"100%"` `linear` over the whole beat (`anim.set` with `trimEnd` keys it by name; checked: 40% at f10 of a 25 f beat), so it
   reads as a clock hand.
4. Put a tick or hit on each beat frame ([hit on the beat](hit-on-the-beat.md)).

## Measured in Carvercat 0.1.6

Comps `K Countdown 25f` and `K Countdown 15f` in [cookbook lab 3](../labs/README.md#cookbook-lab-3carverproj),
300 px ExtraBold numbers, 520 px rings:

| Beat | `inspect lint` | `inspect qc` |
|---|---|---|
| 25 f (100 f in all) | **0 errors, 0 warnings, 0 notes** | no findings |
| 15 f (60 f in all) | 4 warnings `reading_time`: "readable for 15 frames; 1 characters want 25" | no findings |

- Lint asks for at least **25 f (5/6 s)** for any text, even a single digit.
- Number scale settles 4 f into each beat (`inspect curves`, expo over 6 f).

## Traps

- `text.content` can't be keyed, so a countdown is separate clips (or the odometer in
  [count a number up](count-a-number-up.md)): [KI-051](../../ai/references/known-issues.md#ki-051).
- An ellipse's stroke starts at 3 o'clock and runs counter-clockwise: `rotate` the ring `"-90deg"` and key
  `trimStart` for a clockwise sweep from 12 ([donut fill](donut-fill.md)).

## In Carvercat

- Curve names on this page (expo out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Countdown (9:16)` ([ss-countdown](../../ai/patterns/ss-countdown.md)).
- Background: [reading time](../sound-and-timing/reading-time.md), [beat sync](../sound-and-timing/beat-sync.md).
