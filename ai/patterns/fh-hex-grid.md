# Hex grid

**Template** `fh_hex_grid` · Futuristic HUD pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FH Hex grid` in `categories/futuristic-hud/fh-lab-2`.

A background of 84 outlined hexagons (140 px, 2 px dim-cyan stroke) that switch on in a ring spreading from the centre, with a glowing cyan core hex. 120 f.

| Part | Motion | Measured |
|---|---|---|
| Hex 1–84 | opacity Hold: off, on at (distance from centre / 40 px) frames, a 2 f dip to 30%, on | the corners are on by **f26** |
| Core hex | Flicker on | on by **f10** |

Lint 0 errors, 0 warnings; `inspect qc` (240 px) found no flashes. Placed into a fresh comp: lint 0/0/0.

## Pitfalls
- `cc.ngon` fills the shape even when no colour is given; clear it with `nofill()`. The first build was a wall of white hexagons.
- Hexes cut by the frame edge sit still and trip `cropped_at_rest`; the grid keeps only whole hexes.

Inspiration: hexagonal HUD grids. No external text or code was used.
