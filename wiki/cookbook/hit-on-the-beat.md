---
id: cookbook/hit-on-the-beat
title: Sync a hit to a beat
section: cookbook
tags: [beat, bpm, music, sync, hit, cut on beat, rhythm, pulse]
styles: [kinetic-typography, social-short-form, sports, funky, glitch]
topics: [audio, timing, rhythm]
related: [sound-and-timing/beat-sync, techniques/rhythm-editing, sound-and-timing/sfx-spotting, sound-and-timing/audio-in-carvercat]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.silvermansound.com/bpm-to-fps-calculator, https://www.premiumbeat.com/blog/cut-to-the-beat-tip-for-editing-to-music-in-final-cut-pro-x/]
---

# Sync a hit to a beat

**Goal.** Visual hits (pops, cuts, flashes) that land exactly on the music's beats.

## Steps

1. Frames per beat = fps × 60 / BPM. At 30 fps: 120 BPM = **15 f**, 100 BPM = 18 f, 90 BPM = 20 f,
   128 BPM = 14.06 f (round per beat from the start, don't add 14 every time).
2. Place the music clip so its first beat is on a known frame (here f0). Read the first beat from the
   waveform or a click, not from the file start.
3. Start each hit **on** the beat frame at its peak value, then settle: scale 1.3 → 1.0 over 6 f, expo out.
   A hit that starts small and grows peaks after the beat and reads late.
4. Cuts on the beat: start the next clip on the beat frame.
5. Export the audio and check one or two beats against the frames before you build the rest.

## Measured in Carvercat 0.1.6

Comp `K Beat hit` in [cookbook lab 1](../labs/README.md#cookbook-lab-1carverproj): a generated 120 BPM
click track (1 kHz, 10 ms) at f0, eight squares starting at f0, 15, 30 … 105.

- Exported as WAV (48 kHz, 24-bit, stereo) and read back: click onsets at **0.0, 0.5, 1.0 … 3.5 s**, that
  is frames **0, 15, 30, 45, 60, 75, 90, 105** exactly.
- `inspect probe` on each square: scale **1.30 on the beat frame**, 1.094 one frame later, 1.029, 1.008,
  1.002, and 1.000 from five frames after the beat.
- `inspect lint`: **0 errors, 0 warnings, 0 notes**.

## Traps

- 24 fps source audio on a 30 fps timeline rounds clip ends by a frame:
  [KI-067](../../ai/references/known-issues.md#ki-067).
- A music clip longer than the comp hides past the end: [KI-068](../../ai/references/known-issues.md#ki-068).
- Native stagger has one uniform gap, so it cannot follow a syncopated rhythm:
  [KI-041](../../ai/references/known-issues.md#ki-041).

## In Carvercat

- Curve names on this page (expo out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Audio clip gain `media.audio.gain` (dB); export `format: "audio"`, `audioCodec: "wav"`.
- Library: `Beat words` ([kt-beat-words](../../ai/patterns/kt-beat-words.md)), `Countdown (9:16)`
  ([ss-countdown](../../ai/patterns/ss-countdown.md)).
- Click and hit sounds: `scripts/motion/sfx_kit.py` ([sound design](../../ai/references/craft/sound-design.md)).
- Background: [beat sync](../sound-and-timing/beat-sync.md), [rhythm editing](../techniques/rhythm-editing.md).
