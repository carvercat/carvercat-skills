# GOAL slam

**Template** `sp_goal_slam` · Sports pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SP Goal slam`.

Ten white and yellow speed lines radiating from the centre (8 px, kept inside the frame), a red slanted band (closed path), and "GOAL!" (ExtraBold 260 px, yellow, dark outline outside the glyphs).

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Speed lines | 0–8 draw, 6–18 clear | trimEnd 0% → 100% (expo), then trimStart 0% → 100% (accelerating arrival cubic-bezier(0.333, 0, 0.667, 0.333)) | |
| Band | 0–10 | **Slash in** | settles **f7** |
| GOAL! | from 4 | **Impact slam**: impact at f9 | 6.7%, settles **f12** |

Lint 0/0; qc found no flashes. Put a crowd roar and a hit on f9. As an overlay over footage, delete nothing: the template has no background.
