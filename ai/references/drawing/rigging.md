# Drawing a character or object from parts, and rigging it to animate

**Verified 0.0.72** (comp `RIG Character`): a body, head, eye and arm built from shapes; eye parented to head, head and arm parented to body; body squash-and-stretch from its feet, arm waving from the shoulder, head tilting.

## 1. Draw in parts
Every part that moves on its own is its own object: body, head, each upper arm/forearm, each leg, eyes, mouth, props. Static detail can be one object (or one path). Name every part (`clip.rename`).
Build at the final pose, neutral (rotation 0, scale 1), at the size it will be seen. Build back-to-front (far arm first, then body, head, near arm) — track order is draw order.

## 2. Anchors = joints
Set each part's anchor where it bends, BEFORE animating (the anchor change keeps the picture still, so set it, then fine-tune position):
| Part | anchor |
|---|---|
| upper arm, hanging | [0, 1] (top = shoulder) |
| leg | [0, 1] (hip) |
| head | [0, −1] (neck) — but see the parent warning below |
| body | [0, −1] (feet/bottom) so squash keeps it on the ground |
| door / lid / page | the hinge edge ([−1,0] etc.) |
| needle / clock hand | its pivot end |
Units are half-sizes of the part (y up).

## 3. Parent (hierarchy)
`select.clip {index: child}` → `select.add {index: other child}` … → `select.add {index: PARENT}` → `parent.assign` — **the LAST selected is the parent**. (`dry_run:true` first: the reply says "parented N to <name>".) Children then move/rotate/scale with the parent; their position becomes relative (the reply shows the converted value). `parent.clear` bakes and unlinks.
Typical tree: body → head → (eyes, mouth); body → upper arm → forearm → hand; body → legs.

### ⚠ Parent anchor trap (verified)
A child of a parent whose anchor is OFF-CENTRE drifts away when the parent rotates (the eye slid off a head anchored at [0,−1] when the head tilted 10°). With the parent's anchor at [0,0] the child stays put. Until fixed:
- **Use a pivot null (verified 0.0.72):** a tiny shape (ellipse 0.002 W, opacity 0) placed exactly at the joint, anchor [0,0]. Parent the part AND its children to the null; rotate the NULL. The null's centre is the joint.
- Or keep anchors centred on any part that has children and rotate only childless parts about off-centre anchors (arms, legs, hands are usually leaves).

## 4. Group vs parent
| | `edit.group` | `parent.assign` |
|---|---|---|
| result | a container object; members inside | separate objects linked by transform |
| pivot | the group scales about its bounds centre; group position is an offset around 0.5 | the parent's own anchor |
| editing members | `object.enter` / `object.exit` (not batchable); batches can't reach inside | still directly addressable |
| use for | a rigid assembly animated as one (card + label, a whole character for a walk-on) | articulated parts (limbs, heads) |
Common: rig with parents, then group the whole character for its entrance/exit.

## 5. Animate (12 principles applied)
- **Squash & stretch** on the body anchored at the feet: scaleY 1 → 0.85 (scaleX 1.1) on the crouch, → 1.08 (0.95) on the spring, → 1 settle. Volume roughly constant (x·y ≈ 1).
- **Overlap / follow-through:** children lag the parent 2–4 f (head settles after the body; the arm keeps swinging 1–2 smaller arcs).
- **Arcs:** limbs rotate about their joint — never slide a forearm by position.
- **Anticipation:** a small opposite move (crouch, arm back 10–15°) 4–8 f before a big one.
- **Secondary action:** blink (eye scaleY 1 → 0.1 → 1 in 4 f, every 2–4 s), breathing (body scaleY ±1.5 % over 40–60 f, S-curve).
- **Wave:** upper arm 0 → 140° Ease out, then 110 ↔ 140 S-curve 8 f apart, 2–3 cycles.
- Shape-built ground shadow (soft-edge ellipse) that shrinks when the character jumps.

## 6. Checklist
- `carvercat_look` full-frame at key poses (crop looks misdrew backgrounds on 0.0.72).
- `inspect probe` on the parent and one child to confirm they move together.
- Name everything; keep the rig in its own comp so it can be placed/instanced and recoloured via raised face controls.

## Group scaling
A group scales and rotates about the centre of its bounds (a fresh group sits at the comp centre). When a collapse must land on a point, key position together with scale. Don't upscale small paths 8–10× with transform scale (soft/stepped edges) — re-issue `object.path` with points and handle offsets scaled, and keep rest scale near 1.
