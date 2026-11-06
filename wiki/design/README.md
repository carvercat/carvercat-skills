# Design fundamentals

Motion is design that changes over time: every frame still has to work as a composition. These pages cover
the still-frame foundations and how motion changes them.

| Page | One line | Measured in Carvercat |
|---|---|---|
| [Visual hierarchy](visual-hierarchy.md) | What is noticed first, second, third | on #101418, support text passes lint from #6B7480, labels from #8C96A6 |
| [Grids, safe areas and layout](grids-and-layout.md) | Margins, columns, thirds, safe zones | lint safe box `[96, 54, 1824, 1026]`; `look` grid overlay is 6 × 6 |
| [Colour psychology and palettes](colour-psychology.md) | Meanings, roles, 60-30-10 | colours are linear; the renderer uses BT.709 (#808080 via the sRGB curve renders 115) |
| [Contrast and legibility](contrast.md) | Luminance ratios for text | lint's large-text switch at 34 px; it measures rendered ink |
| [Typography pairing](typography-pairing.md) | Choosing and matching faces | x-height and cap height of 10 faces at the same size |
| [Negative space](negative-space.md) | Space as a design element | theory |
| [Gestalt principles in motion](gestalt.md) | Grouping, common fate, closure | theory |
| [Visual flow and eye path](visual-flow.md) | Where the eye goes, across cuts | theory |
| [Colour transitions](colour-transitions.md) | What happens between two colours | blue → yellow passes through grey (180, 180, 180) |

The craft summaries these pages expand on: [composition and layout](../../ai/references/craft/composition-and-layout.md),
[colour](../../ai/references/craft/colour.md), [typography](../../ai/references/craft/typography.md).
