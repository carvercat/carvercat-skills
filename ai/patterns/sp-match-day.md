# Match-day poster

**Template** `sp_match_day` (Library name "Match-day poster") · Sports pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SP Match day` in `categories/sports/sp-lab-3`.

For briefs like "match day", "fixture promo", "kick-off tonight". Red and blue slanted bands slash in from opposite corners, MATCH DAY slams, two crests pop in either side of a VS and a yellow info bar slashes in with the date, time and venue. 120 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Band red (lower left), Band blue (upper right) | 0 | slash in from opposite corners (±768 px, ±324 px), hard expo, 12 f | settles **f8** |
| MATCH DAY (170 px white) | 6 | Impact slam | opacity **f8**, scale settles **f13**, **6.7%** past the impact |
| Underline (560 × 12 px yellow) | 14 | scale X 0 → 1 from the centre, 10 f | |
| Crest 1 (red shield) and 2 (blue), letters, team names (60 px white) | 20 / 26 | scale 0 → 100% with overshoot (12 f); letters 6 f later; names slide in | crest 1 settles **f31**, **9.8% overshoot** |
| VS (90 px yellow) | 36 | Impact slam | |
| Info bar (yellow, 1160 px slanted) + text (38 px dark) | 46 / 50 | Slash in | bar opacity **f48**, position **f53** |

Lint (with `contrast:true`) 0 errors, 0 warnings, 0 notes. `inspect qc` (240 px): no flashes; the hold from f58 reads as a freeze. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 21 pairs, closest 102.6 px (team name / info line). Full-frame looks of the placed comp at f14 and f119: nothing cut; the bands run off the frame edge on purpose and finish before the text.

## Steps
1. Edit the teams, colours and info line in `match_day()`; replace the two shield paths with the clubs' crests (keep their 190 × 230 px footprint).
2. Longer info line: widen the bar (`iw`); the line measures 1000 px at 38 px with tracking 1.15.

## Pitfalls
- **The info bar was too narrow:** sized from `textw` (about 640 px) it cut "SU" and "IUM" off, because the dark text left the yellow bar and vanished on the dark ground. Tracked caps measured 1000 px; lint reported nothing ([KI-157](../references/known-issues.md#ki-157)).
- Keep the bands inside the frame edges and away from the title; a slanted shape cropped at rest is fine only when it is a deliberate bleed.

Inspiration: common broadcast sports graphics conventions. No external text or code was used. Teams, players and leagues are invented.
