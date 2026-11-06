---
id: workflow/storyboards
title: Storyboards and style frames
section: workflow
tags: [storyboard, style frame, moodboard, frames, look development, design approval]
styles: [all]
topics: [workflow, planning, design]
related: [workflow/briefs, workflow/animatics, workflow/review, principles/straight-ahead-and-pose-to-pose, design/visual-flow]
verified: no (theory only)
source_inspiration: [https://milanote.com/guide/motion-graphics-pre-production, https://motionographer.com/2023/06/15/5-storytelling-questions-to-consider-when-creating-styleframes/, https://vivamedia.ca/blog/frame-by-frame-heres-what-to-know-about-working-with-style-frames]
---

# Storyboards and style frames

A **storyboard** decides what happens: the sequence of key moments, each a rough frame with a note about
motion, text and sound. **Style frames** decide how it looks: two to five finished-quality stills that set
colour, type, texture and composition. Approve both before animating; changes are cheap on paper and
expensive in motion.

## The idea

- **Storyboard first**: action and story. Rough is fine; arrows show motion, notes show timing and sound.
- **Style frames second**: pick the most important moments (the hook, a typical scene, the end card) and
  finish them as if they were final frames.
- **Moodboard before style frames** when the look is open: references for colour, type, motion and texture.
- **Each frame answers**: who is this for, what is the focal point, what moves, what is said, what is heard.

## Rules of thumb

- One storyboard panel per beat (roughly every 2–5 s); a 30 s promo is 8–12 panels.
- Write the on-screen text in the panels exactly; it sets the read time and therefore the timing.
- Mark transitions between panels (cut, wipe, match cut) and the eye path ([visual flow](../design/visual-flow.md)).
- Style frames at the delivery resolution and aspect ratio; if there are two aspect ratios, frame both.

## Do and don't

- Do show the end card and the hook in the style frames; they carry the message.
- Do get the storyboard signed off before style frames, and style frames before animation.
- Don't present ten style directions; present two or three distinct ones.
- Don't let the storyboard contain text that will not fit its read time.

## Checklist

- [ ] Every beat of the script has a panel.
- [ ] On-screen text written in full in the panels.
- [ ] Two to five style frames approved at delivery size.
- [ ] Transitions and eye path marked.

## In Carvercat

No Carvercat measurements on this page. Working practice:

- Build style frames as real comps, not separate artwork: a still comp per frame, using the fonts and
  palette the film will use. They then become the key poses ([pose to pose](../principles/straight-ahead-and-pose-to-pose.md)).
- Export stills for review: `export.set {settings:{format:"still"}}` or `carvercat_render {dir, from, to}`
  for PNG frames ([delivery](delivery.md)).
- Contact sheets of a sequence for the storyboard review: `carvercat_look {fps:2}`.
- Templates as starting points for typical frames: [patterns](../../ai/patterns/README.md).
