---
id: cookbook/readable-lower-third
title: Make a lower third readable over busy video
section: cookbook
tags: [lower third, name tag, contrast, plate, legibility, busy background, shadow, lint]
styles: [corporate-brand, saas-ui, sports, explainer, kinetic-typography]
topics: [text, contrast, accessibility]
related: [design/contrast, accessibility/readability, genres/broadcast-packages]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.techsmith.com/blog/edit-videos-lower-thirds/, https://captions.ai/help/guides/engagement/captions-readable-background, https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html]
---

# Make a lower third readable over busy video

**Goal.** A name and role that stay readable whatever the footage behind them does.

## Steps

1. Put a **plate** behind the text: a rectangle in a dark colour at **95%** opacity (`opacity`
   0.95), `borderRadius` small, padding about 40 px around the text.
2. Name in Bold at 64 px or more; role at 40 px or more, near-white (not mid-grey) on the plate.
3. An accent bar on the plate's edge carries the brand colour; the text does not have to.
4. Run `carvercat_inspect mode:lint contrast:true` and `carvercat_look` on several frames of the shot,
   especially the brightest and busiest moments.

## Measured in Carvercat 0.1.6

Comp `K Lower third busy` in [cookbook lab 1](../labs/README.md#cookbook-lab-1carverproj): 70 bright
shapes as "busy video", four versions of the same lower third (name 64 px Bold, role 40 px Medium), lint
with `contrast: true`:

| Version | Role line result |
|---|---|
| A. White text, nothing behind | **error** `low_contrast` 1.29:1 (wanted 3) |
| B. White text with a shadow (`dropShadow` `"0 2.2px 8.3px #000000cc"`; the 0.1.6 note: offset 0.002, softness 0.01, opacity 0.8) | **error** 1.01:1 |
| C. Plate #1B2028 at 85%, role #C9C6BF | **warning** 2.92:1 |
| D. Plate #1B2028 at 95%, role #E6E3DC | no finding |

- A shadow alone did not help: over a light patch it adds almost no measured contrast.
- The names passed in all four versions because they sat on darker shapes at the sampled frame; lint
  judged the frame in the middle of the comp (f60 of 120). Moving footage needs a plate, not luck.
- At 85% the busy shapes still show through the plate; 95% hid them.

## Traps

- Lint skips Regular text under 34 px for contrast: [KI-142](../../ai/references/known-issues.md#ki-142).
- Lint's minimum text size does not scale with 4K comps: [KI-143](../../ai/references/known-issues.md#ki-143).
- Lint ignores masks, so a masked wipe-on plate is judged without its mask:
  [KI-133](../../ai/references/known-issues.md#ki-133).
- The Motion Patterns "Lower third - accent bar" has a small gap at rest:
  [KI-139](../../ai/references/known-issues.md#ki-139).

## In Carvercat

- Library: `Lower third bar`, `Lower third rule`, `Lower third - two boxes`
  ([cb-lower-third](../../ai/patterns/cb-lower-third.md)), `SaaS lower third`
  ([su-lower-third](../../ai/patterns/su-lower-third.md)), `Kinetic lower third`
  ([kt-lower-third](../../ai/patterns/kt-lower-third.md)).
- Background: [contrast](../design/contrast.md), [readability](../accessibility/readability.md).
