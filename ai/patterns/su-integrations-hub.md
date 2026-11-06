# Integrations hub

**Template** `su_integrations_hub` (Library name "Integrations hub") · SaaS UI pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SU Integrations hub` in `categories/saas-launch/saas-ui-lab-3`.

For briefs like "works with your tools", "connects everything", "an ecosystem". A 180 px accent hub tile with the product mark "A" in the centre; six white 120 px app tiles on an ellipse around it (380 × 270 px radii), each with a simple coloured shape (circle, diamond, star, square, hexagon, ring) as a stand-in icon; links draw out from the hub, and a small pulse runs along every link twice. A headline below (Bold 44). 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Hub and mark (mark parented to the hub) | 0 | pop 0 → 1, small spring, 14 f | **4.3% overshoot, settles f13** |
| Link 1–6 (4 px lines, under the tiles) | 12 + 3 f each | trimEnd 0% → 100% (expo, 14 f) | each settles 9 f after its start (Link 1 **f21**) |
| Tile 1–6 (icon parented to its tile) | 20 + 3 f each | pop 0 → 1, small spring, 12 f | **4.3% overshoot**, settle **f31–46** |
| Headline | 36 | lift (16 px, 16 f) | settles **f46** |
| Pulse 1–6 (18 px dots), two rounds | 54 and 98, 4 f apart | hub → tile in 20 f (S curve cubic-bezier(0.333, 0, 0.667, 1)), fade in 4 f, out over the last 5 f | |

Lint 0 errors, 0 warnings (12 notes). Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs.

## Steps
1. Place and apply. Replace the icon shapes with partner logos you are allowed to use (keep each inside the 120 px tile) and the hub mark with your logo.
2. Fewer apps: delete a tile, its icon, link and both pulses. Keep the rest evenly spaced around the ellipse.
3. Edit the headline (about 38 characters at 44 px).

## Pitfalls
- The links start at the hub's centre and are drawn **below** the hub and the tiles, so they appear to leave the hub's edge without any trimming maths.
- Stand-in icons are deliberately plain shapes: a red right-pointing triangle on a white tile reads as a well-known video brand, so the first build's triangle became a diamond.

Inspiration: integration diagrams on SaaS marketing pages. No external text or code was used.
