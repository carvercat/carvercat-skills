---
id: principles/easing-reference
title: Easing reference (measured)
section: principles
tags: [easing, cubic bezier, custom ease, curves, settle, overshoot, design tokens, material, carbon, fluent, atlassian]
styles: [all]
topics: [easing, timing, reference]
related: [principles/slow-in-slow-out, principles/timing-and-spacing, principles/springs, principles/exaggeration, history/flat-design-and-ui-motion]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md, https://m1.material.io/motion/duration-easing.html, https://carbondesignsystem.com/elements/motion/overview/, https://learn.microsoft.com/en-us/windows/apps/design/motion/timing-and-easing, https://atlassian.design/foundations/motion, https://web.dev/articles/choosing-the-right-easing]
---

# Easing reference (measured)

Every easing worth knowing, measured in Carvercat on the same move, so you can choose by numbers: how much
of the move is done at each quarter, whether it overshoots, when it settles and where it is fastest. Use it
with [slow in and slow out](slow-in-slow-out.md) (when to use which family) and [springs](springs.md)
(multi-swing overshoot).

## How to read the table

A dot travelled 1000 px in 20 f (keys at f10 and f30). The `ease` is written on the **first** key, the one the
segment leaves, as in CSS. Positions came from `carvercat_inspect mode:probe` every frame; overshoot and settle from `carvercat_inspect mode:curves`
(settle = the frame after which the value stays within 0.5% of its end, counted from the start of the move).
"Peak speed" is the fastest frame compared with the linear move's 50 px a frame.

## The curves

The curves are written as CSS easing strings. The model's old named easings read back as the
cubic-beziers of their own handles, and measured, they are exactly t² (**quad in**), 1 − (1 − t)² (**quad out**)
and 3t² − 2t³ (the **S-curve**). They are not CSS `ease-in` and `ease-out`: those are further down. Every other
curve is a `cubic-bezier(x1, y1, x2, y2)` (x 0 to 1, y −1.5 to 2.5). Design-system names are the published
token values, re-measured here as Carvercat keys.

