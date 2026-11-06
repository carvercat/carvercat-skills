# Synthwave sun

**Template** `rt_synthwave` · Retro pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `RT Synthwave`.

A night sky, a 520 px sun (linear gradient yellow → pink, top to bottom) cut by five night-coloured bands, a glowing pink horizon at y 640, a perspective floor grid, and "NEON NIGHTS" (ExtraBold 120 px cyan, text fill glow 4).

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Sun | 0–16 | scale 0 → 1 on twos (expo) | settles **f10** |
| Bands | 0–120 | drift up 24 px, linear (one way) | |
| Vertical grid lines (7, from the vanishing point at (960, 640), ending at the frame edge) | 0–20 | Trim end 0 → 1, expo | |
| Horizontal grid lines | starts 0, 20, 40, 60, 80 | each runs horizon → bottom in 40 f with the accelerating arrival curve cubic-bezier(0.333, 0, 0.667, 0.333) (accelerating toward the viewer) | |
| Title | from 20 | **Rise - on twos** | settles **f30** |

Lint 0/0; qc found no flashes. The floor rectangle hides the sun's lower part below the horizon.

**Fixed 2026-10-28 ([KI-155](../references/known-issues.md#ki-155)).** The sun rendered upside down: pink at the top, yellow at the bottom, the blend squeezed into the middle. Its gradient endpoints had been written as comp coordinates with y up (`[0.5, 0.833]` → `[0.5, 0.352]`); a shape gradient is object-local with y down. They are now `[0.5, 0]` → `[0.5, 1]`. Measured on 0.1.6 (rev 1105) at f60, sampled down the sun's centre from y 200 to y 500: yellow `(255, 202, 21)` → `(255, 129, 96)`. Placed into a fresh comp: lint 0/0/0. `categories/retro/rt-lab` and `rt-showcase` carry the same fix ([audit](../references/audits/gradient-direction-audit-2026-10-28.md)).
