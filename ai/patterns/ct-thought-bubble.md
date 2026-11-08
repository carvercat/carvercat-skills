# Thought bubble

**Template** `ct_thought_bubble` (Library name "Thought bubble") · Cartoon Bounce pack · **verified 0.1.8.1 (rev 1127; headless, isolated folders, pack added to a scratch user Library)**, comp `CT Thought bubble` in `categories/cartoon-bounce/ct-lab-3`.

For briefs like "the character wonders", "imagine...", "what's on their mind". A face jellies in, three trail dots pop from small to big, a cloud jellies in and the thought pops inside it. 120 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Head (yellow, ink outline) | 0 | jelly 0 → 110 × 92% → 95 × 105% → 102 × 98% → 100% | settles **f17**; x·y 0.997–1.012 |
| Eye 1–2 | 6 | pop; blink f84–90 | |
| Trail 1–3 (40, 58, 80 px) | 12, 16, 20 | pop 0 → 125 → 92 → 103 → 100% | last settles **f32** |
| Cloud (the pivot: white core ellipse) + 8 puffs + their ink outlines | 24 | jelly 0 → 110 × 92% → 94 × 106% → 103 × 97% → 100%; then floats up 12 px, linear, to f120 | scale settles **f41**; x·y 0.996–1.012 |
| Thought "Snack time?" (ExtraBold 80 px) | 36 | pops from 60%, floats with the cloud | scale settles **f51** |

Lint 0 errors, 0 warnings, 2 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 4 pairs, closest 309 px. Full-frame looks of the placed comp at f30 and f119: nothing cut.

## How the cloud is built
One outline for a lumpy cloud: ink circles 16 px larger than each puff are drawn first, then the white puffs and the white core on top, so only the outer edge stays ink. All 17 parts are parented to the core, so one jelly on the core moves the whole cloud.

## Steps
1. Change the thought; up to about 12 characters fit at 80 px (the core is 520 px wide).
2. Swap the face for your character; keep the trail dots between its head and the cloud.

## Pitfalls
- The float over the hold goes one way only (12 px up). A bob up and down reads as lint `jitter` ([pack pitfall 4](cartoon-bounce.md)).

Inspiration: cartoon thought balloons. No external text or code was used.
