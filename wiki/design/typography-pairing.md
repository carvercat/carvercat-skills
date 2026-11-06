---
id: design/typography-pairing
title: Typography pairing
section: design
tags: [typography, fonts, typeface, pairing, x-height, serif, sans, weight, superfamily]
styles: [all]
topics: [text, typography]
related: [design/visual-hierarchy, techniques/kinetic-type, design/contrast, accessibility/readability]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://blog.typekit.com/2012/05/23/type-study-pairing-typefaces/, https://fonts.google.com/knowledge/choosing_type/pairing_typefaces_within_a_family_superfamily, https://www.fontshop.com/content/how-to-mix-type, https://adobe.design/ideas/three-secrets-to-font-pairing]
---

# Typography pairing

Most motion pieces need one typeface, sometimes two. A good pair contrasts clearly on one or two axes
(serif vs sans, weight, width) while sharing structure (similar x-height and proportions), and each face has
one job.

## The idea

- **One family first**: a family with several weights covers headline, body and caption. Superfamilies
  (a serif and a sans built on one skeleton) are the safest pairs.
- **Contrast, don't compete**: two near-identical sans faces look like a mistake. Pair a geometric display
  with a neutral text face, or a sharp serif headline with a plain sans body.
- **Match x-heights**: lowercase size drives perceived size. Faces with very different x-heights look
  mismatched at the same point size.
- **Roles**: display (headlines, hero words), text (supporting lines), utility (numbers, labels, code).
- **Motion favours sturdy faces**: thin hairlines shimmer when scaled or blurred; open counters and clear
  shapes survive compression and small screens.

## Rules of thumb

- At most two families per film; three weights per family.
- Headline-to-support size ratio about 2:1; caption at least 28 px at 1920 wide.
- Avoid hairline weights below about 60 px; avoid high-contrast serifs (Didone) for small text.
- Tracking: tighten big display type slightly, loosen small caps.

## Measured in Carvercat: same Size, different faces

Each face set at the same nominal size (100 px em), measured with `carvercat_authoring {mode:"geometry"}`
(ink bounds). All resolved exactly (`font_exact` passed) on the test Mac:

| Face (style) | Cap height | x-height | x / cap | "Motion design" at 60 px |
|---|---|---|---|---|
| Rethink Sans (Regular) | 70.0 px | 49.6 px | 0.71 | 377 px |
| Avenir Next (Regular) | 69.5 | 48.9 | 0.70 | 407 |
| Arial (Regular) | 85.9 | 62.2 | 0.72 | 438 |
| Verdana (Normal) | 80.2 | 60.1 | 0.75 | 450 |
| Georgia (Normal) | 81.7 | 56.8 | 0.69 | 447 |
| Times New Roman (Regular) | 80.1 | 54.1 | 0.68 | 420 |
| Palatino (Regular) | 84.5 | 57.4 | 0.68 | 468 |
| Baskerville (Regular) | 77.6 | 46.8 | 0.60 | 404 |
| Bodoni 72 (Book) | 77.6 | 48.9 | 0.63 | 360 |
| Courier New (Regular) | 67.6 | 50.0 | 0.74 | 549 |

- The same `fontSize` gives visibly different sizes: Arial's caps are 23% taller than Rethink Sans's.
  When you swap or pair faces, match **x-heights** by adjusting size (Rethink Sans 100 ≈ Arial 80 by
  x-height), not by keeping the number.
- Old-style serifs (Baskerville 0.60, Bodoni 0.63) have small x-heights: they read smaller and need more
  size or space in motion.
- Widths differ by up to 50% (Bodoni 360 px vs Courier 549 px for the same words): re-measure line breaks
  after any font change.

## Do and don't

- Do confirm the face resolves before building (`font_exact`), especially on another machine.
- Do pair on structure: similar x-height ratio, different classification.
- Don't swap fonts late without re-measuring every line.
- Don't use system fonts you cannot ship with the project; packs use Rethink Sans, which must be installed
  ([KI-136](../../ai/references/known-issues.md#ki-136)).

## Checklist

- [ ] One or two families, each with a role.
- [ ] x-heights matched by size, not by number.
- [ ] `carvercat_authoring {mode:"validate", checks:[{type:"font_exact", id}]}` passes for every text.
- [ ] Line widths re-measured after any face change.

## In Carvercat

- Keys: `fontFamily`, `fontWeight`, `fontStyle`, `fontSize` (px, a true em: the ink of an "H" is the face's cap height times it in every family), `letterSpacing`, `lineHeight`. Old: `text.font.family` (Font), `text.font.style` (Style, the exact style name the system reports,
  which can be localised), `text.font.size`, `text.font.tracking`, `text.font.lineSpacing`.
- List installed faces and styles: `carvercat_authoring {mode:"fonts"}`; check one: `font_exact`.
- Measured tracking, leading and lint size rules for Rethink Sans: [typography craft](../../ai/references/craft/typography.md).
- Arabic and mixed scripts: [RTL and Arabic](../../ai/references/workflows/rtl-and-arabic.md).
- Lab: comp `D Fonts` in [the accessibility lab](../labs/README.md).
