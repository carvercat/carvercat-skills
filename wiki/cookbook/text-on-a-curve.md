---
id: cookbook/text-on-a-curve
title: Set text on a curve, one letter at a time
section: cookbook
tags: [text on a curve, arc text, curved text, circular text, badge text, letters, rotation, path text]
styles: [funky, cartoon-bounce, minimal-luxury, social-short-form]
topics: [text, layout, rotation]
related: [cookbook/sale-badge-spin-in, cookbook/orbit, techniques/kinetic-type, techniques/text-spacing-animation, cookbook/headline-word-by-word]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Kerning]
---

# Set text on a curve, one letter at a time

**Goal.** A word bent along an arc, letters upright to the curve, fading in left to right. Carvercat has no text on
a path ([FR-050](../../ai/references/known-issues.md#fr-050)), so each letter is its own text, placed and turned.

## Steps

1. One text per letter, 130 px Bold, centred (align `center`). A space is an empty slot.
2. Choose the **centre** C = (960, 880), the **radius** R = 520 px and an **angle step** of 10° (letters 66 px
   apart on the arc). Letter *i* of *n* sits at angle *a* = (*i* − (*n* − 1) / 2) × 10°, measured clockwise
   from straight up.
3. Position it at (C*x* + R sin *a*, C*y* − R cos *a*), y down.
4. **Rotate it by *a***: `rotate` is clockwise, so the letter at 50° to the right is turned 50° clockwise, which is
   `rotate` `"50deg"` (the 0.1.6 note stored −50°).
5. Fade the letters in 2 f apart: opacity 0 → 1 over 6 f, letter *i* from f 2 *i*.

## Measured in Carvercat 0.1.6

Comp `K Arc text` ("HELLO WORLD", 10 letters and a space) in [cookbook lab 9](../labs/README.md#cookbook-lab-9carverproj);
`inspect probe` of each letter on f30:

| Letter | H | E | L | L | O | W | O | R | L | D |
|---|---|---|---|---|---|---|---|---|---|---|
| Rotation | −50.0 | −40.0 | −30.0 | −20.0 | −10.0 | 10.0 | 20.0 | 30.0 | 40.0 | 50.0 |
| Bounds centre x | 561.2 | 625.3 | 699.7 | 781.9 | 869.6 | 1050.4 | 1138.1 | 1220.3 | 1294.7 | 1358.8 |
| Bounds centre y | 545.3 | 481.2 | 429.1 | 390.7 | 367.3 | 367.3 | 390.7 | 429.1 | 481.2 | 545.3 |

- The angle of each box centre seen from C is −49.99° … 49.99°, equal to the intended angle to 0.01°; its distance
  from C is **520.6–520.7 px**, the same for all ten (R plus 0.6 px: the box centre is not the letter's position).
- The space leaves a 20° gap (letters O and W sit at −10° and +10°).
- Fade: letter 1 is 0.56 on f2 and 1.0 on f8; letter 11 is 0.56 on f22 and 1.0 on f26.
- `inspect lint`: 0 errors, **5 warnings**, `text_overlap` of 15–27% between neighbours: it compares
  upright boxes of turned letters ([KI-156](../../ai/references/known-issues.md#ki-156)). `carvercat_look` shows no letter touching.

## Traps

- Equal angle steps are equal arc lengths, not equal letter widths: "W" is wide and "I" narrow, so the spacing
  looks uneven. For headlines, add each letter's measured advance to the angle instead (measure with
  `carvercat_authoring mode:geometry`, as in [breaking news bar](breaking-news-bar.md)).
- Rotation sign: `rotate` positive turns clockwise; the old stored rotation was positive counter-clockwise ([weather icon loop](weather-icon-loop.md)).
- Letters edit separately: changing the word means rebuilding the letters.
- A full circle needs the angle step 360° / (letters + spaces).

## In Carvercat

- Commands: `property.set` on each letter's position and rotation; `text.outline` turns a text into Bezier contours
  (a route to editing the shape of a whole word, not a bend).
- Background: [kinetic type](../techniques/kinetic-type.md), [text spacing animation](../techniques/text-spacing-animation.md),
  [sale badge spin-in](sale-badge-spin-in.md).
