# Hanging sign

**Template** `ct_hanging_sign` · Cartoon Bounce pack · **verified 0.1.8.1 (rev 1127; headless, isolated folders, pack added to a scratch user Library)**, comp `CT Hanging sign` in `categories/cartoon-bounce/ct-lab-2`.

A red "OPEN" sign (560 × 220 px) on two strings from a nail, swinging and settling. 90 f, then still.

| Part | Motion | Measured |
|---|---|---|
| Nail (the pivot) | rotation 28° → −16° → 8° → −3.5° → 0° at f0, 12, 23, 33, 42 (S curve cubic-bezier(0.333, 0, 0.667, 1) between) | **30.9%** reported overshoot (the swing), settles **f42** |
| String left/right, Sign board, Sign text | parented to the nail (offset positions, see [ct-character-hop.md](ct-character-hop.md)) | |

Lint 0 errors, 0 warnings. Placed into a fresh comp: lint 0/0/0. Every swing is a visible fraction (about 55%) of the one before: follow-through with real energy loss.

## Pitfalls
- A swing baked from a spring ended in sub-pixel reversals: lint `jitter` on all four parts. Five hand-set extremes fix it.
- An invisible pivot null failed lint (`never_visible`); the nail is the pivot.

Inspiration: follow-through in classic animation; shop signs. No external text or code was used.
