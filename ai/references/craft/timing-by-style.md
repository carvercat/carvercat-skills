# Timing by style (measured in Carvercat)

Frame counts at 30 fps for each style pack. Every number in the "measured" columns was read with `carvercat_inspect mode:curves` on Carvercat 0.1.6 (rev 1105) while building the packs on 2026-10-27; the pack docs linked in the first column have the detail. "Settle" is the frame after which the value stays within 0.5% of its end value, counted from the start of the move. Use these as starting points for a brief in that style, and keep one family's numbers within one film.

How to read a row:
- **Entrance**: the preset length and what it measured. One hero item, one supporting item.
- **Overshoot**: the largest overshoot the style allows (from its presets).
- **Stagger**: the gap between parts (letters, words, rows, bars) used in the pack's templates.
- **Exit**: length of the exit preset. Exits are shorter than entrances in every style.
- **Hold**: what keeps a held frame alive.

| Style (pack doc) | Entrance (hero / support) | Overshoot | Stagger | Exit | Hold |
|---|---|---|---|---|---|
| [SaaS UI](../../patterns/saas-ui.md) | Toast drop 20 f, settles f18; Card lift 18 f, settles f12 | 4.4% (Toast drop); logo Pop - spring 16.2% only on end cards | 3 f (cards, items), 3 f bars | Modal dismiss 9 f, Toast exit 10 f (about 50–70% of the entrance) | 2–3% scale push on long holds |
| [Kinetic Typography](../../patterns/kinetic-typography.md) | Words slam 14 f, settles f13; Letters zoom in 16 f, settles f11 | 4.6% (slam); 16.2% Letters pop for energetic words | 1 f per letter, 3–5 f per word, 12 f per list row | Words exit down 12 f | the next word; beat cuts every 25 f |
| [Data Viz](../../patterns/data-viz.md) | Bar grow - spring 20 f, settles f18; point pop 12 f, settles f11 | 4.4% bars; 16.2% data points | 3–4 f per bar, 14–16 f per donut segment, 8 f per stacked segment | none in the pack: cut or dip | values land 18 f after their bar starts |
| [Corporate Brand](../../patterns/corporate-brand.md) | Soft rise 24 f, settles f21; Card settle 20 f, settles f16 | 0 (no springs) | 4–6 f | Soft fade out 16 f | Photo push - 5 s (6% over 150 f) |
| [Minimal Luxury](../../patterns/minimal-luxury.md) | Slow fade in 36 f, size settles f28, opacity f32 | 0 | 18 f per line or attribute | Slow fade out 30 f | Drift up - 4 s (0.6% H up, about 6.5 px), tracking breathe (+0.04–0.06), 14 px line drift |
| [Social short-form](../../patterns/social-short-form.md) | Hook punch 10 f, settles f7; Whip in 10 f, settles f7 | 4.4% (caption words) | 3 f per caption word | cut | scene change every 1.5–2.5 s |
| [Cartoon Bounce](../../patterns/cartoon-bounce.md) | Squash land 20 f, lands f8, settles f20; Jelly in 28 f, settles f21 | 30.8% (Pop - wobbly) | — | Anticipate jump out 20 f (7 f crouch + 13 f launch) | blinks, bounces with real contact |
| [Funky](../../patterns/funky.md) | Tilt pop 18 f, settles f16; Spin in 20 f, settles f16–18 | 30.9% angle, 16.2% size | — | Spin out 14 f | slow one-way rotation (never ping-pong) |
| [Futuristic HUD](../../patterns/futuristic-hud.md) | Flicker on 12 f, on at f10; Scan open 14 f, settles f10 | 0 (stepped flicker instead) | — | Power down 12 f | one-way sweeps, rotations and scans |
| [Retro](../../patterns/retro.md) | Rise - on twos 16 f, settles f10; Pop - on twos 12 f, settles f12 | 3.9% | — | Exit down - on twos 12 f | everything held for 2 f ("on twos") |
| [Glitch](../../patterns/glitch.md) | Glitch in 12 f, locked by f10; Stretch hit 8 f, settles f6 | stepped jumps, no curves | — | Glitch out 10 f | noise bars, short bursts |
| [Sports](../../patterns/sports.md) | Impact slam 12 f, impact f5, settles f8 | 6.7% past the impact | — | Zoom past 8 f | one hit per beat |
| [Explainer](../../patterns/explainer.md) | Step in 14 f, settles 11 f after start | 0 (Emphasis pulse 15% once, 16 f) | in reading order, at narration speed | cut | one emphasis at a time |
| [Transitions](../../patterns/transitions.md) | covers 30–40 f, cut 15–20 f in | — | Bars stagger 2 f per bar | — | — |

## Reading time (all styles)

Carvercat's lint (`reading_time`) wants **17 characters a second, and at least 25 frames**, counting only fully opaque frames and not counting spaces. Measured on 0.1.6 with test clips at 40 px:

| Text | Characters (no spaces) | Lint wants |
|---|---|---|
| "Launch" | 6 | 25 f |
| "Ship it today" | 11 | 25 f |
| "Every report writes itself every Monday" | 34 | 60 f |
| "We cut our edit time in half the very first week" | 38 | 68 f |
| 15 words (68 characters) | 68 | 120 f |

So `frames = max(25, ceil(characters × 30 / 17))`. A fade-in eats into this: a 25 f clip with a 2 f fade reads as 23 f ([kinetic-typography.md](../../patterns/kinetic-typography.md) pitfall 4). Styles with slow entrances (Minimal Luxury, 36 f fades) need the most extra time: start counting when the text is opaque.

## Choosing within a style

- **Hero vs support**: the hero gets the style's signature move (slam, spring, slow fade); supporting text gets the plain one (Card lift, Soft rise, Step in) 4–12 f later.
- **Values after shapes**: a number next to a spring bar appears 18 f after the bar starts (Data Viz); a label waits for the last bar of a group.
- **Exit length**: 50–70% of the entrance in SaaS and Corporate; equal or longer in Minimal Luxury (30 f out, 36 f in); a cut in Social and Explainer.

See also [motion-principles.md](motion-principles.md) for the curves themselves and [typography.md](typography.md) for type sizes.
