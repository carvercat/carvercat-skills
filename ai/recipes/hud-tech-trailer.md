# HUD tech trailer, 23 s

**Brief:** you need a sci-fi or tech-product teaser with interface graphics. **Verified 0.1.6 (rev 1105), 2026-10-28; builder and measures re-run on Carvercat 0.1.8, 2026-11-04** Sample: `categories/recipes/hud-tech-trailer` (700 f, 1920 × 1080). Builder: `ai/scripts/motion/recipes/rc_hud.py` (the master is a `carvercat/2` file or one `scene.apply`: [how](README.md#how-the-samples-are-built)).

## Shot list
| Time | Frames | Template (track) | Job |
|---|---|---|---|
| 0.0 s | 0–119 | Hex grid (scene) | boot |
| 4.0 s | 120–209 | Target lock (scene) | acquire |
| 7.0 s | 210–329 | Signal bars (scene) | analyse |
| 11.0 s | 330–449 | Map ping (scene) | locate |
| 15.0 s | 450–569 | Alert banner (scene) | alarm |
| 19.0 s | 570–699 | Segment loader (scene) | resolve |
| 10.5 s | from 316 | Scan wipe (overlay / transition) | scan wipe into the map (cut at f330) |

## Measured on the master
- Lint 0 / 0 / 0; every template applied at 1920 × 1080.
- `qc` (240 px) notes the hex-grid hold (f23–119) as a freeze and finds no flashes.

## Adapt it
1. Open each placed template's comp and edit the copy.
2. Keep the cut frames; if a scene grows, move everything after it (and any transition with its cut).

Inspiration: common futuristic hud motion conventions for this kind of brief. No external text or code was used.
