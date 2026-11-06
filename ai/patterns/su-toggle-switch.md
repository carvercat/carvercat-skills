# Toggle switch

**Template** `su_toggle_switch` · SaaS UI pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SU Toggle switch`.

An off-to-on switch drawn at 2× desktop size so it reads in a full video frame: a 240×128 px track and a 104 px knob, centred.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Knob | 14–24 | position −56 → +56 px, Custom cubic-bezier(0.34, 1.2, 0.64, 1) | **1.1% overshoot, settles f23** |
| Knob stretch | 14–26 | scale X 1 → 1.12 (f18, decelerating arrival cubic-bezier(0.333, 0.667, 0.667, 1)) → 1 (f26, S curve cubic-bezier(0.333, 0, 0.667, 1)) | settles **f26** |
| Track on (accent) | 14–24 | opacity 0 → 1, decelerating arrival cubic-bezier(0.333, 0.667, 0.667, 1) | f24 |
| Track off (grey `#D5D8E0`) | 14–24 | opacity 1 → 0 | f24 (no grey rim left round the on state) |

## Steps
1. Place and apply. Scale the instance for smaller UI (0.5 = desktop size).
2. With Cursor click: put the cursor instance so that its f28 (ripple) is the switch's f14. In the showcase the switch starts at 230 and the cursor at 230 with `sourceIn` 14.
3. For on to off, swap the knob's two position values and swap the two tracks' opacity keys.

## Pitfalls
- `cornerRadius` tops out at 0.5, which is not a pill. The track is a 2-point path with a round-capped 128 px stroke.
- Keep the stretch at 12% or less. At 22% the knob poked past the track end during the overshoot (seen in the look).
