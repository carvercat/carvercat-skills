---
id: cookbook/duck-music-under-voice
title: Fade music under voice
section: cookbook
tags: [ducking, music, voice over, gain, mix, dialogue, level, fade]
styles: [all]
topics: [audio, mix]
related: [sound-and-timing/audio-in-carvercat, sound-and-timing/voice-over-pacing, sound-and-timing/music-edits, cookbook/hit-on-the-beat]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://larryjordan.com/articles/automatically-duck-background-music-under-dialog-in-davinci-resolve/, https://composer-docs.vindral.com/script-objects/script-objects-operators-sidechain-ducking.html]
---

# Fade music under voice

**Goal.** The music bed drops while someone speaks and comes back after, smoothly enough that nobody
notices the move.

## Steps

1. Key the music clip's gain, `media.audio.gain` (dB, on the audio clip), with four keys around each
   voice line:
   - full level 10 f **before** the voice starts;
   - the ducked level (−10 to −14 dB) on the frame the voice starts;
   - the ducked level on the frame the voice ends;
   - full level 15 f later (a slower release than the attack).
2. Keep the keys `linear`: the value is in dB, so a linear dB ramp already sounds even.
3. Export the audio and listen, then check the levels in the exported WAV.

## Measured in Carvercat 0.1.6

Comp `K Duck` in [cookbook lab 1](../labs/README.md#cookbook-lab-1carverproj): a two-tone bed (220 + 330 Hz)
with gain keys 0 dB at f30, −12 dB at f40, −12 dB at f100, 0 dB at f115; a 1 kHz "voice" clip f40–f100.
Exported as WAV (48 kHz, 24-bit, stereo, 5.0 s) and the bed's 220 Hz level measured in 0.1 s windows:

| Time | Bed level |
|---|---|
| 0.5 s (before) | 0.0 dB |
| 1.1 s (ramping down) | −5.2 dB |
| 1.4–3.0 s (under the voice) | **−12.2 dB** |
| 3.5 s (ramping up) | −6.7 dB |
| 3.9 s (after) | 0.0 dB |

- The ramp follows the keys linearly in dB: −5.2 dB measured in the 1.1–1.2 s window, −5.4 dB predicted at its
  centre.
- `inspect lint`: **0 errors, 0 warnings, 0 notes**.

## Traps

- Per-clip gain needs 0.0.71 or later; older notes say to bake gain into WAVs:
  [KI-065](../../ai/references/known-issues.md#ki-065).
- Resolve stored a different gain than requested on transfer; check levels after sending:
  [KI-066](../../ai/references/known-issues.md#ki-066).
- A music clip longer than the comp hides past the end: [KI-068](../../ai/references/known-issues.md#ki-068).

## In Carvercat

- Gain `media.audio.gain` keys on the audio clip; export `format: "audio"`.
- Mixing levels and loudness targets: [sound design](../../ai/references/craft/sound-design.md),
  `scripts/motion/mix_check.py`.
- Voice timing: [captions and voice-over](../../ai/references/workflows/captions-and-voiceover.md).
- Background: [audio in Carvercat](../sound-and-timing/audio-in-carvercat.md),
  [voice-over pacing](../sound-and-timing/voice-over-pacing.md), [music edits](../sound-and-timing/music-edits.md).
