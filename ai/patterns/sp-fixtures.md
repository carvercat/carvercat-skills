# Fixture list

**Template** `sp_fixtures` (Library name "Fixture list") · Sports pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SP Fixtures` in `categories/sports/sp-lab-3`.

For briefs like "fixtures", "this weekend's matches", "kick-off times". Five fixture panels slash in 5 f apart, each with the day and time, both teams, a VS chip and team-colour ticks; LIVE tags slam onto the televised games. 150 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Title FIXTURES (64 px white), MATCHWEEK 31 (28 px #B4BCD0) | 0 / 6 | Slash in; fade | |
| Fixture panels 1–5 (1400 × 88 px, slanted) | 8 + 5 per row | Slash in | panel 1 opacity **f10**, position **f15** |
| When (32 px yellow), Home (44 px white, right-aligned at x 870), Away (left-aligned at x 1050) | panel + 2 / 3 / 5 | Slash in | |
| VS chip (72 px disc) + VS (28 px) | panel + 4 | Impact slam | chip opacity **f14**, scale settles **f19** |
| Team-colour ticks (12 × 44 px red, blue) | panel + 6 | fade; placed from the measured name width | |
| LIVE tags 1 and 4 (white plate, dark 28 px text) | 64, 74 | Impact slam | tag 1 opacity **f66**, scale settles **f71** |

Lint (with `contrast:true`) 0 errors, 0 warnings, 0 notes. `inspect qc` (240 px): no flashes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 444 pairs; the only flags are each VS text sitting on its own chip (−46 px, intended). Full-frame looks of the placed comp at f20 (rows still sliding) and f149: nothing cut.

## Steps
1. Edit `rows` in `fixtures()`: (time, home, away, televised). Team names to about 9 characters at 44 px.
2. More than five rows: reduce the 120 px step and the panel height; keep 40 px between panels.

## Pitfalls
- Home and away are aligned to a centre gap, so the VS chip never moves with a long name; the colour ticks use the measured name width (`textw` is fine without tracking).
- A slam on the VS chip overlaps its neighbours at 220%; the chip is a disc with the label inside it and the names stay clear of x 900–1020.

Inspiration: common broadcast sports graphics conventions. No external text or code was used. Teams, players and leagues are invented.
