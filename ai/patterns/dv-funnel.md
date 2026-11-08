# Conversion funnel

**Template** `dv_funnel` (Library name "Conversion funnel") · Data Viz pack · **Verified 0.1.8.4 (rev 1130)**, comp `DV Funnel` in `categories/data-viz/dv-lab-3`.

For briefs like "checkout funnel", "sales pipeline", "where do we lose people". Five centred bars whose widths are their values on one scale (48,200 → 2,890 shoppers, sample data), joined by trapezoid connectors, with the count of each step and the share that continues. The step with the biggest drop is amber, and a takeaway line names it. 150 f, holds.

Frames are comp frames.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Title, subtitle, "Sample data" | 0 | opacity in 8 f, 3 f apart | |
| Step labels (Medium 32 px, right-aligned) | 0 | opacity in, 4 f before their bar | |
| Bars (80 px tall, 880 px for the top step) | 6 + 8 per step | width 0 → 1 from the centre line, 14 f, expo | **0% overshoot**; Bar 1 settles **f15**, Bar 5 **f47** |
| Values (Bold 36 px) | bar + 10 | 16 px from above, 12 f | Value 5 settles **f56** |
| Connectors and rates ("45% continue", 28 px) | next bar + 10 | opacity in 8 f (grey connectors to 1, the amber one to 0.55); rate rises 16 px | Connector 2 settles **f40** |
| Annotation (amber SemiBold 30 px, under the funnel) | 66 | 16 px from above, 12 f | settles **f74** |

Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (closest 24.9 px, title / subtitle).

## Steps
1. New numbers: edit `FUNNEL` in `ai/scripts/motion/data_viz_lab3.py` and rebuild; widths, rates and the amber step are computed.
2. Change the annotation text to the finding the client wants remembered; keep it to one line.

## Pitfalls
- Bars are sized on one scale, so late steps get thin (2,890 of 48,200 is 53 px). Do not widen them for looks: that misstates the drop. If the late steps matter more, make a second funnel of only those steps.
- The bars grow from the centre (the default anchor), so no anchor change is needed; a left anchor would make the funnel lean.

Inspiration: conversion funnels in product analytics. No external text or code was used.
