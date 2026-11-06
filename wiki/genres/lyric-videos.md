---
id: genres/lyric-videos
title: Lyric videos
section: genres
tags: [lyric video, music, kinetic type, words on beat, song, karaoke, typography]
styles: [kinetic-typography, retro, glitch, funky, social-short-form]
topics: [genre, music, typography]
related: [techniques/kinetic-type, sound-and-timing/beat-sync, techniques/rhythm-editing, sound-and-timing/reading-time, accessibility/photosensitivity]
verified: no (theory only)
source_inspiration: [https://www.renderforest.com/blog/how-to-make-lyric-video-with-ai, https://doaj.org/article/f9aca1391cec4c9fb298cc98fcc2ec0c, https://shivuknet.co.il/en/animation/animated-lyric-video/]
---

# Lyric videos

A lyric video sets a song's words in motion: the text appears with the singing, the type and motion carry
the song's mood, and the background supports without competing. It is kinetic typography at song length,
so its craft is rhythm, legibility and variety over three or four minutes.

## The idea

- **The vocal is the timing source**, the beat is the grid: words appear on (or just before) the sung
  syllable; scene changes and big moves fall on bars and phrase starts.
- **Lines, not words, by default**: most of the song shows a line or half-line at a time; save word-by-word
  slams for hooks and choruses.
- **Sections get looks**: verse calm, pre-chorus building, chorus loudest and most stylised, bridge different.
  Repeated choruses can reuse their look with variation.
- **Type carries the mood**: weight, case, tracking and motion style express the song (soft fades for a
  ballad, hard cuts and slams for rap or punk).

## Rules of thumb

- Text appears 0–4 f before the syllable; leaves when the line ends or on the next line's start.
- Each line holds long enough to read (often the singing is slower than reading, but fast verses are not).
- 2–3 type treatments per video at most, mapped to song sections.
- Change composition every 1–2 bars in verses, every bar or beat in choruses.
- Backgrounds slow and low-contrast; text is the hero.

## Do and don't

- Do mark every line's start frame from the audio before designing.
- Do build one treatment per section as a reusable comp or template.
- Don't strobe colours on the beat for long stretches ([photosensitivity](../accessibility/photosensitivity.md)).
- Don't let fast rap lines vanish before they can be read; group them into half-lines.

## Checklist

- [ ] Every line timed to the vocal (0–4 f early).
- [ ] Section looks planned; chorus treatment consistent.
- [ ] Reading time checked on fast sections.
- [ ] `qc` clean for flashes over the whole song.

## In Carvercat

No new measurements on this page.

- Word timing from audio: `ai/scripts/motion/vo_align.py` works on sung vocals with clear diction; check
  against the waveform.
- Beat-locked words: `Beat words`, word-level slams and pops (`Words slam`, `Letters pop`, `Word swap`)
  in [Kinetic Typography](../../ai/patterns/kinetic-typography.md); recipe [kinetic quote reel](../../ai/recipes/kinetic-quote-reel.md).
- Lines with a sung-word fill: `Karaoke line` ([kt-karaoke-line](../../ai/patterns/kt-karaoke-line.md)): two dim lines, each word fills on its sung frame; the frames come from a list in the lab script.
- Long songs: split into section comps nested in a master; continuous motion across them:
  [JSON authoring](../../ai/references/app/json-authoring.md#continuous-motion-across-sub-comps).
- Frames per beat: [beat sync](../sound-and-timing/beat-sync.md).
