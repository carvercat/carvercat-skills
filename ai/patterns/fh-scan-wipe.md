# Scan wipe

**Template** `fh_scan_wipe` · Futuristic HUD pack · **verified 0.1.8.1 (rev 1127 build; headless, isolated folders, pack added to a scratch user Library; `ai/scripts/motion/verify_pack.py`)**, comp `FH Scan wipe` in `categories/futuristic-hud/fh-lab-2`.

A transition: a glowing cyan beam sweeps down the frame with a dark-teal panel growing behind it, then both retract upward. 30 f.

| Part | Motion | Measured |
|---|---|---|
| Scan panel (1000 px drawn, anchor at its top edge, top at y 0) | scale 1.92 × 0 → 1.92 × 1.08, f0–12 (S curve cubic-bezier(0.333, 0, 0.667, 1)); hold to f16; back to 0, f16–30 (accelerating) | covers **f12–16** |
| Scan beam (6 px, glow 0.6) | rides the panel's bottom edge, kept 4 px inside the frame | |

Lint 0 errors, 0 warnings; `inspect qc` (240 px) found no flashes. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place 14 f before your cut, above both scenes; cut at its f14.

## Pitfalls
- A panel anchored at its top edge scales from that edge, so the panel is centred at y 500 (top at 0) for a 1.08 scale to reach the bottom.
- The beam waiting exactly on the frame edge was half off screen and still (`cropped_at_rest`); it waits 4 px inside.

Inspiration: scanline transitions in sci-fi titles. No external text or code was used.
