# Map animation

Read this for location videos: country/emirate maps, zoom-to-location, pin drops, routes, distance/drive-time callouts, catchment rings, masterplan reveals. Carvercat has no map tiles or globe — maps are **native editable paths built from real geography** Verified 0.0.72 in the lab project (`categories/motion-patterns/pattern-lab/`):
- `MAP UAE emirates` — 7 emirates drawn on from Natural Earth, Dubai fill bloom, pin pop + pulse ring, dashed route Dubai → Abu Dhabi, drive-time label.
- `MAP Dubai base` — city explainer: sea + land, 11 highways drawn on with Trim (staggered), project pin + pulse, 5/10 km catchment rings, glowing hero route, 3 landmark pop-up cards with leader lines, callout + arrow.
- `MAP Dubai zoom` — the base comp as an instance with a camera: push in ×1.9 on the project, hold, pull out to reveal the landmarks, fade out.

## 1. Geography → paths (`ai/scripts/maps/geo_paths.py`)
```
python geo_paths.py ne_10m_admin_1_states_provinces.geojson uae.json --where adm0_a3=ARE \
   --proj local --box 260,140,1400,800 --tol 2 --min-area 300 \
   --rename "Dubay:Dubai;Fujayrah:Fujairah" --pins "Burj Khalifa:55.2744,25.1972;DXB:55.3657,25.2532"
```
Output: per feature the simplified rings in comp pixels, a **label anchor (pole of inaccessibility, not the centroid)**, bbox, pins in pixels, and ready `carvercat_batch` steps (one closed `object.path` per ring, largest first). Paste the steps (≤ 256 per batch), then style. For the UAE: 16 rings / 401 points at tol 2 px.
Ready-made (1920×1080): `ai/scripts/maps/data/uae_emirates_1920x1080.json` (local projection) and `western_asia_countries_1920x1080.json` (Equal Earth, 17 countries). Re-run the script for other boxes/aspects (9:16: `--comp 1080x1920 --box 61,268,955,1270`).

| Source (all public domain unless noted) | Use |
|---|---|
| Natural Earth `ne_110m_admin_0_countries` (0.8 MB) | world/globe shots |
| `ne_50m_admin_0_countries` (3 MB) | regions (GCC, Middle East) |
| `ne_10m_admin_1_states_provinces` (41 MB) | **the only NE file with UAE emirates**; names "Dubay"/"Fujayrah" → rename; has 2 "Neutral Zone" features — drop or merge |
| world-atlas TopoJSON (ISC) | shared border arcs (draw each border once) |
| geoBoundaries (licence per country; UAE ADM1 = ODbL) | admin areas NE lacks — needs attribution |
| OpenStreetMap (ODbL) | roads, coastline detail, communities — **"© OpenStreetMap contributors" on screen long enough to read + in credits/description** |
Base URL: `https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/`. Natural Earth shows de-facto borders; check disputed areas before broadcast.

Roads and other lines: `ne_10m_roads` (Natural Earth, 50 MB, motorways/primary only at city scale) — LineStrings become open paths. Use `--bbox lon0,lat0,lon1,lat1` to keep and clip lines to the area, `--fit-bbox` to frame exactly that area (instead of the whole feature, e.g. Dubai without Hatta), and `--fit-from base.json` to reuse another output's projection so roads/pins overlay the land exactly:
```
python geo_paths.py ne10a1.geojson dubai.json --where name=Dubay --proj local --fit-bbox 54.95,24.85,55.6,25.4 \
   --pins "Project site:55.24,25.06;Burj Khalifa:55.2744,25.1972;Dubai Marina:55.1404,25.0805;DXB Airport:55.3657,25.2532"
python geo_paths.py ne10roads.geojson dubai_roads.json --bbox 54.95,24.85,55.6,25.4 --fit-from dubai.json --tol 1.5
```
OpenStreetMap detail (Overpass) is often blocked from sandboxes; if you can fetch an OSM extract, it goes through the same script — and needs the OSM credit on screen.

