---
id: genres/data-stories
title: Data stories
section: genres
tags: [data, charts, statistics, data journalism, numbers, bar chart, line chart, truthful motion]
styles: [data-viz, corporate-brand, explainer]
topics: [genre, data, honesty]
related: [genres/infographics, techniques/line-drawing, techniques/stagger-systems, design/colour-psychology, principles/exaggeration]
verified: no (theory only)
source_inspiration: [https://advids.co/insights/visualizing-data-accurately-best-practices-for-graphs-charts-and-infographics-in-motion, https://link.springer.com/article/10.1007/s12650-025-01066-5, https://netzwerkrecherche.org/wp-content/uploads/2025/10/Bayer-Morini-Data-videos-101.pdf, https://dasycenter.org/datavis-toolkit/animations/]
---

# Data stories

A data story turns numbers into a sequence of facts the viewer can follow: one chart, one finding, one
transition to the next. Motion helps by revealing data in the order it should be read and by connecting
one view to the next. It hurts when it distorts, decorates or overloads.

## The idea

- **A data video is a chain of facts**: each scene states one finding ("sales doubled in Q3"), shows the
  chart that proves it, and hands over to the next fact.
- **Transitions carry the argument**: the same bars re-sort into a ranking, a line extends into the
  forecast, a total splits into its parts. Keep marks continuous so the viewer can track them.
- **Truthful motion**: animated values must pass through honest states. Bars grow from a zero baseline,
  axes do not rescale silently, nothing overshoots its value in a serious story.
- **Annotation is the story**: a highlighted bar, a labelled point, a short headline. Without it, a chart is
  decoration.

## Rules of thumb

- One finding per scene; 4–8 s per chart including read time for its headline and labels.
- Reveal in reading order: axes and baseline, then data, then highlight, then the headline number.
- Bars and segments staggered 3–4 f; values appear just after their bar lands.
- Overshoot: none for serious data; a small spring only for playful brands and never so large it misstates.
- Colour: one highlight hue for the subject, grey for context; labels instead of legends where possible.
- Avoid 3D charts and perspective; they distort comparison.

## Do and don't

- Do keep the same element (a bar, a dot) on screen across a transition so the eye follows it.
- Do show the source on screen or in the end card.
- Don't animate the axis scale without showing it.
- Don't count numbers up so slowly that the viewer cannot read the final value.

## Checklist

- [ ] One finding per scene, stated in a headline.
- [ ] Baselines at zero for bars; no silent axis changes.
- [ ] Highlight colour used once per chart.
- [ ] Final values held long enough to read; source credited.

## In Carvercat

No new measurements on this page; chart templates are measured in their own docs.

- Pack: [Data Viz](../../ai/patterns/data-viz.md): `Bar grow up - spring`, `Data point pop`, `Line chart - draw`,
  `Donut - fill`, `Ranked bars`, `Gauge`, `Column chart`, `Stacked bar`, `Progress rings`, `Comparison bars`,
  `Timeline`, `Waffle chart`, `Area chart`, `Data table`.
- Round 3 for briefs the first rounds could not serve: `Conversion funnel` ([dv-funnel](../../ai/patterns/dv-funnel.md)),
  `Bubble chart` ([dv-bubble-chart](../../ai/patterns/dv-bubble-chart.md)), `Bar chart race` (a ranking over years on one fixed
  scale; [dv-bar-race](../../ai/patterns/dv-bar-race.md)), `Stacked area chart` ([dv-stacked-area](../../ai/patterns/dv-stacked-area.md)),
  `Calendar heatmap` ([dv-heatmap](../../ai/patterns/dv-heatmap.md)); all land with 0% overshoot and say "Sample data" on screen.
- Sports data (Sports round 3): `League table movement` (points change, then the row climbs; [sp-table-move](../../ai/patterns/sp-table-move.md))
  and `Tournament bracket` (winners lit by score; [sp-bracket](../../ai/patterns/sp-bracket.md)).
- Recipe: [quarterly results](../../ai/recipes/quarterly-results.md).
- Counting numbers: [rolling counter](../../ai/patterns/su-rolling-counter.md) (masked digit columns; a native
  number text is a feature request, FR-034 in [known issues](../../ai/references/known-issues.md#fr-034)).
- Bars grow from their base: `transformOrigin` `"50% 100%"` then `scale` `[1, v]` ([Motion Patterns](../../ai/patterns/README.md)).
