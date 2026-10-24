# Review checklist - before showing a Carvercat video to anyone

Run it with `carvercat_look` on entrance, hold and exit frames of every scene, then
once straight through. Agent-neutral.

## Native checks first
- [ ] `carvercat_authoring {mode:"validate"}`: `bounds_inside` the safe box for every text
      and logo, `no_overlap` for text vs UI, `font_exact` for every font - all pass.

## Story and staging
- [ ] Hook/product visible in the first 30-90 f; frame 0 reads as a finished image.
- [ ] One focal point per beat; at most 1-2 primary motions overlap.
- [ ] Reveal order = importance, then reading order; the CTA lands last and holds >= 2 s.
- [ ] Every scene has IN, a living MID and OUT - nothing sits static.

## Timing and easing
- [ ] Durations come from the project scale; identical elements share timing.
- [ ] Entrances Ease out (or customEase), exits Ease in and 20-30 % shorter, on-screen moves S-curve; Linear only for loops; Hold for steps.
- [ ] Staggers: 1-2 f/letter, 2-4 f/word, 3-6 f/line; total spread <= ~20 f; nothing overruns the comp end.
- [ ] Overshoot only on hero/brand moments, 5-15 %, settled within 12 f.

## Text
- [ ] Every line holds >= max(25 f, words x 10 f) + 10 f after it lands, and is still while read.
- [ ] Sizes per [typography.md](typography.md); one accent per scene; <= 2 lines, <= 42 chars/line.
- [ ] No text touches UI or another element; long lines broken onto two lines.
- [ ] Synced text appears on or just before the spoken word.

## UI mock-ups
- [ ] Every moving element (playheads, scrubbed objects, selection handles, pointer) stays inside its panel at every keyframe.
- [ ] Pointer clicks land on the thing they click; ripples centred on the hotspot.

## Transitions
- [ ] Each one is motivated; <= 2-3 types; hit on the beat; screen direction kept.
- [ ] Fast shapes have motion blur; no full-frame glow flashes; <= 3 flashes/s.
- [ ] Hand-off points line up across cuts.

## Look and finish
- [ ] No haze: glow `blend` is 0 outside pulses; no blur left at 10 by default.
- [ ] Logos are crisp (built at size, not upscaled) and pop in place.
- [ ] 9:16 versions respect [vertical-and-safe-areas.md](vertical-and-safe-areas.md).

## Sound
- [ ] Every element/action has its own SFX clip; transition hits land on the cut.
- [ ] Levels: VO ~-16, music ~-23, SFX bus ~-25 LUFS, mix -14 LUFS (`mix_check.py`); per-clip `media.audio.gain` used, not baked files (0.0.71+).
- [ ] Watch once with sound off - the story still reads.

## Project hygiene
- [ ] `carverproj.duplicate_ids()` is empty (or only between comps with no audio).
- [ ] Media paths point inside the project folder; nothing references Downloads.
- [ ] Saved; app readout ~15-25 ms work per frame.

## Expected lint noise
Presets from the Motion Patterns pack create `repeated_key_value` notes (holds between baked keys) — expected. Full-frame backgrounds, wipe bars and iris discs report crops/off-frame — expected. Read warnings, not notes.
