---
id: techniques/stagger-systems
title: Stagger systems
section: techniques
tags: [stagger, offset, cascade, sequence, order, centre out, random, words, letters, grid]
styles: [all]
topics: [choreography, text]
related: [principles/rhythm, principles/follow-through-and-overlap, techniques/kinetic-type, genres/infographics, principles/timing-and-spacing]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://carbondesignsystem.com/elements/motion/choreography/, https://fluent2.microsoft.design/motion, https://blog.frame.io/2023/12/13/insider-tips-how-to-create-a-staggered-layer-sequence-in-after-effects, https://aejuice.com/blog/how-to-stagger-layers-in-after-effects]
---

# Stagger systems

A stagger plays the same animation on several things, each a little later than the one before. It turns
a group into a wave and tells the viewer the reading order. A stagger "system" is the set of rules a film
uses for every group: the gap, the order and the maximum spread.

## The idea

- **Gap**: the delay between neighbours. Small gaps feel like one fluid gesture; large gaps feel like a list.
- **Order**: forward (reading order), reverse, centre-out, edges-in, random. Order carries meaning:
  centre-out says "radiating", random says "scattered, playful".
- **Spread**: gap × (items − 1). Keep it short or the last item arrives after the viewer has moved on.
- **Unit**: letters, words, lines, cards, bars, grid cells. Bigger units need bigger gaps.

## Rules of thumb (30 fps)

| Unit | Gap | Notes |
|---|---|---|
| Letters | 1–2 f | short words only (under about 12 letters) |
| Words | 2–4 f | headlines; sentences up to about 8 words |
| Lines | 4–8 f | quotes, lists |
| Cards / bars | 3–6 f | UI and charts |
| Rows of a list | 8–12 f | each row is read before the next arrives |

- Total spread at most 15–20 f for a single gesture; group long lists into chunks.
- Exits: reverse order or all at once, at half the entrance gap.
- Use one gap per unit type across the whole film.

## Measured in Carvercat

Five lines of five words each, Stagger Text by word, gap 4 f, the same 14 f rise on every line, with a
different `order` per line (`carvercat_look` every 5 f from f8):

| `order` | First word in | Sequence seen |
|---|---|---|
| `forward` | one | one, two, three, four, five |
| `reverse` | five | five, four, three, two, one |
| `centre` | three | three, then two and four, then one and five |
| `edges` | one and five | one and five, then two and four, then three |
| `random` (seed 1) | a fixed shuffled order | the same order every render for the same seed |

With 5 words and a 4 f gap, the last word started 16 f after the first and the line finished 30 f after it
began (16 + 14). That is the spread to plan for. Object staggers (six bars started 4 f apart) are in
[rhythm](../principles/rhythm.md).

**`each` vs `total`.** The Stagger Text `mode` (`amountMode` in the file) changes what the gap means. Four
lines with the same 12 f rise from f10, checked with `carvercat_look` every 4 f:

| Setting | Words | Last word starts | Meaning |
|---|---|---|---|
| `each`, gap 4 | 6 | f30 | 4 f between neighbours; the spread grows with the word count |
| `each`, gap 4 | 3 | f18 | |
| `total`, amount 20 | 6 | f30 | 20 f from first to last start, shared out: 4 f between neighbours |
| `total`, amount 20 | 3 | f30 | 10 f between neighbours |

Use `total` when a line must finish its stagger by a fixed frame whatever its length (captions, beats), and
`each` when the rhythm between words must stay constant.

## Do and don't

- Do pick the order for its meaning; default to reading order.
- Do keep the per-item animation identical so the stagger reads as one system.
- Don't stagger letters of long sentences; stagger words or lines.
- Don't let a stagger's spread overrun the comp end; the last part finishes `gap × (parts − 1)` frames
  after the first ([typography](../../ai/references/craft/typography.md)).

## Checklist

- [ ] One gap per unit type in the whole film.
- [ ] Spread ≤ 20 f for one gesture.
- [ ] Order matches meaning.
- [ ] The last part finishes before the next beat (`carvercat_look` at the end of the stagger).

## In Carvercat

- Text: the Stagger Text effect (one per text, at the top of its effects). `stagger.set` takes `by`
  (word/character/line/all), `order` (forward/reverse/centre/edges/random), `gap` (frames), `mode`
  (each/total) and `seed`. Connect what plays late with `stagger.connect` (relative position, scale,
  rotation, opacity, fill opacity, effect sizes) ([stagger](../../ai/references/effects/stagger.md)).
- In a project file: an effects entry `{"cap": "stagger", "by", "order", "amount": gap, "amountMode": "each",
  "seed", "connected": [paths]}` with keys on `text.relative` channels ([JSON authoring](../../ai/references/app/json-authoring.md)).
- Objects: offset key frames by `start + i × gap` in the file, or `key.box` over MCP.
- Ready-made staggered text: `Words rise - expo`, `Letters cascade - spring`, `Lines reveal - decelerate`
  ([Motion Patterns](../../ai/patterns/README.md)); `Words slam`, `Letters pop`, `Words drop - bounce`
  ([Kinetic Typography](../../ai/patterns/kinetic-typography.md)); `Caption words pop`
  ([Social Short-form](../../ai/patterns/social-short-form.md)).
- Only one staggered preset per property per text ([pattern pitfall 1](../../ai/patterns/README.md)).
- Labs: comp `T Stagger orders` in [the techniques lab](../labs/README.md); comp `T Stagger modes` (each vs total) in [the measurement lab 3](../labs/README.md).
