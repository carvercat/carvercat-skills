# Stagger text (per-word, per-letter, per-line)

A stagger is a tween plus the text's stagger card: `anim.set {id, from|to|fromTo, duration, ease, stagger: {target, each|amount, from, ease}}`. Every part of the text plays the tween, offset in time. Verified: stagger-variants, stagger-exit-by-movement, stagger-manual-card, stagger-preset-apply. On 0.0.72 the 7 staggered presets of the Motion Patterns pack (word rise, letter cascade, word pop, line reveal, letter shimmer, word swing, word exit) on Open Sans were verified; the manual build below comes from earlier verified jobs (0.0.69+) and was re-run here.

## Fast path
```json
{"command": "anim.set", "args": {"id": "#title", "from": {"opacity": 0, "y": "+=40px"}, "duration": "0.5s", "ease": "ease-out",
  "stagger": {"target": "words", "each": "100ms", "from": "start"}}}
```
(verified: stagger-variants). `y: "+=40px"` is relative to the value at the start: the parts rise 40 px into place. Also in a scene document: `s.stagger("title", by="chars", each="30ms", from_="center", keyframes=[...])` in `cc_scene.py` (verified: text-stagger-gsap-style).

| stagger key | values |
|---|---|
| `target` | `chars`, `words`, `lines` |
| `each` or `amount` | `each` is the gap between parts; `amount` is the total spread. Both round to whole frames (`"80ms"` at 30 fps is 2 f); the reply lists it under `units.anim.rounded` |
| `from` | `start`, `end`, `center`, `edges`, `random` |
| `ease` | a CSS curve that distributes the delays (`ease-in-out` bunches them toward the ends); a spring or steps is refused |

Not available, with the reason in the refusal: `seed` (there is no seed key: `from: random` is not repeatable from the call; the manual card below has a `seed`), `copies`, `grid`/`axis`, a colour or `blur` as a staggered property (blur is not a design key in a tween; use the manual build). A stagger needs a text, and a keyframes list does not take a stagger (use `from`, `to` or `fromTo`). A stagger asked for again replaces the first: the same call twice leaves the same keys, and `stagger.list` shows the one card (verified: stagger-restated-and-read-back). Asking for `blur` in a stagger tween is still refused ("a stagger plays opacity, x, y, rotate and scale per part"); use the manual build for a per-letter blur.

Also available as a preset: `preset.apply {name: "Words rise - expo", id}` creates the card, connects its lanes and sets by, order and gap (verified: stagger-preset-apply; it is refused with "already in a slot" if a stagger card already uses the channel). See [../../patterns/README.md](../../patterns/README.md).

## Manual build (any combination; verified: stagger-manual-card)
1. `stagger.new {id}` then `stagger.connectable {id}` lists what a slot can take: `text.position`, `text.scale`, `text.rotation`, `text.anchor`, `text.opacity`, `fill.opacity`, `fill.blur`, `stroke.opacity`, `stroke.blur`, and `transform.*` (which MOVES the object's keys onto the relative row).
2. `stagger.connect {id, param: "text.position"}` (repeat per channel), `stagger.set {id, by: "word"|"character"|"line"|"all", order: "forward"|"reverse"|"centre"|"edges"|"random", gap: <frames>, seed}`.
3. Key the connected channels ONCE as if for a single part, with `key.set` on the stored relative row and CSS curves: `src.e_src_text_relative_<id>.position` [0, -0.045] to [0, 0] and `.opacity` 0 to 1 over about 12 f; `src.e_src_text_fill_<id>.blur` 20 to 0 (the part blur, stored units, range 0 to 20). Every part replays this timeline `gap` frames later. The relative position is in stored units (frame fractions, y up: 0.045 of the height is about 49 px at 1080 high); the verified call writes them directly.

   ```json
   {"command": "stagger.new", "args": {"id": "#title"}}
   {"command": "stagger.connect", "args": {"id": "#title", "param": "text.position"}}
   {"command": "stagger.connect", "args": {"id": "#title", "param": "text.opacity"}}
   {"command": "stagger.connect", "args": {"id": "#title", "param": "fill.blur"}}
   {"command": "stagger.set", "args": {"id": "#title", "by": "word", "order": "forward", "gap": 4}}
   {"command": "key.set", "args": {"id": "#title", "key": "src.e_src_text_relative_clip_3.position", "value": [0, -0.045], "at": 0, "ease": "ease-out"}}
   {"command": "key.set", "args": {"id": "#title", "key": "src.e_src_text_relative_clip_3.position", "value": [0, 0], "at": 12}}
   {"command": "key.set", "args": {"id": "#title", "key": "src.e_src_text_fill_clip_3.blur", "value": 20, "at": 0, "ease": "ease-out"}}
   {"command": "key.set", "args": {"id": "#title", "key": "src.e_src_text_fill_clip_3.blur", "value": 0, "at": 12}}
   ```
4. `stagger.list {id}` reads back slots and keys.

Letters that should blur in use the `fill.blur` slot (the old route of connecting `blur.size` also exists when a blur effect was added first).

## Timing rules
| target | gap | total extra time |
|---|---|---|
| chars | 1 to 2 f (gap 1 for more than 8 letters) | gap x (letters - 1) |
| words | 3 to 5 f (or the mean spoken interval when synced to a voice-over) | gap x (words - 1) |
| lines | 5 to 8 f | gap x (lines - 1) |

`each: "3f"` or `"100ms"` is the gap. The last part finishes `gap x (parts - 1)` frames after the first: make sure it settles before the hold and before the clip end.

## Exits
- A stagger tween needs a visible resting state: `to: {opacity: 0}` is refused (`bad-stagger`, "it rests at 0, so nothing would show"). Exit by movement instead (verified: stagger-exit-by-movement): `to: {y: "+=60px"}` with `stagger` and a `delay`, then gate the whole text out with plain opacity keys written after it: `anim.set {id, keyframes: [{at: "1.8s", opacity: 1}, {at: "1.9s", opacity: 0}]}`.
- The manual card replays the WHOLE key timeline per part, so exit keys you add to the same connected channel stagger out for free (carried over from the 0.0.72 builds, not re-run here).
- A staggered PRESET exit on a channel already used by a staggered preset entrance is refused ("already in a slot"): use a whole-block exit preset, or build the exit keys manually on the same slot.

## Pitfalls
- After connecting, fill opacity may appear in `param.list` only as a slot proxy: use `stagger.list` keys.
- RTL text: see [../workflows/rtl-and-arabic.md](../workflows/rtl-and-arabic.md) (the Resolve transfer mirrors the delay table).
- Random order needs a `seed` for repeatable results: the design `stagger` has none, so use the manual card (`stagger.set {seed}`) when a random order must repeat.
- `anim.get` reads a staggered text's keys back in design values, with a `staggered` list naming the keyed properties (verified: stagger-restated-and-read-back); `stagger.list` has the card and its slots.
