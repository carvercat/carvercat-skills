# Futuristic HUD pack (`fh_`)

Sci-fi interface motion: flicker-on, scan open, CRT power-down, a targeting reticle, corner brackets with a scan line, a typed data readout and a radar sweep. Round 3 adds a biometric scan, drone telemetry, a boot sequence, a holographic turntable in faux 3D, a mission briefing, a voice waveform, a satellite orbit tracker and a warning cascade. For tech launches, gaming, security, space, health tech and data-heavy explainers.

The pack lives in `library/templates/futuristic-hud/`. Install it as in [Installing a pack](README.md#installing-a-pack).

- The presets are built by `ai/scripts/motion/build_futuristic_hud_pack.py`. Its `hold()` helper writes stepped keys (easing Hold) for flickers.
- The templates come from `categories/futuristic-hud/fh-lab`, written by `ai/scripts/motion/futuristic_hud_lab.py`; round 2 from `fh-lab-2` (`futuristic_hud_lab2.py`) and round 3 from `fh-lab-3` (`futuristic_hud_lab3.py`).
- The sample reel is `categories/futuristic-hud/fh-showcase`.

**Status: verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test).**
- Public release binary, headless, isolated folders; the pack was added to a scratch copy's bundled Library ([FR-036](../references/known-issues.md#fr-036)).
- Lint was 0 errors and 0 warnings on every lab comp and the preset bench, and 0/0/0 on the showcase.
- `inspect qc` at 240 px found **no flashes** on the flicker presets or any lab comp.
- Each template was placed into a fresh comp: lint 0/0/0 for all four.

