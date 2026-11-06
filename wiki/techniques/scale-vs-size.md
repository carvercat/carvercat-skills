---
id: techniques/scale-vs-size
title: Animating scale vs size
section: techniques
tags: [scale, size, width, height, stroke width, corner radius, resize, geometry]
styles: [saas-ui, data-viz, explainer, corporate-brand]
topics: [shapes, transform]
related: [techniques/morphing, principles/squash-and-stretch, techniques/line-drawing, techniques/faux-3d]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://uxmag.com/articles/creating-usability-with-motion-the-ux-in-motion-manifesto, https://carbondesignsystem.com/elements/motion/choreography/]
---

# Animating scale vs size

A shape can grow two ways: **scale** it (the whole drawing is magnified, strokes and corners included) or
change its **size** (the geometry gets wider and taller while stroke width and corner rounding follow their
own rules). They look the same at the start and very different at the end.

## The idea

- **Scale** magnifies everything: a 4 px outline becomes 12 px at 3×; small details get chunky. Good for
  pops, zooms and anything that should feel like it comes closer.
- **Size** resizes the shape: outlines keep their weight. Good for UI (a card expanding into a panel, a bar
  growing to its value, a button stretching to fit text).
- Squash and stretch are scale moves (non-uniform scale about an anchor); a container resizing around its
  content is a size move.

## Measured in Carvercat

Two 160 × 100 rounded rectangles (`borderRadius` 16) with an 8 px stroke grew to 480 × 300 over 20 f, one by
`scale` 1 → 3, one by keying `width` and `height` (px: 160 → 480 and 100 → 300).
Probe bounds were identical (160 × 100 → 480 × 300). The rendered frame was not:

| Method | Stroke thickness at the end (pixel rows) | Look |
|---|---|---|
| Scale 3× | 23 px | outline tripled; corners and edges visibly stair-stepped |
| Width and height keys | 10 px (8 px plus anti-aliased edges) | outline kept its weight; edges smooth |

So scaling a stroked shape up both thickens its outline and costs edge quality at large factors. Keep
resting scales near 1 and build big shapes at their final size.

## Do and don't

- Do resize (width/height) when the outline weight or corner look must stay constant.
- Do scale when the whole object should feel nearer or bigger, especially for short pops.
- Don't scale small artwork up 3× or more and hold it; rebuild it at size instead.
- Don't animate width and height for a simple pop; scale is easier and pivots about the anchor.

## Checklist

- [ ] Shapes with strokes that change size use geometry keys or end at scale 1.
- [ ] Large final states are built at size, not scaled up.
- [ ] The end frame checked at full size with `carvercat_look {region}`.

## In Carvercat

- Scale: `scale` (point, keyframeable), pivoting about `transformOrigin`.
- Size: `width`, `height` (px or %) and `borderRadius` (px or % of the short side); the same keys on ellipse, polygon and star (keyframeable).
- Stroke: `strokeWidth` (px). Old names, accepted for one release: `shape.geometry.rectangle` `Width`, `Height` (fractions of comp width),
  `Corner radius`, `shape.stroke` `Width` (a fraction of comp width: 8 px = 0.0042 at 1920).
- Growing bars from an edge: set `transformOrigin` on that edge then scale, as in `Grow up (Y)` and `Grow across (X)`
  ([Motion Patterns](../../ai/patterns/README.md)).
- Lab: comp `M Scale vs size` in [the measurement lab 2](../labs/README.md).
