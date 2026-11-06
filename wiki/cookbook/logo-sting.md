---
id: cookbook/logo-sting
title: Make a logo sting
section: cookbook
tags: [logo, sting, ident, reveal, brand, end card, mark, wordmark]
styles: [corporate-brand, minimal-luxury, saas-ui, sports]
topics: [reveal, timing, easing]
related: [genres/logo-animation, techniques/line-drawing, principles/follow-through-and-overlap, sound-and-timing/sfx-spotting, cookbook/draw-a-line-along-a-path]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://autoae.online/blog/logo-sting, https://www.krumzi.com/blog/how-to-make-an-animated-logo]
---

# Make a logo sting

**Goal.** A three-second brand moment: a frame draws, the mark lands, the name and line follow, a short
hold, a clean exit.

## Steps (90 f at 30 fps)

| Beat | Frames | Object and keys |
|---|---|---|
| Frame draws | f0–f18 | ring (ellipse, stroke only) `trimEnd` `"0%"` → `"100%"`, expo out |
| Mark lands | f10–f26 | mark `scale` 0 → 1 back out, `rotate` `"40deg"` → `"0deg"` expo (clockwise; the 0.1.6 note said −40°) |
| Name rises | f20–f38 | wordmark 40 px rise, expo; opacity in over 9 f |
| Line | f32–f42 | tagline opacity 0 → 1, quad out |
| Hold | f42–f76 | nothing moves: let the logo read |
| Exit | f76–f88 | all `opacity` 1 → 0, accelerate (`cubic-bezier(0.3, 0, 0.8, 0.15)`) |

Overlap the beats by 6–10 f so it reads as one gesture. Put a sound hit on the frame the mark lands
(f10–f12), not at f0.

## Measured in Carvercat 0.1.6

Comp `K Logo sting` in [cookbook lab 1](../labs/README.md#cookbook-lab-1carverproj), measured with
`carvercat_inspect` (`curves`, `composite`, `lint`):

- Ring: first ink f1, **98% drawn at f9** (expo puts most of the stroke in the first half).
- Mark scale: overshoot **9.8%**, settles **f25**; rotation settles f20.
- Wordmark rise: no overshoot, settles **f32**.
- `carvercat_look`: the full lock-up reads from f36; f88 is empty.
- `inspect lint`: **0 errors, 0 warnings**, 3 notes (`repeated_key_value` for the held opacity of the
  wordmark and tagline, `speed_jump` on the wordmark's first frame). Both are expected for a hold and a
  cut-in rise.

## Traps

- Text only resolves installed fonts: [KI-136](../../ai/references/known-issues.md#ki-136).
- `preset.apply` takes one `id` at a time: [KI-113](../../ai/references/known-issues.md#ki-113).
- Shapes larger than the comp are cropped before scaling, so draw a burst at comp size and scale it up:
  [KI-137](../../ai/references/known-issues.md#ki-137).

## In Carvercat

- `trimEnd` keys by design name: `anim.set {id, keyframes: [{at, trimEnd: "0%", ease}, {at, trimEnd: "100%"}]}`, `ease` on the key that leaves (checked: `wiki/tools/verify_keyed_pages.py`, case draw-a-line-along-a-path). A static `trimEnd` is one call. The older stored key `trim.end` (0 to 1) still works.
- Curve names on this page (expo out, quad out, back out, accelerate) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library templates: `Logo resolve - frame` ([cb-logo-resolve](../../ai/patterns/cb-logo-resolve.md)),
  `Logo - stamp reveal` (Motion Patterns pack, [logo-stamp-reveal](../../ai/patterns/logo-stamp-reveal.md)), `Logo reveal`,
  `Brand end card` ([cb-end-card](../../ai/patterns/cb-end-card.md)).
- Presets for the parts: `Pop - spring`, `Rise - expo`, `Exit fade - fast`.
- Background: [logo animation](../genres/logo-animation.md), [follow-through and overlap](../principles/follow-through-and-overlap.md),
  [SFX spotting](../sound-and-timing/sfx-spotting.md).
