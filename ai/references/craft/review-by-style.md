# Review checklists by style

Run the general [review-checklist.md](review-checklist.md) first. Then run the list for the film's style. Each check names the Carvercat tool that answers it; the thresholds are the ones measured while building and verifying the packs on Carvercat 0.1.6 (rev 1105), 2026-10-27 (see [timing-by-style.md](timing-by-style.md)).

Tools: `curves` = `carvercat_inspect mode:curves` (overshoot, settle), `lint` = `carvercat_inspect mode:lint`, `look` = `carvercat_look` (whole frame; `region` crops are unreliable for backgrounds, [KI-135](../known-issues.md#ki-135)), `geometry` = `measure.boxes`.

## Every style
- [ ] `lint` 0 errors, 0 warnings on every comp and the master. Masked builds: lint does not see masks ([KI-133](../known-issues.md#ki-133)); judge them with `look`.
- [ ] Every text clears `reading_time` (17 characters a second, at least 25 opaque frames) and `text_too_small` (labels 28 px or more).
- [ ] Templates placed from the Library: lint the instance comp too (a template placed into a fresh comp linted 0/0/0 for every pack).
- [ ] Fonts: `carvercat_inspect mode:lint|expect` shows the font resolved (Rethink Sans installed, [KI-136](../known-issues.md#ki-136)).

## SaaS UI
- [ ] `curves`: springs only on things that drop in, 4–5% (Toast drop 4.4%); everything else expo, no overshoot.
- [ ] Exits are 50–70% of the entrance (Modal dismiss 9 f after an 18 f Card lift).
- [ ] Text inside a card lifts with Card lift, not a drop; `look` at the entrance frames: no text outside its card.
- [ ] Cursor clicks: the ripple frame equals the press frame; `look` at that frame.

## Kinetic Typography
- [ ] One idea per beat; beat words hold at least 25 f at full opacity (no fade-in on beat cuts).
- [ ] Only one staggered preset per text object (a second is refused); staggered text exits with a non-staggered preset.
- [ ] Letter zooms (2.4×) overhang: `lint text_overlap` clean with the next line at least 1.25× the font size away.
- [ ] Masked word slots: windows sized to the measured ink (`geometry`) plus 6 px.

## Data Viz
- [ ] Values land after their shape: number clips start 18 f after a spring bar starts.
- [ ] `curves`: bars 4.4%, points 16.2%, nothing else springs. Stacked segments do not spring (an overshoot covers the next segment).
- [ ] Ellipse rings: rotated +90° and trimmed 1 − b → 1 − a, so they fill clockwise from 12 o'clock (`look` at 25%, 50%).
- [ ] Highlight one series, grey the rest; axis labels 28 px.

## Corporate Brand
- [ ] `curves`: 0% overshoot on every object.
- [ ] Entrances 14–24 f, exits about 16 f; one accent colour.
- [ ] Light layouts carry their own background object (a dropped "Lab bg" would leave navy text on whatever is underneath).
- [ ] Reveals from behind a rule start fully hidden (travel ≥ the text's own width).

## Minimal Luxury
- [ ] `curves`: 0% overshoot (a stacked fade in/out may report "overshoot 100" on scaleUniform: confirm with `look`).
- [ ] Every hold moves: a drift, a tracking breathe or a line drift; `look` at two hold frames 60 f apart shows a change.
- [ ] Wide tracking measured with `geometry`; nothing past the graphics-safe edge (x 96–1824).
- [ ] Gleams: one text as the mask of a gradient shape; the gleam takes 60–80 f to cross.

## Social short-form (9:16)
- [ ] Hook visible by f10; scene changes every 1.5–2.5 s.
- [ ] Captions inside the 9:16 safe area ([vertical-and-safe-areas.md](vertical-and-safe-areas.md)), clear of the right-hand buttons.
- [ ] No ping-pong bobs (lint reads them as jitter); motion is one-way.
- [ ] Whips have the Motion blur effect.

## Cartoon Bounce
- [ ] Squashes pivot on the contact edge (`transformOrigin` "50% 100%" for landings; stored anchor [0, −1]).
- [ ] Springs up to about 31% are fine here; `curves` settle within about 21 f.
- [ ] Blinks: keys at least 4 f apart (lint `same_frame_keys`).

## Funky
- [ ] Rotation in every entrance; after landing, rotation continues one way only.
- [ ] `curves`: angle springs about 30%, size springs 16% or less.

## Futuristic HUD
- [ ] Glow amount 0.45–0.6, never above 0.8; strokes 3–5 px.
- [ ] Flickers: `inspect qc` shows no flash; stepped opacity uses Hold keys.
- [ ] Sweeps and rotations run one way.

## Retro
- [ ] On twos everywhere: Hold easing, a new pose every 2 f; `curves` shows stepped values.

## Glitch
- [ ] All motion stepped (Hold keys); bursts short, not continuous.
- [ ] No more than 3 flashes a second (`inspect qc`).
- [ ] `curves` may report the first jump as "overshoot": read the keys, not the number.

## Sports
- [ ] One hit per beat, SFX on the impact frame (Impact slam impact at f5).
- [ ] Moves 8–14 f; diagonals consistent in direction.
- [ ] Score changes readable: the new number holds at least 25 f.

## Explainer
- [ ] Everything enters in reading order, at narration speed.
- [ ] One emphasis at a time; Emphasis pulse runs once.
- [ ] Captions follow speech; `reading_time` warnings on fast speech are judged against the voice-over ([../workflows/captions-and-voiceover.md](../workflows/captions-and-voiceover.md)).

## Transitions
- [ ] The frame is fully covered on the cut frame (`look` at the cut ±1).
- [ ] Panels never sit still off screen (lint `cropped_at_rest`): each panel's clip spans only its motion.
- [ ] Shapes drawn at most 1000 px and scaled up ([KI-137](../known-issues.md#ki-137)).
