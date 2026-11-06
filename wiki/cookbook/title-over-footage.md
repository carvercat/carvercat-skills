---
id: cookbook/title-over-footage
title: Put a title over bright footage
section: cookbook
tags: [title, footage, scrim, darken, overlay, legibility, contrast, bright background, video]
styles: [corporate-brand, minimal-luxury, social-short-form, kinetic-typography]
topics: [text, colour]
related: [cookbook/readable-lower-third, design/contrast, accessibility/readability, cookbook/focus-in]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/animation-usability/]
---

# Put a title over bright footage

**Goal.** White title text over a bright, busy shot (sky, clouds, snow) that stays readable, by darkening
the footage under it.

## Steps

1. The footage as a full-frame nested instance (or media clip).
2. Above it, a full-frame black rectangle, the **scrim**. Key its opacity 0 → 0.55 with **ease out** over
   14 f, just before the title arrives, so the shot dims as if the light changed.
3. The title on top (120 px Bold, white), rising 30 px, expo, 16 f, starting as the scrim settles.
4. Check the result with `inspect lint {contrast:true}` and on a rendered frame.

## Measured in Carvercat 0.1.6

Comps `K Footage`, `K Title bare` and `K Title scrim` in [cookbook lab 6](../labs/README.md#cookbook-lab-6carverproj):
a sky with clouds and a sun; scrim f6–f20; frames rendered with `carvercat_render`, background sampled
every 4–6 px in the title's box (x 420–1500, y 470–610):

| | Mean background luminance | White text vs mean | Lint `low_contrast` |
|---|---|---|---|
| No scrim (f40) | 0.734 | 1.19:1 | **error**, 1.58:1 at f37 |
| Scrim 0.55 (f40) | 0.280 | 2.84:1 | none |

- The scrim settled at f19. The brightest background pixel under the title fell from luminance 1.0 (white
  cloud) to 0.558.
- Lint judges the text against the area under its ink and passed the scrim version; a plain mean over the
  whole box is stricter (2.84:1). For small or thin type, darken further or add a local plate
  ([readable lower third](readable-lower-third.md)), and check again.
- `inspect lint contrast:true`: bare, 1 error; with scrim, 0 errors, 0 warnings, 1 note.

## Traps

- Lint checks text in nested instances only when you lint the comp that holds them:
  [FR-042](../../ai/references/known-issues.md#fr-042).
- `cc.py` `lin()` darkens mid-tones in hand-written colours, which changes contrast:
  [KI-141](../../ai/references/known-issues.md#ki-141).
- Lint skips small Regular text: [KI-142](../../ai/references/known-issues.md#ki-142).

## In Carvercat

- Library: `Title centred`, `Feature title`, `Slow dip` ([ml-slow-dip](../../ai/patterns/ml-slow-dip.md)),
  `Dip to colour`.
- Background: [contrast](../design/contrast.md), [readability](../accessibility/readability.md).
