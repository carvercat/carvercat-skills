---
id: principles/arcs
title: Arcs
section: principles
tags: [arcs, motion path, pivot, rotation, parenting, null, swing, trajectory]
styles: [cartoon-bounce, funky, explainer, sports]
topics: [motion path, rigging]
related: [principles/slow-in-slow-out, principles/follow-through-and-overlap, principles/weight, techniques/camera-moves-2d]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation, https://pixune.com/blog/arcs-in-animation/, https://blog.cg-wire.com/arc-animation-principle, https://lesterbanks.com/?p=65610, https://carbondesignsystem.com/elements/motion/choreography/]
---

# Arcs

Living things and thrown things move along curves: a swinging arm traces part of a circle, a tossed ball
traces a parabola. Straight diagonal paths look mechanical. In graphics, arcs make large moves feel
natural; UI-like moves stay straight on purpose.

## The idea

- **Swings** (limbs, signs, pendulums, needles) are circular arcs around a joint.
- **Throws and jumps** are parabolas: steady sideways speed, vertical speed slowing to the top and
  speeding up on the way down.
- Trailing parts follow their own, later arcs (see [follow-through](follow-through-and-overlap.md)).
- Natural arcs are rarely symmetric; the return is often slower or lower.
- Interface-style motion (cards, panels, menus) follows the grid in straight lines; arcs there look
  playful, which may or may not be the brief.

## Rules of thumb

- Moves longer than about 15% of the frame width that are not UI: give them an arc.
- Keep the arc shallow for product and brand work (a sag of 3–8% of the travel), deep for cartoon.
- Speed along an arc matters as much as its shape: ease into and out of the ends of a swing.
- Check arcs with an onion skin or a probe table, not by scrubbing.

## Measured in Carvercat: what makes an arc

**Position keys alone do not make a curve.** A dot keyed at (300, 800), (960, 300) and (1620, 800) with
S-curve easing travelled two straight lines meeting in a point: at f14 it was at (416, 712), exactly on
the straight segment. With S-curve on both segments it also stopped dead at the middle key, and
`inspect lint` flagged a `speed_jump` there. Easing changes speed along the path, never the path's shape.

**A rotating pivot null does make a true arc.** A dot parented to a pivot at (960, 1000) that rotates
from 60° to −60° travelled a circle of radius 500 px: (527, 750) at f10, (960, 500) at f25,
(1393, 750) at f40, every sample 500 px from the pivot.

| Way to get a curved path | Path | Measured | When |
|---|---|---|---|
| 3+ position keys, any easing | straight segments with corners | on the straight segments to within 0.05 px (craft page), 0 px here | never for an arc on its own |
| Bake the curve: a position key every 2 f, `linear` joins | smooth | a parabola stayed within 1.25 px of the true curve between keys (craft page) | any curve from a script; re-bake to retime |
| Separate the axes: vertical eased motion in a nested comp, horizontal `linear` motion of the nest in the master | parabola | verified by look (craft page) | jumps with constant sideways speed |
| Carrier null moving X with `linear`; child parented to it, keyed Y with quad out up and quad in down | parabola | below | the same idea without a nested comp |
| Pivot null + rotation, child parented | exact circle | radius held at 500 px, below | swings, needles, orbits, pendulums |

The craft page [arcs](../../ai/references/craft/principles/arcs.md) measured the first three rows (0.1.6,
2026-10-28) and lists which Library templates have true arcs and which use straight, eased legs.

**A carrier null makes a parabola.** A null moving from x 300 to x 1620 in 30 f (`linear`) carried a
parented dot keyed 500 px up (quad out, apex at f25) and back down (quad in): (476, 569) at f14,
(960, 300) at f25, (1444, 569) at f36. Even sideways steps of 44 px a frame, vertical speed slowing to
the apex and speeding up after it: a thrown-object path.

Positive `rotate` turns clockwise on screen: the pivot keyed from `"-60deg"` up to `"60deg"` carried
the dot clockwise from the left, over the top, to the right (the 0.1.6 note had the stored rotation keyed 60° down to −60°).

## Do and don't

- Do use a pivot null at the joint for anything that swings ([rigging](../../ai/references/drawing/rigging.md)).
- Do keep camera-like moves and UI moves straight.
- Don't expect easing to bend a path.
- Don't offset a middle key to "curve" a move: it makes a corner, and an eased middle key also makes the object stop there.

## Checklist

- [ ] Long non-UI moves travel on a curve.
- [ ] Swings rotate about a real joint (a pivot null), not position keys.
- [ ] No unintended stop at a middle position key (`lint` shows no `speed_jump` there).
- [ ] An onion-skin look (`carvercat_look {onion:true}`) shows an even curve.

## In Carvercat

- Curve names on this page (S-curve, quad out, quad in) are `ease` strings: [names](easing-reference.md#names-used-in-this-wiki).
- Template examples with measured numbers and lint traps for this principle: [craft principle page](../../ai/references/craft/principles/arcs.md).
- Pivot null: a tiny ellipse (0.002 of comp width, 4 px at 1920) at the joint, `opacity` 0,
  `transformOrigin` `"50% 50%"`; key `rotate` on it.
- Parent over MCP: `view.seek` to a frame where the pivot is at its rest angle, `select.clip` the child,
  `select.add` the pivot, then `parent.assign`. On 0.1.6 the **active (last selected) object becomes the
  parent**; the reply names it ("parented 1 to Pivot"). Use `dry_run:true` first.
- In design units a child's `x`, `y` are from its **parent's top-left** (px, y down); `scene.apply` parents by nesting (`children` of a `group`). In a project file,
  parenting is: `parentId` on the child, an effects entry
  `{"id": "e_fx_parent_<clip id>", "cap": "parent", "on": true}` on both child and parent, and the child's
  position stored **relative to the parent** as 0.5 + offset (x as a fraction of comp width, y up as a
  fraction of height). The parabola above was written this way and measured. Comp-space positions with
  only `parentId` put the child in the wrong place.
- `inspect lint` reports an invisible pivot null as an error `never_visible`. For a null that is
  intentional; ignore it.
- Templates with swings: `Swing in` and `Words swing in` ([Motion Patterns](../../ai/patterns/README.md)),
  `Gauge` needle ([dv-gauge](../../ai/patterns/dv-gauge.md)).
- Lab: comp `W Arcs` in [the principles lab](../labs/README.md).
