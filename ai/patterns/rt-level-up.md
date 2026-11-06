# Pixel level up

**Template** `rt_level_up` (Library name "Pixel level up") · Retro pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `RT Level up` in `categories/retro/rt-lab-3`.

For briefs like "level up", "achievement unlocked", "new rank" on a game stream, an 8-bit look. A pixel star (9 × 9 grid of 26 px squares) draws in row by row, LEVEL UP! pops on twos with a hard pink shadow while eight pixel sparks fly out, an XP bar fills one block at a time, LV 11 turns into LV 12 and +500 XP rises. 120 f, overlay (drawn on night blue, which is dropped).

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Pixel r-c (52 squares, orange outline, yellow fill) | row × 2 | each row appears on its frame (cut) | drawn by **f16** |
| Level up (ExtraBold 150 px, yellow, pink hard shadow 10 px) | 12 | Pop - on twos as keys | **3.9%**, **f24** |
| Spark 1–8 (18 px squares) | 14 | fly out 230–330 px on twos, half opacity at f34; clips end at f42 | gone **f42** |
| XP frame (900 × 56 px), XP label, Level old "LV 11" | 20 | fade in on twos | **f24** |
| XP block 1–10 | 26–44 | one block every 2 f (cuts) | full **f44** |
| Level new "LV 12" (replaces LV 11 at f50) | 50 | scale 1.5 → 1 on twos | **f56** |
| XP gain "+500 XP" (ExtraBold 56 px, pink) | 52 | Rise - on twos | **f62** |

Lint 0 errors, 0 warnings in the lab (10 notes, `speed_jump` on the stepped sparks and rise); placed 0/0/0. `inspect qc`: no flashes. Text-gap audit: closest pair 46 px (XP label and the first block). Full-frame look of the placed instance at f30 (sparks at their widest): nothing cut.

## Steps
1. Change the sprite by editing `SPRITE` (`#` outline, `o` fill) in `retro_lab3.py`.
2. Change the numbers; LV 11 needs 25 opaque frames before it is replaced.

## Pitfalls
- 70+ small clips: fine for one instance, but place it once per comp, not on every beat.
- Pixel art needs whole-pixel squares: draw at 1920 × 1080 and do not scale the instance by odd factors, or the grid smears.

Inspiration: 8- and 16-bit game level-up screens. No external text or code was used.
