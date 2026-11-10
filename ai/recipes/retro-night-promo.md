# Retro night promo, 13 s

**Brief:** you need a short retro-themed event or product promo. **Verified 0.1.6 (rev 1105), 2026-10-28; builder and measures re-run on Carvercat 0.1.8, 2026-11-04** Sample: `categories/recipes/retro-night-promo` (384 f, 1920 × 1080). Builder: `ai/scripts/motion/recipes/rc_retro.py` (the master is a `carvercat/2` file or one `scene.apply`: [how](README.md#how-the-samples-are-built)).

## Shot list
| Time | Frames | Template (track) | Job |
|---|---|---|---|
| 0.0 s | 0–89 | Chrome title (scene) | the title |
| 3.0 s | 90–209 | Neon sign (scene) | the place |
| 7.0 s | 210–359 | Arcade start screen (scene) | the call to play |
| 12.0 s | 360–383 | TV switch-off (scene) | switch off |
| 6.1 s | from 184 | Venetian blinds (overlay / transition) | blinds into the arcade (cut at f210) |

## Measured on the master
- Lint 0 errors, 1 warning, 0 notes: the warning is `never_visible` on the finishing layer (an adjustment layer draws nothing itself, [KI-158](../references/known-issues.md#ki-158)). Every template applied at 1920 × 1080.
- **Finishing grain (0.1.10):** an adjustment layer "Film grain" on the top track over the whole 384 f carries `grain "0.14 2.5px softness=0.4 colour=0.5"` (tape-like: coloured, 2.5 px). It is the one grain for every scene, so the templates stay as they are ([grain](../references/effects/grain.md)). Remove it by deleting the layer; approximate in Resolve and After Effects.
- `qc` (240 px) notes the title hold (f24–89) as a freeze and finds no flashes.

## Adapt it
1. Open each placed template's comp and edit the copy.
2. Keep the cut frames; if a scene grows, move everything after it (and any transition with its cut).

## Notes
- The Chrome title in this sample is the fixed one (2026-10-28, [KI-155](../references/known-issues.md#ki-155); [../patterns/rt-chrome-title.md](../patterns/rt-chrome-title.md)): the first release had its chrome upside down. Fixed in the saved sample with `property.set` on the placed word; master lint 0/0/0 before and after.

Inspiration: common retro motion conventions for this kind of brief. No external text or code was used.
