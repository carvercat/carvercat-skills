---
id: techniques/stroke-dashes
title: Dashed and dotted strokes
section: techniques
tags: [dash, dotted, stroke, marching ants, route, map, selection, line style]
styles: [explainer, futuristic-hud, data-viz, saas-ui]
topics: [stroke, lines]
related: [techniques/line-drawing, genres/infographics, techniques/looping]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://blog.nobledesktop.com/learn/after-effects/stroke-animation, https://pixelbakery.com/recipes/trim-paths-animate-text]
---

# Dashed and dotted strokes

Dashed lines say "planned", "route", "boundary", "selection" or "connection to come": map routes, flow
connectors, target areas, guide lines in HUDs. Animated, they suggest movement along the path.

## The idea

- **Static dashes** for meaning (a planned route, a hidden edge).
- **Drawing on a dashed line**: the dashes appear in sequence as the line grows.
- **Marching dashes** (dashes moving along the path) for "active" or "in progress".

## Rules of thumb

- Dash about 2–5× the stroke width; gap about 1.5–3× the stroke width.
- Round caps add half the stroke width to each end of every dash and eat into the gaps; allow for it.
- Draw-on for dashed lines reads best slower than for solid lines (20–40 f).

## Measured in Carvercat

A 1500 px line with a 6 px round-capped stroke (`strokeWidth: 6`, `strokeLinecap: "round"`), dashed with `strokeDasharray`, rendered and measured by pixel runs:

| Setting (round caps, 6 px stroke) | Rendered dash | Rendered gap |
|---|---|---|
| `strokeDasharray: "30px 10px"` (0.1.6: dash 30, gap keyed from 10) | 37 px; 35–36 px on the design-units build (38 dashes) | 2–3 px; 4–5 px |
| `strokeDasharray: "10px 20px"` (0.1.6: dash keyed from 10, gap 20) | 16 px (also 16 px, 50 dashes, on the design-units build) | 14 px (14 px) |

- Round caps added 6 px (the stroke width) to every dash and took the same from every gap, as expected.
- **The model lays the dashes out once, as a whole count** `n = round(length ÷ (dash + gap))`, drawn fraction `dash ÷ (dash + gap)`; the reply's `units.dashEffective` (`{d, g, count, outlinePx, exact}`) says the dash that is really drawn (1500 ÷ 40 = 37.5, so 38 dashes of 29.6 px plus the 6 px caps = 35.6 px, measured 35–36). Round caps add the stroke width to every dash and take it from every gap.
- **Dash and gap do not animate** (`strokeDasharray` is not animatable; 0.1.6: `Dash` keyed 10 → 60 px rendered identical dashes at f0 and f59, [KI-147](../../ai/references/known-issues.md#ki-147)). Animate a dashed line with
  `trimEnd` instead (draw-on; measured on solid lines in [line drawing](line-drawing.md), not on
  dashed ones here), or by moving a mask window.

## Do and don't

- Do set dash and gap once, sized to the stroke.
- Do draw dashed lines on with `trimEnd`.
- Don't key dash or gap for marching ants (`strokeDasharray` is not animatable; 0.1.6: `Dash`/`Gap` keys did not animate).
- Don't mix dashed and dotted styles for the same meaning.

## Checklist

- [ ] Dash and gap allow for cap size.
- [ ] Dashed lines animated with trim or masks, not dash keys.

## In Carvercat

- Keys: `strokeDasharray` (`"12px 6px"`, `[12, 6]`, `dotted`, `none`), `strokeLinecap` (butt, round, square), `strokeLinejoin`, `strokeAlign`.
  `strokeDashoffset`, `pathLength` and an SVG pattern of more than two numbers are refused with the reason. Old names, accepted for one release:
  `shape.stroke.line` (solid, dashed, dotted), `dashLength` (Dash) and `dashGap` (Gap), fractions of comp width, `shape.stroke.cap`.
- Draw-on: [line drawing](line-drawing.md); routes on maps: [maps](../../ai/references/maps/maps.md).
- Lab: comp `S Dashes` in [the measurement lab 4](../labs/README.md).
