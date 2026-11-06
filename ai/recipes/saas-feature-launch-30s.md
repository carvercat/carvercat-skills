# SaaS feature launch, 30 s

**Brief:** announce a new feature in 30 seconds: hook, show the product working, prove it with a number, end on one action. **Verified 0.1.6 (rev 1105), 2026-10-27; builder and measures re-run on Carvercat 0.1.8, 2026-11-04** Sample: `categories/recipes/saas-feature-launch-30s` (900 f, 1920 × 1080, indigo gradient background). Builder: `ai/scripts/motion/recipes/rc_saas.py` (the master is a `carvercat/2` file or one `scene.apply`: [how](README.md#how-the-samples-are-built)).

## Shot list
| Time | Frames | Template (pack) | Job in the story | Notes |
|---|---|---|---|---|
| 0:00 | 0–89 | Feature title (SaaS UI) | hook: what's new | 3% push f20–89 on the instance |
| 0:03 | 90–209 | Chat thread (SaaS UI) | the problem in users' words | bubbles at +0/26/52 f |
| 0:07 | 210–299 | Dropdown menu (SaaS UI) | the product, first touch | |
| 0:09.4 | 282–317 | Slide wipe (Transitions) | cut into the app | covered on the cut at f300 |
| 0:10 | 300–389 | Modal over app (SaaS UI) | the key interaction | full app frame |
| 0:13 | 390–479 | Chart card (SaaS UI) | the result as a chart | bars settle +28–46 f |
| 0:16 | 480–569 | KPI tile (SaaS UI) | the result as a number | 3% push f500–569 |
| 0:19 | 570–689 | Notification toast (SaaS UI) | it reaches you | toast exits by +120 f |
| 0:23 | 690–779 | Stat punch (Kinetic Typography) | the headline claim | "3x faster renders" |
| 0:25.4 | 762–797 | Slide wipe (Transitions) | into the end card | covered on the cut at f780 |
| 0:26 | 780–899 | CTA end card (SaaS UI) | one action | holds 80 f after the last element lands |

## Timing logic
- 9 scenes in 30 s: 3–4 s each, the hook and the end card longer.
- Two transitions only, at the two big changes of setting (into the app, into the close). Other scenes cut.
- Entrance styles stay in one family (SaaS expo/Card lift) except the Stat punch slam, the one exaggerated beat.

## Measured on the master
- Lint 0 / 0 / 0. All 11 placed templates applied at 1920 × 1080.
- The pushes on the Feature title and KPI tile instances measure 0.0004 a frame (`curves`, scaleUniform). `qc` at 240 px still notes those holds as freezes (f26–89, f493–569) because a 3% push is below its threshold; the toast hold (f581–681) and the end card (f811–899) are noted too.
- A push on the Notification toast instance moved the toast past the top edge (lint `cropped_at_rest`, 94% on screen), so that instance has none.

## Adapt it
1. Open each placed template's comp and edit the copy and numbers; replace the Modal's app canvas with your screenshot.
2. Keep the cut frames; if a scene gets longer, move everything after it by the same amount (and the transition with its cut).
3. For 9:16, use the Social Short-form templates instead ([tip-reel-9x16.md](tip-reel-9x16.md)).

Inspiration: the common hook → problem → product → proof → CTA structure of product launch videos. No external text or code was used.
