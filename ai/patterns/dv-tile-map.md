# Tile-grid map

**Template** `dv_tile_map` (Library name "Tile-grid map") · Data Viz pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `DV Tile map` in `categories/data-viz/dv-lab-3`.

For briefs like "by state", "a map of the results", "which regions lead". 51 equal 76 px tiles (50 US states and DC) in an approximate geographic grid, each filled to one of five value bins (share of homes with rooftop solar, sample data), with a legend and the top value ringed. Equal tiles give every state the same weight, which a geographic map does not. 150 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Tiles (track grey) and state codes (SemiBold 28 px) | 4 + column + row (diagonal sweep from the north-west) | scale 0.6 → 1, 10 f, expo; opacity in 4 f | AK settles **f11**, FL **f26** |
| Value fill | 34 + 2·column + row (west to east) | Colour track → bin colour, 8 f, decelerating arrival cubic-bezier(0.333, 0.667, 0.667, 1); codes on the two brightest bins turn dark | AK **f42**, FL **f65** |
| Legend (5 swatches) | 60–74 | opacity in | |
| Top ring | 84 | scale 1.3 → 1, 12 f, expo | settles **f92** |
| Top note ("Highest: Hawaii, 21%") | 88 | 16 px from above | settles **f96** |

Lint 0 errors, 0 warnings, 0 notes. Placed into a fresh comp: lint 0/0/0. Text-gap audit: the 51 flags are each state code on its own tile (intended); every code clears its neighbours.

## Steps
1. New values: edit `SOLAR` and `BINS` in `ai/scripts/motion/data_viz_lab3.py`; the bin, fill and code colour are computed. Move the ring and the note to the new top value.
2. Another country: replace `TILES` (row: [(code, column)]) with that country's grid. For real borders use the map tools ([maps](../references/maps/maps.md)).

## Pitfalls
- **Shape fill colour is keyframeable** (`shape_fill.color`): the bloom is a colour key on the same tile, not a second tile on top.
- The bins are sequential (dark to cyan), one hue: a choropleth of one measure should not use the series colours.
- The tile grid is a layout convention, not geography; say "by state" in the title so no one reads distances into it.

Inspiration: tile-grid maps in election and census graphics. No external text or code was used.
