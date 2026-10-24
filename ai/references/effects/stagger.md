# Stagger Text (per-word, per-letter, per-line)

**Verified 0.0.72:** the 7 staggered presets of the Motion Patterns pack (word rise, letter cascade, word pop, line reveal, letter shimmer, word swing, word exit) on Open Sans; manual builds documented below come from earlier verified jobs (0.0.69+).

## Fast path
`preset.apply {name:"Words rise - expo", id}` — the preset creates the card, connects its lanes and sets by/order/gap. See [../../patterns/README.md](../../patterns/README.md).

## Manual build (any combination)
1. (Optional) `effect.add {id, cap:"blur"}` first if letters should blur in — `blur.size` only becomes connectable once the blur exists.
2. `stagger.new {id}` → `stagger.connectable {id}` (lists what a slot can take: `text.position`, `text.scale`, `text.rotation`, `text.anchor`, `text.opacity`, `fill.opacity`, `fill.blur`, `stroke.*`, `blur.size`, and transform.* which MOVES the object's keys onto the relative row).
3. `stagger.connect {id, param:"text.position"}` (repeat per channel), `stagger.set {id, by:"word"|"character"|"line"|"all", order:"forward"|"reverse"|"centre"|"edges"|"random", gap:<frames>, seed}`.
4. Key the connected channels ONCE as if for a single part — e.g. `src.e_src_text_relative_<id>.position` [0,−0.045] → [0,0] and `.opacity` 0 → 1 over ~12 f; `fx.e_fx_blur_<id>.size` 22 → 0. Every part replays this timeline `gap` frames later.
5. `stagger.list {id}` to read back slots and keys.

## Timing rules
| by | gap | total extra time |
|---|---|---|
| character | 1–2 f (gap 1 for > 8 letters) | gap × (letters − 1) |
| word | 3–5 f (or the mean spoken interval when synced to VO) | gap × (words − 1) |
| line | 5–8 f | gap × (lines − 1) |
The last part finishes `gap × (parts−1)` frames after the first: make sure it settles before the hold and before the clip end.

## Exits
- The stagger replays the WHOLE key timeline per part — so exit keys you add to the same connected channel stagger out for free (manual builds).
- A staggered PRESET exit on a channel already used by a staggered preset entrance is refused ("already in a slot") — use a whole-block exit preset, or build the exit keys manually on the same slot.
- Gate overruns with the clip's own `transform.placement.opacity` at the end.

## Pitfalls
- After connecting, fill opacity may appear in `param.list` only as a slot proxy: use `stagger.list` keys.
- RTL text: see ../workflows/rtl-and-arabic.md (Resolve transfer mirrors the delay table).
- Random order needs a `seed` for repeatable results.
