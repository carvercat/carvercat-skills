# Typography in motion (Carvercat)

Agent-neutral rules for on-screen text in Carvercat promos. Pixel sizes are for a
1920 px or 1080 px wide comp. Text size is `fontSize` in px (a true em); set the px
from the scale below. (Old stored size: a fraction of comp width, `px = size x comp_width x 0.597`.)

## Type scale (approved on the Carvercat intro)
| Role | 16:9 (1920 w) | 9:16 (1080 w) | Weight |
|---|---|---|---|
| Hero line (full-screen statement, end card) | 96 px | 90-110 px | Bold |
| Statement next to UI | 72 px | 79-90 px | Bold |
| Supporting line | 36 px | 40-56 px | Medium |
| Small UI label inside mock-ups | 20-24 px | same, scaled with the UI | Medium/Regular |
| Absolute minimum for anything meant to be read | ~32 px (in-feed social: body >= 32, headline >= 90) | | |

- Display face for headlines, one body face for the rest (the intro used Rethink Sans).
- **One accent per scene**: one orange word or phrase, not several.
- Tighter tracking on display sizes reads premium; extreme weight contrast reads modern.

## Line length and layout
- Promo headlines: 3-7 words; at most 2 lines per card; <= 42 characters per line.
- **Break a headline onto two lines rather than let it touch the UI** - text content
  accepts `\n`; with `vAlign: bottom` the last line stays at the position and earlier
  lines stack above it.
- Keep text inside the safe area (16:9: 80 % title-safe; 9:16: see
  [vertical-and-safe-areas.md](vertical-and-safe-areas.md)). Captions start >= 130 px
  from the left on 9:16 and stay clear of the right-hand button column.
- Contrast >= 4.5:1 (aim 7:1 over footage); over busy video add a scrim, plate or soft
  shadow.

## Entrances (pick per role, keep consistent per film)
| Style | How in Carvercat | Use |
|---|---|---|
| Per-letter blur rise | Stagger Text by character, gap 1.5-2; keys: relative position [0,-0.045]->[0,0] (stored values), relative opacity 0->1, blur 22->0 (stored size, about 25 px) over ~12 f, ease-out (the manual card in [../effects/stagger.md](../effects/stagger.md); a stagger tween takes no blur) | short important words (< ~12 chars) |
| Per-word rise | Stagger Text by word, gap 3-7 | sentences, VO-synced lines |
| Waterfall | by word, 4-6 f per word, 1-2 f overlap, hard opacity (Hold) | energetic hooks |
| Beat slam | whole line, scale 1.5->1 + blur 16->0, 11-18 f, on the beat | music-driven reels |
| Typewriter | reveal by character with Hold keys, ~2 f/char, cursor blink 16 f | prompts, code, AI input |
| Line rise | whole line, +10-30 px & opacity, 12-20 f | supporting text |

Rules: the text lands and then **holds still** while it is read (read time in
[motion-principles.md](motion-principles.md)); exits are faster and simpler than
entrances (8-12 f, ease-in, all at once or reversed stagger at half the gap) - and in
mid-film scenes the transition is the exit.

## Emphasis (one at a time)
- Scale pop 105-115 % and back over 6-10 f.
- Highlighter band grows left -> right behind the word (scaleX from the left edge, `transformOrigin` "0% 50%" (stored anchor [−1, 0]),
  ~18-24 f, after the text has landed; band ~64-105 % of line height, rounded).
- Colour shift to the accent; glow pulse - **key glow `blend` up only during the pulse
  and back to 0**, or the text stays hazy.
- Trim-stroke underline or box drawn on 8-15 f after the word lands (key `trimEnd` 0% to 100% by name).

## Carvercat pitfalls
- A new blur effect starts at size 10 (stored size) -> soft text unless keyed to 0 (`anim.set` with `blur` keys it by name).
- The stagger replays the whole key timeline per part, exit keys included; the last part
  finishes `gap x (parts-1)` frames late and can overrun the comp end. Gate the clip
  with its own placement opacity.
- `object.new` places at the live playhead — give the batch step a `frame` (or seek first).

## Multi-line text
`text` accepts `\n`. With vertical align bottom, the last line stays at the position and earlier lines stack above it — handy for captions that grow upward.

