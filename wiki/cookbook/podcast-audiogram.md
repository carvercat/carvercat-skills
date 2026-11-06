---
id: cookbook/podcast-audiogram
title: Make a podcast audiogram with a lit waveform
section: cookbook
tags: [podcast, audiogram, waveform, progress bar, cover art, episode, audio visual, social clip]
styles: [social-short-form, corporate-brand, funky]
topics: [audio, rhythm, progress]
related: [cookbook/sound-wave-bars, cookbook/progress-bar, cookbook/lyric-line-sync, sound-and-timing/audio-in-carvercat, genres/social-ads]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Podcast]
---

# Make a podcast audiogram with a lit waveform

**Goal.** Cover art, episode title and a waveform whose bars light up left to right as the clip plays, with a
progress line under it. The waveform is drawn by hand: Carvercat has no audio-reactive control
([FR-047](../../ai/references/known-issues.md#fr-047)).

## Steps

1. **Cover** 360 px rounded square at (480, 540) with "Ep. 12"; **title** (64 px) and show name (38 px) at x 760.
2. **Waveform**: 36 rounded bars, 16 px wide, pitch 28 px, from x 760, centred on y 680. Heights are static, set
   by hand or by a formula: here 50 + 150 × |sin(0.9 *i*) × cos(0.37 *i*)| px, between 50 and 200 px. For a real
   episode, make a list of heights from the audio's loudness by eye or with an outside tool.
3. **Playhead**: each bar gets a `hold` colour key from grey to amber on frame **round(*i* × length / 36)**; with a
   216 f clip a bar lights every 6 f.
4. **Progress**: a grey track 996 px wide (to the right edge of the last bar) and an amber fill on top, `transformOrigin`
   `"0% 50%"`, `scale` `[0, 1]` → `[1, 1]` `linear` over the whole clip.
5. Put the audio on its own track; the clip length is the episode excerpt ([audio in
   Carvercat](../sound-and-timing/audio-in-carvercat.md)). The lab comp has no audio file.

## Measured in Carvercat 0.1.6

Comp `K Audiogram` (216 f) in [cookbook lab 9](../labs/README.md#cookbook-lab-9carverproj); pixel at the centre of
a bar in rendered frames, `inspect probe` on the fill:

| Bar | lights on | frame before | on that frame |
|---|---|---|---|
| 1 | f6 | grey (58, 63, 71) | amber (242, 176, 60) |
| 5 | f30 | grey | amber |
| 17 | f102 | grey | amber |
| 35 | f210 | grey | amber |

| Frame | 0 | 1 | 54 | 108 | 162 | 215 |
|---|---|---|---|---|---|---|
| Progress width (px) | 0.0 | 4.6 | 249.0 | 498.0 | 747.0 | 991.4 |

- Fill left edge **760.0 on every frame**; 4.61 px/frame, 996 px reached on f216.
- `inspect lint`: **0 errors, 0 warnings, 0 notes**.

## Traps

- The bars do not follow the sound; with real speech the viewer sees it. Hand-shape the heights to the loud and
  quiet words, or use the beat-keyed bars of [sound-wave bars](sound-wave-bars.md).
- A bar count that does not divide the clip length gives uneven spacing in frames; round the frame, as above.
- Audiograms are watched muted often: add captions ([timed captions](timed-captions-by-hand.md)).

## In Carvercat

- Library: `Podcast episode`, `Signal bars`, `Progress`, `Caption box`.
- Background: [sound-wave bars](sound-wave-bars.md), [progress bar](progress-bar.md),
  [audio in Carvercat](../sound-and-timing/audio-in-carvercat.md).
