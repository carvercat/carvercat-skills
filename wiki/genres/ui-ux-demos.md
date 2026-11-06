---
id: genres/ui-ux-demos
title: UI and UX demo videos
section: genres
tags: [ui demo, product demo, screen recording, cursor, zoom, saas, app, walkthrough, mock ui]
styles: [saas-ui, explainer, corporate-brand, glitch]
topics: [genre, ui, product]
related: [genres/product-launches, genres/explainers, techniques/camera-moves-2d, techniques/masking, design/visual-flow]
verified: no (theory only)
source_inspiration: [https://screen.studio/guide/animations-motion, https://www.tella.com/blog/animated-cursors-for-screen-recordings, https://trainn.co/answers/how-to-add-zoom-effects-to-product-demo-videos/, https://carbondesignsystem.com/elements/motion/overview/]
---

# UI and UX demo videos

A UI demo shows software doing its job: a cursor clicks, a panel opens, a result appears. It is the
workhorse of SaaS marketing and onboarding. Good demos are not screen recordings; they are designed
reconstructions where every action is deliberate and the camera always shows the part that matters.

## The idea

- **Rebuild, don't record**: a clean mock UI (simplified, on brand, with realistic but private-safe data)
  animates better than a capture, can be re-timed, and never shows a stray notification.
- **One action per beat**: cursor moves, clicks, the interface responds, the benefit appears as a short line.
- **The camera follows the action**: zoom to the field being used, then pull back to show context.
- **Interface motion stays interface-like**: panels and menus use crisp, short UI timings (150–300 ms,
  standard curves); the "film" moves (camera, titles) use slower ones.
- **The cursor is a character**: smooth, purposeful paths with an ease, a click with a visible response,
  never idle wandering.

## Rules of thumb

- Feature beat 3–5 s: about 1 s for the cursor travel and click, 1 s for the response, 1–2 s to read the
  benefit.
- Cursor travel on an arc, easing in and out, 12–24 f; click press 3–4 f with a ripple.
- Zooms to 130–200% on the active area; hold during the interaction; never zoom while the viewer reads.
- Simplify the UI: remove menus and data the story does not need; enlarge text that must be read.

## Do and don't

- Do script every click and every value typed.
- Do use realistic but fictional data; no real customer names or personal data.
- Don't record at a small window size and scale up (blurry text).
- Don't let the cursor drift while nothing happens.

## Checklist

- [ ] Each beat: one action, one response, one benefit line.
- [ ] Cursor paths deliberate and eased; clicks visible.
- [ ] Zooms frame the active area and hold during it.
- [ ] Text inside the UI readable at delivery size.

## In Carvercat

No new measurements on this page; the templates below are verified in their pack.

- Pack: [SaaS UI](../../ai/patterns/saas-ui.md): `Cursor click`, `Notification toast`, `Toggle switch`,
  `KPI tile`, `Sidebar drawer`, `Modal over app`, `Chart card`, `Chat thread`, `Dropdown menu`, rolling counter
  and search typing recipes.
- A broken-page moment: `Error 404 page` (glitching 404, a GO HOME button, a cursor that glides in and clicks;
  [gl-error-404](../../ai/patterns/gl-error-404.md)), Glitch round 3.
- Help and onboarding screens (Explainer round 3): `FAQ card` (a question row opens like an accordion and the rows below make room;
  [ex-faq-card](../../ai/patterns/ex-faq-card.md)), `Icon steps` ([ex-icon-steps](../../ai/patterns/ex-icon-steps.md)) and
  `Labelled diagram` for annotating a screen or device ([ex-labelled-diagram](../../ai/patterns/ex-labelled-diagram.md)).
- Recreating real UI pieces (pointer, switch): [shapes §UI](../../ai/references/drawing/shapes.md).
- Camera zooms on the UI: [camera moves in 2D](../techniques/camera-moves-2d.md); typing text:
  [su-search-typing](../../ai/patterns/su-search-typing.md).
- Sci-fi interfaces (Futuristic HUD round 3): `Voice waveform` (an assistant listens, the line types on;
  [fh-voice-waveform](../../ai/patterns/fh-voice-waveform.md)), `Boot sequence` (log lines with OKs and a progress bar;
  [fh-boot-sequence](../../ai/patterns/fh-boot-sequence.md)) and `Drone telemetry`, a full-frame overlay for footage
  ([fh-telemetry](../../ai/patterns/fh-telemetry.md)).
- Recipe: [SaaS feature launch, 30 s](../../ai/recipes/saas-feature-launch-30s.md).