| Curve | `ease` string | 25% time | 50% | 75% | Overshoot | Undershoot | Settles (f into a 20 f move) | Peak speed vs linear | Peak at |
|---|---|---|---|---|---|---|---|---|---|
| Linear | `linear` | 25.0% | 50.0% | 75.0% | 0% | 0% | 20 | 1.0× | constant |
| quad in | `cubic-bezier(0.333333, 0, 0.666667, 0.333333)` | 6.2% | 25.0% | 56.2% | 0% | 0% | 20 | 1.95× | end |
| quad out | `cubic-bezier(0.333333, 0.666667, 0.666667, 1)` | 43.8% | 75.0% | 93.8% | 0% | 0% | 19 | 1.95× | start |
| S-curve | `cubic-bezier(0.333333, 0, 0.666667, 1)` | 15.6% | 50.0% | 84.4% | 0% | 0% | 19 | 1.49× | middle |
| CSS `ease` | `ease` | 40.9% | 80.2% | 96.0% | 0% | 0% | 18 | 2.27× | frame 5 |
| CSS `ease-in` | `ease-in` | 9.3% | 31.5% | 62.2% | 0% | 0% | 20 | 1.64× | end |
| CSS `ease-out` | `ease-out` | 37.8% | 68.5% | 90.7% | 0% | 0% | 19 | 1.64× | start |
| CSS `ease-in-out` | `ease-in-out` | 12.9% | 50.0% | 87.1% | 0% | 0% | 19 | 1.71× | middle |
| expo out | `cubic-bezier(0.16, 1, 0.3, 1)` | 82.6% | 97.2% | 99.8% | 0% | 0% | 13 | 5.62× | start |
| quint out | `cubic-bezier(0.22, 1, 0.36, 1)` | 76.5% | 96.1% | 99.7% | 0% | 0% | 14 | 4.3× | start |
| circ out | `cubic-bezier(0, 0.55, 0.45, 1)` | 66.0% | 86.5% | 96.8% | 0% | 0% | 18 | 6.23× | start |
| cubic out | `cubic-bezier(0.33, 1, 0.68, 1)` | 57.7% | 87.2% | 98.3% | 0% | 0% | 16 | 2.87× | start |
| sine in-out | `cubic-bezier(0.37, 0, 0.63, 1)` | 14.5% | 50.0% | 85.5% | 0% | 0% | 19 | 1.58× | middle |
| M3 standard | `cubic-bezier(0.2, 0, 0, 1)` | 60.7% | 87.8% | 97.5% | 0% | 0% | 17 | 3.89× | frame 3 |
| M3 emph decel | `cubic-bezier(0.05, 0.7, 0.1, 1)` | 83.2% | 95.0% | 99.1% | 0% | 0% | 15 | 8.95× | start |
| M3 emph accel | `cubic-bezier(0.3, 0, 0.8, 0.15)` | 3.5% | 15.4% | 40.6% | 0% | 0% | 20 | 3.6× | end |
| M1 standard | `cubic-bezier(0.4, 0, 0.2, 1)` | 23.7% | 77.6% | 95.9% | 0% | 0% | 18 | 2.65× | frame 7 |
| M1 decel | `cubic-bezier(0, 0, 0.2, 1)` | 57.8% | 83.9% | 96.4% | 0% | 0% | 18 | 3.49× | start |
| M1 accel | `cubic-bezier(0.4, 0, 1, 1)` | 9.9% | 32.5% | 63.0% | 0% | 0% | 20 | 1.6× | end |
| Carbon prod std | `cubic-bezier(0.2, 0, 0.38, 0.9)` | 30.6% | 68.5% | 90.7% | 0% | 0% | 19 | 1.74× | frame 5 |
| Carbon expr std | `cubic-bezier(0.4, 0.14, 0.3, 1)` | 25.8% | 74.7% | 95.4% | 0% | 0% | 18 | 2.22× | frame 7 |
| Carbon prod enter | `cubic-bezier(0, 0, 0.38, 0.9)` | 43.8% | 73.0% | 91.3% | 0% | 0% | 19 | 2.11× | start |
| Carbon prod exit | `cubic-bezier(0.2, 0, 1, 0.9)` | 15.0% | 38.5% | 65.5% | 0% | 0% | 20 | 1.89× | end |
| Fluent decel | `cubic-bezier(0, 0, 0, 1)` | 69.1% | 89.0% | 97.6% | 0% | 0% | 17 | 6.14× | start |
| Fluent accel | `cubic-bezier(1, 0, 1, 1)` | 2.4% | 11.0% | 30.9% | 0% | 0% | 20 | 6.14× | end |
| Atlassian bold out | `cubic-bezier(0, 0.4, 0, 1)` | 79.4% | 93.0% | 98.6% | 0% | 0% | 16 | 9.67× | start |
| back out | `cubic-bezier(0.34, 1.56, 0.64, 1)` | 81.6% | 108.7% | 106.0% | 9.7% | 0% | 19 | 4.31× | start |
| anticipate in | `cubic-bezier(0.36, 0, 0.66, -0.56)` | -6.0% | -8.7% | 18.4% | 0% | 9.7% | 20 | 4.31× | end |
| back in-out | `cubic-bezier(0.68, -0.6, 0.32, 1.6)` | -9.8% | 50.0% | 109.8% | 10.5% | 10.5% | 20 | 4.68× | middle |

The four CSS keywords were added on the Carvercat 0.1.8 build; read the same way (a
1000 px move in 20 f, `carvercat_inspect mode:curves` for the settle and peak). The other rows are the
original measurements, and the lab project `E Curves` reproduces every one of them.

## Names used in this wiki

Pages say "S-curve", "quad out" and "expo out" for these exact curves. The call is the `ease` string:

