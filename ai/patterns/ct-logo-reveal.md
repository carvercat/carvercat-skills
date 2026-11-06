# Squash logo reveal

**Template** `ct_logo_reveal` (Library name "Squash logo reveal") · Cartoon Bounce pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `CT Logo reveal` in `categories/cartoon-bounce/ct-lab-3`.

For briefs like "a playful logo sting", "toy brand", "kids' channel ident". A ball bounces in from the right on real parabolas, squashing on every contact, lands as the logo mark, and the word springs up out of the baseline on the last impact. 120 f.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Logo ball (140 px, anchor at the bottom edge) | f0–42 | a falling half-parabola from the top right, then two hops (230 px and 90 px high), each baked every 2 f; contacts **f14, f30, f42** | position settles **f42** (22 keys) |
| | each contact | 88 × 114% two frames before, 130 × 74% on contact (124 × 80% on the last), then 92 × 109% leaving | x·y **0.962–1.008**; scale settles **f54** |
| Ball shadow | f0–42 | follows x; 40 → 100% and darker as the ball nears the ground | |
| Wordmark "bouncy" (ExtraBold 190 px) | f42 | Stagger Text by character, 2 f apart: each letter rises from 7% H (75.6 px) below, overshoots 1.2% H (12.96 px), settles (4 keys) | last letter in by about **f66** |
| Tagline (Bold 44 px) | f66 | rises 24 px, fades in | settles **f75** |

Lint 0 errors, 0 warnings, 2 notes (`speed_jump` at the last contact, intended). Placed into a fresh comp: lint 0/0/0. Text-gap audit: 1 pair, Wordmark / Tagline 34 px. Full-frame looks of the placed comp at f42 and f119: nothing cut.

## Steps
1. Change `word` and `px` in `logo_reveal()`; the lockup (ball + 36 px + word) is centred from the measured word width (`textw`).
2. For a real logo, keep the ball as the mark or put the logo where the word is.

## Pitfalls
- The arcs are true parabolas because they are baked every 2 f ([arcs, method 1](../references/craft/principles/arcs.md)); a peak key alone makes a "^".
- `inspect curves` reports 300% "overshoot" for the ball's scale and 17% for the word's lane: both are measured against the last key ([KI-152](../references/known-issues.md#ki-152)). Read the keys.
- Per-letter squash is impossible ([KI-134](../references/known-issues.md#ki-134)); the letters rise and settle instead.

Inspiration: bouncing-ball logo stings. No external text or code was used.
