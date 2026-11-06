# Soft edge and mask feather

A soft edge turns a hard shape outline into a gradual ramp. A shape has **one** `softEdge`, and it softens the fill and the stroke together; `feather` is the same thing on a shape that is a mask. Both are **px**, and the number is the **visible ramp**: the distance over which the edge rises from 10 % to 90 %, centred on the shape's edge (measured: 8 / 24 / 60 px set gave 8.07 / 24.07 / 59.88 px, for 500, 800 and 1200 px wide shapes alike). The Gaussian behind it has a sigma of px / 2.563. It does not depend on the shape's size, so `softEdge: 24` is a 24 px ramp on any shape, and it looks the same at every canvas zoom. It lives in the object's own space, so the object's `scale` multiplies it (scale 2 gives a 48 px ramp; verified: one-soft-edge-old-name-and-scale). Range 0 to 0.2 x the frame width (384 px at 1920).

| key | on | what it softens |
|---|---|---|
| `softEdge` | rect, ellipse, polygon, star, path | the fill and the stroke, as one shape |
| `feather` | a shape that is a mask over another object | the matte's edge, so the masked picture fades in over `feather` px |

`strokeSoftEdge` is an **old name** for `softEdge`, still accepted for one release: setting it sets `softEdge` and the reply carries `units.deprecated` = `{use: "softEdge"}`. There is no separate stroke value any more; an old project whose fill and stroke had different values opens with the larger one.

`feather` on anything that is not a mask is refused and points at `softEdge`. A picture or text used as a mask has no feather; use a shape.

