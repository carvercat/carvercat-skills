# Effects, paint and shape craft: index

Read this when you need any visual treatment beyond plain fill: blur, glow, shadow, motion blur, grain, directional blur, gradients, strokes, dashes, trim draw-ons, soft edges, text outlines, stagger, blend modes, masks, or the basement (unpromoted parameters, promotion, ropes).

Everything here is written in design units ([../app/design-units.md](../app/design-units.md)): px, `%`, CSS colours, CSS easing. Every call sequence is run against a real headless Carvercat by `ai/scripts/verify_examples.py`, and a guide says "verified: <case-name>" under each one. Every recipe holds on Carvercat 0.1.8 or later. Numbers that were measured on the stored parameters of Carvercat 0.0.72 (rev 1071) in the lab project (`categories/motion-patterns/pattern-lab/project.carverproj`, comps whose names start with `FX`/`RIG`) say so; they are restated in px where the arithmetic is exact.

| Need | Guide | Lab comp |
|---|---|---|
| Soft focus, blur-in/out, depth | [blur.md](blur.md) | FX Blur Glow Soft |
| Neon, light, bloom **without burning** | [glow.md](glow.md) | FX Glow grid, FX Glow calibration |
| Depth, lift, cards | [shadow.md](shadow.md) | FX Shadow Gradient Stroke |
| Speed on fast moves (follows the object's keys) | [motion-blur.md](motion-blur.md) | FX Shadow Gradient Stroke |
| Speed streaks you aim: whips, slams, pushes | [directional-blur.md](directional-blur.md) | none |
| Film grain, tape and digital noise | [grain.md](grain.md) | none |
| Gradients and shimmer sweeps | [fill-and-gradients.md](fill-and-gradients.md) | FX Shadow Gradient Stroke |
| Strokes, dashes, caps, draw-on (trim) | [stroke-and-trim.md](stroke-and-trim.md) | FX Shadow Gradient Stroke |
| Soft (feathered) shape edges | [soft-edge.md](soft-edge.md) | FX Blur Glow Soft |
| Text fill, outline, hollow type | [text-paint.md](text-paint.md) | FX Shadow Gradient Stroke |
| Per-word/letter animation | [stagger.md](stagger.md) | Text Lab |
| Blend modes, masks, mattes, colour | [compositing-and-masks.md](compositing-and-masks.md) | none |
| Basement: hidden params, promote, raise to a comp face, ropes (wires) | [basement-promote-ropes.md](basement-promote-ropes.md) | FX Basement Ropes |
| Every parameter, range and default; which design key each stored parameter belongs to | [PARAMETERS.md](PARAMETERS.md) (generated) | none |

## The design commands (all effects)

```json
{"command": "property.set", "args": {"id": "#title", "key": "blur", "value": "8px"}}
{"command": "property.set", "args": {"id": "#title", "key": "glow", "value": "12px #ffcc00 0.6 0.2"}}
{"command": "property.set", "args": {"id": "#card", "key": "dropShadow", "value": "0 6px 12px #00000059"}}
{"command": "property.set", "args": {"id": "#title", "key": "brightness", "value": 1.2}}
{"command": "property.set", "args": {"id": "#film", "key": "grain", "value": "0.25 1.5px"}}
{"command": "property.set", "args": {"id": "#panel", "key": "directionalBlur", "value": "40px 30deg"}}
{"command": "property.set", "args": {"id": "#flare", "key": "mixBlendMode", "value": "screen"}}
{"command": "property.set", "args": {"id": "#title", "key": "blur", "value": "none"}}
```

Verified: effects-in-css-terms, blur-focus-pull, glow-presets-and-pulse, shadow-card-lift, grain-design-units, directional-blur-design-units.

| Key | Value | Range |
|---|---|---|
| `blur` | px, a Gaussian sigma (the visible edge ramp is 2.563 x px) | 0 to 115 x W/1920 px; a `%` is refused |
| `glow` | `"radius [colour] [strength 0-1] [mix 0-1]"` (strength 0.8, mix 0.2 when left out) | radius 0 to 115 x W/1920 px |
| `dropShadow` | `"dx dy blur colour"`, **y down**, blur a sigma, colour with alpha | `abs(dx)` at most W/2, `abs(dy)` at most H/2, blur at most 166 px at 1920 |
| `grain` | `"amount [size] [softness=] [colour=] [held] [seed=]"` or an object | amount 0 to 1, size 0.5 to 8 px of a 1920 frame, softness and colour 0 to 1, seed 0 to 9999; [grain.md](grain.md) |
| `directionalBlur` | `"length [angle]"` or `{length, angle}` | length 0 to 500 px of a 1920 frame, angle -360 to 360 deg counter-clockwise from the right; [directional-blur.md](directional-blur.md) |
| `brightness`, `contrast` | a factor (`1.2` or `"120%"`) | brightness 0 to 3, contrast 0 to 2 |
| `mixBlendMode` | one of 16 CSS names | see [compositing-and-masks.md](compositing-and-masks.md) |
| `filter` | a CSS list (`"blur(4px) grain(0.2 2px) directional-blur(40px 30deg) brightness(1.2)"`): blur, drop-shadow, glow, grain, directional-blur, brightness, contrast | replaces the effects of its kinds |
| `mask`, `clipPath`, `feather` | an object id, a CSS shape, px | see [compositing-and-masks.md](compositing-and-masks.md), [soft-edge.md](soft-edge.md) |
| `none` | on any of the above | removes it |

Each is also a `style` key of a scene node and of `object.new {style}`. `carve.preflight` says per key what carves `exact`, `approximate` or `unsupported`.

## Keying effects by design name

Every number here is keyable by its design name in `anim.set`, `key.set` and a scene node's `keyframes`: `blur`, `glow`, `dropShadow`, `grain`, `directionalBlur`, `brightness`, `contrast`, `softEdge`, `feather`, `borderRadius`, `strokeWidth`, `trimStart`, `trimEnd`, `trimOffset` (verified: keyed-blur-focus-pull, keyed-glow-shadow-brightness, keyed-trim-write-on-and-off, keyed-stroke-width-and-border-radius, keyed-feather-wipe, keyed-soft-edge-feather-blur-trim). The `ease` is a CSS curve; `property.get` on the design key reads the value at the playhead in px; `key.remove {id, key, at}` takes a key off by name; `anim.get` and `key.list` read them back. `property.set` of an animated property writes one key at the playhead on that property only, so use `anim.set` or `key.set {at}` when you mean a whole move. A keyword or a count (`strokeLinecap`, `mixBlendMode`, `fontWeight`) is not keyable: it is refused with the reason.

The stored route (`key.set {key: "fx.<entry>.<param>"}`, the conversions in [PARAMETERS.md](PARAMETERS.md) under "Design names") still works and is how you reach what the design keys do not cover; `param.list {id, match: "blur"}` prints the entry path (`fx.e_fx_blur_clip_3`). Each guide gives the design-name recipe first and the stored route after it.

## Mechanics of the stored route (all effects)

These commands still work for one release and are how you reach what the design keys do not cover (motion blur, secondary glow, stagger, the basement).

1. `effect.addable {id}` lists what the object can take (a shape: Fill, Stroke, Gaussian blur, Drop shadow, Glow, Grain, Directional blur, Colour, Motion blur, Trim Stroke; a text: the same minus Trim Stroke plus Stagger Text; verified: stagger-preset-apply). `effect.add {id, cap}` with cap `blur | glow | shadow | grain | dirblur | motionblur | trim | fill | stroke | colour` (`crop`, `expand`, `outline`, `transform` and `stylelayer` are not offered on a shape or a text in this build). Stagger Text is `stagger.new`. Setting a design key (`blur`, `glow`, `dropShadow`, `grain`, `directionalBlur`, `trimEnd`, `brightness`) adds the effect for you.
2. In a batch give it an alias: `{"command":"effect.add","args":{"id":"clip_3","cap":"glow"},"as":"g"}`; later steps address its parameters as `{"$param":["g","amount"]}` (in `property.set` and `key.set` `key`). The reply maps aliases to entry prefixes (`fx.e_fx_glow_clip_3`).
3. Outside a batch use the stored path: `fx.e_fx_<cap>_<clip>.<param>` (check with `param.list {id}`).
4. Several of the same effect on one object are separate entries; address them by path, never by cap.
5. `effect.enable {entry, on}` bypasses without deleting; `effect.remove {entry}` deletes. Order matters (`effect.up/down`).
6. Values out of range refuse the whole batch; the ranges of the stored parameters are in [PARAMETERS.md](PARAMETERS.md).
7. **Look at effects on full-frame looks.** `carvercat_look {region}` and `{object}` crops drew backgrounds and some layers wrongly on 0.0.72 (not re-checked on this build); judge effects on uncropped sheets (or `carvercat_render` plus pixels).
