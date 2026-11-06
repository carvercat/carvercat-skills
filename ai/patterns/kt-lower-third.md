# Kinetic lower third

**Template** `kt_lower_third` (Library name "Kinetic lower third") · Kinetic Typography pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `KT Lower third` in `categories/kinetic-typography/kt-lab-2`.

A 14 px accent bar at x 120 with an ExtraBold name and a Medium role to its right, bottom left. 150 f (5 s) with its own exit.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Accent bar (14×166 px, `#FF4D2E`) | 0 | scale Y 0 → 1 from its top edge (anchor 0, 1), f0–12, Custom expo; 1 → 0 over the last 10 f, accelerating | |
| Name ("MAYA ORTIZ", ExtraBold 76 px, y 840) | 4 | Letters zoom in; Exit down - accelerate (last 12 f) | opaque by **f10**, size settles **f15** |
| Role ("Creative director, Northwind", Medium 36 px, y 936) | 12 | Lines slide in - left; Exit fade - fast (last 8 f) | position settles **f28** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0, enters f0, exits f149.

## Steps
1. Place and apply over the speaker's shot. Edit the name and role inside the comp.
2. Longer hold: lengthen all three clips by the same amount; the exits are anchored to the clip ends.

## Pitfalls
- **Staggered presets cannot share a property on one text.** Both fade (`blend`), so Words exit down on the name was refused ("blend could not be staggered - that is already in a slot of the Stagger") because Letters zoom in already holds the Stagger. The name uses the non-staggered Exit down - accelerate instead.
- Letters zoom in starts each letter at 2.4×, so the first letters overhang the line below. With the role 72 px under the name, lint flagged `text_overlap` (24%); at 96 px it is clean.

Inspiration: broadcast lower thirds with a bold kinetic name. No external text or code was used.
