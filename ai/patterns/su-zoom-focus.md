# Zoom to card

**Template** `su_zoom_focus` (Library name "Zoom to card") · SaaS UI pack · **Verified 0.1.8.4 (rev 1130)**, comp `SU Zoom focus` in `categories/saas-launch/saas-ui-lab-3`.

Object check: during the camera zoom measure.boxes reads text up to 213 px off while the pixels match (edge maps of v1 and v2 at 960 × 540 agree within 2 px on 99.3–100 % of edge pixels at all 7 compared frames, shape 0.00 %). `verify_pack.py --ink-templates` cannot measure the text at f50–99 (no ink inside the reported boxes), so this template has no automatic object-check pass; the pixel comparison above is the evidence.

For briefs like "zoom into the feature", "show the one number that matters", "UI demo with camera moves". A full analytics app frame (dark sidebar, header, three KPI tiles, a bar chart and a "Conversion rate" card with 4.8% and a progress bar). The camera pushes in on the Conversion card, holds while a ring appears and the bar fills, then pulls back. 150 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| App canvas (the camera; every other object is parented to it) | 0 | f20–46: scale 1 → 1.7 and position so the card's centre lands on the frame centre (S curve cubic-bezier(0.333, 0, 0.667, 1)); f46–104: slow linear push 1.7 → 1.76; f104–128: back to 1 (S curve cubic-bezier(0.333, 0, 0.667, 1)) | 0% overshoot; settles **f128** |
| Focus ring (accent outline, 4 px) | 48 | opacity in f48–56, out f98–104 | |
| Focus fill | 0 | trimEnd 30% → 62% f56–80 (expo) | |

Lint 0 errors, 0 warnings (3 notes). Placed into a fresh comp: lint 0/0/0, and the full-frame look of the placed instance shows no cut content (checked for [KI-144](../references/known-issues.md#ki-144)). Text-gap audit: no tight pairs.

## Steps
1. Place and apply. It is a whole app frame (not an overlay). Edit the labels and values, or replace the cards with your own UI parented to App canvas.
2. Another target card: for focus point T and zoom z, the canvas centre position is **C − z·(T − C)** (x, y are its top-left, so subtract half its size) (C = frame centre). Keep T within x 565–1355 and y 318–762 at 1.76× so the frame never leaves the app; the lab script does the maths (`at(z)`).
3. Keep the camera still while the viewer reads: here the reading (ring, bar) happens in the hold, never during the move.

## Pitfalls
- **A held zoom trips lint:** with a still 1.7× hold (same layout, measured), lint reported six `cropped_at_rest` warnings (App canvas 35% on screen, Sidebar 54%, Tile 1 9%, Tile 2 5%, Chart 28%, Bar 3 4%). The slow push through the hold (1.7 → 1.76) keeps the camera moving, clears every warning, and keeps the hold from freezing.
- **Pick a target away from the app's edge.** The first build zoomed on a card at the right edge; at 1.7× the frame ran past the app and showed black.
- At rest the camera's position is the frame centre. Writing the rest key with the zoom formula at z = 1 (C − (T − C)) shifts the whole app by T − C; lint then reported Header and Brand dot as `never_visible`.

Inspiration: zoom-to-feature moves in product demo videos. No external text or code was used.
