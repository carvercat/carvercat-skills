---
id: design/gestalt
title: Gestalt principles in motion
section: design
tags: [gestalt, proximity, similarity, common fate, closure, continuity, figure ground, grouping, pragnanz]
styles: [all]
topics: [perception, composition, choreography]
related: [design/negative-space, design/visual-flow, techniques/stagger-systems, principles/follow-through-and-overlap, techniques/masking]
verified: no (theory only)
source_inspiration: [https://en.wikipedia.org/wiki/Gestalt_psychology, https://www.ixdf.org/literature/topics/gestalt-principles, https://www.toptal.com/designers/ui/gestalt-principles-of-design, https://uxmag.com/articles/creating-usability-with-motion-the-ux-in-motion-manifesto]
---

# Gestalt principles in motion

Gestalt psychology describes how we see wholes rather than parts: we group, complete and simplify what we
see. Every layout uses these rules whether the designer knows them or not. Motion adds one rule that
outranks the rest: **things that move together belong together**.

## The idea

| Principle | What we perceive | In motion graphics |
|---|---|---|
| Proximity | near things form a group | a label close to its bar belongs to it; animate them together |
| Similarity | alike things (colour, shape, size) form a group | all "positive" values share a colour; all buttons share a shape |
| **Common fate** | things moving the same way at the same time form a group | the strongest grouping in motion: a card and its content rise together; a stagger reads as one wave |
| Continuity | the eye follows smooth lines and curves | a line drawing leads to the next element; motion paths guide the eye |
| Closure | we complete incomplete shapes | a ring drawn 90% reads as a circle; a logo can be implied by parts |
| Figure and ground | we split the scene into object and background | a mask edge decides which is which; a wipe can flip them |
| Common region | things inside one boundary form a group | a card or panel groups its contents |
| Prägnanz (simplicity) | we read the simplest interpretation | complicated paths are read as simple ones; keep moves simple |

- **Breaking a group on purpose** is emphasis: the one item that moves differently, or the one red bar.
- The phi phenomenon (apparent motion between flashes) is a Gestalt finding, and the reason frame-based
  animation works at all.

## Rules of thumb

- Group by motion first: give a group one shared move (same direction, same easing, staggered start).
- Separate groups by motion contrast: a different direction or a clearly later start (10+ f).
- Keep labels within about one line-height of what they label, and animate them with it.
- Use closure for elegant reveals: draw 80–95% of a shape and let the eye finish it.

## Do and don't

- Do let related things share fate (direction, timing family).
- Do make the odd one out the thing you want noticed.
- Don't move unrelated items in the same direction at the same time; viewers will assume a relationship.
- Don't separate a label from its object during a move.

## Checklist

- [ ] Each group shares one move; different groups have visibly different moves or timing.
- [ ] Labels travel with their objects.
- [ ] Only the emphasised item breaks the pattern.

## In Carvercat

No new Carvercat measurements on this page. How to apply it:

- Common fate: parent a group to a null and animate the null, or `edit.group` and animate the group
  ([rigging](../../ai/references/drawing/rigging.md)); staggered common fate: [stagger systems](../techniques/stagger-systems.md).
- Common region: a rectangle behind a group (a rectangle with `borderRadius`; old: `shape.geometry.rectangle` `Corner radius`).
- Closure: `trimEnd` stopped short of `"100%"`, e.g. `"92%"` (old: the `trim` effect `End` 0.92) ([line drawing](../techniques/line-drawing.md)).
- Figure and ground: masks and inverted masks ([masking](../techniques/masking.md)).
- Check grouping order: `carvercat_inspect {mode:"timing"}` shows which objects start and settle together.
