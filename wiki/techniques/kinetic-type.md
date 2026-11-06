---
id: techniques/kinetic-type
title: Kinetic typography
section: techniques
tags: [kinetic type, text animation, words, letters, slam, typewriter, tracking, emphasis, lyric]
styles: [kinetic-typography, social-short-form, sports, minimal-luxury, corporate-brand]
topics: [text, rhythm]
related: [techniques/stagger-systems, techniques/masking, sound-and-timing/reading-time, sound-and-timing/beat-sync, genres/lyric-videos, design/typography-pairing]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://wearefevr.com/the-history-of-kinetic-typography, https://vimeo.com/305153408, https://uhra.herts.ac.uk/handle/2299/15885, https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-USA-Timed-Text-Style-Guide]
---

# Kinetic typography

Words that move with meaning: a word slams in on the beat, a sentence rises line by line, a number punches,
a letter spacing breathes. Kinetic type makes text the image. It must still be read, so its first rule is
legibility; its second is that the motion expresses the word.

## The idea

- **Motion mirrors meaning**: "fast" whips in, "calm" fades slowly, "break" splits, "grow" scales up.
- **The vocabulary**: fragmentation (letters fly apart), repetition (a word echoes), rhythm (words on beats),
  variation (size and weight change across a line), distortion (stretch, skew), transparency and
  layering, masking (words from behind edges).
- **One idea per card**: 3–7 words, at most two lines, one emphasised word.
- **Move, then hold**: text animates in, stops completely while read, then leaves.

## Rules of thumb

- Read time after the text lands: at least max(25 f, 10 f per word) + 10 f; Carvercat's lint asks for
  17 characters a second ([reading time](../sound-and-timing/reading-time.md)).
- Entrances 10–20 f; exits 8–12 f, simpler than the entrance.
- Letters stagger 1–2 f (short words only); words 2–4 f; lines 4–8 f ([stagger systems](stagger-systems.md)).
- Beat-driven words: land each word on a beat; at 120 BPM that is every 15 f.
- Emphasis on one word: colour to the accent, a 105–115% scale pop over 6–10 f, or a highlight band.
- Text entrances that scale should start at 94% or larger, or lint flags the text as too small while it grows.

## Measured in Carvercat

- Word stagger orders (forward, reverse, centre, edges, random), gap 4 f, 14 f rise: see
  [stagger systems](stagger-systems.md); five words take 30 f from first movement to last landing.
- Masked rise of a 72 px line into a still window over a rule: visible from 2 f after it starts moving,
  complete 8 f later ([masking](masking.md)).
- Tracking, leading and size measured on 0.1.6 (ink widths per tracking value, lint's 18 px minimum line
  height): [typography craft](../../ai/references/craft/typography.md).

## Do and don't

- Do let the hardest-working word get the strongest move; the rest support.
- Do keep line breaks on meaning (never split "New / York").
- Don't animate text the viewer is in the middle of reading.
- Don't use per-letter animation on sentences, or more than two typefaces in a piece.

## Checklist

- [ ] Every card holds still long enough to read (`inspect lint` `reading_time` clean).
- [ ] Text never goes below 18 px line height, even during a scale entrance (`text_too_small` clean).
- [ ] One emphasised word per card.
- [ ] Motion style matches the word's meaning.

## In Carvercat

- Text object parameters: `text.font` `Font`, `Style`, `Size` (1.0 = 1146.24 px em), `Tracking`, `Word spacing`,
  `Line spacing` (all keyframeable); `text.relative` `Level` (character/word/line) with relative `Position`,
  `Rotation`, `Scale`, `Anchor`, `Opacity` for per-part animation; `text.fill` and `text.outline` for paint.
- Per-part timing: the Stagger Text effect ([stagger](../../ai/references/effects/stagger.md)); outlines and
  paint: [text paint](../../ai/references/effects/text-paint.md).
- The Kinetic Typography pack (verified 0.1.6): `Words slam`, `Letters zoom in`, `Letters pop`,
  `Words drop - bounce`, `Lines slide in - left`, `Words exit down` and templates `Word swap`,
  `Impact stack`, `Line reveal`, `Beat words`, `Focus pull`, `Split title`, `Highlight sweep`,
  `Kinetic quote`, `Stat punch`, `Numbered list`, `Follow end card`; round 3 adds `Karaoke line`,
  `Manifesto scroll`, `Echo stack` (repetition), `Opening credits`, `Strike and replace`,
  `Zoom through letter` and `Poster lockup` (variation in size, justified on measured ink)
  ([kinetic-typography](../../ai/patterns/kinetic-typography.md)).
- Captions synced to voice-over: [captions and voice-over](../../ai/references/workflows/captions-and-voiceover.md).
- Fonts: install Rethink Sans for the packs; text cannot use the app-bundled fonts
  ([KI-136](../../ai/references/known-issues.md#ki-136)).
