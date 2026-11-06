# Colour for motion graphics, in Carvercat

How to choose and apply a palette that reads on screen and stays consistent across a piece. Tool-independent rules first, then the Carvercat controls that do the work.

## Rules

- **Roles, not swatches.** Every palette has five roles:
  - **ground**: the background;
  - **ink**: primary text and marks;
  - **muted**: secondary text, axis labels, captions;
  - **accent**: one colour for the thing that matters;
  - **support**: neutral fills such as tracks, inactive bars and gridlines.
  A second accent is for data series or a single highlight, never decoration.
- **One accent per frame.** If two things are accent-coloured, neither is emphasised. In the packs, the SaaS indigo, kinetic orange, data cyan and corporate teal each appear on one element per beat.
- **Contrast for reading.** Text needs at least 4.5:1 against what is behind it (7:1 for small type over footage), and large display type at least 3:1. Muted text on a dark ground is the usual failure: `#7C8599` on `#0F1420` measures 5.0:1 (WCAG formula), only just above the minimum.
- **Dark grounds are not black.** Use a tinted near-black (`#0B0B0F`, `#0F1420`, `#0B1F3A`) so shadows and glows have somewhere to go and compression does not band.
- **Value before hue.** Squint (or desaturate) the frame: the hierarchy must survive in grey. Give the accent the highest value contrast against the ground, not just the brightest hue.
- **Series colours** in charts: equal lightness and different hue, so no series looks more important by accident. Grey out everything except the series being discussed (the Data Viz ranked bars use `#3A4458` for the rest).
- **Colour moves too.** A colour change is an event. Crossfade it over 8–12 f with an ease (the toggle track), never in one frame unless it is a hard cut on a beat.

## In Carvercat

- **Where colour lives:**
  - shapes: `shape.fill` Colour and Opacity, and `shape.stroke` Colour, Opacity and Width;
  - text: `text.fill` and `text.outline` Colour and Opacity.
  All of these are keyframeable.
- **Gradients:** Paint = gradient, then `Gradient` (stops), `Gradient angle`, `Start`/`End`, `Shape` (linear or radial), `Interpolate`, `Repeat`. The Corporate showcase's footage stand-in is a two-stop navy-to-teal linear gradient. Gradient coordinates are object-local, not comp positions ([../app/creative-controls.md](../app/creative-controls.md)).
- **Values are CSS colours.** Write `"#FF7A00"`, `"rgb(255 122 0)"` or a gradient string; the app converts inside ([../app/design-units.md](../app/design-units.md)). Never write a linear-light array. (The project file stores linear RGB; stored value.)
- **Changing a colour over time:** key the Colour parameter, or, as the SaaS toggle does, crossfade two copies with Opacity keys (more control over the curve, and it keeps each state's exact colour).
- **Whole-layer adjustments:** the Colour effect (`Gain`, `Contrast`). To treat everything below, use an adjustment object.
- **Blend modes** (`transform.compositing` Blend): Screen or Add to brighten (glows, light leaks), Multiply to darken (shadows, paper texture).
- **Checking:** `carvercat_inspect mode:lint` with `contrast: true` renders and measures text contrast against what is actually behind it.

## Palettes used in the verified packs

| Pack | Ground | Ink | Muted | Accent | Support |
|---|---|---|---|---|---|
| SaaS UI | `#0E1020` | `#14151C` on white cards | `#6B7080` | `#5B5BF6` | `#D5D8E0` |
| Kinetic Typography | `#0B0B0F` | `#F4F1EA` | `#9A968E` | `#FF4D2E` (+ `#FFD23F`) | — |
| Data Viz | `#0F1420` | `#E8ECF4` | `#7C8599` | `#3FB8F0` (+ amber, green, pink series) | `#3A4458`, grid `#252C3B` |
| Corporate Brand | `#0B1F3A` / `#F3F5F8` | white / `#0B1F3A` | `#8A94A6` | `#00A3A1` | `#163A63` |
