# Retro weather map

**Template** `rt_weather_map` (Library name "Retro weather map") · Retro pack · **verified 0.1.8.1 (rev 1127)**, comp `RT Weather map` in `categories/retro/rt-lab-3`.

**Measured on 0.1.8.1 (rev 1127, harness `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0, no flashes; against the v1 original the worst silhouette difference is 0.00 % (limit 2 %) and every object is present with the same text (box offset at most 2.6 px); colours are now the exact hex the page states (mean shift 11.5 of 255, intended); windows over a magenta/green underlay: covered f0-149 (cut f0). The frame numbers in the table above are the keys of the generator (`design units`), unchanged.


For briefs like "retro weather forecast", "local news weather", "70s / 80s TV weather map", or a fun "forecast" for an event. A teal sea, a cream island with a brown outline, a WEATHER / TUESDAY header, and four towns that each get a sun, cloud or rain-cloud icon and a red temperature tile with the name below. 150 f, holds. Full-frame sea included. The island, towns and temperatures are invented.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Header (600 × 120 px) | 0 | grows from the left on twos, 12 f | **f8** |
| Header title "WEATHER" (ExtraBold 64 px) / Header day (Bold 34 px) | 6 / 10 | Rise - on twos | **f16** / **f20** |
| Town icons (sun: 160 px rays + 96 px disc; clouds: four parts as one group) | 16, 26, 36, 46 | Pop - on twos as keys (clouds with `group2()` from size 0) | **3.9%**, Port Ash sun **f28**, Kelby cloud **f38** |
| Sun rays | town + 12 | turn −45° to the end, one way, linear | |
| Rain drops (Marrow) | 44 | fade in on twos | **f48** |
| Tiles (140 × 96 px) and temperatures (ExtraBold 60 px) | town + 4 | Pop - on twos; the temperature from size 0.5 | **3.9%**, Port Ash **f32**, Tolly Bay **f62** |
| Town names (Bold 36 px) | town + 8 | Rise 20 px on twos, 12 f | Tolly Bay **f62** |

Lint 0 errors, 0 warnings in the lab (15 notes, `speed_jump` on the stepped moves); placed 0/0/0. `inspect qc`: no flashes. Text-gap audit: closest pair 21.4 px (WEATHER and TUESDAY). Full-frame look of the placed instance at f149: nothing cut.

## Steps
1. Edit `CITIES` (name, x, y, sun / cloud / rain, temperature) and `ISLAND` (outline points, smoothed by `smooth_closed()`) in `retro_lab3.py`, then rebuild.
2. For a real region, trace its outline as points in comp pixels; keep the towns 300 px or more apart.

## Pitfalls
- The temperatures first popped from size 0: their first stepped frame was `text_too_small` (15.8 px, under 18). Pop them from 0.5 (or set them larger).
- After moving a town, check the map with a full-frame look as well as the text-gap audit: the audit pairs texts with shapes up to 80 px only, so a 160 px sun over a label is a look check ([KI-138](../references/known-issues.md#ki-138)).

Inspiration: 1970s and 80s TV weather maps with magnetic symbols. No external text or code was used.
