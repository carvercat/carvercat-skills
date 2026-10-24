# Sound design for Carvercat promos

Agent-neutral. Tools: `../scripts/motion/` (`sfx_kit.py`, `sfx_render.py`,
`music_bed.py`, `mix_check.py`, `vo_align.py`). Everything is synthesized offline with
numpy/scipy, so there are no licence questions; swap in licensed music or library SFX if
the client prefers.

## What "punchy" means (measured)
Reference: Carvercat's built-in SFX pack `library/sfx/carvercat-starter` (in the installed app)
(5 CC0 sounds). Each one has an attack under 2 ms, a decay of 40-180 ms, a length of
0.12-0.55 s, and sits in one tight frequency band (peak -7 dBFS, RMS -21 dBFS).
Sounds that failed review had whooshes that took ~450 ms to reach the hit, tails of
1.4-5 s, and peaks of only -10 to -17 dBFS - they felt soft and late.

## One clip per event
Every element that appears gets its own sound, as its own clip on its own audio track
(house rule). Build a cue sheet first:
1. Entrances: `carverproj.entrances(timeline, scene_start)` lists every opacity/scale
   0->1 moment.
2. Add the actions that keyframe opacity doesn't reveal: pointer clicks, drags, scrubs,
   transitions, draw-ons, typing, sends, counters.
3. Pick a sound and a level per cue (table below), render with `sfx_render.py`, place
   each file at its `start_frame` (`placement.json`).

| Event | Generator | Peak dBFS (before -8 dB bake) | Notes |
|---|---|---|---|
| Logo piece / chip / card / icon appears | `pop(p)` | -6 to -9 | step pitch x1.12 per repeated item |
| Small reveal, panel build, list tick | `tick(p)` | -14 to -16 | quiet; many in a row |
| Pointer click, button press | `click(p)` | -7 to -9 | add a tiny pop for toggles |
| Text line reveal | `swish(0.2, 1800, 9000)` | -20 to -23 | airy; never fights the VO |
| Keyword / accent phrase | `accent(f)` | -8 to -9 | chime + light impact |
| Scene transition | `whoosh_hit(lead, tail)` | -3 | set `lead_s` so the hit lands ON the cut |
| Big hit, burst | `impact()` | -3 | one or two per film |
| Stretch / slide / panel rise | `stretch(d)` | -11 to -13 | |
| Collapse into a point | `suck(d)` | -8 | lead into the dot pop |
| Scrub / drag | `scrub(n, gap)` | -10 | |
| Typing in a prompt | `typing(n, gap)` | -14 | |
| Line/curve draw-on | `draw(d)` | -14 | |
| Outro | `sting()` | -5 | |

### The pop (approved)
A pop is an **upward** pitch glide: ~390 -> 860 Hz in ~20 ms, a 3-4 ms soft onset, a
~25 ms decay, a faint resonant ring and **no sub**. A falling pitch plus a sub reads as
a thud, and was rejected.

## Levels (approved mix)
| Stem | Target |
|---|---|
| VO | ~ -16 LUFS |
| Music | ~ -23 LUFS (6-7 dB under the VO), ducked a further ~6 dB under speech |
| SFX bus (all clips together) | ~ -24 to -25 LUFS - at -18 the user said "too loud" |
| Full mix | normalised to -14 LUFS, peaks <= -1 dBFS |

**Set levels per clip with `media.audio.gain`** ("Level (dB)", -60..+24, 0 = unity,
keyframeable; Carvercat 0.0.71+): `property.set {id, key:"media.audio.gain", value:-6}`
or `key.set` for fades and ducking. It is used in playback AND in every export mixdown.
On older builds (<= 0.0.70) there is no clip gain - bake gains into the WAVs instead.
Check the result against the reference mix from `mix_check.py`.

## Music
`music_bed.py` makes one beat-driven track: 120 BPM, four-on-the-floor kick, claps on
2 and 4, offbeat bass, a 3-3-2 pluck hook on vi-IV-I-V, sidechain pump, risers into the
drop and the CTA, a half-time outro and a final chord stab. **Place the first downbeat so
the main cut lands on a bar** (`(drop - downbeat) % (4 x 1800/BPM) == 0`).

## Voiceover word timing
`vo_align.py VO.wav script.txt --offset-frames <VO start>` -> every word's frame
(+-1-2 f). Put one phrase per line; add pronunciations for brand words or split them
("carver cat"). Key kinetic text 0-4 f before each spoken word.

## Placing audio in the project
- `media.import {paths:[...], frame}` imports many files, each on its own new audio
  track, at `frame` (0.0.71+; older builds placed them at the live playhead). To place
  each file at its own cue frame, import them one per call with that cue's `frame`, or
  import together and set positions in the project JSON: audio clips live in
  `scene.audioTracks[].clips[]`, `left` is in pixels = frame x `scene.ppf` (4 at 30 fps),
  `duration` is in frames.
- Copy, paste and duplicate keep sounds on audio tracks (0.0.71+).
- The clip label shown is the file name (`text`), so name files descriptively
  (`Brand_SFX_07_chip_free.wav`).
- Copy the audio into the project's repo folder and point the media paths there, so the
  project travels with its sound.
