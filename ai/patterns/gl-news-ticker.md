# Scan-line news ticker

**Template** `gl_news_ticker` (Library name "Scan-line news ticker") · Glitch pack · **verified 0.1.8.1 (rev 1127 build; headless, isolated folders, pack added to a scratch user Library; `ai/scripts/motion/verify_pack.py`)**, comp `GL News ticker` in `categories/glitch/gl-lab-3`.

For briefs like "breaking news crawl", "stream ticker", "esports headlines along the bottom". A dark 100 px band at y 960 with three faint scan lines, a red BREAKING tag and a LIVE chip on top of it at the left, and headlines (white SemiBold 44) crawling left at a constant 7 px a frame. 150 f.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Ticker band (1920 × 100) | 0 | switches on like a tube: height 2 → 40 → 104 → 100% (Hold) | **f6** (the 104% step reads 4.1%) |
| Scan line 1–3 (2 px, 5%) | 6 | static | |
| Tag plate / Tag "BREAKING" | 2 / 6 | plate switches on; red/cyan split 12 → 6 → 0 px, re-glitch at f70 and f120 | split **f12**; steady **f122** |
| Live chip / dot / "LIVE" | 8 | chip switches on; the 16 px green dot dims to 30% every 15 f (1 s period) | |
| Headline 1–2 | 0 (visible f10) | linear crawl, 1050 px over the clip; leave through the left frame edge | readable from **f15**; headline 1 whole until about f34 |

Lint 0 errors, 0 warnings, 1 info note; `inspect qc` (240 px): **no flashes**. Placed into a fresh comp: lint 0/0/0, qc no flashes. Text-gap audit: closest pair "LIVE" / its dot, 12.0 px (the dot sits in the chip by design).

## Steps
1. Edit `HEADLINES` in `glitch_lab3.py`. A headline is only added when it gets at least 50 f on screen (lint reading time); for a longer crawl lengthen the clip, do not speed it up past about 8 px a frame.
2. The crawl is not a seamless loop; for a loop see the Funky marquee bands ([fk-marquee-bands.md](fk-marquee-bands.md)).

## Pitfalls
- The tag sits **above** the band, not on it. On the band, the headlines had to pass under the tag behind a mask, and lint still reported `text_overlap` (16%) for the masked part ([KI-160](../references/known-issues.md#ki-160)).

Inspiration: broadcast news crawls and scan-line displays. No external text or code was used.
