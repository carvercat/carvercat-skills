---
id: cookbook/sound-wave-bars
title: Make sound-wave bars jump to the music
section: cookbook
tags: [sound wave, audio bars, equalizer, visualizer, waveform, music, beat, podcast, audiogram]
styles: [social-short-form, funky, futuristic-hud, explainer]
topics: [audio, rhythm, music]
related: [cookbook/hit-on-the-beat, sound-and-timing/beat-sync, sound-and-timing/audio-in-carvercat, principles/rhythm]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Tempo]
---

# Make sound-wave bars jump to the music

**Goal.** A row of rounded bars that jump on every beat of the track and fall back between beats, keyed by
hand from the tempo (Carvercat has no audio-reactive control).

## Steps

1. **Beat frames**: frames per beat = fps × 60 / BPM. At 30 fps and 120 BPM that is **15**; beats on f0, 15,
   30 … Offset by the frame of the first downbeat if the music does not start on f0
   ([hit on the beat](hit-on-the-beat.md)).
2. Nine rounded rectangles 26 × 320 px, `borderRadius` 13, 44 px apart, centred (`transformOrigin` `"50% 50%"`, so they grow up and
   down from the middle).
3. Per bar, key **`scale` `[1, v]`**: on each beat frame the beat's peak (0.4–1.0, a different value per bar and per
   beat) with easing **`hold`**, so the bar is full height on the beat frame itself; then down to the rest
   value 0.12 twelve frames later, decelerate. Scale X stays 1.
4. Alternate two peak patterns (strong and weak beats) so the bars do not repeat every beat.

## Measured in Carvercat 0.1.6

Comp `K Sound bars` in [cookbook lab 8](../labs/README.md#cookbook-lab-8carverproj); `inspect probe` heights
(px; bar 1 peaks 0.55 / 0.40, bar 5 peaks 0.70 / 0.50):

| Frame | 0 | 1 | 4 | 8 | 12 | 14 | 15 | 16 | 20 | 29 | 30 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Bar 1 | 176.0 | 96.7 | 54.0 | 40.9 | 38.4 | 38.4 | 128.0 | 76.4 | 45.2 | 38.4 | 176.0 |
| Bar 5 | 224.0 | 117.1 | 59.4 | 41.8 | 38.4 | 38.4 | 160.0 | 90.0 | 47.6 | 38.4 | 224.0 |

- Every peak lands **on** its beat frame (320 × peak exactly) and the bar is at rest (38.4 px = 0.12) from
  12 f after the beat until the next one.
- Centre y held **540.0** on every frame: the bars grow both ways.
- `inspect lint`: 0 errors, 0 warnings, 0 notes.

## Traps

- The old `easing` named the curve **arriving** at a key; the `ease` of a key shapes the segment that **leaves** it. So `hold` on the key *before* the beat key makes the jump happen on the beat (the 0.1.6 build put `hold` on the beat key itself); an
  eased rise would reach the peak late.
- 120 BPM at 25 fps is 12.5 frames a beat; beats then fall between frames, so round each beat to the nearest
  frame rather than adding 12 or 13 every time ([frame rates](../sound-and-timing/frame-rates.md)).
- Very tall, fast-flashing bars over the whole frame can approach flash limits; this size is far below them
  ([photosensitivity](../accessibility/photosensitivity.md)).

## In Carvercat

- Curve names on this page (decelerate) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Signal bars` (audio scene), `Podcast episode`; sound effects `Soft Click`, `Clean Pop` for a test
  track.
- Background: [beat sync](../sound-and-timing/beat-sync.md), [audio in Carvercat](../sound-and-timing/audio-in-carvercat.md),
  [rhythm](../principles/rhythm.md).
