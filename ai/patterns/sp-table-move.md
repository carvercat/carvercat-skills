# League table movement

**Template** `sp_table_move` (Library name "League table movement") · Sports pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SP Table move` in `categories/sports/sp-lab-3`.

For briefs like "league table", "climb the table", "promotion", "standings update". Six rows slash in; the red row wins (44 → 47), steps out to the right, climbs three places while the rows between drop one place, and a green +3 badge lands. 150 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Title (56 px white), MATCHWEEK 30, PTS head (26 px #B4BCD0) | 0 / 6 / 6 | Slash in; fade | |
| Rank boxes 1–6 (the rank column stays put) | 6 + 3 per row | Slash in | |
| Rows 1–6 (894 px slanted panel, team 40 px white, points 40 px yellow); row 5 is red with white points | 6 + 3 per row | Slash in | |
| Points 44 → 47 (separate clips, hand over on f48) | 20 → 48 | the old value shows 28 f; 47 slams in (220% → 100%) | 47 opacity **f50**, scale settles **f55** |
| Row 5 out, up three places, back | 56 / 66 / 86 / 96 | out +240 px right (expo, f56–66); up 252 px (smooth, f66–86); back in (expo, f86–96) | position settles **f92** |
| Rows 2–4 drop one place (84 px) | 66–86 | smooth, together with the climb | settle **f85** |
| Climb badge: green arrow + "+3" (34 px #3FD08A) | 98 / 100 | slam; fade | arrow opacity **f100**, scale settles **f105** |

`inspect curves` overshoot on the row positions (57% and 184%) is meaningless on multi-key moves; the path is the three segments above, with no overshoot.

Lint (with `contrast:true`) 0 errors, 0 warnings, 14 notes (11 `repeated_key_value`, 3 `speed_jump` where the row starts its move; intended). `inspect qc` (240 px): no flashes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 276 pairs, closest 13.0 px (+3 / its arrow; intended). Full-frame looks of the placed comp at f76 (the red row out at the right, between two rows) and f149: nothing cut or crossed; the end order is HAWKS, FALCONS, WOLVES, BEARS, SHARKS, TIGERS.

## Steps
1. Edit `rows` (team, points) and the mover index (`up = i == 4`, climb of 3 places) in `table_move()`.
2. A different climb: change `3 * step` and the rows that drop (`1 <= i <= 3`).

## Pitfalls
- The mover leaves the column first, so it never passes through another row's text; moved through the column it fails `text_overlap`.
- The points changed in a separate clip: the old one first showed only 14 f and failed `reading_time` (2 characters want 25 f). It shows 28 f now.
- Lint compares text boxes during a move, so the dropping rows move only while the mover is outside the column.

Inspiration: common broadcast sports graphics conventions. No external text or code was used. Teams, players and leagues are invented.
