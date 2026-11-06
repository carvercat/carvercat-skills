# Opening credits

**Template** `kt_opening_credits` (Library name "Opening credits") · Kinetic Typography pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `KT Opening credits` in `categories/kinetic-typography/kt-lab-3`.

For briefs like "opening titles", "series opener", "credits for a short film", "event speakers in order". Three credit cards: a small tracked role ("DIRECTED BY", Medium 40 px, tracking 1.6, muted) above a name (ExtraBold 110 px). The name's letter spacing closes in as it fades up. The main title ("NORTHBOUND", ExtraBold 200 px) then lands over an accent rule that draws out from its centre. 210 f (7 s).

Frames are comp frames.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Role 1–3 | 0, 50, 100 (50 f each) | tracking 2.0 → 1.6, 24 f (expo); fade in 8 f, out in the last 8 f (accelerating) | tracking settles **f15** (card 1) |
| Name 1–3 | 2, 52, 102 (48 f each) | tracking 1.25 → 1.0, 30 f (expo); fade in 8 f, out in the last 8 f | tracking settles **f21**; fully opaque f10–42 (32 f) |
| Main title | 150 | scale 1.12 → 1, 20 f (expo), fade 6 f; then a slow pull to 0.98 by f210 | opaque **f156**; lands **f170** |
| Title rule (8 px, accent) | 160 | Trim Stroke start 0.5 → 0, end 0.5 → 1, 16 f (expo) | settles **f170** |

Lint 0 errors, 0 warnings (6 notes: held opacity keys). Placed into a fresh comp: lint 0/0/0. Text-gap audit: no tight pairs (41.2 px between role and name).

## Steps
1. Edit `CREDITS` and `TITLE` in `ai/scripts/motion/kinetic_type_lab3.py` and rebuild, or edit the texts of a placed instance.
2. Each card gives 32 fully opaque frames: enough for names up to about 18 characters without spaces. Longer names or two names on a card: raise `per`.
3. Land the main title on the strongest musical moment ([title sequences](../../wiki/genres/title-sequences.md)): slide the instance so f150 sits on it.

## Pitfalls
- **Small capitals measure small.** Lint's minimum is an 18 px line height, measured on the ink, and a capitals-only line has no ascenders or descenders. "DIRECTED BY" at 40 px Medium measures 29.0 px tall, so it passes with room to spare. Do not go much below 30 px for role lines (see [saas-ui.md](saas-ui.md#pitfalls-found-while-building-this-pack-016) pitfall 9).
- Cards do not overlap in time: each fades out in its last 8 f, and the next starts on the frame after.

Inspiration: opening title cards in film and series. No external text or code was used.
