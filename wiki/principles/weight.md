---
id: principles/weight
title: Weight
section: principles
tags: [weight, mass, inertia, heavy, light, settle, physics]
styles: [all]
topics: [timing, physics]
related: [principles/timing-and-spacing, principles/slow-in-slow-out, principles/squash-and-stretch, principles/follow-through-and-overlap, principles/exaggeration]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.lollypop.design/blog/2019/march/the-forgotten-art-of-spacing/, https://fluent2.microsoft.design/motion, https://www.pluralsight.com/resources/blog/software-development/character-animation-fundamentals-timing-spacing, https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation]
---

# Weight

The viewer judges how heavy something is from how it starts, stops and reacts. A heavy object takes
longer to get going and longer to stop, and its landing shakes things. A light object darts and stops
almost instantly. Getting weight right makes graphics feel physical; getting it wrong makes them float.

## The idea

- **Inertia**: mass resists change. Heavy = long acceleration and long deceleration (an S-curve with a
  long tail); light = short, front-loaded moves.
- **Impact**: heavy things transfer energy when they stop: a short squash, a small camera bump, a dust
  puff, a low sound.
- **Size and weight usually agree**: big things are heavy. Breaking that rule (a huge thing that darts)
  reads as weightless, which can be a deliberate style (UI, HUD).
- Weight is relative within a scene: give the hero more mass than its supporting elements.

## Rules of thumb

| Feel | Duration for the same travel | Curve | Landing |
|---|---|---|---|
| Light (icon, chip, small dot) | 8–14 f | strong ease out (expo) | none, or a 3–5% overshoot |
| Medium (card, headline) | 14–22 f | ease out / standard | 2–4% settle |
| Heavy (hero product, big block, logo slab) | 24–40 f | S-curve with long deceleration | 3–5% squash on contact, small shake |

- Heavy objects overshoot less, not more. Overshoot reads as springiness, which is lightness.
- Let the impact of a heavy landing reach other objects 1–3 f later (camera bump, neighbouring items jolt).

## Measured in Carvercat

Two objects travelled the same 1200 px:

| Object | Move | Curve | Settles (0.5%) | Peak speed |
|---|---|---|---|---|
| Light: 50 px dot | 12 f | expo out `cubic-bezier(0.16, 1, 0.3, 1)` | 8 f after it starts | first frame |
| Heavy: 260 px square | 30 f | smooth `cubic-bezier(0.65, 0, 0.35, 1)` | 27 f after it starts | middle of the move (f25) |

The heavy square then squashed `[1.04, 0.96]` for 4 f on arrival and settled at f46. Read side by side,
the dot looks flicked and the square looks pushed. Same distance; only timing, spacing and landing differ.

## Do and don't

- Do decide every object's weight before animating; write it next to its role in the plan.
- Do let heavy objects arrive later in a stagger and settle last.
- Don't give a heavy object a springy overshoot.
- Don't give a tiny label a 40 f journey; it will feel stuck in syrup.

## Checklist

- [ ] Heavier objects have longer moves and longer settles.
- [ ] Only light or playful objects overshoot noticeably.
- [ ] Heavy landings have a small reaction (squash, shake or sound) within 1–3 f.

## In Carvercat

- Curve names on this page (S-curve, expo out, smooth) are `ease` strings: [names](easing-reference.md#names-used-in-this-wiki).
- Duration: key spacing in frames. Curve: the `ease` of the key the move leaves (quad out, S-curve, or any `cubic-bezier(...)`;
  old: the arriving key's `easing`, or `Custom` with `customEase`).
- Landing squash: `scale` `[1.04, 0.96]` with the `transformOrigin` on the contact edge
  (`transformOrigin` `"50% 100%"`), back to `[1, 1]` over 4–6 f.
- A camera bump: offset a camera null (parent of the scene objects) 6–12 px for 2 f and settle back over
  6–8 f ([camera moves in 2D](../techniques/camera-moves-2d.md)).
- Presets by weight: light `Pop - spring` (16.2% overshoot), medium `Pop - gentle` (4.4%), heavy
  `Impact slam` ([Sports](../../ai/patterns/sports.md)) or `Stamp` (4.6% undershoot)
  ([Motion Patterns](../../ai/patterns/README.md)).
- Lab: comp `W Weight` in [the principles lab](../labs/README.md).
