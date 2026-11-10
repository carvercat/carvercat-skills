# Grain

`grain` adds film grain to an object's picture, strongest in the mid-tones. Put it on an **adjustment layer** and it grains everything below it (a whole title, a whole shot). It is a design key (Carvercat 0.1.10 and later): `"amount [size] [softness=] [colour=] [held] [seed=]"`, or an object. It is also a function of `filter`.

```json
{"command": "property.set", "args": {"id": "#film", "key": "grain", "value": "0.25 1.5px"}}
{"command": "property.set", "args": {"id": "#film", "key": "grain", "value": "0.4 3px softness=0.5 colour=0 held seed=7"}}
{"command": "property.set", "args": {"id": "#film", "key": "grain", "value": {"amount": 0.3, "size": "2px", "animated": false}}}
{"command": "property.set", "args": {"id": "#title", "key": "filter", "value": "blur(4px) grain(0.3 2px)"}}
{"command": "property.set", "args": {"id": "#film", "key": "grain", "value": "none"}}
```

Verified: grain-design-units.

| Part | Form | Range | Default | Meaning |
|---|---|---|---|---|
| amount | first number, or `amount` / `strength` | 0 to 1 | 0.25 | strength. At mid grey the standard deviation is 0.2 x amount (0.05 at the default, about 0.2 at 1) |
| size | `1.5px`, or `size` | 0.5 to 8 px of a 1920 frame | 1.5 px | the grain cell. It scales with the frame and with the object, like a blur |
| softness | `softness=0.3` | 0 to 1 | 0.3 | blends neighbouring cells; the strength is kept the same |
| colour | `colour=0.25` (`color=` too) | 0 to 1 | 0.25 | 0 is mono (the same grain on red, green and blue); 1 is independent channels |
| animated | the word `held`, or `animated: false` | on / off | on | on draws new grain every frame; `held` keeps one pattern |
| seed | `seed=7` | 0 to 9999, whole | 1 | picks the pattern. The same seed and frame draw the same pixels, so a render repeats |

A bare number after the amount is refused (`"0.3 1.5"`: write `1.5px`). `property.get` reads the whole form back with every part written out (`"0.3 2px softness=0.3 colour=0.25 seed=1"`).

## Keying

`anim.set`, `key.set` and a scene node's `keyframes` key `grain` by name; the value is the same string, and amount, size, softness and colour move between keys. The seed and `held` are not keyed. A key at amount 0 draws nothing, so grain can fade in and out:

```json
{"command": "anim.set", "args": {"id": "#film", "keyframes": [
  {"at": 0, "grain": "0 2px", "ease": "ease-out"}, {"at": 24, "grain": "0.25 2px"}]}}
```

## Refusals

Each refusal says why, what is valid and a corrected call (verified: grain-design-units):

- `out-of-range`: amount or softness or colour outside 0 to 1; size outside 0.5 to 8 px (scaled by W/1920); seed outside 0 to 9999.
- `bad-value`: an unknown key (`bogus=1`), a bare number with no `px`, or `animated` that is not true or false.
- A `filter` list takes `grain(...)` as one function, so `filter` replaces the grain along with blur, glow and the rest of its kinds.

## Where it carves

| Host | Carve | What is sent |
|---|---|---|
| Resolve | **approximate** | a Fusion Film Grain: strength, size and roughness, colour strength, Time Lock and Random Seed |
| After Effects | **approximate** | an Add Grain: intensity, size, softness, saturation, animation speed |

Grain is random, so a match is the same strength, size and character, not the same pixels. Measured by the app on both hosts against its canvas (standard deviation within about 10 %, spatial correlation and red/green correlation close). Run `carve.preflight` and accept the `approximate` line.

## Recipes

- **Film look over a whole shot:** an adjustment layer on top, `grain` `"0.08 1.5px softness=0.4 colour=0.1"`. Quiet, cinematic. Amount above 0.3 reads as damaged film or video noise, not craft.
- **Old print or leader:** `"0.2 2.2px softness=0.4 colour=0.1"` on a warm grey ground (the Retro pack's `rt_film_leader`, [rt-film-leader](../../patterns/rt-film-leader.md)).
- **VHS or tape:** coarse and coloured, `"0.14 2.5px softness=0.4 colour=0.5"` on a finishing adjustment layer (the Retro night promo recipe).
- **Digital noise:** `"0.1 2.5px softness=0.2 colour=0.6"` (the Glitch music teaser recipe).
- **Cinematic quiet:** `"0.06 1.5px softness=0.4 colour=0.1"` (the Luxury product teaser recipe).
- **Stills and held frames:** add `held` so a freeze frame does not shimmer.
- **Grain in on a reveal:** key amount 0 to the resting value over 12 to 24 f.

## Pitfalls

- An adjustment layer covers the whole comp for its length (its `start` and `duration`); put titles above it if they must stay clean.
- An adjustment layer inside a placed template reaches only that template's own objects, not your footage ([KI-158](../known-issues.md#ki-158)); put the finishing grain on the master comp, above everything. `inspect lint` reports every adjustment layer as one `never_visible` warning (the layer draws nothing itself); `carvercat_look` shows the grain.
- Text on a dark ground loses legibility at amount 0.3 and over; check with a `carvercat_look` at full size, and keep contrast with `measure.contrast`.
- Grain is fine detail: judge it at 100 % on an uncropped look, not a thumbnail.
- Bypass with `effect.enable {entry, on: false}`; an off or zero-amount grain costs nothing on the canvas.
