---
id: cookbook/chat-message
title: Bring in chat messages that push the thread up
section: cookbook
tags: [chat, message, bubble, conversation, thread, messenger, ui demo, anchor, push up]
styles: [saas-ui, social-short-form, explainer]
topics: [ui, rigging, text]
related: [genres/ui-ux-demos, principles/springs, cookbook/speech-bubble, cookbook/bullet-list]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://en.wikipedia.org/wiki/Instant_messaging, https://www.nngroup.com/articles/animation-purpose-ux/]
---

# Bring in chat messages that push the thread up

**Goal.** Messages arrive one by one at the bottom of a phone screen: each bubble grows out of its tail
corner, its text lifts in, and the older messages slide up to make room.

## Steps

1. Measure each message's width (`carvercat_authoring geometry`); bubble width = text width + 2 × 30 px,
   height 84 px, `borderRadius` 30.
2. Anchor each bubble at its **tail corner**: incoming (left) `transformOrigin` `"0% 100%"`
   (bottom-left), outgoing (right) `"100% 100%"` (bottom-right). Key `scale` 0 → 1, **back out**, 12 f.
3. The text 5 f later: rise 14 px and fade in over 10 f (expo).
4. Put every bubble and text under one **thread null**, and place message *i* one step lower in the thread
   (step = bubble height + gap = 108 px). When message *i* arrives, move the null up one step, **expo,
   10 f**, starting on the same frame as the bubble. New and old messages then move as one.
5. Hold the last message for its reading time before the comp ends.

## Measured in Carvercat 0.1.6

Comp `K Chat` in [cookbook lab 5](../labs/README.md#cookbook-lab-5carverproj): three 40 px Medium messages
at f10, f40, f70; `inspect probe` and `inspect curves`:

- Bubble 1's bottom-left corner stayed at **(620.0, 942.0)** on every frame from f11 to f30 while its width
  went 143.8 → 458.7 (f17) → 417.9 px: it grows out of the corner.
- Each bubble overshoots **9.8%** and settles **11 f** after it starts (f21, f51, f81).
- The thread moved 105 of its 108 px in the first 5 f (f40 → f45) and was still at f50. Bubble 2's corner
  rode up with it, 996.6 (f41) → 942.0 (f48): it grows into the same bottom slot.
- After two pushes message 1 sat at y 683.6 (899.6 − 2 × 108).
- `inspect lint`: 1 error (`never_visible` on the null), 0 warnings, 7 notes. At 110 f the last message
  got `reading_time` (readable 33 f, wants 34); the lab comp is 120 f.

## Traps

- Parent everything while the thread null is at its first position (here f0): parenting bakes in the
  parent's offset at the playhead ([KI-153](../../ai/references/known-issues.md#ki-153)).
- A `transformOrigin` leaves the shape where it is drawn and only moves the pivot;
  check the corner with `inspect probe` ([clock hand](clock-hand.md)). On nested instances the old `anchor`
  behaved differently (not re-measured for `transformOrigin`): [KI-109](../../ai/references/known-issues.md#ki-109).
- The null is reported as `never_visible`: [FR-041](../../ai/references/known-issues.md#fr-041).

## In Carvercat

- Curve names on this page (back out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Library: `Chat thread` ([su-chat-thread](../../ai/patterns/su-chat-thread.md)), `Message` and `Comment`
  stickers, `Notification toast`.
- Background: [UI and UX demos](../genres/ui-ux-demos.md), [springs](../principles/springs.md).
