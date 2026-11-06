---
id: principles/secondary-action
title: Secondary action
section: principles
tags: [secondary action, ripple, shadow, particles, reaction, accent]
styles: [all]
topics: [choreography, emphasis]
related: [principles/follow-through-and-overlap, principles/staging, principles/appeal, sound-and-timing/beat-sync]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation, https://www.fable.app/blog/12-animation-principles-every-aspiring-motion-designer-should-know, https://dribbble.com/stories/2020/07/27/disney-principles-of-animation-ui-interactions]
---

# Secondary action

A smaller motion that supports the main one: the shadow that grows as a shape lands, the ring that
ripples out from a tap, the sparkle after a logo locks, the underline that draws after a word arrives.
It adds life and clarity without stealing the scene.

## The idea

- The primary action carries the meaning; the secondary action **reacts** to it.
- It is smaller, softer and later: it must never compete for attention.
- Good secondary actions explain physics or cause: a shadow says "this came from above"; a ripple says
  "this was pressed".
- Background ambience (drift, slow rotation) is not secondary action; it does not react to anything.

## Rules of thumb

- Start 2–4 f after the primary starts, or exactly on its landing frame for impact effects.
- Scale it down: 30–60% of the primary's size change, lower opacity, thinner lines.
- Keep it shorter than the primary or let it fade out while the primary holds.
- One secondary action per primary. A ripple, a shadow and particles together are noise.

## Measured in Carvercat

A hero square pops in (scale 0 → 1 over 16 f, back out, `cubic-bezier(0.34, 1.56, 0.64, 1)`); a shadow and a
ripple react (`carvercat_inspect mode:timing`):

| Object | Role | Visible from | Settles |
|---|---|---|---|
| Hero | primary pop | f11 | f26 |
| Shadow (ellipse 260 × 40, black, opacity to 0.5) | grows under the hero, expo out | f14 | f28 |
| Ripple (ellipse stroke 6 px, scale 1 → 1.7, opacity 1 → 0) | rings out at the overshoot | f21 | gone by f36 |

The shadow trails the hero by 3 f and settles 2 f after it, so the hero reads as landing on a surface;
the ripple starts at the hero's overshoot peak (about f19–21) and is gone 10 f after the hero settles.

## Do and don't

- Do tie the secondary to a cause in the primary (landing, press, overshoot peak, beat).
- Do keep its colour within the palette; the accent colour belongs to the primary.
- Don't loop a secondary action that was triggered by a one-time event.
- Don't let it extend the scene: it finishes inside the primary's hold.

## Checklist

- [ ] It starts after, or exactly on, the primary event that causes it.
- [ ] It is clearly smaller or fainter than the primary.
- [ ] It ends before the scene's exit begins.

## In Carvercat

- Curve names on this page (expo out, back out) are `ease` strings: [names](easing-reference.md#names-used-in-this-wiki).
- Template examples with measured numbers and lint traps for this principle: [craft principle page](../../ai/references/craft/principles/secondary-action.md).
- Ripple: an ellipse with `fill: "none"` and a `stroke` (`strokeWidth` 4–8 px), key
  `scale` 1 → 1.6–1.8 with expo out and `opacity` 1 → 0.
- Shadow under a landing shape: a dark ellipse below it, scale from 0 with the hero's timing shifted 2–3 f;
  or `dropShadow` on the hero (`"0 12px 16px #00000066"`: x y blur colour) keyed with the move
  ([shadow and glow](../techniques/shadow-and-glow-in-motion.md); old name: the `shadow` effect with `Offset Y`, `Softness`, `Opacity`, [shadow](../../ai/references/effects/shadow.md)).
- Ready-made: `Tap ripple` ([SaaS UI](../../ai/patterns/saas-ui.md)), `Emphasis pulse`
  ([Explainer](../../ai/patterns/explainer.md)), the underline in `Logo - stamp reveal`
  ([logo-stamp-reveal](../../ai/patterns/logo-stamp-reveal.md)).
- Draw-on underlines and boxes after a word lands: `trimEnd` `"0%"` → `"100%"` over 8–15 f
  ([stroke and trim](../../ai/references/effects/stroke-and-trim.md)).
- Lab: comp `W Secondary` in [the principles lab](../labs/README.md).
