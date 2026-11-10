# Quarterly results, 9:16, 17.5 s

The vertical version of [quarterly-results](quarterly-results.md). **Verified 0.1.6 (rev 1105), 2026-10-28; builder and measures re-run on Carvercat 0.1.8, 2026-11-04** Sample: `categories/recipes/quarterly-results-9x16` (525 f, 1080 × 1920). Builder: `ai/scripts/motion/recipes/rc_dataviz_9x16.py` (the master is a `carvercat/2` file or one `scene.apply`: [how](README.md#how-the-samples-are-built)). Method and traps: [vertical-recuts.md](vertical-recuts.md).

| Time | Frames | Template | Zoom | Job |
|---|---|---|---|---|
| 0:00 | 0–89 | Comparison bars | 1.5 + 3% push | before / after |
| 0:03 | 90–179 | Donut - fill | 2.2 + push | share of goal |
| 0:06 | 180–269 | Progress rings | 1.45 + push | three metrics |
| 0:09 | 270–359 | Waffle chart | 1.45 + push | one share |
| 0:12 | 360–434 | Gauge | 2.4 + push | the score |
| 0:14.1 | 423–446 | Swipe up (9:16) | — | cut at f435 |
| 0:14.5 | 435–524 | Follow end card (9:16) | — | follow |

Dropped: the line chart, ranked bars and data table (wide layouts). Measured: lint 0 / 0 / 0; `qc` notes only the ring hold (f203–269) and the end card hold (f458–524) as freezes. The first build zoomed the comparison bars to 2.0 and the rings to 1.6: the delta badge and a ring were cut by the frame edge while lint stayed 0 / 0 / 0; the look caught it. The rings' labels land at about 24 px: readable, under the 28 px guideline.

Speed streak (0.1.10): the Swipe up transition carries a vertical `directionalBlur` (240 px at 90deg while the panel travels, 0 while it covers; [directional blur](../references/effects/directional-blur.md)); exact in Resolve, approximate in After Effects.
