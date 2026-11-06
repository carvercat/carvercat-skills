---
id: accessibility/captions
title: Captions and subtitles
section: accessibility
tags: [captions, subtitles, sdh, sound off, voice-over, timing, line length, burn-in, social]
styles: [social-short-form, explainer, kinetic-typography, corporate-brand]
topics: [accessibility, text, voice-over]
related: [sound-and-timing/reading-time, accessibility/readability, techniques/kinetic-type, genres/social-ads, workflow/delivery]
verified: no (theory only)
source_inspiration: [https://www.w3.org/WAI/WCAG21/Understanding/captions-prerecorded.html, https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-USA-Timed-Text-Style-Guide, https://partnerhelp.netflixstudios.com/hc/en-us/articles/360051554394-Timed-Text-Style-Guide-Subtitle-Timing-Guidelines, https://clevercast.com/bbc-subtitling-guidelines, https://help.happyscribe.com/en/articles/9395512-shot-changes-in-subtitling]
---

# Captions and subtitles

Most social video is watched without sound, and many viewers are deaf or hard of hearing. Captions make
speech and meaningful sound readable. In motion graphics they are also a design element: styled, animated
word by word, and part of the layout from the start.

## The idea

- **Captions** transcribe speech and important sounds ([music], [door slams]); **subtitles** translate.
  Accessible captions include speaker changes and sound cues, not just words.
- **Burned-in** captions are part of the picture (social, ads); **sidecar** captions (SRT, VTT) are separate
  files the player shows (broadcast, streaming, web). Many deliveries need both.
- **Sync**: a caption appears when speech starts and leaves shortly after it ends; it snaps to shot changes
  when close to them.
- **Styled captions** (word highlights, pops) must still meet reading-time and contrast rules.

## Rules of thumb

| Rule | Value |
|---|---|
| Characters per line | 42 maximum (32–37 for vertical social) |
| Lines per caption | 2 maximum, prefer 1 |
| Reading speed | about 17 characters a second (adults), 13–15 for children or dense content |
| Duration | at least 5/6 s, at most about 7 s |
| Gap between captions | at least 2 frames, or close the gap if under about half a second |
| Shot changes | end 2 frames before a cut, or stay at least half a second past it |
| Position | lower third, inside the safe area; move up when lower graphics appear |

- Break lines at natural phrase boundaries ("the red car / stopped", not "the red / car stopped").
- One speaker per caption where possible; mark speaker changes.
- Word-by-word highlight styles: highlight the spoken word, keep the full line visible for reading.

## Do and don't

- Do write captions from the final voice-over script and align them to the audio.
- Do reserve the caption zone in the layout so graphics never collide with it.
- Don't animate each word in from nothing for long passages; the line becomes unreadable.
- Don't rely only on burned-in captions where the platform supports a caption file.

## Checklist

- [ ] Every line of speech and every meaningful sound is captioned.
- [ ] Line length, line count, durations and gaps within the table above.
- [ ] Captions avoid graphics and faces; contrast passes.
- [ ] A sidecar file is delivered where the platform supports it.

## In Carvercat

No new Carvercat measurements on this page; the measured lint rules are in [reading time](../sound-and-timing/reading-time.md)
and [readability](readability.md).

- Word frames from voice-over: `ai/scripts/motion/vo_align.py`; caption workflow, retiming and multi-section
  jobs: [captions and voice-over](../../ai/references/workflows/captions-and-voiceover.md).
- Caption templates: `Caption pages (9:16)`, `Caption words pop`, `Highlight caption (9:16)`
  ([Social Short-form](../../ai/patterns/social-short-form.md)).
- Multi-line text grows upward with `verticalAlign` bottom ([typography craft](../../ai/references/craft/typography.md)).
- Arabic and right-to-left captions: [RTL and Arabic](../../ai/references/workflows/rtl-and-arabic.md).
