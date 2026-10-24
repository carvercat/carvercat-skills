# UI card stack

**Recipe** · **verified 0.0.72** (`RECIPES`, frames 100–150)

Three rounded cards pop in left to right, 4 f apart. The hero card (accent colour) arrives last, with more spring.

| Card | Clip start | Preset | Angle |
|---|---|---|---|
| 1 | 100 | Pop - gentle | +4° |
| 2 | 104 | Pop - gentle | 0° |
| 3 (hero) | 108 | Pop - spring (16%) | −4° |

Geometry: rectangle width 0.2 W, height 0.26 W, `cornerRadius` 0.012. The centres are 0.14 W apart, so each card overlaps the next by about 30%.

## Steps

1. Create each card **with the batch step's `frame`** (`{"command":"object.new","args":{...},"frame":104}`), NOT `object.new` followed by `clip.move`. See the pitfall below.
2. Set the colour, geometry, `center` and `angle`, then run `preset.apply` on each card, one call each.

## Cards with labels
Style the card AND its text fully, then `edit.group {ids:[card, label]}` and apply the preset to the GROUP so they move as one (verified: Pop, Exit zoom through and position keys all work on groups). After grouping, children are outside the batch's editing scope — change them with `object.enter {id: group}` → edit → `object.exit` (not batchable).

## Pitfall that cost us a rebuild

`clip.move` is an **overwrite edit**. Moving a clip onto a track where another clip already sits trims that clip or deletes it, silently. `object.new` without a `track` picks "a track with room" at the PLAYHEAD, so a series of object.new + clip.move calls can stack onto one track and destroy each other. Either use the step's `frame`, which places the clip and picks a free track for that span, or pass an explicit empty `track`.
