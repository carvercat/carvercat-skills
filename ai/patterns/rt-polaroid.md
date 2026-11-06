# Polaroid memory

**Template** `rt_polaroid` (Library name "Polaroid memory") · Retro pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `RT Polaroid` in `categories/retro/rt-lab-3`.

For briefs like "throwback photo", "family memory", "on this day", "our story began in 1979". An instant photo (white frame with a soft shadow, a square picture, "Summer '79" written on the strip, a strip of tape) drops in from above, tilting, as one piece on twos; the picture develops from dark; a heading, a line and a rule come in on the right. 150 f, overlay. The picture is a gradient stand-in (sky at the top, warm at the bottom); replace it with a photo.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Polaroid frame, Photo, Photo label, Developing, Caption, Tape (one rigid group) | 0 | `group2()`: centre from 140 px right and 700 px up, rotate −14° → 4° (stored angle 14° → −4°; the tape rotate −6°, stored +6°, on top), expo, on twos | lands **f10** (0%) |
| Developing (dark 520 px square over the photo) | 0 | opacity 1 → 0, the decelerating arrival curve cubic-bezier(0.333, 0.667, 0.667, 1), f20–90, smooth (not stepped) | clear by **f84** |
| Photo label | 0 | opacity 0 → 1, f40–70 | |
| Heading (ExtraBold 88 px, brown) | 34 | Rise - on twos | **f44** |
| Line (Medium 48 px, red) | 42 | the same | **f52** |
| Rule (320 × 8 px, orange) | 50 | grows from the left on twos | **f58** |

Lint 0 errors, 0 warnings in the lab (10 notes: `speed_jump` on the stepped drop, and `outside_graphics_safe` at f1 while the caption is still above the frame); placed 0/0/0. `inspect qc`: no flashes. Text-gap audit: closest pair 50.8 px (heading and line). Full-frame looks of the placed instance at f2 and f6 (the photo coming in over the top edge) show nothing cut that should not be.

## Steps
1. Replace `Photo` with a picture (same 520 px square) and keep `Developing` above it.
2. Edit the caption; keep it under about 440 px at 58 px.

## Pitfalls
- Parts of one object turned with their own rotation keys each turn about their own centre and fall apart. `group2()` writes each part's position, angle and size from one shared centre, so the polaroid turns as one piece without parenting ([KI-153](../references/known-issues.md#ki-153)).
- `group2()` skips lanes that never change (scale here): constant Hold keys are `repeated_key_value` notes.

Inspiration: instant-film snapshots and family albums. No external text or code was used.
