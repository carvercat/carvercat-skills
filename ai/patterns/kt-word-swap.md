# Word swap

**Template** `kt_word_swap` · Kinetic Typography pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `KT Word swap` in `categories/kinetic-typography/kt-lab`.

"We build" stays put. The accent word next to it rolls up to the next one: faster → smarter → together. ExtraBold 96 px, centred on the longest phrase.

| Word | Clip | Entrance | Exit |
|---|---|---|---|
| Word 1 "faster" | 10–46 | rises 120 px (1.25 × font size) from under the line, f10–22, Custom expo | f38–46 up 120 px, Custom accelerate (0.3, 0, 0.8, 0.15) |
| Word 2 "smarter" | 46–82 | f46–58 | f74–82 |
| Word 3 "together" | 82–120 | f82–94 | holds |

Measured: each entrance is a 12 f key pair (expo, no overshoot); peak speed 0.048 frame-height per frame on the first frame. Each word is clipped by its own window, a rectangle from the measured ink top − 6 px to the ink bottom (including the g's descender) + 6 px, wide enough for the widest word. Lint 0/0.

## Steps
1. Place and apply. To change the words, edit the texts inside the comp. If a new word is wider, widen all three windows to the widest word + 40 px.
2. For longer holds, lengthen each word clip and move its exit keys; the next word starts on the frame the previous exit ends.
3. To rebuild from scratch, run the `word_swap()` generator in `kinetic_type_lab.py`. It measures the phrase, the space and every word with `carvercat_authoring geometry`, then places the slot and windows.

## Pitfalls
- `property.set {id:"word", key:"mask", value:{"ref":"<window id>"}}`: the window is the mask, not the target ([pack pitfall 2](kinetic-typography.md#pitfalls-found-while-building-this-pack-016)).
- Overlapping the exit and the next entrance gives a "rolling" look but lint warns `text_overlap`. The template keeps them back to back.
