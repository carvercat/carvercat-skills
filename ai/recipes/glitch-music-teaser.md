# Glitch music teaser, 14 s

**Brief:** you need a short teaser for a release, drop or tech launch with a glitch look. **Verified 0.1.6 (rev 1105), 2026-10-28; builder and measures re-run on Carvercat 0.1.8, 2026-11-04** Sample: `categories/recipes/glitch-music-teaser` (430 f, 1920 × 1080). Builder: `ai/scripts/motion/recipes/rc_glitch.py` (the master is a `carvercat/2` file or one `scene.apply`: [how](README.md#how-the-samples-are-built)).

## Shot list
| Time | Frames | Template (track) | Job |
|---|---|---|---|
| 0.0 s | 0–99 | Stutter words (scene) | the hook (NO SIGNAL FOUND) |
| 3.3 s | 100–189 | Block artifact title (scene) | the title |
| 6.3 s | 190–279 | RGB split mark (scene) | the mark |
| 9.3 s | 280–429 | Terminal type-on (scene) | the reveal (ACCESS GRANTED) |
| 0.0 s | from 0 | Tracking band (overlay / transition) | tracking-error overlay over the opening |
| 5.7 s | from 171 | Pixel dissolve (overlay / transition) | pixel dissolve into the mark (cut at f190) |

## Measured on the master
- Lint 0 errors, 1 warning, 0 notes: the warning is `never_visible` on the finishing layer (an adjustment layer draws nothing itself, [KI-158](../references/known-issues.md#ki-158)). Every template applied at 1920 × 1080.
- **Finishing grain (0.1.10):** an adjustment layer "Film grain" over the whole 430 f carries `grain "0.1 2.5px softness=0.2 colour=0.6"`: coloured digital noise under the glitches ([grain](../references/effects/grain.md)). Approximate in Resolve and After Effects.
- `qc` (240 px) notes f280–383 (the terminal typing, too small for it to see) as a freeze and finds no flashes.

## Adapt it
1. Open each placed template's comp and edit the copy.
2. Keep the cut frames; if a scene grows, move everything after it (and any transition with its cut).

Inspiration: common glitch motion conventions for this kind of brief. No external text or code was used.
