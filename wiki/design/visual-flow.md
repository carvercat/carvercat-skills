---
id: design/visual-flow
title: Visual flow and eye path
section: design
tags: [eye path, visual flow, reading order, z pattern, f pattern, leading lines, direction, continuity]
styles: [all]
topics: [composition, attention, continuity]
related: [design/visual-hierarchy, design/gestalt, principles/staging, techniques/match-cuts, techniques/line-drawing]
verified: no (theory only)
source_inspiration: [https://uxplanet.org/f-shaped-pattern-for-reading-content-80af79cd3394?gi=6bbb73c40ed0, https://blog.geveo.com/UX-enhancing-design-layouts, https://carbondesignsystem.com/elements/motion/choreography/, https://www.studiobinder.com/blog/match-cuts-creative-transitions-examples/]
---

# Visual flow and eye path

The eye takes a path through every frame and from one frame to the next. Good motion design plans that path:
where the eye lands first, where it goes next, and where it is when the cut happens, so the next scene starts
right where the eye already is.

## The idea

- **Within a frame**: sparse frames are scanned in a Z (top-left, top-right, diagonal, bottom); dense,
  text-heavy frames in an F (two horizontal sweeps, then down the left). In right-to-left languages, mirror it.
- **Motion leads the eye**: the eye follows a moving object and continues in its direction after it stops.
  Place the next element where that momentum points.
- **Across cuts**: the eye is still where the last action happened. Start the next scene's focal point near
  that spot (or deliberately far, for a jolt).
- **Screen direction**: keep a consistent direction for "forward" (in left-to-right cultures, left to right).
  Reverse it only to mean "back", "return" or "conflict".
- **Leading lines**: lines, gazes, pointing shapes and drawn paths all point the eye.

## Rules of thumb

- Hand off attention: the next element starts moving as the previous one settles (0–4 f overlap).
- The exit direction of scene A matches the entrance direction of scene B.
- Keep the focal point within the central two thirds across a sequence; big jumps across the frame make the
  viewer hunt for the subject again.
- Calls to action go where the eye ends (bottom-right of a Z in left-to-right layouts, or the centre after a
  centred build).

## Do and don't

- Do sketch the eye path on the storyboard as arrows.
- Do use a moving element (pointer, line, highlight) to carry the eye to the next point.
- Don't make the eye ping-pong between corners.
- Don't cut away while the eye is still travelling to the payoff.

## Checklist

- [ ] Each frame's first, second and third look are planned.
- [ ] Exit direction and next entrance direction agree.
- [ ] The focal point at the cut is near the next scene's first focal point (or the jump is deliberate).

## In Carvercat

No new Carvercat measurements on this page. How to check flow:

- `carvercat_look {from, to, fps:4, overlay:["ids"]}` shows the sequence as a contact sheet; follow the focal
  point from cell to cell.
- `carvercat_look {onion:true}` ghosts a move into one picture: the path and its direction at a glance.
- `carvercat_inspect {mode:"expect", checks:["\"A\" left of \"B\" at 30"]}` locks spatial relationships.
- Carry the eye with a drawn path ([line drawing](../techniques/line-drawing.md)), a pointer
  (`Cursor click`, [su-cursor-click](../../ai/patterns/su-cursor-click.md); `Pointer callout`,
  [ex-callout](../../ai/patterns/ex-callout.md)) or a match cut ([match cuts](../techniques/match-cuts.md)).
- Continuity rules for promos: [motion principles §4](../../ai/references/craft/motion-principles.md).
