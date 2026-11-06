---
id: cookbook/logo-mask-reveal
title: Reveal a wordmark from behind its logo mark
section: cookbook
tags: [logo reveal, wordmark, mask, slide out, logo animation, brand, intro, window]
styles: [corporate-brand, minimal-luxury, saas-ui]
topics: [masking, logos, reveal]
related: [cookbook/logo-sting, cookbook/reveal-image-through-text, techniques/masking, genres/logo-animation, cookbook/pop-in]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Logo]
---

# Reveal a wordmark from behind its logo mark

**Goal.** A round mark pops in, then the company name slides out of it to the right, appearing only where it
has left the mark, as if it were coming out of a slot.

## Steps

1. Measure the wordmark once (`carvercat_authoring mode:geometry`): a 140 px Bold "Northwind" placed at x 800
   has its ink from x 800.0 to 1432.7, **632.7 px** wide, so the ink starts at the text position plus the
   measured offset ([breaking news bar](breaking-news-bar.md) does the same for a crawl).
2. Layout: mark disc 170 px at x 700, letter "N" on it; the name's ink at rest from **x 820**, 40 px past the
   mark's right edge (785).
3. **Window**: a rectangle x 790 → 1790, y 420 → 660, the visible part. On the wordmark `property.set {key: "mask", value: "<window>"}`,
   then `parent.clear {ids: ["<window>"]}` so they stay separate clips.
4. Wordmark start position: its ink ends at x 780, left of the window, so it is invisible. Key position
   from that point at **f12** (`linear`) to the rest point at **f40** (expo out, decelerating).
5. Mark and letter: `preset.apply` `Pop - spring` on each, from f0. Put the mark above the wordmark so its
   disc hides the start of the slide.

## Measured in Carvercat 0.1.6

Comp `K Logo reveal` in [cookbook lab 8](../labs/README.md#cookbook-lab-8carverproj). Dark ink (the wordmark,
not the teal mark) found in rendered frames, leftmost and rightmost x:

| Frame | 12 | 14 | 16 | 18 | 20 | 24 | 28 | 34 | 40 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ink x range | none | 791–1035 | 791–1201 | 791–1301 | 791–1360 | 791–1419 | 810–1441 | 819–1450 | 820–1451 | 820–1451 |

- The left edge sits at **791** (the window edge, 790) until f24: the name is cut by the window, never drawn
  over the mark. It leaves the cut between f24 and f28 and settles at 820 by f40.
- Position settles on **f30** (`inspect curves`, expo); peak speed 0.073 of the width a frame on f13.
- Mark: `Pop - spring` overshoots **16.2%** (scale 1.162 at f8), settled f20; opaque from f5.
- `inspect lint contrast:true`: 0 errors, 2 warnings, 3 notes. The warnings: `text_overlap` (the wordmark's
  unmasked box lies under the "N") and `text_too_small` for the "N" (6.5 px tall, measured at the start of the pop, [KI-162](../../ai/references/known-issues.md#ki-162)). Both are artefacts of the build, not of the picture.

## Traps

- Lint ignores masks ([KI-160](../../ai/references/known-issues.md#ki-160)); judge the reveal with
  `carvercat_look` or `inspect composite`.
- Text bounds carry an offset from the text position ([KI-149](../../ai/references/known-issues.md#ki-149)):
  place by measured ink, not by the position you typed.
- The window must start beyond the mark: if its left edge is inside the mark's disc, the name shows through the
  mark's edge.
- One preset per clip ([KI-113](../../ai/references/known-issues.md#ki-113)); the mark and its letter each need
  `Pop - spring`.

## In Carvercat

- Curve names on this page (expo out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Commands: `property.set` (`mask`), `parent.clear`, `preset.apply`, `carvercat_authoring mode:geometry`.
- Library: `Pop - spring`; see [logo sting](logo-sting.md) for a fuller version.
- Background: [logo sting](logo-sting.md), [masking](../techniques/masking.md),
  [logo animation](../genres/logo-animation.md).
