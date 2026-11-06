# Straight ahead and pose to pose

**What it does:** pose to pose plans the key poses first and lets the in-betweens follow; straight ahead draws every frame in order. Motion graphics is mostly pose to pose; stepped, hand-drawn looks come from straight-ahead thinking.

## How in Carvercat
- **Pose to pose** is keyframing: set the start, end and settle poses, then shape the in-betweens with easing (`linear`, `ease-in`, `ease-out`, `ease-in-out`, `hold`, or a `cubic-bezier(...)` on the key that leaves).
- **Straight ahead** is a key on every (or every other) frame with **`hold`** easing, so the value jumps instead of interpolating:
  - "On twos" (12 drawings a second): a new pose every 2 f ([retro.md](../../../patterns/retro.md), `twos()` in `retro_lab.py`).
  - Glitch: held jumps on irregular frames ([glitch.md](../../../patterns/glitch.md)).
  - Digital meters: a new level every 12 f ([fh-signal-bars.md](../../../patterns/fh-signal-bars.md)).
- Springs and bounces are baked to keys with linear joins (`curves.py` → `lane_keys`/`bake`), because preset easings are limited to the named ones.

## Measured examples
| Template | Method | Numbers |
|---|---|---|
| Card lift ([su-card-lift](../../../patterns/saas-ui.md)) | 2 poses, expo | settles **f12** of 18 |
| Pop - on twos ([retro.md](../../../patterns/retro.md)) | stepped every 2 f | 3.9% overshoot, settles **f12** |
| Glitch in ([glitch.md](../../../patterns/glitch.md)) | Hold jumps +3, −2, +1.2, −0.6, +0.3% W (stored value) | locked by **f10** |
| Segment loader ([fh-loader.md](../../../patterns/fh-loader.md)) | Hold opacity, one segment per 9 f | full at f92 |

## Traps
- Hold keys at least 4 f apart for blinks (lint `same_frame_keys`).
- `curves` reports the first held jump as "overshoot"; read the keys, not the number.
