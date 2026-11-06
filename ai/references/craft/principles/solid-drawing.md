# Solid drawing (form and depth)

**What it does:** shapes keep their volume, weight and three-dimensional sense as they move. In motion graphics that means consistent forms, believable light and depth, and volume-keeping deformation.

## How in Carvercat
- **Keep volume** when squashing: x·y within about 10% of 1 ([squash-and-stretch.md](squash-and-stretch.md)).
- **One light:** one shadow direction, softness and opacity for the whole film (native Drop shadow; e.g. SaaS cards `y −0.004, softness 0.02, opacity 0.22–0.3`).
- **Contact:** a flat ellipse shadow under anything that touches the ground; it shrinks and fades with height.
- **Depth:** nearer moves faster (parallax 1.5–2×), and at most three speeds in a frame.
- **Clean geometry:** build shapes at the size they are seen (drawn ≤ 1000 px and scaled up is cropped before scale, [KI-137](../../known-issues.md#ki-137)); pills from round-capped strokes, not corner radius.

## Measured examples
| Template | Device |
|---|---|
| Character hop ([ct-character-hop.md](../../../patterns/ct-character-hop.md)) | volume 0.92–1.02 through crouch, launch, land; shadow 100 → 55% at the peak |
| Bouncing ball ([ct-bouncing-ball.md](../../../patterns/ct-bouncing-ball.md)) | shadow scale and opacity follow the height |
| Photo stack ([fk-photo-stack.md](../../../patterns/fk-photo-stack.md)) | one hard drop shadow on every frame |
| Chrome title ([rt-chrome-title.md](../../../patterns/rt-chrome-title.md)) | a static gradient gives the type a lit, metallic form |
