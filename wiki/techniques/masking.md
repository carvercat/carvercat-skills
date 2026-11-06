---
id: techniques/masking
title: Masking and reveals
section: techniques
tags: [mask, matte, track matte, reveal, wipe, window, slide behind, invert]
styles: [all]
topics: [reveal, compositing]
related: [techniques/kinetic-type, techniques/line-drawing, techniques/match-cuts, principles/staging, genres/title-sequences]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://helpx.adobe.com/uk/after-effects/desktop/work-with-transparency-and-compositing/work-with-track-mattes-and-traveling-mattes/track-mattes-and-traveling-mattes.html, https://blog.motionarray.com/learn/after-effects/after-effects-track-mattes/, https://uxmag.com/articles/creating-usability-with-motion-the-ux-in-motion-manifesto]
---

# Masking and reveals

A mask decides where another object may be seen. Animated masks are behind most "classy" reveals: text
rising out of a line, a photo wiped on by a bar, a word appearing inside a shape, a logo emerging from
behind an edge. The object can move inside a still window, or the window can move over a still object.

## The idea

- **Moving window, still content**: a wipe. The edge of the window is the motion; the content stays put.
- **Still window, moving content**: a slide from behind an edge. The content travels into view while its
  edge stays crisp and fixed.
- **Both move**: the window grows while the content counter-slides; the most elegant and the busiest.
- A mask edge reads as a physical edge. Give the eye a reason for it: a rule line, a card edge, a frame.
- Invert a mask to cut a hole (text knocked out of a plate).

## Rules of thumb

- Slide-behind distance: about the content's own height (a 72 px line rises about 100–110 px).
- Window wipes: 14–20 f with a strong ease out; the content should be fully revealed by about 40% of
  the move so the eye is not chasing it.
- Draw a visible edge (a 2–4 px rule) where content emerges; an invisible edge reads as a glitch.
- Mask once per element; nested masks are hard to revise.

## Measured in Carvercat

Two masks in one comp, checked with `carvercat_inspect mode:composite` (actual pixel contribution, masks
included) and `carvercat_look`:

| Reveal | Setup | Visible from | Fully revealed |
|---|---|---|---|
| Wipe | 96 px text; window rectangle 1000 × 160 with `transformOrigin` `"0% 50%"`, `scale` `[0, 1]` → `[1, 1]` over f10–f28 (expo out, `cubic-bezier(0.16, 1, 0.3, 1)`) | f12 | by f16, 6 f into an 18 f wipe |
| Rise | 72 px text rising 110 px over f14–f32 (expo out) into a still 1100 × 110 window above a 4 px rule | f16 | about f24 |

The text inside the wipe was narrower than the window, so it was complete long before the window
stopped growing: size the window to the content, or the second half of the wipe animates nothing.

`inspect lint` does not see masks: it may report hidden parts as cropped or overlapping
([KI-133](../../ai/references/known-issues.md#ki-133)). Use `mode:composite` and `carvercat_look` to judge
masked work.

## Do and don't

- Do put `transformOrigin` of a growing window on the edge it grows from (`"0% 50%"` for a left edge).
- Do give the emerging edge a rule, a plate or a frame.
- Don't mask text that the viewer must read while it is still being revealed.
- Don't trust lint's crop and overlap findings on masked objects.

## Checklist

- [ ] Window size matches the content (no dead half of the wipe).
- [ ] The emerging edge is motivated by something visible.
- [ ] `mode:composite` shows the content contributing from the frame you planned.
- [ ] `carvercat_look` at the start, middle and end of the reveal looks clean.

## In Carvercat

- Curve names on this page (expo out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Make a mask over MCP: on the object to cut, `property.set {id: "<content>", key: "mask", value: "<window>"}` (the
  window must be on another track; `{ref: "<window>", invert: true}` cuts a hole). The window is parented to the content,
  so `parent.clear {ids: ["<window>"]}` if it should not follow it; the mask stays. `clipPath` (`"inset(0 10% 0 0)"`,
  `circle(100px at 50% 50%)`, `ellipse()`, `polygon()`) makes the window for you. Read it back with `property.get`
  `mask`. Old way, accepted for one release: `mask.make {ids:[window, content]}`: the **first id is the mask**.
- The window is any shape; it can carry its own keys (`scale`, `x`) and a `feather` in px for a soft-edged wipe
  ([soft edge and feather](soft-edge-and-feather.md); `feather` is exact in Resolve, approximate in After Effects).
- Ready-made masked reveals: `Title card - split rule` ([cb-title-card](../../ai/patterns/cb-title-card.md)),
  `Line reveal` ([kt-line-reveal](../../ai/patterns/kt-line-reveal.md)), `Feather wipe reveal`
  ([ml-feather-wipe](../../ai/patterns/ml-feather-wipe.md)), `Slice shift` ([gl-slice-shift](../../ai/patterns/gl-slice-shift.md)),
  `Area chart` ([dv-area-chart](../../ai/patterns/dv-area-chart.md)), rolling counters
  ([su-rolling-counter](../../ai/patterns/su-rolling-counter.md)).
- Masks, blend modes and wipes in depth: [compositing and masks](../../ai/references/effects/compositing-and-masks.md).
- Lab: comp `T Masking` in [the techniques lab](../labs/README.md).
