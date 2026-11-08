# Retro pack (`rt_`)

70s to 80s looks: motion **on twos**, a sunburst title, a synthwave sun over a running grid, rainbow stripes and a checkerboard wipe. Round 3 adds an 80s action title, a mixtape tracklist, a 90s under-construction page, a film countdown leader, a pixel level-up, a 70s TV ident, a polaroid memory and a retro weather map.

The pack lives in `library/templates/retro/`. Install it as in [Installing a pack](README.md#installing-a-pack).

- The presets are built by `ai/scripts/motion/build_retro_pack.py`. Its `twos()` helper samples a curve on even frames and holds between them.
- The templates come from `categories/retro/rt-lab`, written by `ai/scripts/motion/retro_lab.py` (design units through `json_author/cc2.py`: px, y down, degrees clockwise, hex colours; its `twos()` keys a move on every other frame); round 2 from `categories/retro/rt-lab-2` (`retro_lab2.py`); round 3 from `categories/retro/rt-lab-3` (`retro_lab3.py`).
- The sample reel is `categories/retro/rt-showcase`.

**Status: verified 0.1.8.1 (rev 1127).** Round 3 too (2026-10-28).
- Public release binary, headless, isolated folders; the pack was added to a scratch copy's bundled Library ([FR-036](../references/known-issues.md#fr-036)).
- Lint was 0 errors and 0 warnings on every lab comp and the preset bench, and 0/0/0 on the showcase.
- `inspect qc` at 240 px found no flashes in any lab comp.
- Each template was placed into a fresh comp: lint 0/0/0 for all four.

**Fonts:** Rethink Sans must be installed ([KI-136](../references/known-issues.md#ki-136)).

Style:
- 70s: cream `#F4E4C1`, orange, mustard, brown, teal and brick red.
- 80s synthwave: night `#1A0B2E`, hot pink, yellow, purple and cyan, with glow.
- **On twos** is the signature: every pose is held for 2 frames (12 a second), with easing **Hold** arriving at each key.

## Presets (3)

Measured on a 30 f clip that starts at frame 10.

| Name in Library | File | Anchor / frames | What moves | Measured | Use for |
|---|---|---|---|---|---|
| Rise - on twos | rt_rise_twos | in / 16 | y +4% H → 0 on an expo curve, stepped every 2 f; fade on twos over the first 25% | settles **f10**, opaque **f4** | titles, captions |
| Pop - on twos | rt_pop_twos | in / 12 | scale 0 → 1 (gentle spring), stepped | **3.9% overshoot, settles f12** | badges, stickers, stars |
| Exit down - on twos | rt_exit_down_twos | out / 12 | y 0 → +5% H (accelerating), fade over the second half, stepped | the last 12 f | exits |

Lint reports `speed_jump` (info) on stepped moves: that is the point of on twos.

## Templates (4)

| Pattern | File / doc | Length |
|---|---|---|
| Sunburst title | rt_sunburst_title / [rt-sunburst-title.md](rt-sunburst-title.md) | 90 f, full-frame background included |
| Synthwave sun | rt_synthwave / [rt-synthwave.md](rt-synthwave.md) | 120 f, full-frame background included |
| Rainbow stripes | rt_rainbow_stripes / [rt-rainbow-stripes.md](rt-rainbow-stripes.md) | 75 f |
| Checker wipe | rt_checker_wipe / [rt-checker-wipe.md](rt-checker-wipe.md) | 54 f, a transition |

## Templates added in round 2 (8)

| Pattern | File / doc | Length |
|---|---|---|
| 70s stripe lower third | rt_stripe_lower_third / [rt-stripe-lower-third.md](rt-stripe-lower-third.md) | 150 f, exit on twos |
| VHS overlay | rt_vhs_overlay / [rt-vhs-overlay.md](rt-vhs-overlay.md) | 120 f, overlay |
| Groovy badge | rt_groovy_badge / [rt-groovy-badge.md](rt-groovy-badge.md) | 90 f |
| Neon sign | rt_neon_sign / [rt-neon-sign.md](rt-neon-sign.md) | 120 f, steady from f30 |
| Chrome title (static text gradient) | rt_chrome_title / [rt-chrome-title.md](rt-chrome-title.md) | 90 f |
| TV switch-off | rt_tv_off / [rt-tv-off.md](rt-tv-off.md) | 24 f, ending |
| Arcade start screen | rt_arcade_start / [rt-arcade-start.md](rt-arcade-start.md) | 150 f |
| Venetian blinds (transition) | rt_blinds / [rt-blinds.md](rt-blinds.md) | 54 f, cut at f26 |

Round 2 was built and verified the same way on 2026-10-27: every lab comp lints 0 errors / 0 warnings, `inspect qc` at 240 px found no flashes, and each template placed into a fresh comp lints 0/0/0. Clip-id prefixes: `rlt_`, `rvh_`, `rgb_`, `rns_`, `rch_`, `rtv_`, `ras_`, `rbl_`. Lab: `categories/retro/rt-lab-2`, written by `ai/scripts/motion/retro_lab2.py`.

## Round 3: briefs the pack could not serve before

Chosen from [reading a brief](../references/craft/reading-a-brief.md) ("80s night, nostalgia") and the wiki's [title sequences](../../wiki/genres/title-sequences.md), [broadcast packages](../../wiki/genres/broadcast-packages.md), [social ads](../../wiki/genres/social-ads.md) and [broadcast graphics of the 1980s and 1990s](../../wiki/history/broadcast-graphics-80s-90s.md) pages, against what rounds 1 and 2 already cover (sunburst, synthwave, stripes, neon, chrome, VHS, arcade, TV off): the throwback briefs people actually bring (a movie title, a playlist, an old website, a film countdown, a game moment, a channel ident, a family photo, a weather map). Built and verified on 0.1.6 (rev 1105) on 2026-10-28. Every move is baked as keys in `retro_lab3.py`, on twos with Hold: `rise2()` is "Rise - on twos", `pop2()` is "Pop - on twos" and `group2()` moves several parts as one rigid object (shared centre, angle and size, keyed on twos), so there is nothing to apply after `edit.open`. Pops land with the preset's **3.9%** overshoot; slides, rises and the polaroid drop land with 0%. Things that keep moving after they land (reels, rays, the burst, hazard stripes, the orbit dot) move one way at a constant speed. Titles, songs, towns, numbers and the photo are invented stand-ins. Frames are comp frames. Clip-id prefixes: `rat_`, `rmx_`, `ruc_`, `rfl_`, `rlu_`, `rti_`, `rpo_`, `rwm_`.

| Template | File / doc | Brief it serves | Measured | Lint (lab) | Placed |
|---|---|---|---|---|---|
| 80s action title | rt_action_title / [rt-action-title.md](rt-action-title.md) | action-movie title, trailer card, "coming this summer" | title flies in 0.2 → 1 on twos, settles f16 (0%); glint f26–42; tagline f40; release f50; 150 f | 0 / 0 / 2 | 0 / 0 / 0 |
| Mixtape tracklist | rt_mixtape / [rt-mixtape.md](rt-mixtape.md) | mixtape, playlist, tracklist, "side A" | cassette lands f10; reels 6°/f one way; SIDE A f22; tracks f32 to f56, 6 f apart; 150 f | 0 / 0 / 32 | 0 / 0 / 0 |
| Under construction page | rt_under_construction / [rt-under-construction.md](rt-under-construction.md) | 90s website, old-web "coming soon", throwback homepage | bands seamless (240 px per 150 f); headline f14; NEW! f22 (3.9%), blinks every 1.5 s; counter ticks f80 / f120; 150 f | 0 / 0 / 4 | 0 / 0 / 0 |
| Film countdown leader | rt_film_leader / [rt-film-leader.md](rt-film-leader.md) | old film countdown, projector intro | 5-4-3-2, a clockwise sweep per 30 f beat, hard cuts; 120 f | 0 / 0 / 0 | 0 / 0 / 0 |
| Pixel level up | rt_level_up / [rt-level-up.md](rt-level-up.md) | game stream level-up, achievement, new rank | star drawn by f16; LEVEL UP! f24 (3.9%); bar full f44; LV 12 f56; +500 XP f62; 120 f | 0 / 0 / 10 | 0 / 0 / 0 |
| 70s TV ident | rt_tv_ident / [rt-tv-ident.md](rt-tv-ident.md) | channel ident, station bumper, retro logo sting | rings f10 to f22; 7 f36 (3.9%); name f44; tagline f52; orbit dot 3°/f; 150 f | 0 / 0 / 3 | 0 / 0 / 0 |
| Polaroid memory | rt_polaroid / [rt-polaroid.md](rt-polaroid.md) | throwback photo, family memory, "on this day" | drops in as one piece, lands f10 at −4° (0%); develops f20–84; heading f44; line f52; 150 f | 0 / 0 / 10 | 0 / 0 / 0 |
| Retro weather map | rt_weather_map / [rt-weather-map.md](rt-weather-map.md) | retro TV weather, local-news forecast, event "forecast" | header f8; four towns 10 f apart: icon f28–58 (3.9%), tile f32–62; 150 f | 0 / 0 / 15 | 0 / 0 / 0 |

The lab notes are `speed_jump` on the stepped moves (the point of on twos, as in rounds 1 and 2) and one `outside_graphics_safe` while the polaroid's caption is still above the frame. `inspect qc` at 240 px found no flashes in any lab comp. Each template placed into a fresh comp applied "at 1920 x 1080" and linted 0/0/0. The text-gap audit (`audit_text_gaps.py`) flags nothing (closest pair 21.4 px, WEATHER and TUESDAY). Every gradient was checked with a look ([KI-155](../references/known-issues.md#ki-155)): the chrome title has its sky at the top, the sunset glow is dark at the top, the polaroid stand-in has its sky at the top and the web title bar runs navy to light blue left to right. Full-frame looks of the placed instances (the cassette and polaroid entering from outside, the glint and streak at their widest, the hazard bands at f0 and f149, the sparks, the orbit dot) show nothing cut ([KI-144](../references/known-issues.md#ki-144)).

### Round-3 pitfalls
1. **Parts of one object turn about their own centres.** A polaroid's frame, photo and caption each keyed with the same rotation fall apart. `group2()` keys each part's position, rotation and scale from one shared centre on the same even frames, so the group turns and grows as one piece without parenting ([KI-153](../references/known-issues.md#ki-153)).
2. **Constant lanes are notes.** Writing Hold keys for a lane that never changes (scale 1 on every step) gave 48 `repeated_key_value` notes; `group2()` skips such lanes.
3. **Text popping from size 0 can be `text_too_small`.** Lint judges the first stepped frames: a 52 px temperature (15.8 px line) and a 56 px NEW! (17.1 px) were warnings; 150 px and 64 px texts popping the same way passed. Pop small texts from 0.5, or keep them 64 px or larger.
4. **An ellipse stroke runs counter-clockwise from 3 o'clock.** For a clockwise clock-wipe from 12 o'clock turn the shape 90° (`rotate` −90, stored +90°) and key Trim `start` 1 → 0 (keying `end` 0 → 1 swept counter-clockwise).
5. **Scrolling stripes off frame for the whole clip are `never_visible`** (error). `hazard_band()` drops them; a band that moves two stripe periods per comp loops seamlessly.
6. **Two `shadow` effects on one text both render**: a two-step hard extrusion without stacked copies (copies would be `text_overlap`).
7. **Light-ground parts vanish on black.** The mixtape names, the polaroid heading and the level-up colours are drawn for their grounds; check the instance on the real background.

## Sample reel

`categories/retro/rt-showcase` is a 285 f (9.5 s) master: sunburst title → rainbow stripes → (checker wipe, cut under it at f165) → synthwave. Lint 0/0/0.

## Round-2 sample film

`categories/retro/rt-showcase-2` is a 744 f (25 s) master at 1920 × 1080 that plays the round-2 templates back to back with Venetian blinds on one cut, placed from the Library with `library.place` + `template.apply` (rebuild: `ai/scripts/motion/recipes/showcase2.py retro`). Verified 0.1.6 (rev 1105), 2026-10-28: master lint 0 / 0 / 0. Qc (240 px) notes five holds as freezes and no flashes.

## Pitfalls

1. **Overlay comps nested in a master must not carry their lab background.** The first showcase build nested the checker comp with its full-frame cream "Lab bg" and hid the synthwave scene under it. Strip the background, or use the template, which drops it.
2. **A nested clip longer than its comp:** lint did not flag a 86 f instance of a 75 f comp. Keep each instance no longer than its comp.
3. **Perspective grid lines that leave the frame** count as `cropped_at_rest`. End them at the frame edge (the lab computes the intersection).
4. **Horizontal lines "running toward the viewer"** are separate clips that each make one accelerating run (accelerating arrival `cubic-bezier(0.333, 0, 0.667, 0.333)`), started every 20 f. Each run must finish inside the comp (lint: `key_outside_clip`).
5. **A static gradient on text renders** (measured 0.1.6, still true on 0.1.8.1: the generator sets it on the model after the scene is applied, since a text gradient has no design key): `text_fill.paint = gradient` with a gradient object makes chrome or sunset type; only its endpoints cannot be animated (KI-009 c). The endpoints are object-local with y down, `[0.5, 0]` at the top: the first release of the sun and the chrome had them y up and rendered upside down (fixed 2026-10-28, [KI-155](../references/known-issues.md#ki-155)).
6. **Every key must sit inside its clip.** A staggered exit that ran past the comp end was a lint error (`key_outside_clip`); lengthen the comp or start the exits earlier.

Inspiration: 70s graphic design and 80s synthwave conventions, and limited-animation "on twos" timing. No external text or code was used.
