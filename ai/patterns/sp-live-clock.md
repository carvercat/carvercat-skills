# Live score clock

**Template** `sp_live_clock` (Library name "Live score clock") · Sports pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SP Live clock` in `categories/sports/sp-lab-3`.

For briefs like "live score bug with a timer", "match clock", "added time". A 64 px score bug (x 96–742, y 64–128) grows out of its left edge; the match clock steps one second every 30 f and a yellow +3 added-time tab drops out of the clock box at 45:00. 210 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| League, Team A, Score, Team B, Clock boxes | 0, 3, 6, 9, 12 | scale X 0 → 1 from the left edge, hard expo, 10 f | Team A box settles **f10** (about 7 f after its start) |
| NCL (30 px, dark on yellow), HAW / 1 - 0 / WOL (36 px white) | 6, 9, 12, 15 | fade in, 3 f | |
| Clock 1–6 "44:56" … "45:01" (34 px, dark on the white box) | 20, 50, 80, 110, 140, 170 | one clip per second, each handing over on a frame; 30 f on screen (the last 40 f) | Clock 1 opacity settles **f23** |
| Added time tab (yellow, 140 × 48 px, drawn under the clock box) | 140 | slides 48 px down out of the clock box, hard expo, f140–150 | settles **f147** |
| "+3" (30 px, dark on yellow) | 150 | fade in, 3 f | |

Lint (with `contrast:true`) 0 errors, 0 warnings, 0 notes. `inspect qc` (240 px): no flashes; two holds read as freezes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 55 pairs, closest 33.2 px (Clock 5 / Added time). Full-frame looks of the placed comp at f100, f145 (tab half out) and f209: nothing cut; the tab stays under the clock box and above the pitch.

## Steps
1. Change the teams, score and league in `live_clock()`; keep team codes to three letters at 36 px (the boxes are 128 px wide).
2. A different time: edit the `ticks` list (text, start, end). A clock that must run longer is more clips, 30 f each.
3. Put the comp over the match footage; the bug sits in the top-left safe area.

## Pitfalls
- **`text.content` cannot be keyed** ([KI-051](../references/known-issues.md#ki-051)), so the clock is six clips that hand over on one frame. Each is on screen 30 f, over the 25 f reading minimum.
- White on the red and blue boxes needs 36 px or more (large-text 3:1; white on #E63946 is about 4:1); yellow is never text on red (2.9:1).
- The tab is drawn before the clock box so it appears from behind it; at rest it shows only below the box. Look at f145, where it is half out.

Inspiration: common broadcast sports graphics conventions. No external text or code was used. Teams, players and leagues are invented.
