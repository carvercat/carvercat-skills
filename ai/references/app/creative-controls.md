# Effects, paint and transforms through MCP

Read creative-toolkit.md first. All native commands and parameters remain accessible through Client.run/Scene.command/Scene.set/Scene.keys; the convenience methods do not limit what can be authored. native-controls.json is a generated capability/parameter/type/range/default/enum/keyframe snapshot from the matching app registry. It is discovery data, not proof every declared control renders natively. Use Scene.bindings(name) for actual bindings/values/units, and Scene.parameters(name) for panel/promotion state and inspect actual output. Refresh with tools/build_native_controls.py --app PATH; --check detects drift.

## Native effect instances

```python
scene.blur("card", size=2, alias="soft edges")
scene.blur("card", size=5, alias="exit blur")
scene.glow("path", size=14, amount=.9, blend=.3, alias="path light")
scene.shadow("card", x_px=10, y_px=12, softness_px=16,
             opacity=.38, color="#000000", alias="card depth")
scene.trim_path("path", alias="reveal")
scene.fx_keys("reveal", "end", [(0, 0), (30, 1)])
scene.apply()
scene.fx_set("exit blur", "size", 8)  # only this entry changes
scene.apply()
```

effect(name, cap, alias=..., properties={...}) is the generic path for any native addable effect, including fill, stroke, blur, glow, shadow, motionblur and trim. It creates the effect through effect.add, discovers the actual new entry and returns its native prefix. fx_set/fx_keys target the exact entry and promote the selected parameter if needed. No generated entry IDs are constructed. Repeated caps are intentionally distinct; the ambiguous generic blur.size key is not used for duplicates. remove_effect removes only that named entry. Effects and owner maps are saved in Scene manifests and checked through native reopening.

In a single raw MCP batch, effect.add has explicit args.id and optional as. Later property/key arguments use {"$param":["effect_alias","size"]}. The batch returns separate aliases for objects and effects; effect aliases are native fx entry prefixes, never object IDs. Unknown aliases/properties abort the document plan. Use an existing stored prefix when patching a saved effect. Dry-run entries do not survive and must not be retained.

Blur/glow size stays in the documented native filter control units. Filter choice and image resolution affect the resulting support: do not call it a Gaussian pixel radius. Shadow offsets accept comp pixels, converted per X/Y axis with native y-up; softness_px is a nominal width-normalized softness control, not a promised support radius. Probe effect_spread and actual looks measure the visible result. Motionblur uses native shutter degrees/samples and the object's own motion, not optical flow.

## Fill, stroke, gradients and colors

```python
from cc_scene import gradient
scene.paint("card", mode="gradient",
            gradient=gradient([(0,"#31566A"),(1,"#B48EAD")]))
scene.paint("card", layer="shape.stroke", mode="gradient", width_px=8,
            gradient=gradient([(0,"#EBCB8B"),(1,"#88C0D0")]))
scene.paint("path", mode="none")
scene.paint("path", layer="shape.stroke", mode="solid",
            color="#EBCB8B", width_px=9)
```

Use shape.fill/shape.stroke for shape paint, text.fill/text.outline for text paint; paint(width_px=...) maps text.outline to its native thickness relative to the text size, and shape.stroke to a fraction of comp width. Text outline width denotes the whole stroke band; an overlapping fill may hide its inner half. Other native controls use the exact parameter from discovery. Generic set/keys also exposes fill/stroke opacity, soft edges, line/cap/dash choices, gradient properties and text-relative paint controls when native availability permits. Paint selectors may be writable despite absence from param.list; their canonical declared capability key is authoritative and the native command still validates it. Unavailable or unmapped controls must not be assumed to render: validate the live availability and actual native look. There is no invented fallback renderer.

