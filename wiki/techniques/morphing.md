---
id: techniques/morphing
title: Shape morphing
section: techniques
tags: [morph, shape change, polygon, star, corner radius, crossfade, transformation]
styles: [funky, explainer, saas-ui, futuristic-hud, cartoon-bounce]
topics: [shapes, transformation]
related: [techniques/match-cuts, techniques/masking, principles/slow-in-slow-out, genres/logo-animation]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://community.adobe.com/t5/after-effects-discussions/how-do-i-morph-shapes-with-different-points-in-a-controlled-way/td-p/10037068, https://pixflow.net/blog/how-to-create-morphing-animations-in-after-effects/, https://uxmag.com/articles/creating-usability-with-motion-the-ux-in-motion-manifesto]
---

# Shape morphing

A shape turns into another shape: a button becomes a card, a dot becomes a line, a square becomes a
circle, a star softens into a badge. Morphing keeps the viewer's eye on one continuous object, which is
why it is so good for explaining change.

## The idea

- The best morphs change **one** attribute at a time: size, then corners, then colour, not all at once.
- Ease the morph as one gesture (S-curve or ease out); a linear morph looks like a loading glitch.
- When two shapes have nothing in common, a quick scale-and-crossfade at a shared centre reads as a morph.
- Keep the centre (or the anchor edge) fixed so the change looks like transformation, not travel.

## Rules of thumb

- Morph duration 12–24 f; small UI morphs 8–12 f.
- Crossfade morph: both shapes at the same centre, matched in size at the crossover frame, opacity swap
  over 4–6 f in the middle of the size change.
- Pill and circle endpoints are easier with a round-capped thick stroke on a 2-point path than with corner
  radius (see the Carvercat note below).

## Measured in Carvercat: which shape parameters morph

All three shapes keyed from f10 to f40 (S-curve), checked with `carvercat_look` every 5 f (the stored names of 0.1.6 are in the second column; the design names are in the last section):

| Parameter | From → to | What happened |
|---|---|---|
| `sides` (stored `shape.geometry.ngon.sides`) | 3 → 12 | steps through whole numbers: triangle, square, pentagon … 12-gon; no in-between shapes |
| `innerRadius` (stored `shape.geometry.star.innerRadius`, label Depth) | `"37%"` → `"100%"` (stored 0.37 → 1.0) | a smooth morph from a sharp 5-point star to a 10-sided polygon |
| `borderRadius` (stored `shape.geometry.rectangle.cornerRadius`) | `0` → `"25%"` (stored 0 → 0.5, the 0.1.6 maximum) | a smooth morph from a square to a rounded square, not a circle |

- Sides are integers, so a polygon "morph" by sides is stepped. Use it as a deliberate counting effect, or
  hide the steps inside a fast scale pop.
- Star depth 1.0 gives a polygon with twice the point count: the star-to-badge morph is free.
- The old `cornerRadius` 0.5 was the maximum and gave a radius of a quarter of the shorter side, so a rectangle
  could not become a circle or a full pill ([JSON authoring](../../ai/references/app/json-authoring.md)). **The range now runs to half the short side**:
  `borderRadius: "50%"` is a circle on a square and a stadium on any box (a 440 × 110 box reads 55 px). Square to circle by keying the
  stored `shape.geometry.rectangle.cornerRadius` 0 → 1.0 on a 200 px square read `borderRadius` 0, 75 and 100 px at f0, f10 and f20
  (default ease), a circle at the end; `anim.set` with `borderRadius` keys it by name (0 to `"50%"` on the 200 px square read 0, 50 and 100 px at f0, f10 and f20, default ease).

## Do and don't

- Do keep the morphing shape's centre still.
- Do combine a morph with one supporting change (colour or scale), not three.
- Don't rely on `sides` for a smooth morph.
- Don't morph text; animate it out and in.

## Checklist

- [ ] One continuous object from the viewer's point of view.
- [ ] Centre or anchor edge fixed.
- [ ] Eased as one gesture, 8–24 f.
- [ ] Looked at in the middle of the morph (`carvercat_look`), not only at the ends.

## In Carvercat

- Curve names on this page (S-curve) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Geometry keys: `width`, `height` (px or %, keyable today), `borderRadius` (px or % of the short side), `sides` (polygon, whole numbers 3 to 64), `points`
  (star, 3 to 64), `innerRadius` (px or % of the outer radius, 1% to 100%). `borderRadius` and `innerRadius` key by design name (checked: `innerRadius` `"37%"` → `"100%"` read 37 and 100 at f0 and f20)
  (`anim.set` today refuses them: "not a design key"); `sides` and `points` are whole numbers and not animatable. Old names, accepted for one release:
  `shape.geometry.rectangle` `Width`, `Height` (fractions of comp width), `Corner radius`, ngon `Sides`, star `Points` (param `sides`), `Depth` (param `innerRadius`).
- Path shapes: the RENDERER does morph paths. A path clip's `path.geometry` property takes keyframes whose values
  are whole contour sets; with the same contour and point counts on both keys, every node and handle is
  interpolated with the arriving key's easing, and a Hold or a count change holds the earlier shape (on the later
  key's own frame too). Measured on 0.1.6 (rev 1105): the app fixture
  `compiler/fixtures/ae-gate/paths/ae_gate_paths.carverproj`, comp "Morph" (square -> diamond -> circle,
  4 points each), rendered by `--frame-shot`: ink box 442 px at f0, 572 px at f10, 702 px at f20.
  The agent tools set those keys too (measured on 0.1.6): draw the shape with `object.path {d}` (SVG path data in px), `view.seek` to
  a frame, `key.set {key:"path.geometry", value:{closed, points:[{x, y, inX, inY, outX, outY, corner}]}, ease}` (the stored contour is fractions; no design name yet),
  repeat at the next frames; `key.list` reads them back. An 8-node blob keyed f0, f30, f60 moved every node to
  within 1 px of the mean of its two keys at the S-curve midpoint. A key with a different node count is accepted
  silently and the shape jumps instead of morphing ([KI-161](../../ai/references/known-issues.md#ki-161)). Full
  recipe: [blob morph](../cookbook/blob-morph.md); history: [FR-045](../../ai/references/known-issues.md#fr-045).
- Pill shapes: `borderRadius: "50%"` on a rectangle; the older way was a 2-point path with a round-capped stroke as thick as the pill
  ([shapes](../../ai/references/drawing/shapes.md)).
- Lab: comp `T Morphing` in [the techniques lab](../labs/README.md).
