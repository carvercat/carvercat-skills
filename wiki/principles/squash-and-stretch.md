---
id: principles/squash-and-stretch
title: Squash and stretch
section: principles
tags: [squash, stretch, volume, bounce, impact, cartoon, elasticity]
styles: [cartoon-bounce, funky, social-short-form, kinetic-typography]
topics: [deformation, impact, weight]
related: [principles/weight, principles/anticipation, principles/exaggeration, principles/arcs, principles/timing-and-spacing]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation, https://courses.cs.washington.edu/courses/cse458/21au/content/exercises/animation_principles.html, https://patents.google.com/patent/US7221379, https://playbooks.com/skills/dylantarre/animation-principles/squash-stretch-mastery, https://lottiefiles.com/blog/tips-and-tutorials/mastering-disney-12-principles-animation]
---

# Squash and stretch

An object that deforms when it hits, pushes or accelerates looks alive and made of something. It
squashes on impact, stretches when it moves fast, and keeps roughly the same volume while it does.

## The idea

- **Squash**: on impact, the object gets shorter along the direction of travel and wider across it.
- **Stretch**: just before and after impact, at top speed, it gets longer along the direction of travel
  and narrower across it. Stretch also hides the gap between frames, like motion blur does.
- **Keep the volume**: if height goes to 75%, width goes to about 133%; scale X × scale Y stays near 1.
  A squash that only shrinks one axis reads as the object shrinking, not deforming.
- **Pivot at the contact point**: a ball squashes onto the floor, so the bottom edge stays put.
- The amount is a style decision: soft and rubbery for cartoon, barely there for UI and corporate.

## Rules of thumb

| Register | Squash at impact (X, Y) | Stretch in flight | Recover in |
|---|---|---|---|
| UI / corporate | 105%, 95% | none or 97%, 103% | 4–6 f |
| Product / social | 110–115%, 88–90% | 92%, 110% | 5–8 f |
| Cartoon | 120–130%, 70–80% | 85–90%, 112–120% | 6–10 f, one rebound |

- Peak squash is on the contact frame; stretch peaks 2–3 f before contact and 1–3 f after.
- Bounces lose height: each rebound about 40–60% of the previous one, each shorter in time.
- Squash on text: whole words only, small amounts (105/95). Per-letter squash looks broken.

## Measured in Carvercat

A 120 px ball fell from y 200 to a floor at y 930, with `transformOrigin` at `"50% 100%"` (its
bottom edge) and scale keys stretch `[0.9, 1.12]` at f19, squash `[1.25, 0.75]` at contact (f22),
`[0.95, 1.06]` at f25, rest at f28. Probe results:

| Frame | Width | Height | Bottom edge |
|---|---|---|---|
| 19 (stretch) | 108 px | 134 px | 725 |
| 22 (contact) | 150 px | 90 px | 930, exactly on the floor |
| 25 (recoil) | 114 px | 127 px | 758 |
| 28 (rest) | 120 px | 120 px | 654 |

- With `transformOrigin` on the bottom edge, the squash grows from the floor and the ball never sinks into it.
- The position fall used quad in (speeding up into the floor) and the rebound quad out (slowing at
  the top), which is what gravity does.
- `inspect lint` gives an info note `speed_jump` at the contact frame. That is correct: a bounce is a
  sudden change of speed.

## Do and don't

- Do keep area roughly constant (1.25 × 0.75 = 0.94).
- Do put the deformation on the axis of travel: a sideways slam squashes horizontally.
- Don't squash photos, logos with strict brand rules, or body text.
- Don't apply the same squash to every element; save it for the hero and for real contact.

## Checklist

- [ ] `transformOrigin` is on the contact edge before scaling.
- [ ] Peak squash sits exactly on the contact frame.
- [ ] scale X × scale Y stays between about 0.9 and 1.1.
- [ ] The rebound is lower and shorter than the fall.

## In Carvercat

- Curve names on this page (quad out, quad in) are `ease` strings: [names](easing-reference.md#names-used-in-this-wiki).
- Template examples with measured numbers and lint traps for this principle: [craft principle page](../../ai/references/craft/principles/squash-and-stretch.md).
- Properties: `scale` (a point `[x, y]`, keyframeable) and
  `transformOrigin` (CSS: `"50% 100%"` bottom edge, `"0% 50%"` left edge; old name `anchor` in half-sizes, `[0, -1]` and `[-1, 0]`). It is a pivot only: setting it does not move the object.
- Presets: `Squash land` (lands f8, settles f20) and `Jelly in` from the
  [Cartoon Bounce pack](../../ai/patterns/cartoon-bounce.md); `Drop - bounce` from
  [Motion Patterns](../../ai/patterns/README.md) (lands f9, f18, f22).
- Templates: `Bouncing ball` ([ct-bouncing-ball](../../ai/patterns/ct-bouncing-ball.md)) and
  `Boing title` ([ct-boing-title](../../ai/patterns/ct-boing-title.md)).
- Text: scale the whole text clip, or squash by word with a `stagger` on `anim.set` (`from: {scale: ...}`, `target: "words"`; old: `text.relative.scale` through Stagger Text).
- Check with `carvercat_inspect {mode:"probe", objects:"Ball"}`: width and height per frame show the
  squash; the bottom edge (`cy + h/2`) shows whether it stays on the floor.
- Lab: comp `W Squash` in [the principles lab](../labs/README.md).
