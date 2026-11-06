---
id: techniques/null-object
title: Null object
section: techniques
tags: [null, parent, pivot, rig, camera, handle, transform]
styles: [all]
topics: [rigging, camera, structure]
related: [techniques/camera-moves-2d, techniques/parallax, principles/arcs]
verified: design/1 (Carvercat 0.1.8)
source_inspiration: []
---

# Null object

A **null** is an object that is only a transform: a position, a rotation, a scale and a pivot, and nothing to see. It is the
handle you parent other objects to, so that one set of keys moves, turns or scales all of them.

## The idea

- Give a rig one control: park the parts under a null and animate the null.
- Put a pivot exactly where something should turn: a hinge, a nail, the middle of a picture.
- Make a camera: parent the whole world to a null and move the null ([camera-like moves](camera-moves-2d.md)).
- Keep it clean: a null has no size and no opacity, so there is nothing to hide and nothing for lint to flag.

## How it behaves

- **Make it** with `object.new {kind: "null", style: {x, y}, duration}` or as a scene node `type: "null"`. It starts at the
  playhead and lasts 90 frames unless you say how long, so give it the length of the comp.
- **Its box is nominal**: 100 × 100 px, so `x`, `y` are the top-left of that box and its default pivot (`transformOrigin`
  `"50% 50%"`) is the centre. To put the pivot at frame point (960, 200), write `x: 910, y: 150`. The centre of a 1920 × 1080 frame is `x: 910, y: 490`.
- **It has `x`, `y`, `rotate`, `scale` and `transformOrigin`.** `width`, `height` and `opacity` are refused (`not-settable`)
  and `scene.get` leaves them out. It never renders.
- **Parent to it** with `parent.assign {ids: [null, child, child]}` (the first id is the parent; ids take selectors such as
  `#sign`) or nest the children under it in a scene document. A child keeps its place in the frame, and its `x`, `y` are then measured from the null's top-left.
  `parent.clear {ids}` unlinks it again, keeping the place.
- **A null can be the child of another null**: one outer handle for the whole figure, an inner one for a single joint.
- **Opacity does not pass down.** A parent's opacity never reaches its children in After Effects or Resolve, and Carvercat
  matches, so put opacity on the children.

## Measured in Carvercat (checked by `wiki/tools/verify_keyed_pages.py`)

A white 300 × 200 sign hung 100 px below a null whose pivot is the point (960, 200), the null's `rotate` keyed 0 → 30° over 30 f (`ease-in-out`).
Rendered, the sign's centre, (960, 400) at rest, is at (860, 373) at f30, and the corner it left, (1100, 490), is bare background: it swung 30° clockwise
about the null's pivot.

The camera rig of [camera-like moves](camera-moves-2d.md) rebuilt on a real null: three 240 px cards at x 560, 960 and 1360, parented to a null at
(910, 490), `scale` keyed 1 → 1.3 over f10–f40 (S-curve). The cards' centres read 560, 960, 1360 at f10 and 440, 960, 1480 at f40, each 312 px wide: the same
numbers as the first build, measured with the older invisible-ellipse null.

## Do and don't

- Do set the pivot by moving the null, not by moving the children: write the null's `x`, `y` as the joint minus 50.
- Do give the null the full length of the clips it carries; a short null is a parent that ends early.
- Do animate the null for the shared move and the children for their own moves.
- Don't expect a null to fade its children; key their `opacity`.
- A two-level rig (a null under a null, with children under that) reads back through `scene.get` nested as it is parented, with parent-relative positions,
  and the document applies to a fresh comp unchanged ([KI-170](../../ai/references/known-issues.md#ki-170), fixed).

## Carve status

After Effects: a real Null layer, the children parented to it. Resolve: a transform-only parent (a transparent background with a Transform and no
merge) that each child's parent transform reads. `carve.preflight` lists nothing unsupported for either host on these rigs. The live transfer tests in
Resolve and After Effects are still to be done (a later release).

## Checklist

- [ ] The null's pivot sits on the joint, the hinge or the point of interest.
- [ ] The null lasts as long as its children.
- [ ] Opacity is on the children, not the null.
- [ ] Screen-space elements (captions, logos) are not parented to a camera null.

## In Carvercat

- Make: `object.new {kind: "null", frame: 0, duration: "4s", style: {x: 910, y: 150}}`; scene node `{"id": "pivot", "type": "null", "style": {"x": 910, "y": 150}, "children": [...]}`.
- Parent: `parent.assign {ids: ["<null id>", "#child1", "#child2"]}`, `parent.clear {ids}`; animate the null with `anim.set {id, keyframes: [{at, rotate | x | y | scale, ease}]}`.
- Old way, accepted: a tiny ellipse at `opacity` 0 as a pivot, which lint reports as `never_visible`; use a null instead.
- Rigging guide (joints, anchors, parent trap): [rigging](../../ai/references/drawing/rigging.md#null-object). Camera and plane rigs: [camera moves](camera-moves-2d.md), [parallax](parallax.md).
