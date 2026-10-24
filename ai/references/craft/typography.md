# Typography in motion (Carvercat)

Agent-neutral rules for on-screen text in Carvercat promos. Pixel sizes are for a
1920 px or 1080 px wide comp. Carvercat text size is a fraction of comp width:
`px = size x comp_width x 0.597` -> `size = px / (comp_width x 0.597)`.

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
| Per-letter blur rise | Stagger Text by character, gap 1.5-2; keys: relative position [0,-0.045]->[0,0], relative opacity 0->1, blur 22->0 over ~12 f, Ease out | short important words (< ~12 chars) |
| Per-word rise | Stagger Text by word, gap 3-7 | sentences, VO-synced lines |
| Waterfall | by word, 4-6 f per word, 1-2 f overlap, hard opacity (Hold) | energetic hooks |
| Beat slam | whole line, scale 1.5->1 + blur 16->0, 11-18 f, on the beat | music-driven reels |
| Typewriter | reveal by character with Hold keys, ~2 f/char, cursor blink 16 f | prompts, code, AI input |
| Line rise | whole line, +10-30 px & opacity, 12-20 f | supporting text |

Rules: the text lands and then **holds still** while it is read (read time in
[motion-principles.md](motion-principles.md)); exits are faster and simpler than
entrances (8-12 f, Ease in, all at once or reversed stagger at half the gap) - and in
mid-film scenes the transition is the exit.

## Emphasis (one at a time)
- Scale pop 105-115 % and back over 6-10 f.
- Highlighter band grows left -> right behind the word (scaleX from the left edge,
  ~18-24 f, after the text has landed; band ~64-105 % of line height, rounded).
- Colour shift to the accent; glow pulse - **key glow `blend` up only during the pulse
  and back to 0**, or the text stays hazy.
- Trim-stroke underline or box drawn on 8-15 f after the word lands.

## Carvercat pitfalls
- A new blur effect starts at size 10 -> soft text unless keyed to 0.
- The stagger replays the whole key timeline per part, exit keys included; the last part
  finishes `gap x (parts-1)` frames late and can overrun the comp end. Gate the clip
  with its own placement opacity.
- `object.new` places at the live playhead — give the batch step a `frame` (or seek first).

## Multi-line text
`text` accepts `\n`. With vertical align bottom, the last line stays at the position and earlier lines stack above it — handy for captions that grow upward.
