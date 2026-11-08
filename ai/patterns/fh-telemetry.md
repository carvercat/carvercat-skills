# Drone telemetry

**Template** `fh_telemetry` (Library name "Drone telemetry") · Futuristic HUD pack · **verified 0.1.8.1 (rev 1127 build; headless, isolated folders, pack added to a scratch user Library; `ai/scripts/motion/verify_pack.py`)**, comp `FH Telemetry` in `categories/futuristic-hud/fh-lab-3`.

For briefs like "drone footage overlay", "FPV", "vehicle or flight telemetry", "aerospace". A full-frame overlay to put over footage: frame corners, an artificial horizon that banks through a turn and settles level, a heading dial, stepped speed and altitude, and status corners. 150 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Frame corner 1–4 | 0 | static (1680 × 900 px frame) | |
| Horizon (660 px line; the rig pivot) | 0 | draws out from its centre (Trim start 0.5 → 0, end 0.5 → 1, expo, f0–14); roll 0 → −9° (f50) → +4° (f95) → 0° (f125), S curve cubic-bezier(0.333, 0, 0.667, 1); pitch y +24 px (f60), −12 px (f110), 0 (f135) | trim settles **f9**; rotation **f125**; position **f135** |
| Pitch 1–4 (+ right halves) | 0 | parented to Horizon, so the ladder rolls and pitches with it | |
| Aircraft (fixed amber symbol) | 0 | Flicker on f8 | on **f18** |
| Heading ring (dashed 10 px stroke: tick marks) | 0 | scan open f6–16; turns 29° one way over the whole clip (Linear) | scale settles **f13** |
| Heading pointer, Heading 1–3 ("042", "056", "071") | 10 / 60 / 105 | value clips switch (each held ≥ 45 f for reading time) | |
| Speed box, Altitude box (+ 5 static ticks each) | 6 | scan open; values 12.4 → 14.1 → 15.8 and 118 → 124 → 131 switch at f55 and f100 | first value on **f24** |
| Rec dot | 4 | blinks once a second (Hold 100% ↔ 25%, 15 f each) | |
| REC, BAT, GPS, coordinates, MODE | 4–20 | Flicker on | |

Lint (with `contrast:true`) 0 errors, 0 warnings, 2 notes (`repeated_key_value`: the horizon holds level before the turn; intended). `inspect qc` (240 px): no flashes. Placed into a fresh comp: lint 0/0/0; the parented ladder survives placement. Text-gap audit: 476 pairs, closest 16 px (REC / Rec dot). Full-frame looks of the placed comp at f50 (widest bank) and f95: the rolled horizon stays clear of the speed and altitude boxes.

## Steps
1. Place it on a track above the footage; it has no background.
2. Change the readings by editing the value clips (each is its own text clip; keep each on screen 25 f or more).
3. Retime the bank in `telemetry()` (`hz.rot`, `hz.pos`); the ladder follows because it is parented.

## Pitfalls
- A value that changes every few frames fails lint `reading_time`: step readouts at 40 f or slower, or show a scale moving instead of the number.
- Labels above the boxes first sat 8 px from the side ticks (text-gap audit; lint was quiet, [KI-138](../references/known-issues.md#ki-138)); they moved 16 px up and the ticks 10 px out.

Inspiration: common sci-fi HUD and interface conventions. No external text or code was used.