Carve status (stated in every reply and by `carve.preflight`): **Resolve exact** (a Fusion Blur of the shape before the matte). **After Effects approximate**: a Gaussian Blur on the layer (on the matte layer for `feather`), blurriness 3.55 per px of sigma, Repeat Edge Pixels off. In After Effects a scaled layer scales its blur (Carvercat's does not), the layer blur softens fill and stroke together (the same as Carvercat now, with one value), and the blur is not clipped to the layer as a native After Effects mask feather is. Run `carve.preflight {host: "aftereffects"}` and expect `approximate` on these keys.

## Set it

```json
{"command": "property.set", "args": {"id": "#glow", "key": "softEdge", "value": 240}}
{"command": "property.set", "args": {"id": "#ring", "key": "softEdge", "value": "6px"}}
{"command": "property.set", "args": {"id": "#wipe", "key": "feather", "value": 60}}
```

`softEdge` also goes in a scene node's `style` or in `object.new {style}`.

## Typical values (1920 wide)

| Use | Value |
|---|---|
| A slightly soft card or UI edge | 2 to 6 px |
| Soft shadow built from a shape | 20 to 40 px |
| Feathered wipe edge, soft reveal | 40 to 120 px |
| Ambient glow blob, bokeh, light behind a hero | 160 to 320 px (up to 384) |
| Vignette inner edge (`softEdge` on the dark ring) | 200 to 300 px |

Keep the value under about half the shape's smaller side or the shape is eaten. The value is in frame px, so a small object needs a small number.

## Recipe: soft glow and vignette (verified: soft-glow-and-vignette)

A large ellipse at reduced opacity with a big soft edge lights the background; a dark stroke ring just outside the frame gives a vignette.

```json
{"command": "scene.apply", "args": {"scene": {"schema": "carvercat/2.0",
 "comp": {"width": 1920, "height": 1080, "fps": 30, "duration": "3s"},
 "children": [
  {"id": "bg", "type": "rect", "style": {"x": 0, "y": 0, "width": 1920, "height": 1080, "fill": "#0d0d14"}},
  {"id": "glow", "type": "ellipse", "style": {"x": 560, "y": 140, "width": 800, "height": 800, "fill": "#7a5cff", "opacity": 0.55, "softEdge": 240}},
  {"id": "t", "type": "text", "text": "Glow", "style": {"x": 360, "y": 440, "width": 1200, "height": 200, "fontSize": 160, "fontWeight": 800, "fill": "#ffffff", "whiteSpace": "normal", "textAlign": "center"}},
  {"id": "vignette", "type": "rect", "style": {"x": -200, "y": -200, "width": 2320, "height": 1480, "fill": "none",
     "stroke": "#000000", "strokeWidth": 360, "strokeAlign": "inside", "softEdge": 260, "opacity": 0.8}}
 ]}}}
```

`carve.preflight aftereffects` lists `softEdge` as approximate; Resolve lists none. For a glow that follows the text itself, use `glow` ([glow.md](glow.md)).

## Recipe: feathered mask reveal (verified: feathered-wipe)

A window shape becomes the mask over a title; its edge is feathered, then it travels across, so the text appears behind a soft leading edge.

```json
{"command": "property.set", "args": {"id": "<title id>", "key": "mask", "value": {"ref": "<wipe id>"}}}
{"command": "property.set", "args": {"id": "<wipe id>", "key": "feather", "value": 60}}
{"command": "parent.clear", "args": {"ids": ["<wipe id>", "<title id>"]}}
{"command": "anim.set", "args": {"id": "<wipe id>", "keyframes": [
  {"at": 0, "x": -1260, "ease": "ease-in-out"}, {"at": "1.5s", "x": 360}]}}
```

- Object ids come from the `ids` map of the `scene.apply` reply (`{"wipe": "clip_3"}`); `mask` takes an object id, not a selector.
- The mask must be on another track than its target. Making the mask parents it to the target; `parent.clear` lets it move on its own, and its `x`, `y` are frame px again.
- Start the window fully clear of the text: the window here is 1200 px wide at rest `x` 360; start at its resting x minus its width minus the feather, or further left, so the soft edge has not entered yet.
- `ease-in-out` for a reveal that is read, `ease-out` for a quick wipe; 24 to 45 frames.
- Look at frames 12, 22 and 40: the leading edge is a soft ramp, not a line.
- To cut by a CSS shape use `clipPath` (`inset(0 40% 0 0 round 40px)`, `circle(...)`, `polygon(...)`): it makes the mask shape on a new track for you, and that shape can then be feathered with `feather` (verified: clip-path-reveal).
- `feather` is exact in Resolve and approximate in After Effects.

## Animating the soft edge or the feather (verified: keyed-soft-edge-feather-blur-trim, keyed-feather-wipe)

A shape that condenses into focus, a glow that breathes, a feather that tightens as a wipe lands: `softEdge` 300 -> 0 with `opacity` 0 -> 1. `softEdge` and `feather` are keyable by name in `anim.set`, `key.set` and a scene node's `keyframes`:

```json
{"command": "anim.set", "args": {"id": "#glow", "keyframes": [
  {"at": 0, "softEdge": 300, "opacity": 0, "ease": "ease-out"}, {"at": "0.8s", "softEdge": 0, "opacity": 1}]}}
{"command": "anim.set", "args": {"id": "#wipe", "keyframes": [
  {"at": 0, "feather": 120, "ease": "ease-out"}, {"at": 30, "feather": 20}]}}
```

`key.remove {id, key: "softEdge", at: 0}` takes a key off by name. A keyed soft edge carves as a baked spline in Resolve and as a keyed blur in After Effects.

## Soft edge or blur

| Soft edge | Blur |
|---|---|
| feathers only the outline; the inside stays solid | smears the whole object |
| cheap, exact in Resolve | exact in Resolve, approximate in After Effects too |
| light blobs, vignettes, feathered masks, shape shadows | focus pulls, depth of field |

## Pitfalls

- The value is in frame px, not relative to the shape: the same 40 px is a huge feather on a 60 px icon and a subtle one on a 900 px card.
- A soft or feathered shape that animates in scale animates its ramp with it; read the preflight note for After Effects and look at the transfer.
- A scaled shape scales its soft edge (in Carvercat, Resolve and After Effects alike); size the number for the scale the shape ends at, or key `softEdge` against `scale`.
