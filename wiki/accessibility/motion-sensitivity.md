---
id: accessibility/motion-sensitivity
title: Motion sensitivity (vestibular)
section: accessibility
tags: [vestibular, motion sickness, reduced motion, parallax, zoom, spin, accessibility, comfort]
styles: [all]
topics: [accessibility, comfort]
related: [accessibility/photosensitivity, techniques/parallax, techniques/camera-moves-2d, accessibility/readability]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html, https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html, https://www.a11yproject.com/posts/understanding-vestibular-disorders/, https://alistapart.com/article/designing-safer-web-animati, https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion, https://primer.style/accessibility/design-guidance/motion-and-animation]
---

# Motion sensitivity (vestibular)

For people with vestibular disorders (a large share of adults over 40 report some episode) certain motion
causes dizziness, nausea or headaches. The triggers are mostly the "cinematic" moves: big zooms, spins,
parallax, whole-frame movement. Comfortable motion is better motion for everyone.

## The idea

- **Triggers**: scaling and zooming of large areas, spinning, parallax with mismatched speeds, motion that
  fills the field of view, long travel, bouncing and shaking, motion the viewer did not expect.
- **Relative size matters**: a small icon spinning is fine; the whole frame spinning is not.
- **Colour, opacity and blur changes** that do not imply movement are generally comfortable alternatives.
- In interfaces, users can ask for reduced motion; in video they cannot. So video must be comfortable by
  default, or provide a calmer cut.

## Rules of thumb

- Full-frame zooms: keep scale changes under about 20% per second and avoid continuous zoom loops.
- Rotation of the whole frame: a few degrees at most; never continuous spins.
- Parallax: two or three planes, gentle speeds, under about 1.5 s per full-screen shift.
- Shakes: under 12 px, under 10 f, and rare.
- Ambient loops longer than 5 s next to content to be read: keep them very slow or stoppable (players,
  kiosks, websites).
- Offer a reduced-motion version for web and kiosk use: crossfades instead of zooms and pans.

## Measured in Carvercat: no automatic check

Six tiles parented to a camera null that zoomed 1 → 3 in 10 f, back, and again, while spinning two full turns
in 40 f (a deliberately sickening move; probe showed a tile growing 200 → 600 px wide in 10 f and turning 90°
every 5 f). `carvercat_inspect {mode:"lint"}` reported only `speed_jump` info notes (and `never_visible` for the
null); `carvercat_inspect {mode:"qc"}` reported nothing. Neither check measures motion intensity, so comfort
has to be judged against the rules of thumb above: read zoom and rotation rates from `inspect probe` and
compare.

## Do and don't

- Do prefer cuts or crossfades to whip pans and zoom-throughs for long-form content.
- Do warn before intense sequences in long pieces (events, games trailers).
- Don't loop a full-screen moving background behind body text.
- Don't stack zoom, spin and shake in one transition.

## Checklist

- [ ] No continuous full-frame zoom, spin or shake.
- [ ] Parallax and camera moves are gentle and short.
- [ ] A reduced-motion version exists where the medium allows (web, apps, kiosks).
- [ ] Ambient motion behind text is slow.

## In Carvercat

- Measure how much a camera move scales or travels per second: `carvercat_inspect {mode:"probe", objects:"Camera"}`
  ([camera moves](../techniques/camera-moves-2d.md)); parallax speeds per plane ([parallax](../techniques/parallax.md)).
- Lab: comp `M Intense` in [the measurement lab 4](../labs/README.md).
- Make a reduced-motion cut: duplicate the comp (`comp.duplicate`), replace zoom and pan keys with
  opacity crossfades, and export it as a second deliverable.
- Calm alternatives in the packs: `Slow fade in`, `Drift up - 4 s` ([Minimal Luxury](../../ai/patterns/minimal-luxury.md)),
  `Soft rise` ([Corporate Brand](../../ai/patterns/corporate-brand.md)), `Dip to colour` ([Transitions](../../ai/patterns/transitions.md)).
