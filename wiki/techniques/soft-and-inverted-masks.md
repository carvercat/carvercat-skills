---
id: techniques/soft-and-inverted-masks
title: Soft-edged and inverted masks
section: techniques
tags: [mask, feather, soft edge, inverted mask, knockout, cut-out text, wipe, vignette]
styles: [minimal-luxury, corporate-brand, kinetic-typography, retro]
topics: [compositing, reveal]
related: [techniques/masking, techniques/blend-modes, design/negative-space]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://blog.motionarray.com/learn/after-effects/after-effects-track-mattes/, https://vdci.edu/learn/after-effects/understanding-alpha-luma-mattes]
---

# Soft-edged and inverted masks

Two variations on the basic mask ([masking](masking.md)): a **soft** (feathered) mask edge that makes a wipe
glide rather than cut, and an **inverted** mask that shows everything except the mask shape, for knock-out
text and holes.

## The idea

- **Feathered wipes** read as light or mist passing; hard-edged wipes read as graphic and precise.
- **Knock-out**: text cut out of a coloured plate so the background shows through the letters.
- **Vignettes and spotlights**: an inverted soft shape darkens everything outside a focus area.

## Rules of thumb

- `feather` 2–5% of the frame width (40–100 px at 1920) for luxury wipes; 0 for graphic styles.
- A feathered window should travel its `feather` width past the content so the last pixels finish soft.
- Knock-out text needs a heavy weight and large size; thin strokes vanish.

## Measured in Carvercat

- **Feather works.** A white plate masked by a window whose `feather` is 60 px (the lab stores it as 0.03125 of the
  width), wiped open by scaling the window from its left edge: at the midpoint frame the rendered edge ramp from dark to
  full white was **61 px** wide. The `feather` is the width of the ramp. Re-measured on the design-units build (master
  Carvercat 0.1.8, and again on with the checker `wiki/tools/verify_keyed_pages.py`): `feather` 8, 24 and 60 gave 8.2, 24.0 and 60.6 px ([soft edge and feather](soft-edge-and-feather.md)).
- **Invert did not render on 0.1.6.** With the mask made from a 200 px "CUT OUT" text over an orange plate,
  `mask.invert` set to `on` (on the mask, on the masked plate, and on both) was accepted by `property.set`, but
  the render still showed the plate only inside the letters, never around them (KI-146). **It renders through the
  design key `mask`:** on a rectangle mask (800 × 500, centred in a 1920 × 1080 comp) `property.set {key: "mask",
  value: {ref: "<window>", invert: true}}` gave a black centre and orange corners in `carvercat_render` (pixels (0, 0, 0)
  at the centre, (255, 136, 0) at (100, 100)); the same call without `invert` gave the opposite. Not measured with text as the mask.
- A knock-out on a flat background can still be built by colouring the text in the background colour above the plate.

## Do and don't

- Do use `feather` on the window shape for feathered wipes.
- Do check knock-outs on a rendered frame, not in the parameter list.
- Don't use the old `mask.invert` parameter; use `mask: {ref, invert: true}`.
- Don't feather text masks so much that the letters blur at rest.

## Checklist

- [ ] Feather width chosen from the style; window travels past the content.
- [ ] Knock-outs checked on a render.

## In Carvercat

- Feather: `feather` in px on the mask shape (0 to 0.2 × comp width; exact in Resolve, approximate in After Effects), see
  [soft edge and feather](soft-edge-and-feather.md) and [soft edge](../../ai/references/effects/soft-edge.md).
- Mask: `property.set {key: "mask", value: "<mask id>"}` on the object to cut, then `parent.clear` on the mask ([masking](masking.md)).
  Inverted: `value: {ref: "<mask id>", invert: true}`.
- Old names, accepted for one release: `shape.fill.softEdge` (a fraction of the comp width: 0.03125 = 60 px at 1920),
  `mask.make {ids:[mask, content]}`, `mask.invert` (did not render). `feather` keys by design name (`anim.set` with `feather`, checked: 0 → 60 px).
- Ready-made feathered reveal: `Feather wipe reveal` ([ml-feather-wipe](../../ai/patterns/ml-feather-wipe.md)).
- Lab: comp `T Soft masks` in [the measurement lab 3](../labs/README.md).
