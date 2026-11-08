# Two-tone wipe (transition)

**Template:** `Two-tone wipe` (mp_tr_two_tone_wipe) · **Verified 0.1.8.1 (rev 1127)** · 48 f at 30 fps

Two full-frame bars sweep left to right: an accent bar leads and a brand-colour bar follows on top. The cut from Scene A to Scene B happens while the frame is fully covered.


**Measured** on `MP TR Two-Tone Wipe` (one definition for every number below: the lab comp rendered at 320x180, `starts` = first frame that differs from frame 0 by at least 0.5 (mean channel value, 0-255), `steady` = the frames whose picture matches the settled one within 0.5; harness `ai/scripts/motion/verify_pack.py`): first change f14, the wipe bars cover the whole frame (no scene colour left) from f22 to f28, so the cut at f24 is under cover; the picture is steady from f40; the template's last visible frame is f45 (harness `gone` = 46). Lint 0/0/0; shape difference against v1 0.00 %.

## Timing chart (comp frames)


```
Scene A          |=======================|                      0-23
Scene B                                   |====================| 24-47
Wipe 1 (accent)        12 >>>>>>>>>> 22 .... 28 >>>>>>>>>>>>> 41   accelerating in (cubic-bezier(0.333, 0, 0.667, 0.333)) to cover, hold, decelerating away (cubic-bezier(0.333, 0.667, 0.667, 1))
Wipe 2 (brand, top)       15 >>>>>>> 24 . 25 >>>>>>>>> 36          2-3 f behind on the way in, FIRST out
                                    ^ cut at 24 under full cover
```

## Build it by hand (MCP)

1. Make two rectangles, width 1958.4 px and height 1113.6 px (1.02 and 0.58 of the frame width; the frame is 1920 × 1080). Colour them, and put the brand bar on the track above.
2. Key `x` (the top-left of the bar): −1977.6 px (off-frame left) → −19.2 (cover) → hold → 1939.2 (off right). Put `ease: "cubic-bezier(0.333, 0, 0.667, 0.333)"` on the first key (accelerating arrival at the cover key) and `ease: "cubic-bezier(0.333, 0.667, 0.667, 1)"` on the hold key that leaves it (decelerating arrival at the off-right key). A key's `ease` shapes the segment that leaves it. Give `y` −16.8 px (centred vertically).
3. Wipe 2 enters 2–3 f after Wipe 1 and **leaves before it**, so the accent colour trails on the way out.
4. Put the scene cut (the end of A, the start of B) on a frame where both bars cover the whole frame.

## Knobs

- Direction: swap the x signs (right to left), or animate `y` with height 1113.6 px for a vertical wipe.
- Speed: 10 f in and 11–13 f out at 30 fps. Shorter than 8 f reads as a flash.
- Three tones: add a third bar 2 f behind; the exit order is still top first.

## Pitfalls

- If the top bar leaves last, the lower colour is hidden on the exit and the wipe reads as one colour (we hit this in the first build).
- `key.box` (retime keys) is not batchable; use `carvercat_run`.
- Add a whoosh SFX: start it about 3 f before the first bar enters and let it peak at the cover frame (`../references/craft/sound-design.md`).
