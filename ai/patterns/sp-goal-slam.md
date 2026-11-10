# GOAL slam

**Template** `sp_goal_slam` · Sports pack · **Verified 0.1.8.1 (rev 1127)**, comp `SP Goal slam`.

**Re-checked with the new effects on Carvercat 0.1.10, 2026-11-10 (headless, isolated folders, `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0; silhouette against the v1 original passes, objects pass; visible f1-59.

Ten white and yellow speed lines radiating from the centre (8 px, kept inside the frame), a red slanted band (closed path), and "GOAL!" (ExtraBold 260 px, yellow, dark outline outside the glyphs).

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Speed lines | 0–8 draw, 6–18 clear | trimEnd 0% → 100% (expo), then trimStart 0% → 100% (accelerating arrival cubic-bezier(0.333, 0, 0.667, 0.333)) | |
| Band | 0–10 | **Slash in** | settles **f7** |
| Band streak | 0–10 | `directionalBlur` 200 px → 0 at 17.1deg (the slash's own diagonal, atan(12 % H / 22 % W)), linear ([directional blur](../references/effects/directional-blur.md)) | |
| GOAL! | from 4 | **Impact slam**: impact at f9 | 6.7%, settles **f12** |

Lint 0/0; qc found no flashes. Put a crowd roar and a hit on f9. As an overlay over footage, delete nothing: the template has no background.
