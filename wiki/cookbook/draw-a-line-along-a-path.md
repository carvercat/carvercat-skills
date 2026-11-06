---
id: cookbook/draw-a-line-along-a-path
title: Draw a line along a path
section: cookbook
tags: [trim, draw on, route, path, stroke, line, write on, map route, connector]
styles: [explainer, data-viz, corporate-brand, minimal-luxury, futuristic-hud]
topics: [stroke, reveal]
related: [techniques/line-drawing, techniques/stroke-dashes, genres/infographics, cookbook/logo-sting]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://blog.nobledesktop.com/learn/after-effects/stroke-animation, https://pixelbakery.com/recipes/trim-paths-animate-text]
---

# Draw a line along a path

**Goal.** A curved route that draws itself from a start dot to an end dot, then holds.

## Steps

1. Draw the route as a **path** shape (pen, or `object.path {d}` with SVG path data in px, y down). `fill: "none"`,
   `stroke` a colour, `strokeWidth: 8`, `strokeLinecap: "round"`.
2. Key `trimEnd` `"0%"` → `"100%"` (the first write of `trimEnd` adds the Trim Stroke; `anim.set` with `trimEnd` keys it by name, `ease` on the key that leaves). S-curve gives a steady pen;
   expo out gives a fast throw with a long finish.
3. Pop a **start dot** just before the draw and an **end dot** on the frame the draw completes, so the
   eye knows where the line comes from and where it lands.

## Measured in Carvercat 0.1.6

Comp `K Draw path` in [cookbook lab 1](../labs/README.md#cookbook-lab-1carverproj): a 4-node curved path
(about 1400 px across), 8 px round-capped stroke, `trimEnd` `"0%"` → `"100%"` over f10–f40 S-curve; measured with
`carvercat_inspect mode:composite` every frame.

| Frame | Drawn (share of the final stroke pixels) |
|---|---|
| f12 | first ink |
| f25 | 50% (the midpoint of the S-curve) |
| f37 | 98% |
| f40 | 100% |

- Start dot scale 0 → 1 over f6–f16 back out (0.34, 1.56, 0.64, 1): overshoot **9.7%**, settles f16.
- End dot scale 0 → 1 over f40–f52 back out: overshoot **9.8%**, settles f51; it covers the line's tip.
- `inspect lint`: **0 errors, 0 warnings, 0 notes**.

## Traps

- Fill does not follow the trim; draw-on is for strokes. For filled shapes use a mask
  ([masking](../techniques/masking.md)).
- Keyed dash length and gap do not animate, so "marching ants" need `trimOffset`:
  [KI-147](../../ai/references/known-issues.md#ki-147).
- A path's stored position is not its rendered centre: [KI-060](../../ai/references/known-issues.md#ki-060).
- The pen's default stroke covers the fill: [KI-059](../../ai/references/known-issues.md#ki-059).

## In Carvercat

- Curve names on this page (S-curve, expo out, back out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Keys `trimStart`, `trimEnd`, `trimOffset` (%); stroke keys `stroke`, `strokeWidth`, `strokeLinecap`, `strokeDasharray`. Old names,
  accepted for one release: the `trim` effect's `start`/`end`/`offset` (0 to 1), `shape.stroke` `width` (a fraction of the comp width: 8 px = 0.0042 at 1920), `cap`, `line`. Detail: [stroke and trim](../../ai/references/effects/stroke-and-trim.md).
- Library: `Dotted arrow`, `Leader callout` ([cb-leader-callout](../../ai/patterns/cb-leader-callout.md)),
  `Timeline` ([dv-timeline](../../ai/patterns/dv-timeline.md)), map routes
  ([maps](../../ai/references/maps/maps.md)).
- Background: [line drawing](../techniques/line-drawing.md), [stroke dashes](../techniques/stroke-dashes.md).
