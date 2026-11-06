# Push (slide) transition

**Recipe** · **verified 0.0.72** (comp `RECIPES` in `categories/motion-patterns/pattern-lab/project.carverproj`, frames 0–48) · 15 f

Scene A slides out while Scene B slides in behind it, both on the SAME curve, so they stay locked edge to edge.

## Steps (MCP)

```json
{"steps":[
 {"command":"key.set","args":{"id":"A","key":"x","value":0,"atComp":16,"ease":"cubic-bezier(0.7, 0, 0.2, 1)"}},
 {"command":"key.set","args":{"id":"A","key":"x","value":-1920,"atComp":31}},
 {"command":"key.set","args":{"id":"B","key":"x","value":1920,"atComp":16,"ease":"cubic-bezier(0.7, 0, 0.2, 1)"}},
 {"command":"key.set","args":{"id":"B","key":"x","value":0,"atComp":31}}
]}
```
Replace `A` and `B` with the real clip ids. Full-frame scenes at rest sit at x 0, y 0 (1920 × 1080); the curve is on the key that leaves, so the first key of each scene carries it and the last key has none. When the scenes are nested comps, key the comp instances.

## Knobs

- Curve: (0.7, 0, 0.2, 1) is a strong in-out. For a softer push use (0.65, 0, 0.35, 1).
- Length: 12–18 f. Add a whoosh that peaks at the middle frame.
- Direction: swap the signs, or move y (±1080 px) for a vertical push. Both scenes must use the same frames and the same handles.

## Pitfalls

- A 1 px seam can flash between the two edges on one frame (we saw it at f17). Make each scene 0.2% wider (width 1.002, stored value) so the edges overlap.
- The presets `Exit left - accelerate` and `Slide from right - expo` move only 9–10% of the frame. They are for elements, not a full-frame push.
