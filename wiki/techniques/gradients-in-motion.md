---
id: techniques/gradients-in-motion
title: Gradients in motion
section: techniques
tags: [gradient, shimmer, sheen, light sweep, gradient start, gradient end, offset, animated gradient]
styles: [minimal-luxury, saas-ui, futuristic-hud, retro, corporate-brand]
topics: [colour, light]
related: [design/colour-transitions, techniques/faux-3d, techniques/looping, design/colour-psychology]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.schoolofmotion.com/blog/color-theory-after-effects, https://lottiefiles.com/blog/tips-and-tutorials/color-theory-for-motion-design.md]
---

# Gradients in motion

A moving gradient makes a flat shape feel lit: a sheen passing over a card, a glow sweeping through a logo,
a background whose colours drift. In Carvercat the gradient is moved by keying its **start and end points**;
several other gradient controls exist on the panel but do not move the picture in 0.1.6.

## The idea

- **Sheen / shimmer**: a narrow light band in an otherwise flat gradient, swept across the object once.
- **Drift**: a soft two- or three-colour gradient whose endpoints wander slowly behind a held scene.
- **Light direction**: the band and its direction must agree with the scene's light ([solid drawing](../principles/solid-drawing-2d.md)).

## Rules of thumb

- Sheen band 5–10% of the gradient length; sweep it 20–35 f with an S-curve; repeat no more than every 2–3 s.
- Drift: move endpoints by less than half the object's width over several seconds, `linear` or very soft.
- Keep gradient stops in one hue family for calm looks; opposite hues pass through grey in between
  ([colour transitions](../design/colour-transitions.md)).

## Measured in Carvercat

**Sheen by keying start and end (works).** A 1200 px bar with stops base (0.2 grey) at 0, 0.45, 0.55, 1 and
white at 0.5. `shape.fill.gradientStart` keyed `[-1, 0.5]` → `[1, 0.5]` and `gradientEnd` `[0, 0.5]` →
`[2, 0.5]` (stored, object-local fractions, y down; no design name yet) together over f5–f35 (S-curve). Rendered every 5 f, the brightest pixel along the bar:

| Frame | 5 | 10 | 15 | 20 | 25 | 30 |
|---|---|---|---|---|---|---|
| Sheen | off the bar | off the bar | entering at the left edge | centre (x 960) | leaving at the right edge | off the bar |

Moving both points by two object widths carries the band from fully off one side to fully off the other; the
S-curve makes it cross the visible bar quickly, between about f13 and f27.

**Gradient offset does nothing.** `shape.fill.gradientOffset` keyed 0 → 1 over 60 f, with `Repeat` set to
once, repeat or pingpong, rendered identical pixels at f0, 15, 30 and 45. `carvercat_authoring {mode:"controls"}`
reports `Repeat` as "the native gradient renderer does not read this control" and `Interpolate` as unavailable.
This is still [KI-111](../../ai/references/known-issues.md#ki-111) on 0.1.6.

## Do and don't

- Do key start and end together, moving the same distance, to slide a gradient.
- Do keep the sheen subtle on text; it should glint, not flash.
- Don't key `gradientOffset`, `Repeat` or `Interpolate`; they do not change the render.
- Don't loop a sheen constantly; once per hold is plenty.

## Checklist

- [ ] Gradient moved by start/end keys only.
- [ ] Sheen direction matches the scene's light.
- [ ] Checked on rendered frames (`carvercat_render` or `carvercat_look`), not by parameter values.

## In Carvercat

- Curve names on this page (S-curve) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Static gradient: `fill: "linear-gradient(90deg, #333 0%, #fff 50%, #333 100%)"` or `"radial-gradient(circle 200px at 25% 75%, ...)"` (stops in %, a CSS colour with alpha; After Effects keeps only the first and last stop).
  A gradient cannot be keyed by design name (`fill` in a key must be a colour: refused with "not a colour name, hex, rgb() or hsl()"), so the sheen moves by the stored
  `shape.fill.gradientStart` and `gradientEnd` (keyframeable, object-local fractions, y down). Old names, accepted for one release: `shape.fill.paint` gradient,
  `shape.fill.gradient` (stops: position, colour, alpha). Text has the same set on `text.fill`.
- Gradient basics and the shimmer recipe: [fill and gradients](../../ai/references/effects/fill-and-gradients.md);
  logo sheen template: `Light sweep` ([ml-light-sweep](../../ai/patterns/ml-light-sweep.md)).
- Labs: comps `M Gradient` and `M Shimmer` in [the measurement lab 2](../labs/README.md).
