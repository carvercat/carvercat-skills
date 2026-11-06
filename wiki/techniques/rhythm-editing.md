---
id: techniques/rhythm-editing
title: Rhythm editing (cutting to music)
section: techniques
tags: [editing, cuts, beat, music, pacing, montage, shot length, downbeat]
styles: [social-short-form, sports, kinetic-typography, funky]
topics: [editing, rhythm]
related: [sound-and-timing/beat-sync, principles/rhythm, techniques/match-cuts, accessibility/photosensitivity, sound-and-timing/frame-rates]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.premiumbeat.com/blog/cut-to-the-beat-tip-for-editing-to-music-in-final-cut-pro-x/, https://support.apple.com/guide/final-cut-pro/ver65b55a2b7/mac, https://www.vegascreativesoftware.com/in/post-production/how-to-edit-video-footage-to-the-beats-of-music, https://www.silvermansound.com/bpm-to-fps-calculator]
---

# Rhythm editing (cutting to music)

When scene changes, hits and reveals line up with the music, a film feels effortless. Rhythm editing is
choosing where the cuts go: on beats, on bars, on phrase changes, and occasionally against the beat for
surprise.

## The idea

- **Beat**: the pulse. **Bar**: usually 4 beats. **Phrase**: usually 4 or 8 bars, where the music changes.
- Cut on beats for energy, on bars for calm, on phrase starts for big changes (new section, logo).
- Do not cut on every beat for long; vary shot length and speed up the cutting into a build, then release.
- Visual events land on the beat; the anticipation sits just before it ([anticipation](../principles/anticipation.md)).
- Editing snaps to whole frames; a beat that falls between frames goes to the nearest frame.

## Rules of thumb (30 fps)

| Tempo | Frames per beat | Frames per bar (4/4) | Shot length options |
|---|---|---|---|
| 90 BPM | 20 | 80 | 40, 80 f |
| 100 BPM | 18 | 72 | 36, 72 f |
| 120 BPM | 15 | 60 | 30, 60, 120 f |
| 128 BPM | 14.06 | 56.25 | round each beat separately |
| 140 BPM | 12.86 | 51.4 | round each beat separately |

- Frames per beat = 1800 / BPM at 30 fps (fps × 60 / BPM in general).
- For non-integer beats, compute each beat's frame from the start (round(n × 1800 / BPM)); adding a rounded
  step repeatedly drifts off the music.
- Hype: 1–2.5 s shots; explainer beats 3–5 s; a held breather every 8–12 s.
- More than 3 full-frame colour changes a second is a photosensitivity risk ([photosensitivity](../accessibility/photosensitivity.md)).

## Measured in Carvercat

Five full-frame colour shots of 15 f each, cut on every beat at 120 BPM (frames 0, 15, 30, 45, 60).
`carvercat_inspect mode:timing` showed each shot entering exactly on its beat frame and leaving on the
frame before the next. `carvercat_inspect mode:qc` raised **no flash finding** for these two cuts a second
between dark and bright colours; it flagged only the first shot's near-black navy (#101418) as a `black`
stretch. Its loop-seam check correctly reported the sequence does not loop (luma difference 0.33).

## Do and don't

- Do mark beats from the actual track (waveform peaks), then compute the rest from the tempo.
- Do place cuts on frames, landings on beats, anticipation before.
- Don't cut every beat for a whole minute; vary.
- Don't fight a vocal: avoid hard cuts in the middle of a sung word.

## Checklist

- [ ] Beat frames computed from the start of the track, not accumulated.
- [ ] Big changes on phrase starts; cuts on beats or bars.
- [ ] Cut frequency rises into builds and drops in breathers.
- [ ] `qc` shows no flash findings.

## In Carvercat

- Shots: clips on one track butted end to end; in a project file `left` = frame × 4 and `duration` in frames
  ([JSON authoring](../../ai/references/app/json-authoring.md)). Nested comps as shots: one instance per
  shot on the master comp.
- Audio: a media clip with `media.audio` `Level (dB)` (−60 to 24); music beds and SFX guidance:
  [sound design](../../ai/references/craft/sound-design.md); tools `ai/scripts/motion/music_bed.py`,
  `mix_check.py`.
- Beat-locked text: `Beat words` ([kt-beat-words](../../ai/patterns/kt-beat-words.md)); GOAL slam and impacts:
  [Sports](../../ai/patterns/sports.md).
- Transitions on beats: [transitions craft](../../ai/references/craft/transitions.md) and the
  [Transitions pack](../../ai/patterns/transitions.md) (covers cut 15–20 f in).
- Lab: comp `T Beat cuts` in [the techniques lab](../labs/README.md).
