# Motion blur

Motion blur has no design key: add it as an effect with `effect.add {id, cap: "motionblur"}` and set its two stored parameters. Verified: motion-blur-on-a-fast-slide (a 200 px square sliding 576 px in 8 f with `ease-out` renders a clear directional smear on the fast frames and none once it settles; `effect.add` answers "Motion blur added", the entry reads shutter 180 and samples 16, and `property.set {key: "fx.<entry>.shutter", value: 270}` reads back).

```json
{"command": "anim.set", "args": {"id": "#sq", "keyframes": [{"at": 0, "x": 160, "ease": "ease-out"}, {"at": 8, "x": 736}]}}
{"command": "effect.add", "args": {"id": "#sq", "cap": "motionblur"}}
{"command": "property.set", "args": {"id": "#sq", "key": "fx.e_fx_motionblur_clip_3.shutter", "value": 270}}
```

Find the entry path with `param.list {id, match: "motionblur"}`. It follows the object's OWN transform motion (position, scale, rotation): not optical flow, not parent or camera motion of other layers (measured on 0.0.72; the smear in the verified case is the object's own `x` keys).

| param | range | default | meaning |
|---|---|---|---|
| shutter | 0 to 360 | 180 | shutter angle in degrees: 180 is half a frame of travel (film look); 0 is none; 270 to 360 is heavy, stylised |
| samples | 2 to 64 | 16 | sub-frames averaged (Fusion "Quality"); 16 is fine; raise to 32 if you see stepping on very fast moves |

## When
- Any element covering more than about 1/20 of the frame width per frame (about 96 px per frame at 1920 wide): whips, pushes, zoom-throughs, fast slides.
- Not on slow drifts (invisible cost) and not on text that must be read mid-move.
- Transitions: put it on the moving layers (wipe bars, pushed scenes); the transitions guide assumes it.

## Pitfalls
- It only sees the object's own keys: a child moved by its parent, or content inside a moving nested comp, may not blur. Add motion blur on the moving object itself (the parent or instance).
- With a preset that uses many baked keys (linear joins; `motion.apply` and springs bake) the blur follows each segment: fine at 16 samples.
- To aim the streak yourself (a whip at a chosen angle and length) use [directional-blur.md](directional-blur.md): `directionalBlur "160px 0deg"`, keyed to 0 on landing. Motion blur is the realistic default; directional blur is the art-directed one.
- It is a stored effect, not a design key: it is not in `filter`; `carve.preflight` says how it carves.
