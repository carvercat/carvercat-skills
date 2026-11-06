---
id: workflow/lint-and-qc-audit
title: What every style trips on (lint and qc audit)
section: workflow
tags: [audit, lint, qc, contrast, freeze, black, showcases, recipes, review, styles]
styles: [all]
topics: [quality, review]
related: [workflow/review, design/contrast, principles/holds-and-stillness, accessibility/photosensitivity, design/visual-hierarchy]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html, https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html]
---

# What every style trips on (lint and qc audit)

All 13 round-2 showcase projects and all 16 recipe projects in the repository were opened headless and checked
with `carvercat_inspect` lint (with `contrast:true`) and qc: each master comp, and every template comp inside it
on its own. This page reports what came up, so you know which findings to expect in each style and which ones
are real problems.

## Summary

- **Master comps are clean**: 0 lint findings in all 29 projects, with contrast checking on. But the same
  templates linted on their own raised findings that the master did not report: lint on a master does not
  appear to check text inside nested instances, so a clean master is not the whole story.
- **Inside the templates** (211 template comps): 768 `repeated_key_value` and 150 `speed_jump` info notes,
  56 `low_contrast` findings (39 warnings, 17 errors), 3 `effect_clipped_by_frame` notes.
- **qc**: no flashes anywhere; 103 `freeze` findings (311.6 s in total) and 80 `black` findings (84.2 s).

## Per project

| Project | Template comps | Master lint | `repeated_key_value` (info) | `speed_jump` (info) | `low_contrast` in templates | of which dark text with no ground | qc `freeze` (count / s) | qc `black` (count / s) |
|---|---|---|---|---|---|---|---|---|
| ct-showcase-2 | 8 | 0 | 38 | 12 | 3 | 1 | 4 / 10.5 | 0 / 0.0 |
| cb-showcase-2 | 8 | 0 | 51 | 3 | 1 | 0 | 7 / 22.0 | 0 / 0.0 |
| dv-showcase-2 | 8 | 0 | 7 | 0 | 6 | 0 | 2 / 4.6 | 0 / 0.0 |
| ex-showcase-2 | 8 | 0 | 53 | 0 | 4 | 0 | 8 / 27.0 | 0 / 0.0 |
| fk-showcase-2 | 7 | 0 | 29 | 8 | 2 | 2 | 3 / 8.7 | 0 / 0.0 |
| fh-showcase-2 | 8 | 0 | 30 | 17 | 5 | 0 | 2 / 7.5 | 4 / 11.8 |
| gl-showcase-2 | 7 | 0 | 31 | 10 | 0 | 0 | 4 / 12.0 | 3 / 6.6 |
| kt-showcase-2 | 7 | 0 | 21 | 0 | 0 | 0 | 7 / 19.1 | 8 / 1.8 |
| ml-showcase-2 | 8 | 0 | 6 | 0 | 0 | 0 | 6 / 25.3 | 11 / 26.4 |
| rt-showcase-2 | 8 | 0 | 19 | 20 | 1 | 0 | 5 / 13.8 | 9 / 2.9 |
| saas-ui-showcase-2 | 7 | 0 | 62 | 3 | 3 | 0 | 4 / 11.4 | 0 / 0.0 |
| ss-showcase-2 | 8 | 0 | 30 | 1 | 1 | 0 | 5 / 16.0 | 9 / 2.1 |
| sp-showcase-2 | 7 | 0 | 65 | 0 | 0 | 0 | 5 / 15.4 | 0 / 0.0 |
| annual-report-opener | 8 | 0 | 35 | 6 | 1 | 0 | 6 / 15.6 | 0 / 0.0 |
| explainer-how-it-works | 6 | 0 | 36 | 0 | 7 | 3 | 5 / 13.9 | 1 / 0.2 |
| funky-sale-promo | 6 | 0 | 18 | 7 | 2 | 2 | 3 / 7.3 | 0 / 0.0 |
| glitch-music-teaser | 6 | 0 | 15 | 7 | 0 | 0 | 1 / 3.4 | 1 / 2.4 |
| hud-tech-trailer | 7 | 0 | 15 | 17 | 4 | 0 | 1 / 3.2 | 4 / 6.9 |
| kids-explainer | 8 | 0 | 23 | 9 | 3 | 0 | 3 / 6.9 | 0 / 0.0 |
| kinetic-quote-reel-9x16 | 6 | 0 | 8 | 1 | 0 | 0 | 1 / 3.3 | 7 / 1.6 |
| kinetic-quote-reel | 6 | 0 | 8 | 2 | 0 | 0 | 2 / 6.2 | 5 / 2.8 |
| luxury-product-teaser | 8 | 0 | 2 | 0 | 0 | 0 | 5 / 21.6 | 12 / 17.3 |
| quarterly-results-9x16 | 7 | 0 | 5 | 2 | 3 | 0 | 1 / 2.1 | 0 / 0.0 |
| quarterly-results | 8 | 0 | 9 | 1 | 3 | 0 | 3 / 7.1 | 1 / 0.3 |
| retro-night-promo | 5 | 0 | 5 | 12 | 0 | 0 | 1 / 2.2 | 3 / 0.9 |
| saas-feature-launch-30s | 11 | 0 | 75 | 5 | 3 | 0 | 4 / 10.7 | 0 / 0.0 |
| saas-launch-9x16 | 8 | 0 | 25 | 2 | 3 | 0 | 2 / 4.9 | 0 / 0.0 |
| sports-score-update | 6 | 0 | 25 | 3 | 1 | 0 | 2 / 6.7 | 0 / 0.0 |
| tip-reel-9x16 | 6 | 0 | 22 | 2 | 0 | 0 | 1 / 3.2 | 2 / 0.2 |

