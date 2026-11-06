# Party invite

**Template** `fk_party_invite` (Library name "Party invite") · Funky pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FK Party invite` in `categories/funky/fk-lab-3`.

For briefs like "birthday invite", "you're invited", "launch party, RSVP". A tracked YOU'RE INVITED, a slammed pink headline with a hard ink shadow, three tilted pills (date, time, place), an RSVP line, and 14 confetti pieces falling one way in the side lanes. 150 f, holds. Names and dates are invented.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Kicker (ExtraBold 50 px, purple, tracking 1.3) | 0 | stamp 1.3 → 1 | **9.3%**, **f8** |
| Headline "Mia turns 30!" (ExtraBold 170 px, hard shadow 12 px) | 5 | stamp 1.45 → 1, turn into +2° | **9.3%**, **f13** |
| Detail pills 1–3 (ExtraBold 56 px on teal / orange / yellow, −4° / +3° / −2°) | 22, 28, 34 | stamp, 6 f apart | **9.3%**, **f30 / f36 / f42** |
| RSVP (Bold 46 px, ink) | 44 | rise 24 px | **f51** |
| Confetti (rects 20 × 44 and 26 px dots) | 6–46 | fall 1150–1350 px and turn 200–420° linear to the end, x 70–270 and 1660–1850 only | constant |

Lint 0/0/0 in the lab and placed. Text-gap audit: closest pair 70.6 px (kicker / headline). Full-frame looks of the placed instance at f60, f100 and f140: nothing cut; the confetti stays clear of the pills.

## Steps
1. Edit the three pills in `DETAILS` (`funky_lab3.py`): the row is sized and centred from the text. Keep it inside x 335–1585 or move the confetti lanes.

## Pitfalls
- The first confetti lanes (x 70–400 and 1520–1850) let a piece cross ROOFTOP AT LUNA; lint said nothing, the text-gap audit flagged it (−6.9 px). Lanes outside the text row fixed it ([KI-138](../references/known-issues.md#ki-138)).
- Confetti falls one way and turns one way; no bobbing.

Inspiration: party invitations and celebration cards. No external text or code was used.
