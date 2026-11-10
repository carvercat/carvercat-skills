# Tip reel, 9:16, 15.5 s

**Brief:** a vertical reel that hooks in the first second, gives three tips, asks for engagement and ends on follow. **Verified 0.1.6 (rev 1105), 2026-10-27; builder and measures re-run on Carvercat 0.1.8, 2026-11-04** Sample: `categories/recipes/tip-reel-9x16` (465 f, 1080 × 1920, near-black background). Builder: `ai/scripts/motion/recipes/rc_social.py` (the master is a `carvercat/2` file or one `scene.apply`: [how](README.md#how-the-samples-are-built)).

## Shot list
| Time | Frames | Template | Job | Notes |
|---|---|---|---|---|
| 0:00 | 0–74 | Hook title (9:16) | stop the scroll | readable by f10 |
| 0:02.5 | 75–224 | Listicle (9:16) | the three tips | tips 30 f apart |
| 0:07.1 | 213–236 | Swipe up (9:16) | next | covered on the cut at f225 |
| 0:07.5 | 225–374 | Poll sticker (9:16) | engagement | results land at +42–57 f |
| 0:12.1 | 363–386 | Swipe up (9:16) | next | covered on the cut at f375 |
| 0:12.5 | 375–464 | Follow end card (9:16) | follow | |

## Timing logic
- Scenes change every 2.5–5 s; the hook is the shortest.
- Everything stays inside the social safe area (the templates passed `bounds_inside`; check today with `measure.overlaps {within: "safe"}`); captions stay left of the right-hand buttons.

## Measured on the master
- The master comp is authored at 1080 × 1920; every template applied at 1080 × 1920. Lint 0 / 0 / 0.
- `qc` notes the poll hold (f271–363) and the follow card hold (f398–464) as freezes.

- **Speed streak (0.1.10):** the Swipe up transition carries a vertical `directionalBlur` (240 px at 90deg while the panel travels, 0 while it covers; [directional blur](../references/effects/directional-blur.md)); exact in Resolve, approximate in After Effects.

## Adapt it
1. Add the Story progress bar (9:16) over the whole length if the platform does not show one.
2. Swap the Poll for the Countdown (9:16) or the Post card (9:16) for a different middle beat.

Inspiration: the hook → value → engagement → follow structure of short-form reels. No external text or code was used.
