# Blend modes, masks, mattes and colour

## Blend modes: `mixBlendMode`
One of the 16 CSS names: `normal`, `screen`, `multiply`, `overlay`, `soft-light`, `hard-light`, `color-dodge`, `color-burn`, `darken`, `lighten`, `difference`, `exclusion`, `hue`, `saturation`, `color`, `luminosity`. Not keyable. `plus-lighter` is refused (`bad-value`). `combine` is NOT live (0.0.72). Verified: blend-modes-masks-and-colour (all 16 set and read back).

```json
{"command": "property.set", "args": {"id": "#flare", "key": "mixBlendMode", "value": "screen"}}
```

| Use | Mode |
|---|---|
| light leaks, glows, flares, bokeh over dark | `screen` (or `lighten`) |
| shadows, paper/grain textures, darkening | `multiply` |
| texture/grain overlay keeping contrast | `overlay` / `soft-light` |
| colour-tinting a layer | `color` / `hue` |

**Measured on this build (verified: blend-modes-blend-in-linear-light): the modes blend in linear light, not in a browser's sRGB code values.** A `#808080` layer over `#ff7a00` gave `multiply` (128, 55, 0) where CSS gives (128, 61, 0), `screen` (255, 168, 128) and `overlay` (255, 85, 0). Plan on results close to, not equal to, a browser preview. Carve: exact in both hosts per `carve.preflight`.

## Masks: `mask` on the object to cut
```json
{"command": "property.set", "args": {"id": "#photo", "key": "mask", "value": {"ref": "<window id>", "invert": false}}}
{"command": "property.set", "args": {"id": "#photo", "key": "mask", "value": "none"}}
```
`mask` takes the mask object's id (`"clip_7"`, `"#clip_7"`, `"url(#clip_7)"`, or `{ref, invert}`; an id from the `ids` map of `scene.apply`, not a selector) and makes that object the mask over this one; `none` clears it. The mask must be on another track than its target; an object cannot mask itself (`not-settable`).

Verified (mask-and-invert, by pixels): `{ref}` shows the photo only inside the window; `invert: true` cuts a hole instead. `none` clears the invert flag too: after an inverted mask, `none` and then `{"ref": window}` with no `invert` is a normal mask (old builds kept the flag, so older guides said to always write `invert`; writing it is still harmless). One trap, measured:
- A mask over an object that is already masked by it is refused ("those tracks are already covered"), even to change `invert`: clear with `none` first.

Making the mask parents it to the target (its `x`, `y` then count from the target's top-left, which is why the box moved in `measure.boxes`). For a reveal where the content moves behind a still window (rolling digits, rule reveals), or a wipe where the mask moves over still content, run `parent.clear {ids: [mask, target]}` after (its `x`, `y` are frame px again). A feathered mask is `feather` on the mask shape ([soft-edge.md](soft-edge.md)); `feather` is keyable by name in `anim.set` (verified: keyed-feather-wipe), for a feather that tightens as the wipe lands; move the mask shape for the wipe itself.

- **`clipPath`** cuts by a CSS shape and makes the mask shape for you: `inset(0 40% 0 0 round 40px)`, `circle(150px at 50% 50%)`, `ellipse(rx ry at x y)`, `polygon(...)` in the object's layout box. It adds a track and a shape and reports the mask; it refuses an object that is turned or scaled, four radii and `path()`; `none` ends the masks (verified: clip-path-reveal, blend-modes-masks-and-colour).
- Rounded image cards: `clipPath: "inset(0 round 24px)"` after the image has its cover scale; then animate only the image.
- Old route, still working for one release: `mask.make {ids: [mask, target]}`: the FIRST id becomes the mask (measured on 0.1.6 rev 1105: with ids `[rectangle, text]` the rectangle was the mask). The line that said "last id is the mask" was wrong for that build. With the old command, mask shapes must be on video rows and a wrong order masks the wrong way and renders blank; check the saved project for the clip with `isMask: true`. The SaaS UI rolling counter shipped with the old order and only looked right because its digits and windows were both white ([../../patterns/saas-ui.md](../../patterns/saas-ui.md) pitfall 3).

## Mask recipes
- **Text reveal from behind a line (the "slot" reveal):** a rectangle mask covering the area above a baseline; text rises from below into it.
- **Wipe reveal (verified: mask-wipe-and-iris):** mask the text with a rectangle, `parent.clear`, then animate the mask's `width` from 0 to its full width (it grows from its left edge):

  ```json
  {"command": "anim.set", "args": {"id": "<mask id>", "keyframes": [{"at": 0, "width": 0, "ease": "ease-in-out"}, {"at": 30, "width": 1200}]}}
  ```
- **Iris on real content (verified: mask-wipe-and-iris):** an ellipse mask, `parent.clear`, `scale` 0 to cover (`{"at": 0, "scale": 0}` to `{"at": 20, "scale": 3}` for a 400 px circle over a 1200 px title). See [../../patterns/tr-iris.md](../../patterns/tr-iris.md) for sizing limits.
- **Feathered wipe:** [soft-edge.md](soft-edge.md).

## Colour: `brightness`, `contrast`, adjustment layers
```json
{"command": "property.set", "args": {"id": "#photo", "key": "brightness", "value": 1.15}}
{"command": "property.set", "args": {"id": "#photo", "key": "contrast", "value": 1.1}}
```
They are one Colour effect (`gain`, `contrast`): `brightness` 0 to 3 (the stored gain), `contrast` 0 to 2 (the stored contrast is f - 1). **Contrast is not CSS-exact:** CSS pivots at the displayed mid grey, the app turns about linear 0.5; carve: Resolve approximate, After Effects unsupported (brightness only). `saturate`, `hue-rotate`, `invert`, `grayscale`, `sepia`, `backdrop-filter`, `opacity()` and `url()` in `filter` are refused with the reason (no node in either host). Both key by name in `anim.set` (verified: keyed-glow-shadow-brightness).

An **adjustment** node treats everything below it: a scene node `{"id": "grade", "type": "adjustment", "style": {"brightness": 1.2, "contrast": 1.1}}`; it reads back the same values (verified: adjustment-layer-colour). The older command route is `effect.add {cap: "colour"}` (`gain` 0 to 3, `contrast` -1 to 1) and `object.new {kind: "adjustment"}`.

## Other effect caps
`crop`, `expand` (grow/shrink the matte), `outline`, `transform` and `stylelayer` are declared in the registry ([PARAMETERS.md](PARAMETERS.md)) but `effect.addable` does not offer them on a shape or a text in this build (verified: stagger-preset-apply reads the list). They may exist on media; test with a look before relying on them.
