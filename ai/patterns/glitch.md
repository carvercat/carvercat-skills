# Glitch pack (`gl_`)

Broken-signal motion: stepped glitch entrances and exits, a stretch hit, an RGB-split title, a slice-shift logo, a noise overlay and a glitch cut. Round 3 adds a corrupted video title, a scan-line news ticker, a hacker alert, a cyber sale, a signal-lost end card, an error 404 page, a game over screen and a chromatic logo sting. For tech, gaming, music and edgy social pieces.

The pack lives in `library/templates/glitch/`. Install it as in [Installing a pack](README.md#installing-a-pack).

- The presets are built by `ai/scripts/motion/build_glitch_pack.py`. Its `steps()` helper writes held jumps.
- The templates come from `categories/glitch/gl-lab`, written by `ai/scripts/motion/glitch_lab.py`; round 2 from `categories/glitch/gl-lab-2` (`glitch_lab2.py`); round 3 from `categories/glitch/gl-lab-3` (`glitch_lab3.py`).
- The sample sting is `categories/glitch/gl-showcase`.

**Status: all 20 templates verified 0.1.8.1 (rev 1127 build; headless, isolated folders, pack added to a scratch user Library), measured by `ai/scripts/motion/verify_pack.py glitch` (the harness with the object-level checks).**
- The labs (`glitch_lab.py`, `_lab2.py`, `_lab3.py`) and the sample sting (`glitch_showcase.py`) speak design units (`json_author/cc2.py`) and are sent with `scene.apply`. The RGB split is one text with two drop shadows (`filter`; the first is keyed in the scene, the second with `key.set` on its own effect, which a scene cannot key); the pack's presets are baked as keys. `regen_pack.py` rebuilds the templates and the lab and showcase projects (carvercat/2).
- Each template was placed into a fresh 16:9 and a fresh 9:16 comp: lint 0 errors / 0 warnings / 0 notes; qc found no flashes.
- Against the v1 originals (7 frames each; 960 x 540 for the text templates): silhouettes match (at most 2 % of pixels differ), the object-level check finds no missing, empty or moved object and no changed text, and colours are now the exact hex values (the old kit's linear curve made them about 10/255 darker, which is gone).
- Keyed frames in the tables below are the generators' (unchanged). Percentages that came from `inspect curves` ("overshoot", the first jump read as 66.7 %) are 0.1.6 findings that were not re-measured.
- The lab comp `GL End card` is now `GL Signal end`, so its name matches the template file.
- The three presets (`.carverpreset`) are unchanged: they stay in the stored preset format and were verified by loading and applying them in 0.1.8.1.

**Fonts:** Rethink Sans must be installed ([KI-136](../references/known-issues.md#ki-136)).

**Photosensitivity first.** Glitch is the style most likely to produce flashing.
- Keep stepped opacity changes small (noise bars stay at 15–35% opacity, each on for 2 f).
- Keep full-frame luminance changes rare.
- Run `carvercat_inspect mode:qc` on every glitch comp before delivery.

Style: near-black `#0A0A0A`, white, glitch red `#FF2A55`, cyan `#00E5FF`, terminal green `#39FF14`. All motion is **stepped** (easing Hold arrives at each key, so the value jumps on that frame).

## Presets (3)

Measured on a 30 f clip that starts at frame 10.

| Name in Library | File | Anchor / frames | What moves | Measured | Use for |
|---|---|---|---|---|---|
| Glitch in | gl_glitch_in | in / 12 | held horizontal jumps +3, −2, +1.2, −0.6, +0.3% W; stepped opacity 0 → 100 → 40 → 100 → 70 → 100% | locked in by **f10** (curves reports the first jump as 66.7% "overshoot") | titles, logos, UI |
| Glitch out | gl_glitch_out | out / 10 | growing held jumps (−0.8 … +4% W) and stepped opacity to 0 | gone 2 f before the clip end | exits |
| Glitch stretch hit | gl_stretch_hit | in / 8 | scale steps 160 × 60% → 85 × 110% → 112 × 95% → 100% | settles **f6** | a word or logo landing on a beat |

Lint gives `speed_jump` info notes on every step. No `jitter` warning: the jumps are whole pixels, not sub-pixel reversals.

## Templates (4)

| Pattern | File / doc | Length |
|---|---|---|
| RGB split title | gl_rgb_title / [gl-rgb-title.md](gl-rgb-title.md) | 90 f |
| Slice shift | gl_slice_shift / [gl-slice-shift.md](gl-slice-shift.md) | 75 f |
| Noise bars overlay | gl_noise_bars / [gl-noise-bars.md](gl-noise-bars.md) | 60 f |
| Glitch cut | gl_glitch_cut / [gl-glitch-cut.md](gl-glitch-cut.md) | 30 f, cut at f15 |

## Templates added in round 2 (8)

| Pattern | File / doc | Length |
|---|---|---|
| Glitch lower third | gl_lower_third / [gl-lower-third.md](gl-lower-third.md) | 150 f, Glitch out at the end |
| Block artifact title | gl_block_title / [gl-block-title.md](gl-block-title.md) | 90 f |
| Error cascade | gl_error_cascade / [gl-error-cascade.md](gl-error-cascade.md) | 120 f |
| Terminal type-on | gl_terminal / [gl-terminal.md](gl-terminal.md) | 150 f |
| Stutter words | gl_stutter_words / [gl-stutter-words.md](gl-stutter-words.md) | 100 f, a word every 30 f |
| RGB split mark | gl_rgb_mark / [gl-rgb-mark.md](gl-rgb-mark.md) | 90 f |
| Tracking band (overlay) | gl_tracking_band / [gl-tracking-band.md](gl-tracking-band.md) | 90 f |
| Pixel dissolve (transition) | gl_pixel_dissolve / [gl-pixel-dissolve.md](gl-pixel-dissolve.md) | 40 f, cut at f19 |

Round 2 was built and verified the same way on 2026-10-27: every lab comp lints 0 errors / 0 warnings, `inspect qc` at 240 px found no flashes, and each template placed into a fresh comp lints 0/0/0. Clip-id prefixes: `glt_`, `gbt_`, `gec_`, `gtm_`, `gsw_`, `grm_`, `gtb_`, `gpd_`. Lab: `categories/glitch/gl-lab-2`, written by `ai/scripts/motion/glitch_lab2.py`.

## Round 3: briefs the pack could not serve before

Chosen from [reading a brief](../references/craft/reading-a-brief.md) ("music drop, release teaser, edgy tech") and the wiki's [social ads](../../wiki/genres/social-ads.md), [broadcast packages](../../wiki/genres/broadcast-packages.md), [UI and UX demos](../../wiki/genres/ui-ux-demos.md) and [logo animation](../../wiki/genres/logo-animation.md) pages, against what rounds 1 and 2 already cover (glitch titles, a lower third, error windows, a terminal, transitions and overlays): the creator, stream, sale, web and gaming briefs that ask for a glitch look, plus a ticker and a logo sting. Built and verified on 0.1.6 (rev 1105) on 2026-10-28. Every move is baked as Hold keys in `glitch_lab3.py` (`rgb_split()`, `jolt()`, `stretch_hit()` = the pack's Glitch stretch hit, `crt_on()` = a panel switching on like a tube, `steps_x()`, `blink_in()`), so there is nothing to apply after `edit.open` and no masks. Splits settle 12 f after a text starts; panels switch on in 6 f (the 104% step reads **4.1%** in `inspect curves`); stretch hits settle in 6 f (**25.0%**, the first step). Jump lanes with a re-glitch read as large "overshoot" ([KI-152](../references/known-issues.md#ki-152)); the tables quote settle frames instead. Copy, handles, scores and codes are invented stand-ins. Frames are comp frames. Clip-id prefixes: `gvt_`, `gnt_`, `gha_`, `gcs_`, `gse_`, `gnf_`, `ggo_`, `gcl_`.

**Photosensitivity: every round-3 template passes `inspect qc` (240 px) with no `flashes` finding**, in the lab and placed into a fresh comp. The only qc notes are `black` (the near-black ground before the first object) and, placed in a longer comp, `black`/`freeze` after the template ends. No full-frame brightness change, no red element that blinks, and the only repeating blink is a 16 px dot once a second.

| Template | File / doc | Brief it serves | Measured | Lint (lab) | Placed | qc flash |
|---|---|---|---|---|---|---|
| Corrupted video title | gl_video_title / [gl-video-title.md](gl-video-title.md) | creator video title, episode opener | lines f16 / f22; underline f26; meta f31; re-glitch f70–78; 120 f | 0 / 0 (3 info) | 0 / 0 / 0 | none |
| Scan-line news ticker | gl_news_ticker / [gl-news-ticker.md](gl-news-ticker.md) | breaking-news crawl, stream or esports ticker | band f6; tag f12; headlines 7 px/f, readable from f15; 150 f | 0 / 0 (1 info) | 0 / 0 / 0 | none |
| Hacker alert | gl_hack_alert / [gl-hack-alert.md](gl-hack-alert.md) | intrusion detected, security breach scene | panel f6; title f20; trace bar 8 steps to f122; 150 f | 0 / 0 (2 info) | 0 / 0 / 0 | none |
| Cyber sale | gl_cyber_sale / [gl-cyber-sale.md](gl-cyber-sale.md) | Cyber Monday / Black Friday, promo code | −50% size f12, split f18; code plate f36; re-glitch f60, f105; 150 f | 0 / 0 / 0 | 0 / 0 / 0 | none |
| Signal lost end card | gl_signal_end / [gl-signal-end.md](gl-signal-end.md) | video end screen, subscribe, stay tuned | slots f10 / f16; handle f33; subscribe f36; 150 f | 0 / 0 (3 info) | 0 / 0 / 0 | none |
| Error 404 page | gl_error_404 / [gl-error-404.md](gl-error-404.md) | 404 / page not found, web demo | 404 f12; headline f15; button f30; cursor lands f55, clicks f74; 120 f | 0 / 0 (1 info) | 0 / 0 / 0 | none |
| Game over screen | gl_game_over / [gl-game-over.md](gl-game-over.md) | game over / continue, stream fail | title f6 / f9; scores f19 / f23; 3-2-1 at f42, f74, f106; 150 f | 0 / 0 (5 info) | 0 / 0 / 0 | none |
| Chromatic logo sting | gl_chroma_sting / [gl-chroma-sting.md](gl-chroma-sting.md) | glitch logo ident, RGB reveal | R/G/B copies (Screen) white at f12; wordmark f28; re-split f50–54; 90 f | 0 / 0 (3 info) | 0 / 0 / 0 | none |

The info notes are `speed_jump` on the Hold jumps, as in rounds 1 and 2. Each template placed into a fresh comp applied "at 1920 x 1080" and linted 0/0/0. The text-gap audit (`audit_text_gaps.py`) flags nothing (closest pair 12.0 px, the LIVE dot inside its chip; closest text pair 35.2 px, score / hi score). Full-frame looks of the placed instances (8 frames each, plus single frames of the crawling headlines at f12 and f140, the cursor coming in at f44, the stretched GAME OVER at f0 and the split marks at f0) show nothing cut ([KI-144](../references/known-issues.md#ki-144)).

### Round-3 pitfalls
1. **Opacity is linear light.** A white tracking band at 6% showed as a grey bar (about 27% on screen) over near-black; scan lines at 12% crossed text visibly. Faint overlays on dark grounds want 2–5%.
2. **A datamosh smear works natively, but not as a Library template.** A horizontal blur (`blur` size 15–100 (stored value), `lock` false, `sizeY` 0) on an adjustment layer masked to a band smears whatever is under it, the closest native thing to a datamosh. Inside a placed template (a nested instance) the adjustment layer only reaches the instance's own contents, so it does nothing to your footage; and lint reports every adjustment layer as the error `never_visible` ([KI-158](../references/known-issues.md#ki-158)). Build it in the film comp itself, above the cut. Keep the bands 40 px short of the frame edges: the blur darkens the picture near the edge whatever `clipping` says ([KI-159](../references/known-issues.md#ki-159)). The `transform` effect (offset, scale, angle) is an internal recipe, not an authored effect, and changed nothing when written into a project.
3. **Lint does not see masks for text either.** Headlines masked so they vanished under the ticker's tag were still reported `text_overlap` (16%) ([KI-160](../references/known-issues.md#ki-160)); put the tag on its own row.
4. **Block artefacts over resting text count as overlaps** in the text-gap audit (−85.8 px on the sale price at f61). Keep blocks to the entrance; re-glitch a resting word with the split and a jump only.
5. **Reading time limits a crawl.** A fourth headline that entered at f139 was readable for 11 f (lint `reading_time`); the lab only adds a headline that gets 50 f on screen.
6. **Text tracking is not in `cc.textw`.** A chip sized with `textw("LIVE") + 76` was too narrow for the tracked word; widen plates under tracked text by hand and check with a look.

## Sample sting

`categories/glitch/gl-showcase` is a 165 f (5.5 s) master: RGB title → (glitch cut, f75–105, cut at 90) → slice-shift logo with the noise overlay. Lint 0/0/0; qc found no flashes.

## Techniques and pitfalls (0.1.6)

1. **RGB split without a second text:** add two native Drop shadows to the same text (softness 0, opacity 0.85, red and cyan through the Red/Green/Blue parameters). Key their Offset X with Hold steps in opposite directions. Two overlapping texts would fail lint (`text_overlap`).
2. **Slices need one mask per slice:** five copies of the mark, each masked by its own horizontal band (`property.set {id: <mark copy>, key: "mask", value: {"ref": "<band id>"}}`), then `parent.clear {ids:[band, mark copy]}`.
3. **No two keys on one frame:** random blink frames for a 2 f flash must be at least 4 f apart (lint: `same_frame_keys` error).
4. **Bars that jump must stay inside the frame** (lint: `cropped_at_rest`). The lab clamps each jump to the room left on each side.
5. **Short blips as clips, not keys.** A block that is on for 2–4 f is cleanest as its own 2–4 f clip; nothing to collide with `same_frame_keys`.
6. **Lint does not see occlusion.** Stacked windows or cards with text each count for `text_overlap`; keep text only on the top one.

## Round-2 sample film

`categories/glitch/gl-showcase-2` is a 700 f (23 s) master at 1920 × 1080 that plays the round-2 templates back to back with Pixel dissolve on one cut, placed from the Library with `library.place` + `template.apply` (rebuild: `ai/scripts/motion/recipes/showcase2.py glitch`). Verified 0.1.6 (rev 1105), 2026-10-28: master lint 0 / 0 / 0. Qc (240 px) notes four holds as freezes and no flashes.

Inspiration: common digital-glitch and VHS-error conventions. No external text or code was used.
