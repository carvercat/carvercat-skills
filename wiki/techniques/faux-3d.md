---
id: techniques/faux-3d
title: Faux 3D in a 2D tool
section: techniques
tags: [faux 3d, 2.5d, extrusion, shading, gradient, flip, isometric, depth, sphere]
styles: [funky, retro, explainer, cartoon-bounce, saas-ui]
topics: [depth, shading]
related: [principles/solid-drawing-2d, techniques/parallax, techniques/camera-moves-2d, design/colour-psychology]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://80.lv/articles/inside-the-making-of-2-5d-parallax-animation-for-music-artist, https://petapixel.com/2013/11/19/creating-motion-stills-animate-photo-post-parallax-effect, https://uxmag.com/articles/creating-usability-with-motion-the-ux-in-motion-manifesto]
---

# Faux 3D in a 2D tool

Depth without a 3D engine: stacked copies make an extrusion, gradients make a curved surface, a scale
flip makes a turn, layered speeds make space. Faux 3D is a style in itself (flat-with-depth, isometric
icons, retro extruded type), and it renders fast and stays fully editable.

## The idea

- **Extrusion**: copies of a shape stepped 2–6 px down-right in a darker tone, the face on top. Reads as
  a thick block or chunky lettering.
- **Shading**: a radial gradient (light spot off-centre towards the light) turns a circle into a sphere; a
  linear gradient turns a rectangle into a cylinder or a bevel.
- **Turns**: `scale` `[x, 1]` through 0 (see [solid drawing](../principles/solid-drawing-2d.md)).
- **Space**: [parallax](parallax.md) and [camera moves](camera-moves-2d.md).
- Every cue must agree on one light direction.

## Rules of thumb

- Extrusion depth 4–10% of the face height; step 3–5 px per copy; 6–10 copies.
- Extrusion colour: the face colour 30–45% darker, same hue.
- Sphere highlight about one third in from the edge towards the light; dark edge on the far side.
- Hard offset "shadows" (no softness) are a flat-graphics extrusion of one copy: bold, poster-like.

## Measured in Carvercat

On a light ground (#E9E3D7), checked with `carvercat_look`:

- **Extrusion**: 8 copies of a 400 × 260 rounded rectangle, each offset 4 px right and 4 px down in a
  darker orange, the face on top: a solid 32 px slab with a continuous side; the copies merged into one
  surface with no visible steps at 1920 wide.
- **Sphere**: an ellipse with a radial `fill`, stops light blue → dark blue: `"radial-gradient(ellipse 275.8px at 35% 65%, #b8ceff 0%, #102d73 100%)"`
  (the lab's 300 px sphere, read back by `scene.get`): a convincing sphere, with the bright spot left of and **below** the centre.
  The `at X% Y%` point is measured from the object's top-left with y going down, so a light from the upper left needs about `at 35% 35%`
  (the lab's second sphere). The 0.1.6 note was the stored gradient `Start` `[0.35, 0.65]`.

Stacked copies cost one clip each (preview speed was not measured here); keep counts modest on busy
scenes ([performance](../../ai/references/app/performance.md)).

## Do and don't

- Do choose the light direction first and derive shading and extrusion direction from it.
- Do keep extrusion copies in one group so they move as one.
- Don't mix faux-3D objects lit from different sides.
- Don't extrude small text; the side surface fills the counters.

## Checklist

- [ ] One light direction for all shading, extrusion and shadows.
- [ ] Extrusion steps are invisible at output size (`carvercat_look` with `region` zoom).
- [ ] The extruded object animates as one group.

## In Carvercat

- Extrusion: duplicate the shape, offset each copy 3–5 px (`x` and `y`), darker
  `fill`; put the face on the top track. Group with `edit.group` and animate the group.
- Hard offset shadow on text: `Offset shadow title` ([fk-offset-title](../../ai/patterns/fk-offset-title.md)).
- Shading: `fill` as a `linear-gradient(...)` or `radial-gradient(...)` string with stops in % (colour and alpha; old names: `shape.fill.paint` gradient with `Shape` linear or radial, `Start`/`End`) ([fill and gradients](../../ai/references/effects/fill-and-gradients.md)).
- Soft depth: `dropShadow` (old name: the `shadow` effect, [shadow](../../ai/references/effects/shadow.md)).
- Lab: comp `T Faux 3D` in [the techniques lab](../labs/README.md).
