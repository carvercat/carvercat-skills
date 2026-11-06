---
id: sound-and-timing/beat-sync
title: Beat sync
section: sound-and-timing
tags: [beat, bpm, music, sync, frames per beat, downbeat, sfx, hit, phrase]
styles: [social-short-form, kinetic-typography, sports, funky, glitch]
topics: [music, timing]
related: [techniques/rhythm-editing, principles/rhythm, principles/anticipation, sound-and-timing/frame-rates, techniques/kinetic-type]
verified: no (theory only)
source_inspiration: [https://www.silvermansound.com/bpm-to-fps-calculator, https://pypi.org/project/bpm2fps, https://peachpit.com/articles/article.aspx?p=22799, https://www.premiumbeat.com/blog/cut-to-the-beat-tip-for-editing-to-music-in-final-cut-pro-x/, https://tech.ebu.ch/publications/r128]
---

# Beat sync

Motion that lands on the music feels intentional. Beat sync is turning a tempo into frame numbers and
placing the landings of moves, the cuts and the sound effects on them.

## The idea

- **Land on the beat, not start on it**: the eye registers the moment a move arrives (or hits), so the end
  of the ease goes on the beat. Anticipation and travel happen before.
- **Hierarchy of the grid**: beats for small hits (words, icons), bar starts for scene changes, phrase starts
  (every 4 or 8 bars) for big reveals and the logo.
- **Sound effects follow the picture**: one SFX per visual event, on the impact frame, not before.
- **Leave some beats empty**: a grid filled on every beat becomes a metronome.

## Rules of thumb

- Frames per beat = fps × 60 ÷ BPM.

| BPM | 24 fps | 25 fps | 30 fps | 60 fps |
|---|---|---|---|---|
| 90 | 16 | 16.67 | 20 | 40 |
| 100 | 14.4 | 15 | 18 | 36 |
| 120 | 12 | 12.5 | 15 | 30 |
| 128 | 11.25 | 11.72 | 14.06 | 28.13 |
| 140 | 10.29 | 10.71 | 12.86 | 25.71 |

- Non-integer beats: compute beat n as round(n × fps × 60 ÷ BPM) from the start; never add a rounded step
  repeatedly (at 128 BPM and 30 fps a beat is 14.0625 f: adding 14 f each time loses a frame every 16 beats, about every 7.5 s).
- Find the first downbeat from the waveform, then trust the maths; check every 8 bars against the audio.
- Hits: the visual impact 0–2 f before the transient reads as in sync; later than the sound reads as late.
- Lyrics and voice: text appears on the spoken word or up to 4 f before it.

## Do and don't

- Do place the landing frame of each move on the beat and work backwards for its start.
- Do put big changes on phrase starts.
- Don't animate every beat; vary density with the music's energy.
- Don't let SFX pile up: one clip per event, levels per [sound design](../../ai/references/craft/sound-design.md).

## Checklist

- [ ] First downbeat located from the audio; beat frames computed from it.
- [ ] Landings (not starts) on beats; big reveals on phrase starts.
- [ ] Spot-check sync every 8 bars.
- [ ] One SFX per visual event, on the impact frame.

## In Carvercat

This page states arithmetic and craft guidance; no Carvercat behaviour on it was measured. Related
measured pages: [rhythm editing](../techniques/rhythm-editing.md) (shots cut on beat frames) and
[frame rates](frame-rates.md).

- Audio clips: media clips on audio tracks; level is `media.audio` `Level (dB)`; in a project file the audio
  clip needs a matching entry in the project media pool ([JSON authoring](../../ai/references/app/json-authoring.md)).
- Tools: `ai/scripts/motion/music_bed.py` (a bed that fits the cut), `sfx_kit.py` / `sfx_render.py`
  (synthesised pops, whooshes, ticks, impacts), `mix_check.py` (stem loudness), `vo_align.py` (word frames).
- Beat-locked templates: `Beat words` (25 f beat, [kt-beat-words](../../ai/patterns/kt-beat-words.md)),
  `Impact slam` and `GOAL slam` ([Sports](../../ai/patterns/sports.md)).
- Music and SFX targets, levels and the pop/whoosh specs: [sound design](../../ai/references/craft/sound-design.md).
