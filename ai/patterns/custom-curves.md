# Any cubic-bezier, exactly: one `ease` on the key that leaves

**Verified 0.0.72** (with `key.handle` in the stored format). A CSS / After Effects / Figma `cubic-bezier(x1, y1, x2, y2)` is written as it is: in design units a key's `ease` shapes the segment that leaves it, as in CSS, and the app writes the two handles.

| Bezier term | Carvercat |
|---|---|
| x1, y1, x2, y2 | `ease: "cubic-bezier(x1, y1, x2, y2)"` on the first key of the move (`anim.set` keyframes, or `key.set {id, key, value, at, ease}`) |

`x` is a fraction of the gap between the two keys (0..1). `y` is a fraction of the value change, from −1.5 to 2.5, so **y > 1 overshoots** and y < 0 winds up. Read it back with `key.list` / `anim.get`, which show the CSS ease leaving each key.

Measured (0.0.72, stored form): a move from 0.2 to 0.8 over 20 f with (0.16, 1, 0.3, 1) matched the expo-out formula to 3 decimals on every frame. With easeOutBack (0.34, 1.56, 0.64, 1), `inspect curves` reported **9.7% overshoot**, the same as the CSS curve.

```json
{"command": "anim.set", "args": {"id": "#clip", "keyframes": [
  {"at": 0,  "x": <x0>, "ease": "cubic-bezier(0.16, 1, 0.3, 1)"},
  {"at": 20, "x": <x1>}]}}
```

The last key's ease is not stored. In the stored format (what the measurement above used) the same move was two keys with easing Linear plus `key.handle {path, frame: <first key>, side: "out", x: x1, y: y1, tied: false}` and `key.handle {path, frame: <second key>, side: "in", x: x2, y: y2, tied: false}`, where `path` is the stored parameter path that `param.list` prints (for example `tr.e_tr_placement_<id>.position`); `tied:false` was always needed, or the opposite handle of the key moved too.

## The vocabulary (from `../references/craft/motion-principles.md`)

| Name | x1 | y1 | x2 | y2 | Feel |
|---|---|---|---|---|---|
| expo-out | 0.16 | 1 | 0.3 | 1 | fast arrival, long soft landing; the default entrance |
| emphasized-decel | 0.05 | 0.7 | 0.1 | 1 | calm, editorial entrance |
| standard | 0.2 | 0 | 0 | 1 | on-screen moves, A → B |
| emphasized-accel | 0.3 | 0 | 0.8 | 0.15 | exits |
| expo-in-out | 0.87 | 0 | 0.13 | 1 | transitions, wipes, iris |
| back-out | 0.34 | 1.56 | 0.64 | 1 | about 10% overshoot, a cheap spring |
| back-in | 0.36 | 0 | 0.66 | −0.56 | wind-up before an exit |

## Springs and bounces

A cubic cannot do two overshoots (a real spring, a bounce). For those, bake the curve:

- `ai/scripts/motion/curves.py` has `spring(zeta)`, `spring_physics(mass, stiffness, damping, fps)` (Remotion/Framer parameters → frames), `bounce()` and `anticipate_out()`.
- `bake(curve, frames, tol)` returns the fewest keys for which a linear join stays within `tol` of the true curve. Write those keys with `key.set` (`ease: "linear"`) or put them in a preset (see `build_pattern_pack.py`).

Remotion's default spring (mass 1, stiffness 100, damping 10) = damping ratio 0.5 = **16% overshoot, settled in 28 f at 30 fps**. A damping ratio of 0.7 gives about 4.6%.

## When to use which

- **Presets** for anything reusable on one object: one click for the person, and the curve travels with the file.
- **Two keys + handles** when the person will edit the move later: it gives clean, editable curves in the curve editor.
- **Baked keys** only for springs and bounces, and keep them in a preset so nobody has to edit 12 keys by hand.
