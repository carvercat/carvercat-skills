---
id: sound-and-timing/music-edits
title: Editing music to picture
section: sound-and-timing
tags: [music, edit, cut, loop, fade, ending, button, length, bed]
styles: [all]
topics: [audio, music, editing]
related: [sound-and-timing/beat-sync, sound-and-timing/audio-in-carvercat, techniques/rhythm-editing, sound-and-timing/voice-over-pacing]
verified: no (theory only)
source_inspiration: [https://www.premiumbeat.com/blog/cut-to-the-beat-tip-for-editing-to-music-in-final-cut-pro-x/, https://support.apple.com/guide/final-cut-pro/ver65b55a2b7/mac, https://www.silvermansound.com/bpm-to-fps-calculator]
---

# Editing music to picture

Library music rarely has the right length. Editing it, removing or repeating bars so it ends exactly with
the film, is a core motion-design skill, and so is choosing whether picture follows music or music follows
picture.

## The idea

- **Cut on bar lines**: remove or repeat whole bars (or phrases) so the rhythm never stumbles.
- **Real ending, not a fade**: end on the track's own ending ("button"), placed so it lands on the logo or
  call to action. Fades are a last resort.
- **Picture to music or music to picture**: hype pieces cut picture to the music's structure; narrative
  pieces fit music under voice-over and edit music around key lines.
- **Beds**: under voice-over, music sits lower and simpler; swell in the gaps.

## Rules of thumb

- Bar length = 4 × frames per beat (120 BPM: 60 f at 30 fps). Edit points on downbeats.
- Back-time the ending: place the music's ending so its last hit lands on the final picture event, then edit
  the beginning or the middle to fit.
- Crossfade music edits over 2–8 f on a downbeat to hide the join.
- Fade-outs, when needed, 1–3 s and shaped (not a straight decibel ramp, see [audio in Carvercat](audio-in-carvercat.md)).
- Duck music 8–12 dB under voice; let it return in pauses.

## Do and don't

- Do lock the music edit before final animation timing where the piece is music-led.
- Do check the edit on headphones and laptop speakers.
- Don't cut in the middle of a sung phrase or a melodic line.
- Don't fade the music out under the logo if the track has an ending you can use.

## Checklist

- [ ] Music edits on downbeats, crossfaded.
- [ ] The ending lands on the last picture event.
- [ ] Music ducked under voice; no level jumps at edits.

## In Carvercat

No new measurements on this page. Levels, fades and sync are measured on [audio in Carvercat](audio-in-carvercat.md).

- Edit music by splitting the music into several audio clips on one track at bar boundaries (frames from the
  tempo, [beat sync](beat-sync.md)) and keying `media.audio` `Level (dB)` for crossfades and ducking.
- A bed that fits the cut: `ai/scripts/motion/music_bed.py`; loudness of stems: `mix_check.py`.
