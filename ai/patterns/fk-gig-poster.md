# Gig poster

**Template** `fk_gig_poster` (Library name "Gig poster") · Funky pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FK Gig poster` in `categories/funky/fk-lab-3`.

For briefs like "gig poster", "club night on Friday", "live music announcement". A LIVE MUSIC kicker, the act on two big lines with hard purple offset shadows, a yellow date plate, the venue and doors line, a teal squiggle, and a record that rolls in from the right and keeps spinning. 150 f, holds. The act, date and venue are invented stand-ins.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Record (500 px ink disc, two grooves, scalloped orange label, hole) | 0 | slides in from +700 px, expo, 16 f | lands **f10** (0%) |
| Record label (10-point star) | 0 | rolls 120° → 0 with the slide, then 0 → −200° linear to the end (one way) | turning to f148 |
| Kicker "LIVE MUSIC" (ExtraBold 48 px, teal, tracking 1.2) | 0 | stamp 1.3 → 1, back curve, 8 f | **9.3%**, **f8** |
| "SUNNY &" (ExtraBold 160 px, orange, hard shadow 10 px) | 4 | stamp 1.15 → 1 and a 4° turn into +2°, 12 f | **9.8%**, **f15** |
| "THE SPROCKETS" (ExtraBold 116 px, pink, hard shadow 8 px) | 16 | the same | **9.8%**, **f27** |
| Date plate and "FRI 14 NOV" (64 px) | 22 | stamp 1.45 → 1, 10° turn into −4° | **9.3%**, **f30** |
| Squiggle | 28 | trim 0 → 1, expo, 16 f | **f38** |
| Venue line (Bold 48 px) | 34 | rises 24 px, fades in 5 f | **f41** |

Lint 0/0/0 in the lab and placed into a fresh comp. Text-gap audit: closest pair 50.2 px (the two headline lines). Full-frame looks of the placed instance at f4 (record coming in from outside the frame) and f149 show nothing cut ([KI-144](../references/known-issues.md#ki-144)).

## Steps
1. Edit the two headline lines; keep the longer one under about 900 px wide (it ends left of the record at x 1190).
2. Change the date; the plate is sized from the text in `funky_lab3.py` (rebuild), or widen it by hand.

## Pitfalls
- The two headline lines first slammed from 1.45 with a 10° turn: the growing box covered the kicker (`text_overlap` 100%) and the second line (71%), and the far ends of the wide line made `speed_jump` notes (12.9 → 1.0 px/frame). From 1.15 with a 4° turn over 12 f, and the second line starting after the first lands, all three went away.
- The venue line is ink: it disappears on a dark ground. Keep a light ground or recolour it.

Inspiration: music-event flyers and Memphis-style posters. No external text or code was used.
