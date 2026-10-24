# Performance: keeping Carvercat fast

## The duplicate-id trap (measured on Windows, 0.0.69)
`comp.duplicate` copies a comp **with the same clip ids**. On the Windows PC (0.0.69) two
timelines holding the same 106 audio clips and nested-instance ids (a duplicated
assembly) pushed UI work from ~20 ms to ~115 ms per frame and starved the audio; making
the copy's ids unique brought it straight back to ~15-21 ms. The app team could not
reproduce it on a Mac (50.5 vs 50.8 ms), so treat unique ids as **cheap insurance**, not
a law: rename every id in a duplicated comp - `carverproj.make_ids_unique(doc,
timeline_id)` or `reformat.py` (does it automatically) - then `edit.open {force:true}`.
Check any project with `carverproj.duplicate_ids(doc)`.

It is not only `comp.duplicate`: **every new comp starts its clip ids at `clip_1`** (seen on
0.0.72 while building the pattern lab: ten comps, each with its own `clip_1`, `clip_2`, ...).
Separate comps that never meet are harmless. The risk is a master that nests several of them,
or templates applied side by side. That is why `scripts/motion/comp_to_template.py` rewrites
ids with a per-template `--prefix`.

## Diagnosing lag
1. Read the status bar readout `N drawn · X ms work + Y wait` (work = UI frame minus
   vsync wait). Healthy: ~15-25 ms. `carvercat_state.audio.starved` climbing means the
   UI thread is too busy to feed audio.
2. Make trimmed copies of the project, each with one suspect removed (comps, audio
   tracks, media, empty tracks), open each, read the readout on the same comp with the
   playhead idle, and compare. One variable at a time.
3. Ruled out on our project: track count (13 vs 127 tracks made no difference), 774 empty
   video tracks, unused media entries.

## Other habits
- Don't keep hundreds of empty tracks from z-order juggling; they clutter the timeline.
  (`track.remove_empty` is batchable from 0.0.71.)
- Prefer native shapes over traced paths with hundreds of nodes; path geometry
  observations are huge.
- Long background renders (`export.run`) run from a snapshot; cancel with
  `deliver.cancel`.
