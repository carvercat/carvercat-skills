# Boot sequence

**Template** `fh_boot_sequence` (Library name "Boot sequence") · Futuristic HUD pack · **verified 0.1.8.1 (rev 1127 build; headless, isolated folders, pack added to a scratch user Library; `ai/scripts/motion/verify_pack.py`)**, comp `FH Boot sequence` in `categories/futuristic-hud/fh-lab-3`.

For briefs like "the product powers on", "game intro", "initialising", "app launch" in a tech style. Six log lines type on, each answered by a green [ OK ] at the end of a dotted leader, a progress bar steps with every OK, then the core mark draws on and SYSTEM ONLINE flickers in. 150 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Boot header (26 px, #4FA8BF) | 0 | Flicker on | |
| Line 1–6 ("> BIOS CHECK" ..., 38 px) | 8, 21, 34, 47, 60, 73 | type on, 1 f a character (stagger on opacity, Hold) | line 1 typing from **f9** |
| Leader 1–6 (dotted, 3 px) | line + 2 | Trim end 0 → 1, Linear, until its OK | |
| OK 1–6 ("[ OK ]", green #3FD08A) | 22, 37, 49, 63, 70, 90 | Flicker on (line start + characters + 4 f) | OK 6 on **f100** |
| Progress frame / Progress fill | 4 | frame scans open; the fill steps 1/6 wider with each OK (Hold keys, anchored left) | fill full at **f90** |
| Core mark (hexagon, rotated 90°) | 84 | Trim end 0 → 1 (expo), 18 f | settles **f96** |
| Core ring | 86 | trims to 30% (expo, 14 f) and turns 120° one way to the end | |
| Core dot | 96 | Flicker on | |
| Online "SYSTEM ONLINE" (44 px cyan) | 100 | Flicker on | on **f110** |

Lint (with `contrast:true`) 0 errors, 0 warnings, 1 note (`speed_jump` on the stepped fill; intended). `inspect qc` (240 px): no flashes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 105 pairs, closest 28.5 px (OK 6 / Online). Full-frame look of the placed comp at f149: nothing cut.

## Steps
1. Edit `lines` in `boot()`; the OK frames, leaders and progress steps are computed from the line lengths.
2. Replace the core mark with the product's mark (keep it drawn on with Trim).

## Pitfalls
- The leader starts at the measured width of the typed line (`textw` × 1.1 for the tracking); with a different font size, check the first dot does not touch the last letter.
- SYSTEM ONLINE at 48 px with tracking 1.4 first ran past x 1800; at 44 px / 1.3 it ends at 1772.

Inspiration: common sci-fi HUD and interface conventions. No external text or code was used.
