# Motion blur

**Verified 0.0.72:** `effect.add {cap:"motionblur"}` on a square sliding 576 px in 8 f (Ease out) renders a clear directional smear on the fast frames and none once it settles. It follows the object's OWN transform motion (position, scale, rotation) — not optical flow, not parent/camera motion of other layers.

| param | range | default | meaning |
|---|---|---|---|
| shutter | 0–360 | 180 | shutter angle in degrees: 180 = half a frame of travel (film look); 0 = none; 270–360 = heavy, stylised |
| samples | 2–64 | 16 | sub-frames averaged (Fusion "Quality"); 16 is fine; raise to 32 if you see stepping on very fast moves |

## When
- Any element covering more than ~1/20 of the frame width per frame (≈100 px/f at 1080p): whips, pushes, zoom-throughs, fast slides.
- Not on slow drifts (invisible cost) and not on text that must be read mid-move.
- Transitions: put it on the moving layers (wipe bars, pushed scenes) — the transitions guide assumes it.

## Pitfalls
- It only sees the object's own keys: a child moved by its parent, or content inside a moving nested comp, may not blur — add motion blur on the moving object itself (the parent/instance).
- With a preset that uses many baked keys (linear joins) the blur follows each segment — fine at 16 samples.
