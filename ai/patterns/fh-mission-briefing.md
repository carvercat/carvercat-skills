# Mission briefing

**Template** `fh_mission_briefing` (Library name "Mission briefing") · Futuristic HUD pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FH Mission briefing` in `categories/futuristic-hud/fh-lab-3`.

For briefs like "game mission intro", "campaign briefing", "heist or agenda card" in a sci-fi style. A panel scans open inside corner brackets; the mission number and operation name come on, a grid map draws, a dashed route runs to a target that pings, three objectives type on with check boxes, and the deploy time flickers in. 180 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Panel (1300 × 660, #08121A), Panel corner 1–4 | 0 | scan open, 12 f; corners static | scale settles **f8** |
| Header strip | 4 | scan open | |
| Mission no (amber), Clearance (#4FA8BF) | 10 / 14 | Flicker on | |
| Operation "OPERATION NIGHTFALL" (60 px) | 18 | types on, 1 f a character | |
| Map frame, Grid V1–6 / H1–4, Contour 1–3 | 10–24 | scan open; grid lines and contours draw (Trim) f15–40 | |
| Start marker | 36 | Flicker on | |
| Route (dashed, 4 px) | 40 | Trim end 0 → 1, smooth, f40–70 | settles **f67** |
| Target, Target ping 1–3, Target tag | 66 / 70, 100, 130 / 74 | pop 0 → 120 → 100% (f66–76); rings grow 0.3 → 3.2× and fade over 30 f; tag flickers on under the target | scale settles **f76** (the 20% is the keyed peak) |
| Objectives, Check 1–3, Objective 1–3 (32 px) | 30 / 44, 56, 68 / 48, 60, 72 | label and boxes flicker on; each objective types on | |
| Deploy label / Deploy time "00:30:00" (amber 52 px) | 96 / 100 | Flicker on | on **f110** |

Lint (with `contrast:true`) 0 errors, 0 warnings, 0 notes. `inspect qc` (240 px): no flashes; a freeze from f110 (the hold, intended). Placed into a fresh comp: lint 0/0/0. Text-gap audit: 135 pairs, closest 21.6 px (Deploy label / time). Full-frame look of the placed comp at f179: nothing cut, every text inside the panel.

## Steps
1. Replace the map stand-in (grid and contours) with a still of the real map inside the map frame; move the target by `tx, ty`.
2. Keep objectives short (about 20 characters at 32 px fit the panel).

## Pitfalls
- Objectives at 34 px with tracking 1.2 ran 40 px past the panel's right edge; lint has no check for text leaving its plate ([KI-157](../references/known-issues.md#ki-157)). Measure with `measure.boxes` against the panel.
- The target's tag beside the target ran out of the map into the objectives column; under the target it stays inside the map.
- Header texts first sat 6 px from the corner brackets (text-gap audit); they are 60 px in from the panel edge now.

Inspiration: common sci-fi HUD and interface conventions. No external text or code was used.