## Measured in Carvercat 0.1.6 (tracking, leading, size, reading time)

Measured with `carvercat_authoring mode:geometry` (ink bounds; today `measure.boxes`) and `carvercat_inspect mode:lint` on Carvercat 0.1.6 (rev 1105), Rethink Sans, 2026-10-27. Use these instead of guessing widths and holds.

### Tracking (`text_font.tracking`, 1.0 = normal)
"MAISON", Regular 64 px:

| Tracking | 0.9 | 1.0 | 1.1 | 1.2 | 1.4 | 1.6 | 1.8 |
|---|---|---|---|---|---|---|---|
| Ink width | 175 px | 229 px | 282 px | 336 px | 443 px | 550 px | 658 px |

- Width grows linearly: each +0.1 adds about **0.14 × font size per character** (53.6 px for 6 letters at 64 px). Height does not change.
- Wide tracking is expensive: "LE SAC No. 3" at 56 px and 1.5 measured 834 px; "AUTUMN  WINTER" at 88 px and 1.6 measured 1850 px (lint `outside_graphics_safe`). Measure before placing tracked caps off-centre ([ml-price-card.md](../../patterns/ml-price-card.md)).
- Tracking is keyframeable, and centred text stays centred while it changes: a closing-in title needs no position keys ([minimal-luxury.md](../../patterns/minimal-luxury.md)). Keep a "breathe" over a hold to +0.04–0.06.
- Style ranges used in the packs: Kinetic 1.0 (focus pull from 1.6), Corporate wordmark 1.25, Minimal Luxury 1.35–1.8, small tracked captions 1.2–1.5.

### Leading (`text_font.lineSpacing`)
Two lines, Regular 64 px. The ink height grows by **1.345 × font size × line spacing** per extra line:

| Line spacing | 0.9 | 1.0 | 1.1 | 1.15 | 1.3 | 1.5 |
|---|---|---|---|---|---|---|
| Two-line ink height | 124 px | 133 px | 141 px | 145 px | 158 px | 175 px |

- Display lines (ExtraBold/Bold quotes and titles) read well at 1.1–1.15; light, tracked lines at 1.3–1.35 (the Minimal Luxury quote and collection title).
- A two-line block grows around its position, so recheck the gap to the next element when you change line spacing.

### Size and lint's minimum
Ink height of "Hxg 0123" (Medium) is **0.94 × font size** (ascender to descender); caps and digits alone are about 0.72 ×.

| Font size | 18 | 22 | 24 | 28 | 32 | 48 | 64 | 96 |
|---|---|---|---|---|---|---|---|---|
| Ink height | 17.0 | 20.8 | 22.7 | 26.4 | 30.2 | 45.3 | 60.4 | 90.6 |

- Lint `text_too_small` fires under **18 px** of measured line height. Digits at 22 px (about 16 px tall) were flagged in the data-viz lab; 28 px passes. Use **28 px or more** for labels and axis numbers.
- Scale entrances count too: a pop from 60% at 30 px, or from 0 on a 320 px quote mark ("a line is 7.0 px tall"), was flagged. Text entrances start at 94% or larger (Card lift, Stamp, Words slam) ([kt-quote.md](../../patterns/kt-quote.md)).

### Hierarchy used in the verified packs (16:9)
| Role | Sizes used | Weight |
|---|---|---|
| Hero word / number | 150–300 px | ExtraBold / Bold |
| Headline | 72–96 px | Bold / SemiBold / ExtraBold |
| Name in a lower third | 34–76 px | Bold / SemiBold / Regular tracked |
| Supporting line, role, tagline | 26–40 px | Medium / Regular, muted colour |
| Labels, axis numbers, legends | 28–34 px | Medium / SemiBold |

Keep about a 2× step between levels (headline 84 → subline 38; name 76 → role 36) and colour the supporting level muted, not smaller still.

### Reading time in frames
Lint `reading_time` asks for **17 characters a second (spaces not counted) and at least 25 frames**, counting fully opaque frames only: `frames = max(25, ceil(chars × 30 / 17))`. Measured: 6 or 11 characters → 25 f; 34 → 60 f; 38 → 68 f; 68 → 120 f. Per-style timing is in [timing-by-style.md](timing-by-style.md).
