---
id: sound-and-timing/duration-tokens
title: Duration tokens in frames
section: sound-and-timing
tags: [duration, tokens, milliseconds, frames, design system, conversion, ladder]
styles: [saas-ui, corporate-brand, explainer, data-viz]
topics: [timing, reference]
related: [principles/timing-and-spacing, sound-and-timing/frame-rates, principles/easing-reference, history/flat-design-and-ui-motion]
verified: no (theory only)
source_inspiration: [https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md, https://carbondesignsystem.com/elements/motion/overview/, https://www.nngroup.com/articles/animation-duration/, https://learn.microsoft.com/en-us/windows/apps/design/motion/timing-and-easing, https://atlassian.design/foundations/motion]
---

# Duration tokens in frames

Interface design systems publish durations in milliseconds; motion work happens in frames. This page converts
the common durations, so UI motion recreated in video matches the product it shows, and explains how to adapt
them for a film.

## The idea

- Design-system durations are tuned for interactions seen many times a day: short and subtle.
- A product video recreating the UI should use the product's own durations for UI parts (toasts, menus,
  toggles), so it feels like the real thing.
- The video's own moves (titles, camera, transitions) use video timing, usually longer
  ([timing and spacing](../principles/timing-and-spacing.md)).

## Conversion

frames = milliseconds × fps ÷ 1000, rounded to a whole frame.

| Token or use | ms | 24 fps | 25 fps | 30 fps | 60 fps |
|---|---|---|---|---|---|
| Micro feedback (toggle, press) | 100 | 2.4 f | 2.5 f | 3 f | 6 f |
| Carbon fast-02 | 110 | 2.6 f | 2.8 f | 3.3 f | 6.6 f |
| Small UI change | 150 | 3.6 f | 3.8 f | 4.5 f | 9 f |
| Carbon moderate-02 | 240 | 5.8 f | 6 f | 7.2 f | 14.4 f |
| Material medium (standard) | 300 | 7.2 f | 7.5 f | 9 f | 18 f |
| Modal / panel | 250 | 6 f | 6.2 f | 7.5 f | 15 f |
| Large move on big screens | 400 | 9.6 f | 10 f | 12 f | 24 f |
| Material long | 500 | 12 f | 12.5 f | 15 f | 30 f |
| Carbon slow-02 (background dim) | 700 | 16.8 f | 17.5 f | 21 f | 42 f |
| Material extra-long max | 1000 | 24 f | 25 f | 30 f | 60 f |

- Round to whole frames; at 24 and 25 fps several tokens collapse to the same frame count.
- Exits are commonly about 70–85% of the matching entrance.
- Stagger offsets of 20 ms per row (common in tables) are below one frame at 30 fps: in video use 1–2 f.

## Do and don't

- Do copy the product's real durations and curves for UI recreations.
- Do convert at the comp's actual frame rate.
- Don't use UI durations for full-frame transitions or titles; they will feel abrupt in a film.

## Checklist

- [ ] UI parts use product durations converted at the comp's rate.
- [ ] Film-level moves use the film's own duration ladder.

## In Carvercat

This page is arithmetic and design guidance; no Carvercat behaviour on it was measured. Keys and clips are in
frames at the comp's rate ([frame rates](frame-rates.md)); curves for these systems, measured in Carvercat, are in
[the easing reference](../principles/easing-reference.md).
