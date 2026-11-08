# Corporate Brand pack (`cb_`)

Calm, on-brand motion for company films, reports and events: soft rises and fades, a slow photo push, a split-rule title card, a two-box lower third, a frame-drawn logo resolve, a three-stat row, a chapter title, a quote, an end card, an agenda, a team row, a split screen, a leader callout and a brand panel wipe. Round 3 adds an org chart, a values grid, an anniversary card, an office location card, an award badge, a partner logo wall, a careers card and a safety notice.

The pack lives in `library/templates/corporate-brand/`. Install it as in [Installing a pack](README.md#installing-a-pack). It adds to the essentials' Lower third bar/rule, Logo reveal, Title centred and End card.

- The presets are built by `ai/scripts/motion/build_corporate_brand_pack.py`.
- The templates come from `categories/corporate-brand/cb-lab` (written by `ai/scripts/motion/corporate_brand_lab.py`) and, for round 2, `categories/corporate-brand/cb-lab-2` (written by `ai/scripts/motion/corporate_brand_lab2.py`), and for round 3, `categories/corporate-brand/cb-lab-3` (written by `ai/scripts/motion/corporate_brand_lab3.py`).
- The sample film is `categories/corporate-brand/cb-showcase`, written by `ai/scripts/motion/corporate_brand_showcase.py`.

**Status: Verified 0.1.8.1 (rev 1127).**
- Headless `carvercat-host` built from Carvercat 0.1.8.1 (rev 1127), fresh preferences, data and cache folders; the pack was installed into a scratch user Library. Measured with `ai/scripts/motion/verify_pack.py corporate-brand` (full table below).
- Every template placed into a fresh 16:9 and a fresh 9:16 comp: lint 0 errors / 0 warnings / 0 notes, no flashes (qc), for all 20 templates.
- Shape against the v1 original (7 frames; limit 2 %): all 20 pass, worst 0.03 % (Safety notice). The object-level check (missing, empty, moved, text objects) passes for all 20. No `--ink-templates` was needed.
- The showcase-2 master lints 0 / 0 / 0 (rebuilt by `ai/scripts/motion/recipes/showcase2.py corporate-brand`). The per-part "settles" figures in the pages are the authored key frames and curves; they were not re-measured one by one.

**Fonts:** the templates use Rethink Sans, which must be installed on the machine. It is a free Google Font (SIL OFL), and the file is in `ai/scripts/motion/json_author/RethinkSans.ttf`. Without it, text falls back to Arial ([KI-136](../references/known-issues.md#ki-136)). Check with `carvercat_authoring mode:validate` `font_exact`.

Style rules (see also [../references/craft/brand-systems.md](../references/craft/brand-systems.md)):
- One easing family: standard and decelerate curves, no springs or overshoot.
- Entrances 14–24 f, exits about 16 f.
- One accent colour (teal `#00A3A1`) on navy `#0B1F3A` or light `#F3F5F8`.
- SemiBold Rethink Sans with tracked caps for the wordmark.

## Presets (4)

Measured on a 150 f clip that starts at frame 10.

| Name in Library | File | Anchor / frames | What moves | Measured | Use for |
|---|---|---|---|---|---|
| Soft rise | cb_soft_rise | in / 24 | y +1.5% H → 0 (standard), fade over 60% | settles **f21**; opaque by f13 | titles, captions, wordmarks |
| Soft fade out | cb_soft_fall_out | out / 16 | opacity 1 → 0 and 1% upward drift, accelerating | the last 16 f | the calm exit for anything that entered softly |
| Card settle | cb_card_settle | in / 20 | y +2% H and scale 0.97 → 1 (strong decelerate), fade over 50% | settles **f16**, no overshoot; opaque by f10 | cards, panels, stat numbers, logo marks |
| Photo push - 5 s | cb_photo_push | in / 150 | scale 1 → 1.06, linear | 0.04% per frame | stills, plates and held frames |

**Photo push and lint:** keep the clip at 150 f or less. Once the push stops, a full-frame plate held at 106% is reported as `cropped_at_rest`. A 3 s version on a 150 f clip did exactly that in the showcase, so the preset is 5 s.

## Templates (20)

| Pattern | File / doc | Length |
|---|---|---|
| Title card - split rule | cb_title_card / [cb-title-card.md](cb-title-card.md) | 90 f |
| Lower third - two boxes | cb_lower_third / [cb-lower-third.md](cb-lower-third.md) | 150 f, exit 134–150 |
| Logo resolve - frame | cb_logo_resolve / [cb-logo-resolve.md](cb-logo-resolve.md) | 90 f |
| Three stats | cb_three_stats / [cb-three-stats.md](cb-three-stats.md) | 90 f, light background included |
| Chapter title | cb_chapter_title / [cb-chapter-title.md](cb-chapter-title.md) | 90 f, note settles f41 |
| Brand quote | cb_quote / [cb-quote.md](cb-quote.md) | 150 f, exit in the last 16 f |
| Brand end card | cb_end_card / [cb-end-card.md](cb-end-card.md) | 120 f, light background included |
| Agenda | cb_agenda / [cb-agenda.md](cb-agenda.md) | 150 f, marker moves f60–78 |
| Team row | cb_team_row / [cb-team-row.md](cb-team-row.md) | 120 f, light background included |
| Split screen | cb_split_screen / [cb-split-screen.md](cb-split-screen.md) | 150 f, light background included |
| Leader callout | cb_leader_callout / [cb-leader-callout.md](cb-leader-callout.md) | 120 f, exit in the last 16 f |
| Brand panel wipe (transition) | cb_panel_wipe / [cb-panel-wipe.md](cb-panel-wipe.md) | 40 f, cut at f20 |
| Org chart | cb_org_chart / [cb-org-chart.md](cb-org-chart.md) | 150 f, connectors f16–44, last card f69 |
| Values grid | cb_values_grid / [cb-values-grid.md](cb-values-grid.md) | 150 f, light background included, cards f23–41 |
| Anniversary card | cb_anniversary / [cb-anniversary.md](cb-anniversary.md) | 120 f, ring and number f26 |
| Office location card | cb_office_card / [cb-office-card.md](cb-office-card.md) | 150 f, light background included, pin f33, pulse to f64 |
| Award badge | cb_award_badge / [cb-award-badge.md](cb-award-badge.md) | 120 f, badge f23–41, award f59 |
| Partner logo wall | cb_partner_wall / [cb-partner-wall.md](cb-partner-wall.md) | 120 f, light background included, tiles f21–41 |
| Careers card | cb_careers_card / [cb-careers-card.md](cb-careers-card.md) | 150 f, button text f69 |
| Safety notice | cb_safety_notice / [cb-safety-notice.md](cb-safety-notice.md) | 150 f, signal amber, policy f55 |

Round 2 (8 templates) was built and verified the same way on 2026-10-27: every lab comp lints 0 errors / 0 warnings, each template placed into a fresh comp lints 0/0/0, and nothing overshoots. Clip-id prefixes: `cch_`, `cqt_`, `cec_`, `cag_`, `ctm_`, `css_`, `clc_`, `cpw_`.

## Round 3: briefs the pack could not serve before

Chosen from [reading a brief](../references/craft/reading-a-brief.md) ("company film, annual report, event opener") and the wiki's [broadcast packages](../../wiki/genres/broadcast-packages.md), [event openers](../../wiki/genres/event-openers.md), [infographics](../../wiki/genres/infographics.md) and [logo animation](../../wiki/genres/logo-animation.md) pages: the cards an internal-comms or employer-brand film needs that rounds 1 and 2 did not have. Built 2026-10-28; Verified 0.1.8.1 (rev 1127), see the 0.1.8.1 block below. Every move is baked as keys in `corporate_brand_lab3.py`: `soft_rise()` and `card_settle()` write the keys of the Soft rise and Card settle presets, so there is nothing to apply. Every easing lands with **0% overshoot** (the pack's rule). Names, places, logos and the company are invented stand-ins. Frames below are comp frames. Clip-id prefixes: `cog_`, `cvg_`, `can_`, `cof_`, `caw_`, `cpl_`, `chr_`, `csn_`.

| Template | Brief it serves | Measured | Lint (lab) | Placed |
|---|---|---|---|---|
| Org chart | new leadership team, who reports to whom | top card f19; connectors f24–44; report cards f57 / f63 / f69; last role f83 | 0 / 0 / 0 | 0 / 0 / 0 |
| Values grid | company values, "what we stand for" | cards f23–41; last line f59 | 0 / 0 / 0 | 0 / 0 / 0 |
| Anniversary card | "25 years", founding milestone | ring and number f26; span f44; thank-you f67 | 0 / 0 / 0 | 0 / 0 / 0 |
| Office location card | new office, "visit us at" | pin f33; pulse f34–64; city f35; date f55 | 0 / 0 / 0 | 0 / 0 / 0 |
| Award badge | award win, certification | ring and disc f23; star f31; award f53; body f59 | 0 / 0 / 0 | 0 / 0 / 0 |
| Partner logo wall | "trusted by", clients, sponsors | tiles f21–41; "and 400 more" f61 | 0 / 0 / 0 | 0 / 0 / 0 |
| Careers card | "we're hiring", job opening | role f29; pills f33–43; button f59, URL f69 | 0 / 0 / 0 | 0 / 0 / 0 |
| Safety notice | site safety rule, compliance notice | band f15; sign f24; heading f35; policy f55 | 0 / 0 / 0 | 0 / 0 / 0 |

Each template was also checked with the text-gap audit (`audit_text_gaps.py`): no tight pairs in any of the eight (closest 21.3 px, the org chart's title and subtitle). Template apply places each as a nested instance; full-frame looks of all eight placed instances (8 frames each, f0 to the last frame) show nothing cut by the frame edge, including the drawing connectors and rings and the office pin's pulse ([KI-144](../references/known-issues.md#ki-144)).

### Round-3 pitfalls
1. **A polygon's Angle does not rotate it** ([KI-150](../references/known-issues.md#ki-150)). A 3-sided polygon starts with a corner pointing right; set to 45 or 90, in the file or with `property.set`, it rendered the same. Stars also start with a point to the right. Turn triangles and stars with the transform rotation (+90 puts a point up).
2. **A polygon is centred on its circumcentre.** With the point up, a 340 px triangle reaches 170 px above the centre and only 85 px below; place a mark inside it below the centre, not on it.
3. **Presets as keys.** Writing the Soft rise and Card settle keys straight into the comp gives the same settle frames as the presets (Soft rise f + 21, Card settle f + 15 on a 20 f move) and leaves nothing to apply after `edit.open`.
4. **Reading time decides the length.** The last text of each card lands between f55 and f83; with 25 or more opaque frames per line and a 2 s hold for a URL, 120 f is the floor for the short cards and 150 f for the org chart, office and careers cards.
5. **Stand-ins must be visibly stand-ins.** Partner wordmarks, the map and the award are invented; replace them with supplied assets, and never redraw a real organisation's logo or seal as text or shapes.
6. **One accent, one exception.** The safety notice uses signal amber because a warning sign is read by its colour; everything else stays teal on navy or light.

## Sample film

`categories/corporate-brand/cb-showcase` is a 420 f (14 s) master:
- logo resolve;
- title card (3% push over its hold);
- three stats (3% push);
- the lower third over a stand-in footage plate (a navy-to-teal gradient with Photo push - 5 s).

Lint: 0/0/0. QC still notes "freeze" over the title-card and stats holds, because its 96 px analysis does not register a 3% push.

## Round-2 sample film

`categories/corporate-brand/cb-showcase-2` is a 900 f (30 s) master at 1920 × 1080 that plays every round-2 template back to back, placed from the Library with `library.place` + `template.apply` (rebuild: `ai/scripts/motion/recipes/showcase2.py corporate-brand`). Verified 0.1.8.1 (rev 1127): master lint 0 / 0 / 0. `qc` (240 px) notes the long holds as freezes (fine for a hold).

## Verified 0.1.8.1 (rev 1127): design-unit generators

All 20 templates were regenerated as carvercat/2 by the pack's lab modules (design units: px from the top-left, y down, degrees clockwise, exact hex colours, CSS easing); the lab, showcase, showcase-2 and recipe sample projects by the same modules. The `.carverpreset` files are unchanged and load in the app.
- Harness (`verify_pack.py`, 7 frames per template; 320 x 180, 960 x 540 for templates with text; shape limit 2 %). `covered` / `cut` / `settled` / `gone` use the harness definition (covered = the frame reads the same over a magenta and a green underlay; settled = first frame from which the picture no longer changes; gone = last visible frame + 1); None means the template never covers the frame or never goes blank.

| Template | lint 16:9 e/w/n | lint 9:16 e/w/n | v1 vs v2 | worst shape | colour shift | object check | box offset max px | worst ink IoU | covered | cut | settled | gone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Agenda | 0/0/0 | 0/0/0 | pass | 0.01 % | 4.6 | pass | 0.1 | 0.94 | None | None | None | None |
| Anniversary card | 0/0/0 | 0/0/0 | pass | 0.01 % | 2.5 | pass | 0.4 | 0.96 | None | None | None | None |
| Award badge | 0/0/0 | 0/0/0 | pass | 0.01 % | 13.2 | pass | 0.4 | 0.73 | None | None | None | None |
| Brand end card | 0/0/0 | 0/0/0 | pass | 0.00 % | 1.4 | pass | 0.1 | 0.92 | [0, 119] | 0 | None | None |
| Brand panel wipe | 0/0/0 | 0/0/0 | pass | 0.00 % | 11.3 | pass | 0.0 |  | [15, 24] | 15 | 38 | None |
| Brand quote | 0/0/0 | 0/0/0 | pass | 0.02 % | 1.4 | pass | 0.1 | 0.97 | None | None | None | 149 |
| Careers card | 0/0/0 | 0/0/0 | pass | 0.01 % | 10.8 | pass | 0.4 | 0.9 | None | None | None | None |
| Chapter title | 0/0/0 | 0/0/0 | pass | 0.01 % | 3.6 | pass | 0.1 | 0.96 | None | None | None | None |
| Leader callout | 0/0/0 | 0/0/0 | pass | 0.01 % | 2.0 | pass | 0.1 | 0.95 | None | None | None | 119 |
| Logo resolve - frame | 0/0/0 | 0/0/0 | pass | 0.00 % | 3.5 | pass | 0.1 | 0.97 | None | None | None | None |
| Lower third - two boxes | 0/0/0 | 0/0/0 | pass | 0.00 % | 2.4 | pass | 0.0 | 0.98 | None | None | None | 149 |
| Office location card | 0/0/0 | 0/0/0 | pass | 0.00 % | 2.4 | pass | 0.4 | 0.91 | [0, 149] | 0 | None | None |
| Org chart | 0/0/0 | 0/0/0 | pass | 0.02 % | 13.2 | pass | 0.4 | 0.9 | None | None | None | None |
| Partner logo wall | 0/0/0 | 0/0/0 | pass | 0.00 % | 1.3 | pass | 0.4 | 0.94 | [0, 119] | 0 | None | None |
| Safety notice | 0/0/0 | 0/0/0 | pass | 0.03 % | 3.4 | pass | 0.4 | 0.96 | None | None | None | None |
| Split screen | 0/0/0 | 0/0/0 | pass | 0.00 % | 8.1 | pass | 0.1 | 0.87 | [0, 149] | 0 | None | None |
| Team row | 0/0/0 | 0/0/0 | pass | 0.00 % | 1.6 | pass | 0.1 | 0.79 | [0, 119] | 0 | None | None |
| Three stats | 0/0/0 | 0/0/0 | pass | 0.00 % | 1.4 | pass | 0.1 | 0.88 | [0, 89] | 0 | None | None |
| Title card - split rule | 0/0/0 | 0/0/0 | pass | 0.00 % | 2.9 | pass | 0.0 | 0.97 | None | None | None | None |
| Values grid | 0/0/0 | 0/0/0 | pass | 0.00 % | 1.3 | pass | 0.4 | 0.75 | [0, 149] | 0 | None | None |

- Colours are the exact hex of the style notes (the old kit linearised them): the colour shift to v1 is reported, not judged, and is intended.
- What changed: corner radii keep the old cap of a quarter of the short side; "Ease out" is the old curve (1/3, 2/3, 2/3, 1); text boxes are centred on y with the tracking and line height written explicitly; a path's position keys are its bounding box; the scene mask windows are un-parented (parent.clear). Brand panel wipe: covered f15-24, settled f38 (harness definition). Lower third, Brand quote: gone f149; Leader callout: gone f119.

## Pitfalls

1. **Reveal from behind a rule:** the title must start fully hidden. Its travel must be at least its own width (480 px for "Annual Report" at 64 px), or it is visible on frame 0.
2. **Text inside a growing box:** give the text's mask window the same scale keys as the box (anchor [−1, 0]). A static, full-size window shows the text before the box has grown under it.
3. **Lint is mask-blind** ([KI-133](../references/known-issues.md#ki-133)). A subtitle that slid from behind the rule overlapped the hidden title box, so the subtitle now starts at f18 with a 20 px slide and a fade.
4. **`carvercat_look` with `region`** drew the full-frame background only as a strip in one corner, on comps with and without masks ([KI-135](../references/known-issues.md#ki-135)). Judge backgrounds from full-frame looks.
5. **Light templates need their own background object.** `--drop "Lab bg"` removes the lab ground, so a light layout extracted that way puts navy text on whatever is underneath. Round-2 light comps add a separate "Light background" rectangle that stays in the template.
6. **Off-screen panels must not sit still.** A wipe panel parked off-screen raises `cropped_at_rest`; make each panel's clip span only its motion.

Inspiration: common corporate and annual-report motion conventions. No external text or code was used.
