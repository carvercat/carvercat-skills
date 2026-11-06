# Signing announcement

**Template** `sp_signing` (Library name "Signing announcement") · Sports pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SP Signing` in `categories/sports/sp-lab-3`.

For briefs like "new signing", "transfer announcement", "welcome to the club". A red slanted photo panel with a player stand-in slashes in; the name, position, FROM club, a drawing arrow and TO club follow, a yellow contract bar grows and a SIGNED stamp slams onto the chest. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Photo panel (x 120–800) | 0 | Slash in | opacity **f2**, position **f7** |
| Player stand-in (head, shoulders in dark red) | 6 | fade, 6 f | |
| Kicker NEW SIGNING (40 px yellow), Player name (104 px white), Position (36 px #B4BCD0) | 8 / 12 / 16 | Slash in | name settles **f19** |
| Divider (4 px) | 20 | trimEnd 0% → 100%, 14 f | |
| FROM / club, arrow (draws, f34–44) and head, TO / club | 26 / 28 / 34 / 40 / 42 | labels fade; clubs slash in | |
| Contract bar (yellow, 642 px) + text (34 px dark) | 48 / 54 | bar grows from its left edge, 10 f; text fades | bar settles **f55** |
| Stamp plate (dark, 540 × 140, yellow 9 px stroke) + SIGNED (92 px yellow), both turned 8° (stored value) | 64 | slam from 150% to 92% (impact f69), back to 100% | opacity **f66**, scale settles **f72**; 16% past 100% |

Lint (with `contrast:true`) 0 errors, 0 warnings, 0 notes. `inspect qc` (240 px): no flashes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 45 pairs, closest 24.6 px (TO label / TO club). Full-frame looks of the placed comp at f66 (stamp mid-slam) and f149: nothing cut; the stamp stays inside its plate.

## Steps
1. Replace the player stand-in with the cut-out photo under the stamp; keep the photo panel as the background.
2. Change the name, clubs and years in `signing()`. The contract bar width is set for "CONTRACT UNTIL 2030" (562 px of text); change `cw` with a longer line.

## Pitfalls
- **Tracked caps are far wider than `textw` says.** The contract line measures 562 px at 34 px with tracking 1.2; a bar sized from `textw` hid "2030" (dark text running off the bar onto the dark ground). Lint does not check text against its panel ([KI-157](../references/known-issues.md#ki-157)). Measure with `carvercat_authoring geometry`.
- The stamp slammed from 220% overlapped FROM club in lint (`text_overlap` 19%); from 150% it stays clear of the text column.
- Yellow on the red photo panel is 2.9:1; the stamp sits on a dark plate so it reads wherever it lands.

Inspiration: common broadcast sports graphics conventions. No external text or code was used. Teams, players and leagues are invented.
