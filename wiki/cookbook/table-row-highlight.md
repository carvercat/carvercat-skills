---
id: cookbook/table-row-highlight
title: Highlight table rows one at a time
section: cookbook
tags: [table, row highlight, data table, comparison, spreadsheet, band, contrast, columns]
styles: [saas-ui, data-viz, corporate-brand, explainer]
topics: [data, text, timing]
related: [cookbook/list-highlight-bar, cookbook/lyric-line-sync, design/contrast, genres/data-stories, sound-and-timing/reading-time]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/table-design/]
---

# Highlight table rows one at a time

**Goal.** A table of five rows where an amber band steps down the rows and the text of the active row turns dark,
so every highlighted cell stays readable.

## Steps

1. Header at y 260, rule under it, then rows on a **90 px pitch** from y 360 (rows at 360, 450, 540, 630,
   720). Three columns (left edges 380, 960, 1500). Row texts 44 px, white, first column SemiBold.
2. **Band**: an amber rectangle 1260 × 80 (`borderRadius` 14) under the text. Hold each row for 30 f; between rows slide
   the band 6 f with S-curve, landing on frame 30 *r* (keys at 30 *r* − 6 and 30 *r*).
3. **Text colour**: every cell gets a `hold` colour key to dark ink (18, 18, 18) and another back to white. Put
   the flips **3 f before** the band lands and leaves, in the middle of the 6 f slide: dark at 30 *r* − 3, white
   at 30 (*r* + 1) − 3.
4. Use the same row pitch as the band for the text centres, so the band is centred on the row.

Compare [list highlight bar](list-highlight-bar.md), which moves one bar over a list; this page adds columns and
the colour hand-over.

## Measured in Carvercat 0.1.6

Comp `K Table` (180 f) in [cookbook lab 9](../labs/README.md#cookbook-lab-9carverproj); `inspect probe` on the band and
rendered pixels on the cell "500 GB" (row 3):

| Frame | 24 | 25 | 27 | 29 | 30 | 60 | 120 |
|---|---|---|---|---|---|---|---|
| Band centre y | 360.0 | 366.7 | 405.0 | 443.3 | 450.0 | 540.0 | 720.0 |

- The band lands exactly on the rows (360, 450, 540, 630, 720) on the frame the key says.
- The cell's text is ink (18, 18, 18) from **f57** to **f86** and white (242, 242, 240) before and after: the flip
  happens on the frame set (f57 and f87), as a `hold` key should.
- Contrast from the measured pixels: ink on amber **9.86:1**; white on amber would be **1.70:1**. In a first build the
  flips sat on the landing frame (f60), which left white text over the amber band on f57–f59.
- `inspect lint contrast:true`: 0 errors, 0 warnings, 6 notes (`repeated_key_value`, `speed_jump` on the band).

## Traps

- Flip colours in the **middle** of the slide: the band is an eased move, so on the landing frame the band has
  been under the text for several frames.
- 15 cells with two `hold` keys each is 30 keys; script it or write them in the project file.
- A band of 80 px on a 90 px pitch leaves a 10 px gap above and below it; keep the text centres on the pitch.

## In Carvercat

- Curve names on this page (S-curve) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Data table`, `Standings table`, `Attribute row`, `Highlight`.
- Background: [list highlight bar](list-highlight-bar.md), [contrast](../design/contrast.md),
  [data stories](../genres/data-stories.md).
