---
id: cookbook/map-pin-drop
title: Drop a map pin onto a spot
section: cookbook
tags: [map pin, pin drop, location, marker, bounce, ping, ripple, rig, null, travel]
styles: [cartoon-bounce, explainer, saas-ui, social-short-form]
topics: [rigging, shapes]
related: [principles/squash-and-stretch, principles/weight, cookbook/ripple, cookbook/pop-in]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Map_pin, https://en.wikipedia.org/wiki/Squash_and_stretch]
---

# Drop a map pin onto a spot

**Goal.** A location pin falls onto a point on a map, bounces, settles with its tip exactly on the spot, and
a ring pings out from where it landed.

## Steps

1. Build the pin from native shapes: a red ellipse head (100 px), a closed 3-point path for the point (tip at
   the spot) and a small white dot. Its parts start on the drop frame.
2. Add a **null at the tip** (an invisible ellipse) as the pin's rig. Parent the head, point and dot to it:
   `select.clip` each part, `select.add` the null **last**, `parent.assign`.
   **Do this at a frame where the null is at rest** (see the traps).
3. Apply **`Drop - bounce`** to the null (`preset.apply {name, id}`). It keys the null's position from
   0.28 of the frame height above and bounces three times in 24 f, and fades it in.
4. A shadow ellipse (80 × 20 px, black at 28%) on the ground, not parented: key its scale small → full on
   the contact frames (here f19, f28) and slightly smaller on the rebound (f23).
5. A ring (180 × 60 px, 4 px stroke, no fill) on its own clip starting on the first contact frame, 18 f
   long, with **`Tap ripple`**.

## Measured in Carvercat 0.1.6

Comp `K Pin drop` in [cookbook lab 5](../labs/README.md#cookbook-lab-5carverproj): rig clip from f10, tip
at (960, 540); `inspect probe` on the rig:

| Frame | 10 | 19 | 23 | 28 | 30 | 34 → |
|---|---|---|---|---|---|---|
| Tip y (px) | 237.6 | 530.8 | 464.4 | 531.7 | 521.6 | 540.0 |
| | start, 302.4 px up | first contact | rebound peak | second contact | last hop | at rest |

- The preset's start offset is 0.28 × 1080 = **302.4 px**. First contact lands **9 f** after the clip
  starts and stops 9 px short (its keys are baked); the pin is still from **f34**.
- The parented head followed exactly: 127.6 at f10, 430.0 at rest (110 px above the tip, as drawn).
- `Tap ripple` from f19: ring 45 → 180 px wide (0.25 → 1), opacity 0.7 held to f22, 0.35 at f24, gone by
  f35.
- Rendered at f40: (960, 536) is pin red (229, 88, 77); 10 px lower is ground.
- `inspect lint`: 1 error (`never_visible` on the null, see FR-041), 0 warnings, 7 notes (`speed_jump`
  27.1 → 6.7 px/frame at the first contact; repeated keys).

## Traps

- `parent.assign` keeps each child where it is **on the current frame**, so it bakes in the parent's offset
  at the playhead. Parented after the preset at f0 (rig 302.4 px up), the pin came to rest **302.4 px below**
  its spot: [KI-153](../../ai/references/known-issues.md#ki-153). Parent first, or at a rest frame.
- The null is reported as the error `never_visible`: [FR-041](../../ai/references/known-issues.md#fr-041).
- The last-selected object becomes the parent on 0.1.6: [KI-120](../../ai/references/known-issues.md#ki-120).

## In Carvercat

- Library: `Pin` (sticker), `Map ping` ([fh-map-ping](../../ai/patterns/fh-map-ping.md)), `Drop - bounce`,
  `Tap ripple`, `Location` (text).
- Background: [squash and stretch](../principles/squash-and-stretch.md), [weight](../principles/weight.md),
  [ripple](ripple.md).
