# Segment loader

**Template** `fh_loader` (Library name "Segment loader") · Futuristic HUD pack · **verified 0.1.8.1 (rev 1127 build; headless, isolated folders, pack added to a scratch user Library; `ai/scripts/motion/verify_pack.py`)**, comp `FH Loader` in `categories/futuristic-hud/fh-lab-2`.

Ten 70 × 40 px outlined slots that fill one by one with glowing cyan segments, a label, percentages and an amber COMPLETE. 130 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Loader label | 0 | Flicker on | |
| Slot 1–10 | 0 | none (2 px dim outline) | |
| Segment 1–10 | 10, 19 … 91 | opacity Hold 0 → 1: snaps on | Segment 10 on at **f92** |
| Percent "30%", "60%", "100%" | 28, 55, 91 | cut on with the 3rd, 6th and 10th segment | each held 27–39 f |
| Done ("COMPLETE") | 91 | Flicker on | fully on by **f101** |

Lint 0 errors, 0 warnings; `inspect qc` (240 px) found no flashes. Placed into a fresh comp: lint 0/0/0.

## Pitfalls
- Text content cannot be keyed ([KI-051](../references/known-issues.md#ki-051)), so each percentage is its own clip, and each must stay at least 25 f (lint `reading_time`). With COMPLETE at f92 of a 120 f comp, lint measured only 22 readable frames (Flicker on takes 10); the comp is 130 f.

Inspiration: segmented progress bars in game and sci-fi UIs. No external text or code was used.
