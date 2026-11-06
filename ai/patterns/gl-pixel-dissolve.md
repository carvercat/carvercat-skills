# Pixel dissolve

**Template** `gl_pixel_dissolve` · Glitch pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `GL Pixel dissolve` in `categories/glitch/gl-lab-2`.

A transition: 84 blocks (12 × 7, 160 × 154 px, a dark checker) switch on in a random order, cover the frame, then switch off in the same order. 40 f.

| Part | Clip | Measured |
|---|---|---|
| Pixel 1–84 | each block is one clip: on between f2 and f16, off between f22 and f36 (seeded shuffle) | covered **f16–22** |

Lint 0 errors, 0 warnings; `inspect qc` (240 px) found no flashes. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place 19 f before your cut, above both scenes; cut at its f19.

## Pitfalls
- 155 px rows (7 × 155 = 1085) left the bottom row 4% off frame, and lint flagged `cropped_at_rest`. Rows are 1080 / 7 px with a 1 px overlap inside the frame only.
- Each block is a clip, not a keyed opacity, so 84 objects carry no keys at all.

Inspiration: pixel-dissolve transitions of early video systems. No external text or code was used.
