---
id: cookbook/end-cleanly
title: End a video cleanly (fade to black)
section: cookbook
tags: [ending, fade to black, fade out, outro, music fade, last frame, end card]
styles: [all]
topics: [transitions, audio, delivery]
related: [workflow/delivery, sound-and-timing/music-edits, cookbook/duck-music-under-voice, cookbook/cross-dissolve]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://larryjordan.com/articles/automatically-duck-background-music-under-dialog-in-davinci-resolve/, https://tech.ebu.ch/publications/r128]
---

# End a video cleanly (fade to black)

**Goal.** The picture fades to true black and the music fades to silence together, landing on the last
frame.

## Steps

1. A full-frame **black rectangle** on the top track for the last second (30 f): opacity 0 → 1, `linear`,
   with the last key on the **last frame** (f89 of a 90 f comp).
2. Key the music's `media.audio.gain` from 0 dB to **−60 dB** over the same frames. −60 dB is silent in
   practice; a dB ramp sounds even.
3. Let the last title hold before the fade starts; don't fade text that has just arrived.
4. Run `inspect qc`: it reports the black end and long holds, which is fine for an ending.

## Measured in Carvercat 0.1.6

Comp `K End fade` in [cookbook lab 3](../labs/README.md#cookbook-lab-3carverproj), 90 f: a title on #31566A,
black fade f60 → f89, music bed gain 0 → −60 dB f60 → f89.

- `carvercat_render`: f75 background (28, 55, 69) (half way); **f89 is (0, 0, 0)** at the centre and corner.
- `inspect qc`: `black` at f89 ("98% of the picture under 4% luminance - intended fades are fine") and
  `freeze` f0–f60 (a 2 s hold). No flash findings.
- Exported WAV (3.0 s): bed −12.0 dBFS at 1.0 s, −15.0 at 2.0 s, −26.9 at 2.2 s, −45.5 at 2.5 s,
  **−73.2 at 2.9 s**.
- `inspect lint`: **0 errors, 0 warnings, 0 notes**.

## Traps

- A music clip that runs past the comp end is easy to miss; trim it to the fade:
  [KI-068](../../ai/references/known-issues.md#ki-068).
- Exported files nest and hidden files appear in the export folder: [KI-077](../../ai/references/known-issues.md#ki-077).

## In Carvercat

- Library: `Slow dip` ([ml-slow-dip](../../ai/patterns/ml-slow-dip.md)), `Dip to colour`
  ([tx-cover-transitions](../../ai/patterns/tx-cover-transitions.md)), preset `Soft fade out`, end cards
  `Brand end card`, `Follow end card`, `CTA end card`.
- Export: [delivery](../workflow/delivery.md), [export and delivery](../../ai/references/workflows/export-and-delivery.md).
