# Title card - split rule

**Template** `cb_title_card` · Corporate Brand pack · **Verified 0.1.8.1 (rev 1127)**, comp `CB Title card` in `categories/corporate-brand/cb-lab`.

A 4 × 168 px teal rule at the frame centre. "Annual Report" (SemiBold 64 px, white) and "2026" (40 px, teal) are right-aligned to its left. "Growth, focus, people" (40 px, grey) sits to its right.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Rule | 0–14 | scale Y 0 → 1 from its centre, Custom expo | settles **f9** |
| Title | 8–30 | slides 480 px left out from behind the rule, Custom expo; masked by "Left window" (everything left of x 954) | settles **f22** |
| Year | 12–34 | slides 160 px, same mask arrangement ("Left window 2") | |
| Subtitle | clip from 18; 18–40 | slides 20 px right and fades in over 12 f; masked by "Right window" (right of x 966) | settles **f32** |

Masks: `property.set {id:<text>, key:"mask", value:{"ref":"<window id>"}}`, then `parent.clear {ids:[window, text]}` when the window must move independently. Lint 0 errors, 0 warnings.

## Steps
Place and apply, then edit the three texts. If the title gets longer than about 430 px, increase its start offset to its width + 50 px so it still starts hidden.

## Pitfalls
- **Fixed 2026-10-28 (overlap audit).** The year sat 11 px under the title (geometry at rest); it is now 8 px lower, a 19 px gap. Lint does not report gaps this small ([KI-138](../references/known-issues.md#ki-138)).

