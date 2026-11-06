---
id: cookbook/split-screen
title: Make a split-screen
section: cookbook
tags: [split screen, before after, comparison, two up, halves, divider, mask]
styles: [corporate-brand, social-short-form, data-viz, explainer, sports]
topics: [layout, masking, nested comps]
related: [techniques/masking, techniques/nested-comps-and-time, design/grids-and-layout, cookbook/camera-push-on-a-still]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://blog.frame.io/2018/02/12/animated-masks-after-effects/, https://www.techsmith.com/blog/edit-videos-lower-thirds/]
---

# Make a split-screen

**Goal.** Two scenes side by side (before and after, two speakers, two products), each sliding into its
half, with a divider that draws between them.

## Steps

1. Build each side as its **own comp** at full frame size (1920 × 1080) and keep its subject in the
   middle. Place both comps as **nested instances**, centred at x = 480 and x = 1440.
2. Make a **window** for each half: a rectangle 957 px wide (leave a 6 px gutter for the divider), then
   on each instance `property.set {key: "mask", value: "<window>"}`, and `parent.clear` on the windows, so the window
   stays put while the scene slides.
3. Slide the scenes in from their outer edges with position keys (expo out, 20 f), the right side 4 f
   after the left.
4. Draw the **divider**: a 2-point path down the centre, 6 px stroke, `trimEnd` `"0%"` → `"100%"` as the scenes land.

## Measured in Carvercat 0.1.6

Comp `K Split screen` in [cookbook lab 2](../labs/README.md#cookbook-lab-2carverproj), `carvercat_inspect`
`curves`, `probe` and `composite`:

| Part | Keys | Result |
|---|---|---|
| Left scene | centre x −480 → 480, f0 → f20, expo | settles **f13**; centre at 480 from f20 |
| Right scene | centre x 2400 → 1440, f4 → f24, expo | settles **f17** |
| Divider | `trimEnd` `"0%"` → `"100%"`, f20 → f36, expo | first ink f21, 98% drawn f29 |

- `carvercat_look`: each half shows only its own scene at every sampled frame (f0–f40); the labels sit
  centred in their halves.
- `inspect lint`: 0 errors, **3 warnings** (`cropped_at_rest` on both instances: 75% and 25% on screen)
  and 1 note. The warnings come from the parts the masks hide; the picture is right.

## Traps

- Lint ignores masks: [KI-133](../../ai/references/known-issues.md#ki-133).
- Put the window in `value` and the scene in `id`; reversed, the scene becomes the matte (old `mask.make` took the first id as the mask).
- Nested instances ignore a parent's transform, so move the instance itself, not a null:
  [KI-119](../../ai/references/known-issues.md#ki-119).
- Lint does not see content cut inside a moving nested instance: [KI-144](../../ai/references/known-issues.md#ki-144).

## In Carvercat

- `trimEnd` keys by design name: `anim.set {id, keyframes: [{at, trimEnd: "0%", ease}, {at, trimEnd: "100%"}]}`, `ease` on the key that leaves (checked: `wiki/tools/verify_keyed_pages.py`, case draw-a-line-along-a-path). A static `trimEnd` is one call. The older stored key `trim.end` (0 to 1) still works.
- Curve names on this page (expo out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Split screen` ([cb-split-screen](../../ai/patterns/cb-split-screen.md)), `Before and after`
  (Carvercat Essentials), `Before after split (9:16)` ([ss-before-after](../../ai/patterns/ss-before-after.md)),
  `Comparison bars` ([dv-before-after](../../ai/patterns/dv-before-after.md)).
- Background: [masking](../techniques/masking.md), [nested comps](../techniques/nested-comps-and-time.md),
  [grids and layout](../design/grids-and-layout.md).
