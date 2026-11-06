# Quarterly results, 21.5 s

**Brief:** present a quarter's numbers as a sequence of charts, each with one point. **Verified 0.1.6 (rev 1105), 2026-10-28; builder and measures re-run on Carvercat 0.1.8, 2026-11-04** Sample: `categories/recipes/quarterly-results` (645 f, 1920 × 1080, slate gradient). Builder: `ai/scripts/motion/recipes/rc_dataviz.py` (the master is a `carvercat/2` file or one `scene.apply`: [how](README.md#how-the-samples-are-built)).

## Shot list
| Time | Frames | Template (Data Viz) | The one point |
|---|---|---|---|
| 0:00 | 0–89 | Line chart - draw | revenue trend: up to 84% |
| 0:03 | 90–179 | Comparison bars | before vs after: 2.8x |
| 0:06 | 180–269 | Donut - fill | share of goal: 92% |
| 0:08.5 | 255–284 | Dip to colour (Transitions) | section change; cut at f270 |
| 0:09 | 270–359 | Ranked bars | which team led |
| 0:12 | 360–449 | Progress rings | three health metrics |
| 0:15 | 450–569 | Data table | the detail, one row highlighted |
| 0:19 | 570–644 | Gauge | the overall score: 72 |

## Timing logic
- 3 s per chart, 4 s for the table (more to read), 2.5 s for the closing gauge.
- Every chart lands its value after its shape (the pack rule: values 18 f after spring bars).
- One dip marks the change from "how we did" to "who and where".

## Measured on the master
- Lint 0 / 0 / 0; every template applied at 1920 × 1080.
- `qc` (240 px) notes f0–89 as a freeze: the 6 px line drawing does not register at that size (the pack doc says the same); the look shows it drawing. It also notes the ranked-bars hold (f295–359) and the table hold (f478–569).

## Adapt it
1. Change the values inside each chart's comp (bar heights, ring trims, table cells; see each template doc).
2. Keep one highlight colour per chart and grey the rest.

Inspiration: quarterly business review decks turned into motion. No external text or code was used.
