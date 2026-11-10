# Blur

`blur` is a Gaussian sigma in px: `blur: 12` softens the edge over a ramp of 2.563 x 12 = 30.7 px (measured by the app on 6, 12 and 24 px: 2.558 to 2.561 x px). Range 0 to 115 x W/1920 px (115 px at 1920); a larger value is refused with that number, a `%` is refused. It does not depend on the object's size.

**Verified:** blur-in title (28 px to 0 over 18 f, opacity 0 to 1 over 9 f, scale 1.08 to 1) reads as a focus pull (verified: blur-focus-pull).

```json
{"command": "property.set", "args": {"id": "#title", "key": "blur", "value": "28px"}}
{"command": "property.get", "args": {"id": "#title", "key": "blur"}}
{"command": "property.set", "args": {"id": "#title", "key": "blur", "value": "none"}}
```

Carve: Resolve exact (a Fusion Blur), After Effects approximate (a Gaussian Blur, blurriness 3.55 per px of sigma). A scaled layer scales its blur in After Effects; Carvercat's does not.

## Controls
| what | design key | note |
|---|---|---|
| strength | `blur` px | the only design key. A new blur made by `effect.add` starts at 11.5 px; setting `blur` writes exactly what you give |
| a streak along one angle | `directionalBlur` px and deg | a blur is round (`blur(rx ry)` is not built); for a horizontal or any-angle smear use [directional-blur.md](directional-blur.md) (verified: blur-directional-and-depth) |
| mix with the sharp original | stored `blend` (a 0 to 1 factor, default 1) | 0.5 is a dreamy halo over a sharp core |
| spread past the object | stored `clipping` none / domain / frame (default frame) | `none` lets blur spread past the object's bounds |
| filter | stored `filter` box ... fastgaussian | keep fastgaussian; box is cheaper and harsher |

Set the other stored controls with `property.set {key: "fx.<entry>.<param>"}` (find the entry with `param.list {id, match: "blur"}`); the stored `size` is in size units, so use the `blur` design key for the strength and leave `size` alone.

## Recipes
- **Focus pull in (title):** `blur` 29 to 35 px to 0 over 12 to 18 f, `ease-out` (arriving), with `opacity` 0 to 1 over the first half and a tiny `scale` settle 1.06 to 1.08 to 1. Exit is the mirror, faster (8 to 10 f), `ease-in`.

  By design name (verified: keyed-blur-focus-pull):

  ```json
  {"command": "anim.set", "args": {"id": "#title", "keyframes": [
    {"at": 0, "blur": 28, "opacity": 0, "scale": 1.08, "ease": "ease-out"}, {"at": 18, "blur": 0, "opacity": 1, "scale": 1}]}}
  ```

  Read it back at a frame: `view.seek {frame: 9}` then `property.get {key: "blur"}` returns the px at that frame (0 f: 28 px, 18 f: under 0.1 px, 9 f: between).
- **Depth of field:** background layers static 7 to 14 px, mid 0 to 3.5 px, foreground sharp (verified: blur-directional-and-depth). Never blur text the viewer must read.
- **Whip / speed:** use `directionalBlur` (`"160px 0deg"` falling to 0 as the object lands; [directional-blur.md](directional-blur.md)), or [motion-blur.md](motion-blur.md), which follows the real motion.
- **Glass card:** a blurred copy of the background inside a mask under the card (see [compositing-and-masks.md](compositing-and-masks.md); not verified here). `backdrop-filter` is refused: there is no node for it in either host.
- **Several effects at once:** `filter "blur(4px) brightness(1.2)"` (verified: effects-in-css-terms).

## Pitfalls
- Big radii on big objects are expensive; preview with looks, not playback.
- Blur makes edges extend: give room (or stored `clipping` none) and check `inspect probe` `effect_spread`.
