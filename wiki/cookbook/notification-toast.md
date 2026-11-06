---
id: cookbook/notification-toast
title: Drop a notification toast in and out
section: cookbook
tags: [notification, toast, banner, alert, drop down, ui, saas, message, exit]
styles: [saas-ui, social-short-form, explainer]
topics: [ui, timing]
related: [cookbook/chat-message, genres/ui-ux-demos, sound-and-timing/reading-time, principles/springs]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.nngroup.com/articles/animation-purpose-ux/]
---

# Drop a notification toast in and out

**Goal.** A toast ("Payment received") drops in from the top with a little spring, waits to be read, and
leaves upwards.

## Steps

1. The toast: rectangle 720 × 120 px, `borderRadius` 20, white, `dropShadow` `"0 6.5px 16.6px #00000040"` (the lab stores softness 0.02, which is a 16.6 px blur: [shadow and glow](../techniques/shadow-and-glow-in-motion.md)); icon and text on top, at y 110.
2. Make **two clips** of each part, butted: the stay (here f10–f70) and the exit (f70–f90).
3. Apply **`Toast drop - spring`** to the stay clips and **`Toast exit up`** to the exit clips.
4. Give it at least its reading time between landing and leaving.

## Measured in Carvercat 0.1.6

Comp `K Toast` in [cookbook lab 7](../labs/README.md#cookbook-lab-7carverproj); `inspect probe` and `inspect
curves` on the toast:

| Frame | 10 | 12 | 14 | 16 | 20 | 30 … 69 | 79 | 85 | 89 |
|---|---|---|---|---|---|---|---|---|---|
| Toast centre y | 45.2 | 58.1 | 80.0 | 97.8 | 111.8 | 110.0 | 110.0 | 94.9 | 45.2 |
| Opacity | 0 | 0.73 | 0.95 | 1 | 1 | 1 | 1 | 0.89 | 0 |

- `Toast drop - spring` (20 f): starts **64.8 px** above (0.06 of the height), opaque by f16, overshoots
  4.4% (1.9 px low at f20–24) and settles **f28**.
- `Toast exit up` is an **out** preset: it keyed the **last 10 f of its clip** (f79–f89), not the start,
  rising the same 64.8 px and fading.
- `inspect lint contrast:true`: 0 errors, 1 warning, 7 notes. The warning is `reading_time` on the exit
  clip's text alone (18 f): lint counts each clip separately, so a split text is judged per piece.

## Traps

- This lab split each part into an in clip and an out clip rather than stacking two presets on one clip.
- `preset.apply` takes one `id`: [KI-113](../../ai/references/known-issues.md#ki-113).
- The shadow spreads past the frame top during the exit (`effect_clipped_by_frame` note); harmless here.

## In Carvercat

- Library: `Notification toast` ([su-notification-toast](../../ai/patterns/su-notification-toast.md)),
  `Toast drop - spring`, `Toast exit up`, `Alert banner`.
- Background: [UI and UX demos](../genres/ui-ux-demos.md), [reading time](../sound-and-timing/reading-time.md).
