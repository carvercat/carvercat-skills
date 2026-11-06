# Alert banner

**Template** `fh_alert_banner` · Futuristic HUD pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FH Alert banner` in `categories/futuristic-hud/fh-lab-2`.

A 1600 × 150 px dark-amber band with glowing amber edges and "WARNING // HULL BREACH" (amber SemiBold 64 px). 120 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Alert band, Alert edge 1–2 (1000 px drawn, scale X 1.6) | 0 | Scan open (Y) | settles **f10** |
| Alert text | 8 | opacity Hold: on f10, 35% f40–48, on, 35% f70–78, on | steady from **f78** |

Lint 0 errors, 0 warnings; `inspect qc` (240 px) found no flashes. Placed into a fresh comp: lint 0/0/0. Two pulses a second apart stay far under the 3-flashes-a-second limit.

Inspiration: alert banners in sci-fi interfaces. No external text or code was used.
