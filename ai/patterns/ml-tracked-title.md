# Tracked title

**Template** `ml_tracked_title` · Minimal Luxury pack · **Verified 0.1.8.1 (rev 1127)**, comp `ML Tracked title` in `categories/minimal-luxury/ml-lab`.

"MAISON ELAN" in Rethink Sans Regular 72 px caps, ivory, centred. Under it, a 240 px gold rule and the tagline "PARIS · SINCE 1924" (28 px, muted, tracking 1.5).

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Title tracking | 0–60, then 60–120 | 1.8 → 1.35, Custom decelerate (0.05, 0.7, 0.1, 1); then 1.35 → 1.38, linear (breathe) | reaches 1.35 at f60; curves reports 7.1% "overshoot" because it measures the breathe past the f60 target |
| Title opacity | 0–30 | 0 → 1, the decelerating arrival curve cubic-bezier(0.333, 0.667, 0.667, 1) | settles **f28** |
| Rule | 20–50 | Trim Stroke start 0.5 → 0 and end 0.5 → 1 (draws out from the centre), Custom expo | settles **f39** |
| Tagline | from 40 | **Slow fade in** | opacity settles **f72** |

Lint 0/0/0. Edit the two texts inside the comp. Centred text stays centred while its tracking animates.
