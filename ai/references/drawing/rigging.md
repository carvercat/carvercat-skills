# Drawing a character or object from parts, and rigging it to animate

**Verified 0.0.72** (comp `RIG Character`): a body, head, eye and arm built from shapes; eye parented to head, head and arm parented to body; body squash-and-stretch from its feet, arm waving from the shoulder, head tilting.

## 1. Draw in parts
Every part that moves on its own is its own object: body, head, each upper arm/forearm, each leg, eyes, mouth, props. Static detail can be one object (or one path). Name every part (`clip.rename`).
Build at the final pose, neutral (rotation 0, scale 1), at the size it will be seen. Build back-to-front (far arm first, then body, head, near arm) — track order is draw order.

## 2. Anchors = joints
Set each part's `transformOrigin` where it bends, BEFORE animating (the stored anchor change keeps the picture still, so set it, then fine-tune `x`, `y`):
| Part | transformOrigin (stored anchor) |
|---|---|
| upper arm, hanging | "50% 0%" ([0, 1], top = shoulder) |
| leg | "50% 0%" ([0, 1], hip) |
| head | "50% 100%" ([0, −1], neck) — but see the parent warning below |
| body | "50% 100%" ([0, −1], feet/bottom) so squash keeps it on the ground |
| door / lid / page | the hinge edge ("0% 50%" for [−1,0] etc.) |
| needle / clock hand | its pivot end |
`transformOrigin` is as in CSS (`"left top"`, `"50% 50%"`, `"20px 30px"`); stored anchors are half-sizes of the part (y up).

## 3. Parent (hierarchy)
`parent.assign {ids: [PARENT, child, child, ...]}` — **the FIRST id is the parent**, and ids take selectors (`#head`). (`dry_run:true` first: the reply says "parented N to <name>"; the selection form, with the last selected as the parent, is the older route.) Children then move/rotate/scale with the parent; their position becomes relative (the reply shows the converted value). `parent.clear {ids}` bakes and unlinks.
Typical tree: body → head → (eyes, mouth); body → upper arm → forearm → hand; body → legs.

### ⚠ Parent transformOrigin trap (verified)
A child of a parent whose `transformOrigin` is OFF-CENTRE drifts away when the parent rotates (the eye slid off a head with stored anchor [0,−1], "50% 100%", when the head tilted 10°). With the parent's `transformOrigin` at "50% 50%" (stored [0,0]) the child stays put. Use a null at the joint (next section) as the pivot, or:
- Keep `transformOrigin` centred on any part that has children and rotate only childless parts about off-centre origins (arms, legs, hands are usually leaves).
- **Writing the rig as stored JSON (verified 0.1.6):** store each child's position as `0.5 + (child − pivot)` (an offset from the comp centre; stored value), not its absolute position; see [../app/json-authoring.md](../app/json-authoring.md). A fully transparent pivot shape fails lint (`never_visible`, an error): use a null instead, or a visible part at the joint (feet, a nail). Worked examples: [ct-character-hop.md](../../patterns/ct-character-hop.md), [ct-hanging-sign.md](../../patterns/ct-hanging-sign.md).

## Null object
A **null** is an object that is only a transform: `x`, `y`, `rotate`, `scale` and `transformOrigin`, and nothing else. It draws nothing, has no `width`, `height` or `opacity` (each is refused with `not-settable`), and passes no opacity to its children. Use it as the parent of a rig: animate the null and everything parented to it moves, turns and scales together. It replaces the old "tiny transparent ellipse as a pivot", which lint flagged as never visible; a null passes lint (verified: null-rig-pivot).

- **Place it by its box.** A null has a nominal 100 x 100 px box, so `x`, `y` are its top-left and its default `transformOrigin` ("50% 50%") is the box centre. To put the joint at frame point (jx, jy) write `x = jx − 50`, `y = jy − 50`. The centre of a 1920 x 1080 frame is x 910, y 490.
- **Make it** with `object.new {kind: "null", style: {x, y}, duration}` (it starts at the playhead unless `frame` is given and lasts 90 frames unless `duration` says otherwise, so pass the comp length or the children outlive their parent) or as a scene node `type: "null"`.
- **Parent children** with `parent.assign {ids: [null, child, ...]}`: the first id is the parent (selectors work, `#plate`), the children keep their place in the frame, and their `x`, `y` become measured from the null's top-left. Or nest them under the null in a scene document: a child's `x`, `y` are then measured from the null's top-left from the start. `parent.clear {ids}` unlinks. A null can be the child of another null.
- **Animate the null**, not the children: `anim.set {id: <null>, keyframes: [{at, rotate | x | y | scale}]}`. Opacity belongs on the children.
- **Pivot.** Rotation and scale turn about the null's `transformOrigin`, so the null's centre is the joint however the children hang off it.

### Recipe: a hanging sign swinging from a nail (verified: null-rig-pivot)
The joint is at frame point (960, 200), so the null sits at x 910, y 150. The sign hangs 100 px below it and the rope runs from the joint to the sign; both are children, measured from the null's top-left (the sign's frame position (810, 300) is (−100, 150) here).

