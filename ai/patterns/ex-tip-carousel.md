# Tip carousel

**Template** `ex_tip_carousel` (Library name "Tip carousel") · Explainer pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `EX Tip carousel` in `categories/explainer/ex-lab-3`.

For briefs like "3 tips", "do's for beginners", "swipe through" lessons. Three tip cards slide in from the right, one at a time, with page dots under them; each stays long enough to be read. The checklist ticks several items on one page; this shows one idea per screen. Light background included. 210 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Title "Three tips for clearer videos" (56 px ExtraBold) | 0 | Step in | |
| Tip 1 card (1000 × 460), number disc (130 px), number, title (56 px), text (34 px, two lines) | 6 | slide in from +1100 px (quint, 18 f) | in place at **f24** |
| Tip 2 in, tip 1 out | 72 | tip 2 +1100 px → 0 while tip 1 goes 0 → −1100 px, both quint, 18 f | both moves end **f90** |
| Tip 3 in, tip 2 out | 138 | same | both moves end **f156** |
| Page dots (3 grey, 22 px) and the active blue dot (28 px) | 6 | the blue dot moves one dot right with each slide (quint, 18 f) | settles **f149** at the last |

Each tip is on screen at least 66 f (2.2 s) before it leaves. Lint (with `contrast:true`) 0 errors, 0 warnings, 23 notes (12 `repeated_key_value`, 11 `speed_jump`; the holds between slides). `inspect qc` (240 px): no flashes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: 85 pairs, closest 48.5 px (title / text of a tip). Text bounds against the card (x 460–1460): at least 220 px side margin. Full-frame looks of the placed comp at f80, f146 (tip 3 arriving) and f209: nothing cut; the leaving card is only partly on screen by design.

## Steps
1. Edit the three tips in `tip_carousel()` (titles under 700 px at 56 px, texts two lines under 700 px at 34 px).
2. For four tips, add a slide frame to `f_slide`, a dot position and a card; keep 66 f or more per tip.

## Pitfalls
- Lint reported `text_overlap` (15–35%) while the cards crossed: the first build moved the entering card with expo and the leaving card with an accelerate ease, so for a few frames they really overlapped. Both cards now use the same ease over the same 18 f, which keeps them 1100 px apart.
- `reading_time` warned on tip 2 ("readable for 64 frames; 37 characters want 66"): slides at f62 and f118 became f72 and f138.
- A card's clip runs only from its slide-in to its slide-out (it is not parked off screen for the rest of the comp).

Inspiration: common carousel and story-slide conventions. No external text or code was used.
