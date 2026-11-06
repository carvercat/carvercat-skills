---
id: principles/follow-through-and-overlap
title: Follow-through and overlapping action
section: principles
tags: [follow-through, overlap, offset, delay, drag, settle, container, content]
styles: [all]
topics: [choreography, settle]
related: [principles/secondary-action, principles/arcs, principles/rhythm, techniques/stagger-systems, principles/weight]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.schoolofmotion.com/blog/animation-tricks-follow-through-after-effects, https://pixune.com/blog/follow-through-and-overlapping-action/, https://lesterbanks.com/?p=35455, https://cgcookie.com/community/20795-delaying-keyframes, https://uxmag.com/articles/creating-usability-with-motion-the-ux-in-motion-manifesto]
---

# Follow-through and overlapping action

Nothing made of parts stops all at once. When the main body stops, loose parts keep going and settle a
little later (**follow-through**); while it moves, its parts start and stop at slightly different times
(**overlap**, also called offset and delay).

## The idea

- A card lands; its contents land a beat later, as if carried by momentum.
- A character stops; the hair, the scarf and the antenna keep swinging, each smaller than the last.
- On exit the order reverses: the contents leave first, then the container.
- In interface-style motion, the same idea becomes "offset and delay": related items share the move but
  not the start frame, which tells the viewer they belong together but are separate.

## Rules of thumb

- Children lag their parent 2–5 f; each further level of looseness adds 1–3 f.
- The follower travels a little further or overshoots a little more than the leader.
- Total spread from first landing to last landing: 4–10 f for UI and brand, up to 15 f for cartoon.
- Exits: content first, container 2–4 f later, both accelerating.
- Hold the whole group still after the last part lands.

## Measured in Carvercat

A card and two content bars, all with expo-out keys (`cubic-bezier(0.16, 1, 0.3, 1)`):

| Object | Keys | Travel | Starts moving | Settles |
|---|---|---|---|---|
| Card | f6 → f24 | 120 px | f7 | f19 |
| Content | f9 → f29 | 150 px | f10 | f24 |
| Content 2 | f12 → f33 | 170 px | f13 | f28 |

(`carvercat_inspect mode:timing`.) Starting 3 f apart with slightly longer, further moves spread the
landings over 9 f (f19, f24, f28): the content visibly "catches up" with the card. With identical keys on
all three, the group moved as one rigid block.

## Do and don't

- Do key the leader first, then copy its keys to the followers and shift them later.
- Do reverse the order on exit (content out, then container).
- Don't let followers lag so far that they read as separate events (more than about 8 f between
  neighbours).
- Don't add follow-through to text the viewer is already reading.

## Checklist

- [ ] Leader settles first; each follower 2–5 f later.
- [ ] Followers travel equal or further, never less.
- [ ] Exit order is the reverse of the entrance.
- [ ] `inspect timing` settle frames form an even cascade.

## In Carvercat

- Template examples with measured numbers and lint traps for this principle: [craft principle page](../../ai/references/craft/principles/follow-through-and-overlap.md).
- Offset keys in time: in a project file, add the lag to each follower's key frames; over MCP, use
  `key.box` to move a block of keys (`to_start`, `to_end`).
- For words and letters, the Stagger Text effect does overlap for you: `stagger.set {by:"word", gap:3}`
  (see [stagger systems](../techniques/stagger-systems.md)).
- Parenting gives perfect follow without lag; add a small extra key on the child (`x` and `y`
  or `rotation`) for the follow-through on top ([rigging](../../ai/references/drawing/rigging.md)).
- Ready-made: `Card settle` and `Soft rise` ([Corporate Brand](../../ai/patterns/corporate-brand.md)),
  `Card lift` ([SaaS UI](../../ai/patterns/saas-ui.md)), `UI card stack` recipe
  ([ui-card-stack](../../ai/patterns/ui-card-stack.md)).
- Lab: comp `W Follow-through` in [the principles lab](../labs/README.md).
