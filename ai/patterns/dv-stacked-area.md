# Stacked area chart

**Template** `dv_stacked_area` (Library name "Stacked area chart") · Data Viz pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `DV Stacked area` in `categories/data-viz/dv-lab-3`.

For briefs like "how the mix changed", "users by platform over the year", "share and total together". Three stacked layers over 12 months (Android, iOS and Web, millions, sample data); Web is the subject (cyan, top), the others are slate. Labelled inline at the right end instead of a legend, with a callout where Web passes iOS. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Grid (0–40M) and month labels | 0–12 | opacity in 8 f | |
| Windows 1–3 (masks, anchor at the left edge) | 0 | scale X 0 → 1, f8–56, S curve cubic-bezier(0.333, 0, 0.667, 1) | settle **f51** |
| Layers (closed paths, one per window) | 0 | none: the windows reveal them | |
| Web edge (4 px) | 0 | Trim end 0 → 1, f8–56, S curve | settles **f51** |
| Inline labels (30 px) | 58, 62, 66 | 16 px from above, 12 f | Web label settles **f74** |
| Callout dot, stem, text | 70, 74, 80 | dot scale 0 → 1 (expo); stem trim 8 f; text rises | text settles **f88** |

Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0; the three masks survive extraction and placement (full-frame looks at f24 and f40). Text-gap audit: closest 13.0 px (callout text / its stem).

## Steps
1. New data: edit `LAYERS` (bottom first) and `MONTHS` in `ai/scripts/motion/data_viz_lab3.py`; keep the axis max (40) above the top total.
2. After writing the project: `property.set {id:<layer>, key:"mask", value:{"ref":"<window id>"}}`, then `parent.clear {ids:[window, layer]}` when the window must move independently, for each of the three pairs.

## Pitfalls
- One window per layer, all on one timing. The `mask` key with one window and several layers was not tried.
- Each layer is drawn between its own base and top, not from zero, so the stack is honest and the layers do not overlap.
- The callout says "Web passes iOS" because the Web layer becomes thicker than the iOS layer in September; check the claim against the numbers when the data changes.
- Lint does not see masks ([KI-133](../references/known-issues.md#ki-133)); judge the reveal with a look.

Inspiration: stacked area charts in product and market reports. No external text or code was used.
