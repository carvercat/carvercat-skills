---
id: cookbook/point-at-something
title: Point at something with a callout
section: cookbook
tags: [callout, leader line, label, annotation, pointer, feature, explainer]
styles: [explainer, saas-ui, corporate-brand, futuristic-hud]
topics: [annotation, stroke, text]
related: [techniques/line-drawing, design/visual-flow, cookbook/draw-a-line-along-a-path, cookbook/ripple]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://pixelbakery.com/recipes/trim-paths-animate-text, https://www.nngroup.com/articles/principles-visual-design/]
---

# Point at something with a callout

**Goal.** A dot lands on a feature, a leader line draws out from it, and a label arrives at the line's end.

## Steps (in order, overlapping)

1. **Target** (f6): a small dot pops on the feature (scale 0 → 1, back out, 12 f) with a ring that grows and
   fades once (0.4 → 1.4, 18 f).
2. **Leader** (f10–f24): a 3-point path from the dot, angled up and then level, 3 px stroke, `trimEnd`
   `"0%"` → `"100%"` expo. Draw **from** the feature, so the eye travels to the label.
3. **Label** (f20) rises 20 px over 14 f expo where the line levels off; a sub-line 4 f later.
4. Keep the label clear of the object and inside the graphics-safe area.

## Measured in Carvercat 0.1.6

Comp `K Callout` in [cookbook lab 4](../labs/README.md#cookbook-lab-4carverproj), measured with
`inspect curves` and `composite`:

| Part | Keys | Result |
|---|---|---|
| Target dot | scale f6 → f18 back out | overshoot 9.8%, settles f17 |
| Leader | `trimEnd` f10 → f24 expo | first ink f11, 98% drawn **f18** |
| Label (48 px Bold) | rise f20 → f34 | settles f29 |
| Sub-line (32 px Medium) | rise f24 → f38 | settles f33 |

- `inspect lint contrast:true`: 0 errors, 0 warnings, 2 notes (`speed_jump` on the two rises).

## Traps

- Lint wants 18 px of measured line height: lowercase words without ascenders fail under about a 35 px
  font size ([search typing](../../ai/patterns/su-search-typing.md)); small Regular text also skips the
  contrast check: [KI-142](../../ai/references/known-issues.md#ki-142).
- The pen's default stroke covers the fill: [KI-059](../../ai/references/known-issues.md#ki-059).
- No arrow primitive; build arrowheads from a polygon: [KI-114](../../ai/references/known-issues.md#ki-114).

## In Carvercat

- `trimEnd` keys by design name: `anim.set {id, keyframes: [{at, trimEnd: "0%", ease}, {at, trimEnd: "100%"}]}`, `ease` on the key that leaves (checked: `wiki/tools/verify_keyed_pages.py`, case draw-a-line-along-a-path). A static `trimEnd` is one call. The older stored key `trim.end` (0 to 1) still works.
- Curve names on this page (back out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Leader callout` ([cb-leader-callout](../../ai/patterns/cb-leader-callout.md)), `Callout`
  ([ex-callout](../../ai/patterns/ex-callout.md)), `Map ping` ([fh-map-ping](../../ai/patterns/fh-map-ping.md)),
  stickers `Arrow`, `Dotted arrow`.
- Background: [line drawing](../techniques/line-drawing.md), [visual flow](../design/visual-flow.md).
