# Sports score update, 14 s

**Brief:** a goal goes in: update the score bug, celebrate, replay, name the scorer, then the result. **Verified 0.1.6 (rev 1105), 2026-10-27; builder and measures re-run on Carvercat 0.1.8, 2026-11-04** Sample: `categories/recipes/sports-score-update` (420 f, 1920 × 1080, green pitch stand-in gradient; replace it with match footage). Builder: `ai/scripts/motion/recipes/rc_sports.py` (the master is a `carvercat/2` file or one `scene.apply`: [how](README.md#how-the-samples-are-built)).

## Shot list
| Time | Frames | Template | Job | Notes |
|---|---|---|---|---|
| 0:00 | 0–119 | Score bug | the live score; it rolls from 2-1 to 3-1 at f52–68 | top-left overlay |
| 0:01.6 | 49–108 | GOAL slam | the celebration | impact at +9 f = **f58**, the frame the new score starts to roll |
| 0:04 | 120–164 | Replay stinger | into the replay footage | stripes clear by +33 f |
| 0:05 | 150–299 | Player lower third | who scored | over the replay |
| 0:09.5 | 285–314 | Slash wipe | to the result | covered on the cut at f300 |
| 0:10 | 300–419 | Full-time score | the result | holds |

## Timing logic
- One hit per beat: the GOAL impact and the score roll share f58; SFX on that frame.
- The replay stinger starts as the score bug and GOAL finish (f120), so two loud graphics never overlap.

## Measured on the master
- Lint 0 / 0 / 0.
- `qc` notes the lower-third hold (f173–288) and the full-time hold (f335–419) as freezes; over real footage the picture moves underneath.

Inspiration: broadcast goal-update sequences. No external text or code was used.
