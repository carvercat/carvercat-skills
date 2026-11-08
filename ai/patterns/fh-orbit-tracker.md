# Orbit tracker

**Template** `fh_orbit_tracker` (Library name "Orbit tracker") · Futuristic HUD pack · **verified 0.1.8.1 (rev 1127 build; headless, isolated folders, pack added to a scratch user Library; `ai/scripts/motion/verify_pack.py`)**, comp `FH Orbit tracker` in `categories/futuristic-hud/fh-lab-3`.

For briefs like "satellite launch", "space mission", "GPS / telecom coverage", "mission control". A wireframe planet turns (faux 3D meridians), a tilted dashed orbit passes in front of it, a satellite with two trail dots runs one way along the orbit and hides behind the planet, the ground station pings as it passes and SIGNAL ACQUIRED flickers in. 150 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Orbit (back, dashed 760 × 240 px, turned 16°) | 0 | Trim end draws f4–28; sits under the planet, so the planet's fill hides its far half | |
| Planet (420 px, #08121A fill, cyan stroke) | 0 | scan open, 12 f | scale settles **f8** |
| Latitude 1–3 | 8 | flattened ellipses draw f8–26 | |
| Meridian 1–3 | 8 | width = 2R·\|sin φ\| (scale x), φ turning 180° in 150 f (the pattern repeats, so the turn loops), baked every 2 f | |
| Orbit front | 0 | the same ellipse trimmed to its near half (start 0.5, end 0.5 → 1, f4–28), above the planet | |
| Station (amber diamond), Station ping 1–2 | 12 / 24, 38 | Flicker on; rings grow 0.3 → 3× as the satellite passes nearest | |
| Satellite, Satellite trail 1–2 | 0 | position baked every 2 f along the orbit (0.95 of a turn, counter-clockwise from the near left); opacity Hold 0 while the dot is on the far half and inside the planet's disc; on from f20 | opacity last changes **f122** |
| Sat name, Altitude / Velocity / Inclination | 6 / 12, 18, 24 | flicker on; values type on | |
| Signal "SIGNAL ACQUIRED" (green 34 px) | 30 | Flicker on | on **f40** |

Lint (with `contrast:true`) 0 errors, 0 warnings, 0 notes. `inspect curves` reports 216% "overshoot" on a meridian's scale and 953% on the satellite's position: baked multi-move lanes ([KI-152](../references/known-issues.md#ki-152)); each segment is Linear between computed points. `inspect qc` (240 px): no flashes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 36 pairs, closest 22.2 px. Full-frame looks of the placed comp at f20 and f60: nothing cut.

## Steps
1. Change the orbit in `orbit()`: `oa`, `ob`, `tilt`; the satellite start `u0` and travel `du`. Positions, the hidden stretch and the acquisition frame are recomputed.
2. Move the station with `gx, gy` (keep it on the planet's near side).

## Pitfalls
- An ellipse's stroke starts at 3 o'clock and runs counter-clockwise, so its near (lower) half is Trim 0.5–1; the same holds after a rotation, because trim works in the shape's own frame.
- Hide a dot "behind" a shape with Hold opacity keys at the computed crossing frames; a dot cannot change layers mid-clip.
- The readout column at 1200 px ran SIGNAL ACQUIRED to x 1844, past the graphics-safe edge (1824); the column now starts at 1150.

Inspiration: common sci-fi HUD and interface conventions. No external text or code was used.
