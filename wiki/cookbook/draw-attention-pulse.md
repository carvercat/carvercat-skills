---
id: cookbook/draw-attention-pulse
title: Pulse a button to draw attention
section: cookbook
tags: [pulse, emphasis, call to action, cta, button, swell, look here]
styles: [saas-ui, explainer, social-short-form, corporate-brand]
topics: [emphasis, ui]
related: [design/visual-hierarchy, principles/staging, cookbook/pop-in, cookbook/ripple]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/animation-usability/, https://www.nngroup.com/articles/principles-visual-design/]
---

# Pulse a button to draw attention

**Goal.** One swell on a button or key object at the moment the narration names it: "look here", once.

## Steps

1. Split the object's clip at the frame the narration names it (`clip.blade {frame}`, or two clips in the
   project file), so the pulse can live on the second part.
2. Apply **`Emphasis pulse`** to the second part (`preset.apply {name, id}`).
3. Pulse once. Repeating every second turns emphasis into noise; for a waiting state use a quiet loop
   instead ([loop seamlessly](seamless-loop.md)).
4. Add a ripple on the same frame for a click ([ripple](ripple.md)).

## Measured in Carvercat 0.1.6

Comp `K Pulse` in [cookbook lab 2](../labs/README.md#cookbook-lab-2carverproj): a 420 × 110 px button,
split at f20, `Emphasis pulse` on the part from f20; label on a separate text above it.

- What the preset wrote: `scale` (old name `scaleUniform`) 1.0 → **1.15** at +6 f → 1.0 at +16 f (16 baked `linear` keys).
- `carvercat_inspect probe`: width 420 px at f19, 466 at f22, **483 at f26**, 467 at f30, 427 at f33, 420
  from f36. No jump across the split.
- `inspect lint`: **0 errors, 0 warnings, 0 notes**.
- The label did not swell with it: put the label on the same pulse (or parent it) if it should.

## Traps

- `preset.apply` takes one `id` at a time: [KI-113](../../ai/references/known-issues.md#ki-113).
- Extending a clip does not extend keyed exits on relative text channels:
  [KI-049](../../ai/references/known-issues.md#ki-049).

## In Carvercat

- Presets: `Emphasis pulse` (Explainer), `Card lift` (SaaS UI); templates `Callout`
  ([ex-callout](../../ai/patterns/ex-callout.md)), `CTA end card` ([su-cta-end-card](../../ai/patterns/su-cta-end-card.md)).
- Background: [visual hierarchy](../design/visual-hierarchy.md), [staging](../principles/staging.md).
