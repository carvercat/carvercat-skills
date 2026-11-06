---
id: cookbook/lower-third-speaker-swap
title: Swap a lower third between two speakers
section: cookbook
tags: [lower third, name, title, speaker, interview, panel, swap, resize plate, broadcast]
styles: [corporate-brand, sports, explainer, minimal-luxury]
topics: [text, layout]
related: [cookbook/readable-lower-third, cookbook/word-swap, genres/broadcast-packages, sound-and-timing/reading-time]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Lower_third]
---

# Swap a lower third between two speakers

**Goal.** One lower third that changes from speaker A to speaker B in an interview: the names and roles
swap and the plate resizes to the new, longer name, without the graphic leaving the screen.

## Steps

1. Measure both names (56 px Bold) and roles (34 px Medium). Plate width for each = the longer of its two
   lines + 2 × 40 px padding + the accent bar.
2. Draw the plate at the **largest** width, anchored on its **left edge** (`transformOrigin` `"0% 50%"`), and key
   `scale` `[width / largest width, 1]`: 0 → A in (expo, 12 f), A → B (S-curve, 12 f), B → 0 out.
3. Names and roles as separate clips per speaker. Out: A's name rises 20 px and fades over 7 f
   (accelerate), the role 3 f later. In: B's name from 24 px below, expo 12 f, the role 3 f later.
4. Start B a few frames **after** A is gone, and resize the plate in that gap, so two names are never on
   screen together.

## Measured in Carvercat 0.1.6

Comp `K Speaker swap` in [cookbook lab 5](../labs/README.md#cookbook-lab-5carverproj): A "Maya Okafor" / "Head
of Design" f8–f71, B "Daniel Reyes-Whitfield" / "Chief Operating Officer" from f76, plate resize f70–f82;
`inspect probe`:

| | Plate left | Plate right | Longest line right | Padding |
|---|---|---|---|---|
| Speaker A (f40) | 160.0 | 565.8 | 525.8 | 40.0 |
| Speaker B (f110) | 160.0 | 805.6 | 765.6 | 40.0 |

- The left edge held at 160.0 through the resize (159.9 at f76) while the right edge went 565.8 → 805.6;
  the plate closed back to 160.0 by f148.
- A's name was at opacity 0.41 on f70 and 0 on f71; B's started on f76. **No frame showed both names.**
- `inspect lint`: 0 errors, 0 warnings, 15 notes (repeated keys and the exit's `speed_jump`).

## Traps

- Bounds drop a trailing space, so measure the lines without one: [KI-149](../../ai/references/known-issues.md#ki-149).
- `text.content` can't be keyed; a new name is a new clip: [KI-051](../../ai/references/known-issues.md#ki-051).
- `scale` resizes the whole plate, `borderRadius` included; this lab kept the radius small (10 px). A true pill is
  `borderRadius: "50%"` on a rectangle (the old `cornerRadius` stopped at a quarter of the short side: [KI-121](../../ai/references/known-issues.md#ki-121)).

## In Carvercat

- Curve names on this page (S-curve, accelerate) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Lower third - two boxes` ([cb-lower-third](../../ai/patterns/cb-lower-third.md)), `Speaker lower third`
  ([ex-lower-third](../../ai/patterns/ex-lower-third.md)), `Kinetic lower third`, `Player lower third`.
- Background: [readable lower third](readable-lower-third.md), [reading time](../sound-and-timing/reading-time.md).
