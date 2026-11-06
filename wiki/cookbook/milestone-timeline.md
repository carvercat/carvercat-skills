---
id: cookbook/milestone-timeline
title: Animate a timeline with milestones
section: cookbook
tags: [timeline, milestones, history, roadmap, company story, years, line draw, dots]
styles: [corporate-brand, explainer, saas-ui, data-viz]
topics: [line drawing, timing, data]
related: [cookbook/draw-a-line-along-a-path, cookbook/pop-in, techniques/line-drawing, genres/explainers, sound-and-timing/reading-time]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Timeline]
---

# Animate a timeline with milestones

**Goal.** A line draws across the screen and each milestone (dot, year, caption) pops up exactly as the line
reaches it.

## Steps

1. The line: a 2-point path from x 240 to x 1680 at y 560, 6 px stroke. Key `trimEnd` `"0%"` → `"100%"` from f10 to
   f70 with **`linear`** easing: the tip then moves at a constant 24 px a frame.
2. Milestone *i* at x*ᵢ*. The tip reaches it on **f = 10 + 60 × (x*ᵢ* − 240) / 1440**: here 10, 30, 50, 70
   for x 240, 720, 1200, 1680.
3. Start each dot's clip on that frame and apply **`Pop - spring`**; the year 2 f later with `Rise - expo`,
   the caption 4 f later with `Soft rise`.
4. If you ease the trim instead, read each arrival frame off the trim curve (`inspect curves`) or with
   `inspect composite`; the formula above holds only for `linear`.

## Measured in Carvercat 0.1.6

Comp `K Milestones` in [cookbook lab 8](../labs/README.md#cookbook-lab-8carverproj); the line's tip found in
rendered frames on y 560:

| Frame | 11 | 29 | 30 | 31 | 49 | 50 | 69 | 70 |
|---|---|---|---|---|---|---|---|---|
| Tip x | 266 | 698 | 722 | 746 | 1178 | 1202 | 1658 | 1682 |

- The tip passes milestones 2, 3 and 4 (x 720, 1200, 1680) on f30, f50 and f70, within 2 px; f10 shows no line
  yet (trim 0).
- Dot 2 (`Pop - spring`, clip from f30): width 0 on f30, 41.8 px peak on f38 (16.2% over), settles **f50**.
  Year 2 (`Rise - expo` from f32) is opaque by f40 and still by f44.
- `inspect lint contrast:true`: 0 errors, 2 warnings, both on the last caption: `low_contrast` **4.23:1** for
  #8C8A86 at 32 px on the dark ground (wanted 4.5) and `reading_time` (the lab ends 26 f after it). Use a
  lighter caption grey.

## Traps

- Each preset is applied to one clip at a time ([KI-113](../../ai/references/known-issues.md#ki-113)); a
  preset keys from its clip's start, so place the clip on the arrival frame rather than moving keys.
- `inspect curves` reads the second half of a spring as overshoot if the lane holds another move
  ([KI-152](../../ai/references/known-issues.md#ki-152)).

## In Carvercat

- `trimEnd` keys by design name: `anim.set {id, keyframes: [{at, trimEnd: "0%", ease}, {at, trimEnd: "100%"}]}`, `ease` on the key that leaves (checked: `wiki/tools/verify_keyed_pages.py`, case draw-a-line-along-a-path). A static `trimEnd` is one call. The older stored key `trim.end` (0 to 1) still works.
- Library: `Timeline` and `Milestone timeline` scenes, `Pop - spring`, `Rise - expo`, `Soft rise`.
- Background: [line drawing](../techniques/line-drawing.md), [draw a line along a path](draw-a-line-along-a-path.md),
  [reading time](../sound-and-timing/reading-time.md).
