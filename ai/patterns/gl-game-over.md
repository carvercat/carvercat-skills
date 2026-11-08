# Game over screen

**Template** `gl_game_over` (Library name "Game over screen") · Glitch pack · **verified 0.1.8.1 (rev 1127 build; headless, isolated folders, pack added to a scratch user Library; `ai/scripts/motion/verify_pack.py`)**, comp `GL Game over` in `categories/glitch/gl-lab-3`.

For briefs like "game over", "you died / continue?", "stream fail moment". GAME OVER (red ExtraBold 200) lands with the stretch hit and a cyan offset, score and hi-score lines, then CONTINUE? with a 3-2-1 count. 150 f. (The Retro pack's arcade start screen is the attract screen; this is the losing one.)

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Game over | 0 | Glitch stretch hit as Hold keys; jumps −36, +22, −8, 0 px; one cyan hard shadow +30 → −19 → +12 → +8 px | size **f6** (25.0%); position **f9**; shadow rests at 8 px |
| Score / Hi score (SemiBold 48, tracked) | 14 / 18 | opacity Hold steps | **f19 / f23** |
| Continue? (ExtraBold 72) / Coin line | 36 / 40 | opacity Hold steps | |
| Count 1–3 ("3", "2", "1", cyan 96) | 42, 74, 106 | each one 32 f clip; a jump +18, −8, 0 px on arrival | each steady 4 f after it starts |

Lint 0 errors, 0 warnings; `inspect qc` (240 px): **no flashes**. Placed into a fresh comp: lint 0/0/0, qc no flashes. Text-gap audit: closest pair score / hi score, 35.2 px. At f0 the stretched title is 1.6 × wide (about 1760 px); the full-frame look of the placed instance at f0 shows it inside the frame.

## Steps
1. Each count digit needs about 25 opaque frames for lint's reading time; keep 30 f or more per digit.

Inspiration: arcade and console game-over screens. No external text or code was used.
