# Funky countdown

**Template** `fk_countdown` (Library name "Funky countdown") · Funky pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `FK Countdown` in `categories/funky/fk-lab-3`.

For briefs like "3, 2, 1, go", "countdown into the drop", "start of the show". Four 30 f beats (3, 2, 1, GO!), each a 700 px 16-point starburst in a new colour, an ink disc and a yellow number with a hard shadow in the burst's colour. Hard cuts on the beat. 120 f (16:9; the Social pack's countdown is 9:16).

| Part (per beat, frames from the beat start) | Motion | Measured |
|---|---|---|
| Burst (pink / teal / orange / purple, ink outline) | scale 0.4 → 1 on the pop curve, 10 f; turns 40° one way over the beat (alternating) | **15.8%**, **f10** |
| Disc (400 px, ink) | scale 0.6 → 1, pop curve, 8 f | **15.8%**, **f8** |
| Number (ExtraBold 260 px; GO! 160 px) | stamp 1.6 → 1 with a −14° turn into 0, 8 f | **9.3%**, **f8** (GO! settles comp f98) |

Every clip is exactly one beat long, so nothing holds and nothing fades out. Lint 0/0/0 in the lab and placed. Text-gap audit: no pairs share a rest window. Full-frame looks of the placed instance at f5 and f95: nothing cut.

## Steps
1. Retime to music by changing the beat length (`per`) in `funky_lab3.py`; each number needs 25 opaque frames for lint's reading time.

Inspiration: retro TV countdowns and starburst stickers. No external text or code was used.
