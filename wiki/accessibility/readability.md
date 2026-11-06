---
id: accessibility/readability
title: Readability of on-screen text
section: accessibility
tags: [readability, legibility, text size, contrast, safe area, line length, reading time, lint]
styles: [all]
topics: [accessibility, text]
related: [design/contrast, sound-and-timing/reading-time, accessibility/captions, design/typography-pairing, design/grids-and-layout]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html, https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-USA-Timed-Text-Style-Guide, https://www.ssw.com.au/rules/post-production-do-you-give-enough-time-to-read-texts-in-your-videos]
---

# Readability of on-screen text

Text in motion has to be read in a moment, on any screen, often with the sound off. Readability is the sum
of five things: size, contrast, position, length and time. Carvercat's lint checks four of them
automatically; this page collects the numbers.

## The idea

- **Size**: on a phone, a 1920-wide frame is shown about 6 cm tall; text that looked fine on a monitor
  disappears.
- **Contrast**: see [contrast](../design/contrast.md).
- **Position**: inside the safe area, away from platform UI, never under faces or busy detail.
- **Length**: few words, short lines, one idea per card.
- **Time**: long enough to read twice, still while being read ([reading time](../sound-and-timing/reading-time.md)).

## Rules of thumb (1920 × 1080)

| Check | Minimum | Better |
|---|---|---|
| Body and labels | 28 px font size | 32–40 px |
| Captions for social | 40 px on 1080-wide vertical | 48–56 px |
| Contrast | 4.5:1 normal, 3:1 large | 7:1 over footage |
| Line length | 42 characters | 30–35 |
| Lines per card | 2 | 1 |
| Read time | 17 characters a second, 5/6 s minimum | 12–15 characters a second |

- Use mixed case for anything longer than a few words; all caps slows reading.
- Medium and Bold weights survive compression better than Light.

## Measured in Carvercat: what lint checks

| Lint check | Rule as measured | Notes |
|---|---|---|
| `text_too_small` | measured line height under **18 px** (default `min_text_px`) | lint's line height for Rethink Sans is 0.725 × the font size, whatever the word or weight: 18 px → 13.0, 24 px → 17.4 (flagged), 26 px → 18.9 (passes) |
| `low_contrast` (opt-in `contrast:true`) | 4.5:1, or 3:1 from **34 px** font size | measures rendered ink, so it is stricter than nominal colour ratios; Regular text under 34 px is not checked ([KI-142](../../ai/references/known-issues.md#ki-142)) |
| `outside_graphics_safe` | ink outside `[96, 54, 1824, 1026]` (5%) | an info note |
| `reading_time` | 17 characters a second (no spaces), at least 5/6 s, fully opaque frames only | `reading_cps` changes the speed |

So the floor for Rethink Sans is a 25–26 px font size to pass `text_too_small`; other faces have other
ratios ([typography pairing](../design/typography-pairing.md)). Use 28 px or more and you are safe
([typography craft](../../ai/references/craft/typography.md)).

## Do and don't

- Do run lint with `contrast:true` and a `reading_cps` that matches the audience.
- Do preview at phone size (`carvercat_look {max_edge:400}`) before delivery.
- Don't put text over faces, logos or high-detail footage without a plate.
- Don't animate text while it is being read.

## Checklist

- [ ] `inspect lint {contrast:true}`: no `text_too_small`, `low_contrast`, `reading_time` or
      `outside_graphics_safe` findings for text.
- [ ] Small Regular text checked by hand for contrast ([KI-142](../../ai/references/known-issues.md#ki-142)).
- [ ] Looked at phone size.
- [ ] Two lines and 42 characters at most per card.

## In Carvercat

- Lint: `carvercat_inspect {mode:"lint", contrast:true, reading_cps:17, min_text_px:18}`.
- Text size: `fontSize` in px (a true em; old `text.font.size`: 1.0 = 1146.24 px em on a 1920-wide comp for Rethink Sans); `text.fit` picks the largest size that fits a box; measure real ink with
  `carvercat_authoring {mode:"geometry", id}`.
- Plates and outlines: a rectangle behind the text, or `text.outline` ([text paint](../../ai/references/effects/text-paint.md)).
- Captions: [captions](captions.md).
- Lab: comps `C Contrast`, `C Sizes` and `C Safe` in [the accessibility lab](../labs/README.md).
