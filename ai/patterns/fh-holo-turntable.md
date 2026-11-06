# Holo turntable (faux 3D)

**Template** `fh_holo_turntable` (Library name "Holo turntable (faux 3D)") · Futuristic HUD pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FH Holo turntable` in `categories/futuristic-hud/fh-lab-3`.

For briefs like "product reveal in a sci-fi style", "hologram", "360° view", "CAD / engineering". A wireframe box turns a full turn above a projector base in faux 3D, with perspective and depth brightness; a scan arc runs round the base, a scan line passes down the model and a callout lists its data. 150 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Base ring 1–2 | 0 / 3 | scan open (flattened ellipses 460 × 96, 340 × 70) | |
| Light cone (trapezoid path) | 8 | opacity 0 → 8%, f8–20 | |
| Base scan (5 px arc) | 6 | Trim end 0 → 22% (expo, f6–16); Trim offset 0 → 1.5, Linear, f6–150 (the arc runs round the base, one way) | end settles **f13** |
| Edge 1–12 (3 px rectangles) | 0 | one full turn in 150 f (from 25°), tilt 20°, focal 1700 px: each edge's position (midpoint), rotation (its angle, unwrapped by 180°), length (scale x) and opacity (depth: far 35%, near 100%) baked every 2 f, Linear; edges switch on f10–24 | 76 keys a lane; the turn loops at f150 |
| Corner 1–8 (12 px dots) | 0 | position and depth opacity baked every 2 f; on from f24 | |
| Model scan | 30 | y −250 → +250 px over the model, S curve cubic-bezier(0.333, 0, 0.667, 1), f30–84; fades out by f88 | position settles **f81** |
| Callout leader, Model name, Scan / Dims / Mass | 20–54 | leader draws f20–34; name flickers on f26; label + typed value pairs at f34, f42, f50 | name on **f36** |

Lint (with `contrast:true`) 0 errors, 0 warnings, 45 notes (`repeated_key_value`: each edge and corner holds 0% before it switches on; intended). `inspect curves` reports 46–49% "overshoot" on the baked opacity lanes: it measures many moves against the last key ([KI-152](../references/known-issues.md#ki-152)); every segment is Linear between computed values. `inspect qc` (240 px): no flashes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 21 pairs, closest 28 px. Full-frame looks of the placed comp at f60 and f110 (widest views of the box): nothing cut, the box stays clear of the callout.

## Steps
1. Change the box in `turntable()`: half width `a`, half height `h`, half depth `c`; tilt `el`, `focal`, the start angle and turn per clip in `theta()`. Regenerate: the edges are recomputed.
2. For another product shape, list its vertices and edges; every edge is a thin rectangle keyed the same way.

## Pitfalls
- A line segment has no direction: unwrap its angle by 180°, not 360°, or an edge flips half a turn between two keys.
- Scale only the length (x) of an edge rectangle; its 3 px thickness stays.
- Depth brightness sells the 3D more than perspective does: without it the box reads as a flat, flipping shape.

Inspiration: common sci-fi HUD and interface conventions. No external text or code was used.
