# Tournament bracket

**Template** `sp_bracket` (Library name "Tournament bracket") · Sports pack · **Verified 0.1.8.1 (rev 1127)**, comp `SP Bracket` in `categories/sports/sp-lab-3`.

For briefs like "bracket", "knockout stage", "cup draw", "playoffs". Eight quarter-final slots slash in, join lines draw to the semi-finals, then the final, and the CHAMPION panel slams in. 180 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Round headers (26 px #B4BCD0) | 0 / 56 / 100 / 140 | fade, 3 f | |
| QF slots 1–8 (320 × 56 px slanted panel, team 30 px white, score 30 px yellow) | 4 + 3 per slot | Slash in; scores fade in at 30, 32, 34, 36 | QF 1 settles **f11** |
| QF join lines + feed lines (4 px) | 42 / 50 | trimEnd 0% → 100%, 12 f (feed 6 f) | QF join 1 settles **f50** |
| SF slots 1–4, joins | 58 + 3 per slot; 88 | the same; scores at 78, 80 | |
| Final slots 1–2, joins | 102, 105; 128 | the same; scores at 120 | |
| Winner edge (8 × 44 px yellow bar) | with each score | scale Y 0 → 1 from the top, 8 f | |
| CHAMPION panel (340 px yellow) + HAWKS (56 px dark) | 140 | Impact slam | opacity **f142**, scale settles **f147**, **6.7%** past the impact |
| CUP 2026 (30 px #B4BCD0) | 152 | fade | |

Lint (with `contrast:true`) 0 errors, 0 warnings, 0 notes. `inspect qc` (240 px): no flashes. Placed into a fresh comp: lint 0/0/0 (70 objects). Text-gap audit: 1173 pairs, closest 14.0 px (QF 8 team / its winner edge bar; intended). Full-frame looks of the placed comp at f60, f144 and f179: nothing cut; the CHAMPION panel ends at x 1800.

## Steps
1. Edit the `qf`, `sf` and `fi` lists in `bracket()` (team, score). The winner edge is computed from the scores; keep the winners consistent between rounds.
2. For 4 teams drop the quarter-final column; for 16 add a column and shift the x positions.

## Pitfalls
- The join and feed lines are open paths drawn with trim end; slots must be on the same frames as their joins or a line points at an empty slot.
- Rounds draw left to right, one per beat; a round whose slots arrive before the previous round's scores reads as a guess.

Inspiration: common broadcast sports graphics conventions. No external text or code was used. Teams, players and leagues are invented.
