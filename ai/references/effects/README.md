# Effects, paint and shape craft: index

Read this when you need any visual treatment beyond plain fill: blur, glow, shadow, motion blur, gradients, strokes, dashes, trim draw-ons, soft edges, text outlines, stagger, blend modes, masks, or the basement (unpromoted parameters, promotion, ropes).

Every guide says **what was verified on Carvercat 0.0.72 (rev 1071)** in the lab project (`categories/motion-patterns/pattern-lab/project.carverproj`, comps whose names start with `FX`/`RIG`), and marks the rest "not verified".

| Need | Guide | Lab comp |
|---|---|---|
| Soft focus, blur-in/out, depth | [blur.md](blur.md) | FX Blur Glow Soft |
| Neon, light, bloom **without burning** | [glow.md](glow.md) | FX Glow grid, FX Glow calibration |
| Depth, lift, cards | [shadow.md](shadow.md) | FX Shadow Gradient Stroke |
| Speed on fast moves | [motion-blur.md](motion-blur.md) | FX Shadow Gradient Stroke |
| Gradients and shimmer sweeps | [fill-and-gradients.md](fill-and-gradients.md) | FX Shadow Gradient Stroke |
| Strokes, dashes, caps, draw-on (trim) | [stroke-and-trim.md](stroke-and-trim.md) | FX Shadow Gradient Stroke |
| Soft (feathered) shape edges | [soft-edge.md](soft-edge.md) | FX Blur Glow Soft |
| Text fill, outline, hollow type | [text-paint.md](text-paint.md) | FX Shadow Gradient Stroke |
| Per-word/letter animation | [stagger.md](stagger.md) | Text Lab |
| Blend modes, masks, mattes, colour | [compositing-and-masks.md](compositing-and-masks.md) | — |
| Basement: hidden params, promote, raise to a comp face, ropes (wires) | [basement-promote-ropes.md](basement-promote-ropes.md) | FX Basement Ropes |
| Every parameter, range and default | [PARAMETERS.md](PARAMETERS.md) (generated) | — |

## Common mechanics (all effects)
1. `effect.addable {id}` lists what the object can take. `effect.add {id, cap}` with cap `blur | glow | shadow | motionblur | trim | fill | stroke | colour | transform | crop | outline | expand | stylelayer` (Stagger Text is `stagger.new`).
2. In a batch give it an alias: `{"command":"effect.add","args":{"id":"clip_3","cap":"glow"},"as":"g"}`; later steps address its parameters as `{"$param":["g","amount"]}` (in `property.set` and `key.set` `key`). The reply maps aliases to entry prefixes (`fx.e_fx_glow_clip_3`).
3. Outside a batch use the stored path: `fx.e_fx_<cap>_<clip>.<param>` (check with `param.list {id}`).
4. Several of the same effect on one object are separate entries; address them by path, never by cap.
5. `effect.enable {entry, on}` bypasses without deleting; `effect.remove {entry}` deletes. Order matters (`effect.up/down`).
6. Values out of range refuse the whole batch — ranges are in PARAMETERS.md.
7. **Look at effects on full-frame looks.** `carvercat_look {region}` and `{object}` crops drew backgrounds and some layers wrongly on 0.0.72; judge effects on uncropped sheets (or `carvercat_render` + pixels).
