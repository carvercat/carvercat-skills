# Follow-through and overlapping action

**What it does:** parts of a thing do not stop at the same time. Loose parts keep going and settle after the main body; groups arrive one after another instead of all at once.

## How in Carvercat
- **Overlap within a group:** the Stagger effect (by letter, word or line) on text presets, or start times a few frames apart on separate objects.
- **Follow-through after a stop:** a decaying swing or wobble after the main move: spring presets, or hand-set extremes that shrink each time.
- **Containers first, content after:** a card lands, then its text 2–4 f later; on exit the content leaves first.

## Measured examples
| Template | Overlap / follow-through | Numbers |
|---|---|---|
| Hanging sign ([ct-hanging-sign.md](../../../patterns/ct-hanging-sign.md)) | swing 28 → −16 → 8 → −3.5 → 0° (each about 55% of the last) | still from **f42** |
| Words slam ([kinetic-typography.md](../../../patterns/kinetic-typography.md)) | 5 f per word | 4.6% overshoot, settles f13 per word |
| Column chart ([dv-column-chart.md](../../../patterns/dv-column-chart.md)) | 4 f per column | Column 1 settles f26, Column 6 f46 |
| Card + text (SaaS lower third, [su-lower-third.md](../../../patterns/su-lower-third.md)) | pill f0, chip f4, name f8, role f11 | pill settles f9 |
| Orbit end card ([fk-orbit-end.md](../../../patterns/fk-orbit-end.md)) | satellites parented to a turning hub | one way, 120° over the hold |

## Traps
- Two staggered presets on one text cannot share a property; in practice one staggered preset per text ([kinetic-typography.md](../../../patterns/kinetic-typography.md)).
- A long baked spring tail is read as `jitter`; end a swing with 3–5 visible extremes.
- The last part of a stagger finishes `gap × (parts − 1)` frames late ([KI-050](../../known-issues.md#ki-050)); make sure it lands inside the clip.
