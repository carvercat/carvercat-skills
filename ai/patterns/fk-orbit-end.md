# Orbit end card

**Template** `fk_orbit_end` (Library name "Orbit end card") · Funky pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FK Orbit end card` in `categories/funky/fk-lab-2`.

A 300 px purple hub ("BYE!", yellow 110 px) with four coloured satellites on a 260 px orbit, and a handle below. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Orbit hub | 0 | Tilt pop; then rotation 0 → 120°, f18–150 (linear, one way) | size **16.2%**, settles **f16** |
| Satellite 1–4 | 0 | parented to the hub: they pop with it and orbit as it turns | |
| Hub text | 8 | Stamp, plus rotation −14° → 0 | |
| Follow | 24 | Slide in - wiggle | angle **30.3%**, settles **f43** |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0. The parenting survives placement.

## How it is built
The satellites are children of the hub. In the project file a child's position is an offset from the comp centre, so the lab stores `0.5 + (satellite − hub)` ([../references/app/json-authoring.md](../references/app/json-authoring.md)). The hub text is not parented, so it stays upright.

## Pitfalls
- Tilt pop from 0 on the 110 px hub text failed lint `text_too_small` (16.1 px at the start); Stamp fixes it.

Inspiration: orbiting-icon logo lockups. No external text or code was used.
