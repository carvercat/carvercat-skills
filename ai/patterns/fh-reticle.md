# Targeting reticle

**Template** `fh_reticle` · Futuristic HUD pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FH Reticle` in `categories/futuristic-hud/fh-lab`.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Outer ring (440 px, 4 px dashed cyan: dash 28, gap 14; glow) | 0–14, then 0–90 | **Scan open (Y)**; rotation 0 → 60°, linear | scale settles **f10** |
| Inner arcs (300 px, 8 px butt-capped, glow) | 6–20, then 6–90 | Trim Stroke end 0.1 → 0.45 (expo); rotation 0 → −90°, linear | arc settles **f15** |
| Crosshairs (4 lines, ±90 to ±270 px from the centre) | 10–22 | Trim end 0 → 1, expo | |
| Centre dot / "TARGET LOCKED" (34 px amber, tracked) | from 20 / 30 | **Flicker on** | label fully on at **f40** |

Lint 0/0; qc found no flashes. Move the instance so the centre sits on the target. Change the label text inside the comp.
