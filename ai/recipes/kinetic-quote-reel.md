# Kinetic quote reel, 18 s

**Brief:** a type-only piece: an opening line, a rotating claim, a quote, a beat of words, and a follow. **Verified 0.1.6 (rev 1105), 2026-10-28; builder and measures re-run on Carvercat 0.1.8, 2026-11-04** Sample: `categories/recipes/kinetic-quote-reel` (550 f, 1920 × 1080, near-black). Builder: `ai/scripts/motion/recipes/rc_kinetic.py` (the master is a `carvercat/2` file or one `scene.apply`: [how](README.md#how-the-samples-are-built)).

## Shot list
| Time | Frames | Template (Kinetic Typography) | Job |
|---|---|---|---|
| 0:00 | 0–59 | Focus pull | the opener |
| 0:02 | 60–179 | Word swap | "We build faster / smarter / together" |
| 0:05.4 | 162–197 | Split doors (Transitions) | into the quote; cut at f180 |
| 0:06 | 180–329 | Kinetic quote | the voice |
| 0:11 | 330–429 | Beat words | THINK / BUILD / SHIP / REPEAT, 25 f each |
| 0:14.3 | 430–549 | Follow end card | follow |

## Timing logic
- Beat words are cut at 25 f each (72 BPM at one word a beat, or 144 BPM at one word every two beats); place music so the cuts land on beats.
- One transition, at the change from claims to the quote.

## Measured on the master
- Lint 0 / 0 / 0.
- `qc` (240 px) notes the quote hold (f234–329) and the end card hold (f454–549) as freezes.

Inspiration: manifesto and lyric-style typography videos. No external text or code was used.
