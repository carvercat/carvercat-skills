# Blend modes, masks, mattes and colour

## Blend modes (`transform.compositing.blend`)
Normal, Screen, Multiply, Overlay, Soft Light, Hard Light, Color Dodge, Color Burn, Darken, Lighten, Difference, Exclusion, Hue, Saturation, Color, Luminosity (not keyframeable). `combine` is NOT live on 0.0.72.
| Use | Mode |
|---|---|
| light leaks, glows, flares, bokeh over dark | Screen (or Lighten) |
| shadows, paper/grain textures, darkening | Multiply |
| texture/grain overlay keeping contrast | Overlay / Soft Light |
| colour-tinting a layer | Color / Hue |
Status: modes are declared and set by `property.set {key:"tr.e_tr_compositing_<id>.blend", value:"Screen"}`; their rendering was not pixel-verified in this pass.

## Masks (verified in earlier jobs, 0.0.69+)
- `mask.make`: select the CONTENT first (`select.clip`), then `select.add` the SHAPE; the last-selected (active) object becomes the mask over the others. In a batch: `mask.make {ids:[target, mask]}` — last id is the mask.
- The mask shape hides itself AND parents the target to it: moving the mask drags the content. For a WIPE (mask moves, content stays) run `parent.clear {ids:[target, mask]}` afterwards.
- Mask shapes must be on video rows. Wrong order (shape first) masks the wrong way and renders blank.
- Rounded image cards: set the image's cover scale BEFORE `mask.make`; then animate only the image — the mask follows.
- `mask.invert`, soft-edged mask shapes for feathered wipes (declared; not verified here).

## Mask recipes
- **Text reveal from behind a line:** rectangle mask covering the area above a baseline; text rises from below into it (the "slot" reveal).
- **Wipe reveal:** mask rectangle scaleX 0 → 1 with anchor [−1,0], content unparented.
- **Iris on real content:** ellipse mask scale 0 → cover (see ../../patterns/tr-iris.md for sizing limits).

## Colour effect (`effect.add {cap:"colour"}`)
`gain` 0–3, `contrast` −1–1 — quick brightness/contrast on one layer (declared; not verified here). Use an **adjustment** object (`object.new {kind:"adjustment"}`) to treat everything below it.

## Other effect caps (declared, not verified in this pass)
`crop` (x, y, width, height), `expand` (amount −0.1–0.1: grow/shrink the matte), `outline` (thickness, length, start — an outline draw on any layer), `transform` (x, y, size, angle — an extra transform inside the effect stack), `stylelayer` (extra fill/outline/border layers with offset/blur — text-style layers). See [PARAMETERS.md](PARAMETERS.md). Test with a look before relying on them.
