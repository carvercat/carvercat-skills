# Character hop

**Template** `ct_character_hop` · Cartoon Bounce pack · **verified 0.1.8.1 (rev 1127; headless, isolated folders, pack added to a scratch user Library)**, comp `CT Character hop` in `categories/cartoon-bounce/ct-lab-2`.

A green blob character (200 × 260 px, two eyes) hops 880 px to the right with anticipation, stretch, arc, squash and recovery, then blinks. 90 f.

| Part | Frames | Motion |
|---|---|---|
| Feet (the pivot; a visible ink oval at the contact point) | f10–18 | crouch: scale 115 × 80% (anticipation) |
| | f18–22 | launch: stretch to 85 × 120% |
| | f18–29–40 | the jump: up 340 px (decelerating arrival cubic-bezier(0.333, 0.667, 0.667, 1) to the peak), down (accelerating arrival cubic-bezier(0.333, 0, 0.667, 0.333) to the ground); the path is two straight legs, eased ([arcs](../references/craft/principles/arcs.md)) |
| | f40–41 | land: squash 125 × 75% |
| | f41–56 | recover: 92 × 108%, 103 × 97%, 100% (S curve cubic-bezier(0.333, 0, 0.667, 1)) |
| Body, Eye 1–2 | — | parented to Feet; eyes blink f64–70 |
| Hop shadow | f18–40 | follows on the ground, shrinks to 55% at the peak |

Measured: position settles **f40**, scale **f59**. Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0. The rig survives placement.

## How the rig is built
Body and eyes are parented to the Feet oval, and only the Feet move. In the project file a child's position is stored as an **offset from the comp centre** (measured on 0.1.6), so the lab writes `0.5 + (child − feet)` for each child ([../references/app/json-authoring.md](../references/app/json-authoring.md)).

## Pitfalls
- A fully transparent pivot null failed lint (`never_visible`, an error). The pivot is a visible part (the feet).
- Children written at their absolute positions landed displaced by (pivot − centre): the body appeared at the bottom-left corner.
- A recovery baked from a spring ended in sub-pixel wobbles that lint read as `jitter`. Three hand-set S curve keys fix it.
- Position is one point and travels in a straight line between keys (measured 2026-10-28), so the jump is two eased straight legs, not a curve, and its x also eases at the peak. For a true arc, bake the curve to keys every 2 f or nest the vertical move and slide the nest sideways ([../references/craft/principles/arcs.md](../references/craft/principles/arcs.md); [cartoon-bounce.md](cartoon-bounce.md) pitfall 2).

Inspiration: the classic principles of animation (anticipation, squash and stretch, arcs). No external text or code was used.
