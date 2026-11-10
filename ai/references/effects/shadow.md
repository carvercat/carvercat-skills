# Drop shadow

`dropShadow "dx dy blur colour"`: offset in px with **y down** (a positive `dy` puts the shadow below), `blur` a Gaussian sigma in px (the fall-off ramp is 2.563 x blur), the colour with its alpha (`#00000059` is black at 35 %). `property.set {key: "dropShadow", value: "0 6px 12px #00000059"}`; `"none"` removes it. Verified: shadow-card-lift.

Ranges: `abs(dx)` at most W/2, `abs(dy)` at most H/2, blur 0 to 166 px at 1920 (0.0866 x W); anything outside is refused with the limit. There is no spread: a fourth length is refused (`"0 4px 8px 2px #000"`); the object form `{x, y, blur, color}` also works. Measured by the app: for `10px 4px 8px` the shadow's right edge is 10 px out and its bottom edge 4 px below the box edge.

Carve: Resolve exact, After Effects approximate.

**Verified:** "lift" on a white card over a light grey ground: the shadow goes from `"0 6px 12px #00000059"` to `"0 28px 30px #00000033"` over 18 f while the card rises 15 px and scales 1 to 1.04 (verified: keyed-glow-shadow-brightness). It reads as the card lifting toward the viewer.

Tint a shadow toward the background hue on a coloured ground, never pure black. A shadow alone as its own soft layer and the light-direction mode are stored controls and are not verified; the design key covers offset, blur and colour.

## Recipes
- **Resting card (UI):** `"0 6px 12px #00000059"` (alpha 0.25 to 0.35 is `#00000040` to `#00000059`). Big soft plus low opacity beats small hard plus dark.
- **Lift / hover:** animate the offset and the blur up together and the opacity down slightly (the further away, the softer and fainter), plus `scale` 1.03 to 1.05 and a 1 to 2 % rise. 12 to 18 f, `ease-out`. One key holds offset, blur and colour (verified: keyed-glow-shadow-brightness):

  ```json
  {"command": "anim.set", "args": {"id": "#card", "keyframes": [
    {"at": 0, "dropShadow": "0 6px 12px #00000059", "scale": 1, "y": 340, "ease": "ease-out"},
    {"at": 18, "dropShadow": "0 28px 30px #00000033", "scale": 1.04, "y": 325}]}}
  ```

  At frame 18 `property.get {key: "dropShadow"}` reads back `0px 28px 30px` and the colour.
- **Long shadow (flat design):** equal offsets, no blur, low alpha, tinted: `"30px 30px 0 #00000033"`.
- **Text legibility over images:** a soft halo rather than a directional drop: `"0 0 17px #00000080"`.

## Rules
- One light direction for the whole piece (all shadows offset the same way).
- Shadows on dark backgrounds barely read; use a lighter ground or a glow/rim instead ([glow.md](glow.md)).
- Children of a shadowed group: put the shadow on the group/card, not on every child.