Hex colors convert with the established BT.709 transfer curve used by the app's agent contract. #RRGGBBAA separates alpha/opacity appropriately. Gradient stops have positions 0..1 and independent alpha; coordinates are normalized object-local values, not comp positions. gradient supports native linear/radial modes. Stroke widths use comp pixels divided by comp width. Do not linearize a value twice or confuse position coordinates with gradient coordinates.

## Position, transform and animation

transform accepts pixel position, native dimensionless XY scale, degrees rotation, opacity 0..1 and native anchor fractions of the object half-size (x right, y up; not fractions of comp size). position converts top-left/y-down to the native center's normalized/y-up coordinates. keys accepts any native/discovered property path; fx_keys accepts exact effect entries. Explicit comp frames, duplicate-frame deduplication, cubic handles and revision checks apply to all these channels, not only opacity. entrance preserves the authored base scale (important for cover-fitted images) instead of resetting everything to scale 1.

## Stagger text and path trim

stagger creates the native Stagger Text card, connects explicit channels and sets word/character/line timing/order/gap. Example channels are text.position and fill.opacity; also discover stroke.opacity/stroke.blur and effect-size slots. The input vocabulary for stagger.connect differs from property capability paths: use its live schema. Animate the intended relative-text/fill channels, inspect stagger.list and key.list, then look at entrance/hold/exit samples. An outline needs its own opacity connection if it must reveal with fill. Stagger is a specialized native card, not fabricated per-word objects.

path takes pixel points and converts to native path fractions with y-down, unlike clip position. trim_path adds native Trim Stroke and fx_keys animates start/end/offset. Preserve the authored open/closed path and fill/stroke choices; a reveal on a filled shape is not the same design as a stroke reveal.

For revisions, replace_keys deliberately replaces one property animation; patch/keys otherwise preserve unmentioned keys. extend_hold deliberately reconciles the named placement and relative-text opacity channels only. Other fill/outline/stagger/effect visibility channels are discovered and reviewed, never silently cleared.

## Evidence and limits

The native effects fixture covers gradient fill/stroke, transformed card, repeated blur targeting and animation, glow, shadow, trimmed open path, stagger text, baseline placement, invalid-parameter rollback, targeted removal and native save/reopen. Actual samples were inspected. The full declaration catalog is broader than this representative test fixture; do not claim every parameter/filter combination or Resolve equivalence was pixel-verified.


## Discovery corrections and transfer limits

fx_set/fx_keys no longer promote every parameter blindly. Existing controls are validated through native discovery; promotion occurs when requires_promotion is true or explicitly requested. Pending effect creation uses matching registry hints, followed by native atomic validation. A declared row is not proof that a native binding exists.

Repeatable Stroke opacity is stored and rendered, but absorbed into Colour and intentionally has no separately promotable row. An earlier failure was a promotion failure, not an absent writable scalar. Direct fx_set(alias, "opacity", .5) is supported. fx_color(alias, "#D5B067", alpha=.4) writes RGBA explicitly; alpha and standalone opacity multiply. Colour keyframes and scalar keyframes remain different tracks.

Text gradientStart/gradientEnd writes still refuse because those separate properties are not live. Static packed gradient data is supported; do not advertise separate native endpoint tracks or full Resolve gradient equivalence. Newer builds transfer animated shape endpoints and numeric effect tracks, fixes nested clock shifts and single-factor scale easing, and preserves Fill coverage. Remaining text-gradient mapping, halo/glyph-edge, two-factor subframe scale and RGBA-effect animation parity are documented, not certified.

## Library paint faces

A native gradient is a mode inside the visible Colour picker, not a separate panel row. A reusable gradient face needs both the source Colour and Gradient channels handed up. Raising only Gradient preserves a stored control but hides the visible picker; raising only Colour leaves the actual palette unavailable. Keep both, and inspect the native parent panel. For MCP edits inspect the active paint mode: a gradient is recoloured through its packed gradient/stops, while the stored solid colour remains a reference for switching back to Solid. Do not report a successful write to that inactive reference as recolouring the rendered gradient.
