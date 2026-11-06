# Before after split (9:16)

**Template** `ss_before_after` (Library name "Before after split (9:16)") · Social Short-form pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SS Before after` in `categories/social-media-reels/ss-lab-2`.

Two 920 × 560 px rounded panels stacked vertically (stand-ins for two clips) with outlined labels: "BEFORE" (white) and "AFTER" (yellow), ExtraBold 64 px. 120 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Before panel (y 290–850) | 0 | Hook punch | |
| Before label | 6 | Hook punch | |
| After panel (y 900–1460) | 16 | Whip in - left | settles **f23** |
| After label | 22 | Hook punch | settles **f29** |

Lint 0 errors, 0 warnings. `bounds_inside` the safe box [61, 268, 955, 1270] passed for every object. Placed into a fresh 1080 × 1920 comp (`comp.format`): applied at 1080 × 1920, lint 0/0/0.

## Steps
1. Place and apply. Replace each panel with a clip masked by it: `property.set {id:<clip>, key:"mask", value:{"ref":"<panel id>"}}`, then `parent.clear {ids:[panel, clip]}`.
2. Add the Motion blur effect to the After panel's whip.

## Pitfalls
- The After panel reaches into the button column (x > 851 below y 1151). That is fine for footage; keep text out of it.

Inspiration: before/after reveals in short-form video. No external text or code was used.
