---
id: genres/explainers
title: Explainer videos
section: genres
tags: [explainer, how it works, voice-over, script, process, steps, icons, saas, education]
styles: [explainer, saas-ui, data-viz, corporate-brand]
topics: [genre, storytelling, voice-over]
related: [genres/infographics, genres/ui-ux-demos, genres/data-stories, techniques/line-drawing, sound-and-timing/reading-time, workflow/briefs]
verified: no (theory only)
source_inspiration: [https://b2w.tv/blog/explainer-video-script, https://commoncraft.com/explainer-tip-writing-explainer-video-script, https://typecast.ai/learn/?p=14931, https://www.b2w.tv/blog/how-to-make-infographics-videos]
---

# Explainer videos

An explainer makes one idea understandable in a minute or two: what a product does, how a process works,
why something matters. It is voice-over led, built from simple shapes, icons, UI and type, and judged by one
thing: did the viewer get it?

## The idea

- **Structure**: hook (the problem in one line) → problem (why it hurts) → solution (the product or idea) →
  how it works (3 steps, rarely more) → proof (a number, a customer) → one call to action.
- **The script is the film**: write it first, read it aloud, cut it until every sentence earns its place.
- **Show what is said, one idea per shot**: the visual illustrates the current sentence, never the previous
  or the next one.
- **Metaphor carefully**: one visual metaphor per film, introduced once and reused.

## Rules of thumb

| Length | Words of voice-over (about 130–150 a minute) | Steps |
|---|---|---|
| 30 s | 65–75 | 1–2 |
| 60 s | 130–150 | 3 |
| 90 s | 195–225 | 3–4 |

- Hook within 2 s; problem 10–20 s; solution and how-it-works most of the time; call to action 5–10 s.
- Under about 130 words a minute feels padded, over about 160 rushed.
- Visual changes every 3–5 s, in step with the narration.
- On-screen text supports the voice: keywords only, never the whole sentence.
- Calm, consistent motion: one easing family, a steady stagger, emphasis by colour or a small pulse.

## Do and don't

- Do make the steps visually parallel (same layout, same entrance) so the viewer sees "step 1, 2, 3".
- Do use a pointer, a line or a highlight to lead the eye through each step.
- Don't animate decoration while the narration explains something important.
- Don't put more than one new concept on screen at once.

## Checklist

- [ ] Script read aloud and timed; word count fits the length.
- [ ] Each sentence has one visual; each visual one idea.
- [ ] Steps share one layout and one entrance.
- [ ] Text holds pass `inspect lint` reading time.
- [ ] Muted viewing still tells the story (captions or keyword text).

## In Carvercat

No new measurements on this page; the building blocks below are verified in their own docs.

- Whole recipe: [explainer: how it works](../../ai/recipes/explainer-how-it-works.md) (25 s, assembled from
  Library templates, lint and qc checked).
- Pack: [Explainer](../../ai/patterns/explainer.md): `Step in`, `Emphasis pulse`, `Process steps`, `Icon grid`,
  `Pointer callout`, `Milestone timeline`.
- Training and compliance films: `Safety notice` (warning triangle, rule, scope and policy reference, signal amber;
  [cb-safety-notice](../../ai/patterns/cb-safety-notice.md)) from the Corporate Brand pack.
- Kids' and playful lessons (Cartoon Bounce round 3): `Lesson title card` (card lands with a squash, letters bounce in;
  [ct-lesson-title](../../ai/patterns/ct-lesson-title.md)), `Boing arrow` ("tap here" pointing at a button;
  [ct-boing-arrow](../../ai/patterns/ct-boing-arrow.md)), `Thought bubble` ([ct-thought-bubble](../../ai/patterns/ct-thought-bubble.md))
  and `Walk cycle (rigged)` for a mascot that walks in with planted feet ([ct-walk-cycle](../../ai/patterns/ct-walk-cycle.md)).
- Space and science explainers (Futuristic HUD round 3): `Orbit tracker` (a satellite runs round a turning wireframe
  planet and hides behind it; [fh-orbit-tracker](../../ai/patterns/fh-orbit-tracker.md)).
- Explainer round 3: `Cause and effect` (a chain that branches; [ex-cause-effect](../../ai/patterns/ex-cause-effect.md)),
  `Pros and cons` (two lists, a seesaw tips to the heavier side, a verdict; [ex-pros-cons](../../ai/patterns/ex-pros-cons.md)),
  `Labelled diagram` (leader lines to the parts of an object; [ex-labelled-diagram](../../ai/patterns/ex-labelled-diagram.md)),
  `Icon steps` (three cards with drawn icons; [ex-icon-steps](../../ai/patterns/ex-icon-steps.md)), `FAQ card` (one answer opens;
  [ex-faq-card](../../ai/patterns/ex-faq-card.md)), `Word definition` (with a speaker and a respelling;
  [ex-word-definition](../../ai/patterns/ex-word-definition.md)), `Tip carousel` ([ex-tip-carousel](../../ai/patterns/ex-tip-carousel.md))
  and `Problem and solution` ([ex-problem-solution](../../ai/patterns/ex-problem-solution.md)); all pass `contrast:true` at 4.5:1.
- Lines that connect steps: [line drawing](../techniques/line-drawing.md); staggered steps:
  [stagger systems](../techniques/stagger-systems.md).
- Voice-over to frames: `ai/scripts/motion/vo_align.py`; captions: [captions](../accessibility/captions.md).
