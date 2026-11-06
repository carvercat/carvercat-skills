---
id: workflow/animatics
title: Animatics
section: workflow
tags: [animatic, timing, scratch voice-over, blocking, edit, pre-visualisation, hold keys]
styles: [all]
topics: [workflow, timing]
related: [workflow/storyboards, workflow/review, principles/straight-ahead-and-pose-to-pose, sound-and-timing/beat-sync, sound-and-timing/reading-time]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://schoolofmotion.com/blog/what-are-animatics-and-why-are-they-important, https://assets.boords.com/animatic/how-to-make-an-animatic, https://milanote.com/guide/motion-graphics-pre-production]
---

# Animatics

An animatic is the storyboard on a timeline: each panel held for its real duration, with scratch
voice-over and music, sometimes with rough moves. It answers the question nothing else can before
animation: **does the film work in time?**

## The idea

- Time each panel to the voice-over, the music and the on-screen text's read time.
- Scratch voice-over (your own voice is fine) reveals scenes that run long or short.
- The approved animatic becomes the **edit reference**: scene lengths are locked, animation fills them.
- In motion graphics the animatic can be "blocked" animation: key poses only, jumping from pose to pose.

## Rules of thumb

- Every text panel holds at least its read time ([reading time](../sound-and-timing/reading-time.md)).
- Leave 6–12 f of handle at both ends of each scene for transitions.
- Land big changes on musical phrase starts; check every 8 bars against the audio ([beat sync](../sound-and-timing/beat-sync.md)).
- Review the animatic at full speed with sound, then muted.

## Measured in Carvercat

- **Blocking with `hold` keys** works as a stepped animatic inside the final comp: a key with `hold` ease
  keeps the previous value and jumps exactly on its own frame, so poses hold their full duration and
  change on the planned frame. Changing the easing later turns the same keys into the final motion
  ([pose to pose](../principles/straight-ahead-and-pose-to-pose.md), comp `W Blocking`).
- **Shots placed on beat frames** hold exactly their frame ranges (`inspect timing` showed each 15 f shot
  entering on its beat; comp `T Beat cuts`, [rhythm editing](../techniques/rhythm-editing.md)).
- **Read times** for every text panel are checked by lint at any frame rate
  ([reading time](../sound-and-timing/reading-time.md)).

## Do and don't

- Do lock scene lengths at the animatic stage and protect them.
- Do include on-screen text in the animatic at its final wording.
- Don't polish anything before the animatic is approved.
- Don't skip the muted review; most social viewers will watch muted.

## Checklist

- [ ] Every scene timed to voice-over, music and read time.
- [ ] Handles for transitions.
- [ ] Approved at full speed with and without sound.
- [ ] `inspect lint` reading-time clean on the animatic's text.

## In Carvercat

- Build the animatic as the real master comp: one nested comp (or one still group) per scene, butted on one
  track; poses keyed with `hold`.
- Scratch audio: an audio media clip on an audio track; level `media.audio` `Level (dB)`.
- Export a review file quickly: H.264 MP4 ([delivery](delivery.md)); a GIF at 50% and 15 fps for chat.
- Timing at a glance: `carvercat_inspect {mode:"timing"}` lists every object's enter, move, settle and exit.
