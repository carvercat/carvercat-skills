# Sidebar drawer

**Template** `su_sidebar_drawer` · SaaS UI pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SU Sidebar drawer`.

A full 1920×1080 app frame: a light canvas, a header with a "Dashboard" title, and three stand-in cards. A 360 px dark sidebar (brand dot plus four menu bars) slides in over it while a scrim dims the dashboard.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Sidebar, Brand dot, Menu 1–4 | 6–28 | position −360 px → 0, Custom expo cubic-bezier(0.16, 1, 0.3, 1). One key pair on every part, so the drawer moves as one piece | settles **f20** |
| Scrim (ink, full frame) | 6–28 | opacity 0 → 0.4, same curve | settles **f20** |

## Steps
1. Place and apply. Replace the stand-in Header and Card objects with your screen (keep them under the Scrim).
2. To close: key the sidebar parts back to −360 px with an accelerating Custom curve cubic-bezier(0.3, 0, 0.8, 0.15) over about 14 f, and the scrim back to 0.

## Why a drawer and not a push
A push that slides the dashboard 360 px right leaves its right side off frame at rest, and lint reports it (`cropped_at_rest` 50% on the last card). The overlay drawer keeps every object fully on screen. Lint: 0 errors, 0 warnings; info notes for the expo's fast first frame and the header title above the graphics-safe line (it is app chrome).
