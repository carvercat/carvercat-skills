# Bar chart race

**Template** `dv_bar_race` (Library name "Bar chart race") · Data Viz pack · **Verified 0.1.8.4 (rev 1130)**, comp `DV Bar race` in `categories/data-viz/dv-lab-3`.

For briefs like "how the ranking changed over the years", "leaderboard over time". Five bike-share stations (sample data) on a fixed 0–600 scale re-rank three times, 2022 → 2025; the subject (Riverside) is cyan and climbs from 4th to 1st. A big year label steps with each transition. 220 f, holds 36 f on the final ranking.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Bars (72 px tall, anchor at the left edge) | 4 + 3 per 2022 rank | width 0 → value, 16 f, expo | builds f4–32, **0% easing overshoot** |
| Re-ranks | f60–80, f112–132, f164–184 | width (scale X) and row (position Y) together, smooth (S curve cubic-bezier(0.333, 0, 0.667, 1)) | last moves settle **f182** |
| Names (32 px, right-aligned) | 0 | ride with their bar; a name that crosses another hides (opacity 1 → 0 in 4 f) and returns in the last 6 f | Name Harbor back **f134** |
| Values (30 px), one text per year | on each hold | in 6 f at the end of a re-rank, out 4 f at the start of the next | each held 28–32 opaque frames |
| Year (Bold 120 px, muted) | one text per year | out 6 f at a re-rank start, the next in 6 f later | never two on screen; 2025 opaque **f176** |

Lint 0 errors, 0 warnings (83 notes: held key values between re-ranks). Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (closest 19.5 px). Full-frame looks of the placed instance at f66, 70, 74, 118, 122, 172 and 176: the bars move inside the frame, nothing is cut.

## Steps
1. New data: edit `RACE`, `RACE_YEARS` and the scale (`1000 / 600` px per unit) in `race()` in `ai/scripts/motion/data_viz_lab3.py`; ranks, crossings and label positions are computed. More years: add a (start, end) pair to `T`, 52 f apart.
2. Keep holds at 28 f or more of opaque values: lint's reading time asks 25 frames for a 3-digit value.

## Pitfalls
- **Lint checks `text_overlap` while texts move, at any opacity above 0.** Names dimmed to 0.5, 0.3 and even 0.15 while crossing still raised four warnings; only 0 cleared them. So crossing names hide for the middle of the move.
- The scale is fixed for the whole race. Rescaling the axis between years makes growth look like decline.
- `inspect curves` reports 8.4% "overshoot" on Midtown's width: its value goes 520 → 540 → 498, so the first year is above the last. It is data, not easing.
- A value text's keys must stay inside its clip (lint error `key_outside_clip`), so each year's value ends its clip as it fades out instead of riding to the next row.

Inspiration: animated bar chart races in data journalism. No external text or code was used.
