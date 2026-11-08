# Map ping

**Template** `fh_map_ping` · Futuristic HUD pack · **verified 0.1.8.1 (rev 1127 build; headless, isolated folders, pack added to a scratch user Library; `ai/scripts/motion/verify_pack.py`)**, comp `FH Map ping` in `categories/futuristic-hud/fh-lab-2`.

An amber point at (820, 560) with three cyan rings rippling out, a leader line, coordinates and a place name. 120 f.

| Part | Clip | Motion | Measured |
|---|---|---|---|
| Ping ring 1–3 | f0, 20, 40, 40 f each | scale 0.1 → 2.2 (decelerate) and fade to 0 | ring 1 scale settles **f30** |
| Ping dot | 0 | Flicker on | |
| Ping leader | 10 | Trim end, f10–24 | |
| Ping coords, Ping name | 20, 26 | Flicker on | coords on by **f30** |

Lint 0 errors, 0 warnings; `inspect qc` (240 px) found no flashes. Placed into a fresh comp: lint 0/0/0. Each ring only grows (one way) and lives only for its own 40 f.

## Steps
1. Place over a map or footage; move the instance so the dot sits on the location; edit the coordinates and name.

Inspiration: location pings on tactical maps. No external text or code was used.
