---
id: cookbook/vertical-captions
title: A 9:16 caption style
section: cookbook
tags: [captions, 9:16, vertical, social, reels, shorts, tiktok, word by word, safe zone]
styles: [social-short-form, kinetic-typography]
topics: [text, captions, safe areas]
related: [genres/social-ads, accessibility/captions, sound-and-timing/reading-time, cookbook/highlight-a-word, cookbook/readable-lower-third]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.houseofmarketers.com/guide-to-safe-zones-tiktok-facebook-instagram-stories, https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-USA-Timed-Text-Style-Guide]
---

# A 9:16 caption style

**Goal.** Social captions that pop in word by word with the speech, sit low in the frame, and stay clear
of the platform's buttons and text.

## Steps

1. Comp **1080 × 1920**, 30 fps.
2. One text object per caption page (2–4 words), ExtraBold, 72 px, white, centred. Keep the line short:
   about 540 px wide at most.
3. Place the centre at **x 490**, not 540: the right edge holds the like/comment/share column. Put the
   line at about **y 1240** (65% down), above the caption and handle area at the bottom.
4. Apply the Library preset **`Caption words pop`** to each page (`preset.apply {name, id}`): words 3 f
   apart, each popping from 70%.
5. Cut pages back to back on the speech; give each page at least its reading time.
6. For bright footage add an outline or a plate ([text outlines](../techniques/text-outlines.md),
   [readable lower third](readable-lower-third.md)).

## Measured in Carvercat 0.1.6

Comp `V Captions 9x16` in [cookbook lab 2](../labs/README.md#cookbook-lab-2carverproj): page 1 "Captions
sit low" f0–f45, page 2 "but clear of the UI" f45–f90.

- What the preset wrote: per word, opacity 0 → 1 over 2 f; scale 0.7 → 1.0 with a **4.4%** overshoot,
  settled 8 f after the word starts.
- `carvercat_inspect composite`, frame by frame: page 1 words appeared at **f1, f4, f7** (whole line
  still from f10); page 2 words at **f46, f49, f52, f55, f58** (still from f61).
- Measured bounds: page 1 x 247–733 px (centre 490), y 1212–1281; page 2 x 220–760, y 1214–1266. Both end
  well left of x 900.
- `inspect lint contrast:true`: 0 errors, 0 warnings, 2 notes (`repeated_key_value`).

## Traps

- Lint has no platform safe zones for 9:16, so text under the buttons raises nothing: check with
  `carvercat_look` ([FR-040](../../ai/references/known-issues.md#fr-040)).
- Lint's minimum text size does not scale with the comp: [KI-143](../../ai/references/known-issues.md#ki-143).
- Lint does not report content cut inside a zoomed nested instance (common in 16:9 → 9:16 re-cuts):
  [KI-144](../../ai/references/known-issues.md#ki-144).
- Stagger has one uniform gap, so word onsets cannot follow the speech exactly; split pages instead:
  [KI-041](../../ai/references/known-issues.md#ki-041).

## In Carvercat

- Library (Social Short-form 9:16): `Caption words pop`, `Caption pages (9:16)`
  ([ss-caption-pages](../../ai/patterns/ss-caption-pages.md)), `Highlight caption (9:16)`
  ([ss-highlight-caption](../../ai/patterns/ss-highlight-caption.md)).
- Voice-over to word frames: [captions and voice-over](../../ai/references/workflows/captions-and-voiceover.md).
- Safe areas: [vertical and safe areas](../../ai/references/craft/vertical-and-safe-areas.md),
  [vertical re-cuts](../../ai/recipes/vertical-recuts.md).
- Background: [social ads](../genres/social-ads.md), [captions](../accessibility/captions.md),
  [reading time](../sound-and-timing/reading-time.md).
