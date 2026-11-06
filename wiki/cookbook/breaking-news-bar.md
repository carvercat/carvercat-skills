---
id: cookbook/breaking-news-bar
title: Make a "breaking news" bar with a ticker
section: cookbook
tags: [breaking news, news bar, ticker, crawl, lower third, headline, broadcast, scrolling text]
styles: [corporate-brand, sports, explainer]
topics: [text, timing, loops]
related: [genres/broadcast-packages, cookbook/readable-lower-third, cookbook/credits-roll, cookbook/seamless-loop, history/broadcast-graphics-80s-90s]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/News_ticker]
---

# Make a "breaking news" bar with a ticker

**Goal.** A red "BREAKING" label slides in, a white headline plate grows out of it, and a ticker crawls along
the bottom without ever showing a gap.

## Steps

1. **Label**: red rectangle 360 × 80 at the left (y 840–920) with "BREAKING" on it; apply
   `Slide from left - expo` to both.
2. **Headline plate**: white rectangle from x 360 to the right edge, `transformOrigin` `"0% 50%"`, `scale` `[0, 1]` → `[1, 1]` from f6 to
   f24 (expo out). The headline text comes in at f16 with `Rise - expo`.
3. **Ticker band**: dark rectangle 1920 × 56 under the plate.
4. **Ticker text**: measure the advance of one run of the ticker text, **trailing spaces included**: width of
   the text twice minus width of the text once (`carvercat_authoring mode:geometry`). Here 4539.7 − 2251.7 =
   **2288 px** at 40 px Regular.
5. Two copies of the text, left edges at 0 and 2288. Key both **`linear`** to 2288 px further left over the
   loop (here 300 f). On the frame after the last, copy 2 sits where copy 1 started, so the crawl loops.
   The run must be wider than the frame (2288 > 1920), or add a third copy.

## Measured in Carvercat 0.1.6

Comp `K Breaking news` in [cookbook lab 8](../labs/README.md#cookbook-lab-8carverproj); `inspect probe` on the
ticker copies and the plate:

| Frame | 0 | 1 | 150 | 299 |
|---|---|---|---|---|
| Ticker 1 left edge | 0.0 | −7.6 | −1144.0 | −2280.4 |
| Ticker 2 left edge | 2288.1 | 2280.5 | 1144.1 | 7.7 |

- Speed **7.627 px/frame** (2288 / 300), constant; the gap between the copies held at 2288.0–2288.1 px every
  frame, and f299 + 1 frame puts copy 2 at 0.0, copy 1's start.
- Plate: left edge held at **360.0** every frame; width 831.5 px on f8, 1532 on f16, full 1560 on **f24**.
- `Slide from left - expo` moved the label in 172.8 px (0.09 of the width), opaque by f8, settled f16.
- `inspect lint contrast:true`: 0 errors, 0 warnings, 4 notes (`outside_graphics_safe` for "BREAKING", inside the
  5% margin at the left edge, and `repeated_key_value`).
- `inspect qc` says the comp does **not** loop (seam 0.048): the label and plate animate in from nothing at f0.
  Put the ticker in its own comp if the whole thing must loop.

## Traps

- Measuring the single text gives 2251.7 px: the bounds stop at the last glyph and drop the trailing spaces
  ([KI-149](../../ai/references/known-issues.md#ki-149)); copies spaced by that would collide.
- `qc` judges a loop by brightness only ([KI-140](../../ai/references/known-issues.md#ki-140)); check the copy
  positions as above.
- Keep a crawl slow enough to read: 7.6 px/frame at 30 fps is 229 px a second; with this text's average
  advance of 16.7 px per character that is about 14 characters a second, near lint's 17 chars/s reading rate.

## In Carvercat

- Curve names on this page (expo out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Headline bar`, `Alert banner`, `Live` sticker, `Lower third bar`, `Slide from left - expo`,
  `Rise - expo`.
- Background: [broadcast packages](../genres/broadcast-packages.md), [readable lower third](readable-lower-third.md),
  [credits roll](credits-roll.md) (the same `linear` crawl, vertically).
