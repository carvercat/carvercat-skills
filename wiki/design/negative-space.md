---
id: design/negative-space
title: Negative space
section: design
tags: [negative space, white space, breathing room, figure ground, minimalism, focus, margins]
styles: [minimal-luxury, corporate-brand, saas-ui, all]
topics: [composition, attention]
related: [design/visual-hierarchy, design/gestalt, design/grids-and-layout, principles/staging, history/swiss-international-style]
verified: no (theory only)
source_inspiration: [https://en.wikipedia.org/wiki/Negative_space, https://designmodo.com/negative-space/, https://www.nngroup.com/articles/principles-visual-design/]
---

# Negative space

Negative space is everything that is not the subject: the margins, the gaps, the quiet area around a word.
It is not empty; it is what gives the subject its shape and importance. In motion, negative space also
exists in **time**: pauses and still frames are the negative space of a sequence.

## The idea

- **Space signals importance**: the more room around something, the more precious it looks. Luxury brands
  use this deliberately; discount flyers do the opposite.
- **Space groups and separates**: small gaps join items, large gaps split them (see [Gestalt](gestalt.md)).
- **Figure and ground** can swap: the gap between two shapes can itself form a shape (a hidden arrow, a
  face between two profiles). In motion, a shape can be revealed by the space around it closing in.
- **Temporal space**: a beat of stillness before a reveal makes the reveal land. A film with no pauses has
  no emphasis.

## Rules of thumb

- Leave at least 30–40% of a hero frame empty; minimal styles 60% or more.
- Margins around a hero at least its own cap height; between groups at least twice the gap within a group.
- One idea per frame: if two ideas share a frame, they fight for the space.
- Hold a composed, still frame for at least 1–1.5 s before the next change.
- Animate into space, not out of it: elements arriving into an empty area read clearly; elements arriving
  into clutter disappear.

## Do and don't

- Do design the empty areas as carefully as the filled ones.
- Do use space, not boxes and lines, to separate groups where possible.
- Don't fill space because the client "paid for the whole frame".
- Don't let motion paths cut through the breathing room of another element.

## Checklist

- [ ] The hero has generous, even space around it.
- [ ] Gaps between groups are clearly larger than gaps within groups.
- [ ] Every sequence has at least one held, quiet frame.

## In Carvercat

No new Carvercat measurements on this page. Tools that help:

- Measure gaps: `carvercat_authoring {mode:"geometry", id}` gives an object's bounds; subtract neighbours.
- Keep space clear: `carvercat_authoring {mode:"validate", checks:[{type:"no_overlap", ids:[...]}]}` with
  `tolerance_px` set to the minimum gap you want.
- Find still stretches and whether a scene breathes: `carvercat_inspect {mode:"timing"}` lists
  `still_spans`.
- Styles built on space: [Minimal Luxury](../../ai/patterns/minimal-luxury.md) (slow fades, wide tracking),
  [Corporate Brand](../../ai/patterns/corporate-brand.md).
