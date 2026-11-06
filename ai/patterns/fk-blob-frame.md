# Blob photo frame

**Template** `fk_blob_frame` (Library name "Blob photo frame") · Funky pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FK Blob frame` in `categories/funky/fk-lab-3`.

For briefs like "meet the team", "guest intro", "profile photo in a fun shape". A photo inside a blob-shaped mask window (7 smooth nodes, about 600 px), a purple blob offset 30 px behind it, an ink outline blob turning the other way, a MEET MIRA sticker and the role. 120 f, holds. The photo is a gradient stand-in; the name is invented.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Blob window (the mask, made with `property.set` key `mask`) | 0 | pop 0 → 1 on the pop curve, 14 f; then 0 → 30° linear (one way) | **15.8%**, **f13** |
| Photo (760 px gradient square) | 0 | slow push 1 → 1.06, linear | to f119 |
| Blob back (purple, +30 px) | 2 | pop; 0 → 30° | **15.8%**, **f15** |
| Blob ring (ink 8 px, 720 px) | 6 | pop; 0 → −30° (the other way) | **15.8%**, **f19** |
| Name sticker (yellow plate, ExtraBold 84 px) | 18 | stamp 1.45 → 1, turn into −4° | **9.3%**, **f26** |
| Role (ExtraBold 52 px, purple) | 30 | rise 24 px | **f37** |
| Sparks (two 4-point stars) | 26, 31 | Spin in, then ±40° | **9.8%**, **f44** (spark 2) |

Lint 0/0/0 in the lab and placed. Text-gap audit: closest pair 68.2 px (name / role). Full-frame looks of the placed instance at f30 and f119 show the photo fully inside the turning window ([KI-144](../references/known-issues.md#ki-144)).

## Steps
1. Replace the gradient square with the photo (at least 760 × 760 px, centred on the blob): the window reaches 341 px from the centre at most, so a 760 px picture never shows an edge while it turns.
2. Rebuild from `funky_lab3.py` to change the blob (`BLOB` radii); after `edit.open` run `property.set {id:"photo", key:"mask", value:{"ref":"<window id>"}}` and `parent.clear {ids:[window, photo]}`.

## Pitfalls
- The ink ring and the role are nearly invisible on a dark ground; keep a light ground or recolour them.
- Masked placement survives `comp_to_template.py`: the placed instance showed the photo inside the blob only.

Inspiration: organic blob frames in playful brand identities. No external text or code was used.
