# Button press

**Template** `ct_button_press` · Cartoon Bounce pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `CT Button press` in `categories/cartoon-bounce/ct-lab-2`.

A chunky 480 × 150 px red button on an ink base 18 px below it, labelled "PRESS ME". 60 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Button top (anchor at its bottom edge) and Button label | 0 | down 18 px f18–21 (accelerating arrival cubic-bezier(0.333, 0, 0.667, 0.333)) with a squash to 105 × 88%; hold to f24; back up on a bouncy spring f24–38 | position and scale settle **f38** |
| Press ring | 21 | scale 0.9 → 1.35 (expo) and opacity 0.8 → 0 over 16 f | |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place so that f21 (contact) lands on the click sound. Pair with the SaaS [cursor click](su-cursor-click.md) for a pointer.

Inspiration: the squash of a pressed arcade button. No external text or code was used.
