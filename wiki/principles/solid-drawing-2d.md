---
id: principles/solid-drawing-2d
title: Solid drawing in 2D motion
section: principles
tags: [solid drawing, volume, depth, light direction, shadow, perspective, card flip, consistency]
styles: [all]
topics: [depth, form]
related: [techniques/faux-3d, techniques/parallax, principles/appeal, principles/staging, design/colour-psychology]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation, https://theses.fh-hagenberg.at/index.php/system/files/pdf/Wolf12.pdf, https://uxmag.com/articles/creating-usability-with-motion-the-ux-in-motion-manifesto]
---

# Solid drawing in 2D motion

In character animation, solid drawing means drawing forms that have volume, weight and balance. Flat
motion graphics have no drawing in that sense, but the principle survives as **consistency of form and
space**: objects keep their size and shape logic, light comes from one place, depth is believable, and
nothing turns into a different object halfway through a move.

## The idea

- **One world**: one light direction, one shadow angle and softness, one perspective for everything.
- **Forms keep their construction**: a card that turns stays a card (it narrows and comes back), it does not
  stretch into a different shape.
- **No twins**: avoid perfectly mirrored poses and identical elements in lock-step; a little asymmetry
  reads as designed rather than duplicated.
- **Depth cues stack**: overlap, size, shadow, blur and parallax all have to agree on what is near.

## Rules of thumb

- Shadows: same offset direction and softness for every object in the scene; nearer objects cast
  longer, softer shadows.
- Depth layers: at most 3 speeds (background, middle, foreground); foreground 1.5–2× the background.
- Card turns: narrow scaleX toward 0 with quad in, swap the face at 0, open with quad out.
- Keep stroke widths consistent across objects of the same kind, and do not scale strokes into
  mismatched weights.

## Measured in Carvercat: a card flip on scale X

A 420 × 280 card with a `dropShadow` (the lab's `"11.5px 10.8px 16.6px #00000073"`), `scale` `[x, 1]` keyed 1 → 0 (f10 → f20,
quad in) → 1 (f30, quad out). Probe widths:

| Frame | 10 | 14 | 17 | 20 | 23 | 26 | 30 |
|---|---|---|---|---|---|---|---|
| Width | 420 | 353 | 214 | 0 | 214 | 353 | 420 |

The narrowing speeds up into the edge-on frame and slows coming out, which is how a turning card's
projected width behaves near edge-on. Swap the front for the back on f20, where the width is 0: the
change is invisible. Two things the look showed: scaling X also squeezes the rounded corners into
narrow ellipses mid-turn (fine at speed, visible in a slow turn), and the default black shadow was
almost invisible on the near-black lab ground: a drop shadow needs a lighter background to read.

## Do and don't

- Do write the scene's light direction in the plan and set every shadow from it.
- Do swap faces of a turning card on its zero-width frame.
- Don't mix soft and hard shadows, or shadows going different ways, in one frame.
- Don't scale a shape non-uniformly by accident (a "squashed" logo at rest is a construction error).

## Checklist

- [ ] One light direction; every `dropShadow` matches it.
- [ ] Depth cues agree (bigger, sharper, faster and in front go together).
- [ ] Turning objects swap faces on the edge-on frame.
- [ ] Resting objects have scale `[1, 1]` unless the design says otherwise.

## In Carvercat

- Curve names on this page (quad out, quad in) are `ease` strings: [names](easing-reference.md#names-used-in-this-wiki).
- Template examples with measured numbers and lint traps for this principle: [craft principle page](../../ai/references/craft/principles/solid-drawing.md).
- Shadow: `dropShadow` such as `"0 13px 16px #00000066"` (x y blur colour; y is **down**, in px: the 0.1.6 note's stored Offset Y −0.012 is 0.012 × 1080 = 13 px down; the colour's alpha is the opacity); same values on every object of a scene ([shadow and glow](../techniques/shadow-and-glow-in-motion.md); old name: the `shadow` effect, [shadow](../../ai/references/effects/shadow.md)).
- Card turn: key `scale` X, faces on two clips cut on the zero frame; `Flip in (X)`
  preset (4.4% overshoot) in [Motion Patterns](../../ai/patterns/README.md).
- Layered depth: [parallax](../techniques/parallax.md) and [faux-3D](../techniques/faux-3d.md).
- Check: `carvercat_look` at the edge-on frame and the rest frames; `carvercat_inspect mode:probe` for widths.
- Lab: comp `W Depth` in [the principles lab](../labs/README.md).
