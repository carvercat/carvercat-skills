---
id: principles/slow-in-slow-out
title: Slow in and slow out (easing)
section: principles
tags: [easing, ease out, ease in, s-curve, bezier, custom ease, acceleration, deceleration]
styles: [all]
topics: [easing, timing]
related: [principles/timing-and-spacing, principles/weight, principles/exaggeration, principles/arcs, techniques/stagger-systems]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation, https://web.dev/articles/choosing-the-right-easing, https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md, https://carbondesignsystem.com/elements/motion/overview/, https://atlassian.design/foundations/motion, https://learn.microsoft.com/en-us/windows/apps/design/motion/timing-and-easing, https://medium.com/motion-in-interaction/bea05243fe3]
---

# Slow in and slow out (easing)

Real things do not start or stop instantly: they gather speed and lose it. Easing is how a move
spends its frames, bunched at the ends and spread in the middle. In motion graphics it is the one
principle that applies to almost every key you set.

## The idea

- **Ease out (decelerate, `ease-out`)**: fast start, gentle arrival. The thing is already moving when we see it and
  comes to rest. Use it for anything that **arrives**.
- **Ease in (accelerate, `ease-in`)**: gentle start, fast finish. Use it for anything that **leaves for good**.
  Never end an on-screen move with it: the object hits its end pose at full speed and looks stopped by a wall.
- **S-curve (ease in and out, `ease-in-out`)**: slow, fast, slow. For an object that moves from one rest pose to another
  while staying on screen, and for camera-like moves.
- **Linear** (`linear`): constant speed. Only for things that never start or stop inside the shot (a spinning
  radar, a ticker, a drifting background, a progress bar tied to time).
- Naming warning: some animation texts call a decelerating move "slow in" and some software calls it
  "ease in". This wiki names easing by what the speed does. The CSS words are the same as the call: `ease-out`
  decelerates. The named curves it measured are listed in [easing reference](easing-reference.md#names-used-in-this-wiki).

## Rules of thumb

- Arrivals decelerate, departures accelerate, on-screen relocations use an S-curve.
- The stronger the curve, the shorter the move can be and still read: a premium expo-out arrival of
  18 f feels as calm as a 30 f plain ease out.
- One easing family per film. Vary durations, not curve styles ([brand systems](../../ai/references/craft/brand-systems.md)).
- Moves under about 5 f: ease out only; the eye cannot see an S-curve that short.
- Bounce and elastic curves need room to settle (about 25 f or more) and belong to playful styles.

## Measured in Carvercat

A dot travelled 1200 px in 20 f (frames 10 to 30), the `ease` written on the key it leaves; positions were
read every frame with `carvercat_inspect mode:probe`. "Peak" is the fastest single frame compared with
the linear move's 60 px a frame.

| `ease` on the leaving key | Travel done at 25% of the time | at 50% | at 75% | Peak speed | Where the peak is |
|---|---|---|---|---|---|
| `linear` | 25.0% | 50.0% | 75.0% | 1.0× | everywhere |
| quad in, `cubic-bezier(0.333333, 0, 0.666667, 0.333333)` | 6.2% | 25.0% | 56.2% | 1.95× | last frame |
| quad out, `cubic-bezier(0.333333, 0.666667, 0.666667, 1)` | 43.8% | 75.0% | 93.8% | 1.95× | first frame |
| S-curve, `cubic-bezier(0.333333, 0, 0.666667, 1)` | 15.6% | 50.0% | 84.4% | 1.5× | middle |
| expo out, `cubic-bezier(0.16, 1, 0.3, 1)` | 82.6% | 97.2% | 99.8% | 5.6× | first frame |
| decelerate, `cubic-bezier(0.05, 0.7, 0.1, 1)` | 83.2% | 95.0% | 99.0% | 9.0× | first frame |
| standard, `cubic-bezier(0.2, 0, 0, 1)` | 60.7% | 87.8% | 97.5% | 3.9× | frames 2 to 3 |
| accelerate, `cubic-bezier(0.3, 0, 0.8, 0.15)` | 3.5% | 15.4% | 40.6% | 3.6× | last frame |
| smooth, `cubic-bezier(0.65, 0, 0.35, 1)` | 7.1% | 50.0% | 92.9% | 2.7× | middle |

What the numbers say:
- The model's own named curves are gentle. Quad out matches 1 − (1 − t)², quad in matches t², and the S-curve
  matches 3t² − 2t³, to the pixel. The CSS keywords are a little stronger (`ease-out` 37.8% at a quarter,
  `ease` 40.9%; see [easing reference](easing-reference.md)). They are fine for small, quiet moves and weak for hero arrivals.
- Expo out and decelerate are front-loaded: more than 80% of the travel is done in the first quarter.
  This is what reads as "premium" and why such moves can be short.
- An accelerating custom exit leaves 60% of its travel for the last quarter, so it vanishes decisively.
- `inspect lint` adds an info note `speed_jump` on moves that start at full speed (expo, decelerate). It is
  expected for arrivals that begin off screen or invisible; ease the first key only if the jump shows.

## Do and don't

- Do put the `ease` on the key the move **leaves**: as in CSS, a key's ease shapes the segment that starts at it, so the
  last key has none.
- Do pair a front-loaded arrival with a fade that finishes early (opacity full by about 40% of the move).
- Don't leave `linear` on anything that starts or stops in frame.
- Don't use `ease-in` on an entrance: the object crawls at the start, which is when the viewer is looking.
- Don't mix three curve families in one scene; the motion looks like it came from three designers.

## Checklist

- [ ] Every arrival uses `ease-out` or a decelerating `cubic-bezier`.
- [ ] Every final exit uses `ease-in` or an accelerating `cubic-bezier`, about 70% of the entrance length.
- [ ] `linear` appears only on continuous motion.
- [ ] `carvercat_inspect mode:curves` shows the settle frame where you expect it.

## In Carvercat

- Template examples with measured numbers and lint traps for this principle: [craft principle page](../../ai/references/craft/principles/slow-in-slow-out.md).
- Easing lives on keys, written as CSS: `anim.set {id, keyframes: [{at: 0, y: 40, ease: "cubic-bezier(0.16, 1, 0.3, 1)"},
  {at: "14f", y: 0}]}` or `key.set {key: "y", value: 0, at: "14f", ease: "ease-out"}`. The `ease` shapes the segment
  that **leaves** the key; the last key has none. Words: `linear`, `ease`, `ease-in`, `ease-out`, `ease-in-out`,
  `cubic-bezier(x1, y1, x2, y2)`, `steps(n)`, `hold`, `spring(...)`.
- Old names, accepted for one release: `easing` as `Linear`, `Ease in`, `Ease out`, `S-curve`, `Hold` or `Custom` with
  `customEase`, written on the **arriving** key, and `key.handle`. They read back as `cubic-bezier` of their handles; see
  [custom curves](../../ai/patterns/custom-curves.md).
- Ready-made arrivals with expo-out baked in: `Rise - expo`, `Slide from left - expo`,
  `Slide from right - expo`, `Zoom settle` ([Motion Patterns](../../ai/patterns/README.md)); exits:
  `Exit up - accelerate`, `Exit left - accelerate`, `Exit fade - fast`.
- Per-style curve families and measured settle frames: [timing by style](../../ai/references/craft/timing-by-style.md).
- Check a curve with `carvercat_inspect {mode:"curves", objects:"Name"}`: it prints the keys, the
  easing names, peak speed, overshoot % and settle frame.
- Lab: comp `W Spacing` in [the principles lab](../labs/README.md).
