---
id: principles/rhythm
title: Rhythm
section: principles
tags: [rhythm, cadence, pacing, stagger, beat, repetition, variation]
styles: [all]
topics: [pacing, choreography]
related: [principles/timing-and-spacing, techniques/stagger-systems, sound-and-timing/beat-sync, techniques/rhythm-editing, principles/follow-through-and-overlap]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://carbondesignsystem.com/elements/motion/choreography/, https://fluent2.microsoft.design/motion, https://www.silvermansound.com/bpm-to-fps-calculator, https://www.premiumbeat.com/blog/cut-to-the-beat-tip-for-editing-to-music-in-final-cut-pro-x/]
---

# Rhythm

Rhythm is the pattern of events over time: when things start, land and rest. A film with good rhythm
feels inevitable even with the sound off. Rhythm works at three scales: inside one move (spacing), across
a group (stagger), and across the film (beats, scenes, breathers).

## The idea

- **Regular intervals** create a pulse the viewer can predict and lean into (bars rising every 4 f).
- **Variation** keeps the pulse alive: a long hold after a run of quick hits, a pause before the payoff.
- **Accents** are the events that break or land on the pulse: the hero, the number, the logo.
- Silence counts. A still frame between two busy beats is part of the rhythm.

## Rules of thumb

- Group stagger: 3–6 f between items; total spread at most 15–20 f; more than 5–6 items, stagger in groups.
- Scene rhythm: alternate busy and calm. One breather (held, quiet frame) every 8–12 s in a promo.
- Vary scene lengths: the slowest scene about 3× the fastest.
- With music, pulse on beats (frames per beat = 1800 / BPM at 30 fps; see [beat sync](../sound-and-timing/beat-sync.md)),
  accents on bar starts, big reveals on phrase starts.
- Repetition must be exact to read as rhythm: same duration, same curve, same gap.

## Measured in Carvercat

Six bars, each `scale` `[1, 0]` → `[1, 1]` over 14 f (expo out, `transformOrigin` `"50% 100%"`), started 4 f apart
from f10 (`carvercat_inspect mode:timing`):

| Bar | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Visible from | f11 | f15 | f19 | f23 | f27 | f31 |
| Settles | f22 | f26 | f30 | f34 | f38 | f42 |

The landings form the same 4 f pulse as the starts, so the eye reads one even ripple of 32 f. A beat dot
pulsing every 15 f (120 BPM: 1 → 1.25 in 3 f, back over 9 f) above them shows how a 4 f object stagger and
a 15 f beat can coexist: the stagger is the texture, the beat is the pulse.

## Do and don't

- Do choose the interval first, then fit the elements to it.
- Do break the rhythm deliberately for the payoff (a beat of stillness, then the hit).
- Don't let small timing errors creep in (3, 4, 5, 3 f gaps read as sloppy, not as variation).
- Don't run the whole film at one tempo.

## Checklist

- [ ] Staggered groups use one fixed gap.
- [ ] `inspect timing` shows an even cascade of settle frames.
- [ ] There is at least one deliberate pause in every 8–12 s.
- [ ] Accents land on beats or bar starts when there is music.

## In Carvercat

- Curve names on this page (expo out) are `ease` strings: [names](easing-reference.md#names-used-in-this-wiki).
- Text: the Stagger Text effect sets an exact gap: `stagger.set {by:"word", gap:3}`; `order` can be
  `forward`, `reverse`, `centre`, `edges` or `random` ([stagger](../../ai/references/effects/stagger.md)).
- Objects: offset key frames by a fixed amount (in a script, `f = start + i * gap`).
- Beats: compute frames from BPM and place keys on them; `kt-beat-words` uses a 25 f beat
  ([kt-beat-words](../../ai/patterns/kt-beat-words.md)).
- Ready-made rhythmic groups: `Bars stagger` (2 f per bar) in [Transitions](../../ai/patterns/transitions.md),
  `Ranked bars` and `Column chart` in [Data Viz](../../ai/patterns/data-viz.md), `Numbered list` (12 f per row)
  in [Kinetic Typography](../../ai/patterns/kinetic-typography.md).
- Lab: comp `W Rhythm` in [the principles lab](../labs/README.md).
