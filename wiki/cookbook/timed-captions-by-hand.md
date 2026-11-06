---
id: cookbook/timed-captions-by-hand
title: Time captions from a script (what an SRT would give)
section: cookbook
tags: [captions, subtitles, SRT, timecodes, cues, speech, accessibility, lower captions]
styles: [social-short-form, corporate-brand, explainer]
topics: [text, timing, accessibility]
related: [cookbook/vertical-captions, cookbook/lyric-line-sync, sound-and-timing/reading-time, sound-and-timing/frame-rates, sound-and-timing/voice-over-pacing]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/SubRip]
---

# Time captions from a script (what an SRT would give)

**Goal.** Captions that appear and disappear on the exact frames of a subtitle list. Carvercat cannot import an
SRT file ([FR-049](../../ai/references/known-issues.md#fr-049)); each cue becomes a text clip with a start and a length.

## Steps

1. Take each cue as start and end in seconds (an SRT line "00:00:03,000 --> 00:00:05,400" is 3.0 and 5.4).
2. **Frame = round(seconds × fps)**: start frame *s*, end frame *e* (exclusive). At 30 fps 0.5 s is 15 and 2.9 s is 87.
   The clip starts on *s* and lasts *e* − *s* frames.
3. One text per cue, 52 px, centred at (960, 900), white; no fades (subtitles cut on and off). A hard cut is
   what viewers expect; a 4 f fade is a style choice.
4. Check against lint: 17 characters a second, and a cue never shorter than 25 f (5/6 s).
5. Keep the cues in time order on separate tracks or one track back to back; gaps between cues are what you
   want, not overlaps.

## Measured in Carvercat 0.1.6

Comp `K Captions` (450 f, 30 fps) in [cookbook lab 9](../labs/README.md#cookbook-lab-9carverproj); six cues, first and last
frame each is on screen found with `inspect probe`:

| Cue | SRT start → end (s) | Expected frames | On screen | Frames |
|---|---|---|---|---|
| 1 | 0.5 → 2.9 | 15 – 86 | 15 – 86 | 72 |
| 2 | 3.0 → 5.4 | 90 – 161 | 90 – 161 | 72 |
| 3 | 5.6 → 8.2 | 168 – 245 | 168 – 245 | 78 |
| 4 | 8.4 → 10.0 | 252 – 299 | 252 – 299 | 48 |
| 5 | 10.2 → 10.7 | 306 – 320 | 306 – 320 | 15 |
| 6 | 11.0 → 14.0 | 330 – 419 | 330 – 419 | 90 |

- Every cue is on screen exactly from round(start × 30) to round(end × 30) − 1.
- `inspect lint contrast:true`: 0 errors, **1 warning**: cue 5 ("Done.", 15 f) `reading_time`, "5 characters want
  25 f". The other five cues are clean.

## Traps

- At 25 fps a start of 0.5 s is frame 12.5; choose one rounding rule (round half up, or half to even as Python's
  `round` does) and use it for every cue ([frame rates](../sound-and-timing/frame-rates.md)).
- The end of a cue is exclusive: a clip of `e − s` frames shows its last cue frame on `e − 1`.
- Hundreds of cues are not practical by hand: write them from the list with a script or in the project file.
- Captions for 9:16 have their own placement: [vertical captions](vertical-captions.md).

## In Carvercat

- Library: `Caption box`, `Subtitle`, `Caption pages (9:16)`, `Highlight caption (9:16)`, `Caption words pop`.
- Commands: `clip.move`, `clip.trim` for start and length; `text.edit` for the words.
- Background: [vertical captions](vertical-captions.md), [reading time](../sound-and-timing/reading-time.md),
  [voice-over pacing](../sound-and-timing/voice-over-pacing.md).