```json
{"command": "scene.apply", "args": {"scene": {"schema": "carvercat/2.0",
 "comp": {"width": 1920, "height": 1080, "fps": 30, "duration": "3s"},
 "children": [
  {"id": "bg", "type": "rect", "style": {"x": 0, "y": 0, "width": 1920, "height": 1080, "fill": "#101018"}},
  {"id": "pivot", "type": "null", "style": {"x": 910, "y": 150}, "children": [
    {"id": "sign", "type": "rect", "style": {"x": -100, "y": 150, "width": 300, "height": 200, "fill": "#ff7a00", "borderRadius": 16}},
    {"id": "rope", "type": "rect", "style": {"x": 46, "y": 50, "width": 8, "height": 100, "fill": "#ffffff"}}]}]}}}
{"command": "anim.set", "args": {"id": "#pivot", "keyframes": [
  {"at": 0, "rotate": 0, "ease": "ease-in-out"}, {"at": 30, "rotate": 30}]}}
```

At frame 30 the sign has swung 30° clockwise about the nail: its centre, (960, 400) at rest, is at (860, 373), and the corner area it left is bare background (read from a look: orange at (860, 373), background at (1100, 490)). The rope stays attached because it is parented to the same null.

### Recipe: one null carrying a group of separate objects (verified: null-rig-parent-assign)
Build the objects first, then add the null and parent them. A card, a label and a badge that enter as one: make the objects with `scene.apply`, then

```json
{"command": "object.new", "args": {"kind": "null", "duration": "4s", "style": {"x": 910, "y": 490}}}
{"command": "parent.assign", "args": {"ids": ["<null id>", "#plate", "#dot"]}}
{"command": "anim.set", "args": {"id": "<null id>", "keyframes": [
  {"at": 0, "x": 910, "ease": "ease-out"}, {"at": 20, "x": 1310}]}}
```

`object.new` returns the null's id in `touched`. The children keep their places when assigned, and moving the null 400 px right moves both with it (read from a look at frame 20). A second null made the child of the first (`parent.assign {ids: [outer, inner, "#dot"]}`) carries its own children, so one null can drive the whole figure and an inner one a single joint. `scene.get` reads a two-level rig back nested, as it is parented, and the document round-trips through `scene.apply` ([KI-170](../known-issues.md#ki-170), fixed; verified: null-rig-parent-assign).

### Null versus group
Use a null when you want a handle: a joint, an anchor, a camera-like move for several loose objects, a single control for a rig. A `group` is a transparent container with its own bounds. Both carry their children; a null adds nothing to the picture and its children stay separate objects with their own keys.

### Carve status
After Effects: a real Null layer with the children parented to it. Resolve: a transform-only parent (a transparent background with a Transform and no merge) that each child's parent transform reads. `carve.preflight` lists no unsupported item for either host on the rig above (verified: null-rig-pivot). Opacity does not pass from a null to its children in either host, which matches Carvercat. The live Resolve and After Effects transfer tests of nulls are still pending (a later release).

## 4. Group vs parent
| | `edit.group` | `parent.assign` |
|---|---|---|
| result | a container object; members inside | separate objects linked by transform |
| pivot | the group scales about its bounds centre; group position is an offset around 0.5 (stored value) | the parent's own `transformOrigin` |
| editing members | `object.enter` / `object.exit` (not batchable); batches can't reach inside | still directly addressable |
| use for | a rigid assembly animated as one (card + label, a whole character for a walk-on) | articulated parts (limbs, heads) |
Common: rig with parents, then group the whole character for its entrance/exit.

## 5. Animate (12 principles applied)
- **Squash & stretch** on the body with `transformOrigin` "50% 100%" (feet): scaleY 1 → 0.85 (scaleX 1.1) on the crouch, → 1.08 (0.95) on the spring, → 1 settle. Volume roughly constant (x·y ≈ 1).
- **Overlap / follow-through:** children lag the parent 2–4 f (head settles after the body; the arm keeps swinging 1–2 smaller arcs).
- **Arcs:** limbs rotate about their joint — never slide a forearm by position.
- **Anticipation:** a small opposite move (crouch, arm back 10–15°) 4–8 f before a big one.
- **Secondary action:** blink (eye scaleY 1 → 0.1 → 1 in 4 f, every 2–4 s), breathing (body scaleY ±1.5 % over 40–60 f, ease-in-out).
- **Wave:** upper arm 0 → 140° (stored value; `rotate` is clockwise) ease-out, then 110 ↔ 140 ease-in-out 8 f apart, 2–3 cycles.
- Shape-built ground shadow (soft-edge ellipse) that shrinks when the character jumps.

## 6. Checklist
- `carvercat_look` full-frame at key poses (crop looks misdrew backgrounds on 0.0.72).
- `inspect probe` on the parent and one child to confirm they move together.
- Name everything; keep the rig in its own comp so it can be placed/instanced and recoloured via raised face controls.

## Group scaling
A group scales and rotates about the centre of its bounds (a fresh group sits at the comp centre). When a collapse must land on a point, key position together with scale. Don't upscale small paths 8–10× with transform scale (soft/stepped edges) — re-issue `object.path` with points and handle offsets scaled, and keep rest scale near 1.
