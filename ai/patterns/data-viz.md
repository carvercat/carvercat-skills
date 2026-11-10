# Data Viz pack (`dv_`)

Charts in motion: spring bars, data-point pops, a line chart that draws itself, a donut that fills clockwise, ranked bars, a gauge, a column chart, a stacked bar, progress rings, comparison bars, a timeline, a waffle chart, an area chart and a data table. Round 3 adds a conversion funnel, a bubble chart, a bar chart race, a stacked area chart, a tile-grid map, an icon array and a calendar heatmap.

The pack lives in `library/templates/data-viz/`. Install it as in [Installing a pack](README.md#installing-a-pack). It adds to Motion Patterns (Grow up (Y), Grow across (X), Bar chart - grow) and to the essentials' Bar chart, Progress and Stat card.

- The presets are built by `ai/scripts/motion/build_data_viz_pack.py`.
- The templates are extracted with `comp_to_template.py` from `categories/data-viz/dv-lab/project.carverproj` (written by `ai/scripts/motion/data_viz_lab.py`) and, for round 2, `categories/data-viz/dv-lab-2/project.carverproj` (written by `ai/scripts/motion/data_viz_lab2.py`), and for round 3, `categories/data-viz/dv-lab-3/project.carverproj` (written by `ai/scripts/motion/data_viz_lab3.py`).
- The sample film is `categories/data-viz/dv-showcase`, written by `ai/scripts/motion/data_viz_showcase.py`.

**Status: Verified 0.1.8.4 (rev 1130; headless, isolated folders, `ai/scripts/motion/verify_pack.py`).** This is the build the harness report states (displayVersion 0.1.8.4, version 0.1.9-dev.4, rev 1130), run on 2026-11-08; it replaces the 0.1.6 verification. All 19 templates of the pack were regenerated as carvercat/2 by the design-unit lab scripts and checked:
- Each template was placed in a fresh 16:9 and a fresh 9:16 comp: lint 0/0/0 and no flashes in qc, on all 19.
- Each template was compared with its v1 original at 7 frames (silhouette difference at most 2 %; colours are now exact hex, a known and intended shift) and object by object (every object present, text identical, ink and box within 16 px): 19 of 19 pass.
- The lab comps lint 0 errors on 0.1.8.4. Their warnings come from `--lab` lint, which resizes the comps to 320 × 180 and so over-reports; the placed templates are the reference (0/0/0).
- Settle and start frames quoted on the pages below are the authored key frames, unchanged by the conversion (the 7-frame comparison with v1 confirms the motion); they were measured on 0.1.6 and not re-measured one by one.
- The sample projects (labs, showcase, showcase-2) are rebuilt as carvercat/2 by `regen_pack.py` and `regen_showcase2.py`; a second run leaves `git status` unchanged.

**Fonts:** the templates use Rethink Sans, which must be installed on the machine. It is a free Google Font (SIL OFL), and the file is in `ai/scripts/motion/json_author/RethinkSans.ttf`. Without it, text falls back to Arial ([KI-136](../references/known-issues.md#ki-136)). Check with `carvercat_authoring mode:validate` `font_exact`.

Style: data. Slate ground `#0F1420`, ink `#E8ECF4`, muted `#7C8599`, gridlines `#252C3B`. Series colours: cyan `#3FB8F0`, amber `#F59E0B`, green `#34D399`, pink `#F472B6`. Highlight one series and grey the rest (`#3A4458`). Rethink Sans.

## Presets (3)

| Name in Library | File | Anchor / frames | What moves | Measured | Use for |
|---|---|---|---|---|---|
| Bar grow up - spring | dv_bar_grow_spring | in / 20 | scale Y 0 → 1, gentle spring | **4.4% overshoot, settles f18** | columns; set `transformOrigin "50% 100%"` first (stored anchor [0, −1]) |
| Bar grow across - spring | dv_bar_grow_across_spring | in / 20 | scale X 0 → 1, gentle spring | **4.4% overshoot, settles f18** | horizontal bars; set `transformOrigin "0% 50%"` first (stored anchor [−1, 0]) |
| Data point pop | dv_point_pop | in / 12 | scale 0 → 1, bouncy spring, fade 0–25% | **16.2% overshoot, settles f11** | chart markers; start each clip on the frame the line reaches it |

## Templates (19)

| Pattern | File / doc | Length |
|---|---|---|
| Line chart - draw | dv_line_chart / [dv-line-chart.md](dv-line-chart.md) | 90 f |
| Donut - fill | dv_donut / [dv-donut.md](dv-donut.md) | 90 f |
| Ranked bars | dv_ranked_bars / [dv-ranked-bars.md](dv-ranked-bars.md) | 90 f |
| Gauge | dv_gauge / [dv-gauge.md](dv-gauge.md) | 75 f |
| Column chart | dv_column_chart / [dv-column-chart.md](dv-column-chart.md) | 90 f, columns settle f26–46 |
| Stacked bar | dv_stacked_bar / [dv-stacked-bar.md](dv-stacked-bar.md) | 90 f, segments settle f16–40 |
| Progress rings | dv_progress_rings / [dv-progress-rings.md](dv-progress-rings.md) | 90 f, rings settle f25–37 |
| Comparison bars | dv_before_after / [dv-before-after.md](dv-before-after.md) | 90 f, badge settles f58 |
| Timeline | dv_timeline / [dv-timeline.md](dv-timeline.md) | 120 f, axis f6–60 |
| Waffle chart | dv_waffle_chart / [dv-waffle-chart.md](dv-waffle-chart.md) | 90 f, cells f4–40 |
| Area chart (masked reveal) | dv_area_chart / [dv-area-chart.md](dv-area-chart.md) | 90 f, reveal f8–50 |
| Data table | dv_data_table / [dv-data-table.md](dv-data-table.md) | 120 f, highlight f56–70 |
| Conversion funnel | dv_funnel / [dv-funnel.md](dv-funnel.md) | 150 f, bars f6–47, takeaway f66 |
| Bubble chart | dv_bubble_chart / [dv-bubble-chart.md](dv-bubble-chart.md) | 150 f, bubbles f14–58, label f64–76 |
| Bar chart race | dv_bar_race / [dv-bar-race.md](dv-bar-race.md) | 220 f, re-ranks f60, f112, f164 |
| Stacked area chart | dv_stacked_area / [dv-stacked-area.md](dv-stacked-area.md) | 150 f, reveal f8–56 (masks) |
| Tile-grid map | dv_tile_map / [dv-tile-map.md](dv-tile-map.md) | 150 f, fill f34–66, top value f84 |
| Icon array | dv_icon_array / [dv-icon-array.md](dv-icon-array.md) | 120 f, highlight f36–69, stat f70 |
| Calendar heatmap | dv_heatmap / [dv-heatmap.md](dv-heatmap.md) | 150 f, squares f6–32, best week f52–74 |

Template clip ids carry the prefixes `dlc_`, `ddn_`, `drb_`, `dgg_` (round 1) and `dcc_`, `dsb_`, `dpr_`, `dba_`, `dtl_`, `dwf_`, `dac_`, `ddt_` (round 2) and `dfn_`, `dbc_`, `drc_`, `dsa_`, `dcm_`, `dia_`, `dhm_` (round 3); no two templates in the skills library share one.

Round 2 (8 templates) was built and verified the same way on 2026-10-27: every lab comp lints 0 errors / 0 warnings / 0 notes, and each template placed into a fresh comp lints 0/0/0. Round 2 also uses Pop - gentle and Zoom settle from the Motion Patterns presets in the bundled essentials; the motion is baked into the templates as keys.

## Round 3: briefs the pack could not serve before

Chosen from [reading a brief](../references/craft/reading-a-brief.md) ("quarterly / annual numbers, KPIs") and the wiki's [data stories](../../wiki/genres/data-stories.md) and [infographics](../../wiki/genres/infographics.md) pages (funnels, rankings over time, maps, icon counts). Built on 0.1.6 (rev 1105) on 2026-10-28; re-verified on 0.1.8.4 (rev 1130) on 2026-11-08. Every move is baked as keys in `data_viz_lab3.py` (no presets to apply; the stacked area's three masks are made with `mask.make`). Every easing lands with **0% overshoot** (serious data, [data stories](../../wiki/genres/data-stories.md)). Every number is sample data and each template says "Sample data" on screen. Frames below are comp frames.

| Template | Brief it serves | Measured | Lint (lab) | Placed |
|---|---|---|---|---|
| Conversion funnel | checkout / sales funnel, "where we lose people" | bars f15–47, values by f56, takeaway f74 | 0 / 0 / 0 | 0 / 0 / 0 |
| Bubble chart | two measures and a size, competitor map | bubbles f22–58, context dims f69, label f76 | 0 / 0 (9 notes) | 0 / 0 / 0 |
| Bar chart race | ranking over years, leaderboard | build f4–32; re-ranks of 20 f at f60 / f112 / f164, last settles f182 | 0 / 0 (83 notes) | 0 / 0 / 0 |
| Stacked area chart | mix over time, users by platform | masked reveal and edge settle f51; labels f74; callout f88 | 0 / 0 / 0 | 0 / 0 / 0 |
| Tile-grid map | results by state or region | tiles f11–26; value fill f42–65; top value f96 | 0 / 0 / 0 | 0 / 0 / 0 |
| Icon array | "1 in 4 people", survey share | icons f11–32; highlight f69; stat f79 | 0 / 0 / 0 | 0 / 0 / 0 |
| Calendar heatmap | daily activity, habit, streak | squares f11–32; best-week outline f67, note f74 | 0 / 0 / 0 | 0 / 0 / 0 |

Notes are all `repeated_key_value` (held values between keys, intended). Each template was also checked with the text-gap audit (`audit_text_gaps.py`): no tight pairs except the tile map's 51 state codes, each inside its own tile (intended). Bar chart race and Stacked area chart move inside their instance; full-frame looks of the placed instances (race f66–176, reveal f24 and f40) show nothing cut ([KI-144](../references/known-issues.md#ki-144)).

### Round-3 pitfalls
1. **Lint checks `text_overlap` while texts move, at any opacity above 0.** Bar race names dimmed to 0.5, 0.3 and 0.15 as they crossed still raised four warnings; only 0 cleared them. Hide crossing labels for the middle of the move ([dv-bar-race.md](dv-bar-race.md)).
2. **Keys must stay inside the clip** (`key_outside_clip` is an error). A text that fades out at the start of a move cannot carry the move's end key; end its clip as it fades.
3. **Reading time applies to every value text on a hold:** 3 digits want 25 opaque frames, so a race hold is at least 28 f plus the fades.
4. **`inspect curves` overshoot is measured against the last key, not the easing.** A value that goes up and then down (Midtown 520 → 540 → 498) or an opacity that steps back (0.9 → 0.55) reports 8–64% "overshoot" with no spring. Read the keys before calling it a spring.
5. **Colour is keyframeable on shapes too** (`shape_fill.color`): a choropleth fill or an icon highlight is a colour key on the same object, not a second object on top.
6. **Size bubbles by area** (diameter ∝ √value), and keep one fixed scale through a race; anything else misstates the data.
7. **The text-gap audit counts a label inside its own small shape** (a tile code) as a negative gap. Check that each flag is a label on its own shape before acting on it.

## Sample film

`categories/data-viz/dv-showcase` is a 345 f (11.5 s) master: line chart → ranked bars → donut → gauge, with a 3% push on the line chart and bars instances. Lint: 0/0/0.

`inspect qc` reports "freeze" over the line-chart scene (f0–89) and the bars' hold. Its analysis render is 96 px wide by default, and at that width a 6 px line drawing and a 3% push do not register. The look shows the motion. A wider qc render (`width` up to 480) may catch it; that was not tried.

## Measured geometry facts (0.1.6)

- **An ellipse's stroke path starts at 3 o'clock and runs counter-clockwise.**
  - `trimEnd` 0% → 25% draws 3 → 12 o'clock, and 0% → 50% draws 3 → 12 → 9.
  - For a clockwise share [a, b] starting at 12 o'clock, rotate the ellipse **90°** (`rotate` −90, stored +90°) and trim from `(1 − b) × 100%` to `(1 − a) × 100%`.
- **Rotation is positive counter-clockwise.** A needle drawn pointing right (0°) at 180° points left; animating 180° → 50.4° sweeps it over the top.
- Trim Stroke on a polyline is proportional to path length. The line chart times each point with the inverse of its ease (`t_for_progress` in `data_viz_lab.py`).

## Data-motion rules used here

- **Let numbers land after their shape.** A value next to a spring bar appears 18 f after the bar starts. At 4.4% overshoot a 920 px bar passes its end by 40 px, which would run into the label.
- **Stagger series 4 f apart** (bars), and **14–16 f apart** (donut segments), so each value is read separately.
- **Axis labels at 28 px or more.** At 22 px, digits measure about 16 px tall and lint flags them (minimum 18 px).
- Build up in reading order: grid, then data, then highlight value.

## Round-2 sample film

`categories/data-viz/dv-showcase-2` is a 780 f (26 s) master at 1920 × 1080 that plays every round-2 template back to back, placed from the Library with `library.place` + `template.apply` (rebuild: `ai/scripts/motion/recipes/showcase2.py data-viz`). Verified 0.1.8.4 (rev 1130), 2026-11-08, rebuilt as carvercat/2 by `regen_showcase2.py`: master lint 0 / 0 / 0. `qc` (240 px) notes the long holds as freezes (fine for a hold).

Inspiration: common data-storytelling motion conventions. No external text or code was used.
