# Listicle (9:16)

**Template** `ss_listicle` · Social Short-form pack · **verified 0.1.8.1 (rev 1127)**, comp `SS Listicle` in `categories/social-media-reels/ss-lab-2`.

**Measured on 0.1.8.1 (rev 1127, harness `verify_pack.py`):** placed in a fresh 16:9 and 9:16 comp, lint 0/0/0 and 0/0/0, no flashes; against the v1 original the worst silhouette difference is 0.11 % (limit 2 %) and every object is present with the same text (box offset at most 2.0 px); colours are now the exact hex the page states (mean shift 6.1 of 255, intended). The frame numbers in the table above are the keys of the generator (`design units`), unchanged.


A two-line hook header ("3 THINGS / I WISH I KNEW", ExtraBold 96 px, line spacing 1.05) and three tips, each with a pink numbered badge (96 px), 150 px apart. 150 f (5 s), holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| List header | 0 | Hook punch | |
| Badge 1–3 | 24, 54, 84 | scale 0 → 1, 10 f, back ease | **9.7% overshoot**; Badge 1 settles **f34** |
| Badge num 1–3 | badge + 2 | Hook punch | |
| Tip 1–3 (Bold 50 px) | badge + 4 | Caption words pop (3 f per word) | 4.4% overshoot per word |

Lint 0 errors, 0 warnings. `bounds_inside` the safe box [61, 268, 955, 1270] passed for every object. Placed into a fresh 1080 × 1920 comp (`comp.format`): applied at 1080 × 1920, lint 0/0/0. Each tip is on screen for at least 62 f before the end, well over lint's reading time.

## Steps
1. Place and apply. Edit the header and tips; one line each. The longest tested tip, "Start before you're ready" (25 characters at 50 px from x 250), passed `bounds_inside`.
2. Pace: 30 f between tips suits short tips; add 1 f per extra character for long ones.

Inspiration: numbered "things I wish I knew" listicles in short-form video. No external text or code was used.
