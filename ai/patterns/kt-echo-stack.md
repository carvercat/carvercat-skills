# Echo stack

**Template** `kt_echo_stack` (Library name "Echo stack") · Kinetic Typography pack · **verified 0.1.8.1 (rev 1127; `ai/scripts/motion/verify_pack.py`: placed in a fresh 16:9 and a fresh 9:16 comp, lint 0/0/0, qc no flash; against the v1 original the silhouette differs by at most 0.00 % of pixels over 7 frames; object-level check pass)**, comp `KT Echo stack` in `categories/kinetic-typography/kt-lab-3`.

For briefs like "hype opener", "music drop", "say it louder", "event countdown": repetition, one of the kinetic-type devices the pack did not have. A hero word ("LOUDER", ExtraBold 150 px, accent) slams in; four outline-only copies (inner pair off-white, outer pair muted) ripple out to rows 150 px above and below it and keep spreading a little through the hold. 120 f.

Frames are comp frames.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Word (filled accent) | 0 | scale 1.5 → 1, 10 f (expo), opacity in 3 f | settles **f7** |
| Echo up 1 / down 1 (outline `#F4F1EA`) | 10 | from 36 px nearer the centre to ±150 px, 14 f (expo); scale 0.94 → 1; fade 4 f | opacity **f14**, size **f19**, position in by **f24** |
| Echo up 2 / down 2 (outline `#9A968E`) | 14 | the same to ±300 px | opacity **f18**, size **f23**, in by **f28** |
| Drift | to f120 | inner echoes 6 px, outer 12 px further out (linear) | keeps the hold alive |

Outline-only text: `text.fill` Paint none, `text.outline` Paint solid, Thickness 0.035. Lab comp lint on 0.1.8.1 (native size): 0 errors, 4 warnings, 0 notes (`text_overlap` between neighbouring text boxes at single frames while the parts move; the v1 lab linted 0 warnings on the same build, not yet traced). Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (44.2 px between rows).

## Steps
1. Place and apply. Change the word in all five texts (they must match).
2. Longer words: keep the line under about 1000 px wide; the rows are 150 px apart for a 150 px font (108 px cap height + 42 px gap).
3. On a beat: put the hero hit on the beat, the inner echoes 10 f later and the outer ones 4 f after that (at 120 BPM a beat is 15 f).

## Pitfalls
- **Lint flags overlaps while things move.** The first version slid the echoes out from behind the hero word. Lint reported four `text_overlap` warnings at f13 and f16 (47% and 86% of the smaller box). The echoes now start 36 px short of their rows and grow from 0.94, so no two texts ever overlap.
- A partly transparent echo never counts as read (lint counts only fully opaque frames), so dim the outer echoes with a darker outline colour, not with opacity.

Inspiration: the repetition device in kinetic typography. No external text or code was used.
