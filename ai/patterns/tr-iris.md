# Colour iris (transition)

**Template:** `Colour iris` (mp_tr_iris) · **verified 0.0.72** · 48 f

A circle in Scene B's colour grows from a point until it covers the frame, then Scene B is cut in underneath it.

## Timing

```
Scene A   |=============================|          0-29
Iris          12 ........ (expo in-out) ...... 30   scale 0 -> 6.5 (two keys + custom handles)
Scene B                                  |======|  30-47
```

## Steps

1. Ellipse (default diameter 0.2 W = 384 px). Fill it with Scene B's colour.
2. `key.set scale 0` at the start with `ease: "cubic-bezier(0.87, 0, 0.13, 1)"` (expo-in-out; the key that leaves carries the curve) and `scale S` at the end (see [custom-curves.md](custom-curves.md)).
3. S = frame diagonal ÷ diameter × 1.05. **Keep the disc big and the scale small:** diameter ≤ 1075 px (0.56 W, ≤ the frame height) and S ≤ ~2.5 — a 384 px disc scaled ×6 renders stair-stepped, and a shape whose geometry is larger than the frame is cropped to the frame before scaling (field test, 0.0.72). For 1920×1080: diameter 1056 px (0.55 W), S = 2203 / 1056 × 1.05 ≈ 2.2.
4. Move the circle (`x`, `y` are the top-left of its box) so its centre is on the subject (a button, a face, a product) so the iris opens from it. This is the "match cut" version.

## Knobs

- Reverse iris (close onto a point): run the keys backwards, from scale S to 0, over the end of Scene A.
- A ring instead of a disc: give the ellipse a stroke with no fill, and key `strokeWidth` as well.
