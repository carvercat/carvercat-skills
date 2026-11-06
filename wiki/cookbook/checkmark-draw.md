---
id: cookbook/checkmark-draw
title: Draw a success checkmark
section: cookbook
tags: [checkmark, tick, success, done, confirmation, draw on, trim, ui feedback]
styles: [saas-ui, explainer, social-short-form]
topics: [ui, line drawing]
related: [cookbook/draw-a-line-along-a-path, cookbook/donut-fill, cookbook/pop-in, genres/ui-ux-demos]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/animation-purpose-ux/]
---

# Draw a success checkmark

**Goal.** "Done": a ring draws round, fills green with a small pop, and a white tick draws itself across it.

## Steps

1. Ring: a 240 px circle, no fill, 12 px green stroke; `trimEnd` `"0%"` → `"100%"`, S-curve, 16 f (`anim.set` with `trimEnd` keys it by name).
2. Disc: a filled 240 px green circle on a clip starting as the ring closes, with **`Pop - gentle`**
   (from 60%, 4.4% over).
3. Tick: an open 3-point path, 16 px white stroke, round caps and corners; short arm down-right, long arm
   up-right. `trimEnd` `"0%"` → `"100%"`, **decelerate**, 10 f, starting as the disc lands.

## Measured in Carvercat 0.1.6

Comp `K Checkmark` in [cookbook lab 7](../labs/README.md#cookbook-lab-7carverproj): ring f4–f20, disc from f18,
tick f20–f30; `inspect composite` and `inspect curves`:

- The tick first showed at **f21** and was 98% drawn at **f27**: decelerate draws most of the stroke in the
  first frames, so it reads as a quick flick.
- `Pop - gentle` on the disc: opaque from f25, scale 0.6 → 1.018 (f29) → 1, settled **f36**.
- `inspect lint`: 0 errors, 0 warnings, 1 note.
- The ring's own draw can't be read from `inspect composite` once the disc covers it (its pixel count kept
  changing until f33); use its trim keys, f4–f20.

## Traps

- An ellipse's trim starts at 3 o'clock and runs counter-clockwise (the reply says `trimOrigin`); mirror or rotate it to start
  elsewhere ([donut fill](donut-fill.md), [loading spinner](loading-spinner.md)).
- Stored path placement is not the rendered centre; check the tick sits in the disc on a render:
  [KI-060](../../ai/references/known-issues.md#ki-060).

## In Carvercat

- Curve names on this page (S-curve, decelerate) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Check` sticker, `Checklist` ([ex-checklist](../../ai/patterns/ex-checklist.md)), the submit-success
  pattern [su-submit-success](../../ai/patterns/su-submit-success.md), `Pop - gentle`.
- Background: [draw a line along a path](draw-a-line-along-a-path.md), [line drawing](../techniques/line-drawing.md).
