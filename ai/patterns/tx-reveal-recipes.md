# Reveal transitions (4 recipes)

**Recipes** · Transitions pack · **verified 0.1.8.1 (rev 1127 build; `ai/scripts/motion/verify_pack.py transitions --lab transitions_lab`)**, comps `TX Shape reveal`, `TX Line sweep`, `TX Whip pan`, `TX Zoom blur punch` in `categories/transitions/tx-lab`. Each needs your two scenes, so build it in place. Scene A and Scene B are your nested comps or footage clips.

## Shape reveal (24 f)
1. Put scene B above scene A from the start of the reveal.
2. Add a star (5 points, inner radius 0.5) **1000 px** wide at the centre, from the same frame.
3. `property.set {id: <scene B>, key: "mask", value: {"ref": "<star id>"}}`, then `parent.clear {ids:[star, scene B]}`.
4. Key the star's scale 0 → 5.0 over 24 f (`cubic-bezier(0.7, 0, 0.84, 0)`), then a slow 5.0 → 5.3 to the end of the clip. Key its rotation +40° → 0 clockwise (stored −40°, expo).

Measured: the picture changes from f18 (the star is still small) and is settled at f27. Lint 0/0/0. At scale 5 the inner radius (1250 px) passes the frame half-diagonal (1101 px), so scene B is fully shown.

## Line sweep (24 f)
1. Put scene B above scene A, and add a frame-size rectangle "window" one frame width to the left.
2. Mask scene B with it (window first, then `parent.clear`).
3. Key the window's `x` −1 W → 0 (the frame width) over 24 f (`cubic-bezier(0.65, 0, 0.35, 1)`).
4. Add an 8 px white line with Glow (stored size 12, amount 0.6) at x 0, keyed 0 → +1 W on the same frames: it rides the window's right edge.

Measured: the picture changes from f4 and is settled at **f27**. Lint 0/0/0.

## Whip pan (14 f around the cut)
1. Scene A: hold until 8 f before the cut. Then key position 0 → −1 W and scale X 1 → 1.4 (accelerating) by the cut.
2. Scene B: from the cut, key position +1 W → 0 and scale X 1.4 → 1 over 7 f (expo).
3. Add the **Motion blur** effect to both, shutter 360.

Measured: the picture changes from f9 and is settled at **f21**. Lint 0/0/1 (the speed jumps of the whip, intended). Add a whoosh 4 f before the cut.

## Zoom blur punch (23 f around the cut)
1. Scene A: scale 1 → 2.6 and a Gaussian blur 0 → 46 px (stored value 40) over the 11 f before the cut (accelerating).
2. Scene B: from the cut, scale 1.5 → 1 (expo, 12 f) and blur 46 px → 0 (expo, 10 f).

Measured: the picture changes from f8 and is settled at **f20**. Lint 0/0/0. This is a blurred variant of Motion Patterns' [zoom-through](tr-zoom-through.md).

The measures use one definition: "changes from" is the first frame whose picture differs from frame 0, "settled" the first frame from which it equals the last frame (mean channel difference below 0.5/255, 320 x 180 render).
