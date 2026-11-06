---
id: principles/springs
title: Springs and damping
section: principles
tags: [spring, damping ratio, overshoot, wobble, physics, bounce, baked keys, settle]
styles: [cartoon-bounce, funky, social-short-form, saas-ui, kinetic-typography]
topics: [easing, physics]
related: [principles/exaggeration, principles/easing-reference, principles/weight, principles/follow-through-and-overlap]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://web.dev/articles/choosing-the-right-easing, https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md, https://skills.cat/skills/dylantarre/animation-principles/video-motion-graphics]
---

# Springs and damping

A spring overshoots its target and swings back, each swing smaller, until it rests. It is the most natural
way to show elasticity and energy, and one number describes its character: the **damping ratio** (ζ). Low
ζ wobbles a lot; ζ = 1 arrives without overshoot (critically damped); higher is sluggish.

## The idea

- A cubic curve can overshoot only once. A spring can swing several times, which reads as "springy" rather
  than "eased".
- Damping sets personality: 0.3 rubbery, 0.5 bouncy, 0.7 gentle, 0.85–1.0 confident with no visible
  bounce. Duration sets how fast it all happens.
- Springs suit things that are light and alive (icons, stickers, badges, cartoon parts), not cameras,
  full-frame transitions or serious data.

## Measured in Carvercat

A spring is an ease: `spring(duration, bounce)` or `spring(stiffness, damping, mass)`. The app bakes it into one
key per frame, so what you get in the project is plain keys. Each dot below travelled 1000 px over 24 f with a
spring of the given damping ratio, first baked by a script (Linear joins between keys), then probed every frame:

| Damping ζ | Overshoot | Crossings of the target | Half the distance by | Settled (0.5%) by | Keys after baking |
|---|---|---|---|---|---|
| 0.3 | 34.8% | 5 | frame 2 | frame 23 | 19 |
| 0.4 | 25.2% | 3 | frame 3 | frame 23 | 16 |
| 0.5 | 16.2% | 3 | frame 3 | frame 21 | 14 |
| 0.6 | 9.4% | 2 | frame 4 | frame 23 | 14 |
| 0.7 | 4.6% | 1 | frame 5 | frame 23 | 13 |
| 0.85 | 0.3% | 1 | frame 6 | frame 19 | 12 |
| 1.0 | 0.0% | 0 | frame 5 | frame 21 | 13 |

- The same table with the native ease, checked on a headless Carvercat built from Carvercat 0.1.8
  (Carvercat 0.1.8): `spring(0.8, b)` on a 1000 px move over 24 f (0.8 s), read every frame. `bounce` is 1 − ζ:

  | ζ | `ease` | Overshoot | Half the distance by | Settled (0.5%) by |
  |---|---|---|---|---|
  | 0.3 | `spring(0.8, 0.7)` | 37.0% | frame 5 | frame 24 |
  | 0.4 | `spring(0.8, 0.6)` | 25.4% | frame 5 | frame 24 |
  | 0.5 | `spring(0.8, 0.5)` | 16.3% | frame 5 | frame 23 |
  | 0.6 | `spring(0.8, 0.4)` | 9.5% | frame 6 | frame 24 |
  | 0.7 | `spring(0.8, 0.3)` | 4.6% | frame 6 | frame 24 |
  | 0.85 | `spring(0.8, 0.15)` | 0.6% | frame 6 | frame 24 |
  | 1.0 | `spring(0.8, 0)` | 0.0% | frame 7 | frame 24 |

  The named springs overshoot `spring-default` 0%, `spring-gentle` 7.3%, `spring-wobbly` 20.7%, `spring-stiff`
  5.0%, `spring-slow` 0%. A spring on a bounded property (opacity) that would overshoot 1 is refused; use
  `spring(duration, 0)` there.
- Overshoot falls fast with damping: about 35% at 0.3, 16% at 0.5 (the classic "bouncy" spring, the same as
  `Pop - spring`), under 5% from 0.7.
- Lower damping is also **faster to the target**: half the distance in 2 f at ζ 0.3, 5–6 f at 0.85–1.0.
- All of them settle near the end of their 24 f because `spring()` sizes the curve to settle at its length;
  choose the length for the time you want it to take, then ζ for the character.
- Baking keeps the file small: 12–19 keys for 24 f, with linear joins accurate to 0.6% of the travel.

## Do and don't

- Do use ζ 0.6–0.8 for UI and product pops, 0.4–0.5 for playful, 0.3 only for cartoon wobble.
- Do keep one damping value per film for the same kind of element.
- Don't spring text that must be read straight away; the swings delay the moment it is still.
- Don't spring position and scale of the same object with different damping; it looks broken.

## Checklist

- [ ] Damping chosen from the table by register; one value per element type.
- [ ] `inspect curves` shows the overshoot and settle you planned.
- [ ] No springs on cameras, transitions or data values.

## In Carvercat

- Springs: `anim.set {keyframes: [{at: 0, scale: 0.6, ease: "spring(0.8, 0.5)"}, {at: 24, scale: 1}]}` (ζ = 1 −
  bounce; the first number is the period in seconds) or `ease: "spring-gentle"`. The app bakes one key per frame.
  Old way, accepted: bake with `curves.spring(zeta, frames)` and `curves.bake(curve, frames)` and write the keys
  with `linear` ([custom curves](../../ai/patterns/custom-curves.md)).
- Ready-made springs: `Pop - spring` (16.2%), `Pop - gentle` (4.4%), `Swing in` ([Motion Patterns](../../ai/patterns/README.md));
  `Pop - wobbly` (30.8%), `Jelly in` ([Cartoon Bounce](../../ai/patterns/cartoon-bounce.md)); `Toast drop - spring`
  ([SaaS UI](../../ai/patterns/saas-ui.md)).
- Single overshoot without baking: a back curve ([exaggeration](exaggeration.md)).
- Lab: comp `E Springs` in [the measurement lab 2](../labs/README.md).
