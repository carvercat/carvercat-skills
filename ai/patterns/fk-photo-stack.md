# Photo stack

**Template** `fk_photo_stack` · Funky pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FK Photo stack` in `categories/funky/fk-lab-2`.

Three white 420 × 500 px photo frames (ink outline, soft shadow) tilted −9°, +5° and −3°, each with a 360 px coloured picture area. 120 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Photo 1–3 and Picture 1–3 | 0, 10, 20 | Slide in - wiggle | angle **30.3%**; Photo 1 settles **f19**, Photo 3 **f39** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Replace each Picture with an image masked by it (`property.set {id:"image", key:"mask", value:{"ref":"<picture id>"}}`, then `parent.clear {ids:[picture, image]}`), and give the image the same preset and start.

Inspiration: scrapbook photo collages. No external text or code was used.
