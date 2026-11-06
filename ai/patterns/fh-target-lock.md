# Target lock

**Template** `fh_target_lock` · Futuristic HUD pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FH Target lock` in `categories/futuristic-hud/fh-lab-2`.

Four corner brackets close in on an amber target at (1180, 470), then a leader line and the LOCKED label. 90 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Lock corner 1–4 | 0 | from 320 px out, turning 90° → 0, 24 f, expo; opacity in 4 f | settle **f15** |
| Target | 0 | Flicker on | |
| Lock leader | 26 | Trim end 0 → 1, f26–38 | |
| Lock text, Lock data | 34, 40 | Flicker on | LOCKED on by **f44** |

Lint 0 errors, 0 warnings; `inspect qc` (240 px) found no flashes. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Move the whole instance so the target sits on the subject; for a moving subject key the instance's position.

Inspiration: target-acquisition overlays. No external text or code was used.
