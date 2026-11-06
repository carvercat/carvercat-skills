---
id: principles/exaggeration
title: Exaggeration and overshoot
section: principles
tags: [exaggeration, overshoot, back easing, spring, emphasis, punch]
styles: [cartoon-bounce, funky, kinetic-typography, social-short-form, sports]
topics: [emphasis, easing]
related: [principles/anticipation, principles/squash-and-stretch, principles/weight, principles/appeal, principles/slow-in-slow-out]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation, https://dribbble.com/stories/2020/07/27/disney-principles-of-animation-ui-interactions, https://designproject.io/blog/5-animation-principles-figma/, https://web.dev/articles/choosing-the-right-easing]
---

# Exaggeration and overshoot

Exaggeration pushes a move past realism so its meaning reads instantly: the pop is bigger, the slam
harder, the bounce higher. In graphics its most common form is **overshoot**: the value goes past its
target and settles back.

## The idea

- Exaggerate the **idea** of the action, not every action: the hero, the key number, the punchline.
- Overshoot says "springy, energetic, light". It also hides the moment of arrival in a little flourish.
- Push the brief's register: a toy brand can take 25%, a bank about 0–4%.
- Exaggeration needs contrast. A 16% pop among calm neighbours reads; among ten other pops it is noise.

## Rules of thumb

| Register | Overshoot | Settle | Swings |
|---|---|---|---|
| Corporate, luxury, data accuracy | 0% | — | — |
| UI, product, SaaS | 3–5% | 6–10 f | 1 |
| Social, kinetic type, sports | 8–16% | 8–12 f | 1–2 |
| Cartoon, funky, kids | 20–30% | 10–20 f | 2–3 decaying |

- Never overshoot full-frame transitions, camera moves, or things that must look precise (chart bars that
  represent values, unless the brief accepts a playful style).
- Overshoot rotation more than position: a 10° swing past the rest angle reads, 40 px past a target looks
  like an error.

## Measured in Carvercat: back curves

Scale 0 → 1 over 16 f with one custom curve on the first key (the one the move leaves), `cubic-bezier(0.34, y1, 0.64, 1)`, read with
`carvercat_inspect mode:curves`:

| `ease` | Overshoot | Peak (frames into the move) | Settled within 0.5% (frames into the move) |
|---|---|---|---|
| `cubic-bezier(0.34, 1.3, 0.64, 1)` | 3.0% | 11 | 14 |
| `cubic-bezier(0.34, 1.56, 0.64, 1)` | 9.8% | 9 | 15 |
| `cubic-bezier(0.34, 1.75, 0.64, 1)` | 15.8% | 8 | 15 |
| `cubic-bezier(0.34, 2, 0.64, 1)` | 25.0% | 8 | 15 |
| Three keys: 0 → 1.08 at 11 f (quad out) → 1 at 16 f (S-curve) | 8.0% | 11 | 15 |

- The first handle's y sets the size of the overshoot: 1.3 is subtle, 1.56 is the classic "back", 2.0 is
  cartoon.
- A single cubic curve makes exactly one overshoot. Two or more decaying swings need more keys, or a
  baked spring preset.

## Do and don't

- Do reserve the strongest overshoot for one element per scene.
- Do match overshoot to weight: lighter things overshoot more ([weight](weight.md)).
- Don't put an overshooting curve on opacity: its range is 0 to 1, so there is nothing to overshoot into; ease it out instead.
- Don't overshoot text below about 94% of its rest size on the way in; `inspect lint` flags text that is
  too small during a scale entrance ([typography](../../ai/references/craft/typography.md)).

## Checklist

- [ ] Overshoot amount matches the style's register table above.
- [ ] Only the hero overshoots hard.
- [ ] `inspect curves` reports the overshoot % and settle frame you planned.

## In Carvercat

- Curve names on this page (S-curve, quad out) are `ease` strings: [names](easing-reference.md#names-used-in-this-wiki).
- Template examples with measured numbers and lint traps for this principle: [craft principle page](../../ai/references/craft/principles/exaggeration.md).
- One overshoot: `ease: "cubic-bezier(0.34, 1.56, 0.64, 1)"` on the key the move leaves, e.g. `anim.set {keyframes: [{at: 0, scale: 0, ease: "cubic-bezier(0.34, 1.56, 0.64, 1)"}, {at: 16, scale: 1}]}`.
  Old way, accepted for one release: `"easing": "Custom", "customEase": [0.34, 1.56, 0.64, 1]` on the arriving key (or `key.handle` out (0.34, 1.56) on the first key, in (0.64, 1) on the second).
- Springs with several swings are an ease of their own (`spring(0.8, 0.5)`, see [springs](springs.md)); older: baked into keys by `ai/scripts/motion/curves.py`; ready-made:
  `Pop - spring` (16.2%), `Pop - gentle` (4.4%), `Swing in` (16.3% past zero),
  `Stamp` (4.6% undershoot) in [Motion Patterns](../../ai/patterns/README.md); `Pop - wobbly` (30.8%) in
  [Cartoon Bounce](../../ai/patterns/cartoon-bounce.md); `Tilt pop` (30.9% angle) in
  [Funky](../../ai/patterns/funky.md).
- Per-style overshoot limits measured on the packs: [timing by style](../../ai/references/craft/timing-by-style.md).
- Lab: comp `W Overshoot` in [the principles lab](../labs/README.md).
