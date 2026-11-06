# Drop shadow

`dropShadow "dx dy blur colour"`: offset in px with **y down** (a positive `dy` puts the shadow below), `blur` a Gaussian sigma in px (the fall-off ramp is 2.563 x blur), the colour with its alpha (`#00000059` is black at 35 %). `property.set {key: "dropShadow", value: "0 6px 12px #00000059"}`; `"none"` removes it. Verified: shadow-card-lift.

Ranges: `abs(dx)` at most W/2, `abs(dy)` at most H/2, blur 0 to 166 px at 1920 (0.0866 x W); anything outside is refused with the limit. There is no spread: a fourth length is refused (`"0 4px 8px 2px #000"`); the object form `{x, y, blur, color}` also works. Measured by the app: for `10px 4px 8px` the shadow's right edge is 10 px out and its bottom edge 4 px below the box edge.

Carve: Resolve exact, After Effects approximate.

**Verified (0.0.72, stored units):** "lift" on a white card over a light grey ground: shadow offset 4 px to 27 px below, softness 5 px to 25 px, opacity 0.45 to 0.3 over 18 f, with the card rising 16 px and scaling 1 to 1.04. It reads as the card lifting toward the viewer.

## Stored parameters behind it
| stored param | range | meaning | design equivalent |
|---|---|---|---|
| x, y | -0.5 to 0.5 | offset as frame fractions, **y up** (a negative y is below) | dx = x x W; dy = -y x H |
| softness | 0 to 0.2 | blur of the shadow, width-normalised | blur px = softness x 0.433 x W |
| opacity | 0 to 1 | | the colour's alpha |
| red/green/blue | 0 to 1 | shadow colour, linear light | the colour (tint toward the background hue, never pure black on colour) |
| output | image / shadow | `shadow` renders the shadow alone (a separate soft layer) | none |
| lightX/lightY/lightDistance | | light-direction mode | not verified |

## Recipes
- **Resting card (UI):** `"0 6px 12px #00000059"` (alpha 0.25 to 0.35 is `#00000040` to `#00000059`). Big soft plus low opacity beats small hard plus dark.
- **Lift / hover:** animate the offset and the blur up together and the opacity down slightly (the further away, the softer and fainter), plus `scale` 1.03 to 1.05 and a 1 to 2 % rise. 12 to 18 f, `ease-out`. By design name (verified: keyed-glow-shadow-brightness): see below. The stored route (verified: shadow-card-lift) keys the stored shadow entry: from `"0 6px 12px #00000059"` to `"0 28px 30px #00000033"` with the stored values y = -dy/H, softness = blur/(0.433 W), opacity = alpha:

  ```json
  {"command": "property.set", "args": {"id": "#card", "key": "dropShadow", "value": "0 6px 12px #00000059"}}
  {"command": "key.set", "args": {"id": "#card", "key": "fx.e_fx_shadow_clip_2.y", "value": -0.00556, "at": 0, "ease": "ease-out"}}
  {"command": "key.set", "args": {"id": "#card", "key": "fx.e_fx_shadow_clip_2.y", "value": -0.02593, "at": 18}}
  {"command": "key.set", "args": {"id": "#card", "key": "fx.e_fx_shadow_clip_2.softness", "value": 0.01443, "at": 0, "ease": "ease-out"}}
  {"command": "key.set", "args": {"id": "#card", "key": "fx.e_fx_shadow_clip_2.softness", "value": 0.03608, "at": 18}}
  {"command": "key.set", "args": {"id": "#card", "key": "fx.e_fx_shadow_clip_2.opacity", "value": 0.35, "at": 0, "ease": "ease-out"}}
  {"command": "key.set", "args": {"id": "#card", "key": "fx.e_fx_shadow_clip_2.opacity", "value": 0.2, "at": 18}}
  {"command": "anim.set", "args": {"id": "#card", "keyframes": [{"at": 0, "scale": 1, "y": 340, "ease": "ease-out"}, {"at": 18, "scale": 1.04, "y": 325}]}}
  ```

  At frame 18 `property.get {key: "dropShadow"}` reads back about `0px 28px 30px`. The design-name form (verified: keyed-glow-shadow-brightness):

  ```json
  {"command": "anim.set", "args": {"id": "#card", "keyframes": [
    {"at": 0, "dropShadow": "0 6px 12px #00000059", "scale": 1, "y": 340, "ease": "ease-out"},
    {"at": 18, "dropShadow": "0 28px 30px #00000033", "scale": 1.04, "y": 325}]}}
  ```
- **Long shadow (flat design):** equal offsets, no blur, low alpha, tinted: `"30px 30px 0 #00000033"`.
- **Text legibility over images:** a soft halo rather than a directional drop: `"0 0 17px #00000080"`.

## Rules
- One light direction for the whole piece (all shadows offset the same way).
- Shadows on dark backgrounds barely read; use a lighter ground or a glow/rim instead ([glow.md](glow.md)).
- Children of a shadowed group: put the shadow on the group/card, not on every child.
