---
id: cookbook/lyric-line-sync
title: Light up a lyric line in sync with the song
section: cookbook
tags: [lyrics, karaoke, sync, word timing, music video, highlight, beat, sing along]
styles: [kinetic-typography, social-short-form, retro]
topics: [text, timing, audio]
related: [genres/lyric-videos, cookbook/hit-on-the-beat, sound-and-timing/beat-sync, cookbook/headline-word-by-word]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Karaoke]
---

# Light up a lyric line in sync with the song

**Goal.** A lyric line shown whole and dim, each word lighting up exactly when it is sung, with a small
bump, even though the words are not evenly spaced in time.

## Steps

1. Get each word's onset frame from the song (by ear, from a beat grid, or from the singer's timing):
   here f10, 25, 33, 40, 55, 70 (frame = seconds × 30).
2. One text **per word**, laid out as the measured line: word *i* starts at line left + width of the
   first *i* words − width of word *i*.
3. Each word's `fill` keyed dim on f0 and bright on its onset with **`hold`**.
4. A bump on the onset: scale 1 → 1.08 over 3 f, back over 7 f.

## Measured in Carvercat 0.1.6

Comp `K Lyric` in [cookbook lab 7](../labs/README.md#cookbook-lab-7carverproj): "Hold on to the light tonight",
96 px Bold, centred; frames rendered with `carvercat_render`, brightest pixel inside each word:

| Word | Hold | on | to | the | light | tonight |
|---|---|---|---|---|---|---|
| Onset | f10 | f25 | f33 | f40 | f55 | f70 |
| Frame before | 96 | 96 | 96 | 96 | 96 | 96 |
| Onset frame | 242 | 242 | 242 | 242 | 242 | 242 |

- Every word lit **on its onset frame**, not before. Word left edges: 406.4, 622.8, 751.3, 859.9, 1023.0,
  1220.0 px; the line reads as one line.
- `inspect lint contrast:true`: 0 errors, 1 warning (`low_contrast` 2.35:1 on a word in its dim state), 1 note.
  The dim colour is meant to recede; use a brighter dim if the line must be readable before it is sung.

## Traps

- Stagger Text has one uniform gap, so it can't follow real word timing:
  [KI-041](../../ai/references/known-issues.md#ki-041); per-word timing isn't stored natively
  ([FR-021](../../ai/references/known-issues.md#fr-021)).
- Bounds drop a trailing space; measure prefixes without one: [KI-149](../../ai/references/known-issues.md#ki-149).
- Check the onsets against the exported audio, not the timeline view ([hit on the beat](hit-on-the-beat.md)).

## In Carvercat

- Library: `Beat words` ([kt-beat-words](../../ai/patterns/kt-beat-words.md)); the karaoke line pattern
  [kt-karaoke-line](../../ai/patterns/kt-karaoke-line.md); `Highlight caption (9:16)`.
- Background: [lyric videos](../genres/lyric-videos.md), [beat sync](../sound-and-timing/beat-sync.md).
