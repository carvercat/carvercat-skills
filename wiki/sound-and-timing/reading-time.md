---
id: sound-and-timing/reading-time
title: Reading time
section: sound-and-timing
tags: [reading time, hold, characters per second, words per minute, subtitles, captions, lint]
styles: [all]
topics: [text, timing, accessibility]
related: [techniques/kinetic-type, accessibility/readability, accessibility/captions, sound-and-timing/frame-rates, principles/timing-and-spacing]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-USA-Timed-Text-Style-Guide, https://partnerhelp.netflixstudios.com/hc/en-us/articles/360051554394-Timed-Text-Style-Guide-Subtitle-Timing-Guidelines, https://clevercast.com/bbc-subtitling-guidelines, https://www.overseeros.com/blog/how-long-should-on-screen-text-stay-youtube, https://www.ssw.com.au/rules/post-production-do-you-give-enough-time-to-read-texts-in-your-videos]
---

# Reading time

Text on screen is only useful if it stays long enough to read. The hold must be planned in frames before
animating, because it sets the length of the scene, not the other way round.

## The idea

- People read on-screen text at roughly 3 words or 15–20 characters a second, slower for numbers,
  technical words, second languages and children.
- Reading starts when the text is **still and fully visible**, not when it starts animating in.
- Text that must be read while something else moves needs more time; the eye is shared.
- Subtitle practice gives good limits: about 17 characters a second for a general audience, 42 characters a
  line, at most two lines, at least 5/6 s and at most about 7 s per caption.

## Rules of thumb

- Hold after landing ≥ max(25 f, 10 f per word) + 10 f at 30 fps (4 words → 50 f, 8 words → 90 f).
- Short punch (1–2 words): 1–1.5 s. Statement of 6–8 words: 2.5–4 s.
- Numbers and data: budget about 12–17 characters a second.
- Kids, accessibility-first or non-native audiences: 12 characters a second.
- If the text cannot fit its read time in the edit, cut words, not time.

## Measured in Carvercat

Carvercat's lint (`carvercat_inspect mode:lint`, check `reading_time`) counts characters without spaces and
only the frames where the text is fully opaque. Default speed 17 characters a second; minimum 5/6 s. A
34-character line ("Every report writes itself every Monday") held 3 frames short of 2 s at each rate:

| Comp rate | Readable frames | Lint wants at 17 cps | At `reading_cps: 12` |
|---|---|---|---|
| 24 fps | 45 | 48 | 68 |
| 25 fps | 47 | 50 | 71 |
| 30 fps | 57 | 60 | 85 |
| 60 fps | 117 | 120 | 170 |

So `wanted frames = max(5/6 s, characters ÷ cps) × fps`, rounded up. The same line held exactly 2 s passed
at every rate. Pass `reading_cps` to lint to check a slower audience; `min_text_px` (default 18) checks size.
More measured values (6, 11, 38 and 68 characters): [timing by style](../../ai/references/craft/timing-by-style.md).

## Do and don't

- Do count the hold from the frame the text is fully opaque; a fade-in eats into it.
- Do write captions before animating; their read times set the scene lengths.
- Don't put essential text on screen for under 25 f at 30 fps.
- Don't animate text while it is being read (no drifting letters, no tracking breathe faster than the eye).

## Checklist

- [ ] `inspect lint` shows no `reading_time` findings (at 12 cps for accessibility-first work).
- [ ] At most 2 lines and about 42 characters a line per card.
- [ ] No card holds over about 7 s; split long text.

## In Carvercat

- Lint: `carvercat_inspect {mode:"lint", reading_cps:17, min_text_px:18}`; findings name the object, the
  readable frames and the frames wanted.
- Measure text width before placing it: `carvercat_authoring {mode:"geometry", id}`.
- Captions to voice-over: `ai/scripts/motion/vo_align.py` gives word frames;
  [captions and voice-over](../../ai/references/workflows/captions-and-voiceover.md).
- Caption templates: `Caption pages (9:16)` ([ss-caption-pages](../../ai/patterns/ss-caption-pages.md)),
  `Highlight caption (9:16)` ([ss-highlight-caption](../../ai/patterns/ss-highlight-caption.md)).
- Lab: the `Read 34 chars` text in comps `S 24 fps` … `S 60 fps` of [the timing lab](../labs/README.md).
