---
id: design/contrast
title: Contrast and legibility
section: design
tags: [contrast, wcag, legibility, luminance, ratio, text over video, scrim, plate, accessibility]
styles: [all]
topics: [colour, text, accessibility]
related: [accessibility/readability, design/visual-hierarchy, design/colour-psychology, principles/staging, accessibility/photosensitivity]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html, https://www.nngroup.com/articles/principles-visual-design/, https://www.schoolofmotion.com/blog/color-theory-after-effects]
---

# Contrast and legibility

Contrast is the difference that lets the eye separate one thing from another: light against dark, big
against small, busy against calm. For text it is not a matter of taste: below a certain luminance ratio a
large share of viewers cannot read it, on a phone in daylight almost nobody can.

## The idea

- **Luminance contrast** decides legibility. Hue contrast alone (red on green, blue on purple) is not enough.
- The web accessibility rule of thumb carries over to video: at least **4.5:1** for normal text and **3:1**
  for large text; 7:1 is the comfortable target over moving pictures.
- **Value check**: view the frame in greyscale. If the focal element does not stand out in grey, colour
  will not save it.
- Over footage, contrast changes every frame. Use a scrim (a dark gradient), a plate (a solid box behind the
  text), an outline or a soft shadow.
- Contrast is also a hierarchy tool for shapes; don't use low contrast to "de-emphasise" text that must be read.

## Rules of thumb

| Situation | Minimum | Target |
|---|---|---|
| Body text, captions, labels | 4.5:1 | 7:1 |
| Large display text | 3:1 | 4.5:1 |
| Text over footage | 4.5:1 at its worst frame | a plate or scrim at 50–70% black |
| Non-text graphics that carry meaning (chart lines, icons) | 3:1 against neighbours | — |

- Keep one high-contrast accent; everything else steps down in value.
- Thin, light weights need more contrast than bold weights at the same colour.

## Measured in Carvercat

`carvercat_inspect {mode:"lint", contrast:true}` renders the frame and measures the **ink** of each text
against what is behind it. Grey text on black, Rethink Sans, at many sizes:

| Finding | Result |
|---|---|
| Size where lint switches from 4.5:1 to 3:1 ("large text") | **34 px** font size and up, Regular and Bold alike |
| Severity | `error` when far below (2.08 vs 4.5 wanted), `warning` when close (3.12 or 3.93 vs 4.5; 2.08 vs 3.0) |
| Measured ratio vs the colour's nominal ratio | lower: #767676 on black is 4.6:1 on paper but measured 3.12:1 as 24 px Bold text; #595959 (3.0:1 nominal) measured 2.08–2.37:1 |
| Regular text under 34 px | **not checked**: #595959 Regular at 24–32 px got no finding at all, while the same colour in Bold was an error ([KI-142](../../ai/references/known-issues.md#ki-142)) |

Because lint averages the anti-aliased ink, its ratios are stricter than the nominal colour ratio: aim for
nominal 7:1 and lint will pass. And because thin Regular text under 34 px is skipped, check small captions
by colour yourself (ratio of the two hex colours) until [KI-142](../../ai/references/known-issues.md#ki-142) is fixed.

## Do and don't

- Do pick text colours from a palette where every text/background pair is at least 4.5:1 nominal.
- Do put a plate or scrim under text over footage, and check the busiest frame.
- Don't rely on colour alone to separate meaning (red vs green bars need labels or shapes too).
- Don't use pure white on pure black for long reads in a dark room; off-white on near-black is calmer.

## Checklist

- [ ] `inspect lint contrast:true` shows no `low_contrast` findings.
- [ ] Small Regular captions checked by hand ([KI-142](../../ai/references/known-issues.md#ki-142)).
- [ ] Text over footage checked at its worst frame.
- [ ] A greyscale look still shows the focal point.

## In Carvercat

- Lint: `carvercat_inspect {mode:"lint", contrast:true}`; the finding reports `ratio`, `wanted`, the text
  and background luminance and the frame.
- Plates: a rectangle behind the text, `opacity` 0.5–0.8; scrims: a rectangle with `fill: "linear-gradient(180deg, #00000000 0%, #000000b3 100%)"`
  (transparent to 70% black; [fill and gradients](../../ai/references/effects/fill-and-gradients.md); old names: `shape.fill.opacity`, a linear `shape.fill.paint` gradient).
- Outlines and shadows on text: `stroke` (the outline colour; thickness `text.outline.thickness` has no design name yet) and `dropShadow`
  (old: the `shadow` effect; [text paint](../../ai/references/effects/text-paint.md), [shadow](../../ai/references/effects/shadow.md)).
- CSS colour strings are decoded for you; only a raw colour array is linear light ([colour psychology](colour-psychology.md#in-carvercat)). `measure.contrast` (WCAG ratio and AA/AAA verdicts on two displayed colours, no render) checks a pair before you build it.
- Palette roles and contrast pairs: [colour craft](../../ai/references/craft/colour.md).
- Lab: comp `C Contrast` in [the accessibility lab](../labs/README.md).
