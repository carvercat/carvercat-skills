# Kanban drag

**Template** `su_kanban_drag` (Library name "Kanban drag") · SaaS UI pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SU Kanban drag` in `categories/saas-launch/saas-ui-lab-3`.

For briefs like "project management", "move work forward", "drag and drop". A three-column board (To do, In progress, Done: 440×520 px columns) with four cards (376×110 px, title Medium 26 and a colour tag). The cursor picks up "Ship pricing page", carries it to Done over a dashed drop slot and drops it; the card below in To do moves up to close the gap. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Columns and titles | 0, 3, 6 | lift (24 px) | |
| Cards (title and tag parented to the card) | 8, 11, 14, 17 | lift (24 px); contents fade in 3 f later | Card A opaque **f15** |
| Cursor (the round-1 cursor shape at 2×, pivot on its tip) | 24 | in from lower right f24–40 (S curve cubic-bezier(0.333, 0, 0.667, 1)), press to 0.85 at f42–45, release f84–90, out f102–120 | |
| Card A grab | f42–48 | up 8 px, scale 1.04, tilt −3° (stored value), decelerating cubic-bezier(0.333, 0.667, 0.667, 1) | |
| Card A carry and drop | f48–84, f84–96 | S curve cubic-bezier(0.333, 0, 0.667, 1) to Done; drop: scale, tilt and height back with the small spring | position within 0.5% from **f88**; scale settles **f95**, tilt **f96** |
| Drop slot (dashed outline) | 50 | opacity in f50–58, out f84–89 | |
| Card B closes the gap | f88–102 | up 130 px (expo) | settles **f97** |

Lint 0 errors, 0 warnings (13 notes). Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (12 px, a card title to its tag).

## Steps
1. Place and apply. Edit column titles and card titles (about 20 characters at 26 px).
2. A different target: change Card A's carry keys and the cursor's keys by the same offset (both move together), and move the drop slot.
3. In a product film, cut to this after a title; 150 f gives the eye time to follow one card.

## Pitfalls
- **Draw order is creation order:** the dragged card must be made after every card it passes over. The first build made it first and it slid *under* "Migrate billing".
- The cursor is not parented to the card; it carries the same keys and easing. Tilting the card turns it about its centre, so the cursor tip drifts about 6 px from the grab point at −3° (stored value); that reads as natural.
- `curves` reports large "overshoot" numbers for the cursor's position and Card A's size: those are several moves read as one. The look shows none beyond the small spring.

Inspiration: drag-and-drop conventions of task boards. No external text or code was used.
