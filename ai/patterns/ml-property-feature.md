# Property feature

**Template** `ml_property_feature` (Library name "Property feature") · Minimal Luxury pack · **Verified 0.1.8.1 (rev 1127)**, comp `ML Property feature` in `categories/minimal-luxury/ml-lab-3`.

For briefs like "hotel suite", "villa for sale", "the residence". A photo window opens from the left on a slowly pushing photo (a gradient stand-in here), and the name of the place, a gold rule and three details settle on the right. 180 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Photo (stand-in, 1000 × 640 px at x 700, y 540, vertical warm gradient) | 0 | scale 1.00 → 1.04, linear over the clip (the push) | linear to **f179** |
| Photo window (the mask, same size, anchor at the left edge) | 0 | width 0 → 1, f0–54, S curve cubic-bezier(0.333, 0, 0.667, 1), the curve arriving at the key | **0% overshoot**, settles **f49** |
| Kicker "THE RESIDENCE" (gold Regular 26 px, tracking 1.5, x 1300) | 30 | opacity in 36 f | |
| Name "Villa Serena" (ivory Regular 64 px) | 40 | up 14 px over 40 f (decelerate), then a 0.3% H drift | opaque **f71** |
| Rule (240 px gold, y 530) | 0 | draws left to right, f56–96, S curve | settles **f92** |
| Details (muted Regular 30 px, 52 px apart) | 70, 82, 94 | opacity in 36 f | Detail 3 opaque **f125** |

Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 10 pairs, closest 30.0 px (Detail 2 / Detail 3). Full-frame looks of the placed instance at f30 and f179: the window opens and the photo pushes inside the frame; nothing is cut.

How it is built: the window is the mask and the photo its content (`property.set {id:"photo", key:"mask", value:{"ref":"<window id>"}}`, then `parent.clear {ids:[window, photo]}`). The push is on the photo; the window holds still, so the photo's edges stay where the window puts them.

## Steps
1. Replace the stand-in: import the photo or video, place it at x 700, y 540 and size it to cover 1000 × 640 px, run `property.set {id:"your photo", key:"mask", value:{"ref":"<Photo window id>"}}` + `parent.clear {ids:[Photo window, your photo]}`, then delete the Photo rectangle.
2. Change the kicker, name and details. Keep the name to one line ("Villa Serena" at 64 px measures 337 px; the column has 524 px before the graphics-safe edge at x 1824).

## Pitfalls
- A 4% push over 6 s is below what `qc` notices; judge it with a look at the first and last frame.
- The stand-in is dark on purpose (a warm-black photo stand-in); a real photo will carry more contrast. Check the details' contrast against the ground, not against the photo.

Inspiration: hotel and property listings in luxury real-estate films. No external text or code was used.
