# Push (slide) transition

**Recipe** · **verified 0.0.72** (comp `RECIPES` in `categories/motion-patterns/pattern-lab/project.carverproj`, frames 0–48) · 15 f

Scene A slides out while Scene B slides in behind it, both on the SAME curve, so they stay locked edge to edge.

## Steps (MCP)

```json
{"steps":[
 {"command":"key.set","args":{"id":"A","key":"center","value":[0.5,0.5],"easing":"Linear"},"frame":16},
 {"command":"key.set","args":{"id":"A","key":"center","value":[-0.5,0.5],"easing":"Linear"},"frame":31},
 {"command":"key.handle","args":{"id":"A","path":"tr.e_tr_placement_A.position","frame":16,"side":"out","x":0.7,"y":0,"tied":false}},
 {"command":"key.handle","args":{"id":"A","path":"tr.e_tr_placement_A.position","frame":31,"side":"in","x":0.2,"y":1,"tied":false}},
 {"command":"key.set","args":{"id":"B","key":"center","value":[1.5,0.5],"easing":"Linear"},"frame":16},
 {"command":"key.set","args":{"id":"B","key":"center","value":[0.5,0.5],"easing":"Linear"},"frame":31},
 {"command":"key.handle","args":{"id":"B","path":"tr.e_tr_placement_B.position","frame":16,"side":"out","x":0.7,"y":0,"tied":false}},
 {"command":"key.handle","args":{"id":"B","path":"tr.e_tr_placement_B.position","frame":31,"side":"in","x":0.2,"y":1,"tied":false}}
]}
```
Replace `A` and `B` with the real clip ids. When the scenes are nested comps, key the comp instances.

## Knobs

- Curve: (0.7, 0, 0.2, 1) is a strong in-out. For a softer push use (0.65, 0, 0.35, 1).
- Length: 12–18 f. Add a whoosh that peaks at the middle frame.
- Direction: swap the signs, or move y for a vertical push. Both scenes must use the same frames and the same handles.

## Pitfalls

- A 1 px seam can flash between the two edges on one frame (we saw it at f17). Make each scene 0.2% wider (width 1.002) so the edges overlap.
- The presets `Exit left - accelerate` and `Slide from right - expo` move only 9–10% of the frame. They are for elements, not a full-frame push.