**Fonts:** Rethink Sans must be installed ([KI-136](../references/known-issues.md#ki-136)). The app's bundled JetBrains Mono would suit readouts, but text cannot use bundled fonts today (FR-037).

Style:
- Near-black `#05080F`, cyan `#35E0FF` with a Glow (amount 0.45–0.6, never above 0.8), amber `#FFB020` for alerts.
- Dim cyan `#0E6F86` is for lines and frames only: as text it measures **2.5:1** (lint `contrast:true`, 26 px SemiBold). Round 3 labels use `#4FA8BF` (7.3:1 nominal), alerts `#FF6B5E`, OK states `#3FD08A`, all of which pass lint at 4.5:1.
- Thin strokes (3–5 px), wide-tracked SemiBold caps.
- Everything that keeps moving moves one way: rotations, sweeps, scans.

## Presets (3)

Measured on a 30 f clip that starts at frame 10.

| Name in Library | File | Anchor / frames | What moves | Measured | Use for |
|---|---|---|---|---|---|
| Flicker on | fh_flicker_on | in / 12 | stepped opacity 0 → 80 → 15 → 90 → 50 → 100% (Hold keys, 2 f apart) | fully on at **f10**; qc: no flash | labels, icons, panels switching on |
| Scan open (Y) | fh_scan_open | in / 14 | scale Y 2% → 100% (expo), fade 0–20% | settles **f10** | panels, rings, video windows |
| Power down | fh_power_down | out / 12 | scale Y → 2% (accelerating, 6 f), then scale X → 0 (6 f) | line at **−7 f**, point at **−1 f** from the clip end | the CRT switch-off exit |

## Templates (4)

| Pattern | File / doc | Length |
|---|---|---|
| Targeting reticle | fh_reticle / [fh-reticle.md](fh-reticle.md) | 90 f |
| Corner brackets scan | fh_brackets / [fh-brackets.md](fh-brackets.md) | 75 f |
| Data readout | fh_readout / [fh-readout.md](fh-readout.md) | 100 f |
| Radar sweep | fh_radar / [fh-radar.md](fh-radar.md) | 120 f |

## Templates added in round 2 (8)

| Pattern | File / doc | Length |
|---|---|---|
| HUD ID lower third | fh_id_lower_third / [fh-id-lower-third.md](fh-id-lower-third.md) | 150 f, exit in the last 12 f |
| Segment loader | fh_loader / [fh-loader.md](fh-loader.md) | 130 f |
| Hex grid (background) | fh_hex_grid / [fh-hex-grid.md](fh-hex-grid.md) | 120 f |
| Signal bars | fh_signal_bars / [fh-signal-bars.md](fh-signal-bars.md) | 120 f, stepped |
| Target lock | fh_target_lock / [fh-target-lock.md](fh-target-lock.md) | 90 f |
| Alert banner | fh_alert_banner / [fh-alert-banner.md](fh-alert-banner.md) | 120 f |
| Map ping | fh_map_ping / [fh-map-ping.md](fh-map-ping.md) | 120 f |
| Scan wipe (transition) | fh_scan_wipe / [fh-scan-wipe.md](fh-scan-wipe.md) | 30 f, cut at f14 |

Round 2 was built and verified the same way on 2026-10-27: every lab comp lints 0 errors / 0 warnings, `inspect qc` at 240 px found no flashes, and each template placed into a fresh comp lints 0/0/0. Clip-id prefixes: `fid_`, `fld_`, `fhx_`, `fsg_`, `ftl_`, `fal_`, `fmp_`, `fsw_`. Lab: `categories/futuristic-hud/fh-lab-2`, written by `ai/scripts/motion/futuristic_hud_lab2.py`.

## Round 3: briefs the pack could not serve before

Chosen from [reading a brief](../references/craft/reading-a-brief.md) ("tech product, game, security, sci-fi teaser") and the wiki's [UI and UX demos](../../wiki/genres/ui-ux-demos.md), [product launches](../../wiki/genres/product-launches.md), [explainers](../../wiki/genres/explainers.md) and [event openers](../../wiki/genres/event-openers.md) pages, against what rounds 1 and 2 already cover (the radar sweep exists, so it was not rebuilt). Built and verified on 0.1.6 (rev 1105) on 2026-10-28. Every move is baked as keys in `futuristic_hud_lab3.py` (no presets to apply): `flick()` writes the Flicker-on steps as Hold keys and `type_on()` types a text 1 f a character. Faux 3D is computed in the script and baked every 2 f. Every readout passes lint `contrast:true` at 4.5:1 (the [wiki audit](../../wiki/design/contrast.md) found HUD readouts near 2.6:1). Names, numbers and places are sample copy; the body, map and planet are shape stand-ins. Frames are comp frames. Clip-id prefixes: `fbs_`, `ftm_`, `fbt_`, `fho_`, `fmb_`, `fvw_`, `fob_`, `fwc_`.

| Template | Brief it serves | Measured | Overshoot | Lint (lab, contrast:true) | Placed |
|---|---|---|---|---|---|
| Biometric scan ([fh-bio-scan.md](fh-bio-scan.md)) | health tech, medical device, wearable, medbay | beam f18–78 at 9 px/f, gone f86; heart ping f50, settles f60; ECG f20–110, pen fades f116; vitals from f56; status on f96 | keyed pops 115% | 0 / 0 (6 notes) | 0 / 0 / 0 |
| Drone telemetry ([fh-telemetry.md](fh-telemetry.md)) | drone footage overlay, FPV, vehicle telemetry | horizon draws by f9; bank −9° (f50), +4° (f95), level f125; pitch settles f135; heading 042 → 056 → 071 (f60, f105); values on f24 | 0% | 0 / 0 (2 notes) | 0 / 0 / 0 |
| Boot sequence ([fh-boot-sequence.md](fh-boot-sequence.md)) | power on, game intro, initialising | 6 lines from f8, 13 f apart; OKs f22–90; progress full f90; mark drawn f96; SYSTEM ONLINE on f110 | 0% | 0 / 0 (1 note) | 0 / 0 / 0 |
| Holo turntable, faux 3D ([fh-holo-turntable.md](fh-holo-turntable.md)) | product reveal, hologram, 360° view | one full turn in 150 f (loops); 12 edges + 8 corners baked every 2 f; edges on f10–24; scan line f30–81; callout on f36 | 0% (baked lanes read 46–49%, KI-152) | 0 / 0 (45 notes) | 0 / 0 / 0 |
| Mission briefing ([fh-mission-briefing.md](fh-mission-briefing.md)) | game mission intro, campaign briefing | panel f8; route f40–67; target settles f76, pings f70/100/130; objectives f48–72; deploy time on f110 | keyed pop 120% | 0 / 0 / 0 | 0 / 0 / 0 |
| Voice waveform ([fh-voice-waveform.md](fh-voice-waveform.md)) | AI voice assistant, voice command, audio | waves slide one way f0–149; height 35% → 100% (f24) … 35% (f122); line types from f30; confirm on f120 | 0% | 0 / 0 (3 notes) | 0 / 0 / 0 |
| Orbit tracker ([fh-orbit-tracker.md](fh-orbit-tracker.md)) | satellite launch, space, GPS / telecom coverage | planet f8; orbit draws f4–28; meridians turn 180° per clip (loops); satellite on f20, hidden behind the planet until f122; signal on f40 | 0% (baked lanes misread, KI-152) | 0 / 0 / 0 | 0 / 0 / 0 |
| Warning cascade ([fh-warning-cascade.md](fh-warning-cascade.md)) | hacked, overload, malfunction, game over | windows f4–36, 9 f apart; banner settles f63; text on f64, dips f90–98 | 0% | 0 / 0 / 0 | 0 / 0 / 0 |

Notes are `repeated_key_value` on holds (the turntable's edges hold 0% before they switch on) and `speed_jump` where the scan beam stops and the progress fill steps; intended. `inspect qc` at 240 px found no flashes on any round-3 comp (the mission briefing's hold reads as a freeze). Each template was checked with the text-gap audit (`audit_text_gaps.py`): no flags; the closest pair is 16 px (telemetry, REC / its dot). Full-frame looks of every placed template at its widest moving frame and its last frame show nothing cut ([KI-144](../references/known-issues.md#ki-144)). The waveform's masks and the telemetry's parented ladder survive placement.

### Round-3 pitfalls
1. **Readouts need their own colour.** The pack's dim cyan as text measures 2.5:1; use it for lines and frames, and `#4FA8BF` or brighter for labels. Convert text colours with the renderer's BT.709 curve, not `cc.lin` ([KI-141](../references/known-issues.md#ki-141)).
2. **Wide-tracked caps are much wider than they look.** "BIOMETRIC SCAN" at 40 px with tracking 1.4 is 664 px wide. Readout columns, objectives and headers ran into each other or past their panel in the first build; lint reported one of four (it has no check for text leaving its panel, [KI-157](../references/known-issues.md#ki-157)). Measure with `carvercat_authoring geometry` and run the text-gap audit.
3. **Faux 3D: bake it.** A turning box is 12 thin rectangles whose midpoint, angle, length (scale x) and depth opacity are computed every 2 f; unwrap a line's angle by 180°. Globe meridians are ellipses whose width is 2R·\|sin φ\|. A dot goes "behind" a shape with Hold opacity at the computed crossings.
4. **Scale y thins a stroke too.** A wave squashed to 8% drew as broken dashes; keep a stroked shape's squash at 35% or more, or animate its geometry instead.
5. **Readings that change need reading time.** A value clip on screen under 25 f fails `reading_time`; step numbers at 40 f or slower.
6. **`inspect curves` overshoot is meaningless on baked lanes** (46–953% here, [KI-152](../references/known-issues.md#ki-152)); quote keyed peaks instead.
7. **One-way motion still holds**: the turntable turns, the meridians turn, the waves slide and the base arc runs, each one way at constant speed, so the turn and the meridians loop at the clip end.

## Sample reel

`categories/futuristic-hud/fh-showcase` is a 385 f (12.8 s) master: brackets scan → data readout → radar sweep → targeting reticle. Lint 0/0/0. QC at its default 96 px reports "freezes" over the thin-line scenes. At 240 px the individual comps show none.

## Round-2 sample film

`categories/futuristic-hud/fh-showcase-2` is a 850 f (28 s) master at 1920 × 1080 that plays the round-2 templates back to back with Scan wipe on one cut, placed from the Library with `library.place` + `template.apply` (rebuild: `ai/scripts/motion/recipes/showcase2.py futuristic-hud`). Verified 0.1.6 (rev 1105), 2026-10-28: master lint 0 / 0 / 0. Qc (240 px) notes two holds as freezes and no flashes.

## Pitfalls and techniques (0.1.6)

1. **A pie slice from a stroke:** an ellipse whose stroke width equals its diameter covers the whole disc. Trim it to a share (here 0.07) to get a wedge. Use **butt caps**: round caps turn the slice into a blob.
2. **Clockwise sweeps:** rotation is positive counter-clockwise, so a clockwise radar uses negative rotation (−360° per 60 f). A blip at math angle θ is passed at ((360 − θ) mod 360) / 360 × period frames.
3. **Dashed rings:** `shape.stroke` Line = dashed with dash and gap lengths, plus a one-way rotation, makes a scanning ring with no extra objects.
4. **Keep crosshairs off labels:** lint does not report a thin line crossing text, but the look does.
5. **Power down is for shapes.** On text it fails lint `text_too_small` (it squeezes the line to 2%); give text Exit fade - fast.
6. **Digital meters step.** Hold keys give stepped levels with no in-betweens; a smooth up-and-down meter risks lint `jitter`.
7. **`cc.ngon` always fills;** call `nofill()` for outlines.

Inspiration: common sci-fi HUD and interface conventions. No external text or code was used.
