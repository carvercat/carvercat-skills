---
id: cookbook/tutorial-callouts
title: Add numbered tutorial callouts to a screen
section: cookbook
tags: [callout, tutorial, annotation, numbered steps, screen recording, how-to, pointer, label]
styles: [saas-ui, explainer, corporate-brand]
topics: [annotation, timing, layout]
related: [cookbook/point-at-something, cookbook/animated-arrow, cookbook/draw-a-line-along-a-path, cookbook/pop-in, genres/ui-ux-demos]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/animation-duration/]
---

# Add numbered tutorial callouts to a screen

**Goal.** Over a screen recording, a numbered circle pops in beside a control, a line draws to it, and a
label rises next to the number; the next callout follows 40 frames later.

## Steps

1. For callout *k* (k = 0, 1, 2) start at **f = 20 + 40 k**.
2. **Circle**: an amber disc 80 px with the number (48 px, dark) on top; both scale 0 → 1 over 12 f with the
   `pop` bezier (0.34, 1.75, 0.64, 1). Put the circle beside the control, not on it.
3. **Line**: a 2-point path from the circle's edge (40 px along the direction) to the control's edge, 5 px, round
   caps. Key `trimEnd` `"0%"` → `"100%"` from f + 8 to f + 20 with expo out. End the line a few px short of the control so
   it touches the edge, not the middle: stop where the line leaves the control's box plus 6 px.
4. **Label**: 44 px text 62 px right of the circle centre, starting f + 12, rising 24 px with opacity 0 → 1
   (expo, 14 f).
5. Hold the last callout for 30 f or more; with three callouts the comp is 150 f.

## Measured in Carvercat 0.1.6

Comp `K Callouts` in [cookbook lab 9](../labs/README.md#cookbook-lab-9carverproj); circle width by `inspect
probe`, line tip by finding amber pixels along the line in rendered frames:

| Callout 1 (starts f20) | f20 | f24 | f28 | f32 |
|---|---|---|---|---|
| Circle width | 0 | 83.3 | 90.0 | 80.0 |
| Line tip, px from circle centre | none | none | 44 | 168 |

- The circle overshoots to **90 px (12.5%)** on +8 f and settles at 80 px on +12 f (`inspect curves`: 15.8% on
  the scale, between sampled frames).
- Line tip at +8, +10, +12, +14, +20 f: 44, 137, 168, 178, 182 px; the aim point was 180.6 px, and the stroke's
  round cap adds about 1.5 px. Callouts 2 and 3 ended at 206 (aim 204.0) and 162 (aim 160.2).
- Label 1: opacity 0.82 and cy 257.3 on f36, 1.0 and 254.4 on f40, 254.0 at rest: it rose 24 px.
- Callouts 2 and 3 are the same, 40 and 80 f later (circles start f60 and f100).
- `inspect lint`: 0 errors, **3 warnings**, `text_too_small` on the three numbers (12.9–13.1 px tall) although
  they are 48 px at rest: lint measured the frames where the pop was still small
  ([KI-162](../../ai/references/known-issues.md#ki-162)).

## Traps

- Number text keyed from scale 0 trips `text_too_small`: [KI-162](../../ai/references/known-issues.md#ki-162);
  start the number at scale 0.5 or higher, or accept the warning.
- A line to a control's centre hides under the control; stop on the box edge.
- The label must not overlap a control or another callout; check with `carvercat_look` at the last frame.

## In Carvercat

- `trimEnd` keys by design name: `anim.set {id, keyframes: [{at, trimEnd: "0%", ease}, {at, trimEnd: "100%"}]}`, `ease` on the key that leaves (checked: `wiki/tools/verify_keyed_pages.py`, case draw-a-line-along-a-path). A static `trimEnd` is one call. The older stored key `trim.end` (0 to 1) still works.
- Curve names on this page (expo out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Callout`, `Pointer callout`, `Leader callout`, `Cursor`, `Step`; `Pop - spring` for the circle.
- Background: [point at something](point-at-something.md), [draw a line along a path](draw-a-line-along-a-path.md),
  [UI and UX demos](../genres/ui-ux-demos.md).