## What the findings mean, style by style

**Contrast (the one that matters).** Three kinds, by count of distinct template texts (37):

| Kind | Where | Typical measured ratio | Verdict |
|---|---|---|---|
| Muted secondary labels a little under 4.5:1 | Data Viz (timeline captions, comparison and gauge labels), Corporate (split-screen kicker, stat labels), SaaS (chart delta, modal label, CTA URL), Explainer (step text) | 2.9–4.3 | real: lighten the label or enlarge it to 34 px+ (then 3:1 applies) |
| Thin HUD text in dim cyan | Futuristic HUD (ID line, loader, signal, lock data, map ping) | 2.55–2.75 | real: the style's dim readouts fail on near-black |
| Light text on mid-tone fills | Cartoon (bouncy list, boing title), Explainer (cycle, Venn, compare columns), Retro (badge), Sports (replay word), Social (highlight caption word) | 1.2–2.9 | real where the text sits on a bright shape; check in context |
| Dark text in a template with no ground of its own | Funky (squiggle phrase, orbit "Follow"), Cartoon ribbon role, Explainer step titles | 1.07–1.14 | **artefact**: linted alone the template has a black ground; in the master it sits on a light background |

The rule from [contrast](../design/contrast.md) and [visual hierarchy](../design/visual-hierarchy.md) applies: lint
measures rendered ink, so a muted grey needs about 1.2–1.4× the nominal ratio to pass.

**Freeze (expected).** Every project had held moments of 2 s or more; qc calls them `freeze` even when a slow
push is running ([holds and stillness](../principles/holds-and-stillness.md)). Corporate, Explainer and Minimal
Luxury pieces had the most held time (22–27 s per showcase). Not an error; review that each hold is intentional.

**Black (expected in dark styles).** Minimal Luxury (26.4 s in its showcase, 17.3 s in the luxury teaser),
Futuristic HUD, Glitch, Retro night, Kinetic Typography and Social pieces on near-black grounds: qc's `black`
fires when 98% of the picture is under 4% luminance. Fine for those styles; a problem only for genuinely empty
frames.

**Info notes (ignore unless they surprise you).** `repeated_key_value` ("opacity holds 1.0 between two keys")
is how templates hold values between moves; `speed_jump` marks moves that start or stop abruptly, which
stepped styles (Retro on twos, HUD flicker, Glitch, Cartoon squash) do on purpose. `effect_clipped_by_frame`
appeared on two full-width beams and a toast's shadow at the frame edge.

## Do and don't

- Do lint each template comp, not only the master; the master did not report nested-text findings.
- Do treat dark-text-on-black findings in ground-less templates as artefacts after checking the master look.
- Don't ship HUD readouts or muted chart labels without checking contrast; they were the most common real failures.
- Don't read qc `freeze` and `black` as errors in calm or dark styles.

## Checklist

- [ ] Every template comp linted with `contrast:true`.
- [ ] Real contrast findings fixed (lighter, larger, or a plate).
- [ ] qc: no flashes; freezes and black stretches all intentional.

## In Carvercat

- Per comp: `comp.switch` to each template comp, then `carvercat_inspect {mode:"lint", contrast:true}`; for the
  whole film `carvercat_inspect {mode:"qc"}` on the master.
- The projects audited: `categories/*/*-showcase-2/` and `categories/recipes/*/` (copies were opened, the
  repository files were not modified). Recipes: [ai/recipes](../../ai/recipes/README.md); style review lists:
  [review by style](../../ai/references/craft/review-by-style.md).
