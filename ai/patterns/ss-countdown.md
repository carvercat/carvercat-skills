# Countdown (9:16)

**Template** `ss_countdown` · Social Short-form pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SS Countdown` in `categories/social-media-reels/ss-lab-2`.

"3", "2", "1" (white, ExtraBold 300 px) and "GO" (yellow, 220 px), one 25 f beat each, each inside a 420 px ring that draws round over its beat. 100 f.

| Part | Clip | Motion | Measured |
|---|---|---|---|
| Count 1–4 | f0, 25, 50, 75, 25 f each | scale 1.35 → 1, 8 f, expo; no fade (a hard cut in) | settles **5 f** into each beat |
| Ring 1–4 (14 px stroke, rotation 90° (stored value); the GO ring pink) | same | trimStart 100% → 0% over the 25 f, linear | |

Lint 0 errors, 0 warnings. `bounds_inside` the safe box [61, 268, 955, 1270] passed for every object. Placed into a fresh 1080 × 1920 comp (`comp.format`): applied at 1080 × 1920, lint 0/0/0. Each number is readable for its full 25 f (lint's minimum), so there is no fade-in.

## Steps
1. Place so that "GO" lands on your beat drop (instance start = drop − 75 f). Add a tick SFX on f0, 25, 50 and a hit on 75.

Inspiration: 3-2-1 countdowns before a reveal. No external text or code was used.
