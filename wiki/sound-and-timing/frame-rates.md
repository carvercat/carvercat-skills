---
id: sound-and-timing/frame-rates
title: Frame rates
section: sound-and-timing
tags: [frame rate, fps, 24 fps, 25 fps, 30 fps, 60 fps, on twos, stepped, conversion, comp.format]
styles: [all]
topics: [timing, delivery]
related: [principles/timing-and-spacing, sound-and-timing/beat-sync, sound-and-timing/reading-time, workflow/delivery, principles/straight-ahead-and-pose-to-pose]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.fujifilm-x.com/en-in/stories/understanding-frame-rates/, https://www.masterclass.com/articles/how-frame-rates-affect-film-and-video, https://wwwapi.idtech.com/blog/what-does-animating-on-ones-twos-and-threes-mean, https://wavemotioncannon.com/2016/12/31/an-introduction-to-framerate-modulation/, https://animationpodcast.com/?p=34]
---

# Frame rates

The frame rate is how many pictures a second the film shows. It changes how smooth motion looks, how
fine your timing can be, and whether the file plays correctly where it is delivered. Choose it at the start
from the delivery spec, and do not change it halfway.

## The idea

| Rate | Where it comes from | Feel | Use |
|---|---|---|---|
| 24 | cinema | slight judder on fast pans, "film" | brand films, title sequences, footage shot at 24 |
| 25 | 50 Hz broadcast regions | like 24 | broadcast in those regions, footage shot at 25 |
| 30 (29.97) | 60 Hz broadcast regions, web default | crisp | social, web, SaaS, explainers |
| 50 / 60 | high-frame-rate video, games, screens | very smooth | UI recordings, sports, fast motion graphics |

- Match the footage: graphics over 25 fps footage are made at 25.
- Higher rates make fast moves smoother but double the frames to render and store.
- "On twos" (each pose held 2 frames) halves the drawing rate on purpose for a hand-made, retro or
  anime feel; it is a style, not a delivery rate. Mixing ones and twos within a piece is an expressive tool.

## Rules of thumb

- Durations are in time first, frames second: a 0.5 s entrance is 12 f at 24, 15 f at 30, 30 f at 60.
- Very short moves lose precision at 24 fps (a 3 f flash is 125 ms at 24, 100 ms at 30).
- Pick a rate that makes music beats land on whole frames where you can (120 BPM: 12 f at 24, 15 f at 30,
  30 f at 60).

## Measured in Carvercat

Four comps, each 3 s long, at 24, 25, 30 and 60 fps, each with a one-second expo-out move starting at
0.5 s (`carvercat_inspect mode:timing`):

| Comp | Frames | Move starts | Move settles (0.5%) |
|---|---|---|---|
| 24 fps | 72 | f13 | f33 |
| 25 fps | 75 | f13 | f34 |
| 30 fps | 90 | f16 | f41 |
| 60 fps | 180 | f31 | f80 |

**Changing the rate of an existing comp keeps frame numbers, not time.** `comp.format {fps:60}` on the
30 fps comp changed only `sceneFps`: the comp stayed 90 frames long (now 1.5 s instead of 3 s) and the
keys stayed on frames 15 and 45, so everything played twice as fast. To convert a comp's rate, rescale
every clip start, length and key frame by new ÷ old (or rebuild it), then check with `inspect timing`.

Lint is time-based: its reading-time minimum is 5/6 s at any rate (20 f at 24, 25 f at 30, 50 f at 60), see
[reading time](reading-time.md).

## Do and don't

- Do read the delivery spec before building; set the rate in the first comp and copy it everywhere.
- Do keep nested comps at the master's rate.
- Don't change `comp.format` fps on a finished comp and expect the same timing.
- Don't animate on twos by accident (a 12 fps feel on smooth UI motion reads as lag).

## Checklist

- [ ] One frame rate across all comps, matching delivery and footage.
- [ ] Durations converted by time when reusing timing from a different rate.
- [ ] After any rate change, `inspect timing` shows the expected seconds.

## In Carvercat

- Set the rate: `comp.format {width, height, fps}` or the Format window; in a project file
  `scene.sceneFps`. Keys and clip positions are in frames.
- Stepped "on twos" motion: `hold` easing on keys every 2 frames; ready-made `Rise - on twos`,
  `Pop - on twos`, `Exit down - on twos` ([Retro](../../ai/patterns/retro.md)).
- Export settings: [export and delivery](../../ai/references/workflows/export-and-delivery.md).
- Lab: comps `S 24 fps`, `S 25 fps`, `S 30 fps`, `S 60 fps` in [the timing lab](../labs/README.md).
