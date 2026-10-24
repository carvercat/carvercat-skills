# Assembling a multi-beat promo in ONE comp

**Verified 0.0.72** by a cold-start field test: an agent with only this skill built a 15 s, 4-beat promo in about 80 tool calls (comp `FIELD TEST promo` in `lab/field-test.carverproj`).

## 1. Skeleton first (before any content)
1. `comp.new` → `comp.format {width:1920,height:1080,fps:30}` → `comp.duration {frames:450}`.
2. Add the tracks you will need up front (`track.add` ×N) so `object.new` never has to look for "a track with room". Layering, bottom to top:

| Track | Holds |
|---|---|
| V1 | full-length background (`object.new {kind:"background"}` with the step's `frame: 0`, duration = comp) |
| V2 | ambient layer: a big soft shape (soft edge or blur, opacity 0.05–0.1) drifting the whole length — gives every hold life |
| V3–V8 | beat content (one beat may reuse tracks of an earlier beat once that beat's clips have ended) |
| above content | transitions (wipe bars, iris discs) |
| top | end card (so no transition covers it) |

Track indexes count audio tracks too; re-read `carvercat_list` after `track.add`.

## 2. Frame map (write it before building)

| Beat | Frames | Content ends | Transition (on top) | Cut frame |
|---|---|---|---|---|
| 1 Hook | 6–90 | 90 | two-tone wipe 76–104 | 90 (under full cover) |
| 2 Features | 96–210 | 210 | zoom-through: exits 198–210, next settles from 206 | 206–210 overlap |
| 3 Chart | 210–330 | 330 | iris 300–345 | 330 (under cover) |
| 4 End card | 336–450 | 450 | fade to black 432–449 | — |

Rules: content clips END at the cut; the next beat's clips START at (or 3–4 f before) the cut; presets are anchored to clip ends, so trimming a clip moves its entrance/exit with it.

## 3. Per beat
- Build objects (style fully: always set `text.fill.color`; place with `authoring.place_bounds` BEFORE animating).
- Group things that move together (card + label) and animate the group.
- Entrances from the pack (one `preset.apply` per object), 3–6 f apart, hero last.
- Hold motion: 2–4 % scale or a 1–2 % drift over the hold (two `key.set` keys, S-curve) on the hero or the group.
- Exits: `Exit … - accelerate` / `Exit fade - fast` / `Exit zoom through`, ~70 % of the entrance length, ending at the cut.

## 4. Check
`carvercat_look` entrance / hold / exit of every beat (`count` 4–6, `max_edge` ≤ 1000), `inspect lint` (notes from presets are expected), `authoring validate` for safe area and overlaps (ignore false failures on nested instances), then `edit.save {path}` (save-as).
