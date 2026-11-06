---
id: cookbook/headline-word-by-word
title: Animate a headline word by word
section: cookbook
tags: [headline, words, stagger, rise, title, word by word, preset]
styles: [kinetic-typography, saas-ui, corporate-brand, explainer, all]
topics: [text, stagger]
related: [techniques/stagger-systems, techniques/kinetic-type, sound-and-timing/reading-time, cookbook/type-on-text]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://wearefevr.com/the-history-of-kinetic-typography, https://www.nngroup.com/articles/animation-duration/]
---

# Animate a headline word by word

**Goal.** A headline whose words rise into place one after another, the workhorse title entrance.

## Steps

1. One text object with the whole headline. Start its clip on the entrance frame.
2. Apply **`Words rise - expo`** (`preset.apply {name, id}`). It adds Stagger Text by word and keys the
   relative position and opacity.
3. Hold the finished line for its reading time (17 characters a second, at least 25 f), then exit with
   `Words exit down` or a whole-block fade.

## Measured in Carvercat 0.1.6

Comp `K Headline` in [cookbook lab 4](../labs/README.md#cookbook-lab-4carverproj): "Make every frame count"
110 px Bold, clip from f10, `Words rise - expo`.

- What the preset wrote: relative position offset −0.03 → 0 (settles 11 f after the word starts) and
  opacity 0 → 1 over 8 f, as baked `linear` keys; Stagger Text by word.
- `carvercat_inspect composite`: the four words appeared at **f11, f14, f17, f20** (3 f apart); the line
  was still from about f30.
- `inspect lint`: 0 errors, 0 warnings, 1 note (`repeated_key_value`).

## Traps

- One uniform gap per Stagger Text: [KI-041](../../ai/references/known-issues.md#ki-041).
- A staggered exit on the same property is refused, and staggered parts end gap × (words − 1) late:
  [KI-050](../../ai/references/known-issues.md#ki-050).
- Extending the clip does not move a relative-opacity exit: [KI-049](../../ai/references/known-issues.md#ki-049).

## In Carvercat

- Presets: `Words rise - expo`, `Words drop - bounce`, `Words slam`, `Words exit down`,
  `Lines reveal - decelerate`, `Lines slide in - left`.
- Effect detail: [stagger](../../ai/references/effects/stagger.md). Background:
  [stagger systems](../techniques/stagger-systems.md), [reading time](../sound-and-timing/reading-time.md).
