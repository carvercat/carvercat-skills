# VHS overlay

**Template** `rt_vhs_overlay` · Retro pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `RT VHS overlay` in `categories/retro/rt-lab-2`.

A camcorder playback overlay for footage: "PLAY" with a right-pointing triangle (top left), a red REC dot and label (top right), tape time "SP 0:04:27" and a date (bottom). White Bold 52–64 px. 120 f; stretch the clips for longer shots.

| Part | Motion |
|---|---|
| REC dot | opacity on Hold keys: on 15 f, off 15 f (once a second) |
| Everything else | still |

Lint 0 errors, 0 warnings; `inspect qc` (240 px) found no flashes. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place over your footage for the whole shot; edit the time and date.
2. Pair with the Glitch pack's noise bars for tape damage.

## Pitfalls
- A 3-gon at 0° points right, which is what the play arrow needs.
- Blinks are Hold keys 15 f apart, far from lint's `same_frame_keys` and the 3-flashes-a-second limit.

Inspiration: VHS camcorder viewfinder overlays. No external text or code was used.
