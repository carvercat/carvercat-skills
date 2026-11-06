---
id: cookbook/story-progress-bar
title: Make a social story progress bar
section: cookbook
tags: [story, progress bar, segments, instagram story, 9:16, vertical, timer, tap through, social]
styles: [social-short-form, saas-ui]
topics: [ui, layout, timing]
related: [cookbook/progress-bar, cookbook/vertical-captions, genres/social-ads, workflow/delivery]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/progress-indicators/]
---

# Make a social story progress bar

**Goal.** The row of thin segments at the top of a 9:16 story: one segment per card, each filling left to
right while its card is on screen.

## Steps

1. A 1080 × 1920 comp. Segments across the top: 32 px side margins, 8 px gaps, 6 px tall, at y 40. Three
   cards → each segment (1080 − 2 × 32 − 2 × 8) / 3 = 333.3 px.
2. Per segment a **track** (white at 35%) and a **fill** (white) of the same size; anchor the fill on its
   left edge (`transformOrigin` `"0% 50%"`).
3. Key the fill's `scale` `[0, 1]` → `[1, 1]` **`linear`** over its card's frames (here 50 f each, back to back).
   Linear, because it is a clock.
4. Cut the cards on the same frames the segments complete.

## Measured in Carvercat 0.1.6

Comp `V Story progress` in [cookbook lab 7](../labs/README.md#cookbook-lab-7carverproj), 150 f; `inspect probe`,
fill left and right edges:

| Frame | 0 | 25 | 49 | 50 | 75 | 99 | 100 | 125 | 149 |
|---|---|---|---|---|---|---|---|---|---|
| Fill 1 | 32.0 → 32.0 | 32.0 → 198.6 | → 358.6 | → **365.4** | full | full | full | full | full |
| Fill 2 | empty | empty | empty | 373.3 | → 540.0 | → 700.1 | → **706.6** | full | full |
| Fill 3 | empty | empty | empty | empty | empty | empty | 714.7 | → 881.4 | → 1041.3 |

- The left edges held (32.0, 373.3, 714.7) while the fills grew: the anchor keeps them pinned. Half a
  segment at the half-way frame (198.6 at f25).
- The last fill reached 1041.3 at f149, the comp's last frame; its full value (1048.0) is keyed on f150, one past it.
- `inspect lint`: **0 errors, 0 warnings, 0 notes**; lint does not judge platform safe zones (the bar sits
  in the top zone the app covers with its own UI): [FR-040](../../ai/references/known-issues.md#fr-040).

## Traps

- Put the last key one frame past the comp's last frame and the bar never shows full; key it at the last
  frame if it must ([seamless loop](seamless-loop.md) explains the off-by-one).
- Lint's minimum text size does not scale with the comp height: [KI-143](../../ai/references/known-issues.md#ki-143).

## In Carvercat

- Library: `Story progress bar (9:16)` ([ss-progress-bar](../../ai/patterns/ss-progress-bar.md)), `Progress`.
- Background: [progress bar](progress-bar.md), [vertical captions](vertical-captions.md).
