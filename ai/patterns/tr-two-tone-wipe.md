# Two-tone wipe (transition)

**Template:** `Two-tone wipe` (mp_tr_two_tone_wipe) · **verified 0.0.72** · 48 f at 30 fps

Two full-frame bars sweep left to right: an accent bar leads and a brand-colour bar follows on top. The cut from Scene A to Scene B happens while the frame is fully covered.

## Timing chart (comp frames)

```
Scene A          |=======================|                      0-23
Scene B                                   |====================| 24-47
Wipe 1 (accent)        12 >>>>>>>>>> 22 .... 28 >>>>>>>>>>>>> 41   Ease in to cover, hold, Ease out away
Wipe 2 (brand, top)       15 >>>>>>> 24 . 25 >>>>>>>>> 36          2-3 f behind on the way in, FIRST out
                                    ^ cut at 24 under full cover
```

## Build it by hand (MCP)

1. Make two rectangles, width 1.02 and height 0.58 (geometry is in frame-WIDTH units, so 0.5625 is full height at 16:9). Colour them, and put the brand bar on the track above.
2. Key `center` x: −0.52 (off-frame left) → 0.5 (cover, easing `Ease in`) → hold → 1.52 (off right, easing `Ease out`). `key.set` takes the easing of the segment ARRIVING at that key.
3. Wipe 2 enters 2–3 f after Wipe 1 and **leaves before it**, so the accent colour trails on the way out.
4. Put the scene cut (the end of A, the start of B) on a frame where both bars cover the whole frame.

## Knobs

- Direction: swap the x signs (right to left), or animate `center` y with height 0.58 for a vertical wipe.
- Speed: 10 f in and 11–13 f out at 30 fps. Shorter than 8 f reads as a flash.
- Three tones: add a third bar 2 f behind; the exit order is still top first.

## Pitfalls

- If the top bar leaves last, the lower colour is hidden on the exit and the wipe reads as one colour (we hit this in the first build).
- `key.box` (retime keys) is not batchable; use `carvercat_run`.
- Add a whoosh SFX: start it about 3 f before the first bar enters and let it peak at the cover frame (`../references/craft/sound-design.md`).
