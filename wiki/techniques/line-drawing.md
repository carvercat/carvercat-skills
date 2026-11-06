---
id: techniques/line-drawing
title: Line drawing and trim paths
section: techniques
tags: [trim, draw on, stroke, line, path, write on, travelling dash, underline, icon draw]
styles: [explainer, corporate-brand, data-viz, minimal-luxury, futuristic-hud]
topics: [stroke, reveal]
related: [techniques/masking, techniques/morphing, genres/infographics, genres/logo-animation, principles/secondary-action]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://blog.nobledesktop.com/learn/after-effects/stroke-animation, https://pixelbakery.com/recipes/trim-paths-animate-text, https://community.adobe.com/t5/after-effects-discussions/a-line-to-reveal-shape/m-p/13438268]
---

# Line drawing and trim paths

A line that draws itself is one of the clearest ways to show a path, a connection, a route, a chart or a
signature. The technique: a stroked shape whose visible portion is animated from nothing to the whole
length ("trim").

## The idea

- **Draw on**: the visible end grows from 0 to 1 along the path.
- **Draw off**: the start catches up with the end; the line disappears in its direction of travel.
- **Travelling dash**: a short visible window (start and end close together) slides along the path, like
  a pulse in a wire or a comet.
- Lines lead the eye: the draw direction is a reading direction. Draw left to right, top to bottom, or
  from cause to effect.

## Rules of thumb

- Draw-on duration 15–30 f for a hero line, 8–15 f for an underline or a box around a word.
- Ease out (decelerate into the end) so the line arrives rather than stops.
- Round caps for friendly styles, butt caps for technical ones; keep one cap style per film.
- Stroke widths: 2–4 px for UI and data, 6–10 px for illustrative lines at 1920 wide.
- Stagger several lines 3–6 f; draw the main line first, then its labels.

## Measured in Carvercat

Three stroked shapes with `trimStart` / `trimEnd` / `trimOffset` (the Trim Stroke effect), checked with `carvercat_look` and `carvercat_inspect mode:composite`:

| Shape | Keys | Result |
|---|---|---|
| 4-point open path, 8 px | `trimEnd` `"0%"` → `"100%"`, f10–f30, expo out | 50% of its final drawn pixels at f12 (2 f in), 76% at f14, 94% at f18, complete at f26 |
| Straight 2-point path, 8 px | `trimStart` `"0%"`, `trimEnd` `"20%"` (fixed), `trimOffset` `"0%"` → `"80%"` over f10–f40 (S-curve) | a dash 20% of the length travelled from the left end to the right end |
| Ellipse with stroke only, 8 px | `trimEnd` `"0%"` → `"100%"`, f10–f34, expo out | a circle drawing itself: 45% at f12, 92% at f18, complete at f24 |

With expo out the line covers most of its length in the first quarter of the move: a fast stroke with a
long, gentle finish. For a steadier "pen" feel use S-curve or quad out.

## Do and don't

- Do give the stroke no fill (`fill: "none"`) when trimming.
- Do start the draw at the end the eye should follow from.
- Don't trim filled shapes and expect the fill to draw on; fill does not follow the trim. Use a mask for that
  ([masking](masking.md)).
- Don't draw many lines at the same speed at the same time; stagger them.

## Checklist

- [ ] The stroke draws in the reading direction.
- [ ] The line arrives with an ease out and holds.
- [ ] Caps and widths are consistent across the film.
- [ ] Mid-draw frames look intentional (`carvercat_look`).

## In Carvercat

- Curve names on this page (S-curve, expo out, quad out, decelerate) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Keys: `trimStart`, `trimEnd`, `trimOffset` in % (range 0 to 100, offset -100 to 100; shapes only). The first write of any of them adds
  the Trim Stroke effect, and the reply says where it starts: `trimOrigin` (rectangles and ellipses start where the ray right of the centre meets the
  outline and run counter-clockwise on screen; a path starts at its first point). Key `trimEnd` for draw on, `trimStart` for draw off,
  `trimOffset` for a travelling window. All three key by design name in `anim.set` and `key.set`; the effect's stored parameter (0 to 1) still works.
- Stroke: `stroke`, `strokeWidth: 8` (px), `strokeLinecap` butt/round/square, `strokeDasharray` solid/dashed/dotted. Old names, accepted for one release:
  the `trim` effect `Start`/`End`/`Offset` as 0 to 1, `effect.add {cap: "trim"}`, `shape.stroke` `Width` (a fraction of comp width: 8 px = 0.0042 at 1920), `Cap`, `Line`.
- Where an ellipse's stroke starts and which way it runs: [data-viz measured geometry](../../ai/patterns/data-viz.md).
- Ready-made: `Line chart - draw` ([dv-line-chart](../../ai/patterns/dv-line-chart.md)), `Timeline`
  ([dv-timeline](../../ai/patterns/dv-timeline.md)), `Logo resolve - frame`
  ([cb-logo-resolve](../../ai/patterns/cb-logo-resolve.md)), `Leader callout`
  ([cb-leader-callout](../../ai/patterns/cb-leader-callout.md)), map routes ([maps](../../ai/references/maps/maps.md)).
- More: [stroke and trim](../../ai/references/effects/stroke-and-trim.md).
- Lab: comp `T Line drawing` in [the techniques lab](../labs/README.md).
