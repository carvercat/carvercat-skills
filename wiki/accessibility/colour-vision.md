---
id: accessibility/colour-vision
title: Colour vision deficiency
section: accessibility
tags: [colour blindness, color blind, deuteranopia, protanopia, tritanopia, palette, red green, redundancy]
styles: [all]
topics: [accessibility, colour]
related: [design/contrast, design/colour-psychology, genres/data-stories, design/colour-transitions]
verified: no (theory only)
source_inspiration: [https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html, https://en.wikipedia.org/wiki/Color_psychology, https://advids.co/insights/visualizing-data-accurately-best-practices-for-graphs-charts-and-infographics-in-motion]
---

# Colour vision deficiency

A noticeable share of viewers, mostly men, see colour differently: most commonly they confuse reds and
greens, more rarely blues and yellows. Graphics that use colour alone to carry meaning (red bad, green good;
one line red, the other green) fail for them. The fix is cheap: never let colour be the only signal.

## The idea

- **Redundancy**: pair colour with a second cue: a label, a shape, a pattern, a position, an icon, or
  motion.
- **Luminance difference**: two colours that differ clearly in lightness stay distinguishable for nearly
  everyone; hue-only differences do not.
- **Safe pairs**: blue with orange, blue with red, dark with light versions of one hue. Risky pairs: red with
  green, green with brown, blue with purple.
- **Motion helps**: highlighting one bar by moving or pulsing it works regardless of colour vision.

## Rules of thumb

- Charts: label lines directly at their ends instead of a colour legend; highlight with colour **and** weight.
- Status: positive/negative with icons or signs (+/−, arrows) as well as colour.
- Check the palette in greyscale: if two meaningful colours look the same grey, change one's lightness.
- Keep the accent colour also the highest-contrast element, so it stands out without hue.

## Do and don't

- Do test key frames in greyscale and with a colour-blindness simulator.
- Do use blue/orange for two-series comparisons.
- Don't use red versus green as the only difference.
- Don't encode categories in more than about six colours.

## Checklist

- [ ] No meaning carried by hue alone.
- [ ] Meaningful colours differ in lightness as well as hue.
- [ ] Charts labelled directly.

## In Carvercat

No measurements on this page.

- Greyscale check: the colour effect has only `brightness` (old `Gain`) and `contrast`, no saturation control (`saturate`, `grayscale`, `sepia` and `hue-rotate` are refused with the reason), so review
  exported frames in an external viewer's greyscale mode, or compare luminance values: lint's contrast check
  reports text and background luminance ([contrast](../design/contrast.md)).
- Direct labels and highlights in charts: [Data Viz pack](../../ai/patterns/data-viz.md); motion highlights:
  `Emphasis pulse` ([Explainer](../../ai/patterns/explainer.md)).