| Name | `ease` string | Old name (accepted for one release) |
|---|---|---|
| linear | `linear` | `Linear` |
| quad in (t²) | `cubic-bezier(0.333333, 0, 0.666667, 0.333333)` | `Ease in` |
| quad out (1 − (1 − t)²) | `cubic-bezier(0.333333, 0.666667, 0.666667, 1)` | `Ease out` |
| S-curve (3t² − 2t³) | `cubic-bezier(0.333333, 0, 0.666667, 1)` | `S-curve` |
| expo out | `cubic-bezier(0.16, 1, 0.3, 1)` | `Custom` with `customEase` |
| decelerate (unqualified) | `cubic-bezier(0.05, 0.7, 0.1, 1)` | `Custom` |
| accelerate (unqualified) | `cubic-bezier(0.3, 0, 0.8, 0.15)` | `Custom` |
| back out (about 9.7% overshoot) | `cubic-bezier(0.34, 1.56, 0.64, 1)` | `Custom` with `customEase` |
| hold (jump at the next key) | `hold` | `Hold` |
| springs and steps | `spring(...)`, `steps(4, jump-end)`, baked into keys | none |

CSS `ease-in` and `ease-out` are **not** the old `Ease in` and `Ease out` (compare the rows above): a page that
says `ease-out` means the CSS curve; a page that says "quad out" means 1 − (1 − t)². A name the build does not
know is refused with code `bad-ease` (it used to become Linear silently).

## What the numbers say

- **Arrivals, strongest to gentlest by the 25% column**: M3 emphasised decelerate (83%), expo out (83%),
  Atlassian bold out (79%), quint out (77%), Fluent decelerate (69%), circ out (66%), M3 standard (61%),
  M1 decelerate (58%), cubic out (58%), named `Ease out` (44%), Carbon productive entrance (44%).
- **The strongest arrivals settle earliest** (expo 13 f, quint 14 f into a 20 f move) and leave a long
  invisible tail; gentle curves are still moving at the end (19–20 f).
- **Exits**: Fluent accelerate leaves 69% of the distance for the last quarter (the most abrupt); M3
  emphasised accelerate 59%; M1 accelerate 37%; named `Ease in` 44%.
- **Overshoot curves**: back out goes 9.7% past the target, peaking about halfway through the move; anticipate in dips
  9.7% backwards before leaving; back in-out does both (10.5% each way). They settle within a frame of the last key.
- **In-and-out curves** (S-curve, sine in-out, M1 standard, Carbon standards) are symmetric or nearly: use
  them for on-screen relocations, not for entrances.
- Design systems were tuned for interface elements of a few hundred milliseconds; on a 20 f (667 ms) video
  move the same curves read calmer than in an app.

## Do and don't

- Do pick one arrival curve and one exit curve per film, then vary durations.
- Do read the 25% column when a move feels late: a stronger arrival curve fixes it without shortening it.
- Don't use an exit curve (accelerate) for an entrance or the reverse.
- Don't use overshoot curves on serious data, camera moves or full-frame transitions.

## Checklist

- [ ] Arrival and exit curves chosen from this table and written in the project notes.
- [ ] `inspect curves` on the hero move shows the overshoot and settle you expect.

## In Carvercat

- Over MCP: `anim.set {id, keyframes: [{at: 0, x: 385, ease: "cubic-bezier(0.16, 1, 0.3, 1)"}, {at: "20f", x: 1385}]}`.
  The `ease` sits on the key the segment **leaves** (CSS rule); the last key has none. Read it back with
  `key.list {key: "x"}`, which answers with the CSS string. See [custom curves](../../ai/patterns/custom-curves.md).
- Old names, accepted for one release: `easing: "Ease in" | "Ease out" | "S-curve" | "Hold" | "Custom"` with
  `customEase`, and `key.handle`. They sit on the **arriving** key and read back as the `cubic-bezier` of their own
  handles, marked `old`.
- Measure your own: `carvercat_inspect {mode:"curves", objects:"Name"}` (it prints stored fractions and the old
  easing words; the shape of the curve is what you read there).
- Lab: comp `E Curves` in [the measurement lab 2](../labs/README.md).
