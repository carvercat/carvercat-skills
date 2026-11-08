# HUD ID lower third

**Template** `fh_id_lower_third` (Library name "HUD ID lower third") · Futuristic HUD pack · **verified 0.1.8.1 (rev 1127 build; headless, isolated folders, pack added to a scratch user Library; `ai/scripts/motion/verify_pack.py`)**, comp `FH ID lower third` in `categories/futuristic-hud/fh-lab-2`.

Four cyan corner brackets (820 × 180 px box at bottom left, x 120–940, y 795–975, glow 0.45) around a tracked callsign (SemiBold 46 px, tracking 1.3), an ID line (28 px, dim cyan) and an amber status dot. 150 f (5 s) with its own exit.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| ID corner 1–4 | 0 | Trim end 0 → 1 over 12 f (expo); Power down (last 12 f) | drawn by **f8** |
| Callsign, ID line | 8, 16 | Flicker on; Exit fade - fast | |
| Status dot | 22 | Flicker on; Power down | |

Lint 0 errors, 0 warnings; `inspect qc` (240 px) found no flashes. Placed into a fresh comp: lint 0/0/0.

## Pitfalls
- Power down squeezes its target to 2% height. On text that is a lint `text_too_small` warning ("a line is 0.7 px tall"), so the texts leave with Exit fade - fast and only the shapes power down.
- Tracked caps are wide: the 15-character callsign at 46 px and tracking 1.3 ends near x 850 (geometry), about 700 px from its start.
- **Fixed 2026-10-28 (overlap audit).** The first release put the status dot on the callsign's last letters (22 px overlap) and the ID line 0.4 px from the lower brackets, with lint 0/0/0 ([KI-138](../references/known-issues.md#ki-138)). The dot is now at x 890 and the bracket box is 820 × 180 px; the smallest gap at rest is 18.1 px (callsign to the top-left bracket).

Inspiration: sci-fi identity tags. No external text or code was used.