Projections: `equal_earth` (world/region, honest areas), `mercator` (to match web/satellite plates; city scale), `local` (equirectangular × cos(lat0): community/city/emirate scale — indistinguishable from Mercator under ~50 km).

## 2. Styling (verified look)
- Base: very dark navy background [0.004,0.009,0.02]; land a step lighter [0.02,0.035,0.06]; borders thin (0.0012 W) low-contrast [0.25,0.32,0.42]. Land/water 5–10 % apart in brightness.
- ONE accent for the story (the highlighted emirate, the route, the hero pin). Labels: uppercase, bold, tracking 1.15, ≥ 28 px at 1080p (≥ 36–48 px for 9:16); secondary labels grey.
- Glow only on the hero (pin or route), within the [glow limits](../effects/glow.md).

## 3. Shot recipes (timings at 30 fps)
| Shot | Build | Timing |
|---|---|---|
| **Border draw-on** | Trim effect on every path, end 0 → 1 S-curve; stagger each ring 2 f, mainland first | 40 f per ring (~1.3 s); constant per item, don't scale with border length |
| **Region highlight / fill bloom** | key `shape.fill.color` base → accent (Ease out) after its border completes; optional opacity overshoot | 14 f; label rises 0.7 s later (`Rise - expo`) |
| **Pin drop** | white dot `Pop - spring` + pulse ring (stroke ellipse, size 0.5 → 3, opacity 1 → 0, Ease out) | pin 12–24 f, ring 24 f, 1–2 rings |
| **Route** | open `object.path` (3–6 points, `smooth:true`), stroke round cap, dashed 0.006/0.005, Trim end 0 → 1 S-curve; destination pin pops when it arrives | 1–1.5 s local, 3–6 s long-haul; hold 0.3–0.5 s either side |
| **Drive-time / distance label** | text after the route lands, `Words rise - expo`, seated with `authoring.place_bounds` clear of the line; say "approx." and the basis | holds ≥ 2 s |
| **Catchment rings** | concentric stroke ellipses at real distances (km → px with the script's transform scale; in Mercator divide by cos(lat)), grow 0 → 1 staggered 5–8 f, label on the ring edge | 0.6–1 s each |
| **Zoom to location** | build the map in its own comp; place the instance, key its scale and position (scale in LOG space: equal ratios per frame), keep the target centred; cross-fade to a detailed comp at the end | 3–5 s, ease in-out (0.645, 0.045, 0.355, 1) |
| **Leader-line label** | dot → short line draw (trim 10 f) → text rise | 0.3 s + 0.3 s |
| **Masterplan reveal** | map at community scale cross-dissolves into the plan registered to the same geography; plots draw on → phase fills wipe → amenity icons pop | 4–8 s |

## 3b. Explainer kit — `ai/scripts/maps/map_overlay.py` (verified, `MAP Dubai base`)
One spec file → batch steps for every explainer element, all in the map comp's pixel space:
```
python map_overlay.py dubai.json spec.json overlay_steps.json      # 212 steps for the Dubai demo
```
| Element | How it is built | Timing used |
|---|---|---|
| **Road draw-on** | each road an open path, stroke 0.0012 W light grey, `trim` end 0→1 S-curve | 36 f per road, staggered 3 f, starts f12 |
| **Hero pin + pulse** | accent ellipse 0.016 W with 0.002 white stroke; pulse = stroke ellipse, `size` 0.5→3 and `blend` 1→0, Ease out | pin f64 (`Pop - spring`), pulse 24 f |
| **Catchment rings** | stroke ellipses, diameter = 2 × km × px/km ÷ W (px/km = transform.scale ÷ 6371; Mercator ÷ cos lat), dashed 0.004/0.004, 60 % alpha; `size` 0→1 Ease out; label above the ring | 22 f, 8 f apart |
| **Hero route** | smooth open path hero → landmark, width 0.003, round cap, trim S-curve, **glow size 12 / amount 0.6** (halo ~30 px, never burns — see [glow](../effects/glow.md)) | 30 f |
| **Landmark pop-up** | white dot (`Pop - spring`) → leader line trim 8 f → white rounded card 0.1 × 0.036 W, radius 0.008 (`Pop - gentle`) → bold name 0.0115 + accent sub-line 0.01 (`Rise - expo`) | +4 / +10 / +12 / +14 f; next landmark 8 f later |
| **Callout + arrow** | bold tracked text; arrow = shaft path with trim + separate 3-point chevron head path (round corners) that fades in as the shaft lands | shaft 10 f, head 3 f |
| **Zoom in / out (camera)** | new comp → `comp.place {comp: <map comp index>, at:0}`; on the instance set `tr.e_tr_placement_<id>.anchor` to the target, then key `.scale` and `.position` (see below) | in 32 f, hold 22 f, out 30 f, S-curve |
| **Out** | instance opacity 1→0 + scale 1→1.06 Ease in over the last 14 f | |

Presets after the batch (one id per `preset.apply` call): pins `Pop - spring`, cards `Pop - gentle`, names/sub-lines/callout `Rise - expo`.

**Camera maths (verified).** On a comp *instance* the anchor is a pure pivot — setting it does NOT shift position to compensate (unlike shapes). With anchor `a` (half-sizes) and position `p`, the target sits at `p + a/2` on screen and stays put while scaling. So:
- wide: `p = [0.5, 0.5]` (map unshifted), anchor = `(target − 0.5) × 2` (target in centre fractions, y up);
- zoomed and centred: key `p = 0.5 − a/2` together with the scale key, back to `[0.5,0.5]` when pulling out.
Example: project at [0.4689, 0.4042] → anchor [−0.0622, −0.1916]; zoom keys scale 1 (f62) → 1.9 (f94) hold → 1 (f146), position [0.5,0.5] → [0.5311,0.5958] → [0.5,0.5]. Vector paths and text inside the nested comp stayed sharp at ×1.9.
Paths are parameter keys: `property.set`/`key.set` with key `tr.e_tr_placement_<instance id>.scale` (value `[x,y]`), `.position`, `.anchor`, `.opacity`; `param.list {id, where:"panel"}` lists them. The short keys (`scale`, `anchor`, `blend`) are refused on instances.

## 4. Real-estate conventions
- Establish → locate → connect → reveal: country/emirate → project pin → landmark distances → masterplan/render.
- "Distance to landmarks": project pin is the hero at/near centre; 4–8 landmarks with "X min"/"X km" pills; reveal nearest first, 6–12 f apart; one unit throughout (Dubai marketing: minutes by car); times from routing, labelled "approx."; straight-line km from the script's haversine only when you say "straight-line".
- Keep "illustrative / artist's impression" on renders; property ads in Dubai carry permit/QR requirements — check the client's compliance team.

## 5. Pitfalls
- Paths with hundreds of points are fine; > 2,000 points per path slows looks — raise `--tol`.
- Large map comps scaled up > 2.5× step their edges: build the detailed comp at the zoomed size instead.
- Children of the map instance (pins/labels) belong INSIDE the map comp so they move with the zoom, or in the parent comp re-projected every key — prefer inside.
- Don't clip borders to the frame; draw full geometry. If you fit to a bbox, make the bbox (or the clip) larger than the frame, or the land shows a straight cut edge in the wide shot (seen on `MAP Dubai base`; hidden once zoomed).
- `text.font.size` has a floor of 0.01 W (≈ 19 px at 1080p) — smaller sizes refuse the whole batch.
- There is no batch arrow command — build shaft + chevron (the script does).
- Creating many objects at once: give every step a `frame`; the batch picks a free track. A batch ending in a refused step rolls back everything — split long builds (base, overlay, presets).
- Never hide provider attribution (OSM, Mapbox, Google Earth imagery must stay credited).

Sources and licences: see [../../SOURCES.md](../../SOURCES.md) (Remotion maps skill — ideas only; Natural Earth; Adobe/AE map tutorials; OSM attribution guidelines).
