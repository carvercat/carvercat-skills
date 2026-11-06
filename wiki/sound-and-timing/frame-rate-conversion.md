---
id: sound-and-timing/frame-rate-conversion
title: Converting a comp to another frame rate
section: sound-and-timing
tags: [frame rate, conversion, 25 fps, 24 fps, 60 fps, rescale, keys, retime, pal, ntsc]
styles: [all]
topics: [timing, delivery]
related: [sound-and-timing/frame-rates, sound-and-timing/beat-sync, techniques/nested-comps-and-time, workflow/delivery]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.fujifilm-x.com/en-in/stories/understanding-frame-rates/, https://partnerhelp.netflixstudios.com/hc/en-us/articles/360051554394-Timed-Text-Style-Guide-Subtitle-Timing-Guidelines]
---

# Converting a comp to another frame rate

A 30 fps film needs a 25 fps broadcast version; a 24 fps title needs a 60 fps screen version. Carvercat stores
time in frames, and changing the comp's rate does not move anything ([frame rates](frame-rates.md)): the film
just plays faster or slower. To keep the timing in seconds, every frame number in the comp has to be rescaled.

## The procedure

Multiply by r = new fps ÷ old fps:

1. the comp's `duration` (frames) and `sceneFps` (set to the new rate);
2. every clip's start (`left`, stored in timeline pixels at 4 per frame: divide by 4, multiply, multiply by 4)
   and length (`duration`);
3. every clip's `sourceIn` (for nested instances and trimmed media);
4. every keyframe's `frame` on every property, effect and text channel;
5. the same for every nested comp the master uses (they keep their own frame counts).

Then reopen, check `carvercat_inspect {mode:"timing"}` against the original in seconds, and re-run lint (reading
time is in seconds, so it stays valid).

## Measured in Carvercat

The 30 fps timing-lab comp (a one-second expo move from 0.5 s, a 34-character line held 2 s, 3 s long) rescaled
with the procedure above, then opened and inspected:

| Target | Keys | Move starts / settles | Text leaves | Comp |
|---|---|---|---|---|
| 25 fps, fractional keys kept | 12.5 → 37.5 | f13 / f35 | f49 (2.0 s) | 75 f |
| 25 fps, rounded to whole frames | 12 → 38 | f13 / f35 | f49 | 75 f |
| 24 fps, rounded | 12 → 36 | f13 / f33 | f47 (2.0 s) | 72 f |
| 60 fps | 30 → 90 | f31 / f80 | f119 (2.0 s) | 180 f |

- **Fractional key frames are accepted** (12.5, 37.5) and play correctly; the move then lasts exactly 1 s.
- Rounding to whole frames changed the 25 fps move from 25 to 26 frames (12 → 38): a 4% timing change. Round
  only start and end keys of moves that must stay exact, or keep fractions.
- Lint raised nothing new after conversion (only the expected `speed_jump` info on the expo start).

## Do and don't

- Do convert every comp in the project, nested ones included, with the same ratio.
- Do re-check beat-synced keys: frames per beat change (120 BPM: 15 f at 30 fps, 12.5 at 25, 12 at 24).
- Don't use `comp.format {fps}` alone; it keeps frame numbers and changes the film's speed.
- Don't round stepped animation (on twos) blindly: 2-frame steps become 1.67 f at 25 fps; re-step it instead.

## Checklist

- [ ] Comp duration, clip starts and lengths, `sourceIn` and all keys rescaled by the same ratio.
- [ ] `inspect timing` matches the original in seconds.
- [ ] Beat-synced and stepped animation re-checked.

## In Carvercat

- Script it on the project file (the fields above are listed in [JSON authoring](../../ai/references/app/json-authoring.md));
  a 20-line converter is enough. Then `edit.open {path, force:true}` and inspect.
- 16:9 to 9:16 is a different conversion (space, not time): [vertical and safe areas](../../ai/references/craft/vertical-and-safe-areas.md).
- Lab: the converted copies were made from comp `S 30 fps` in [the timing lab](../labs/README.md).
