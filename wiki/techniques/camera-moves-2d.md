---
id: techniques/camera-moves-2d
title: Camera-like moves in 2D
section: techniques
tags: [camera, null, push in, zoom, pan, truck, shake, rig, world]
styles: [all]
topics: [camera, depth]
related: [techniques/null-object, techniques/parallax, techniques/faux-3d, principles/weight, accessibility/motion-sensitivity, principles/arcs]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://blog.cg-wire.com/camera-work-in-animation/, https://helpx.adobe.com/sk/after-effects/how-to/camera-animation.html, https://creativecow.net/?p=39768, https://rainboxprod.coop/forum/viewtopic.php?p=2073]
---

# Camera-like moves in 2D

Carvercat is a 2D compositor, but scenes can still feel filmed: a slow push towards the hero, a pan
across a wide layout, a shake on impact. The trick is a **camera null**: an invisible object that every
scene element is parented to. Moving, scaling or rotating the null moves the whole world as one.

## The idea

- **Push in / pull out**: scale the world up or down about the point of interest.
- **Pan / truck**: move the world sideways (opposite to the imagined camera).
- **Tilt-like roll**: a few degrees of rotation on the world for energy.
- **Shake**: a few frames of small, decaying offsets after an impact.
- Camera moves are **S-curves** (start and stop softly) or slow `linear` drifts; they never overshoot.

## Rules of thumb

- Slow push during a hold: 2–6% scale over 3–5 s.
- Purposeful push to a detail: 20–40% over 24–45 f, S-curve.
- Pans: travel at most about one frame width per 1.5 s at 30 fps for comfortable viewing.
- Shake: 6–12 px, 2–3 swings, decaying over 6–10 f; never on text being read.
- Push towards the point of interest: put the null's centre on it, or the edges drift.

## Measured in Carvercat

Three cards at x 560, 960 and 1360 parented to a camera null at the frame centre; the null's
`scale` keyed 1 → 1.3 over f10–f40 (S-curve). Probe:

| Card | x at f10 | x at f40 | Width f10 → f40 |
|---|---|---|---|
| Card 1 | 560 | 440 | 240 → 312 |
| Card 2 | 960 | 960 | 240 → 312 |
| Card 3 | 1360 | 1480 | 240 → 312 |

Children scale about the null's centre: offsets from it grow by exactly 1.3 (400 px → 520 px) and so do
sizes. The card on the null's centre does not move: that is the point of interest.

## Do and don't

- Do put the null on the point of interest before scaling.
- Do parent everything that belongs to the world; leave captions and logos (screen space) unparented.
- Don't overshoot or bounce a camera move.
- Don't push and pan and roll at once; pick one, add a second only if the first is subtle.
- Nested-comp instances ignore their parent ([KI-119](../../ai/references/known-issues.md#ki-119)): bake
  the camera move into an instance's own keys.

## Checklist

- [ ] Camera null sits on the point of interest.
- [ ] Screen-space elements (captions, bugs) are not parented.
- [ ] Camera moves use S-curve or `linear`, no overshoot.
- [ ] `inspect probe` shows children moving as expected.

## In Carvercat

- Curve names on this page (S-curve) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Null: a real null object, `object.new {kind: "null", frame: 0, duration: "3s", style: {x: 910, y: 490}}` (its box is 100 × 100 px, so that is the
  centre of a 1920 × 1080 frame), then `parent.assign {ids: ["<null id>", "#card1", "#card2", "#card3"]}`: the first id is the parent and the
  children keep their screen spot. Animate the null's `scale`, `x`, `y` or `rotate` ([null object](null-object.md)). It draws nothing, so lint has nothing to report;
  the old tiny `opacity` 0 ellipse, parented by selecting the children and then the null, still works and is reported as `never_visible`.
  Rebuilt on a null the table above reads the same (cards at 560, 960, 1360 at f10 and 440, 960, 1480 at f40, 312 px wide; checked by `wiki/tools/verify_keyed_pages.py`).
- In a project file, parenting needs `parentId`, `parent` effects entries on both clips and a child position
  stored relative to the parent ([arcs](../principles/arcs.md#in-carvercat)).
- Whole-film cameras through named poses and continuous subscenes: [JSON authoring](../../ai/references/app/json-authoring.md#continuous-motion-across-sub-comps).
- Ready-made: `Photo push - 5 s` (6% over 150 f) ([cb-photo push in Corporate Brand](../../ai/patterns/corporate-brand.md)),
  `Zoom settle` ([Motion Patterns](../../ai/patterns/README.md)), `Zoom past` ([Sports](../../ai/patterns/sports.md)),
  map zooms ([maps](../../ai/references/maps/maps.md)).
- Lab: comp `T Camera` in [the techniques lab](../labs/README.md).
