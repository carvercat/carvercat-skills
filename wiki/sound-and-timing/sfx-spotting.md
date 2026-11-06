---
id: sound-and-timing/sfx-spotting
title: Spotting sound effects to motion
section: sound-and-timing
tags: [sfx, sound effects, whoosh, pop, impact, click, spotting, sync, sound design]
styles: [all]
topics: [audio, timing]
related: [sound-and-timing/audio-in-carvercat, sound-and-timing/beat-sync, principles/anticipation, principles/secondary-action]
verified: no (theory only)
source_inspiration: [https://www.premiumbeat.com/blog/cut-to-the-beat-tip-for-editing-to-music-in-final-cut-pro-x/, https://www.vegascreativesoftware.com/in/post-production/how-to-edit-video-footage-to-the-beats-of-music]
---

# Spotting sound effects to motion

"Spotting" is deciding which visual events get a sound and exactly where the sound starts. Good SFX make
motion feel physical (a pop has a pop, a whoosh has air) and guide attention; too many make a film tiring.

## The idea

- **One sound per meaningful event**: arrivals of hero elements, impacts, clicks, transitions. Not every small
  move.
- **Sync points differ by sound type**:
  - impacts, pops, clicks: the transient sits **on** the frame of contact or landing;
  - whooshes: the sound **leads** the move and peaks at the fastest frame, so it starts a few frames before;
  - risers: build over the anticipation and resolve on the hit.
- **Sound follows weight**: heavy objects get low, longer sounds; light ones short, high sounds
  ([weight](../principles/weight.md)).
- **Silence is a sound**: drop SFX for a beat before the big hit.

## Rules of thumb

- Hit sounds: transient on the impact frame (0 to −1 f).
- Whoosh: start 4–10 f before the fastest frame of the move; peak at the fastest frame; tail through the settle.
- UI clicks and pops: 2–4 f long, on the frame the element appears or the button is pressed.
- Density: about one SFX per second of busy animation at most; fewer in calm styles.
- Level SFX below voice and around or below music peaks; vary pitch slightly on repeats.

## Do and don't

- Do mark impact and fastest frames with `inspect timing` and curves, then place sounds on them.
- Do layer a small sound with a big visual only when the visual is the hero.
- Don't put a whoosh on every move; it becomes noise.
- Don't let SFX mask the voice-over.

## Checklist

- [ ] Every hero event has one sound, on the right frame for its type.
- [ ] Whooshes lead their moves; impacts land on contact.
- [ ] One beat of silence before the biggest hit.

## In Carvercat

No new measurements on this page; sync to the frame is measured on [audio in Carvercat](audio-in-carvercat.md).

- Find frames: `carvercat_inspect {mode:"timing"}` (moves, settles) and `{mode:"curves"}` (peak speed frame).
- Synthesised pops, whooshes, ticks, impacts: `ai/scripts/motion/sfx_kit.py`, `sfx_render.py`; per-event
  rules and levels: [sound design](../../ai/references/craft/sound-design.md).
