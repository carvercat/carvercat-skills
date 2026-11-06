# Staging

**What it does:** one idea per beat, presented so it cannot be missed. Everything else steps back.

## How in Carvercat
- **Dim the rest:** a scrim (a frame-size rectangle at 30–50% opacity) between the app and the dialog.
- **Grey the rest:** one series in the accent, the others neutral.
- **Order the build:** grid, then data, then the highlight value; title, then support.
- **Give it time:** start the next beat only after the last one is readable (lint `reading_time`).
- Check a paused frame with `carvercat_look`: every entrance, hold and exit frame should read on its own.

## Measured examples
| Template | Staging device | Numbers |
|---|---|---|
| Modal over app ([su-modal.md](../../../patterns/su-modal.md)) | scrim to 45% | f6–20; the modal settles **f20** |
| Column chart ([dv-column-chart.md](../../../patterns/dv-column-chart.md)) | one cyan column, five grey | peak value lands **f46** after the last column |
| Standings table ([sp-standings.md](../../../patterns/sp-standings.md)) | red highlight behind one row | grows at f50, after every row has settled (f33) |
| Highlight sweep ([kt-highlight-sweep.md](../../../patterns/kt-highlight-sweep.md)) | marker behind one word | marker f14–26, word f18 |
| Compare columns ([ex-compare-columns.md](../../../patterns/ex-compare-columns.md)) | the second column waits 40 f | first column done by about f40 |

## Traps
- Lint does not see occlusion: stacked cards with text all count for `text_overlap`. Keep text on the front card only ([gl-error-cascade.md](../../../patterns/gl-error-cascade.md)).
- Lint does not see masks ([KI-133](../../known-issues.md#ki-133)); check masked staging with a look.
