---
id: genres/infographics
title: Animated infographics
section: genres
tags: [infographic, icons, maps, charts, statistics, process, timeline, icon grid]
styles: [explainer, data-viz, corporate-brand, saas-ui]
topics: [genre, information]
related: [genres/data-stories, genres/explainers, techniques/line-drawing, techniques/stagger-systems, design/gestalt, design/grids-and-layout]
verified: no (theory only)
source_inspiration: [https://blog.nobledesktop.com/tips-for-creating-effective-animated-infographics, https://www.b2w.tv/blog/how-to-make-infographics-videos, https://advids.co/insights/visualizing-data-accurately-best-practices-for-graphs-charts-and-infographics-in-motion]
---

# Animated infographics

An animated infographic presents information visually: icons, maps, timelines, numbers and short labels,
usually to a voice-over. It sits between the explainer (one idea) and the data story (one dataset): many
small facts, organised so they can be taken in at a glance.

## The idea

- **A visual system first**: one icon style (stroke weight, corner radius, fill), one palette, one type
  family, one grid. Consistency is what makes many facts readable.
- **Group facts** with space and shared motion ([Gestalt](../design/gestalt.md)): a row of three stats enters
  as one staggered gesture; a new group gets a new gesture.
- **Draw connections**: lines, arrows and routes show relationships and sequence ([line drawing](../techniques/line-drawing.md)).
- **Numbers deserve emphasis**: the number big, the label small and close, units consistent.

## Rules of thumb

- Under about 90 s total; 5–8 s per group of facts.
- Icons at least 64 px on 1920 wide; stroke icons 4–6 px.
- Stagger items in a group 4–6 f; groups separated by a clear beat (10+ f or a transition).
- Labels within one line-height of their icon or number; animate them together.
- Maps: draw borders and routes, pin locations, zoom in only once or twice.

## Do and don't

- Do build an icon set in one style before animating.
- Do keep the same position for recurring elements (a total in the corner, a legend).
- Don't use more than one decorative motion per scene.
- Don't put more than about seven items on screen at once; split into pages.

## Checklist

- [ ] One icon style, one palette, one type family.
- [ ] Facts grouped; each group enters as one gesture.
- [ ] Numbers big, labels close, units consistent.
- [ ] Every text holds for its read time.

## In Carvercat

No new measurements on this page; the templates are measured in their packs.

- Pack: [Explainer](../../ai/patterns/explainer.md) (`Icon grid`, `Process steps`, `Pointer callout`,
  `Milestone timeline`), [Data Viz](../../ai/patterns/data-viz.md) (charts), `Three stats`
  ([cb-three-stats](../../ai/patterns/cb-three-stats.md)).
- Data Viz round 3: `Icon array` ("1 in 4 people"; [dv-icon-array](../../ai/patterns/dv-icon-array.md)) and `Tile-grid map`
  (results by state, equal tiles; [dv-tile-map](../../ai/patterns/dv-tile-map.md)).
- Corporate Brand round 3: `Org chart` (a top card and three reports joined by drawn connectors; [cb-org-chart](../../ai/patterns/cb-org-chart.md)),
  `Values grid` (four value cards; [cb-values-grid](../../ai/patterns/cb-values-grid.md)) and `Office location card`
  (map stand-in, pin and address; [cb-office-card](../../ai/patterns/cb-office-card.md)); all land with 0% overshoot.
- Explainer round 3: `Cause and effect` (a branching chain of cards joined by drawn arrows; [ex-cause-effect](../../ai/patterns/ex-cause-effect.md)),
  `Labelled diagram` (an object with four leader-line labels; [ex-labelled-diagram](../../ai/patterns/ex-labelled-diagram.md)) and
  `Icon steps` ([ex-icon-steps](../../ai/patterns/ex-icon-steps.md)).
- Maps from real geography with draw-on routes and pins: [maps](../../ai/references/maps/maps.md),
  `ai/scripts/maps/map_overlay.py`.
- A playful location: `Bouncy map pin` (a pin drops and squashes on its point, then a label pops;
  [ct-map-pin](../../ai/patterns/ct-map-pin.md)), Cartoon Bounce round 3.
- Shapes and icon drawing: [shapes](../../ai/references/drawing/shapes.md); arrows: `authoring.arrow` in a batch
  ([JSON authoring](../../ai/references/app/json-authoring.md)).
