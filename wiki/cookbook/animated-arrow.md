---
id: cookbook/animated-arrow
title: Draw an arrow that points at something
section: cookbook
tags: [arrow, pointer, draw on, curved arrow, arrowhead, trim, explainer, annotation]
styles: [explainer, saas-ui, social-short-form, funky]
topics: [shapes, line drawing]
related: [cookbook/draw-a-line-along-a-path, cookbook/point-at-something, techniques/line-drawing, genres/explainers]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/animation-usability/]
---

# Draw an arrow that points at something

**Goal.** A curved arrow draws itself towards a label, and its head snaps on at the end, pointing along
the line.

## Steps

1. Shaft: a 2-point path with handles, 10 px stroke, round caps. The last point's **in-handle** sets the
   direction the line arrives in: here (−260, +156) px, so it arrives heading up and to the right.
2. Draw it on with `trimEnd` `"0%"` → `"100%"`, S-curve, 22 f (the first write of `trimEnd` adds the Trim Stroke; `anim.set` with `trimEnd` keys it by name).
3. Head: a separate open 3-point path (a chevron) drawn pointing **right**, tip on the shaft's end point,
   arms 44 px back and 40 px out, same stroke, round caps and corners.
4. Anchor the head on its tip (`transformOrigin` `"100% 50%"`, the right-middle of its bounds) and rotate it to the
   arriving direction: atan2(156, 260) = 31.0°, which is `rotate` **`"-31deg"`** (rotate is clockwise, so up and to the right is negative).
5. Start the head clip 2 f before the trim ends; pop it in with scale 0 → 1, **back out**, 8 f.

## Measured in Carvercat 0.1.6

Comp `K Arrow` in [cookbook lab 6](../labs/README.md#cookbook-lab-6carverproj): shaft from (420, 760) to
(1380, 440), trim f8–f30, head from f28; `inspect composite` and `carvercat_render` at f50:

- The shaft first showed at **f9** and was 98% drawn at **f29**.
- The head popped 9.3% over and settled at **f36**.
- Rendered pixels: the tip (1380, 440) and both rotated arm points at 80% of their length, (1333, 431) and
  (1366, 486), are arrow amber (242, 176, 60); the unrotated arm point (1345, 408) is paper: the 31° turn is
  what lines the head up with the shaft.
- `inspect lint`: **0 errors, 0 warnings, 0 notes**.

## Traps

- There is no arrow primitive or arrow command; it is a shaft plus a head:
  [KI-114](../../ai/references/known-issues.md#ki-114).
- Turn the head with `rotate`. The old shape `angle` is stored but not drawn:
  [KI-057](../../ai/references/known-issues.md#ki-057), [KI-150](../../ai/references/known-issues.md#ki-150).
- Stored path placement is not the rendered centre; place the head by its tip and check it on a render:
  [KI-060](../../ai/references/known-issues.md#ki-060).

## In Carvercat

- Curve names on this page (S-curve, back out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Arrow`, `Dotted arrow`, `Pointer callout` ([ex-callout](../../ai/patterns/ex-callout.md)),
  `Leader callout` ([cb-leader-callout](../../ai/patterns/cb-leader-callout.md)).
- Old names, accepted for one release: `trim.end` (0 to 1), `transform.placement.rotation` (counter-clockwise positive), `anchor` in half-sizes.
- Background: [draw a line along a path](draw-a-line-along-a-path.md), [line drawing](../techniques/line-drawing.md).
