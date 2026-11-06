# SaaS UI pack (`su_`)

Product-interface motion for SaaS launch and feature videos: toasts, cards, modals, drawers, cursor clicks, toggles, KPI tiles, chart cards, chat threads, dropdowns, a lower third, a feature title, a CTA end card, a rolling number counter and a search box that types itself. Round 3 adds pricing plans, a browser window that loads, a submit button that turns into a success state, a kanban drag, an integrations hub, a camera zoom into one dashboard card and a review card.

The pack lives in `library/templates/saas-ui/`. Install it as in [Installing a pack](README.md#installing-a-pack). It adds to Motion Patterns and does not replace it.

- The presets are built by `ai/scripts/motion/build_saas_ui_pack.py`.
- The templates are extracted with `comp_to_template.py` from two lab projects: `categories/saas-launch/saas-ui-lab/project.carverproj` (written by `ai/scripts/motion/saas_ui_lab.py`) for round 2, `categories/saas-launch/saas-ui-lab-2/project.carverproj` (written by `ai/scripts/motion/saas_ui_lab2.py`), and for round 3, `categories/saas-launch/saas-ui-lab-3/project.carverproj` (written by `ai/scripts/motion/saas_ui_lab3.py`).
- The sample film is `categories/saas-launch/saas-ui-showcase/`, written by `ai/scripts/motion/saas_ui_showcase.py`.

**Status: verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test).** The build was the public release binary, run headless (`--mcp`) with isolated preferences, data and cache folders, on 2026-10-27. A packaged build loads Library packs only from its own bundle, so for the preset and placement tests the pack was copied into the `Contents/Resources/library/templates` folder of a scratch copy of the app; the program binary is byte-identical to the release. The pack was first built on the verification build (source marked dirty). Re-verified on, every preset and template number below is identical, the five templates re-extract to identical scenes, and placement lint is again 0/0/0. Each item was checked in four ways:
- `carvercat_inspect mode:curves`: overshoot and settle frame. "Settle" is the clip frame after which the value stays within 0.5%.
- `carvercat_look`: whole-frame and zoomed contact sheets of the entrance, hold and exit.
- `carvercat_inspect mode:lint`: 0 errors and 0 warnings, except on the rolling-counter lab comp (see its doc).
- For templates: `library.place` + `template.apply` into a fresh comp, then lint (0/0/0) and a look.

**Fonts:** the templates use Rethink Sans, which must be installed on the machine. It is a free Google Font (SIL OFL), and the file is in `ai/scripts/motion/json_author/RethinkSans.ttf`. Without it, text falls back to Arial ([KI-136](../references/known-issues.md#ki-136)). Check with `carvercat_authoring mode:validate` `font_exact`.

Style: SaaS. Calm expo or decelerate landings, small springs (4–5%) only on things that drop in, accelerating exits at about 50–70% of the entrance length, rounded white cards on a deep indigo ground, one accent colour (`#5B5BF6`), and Rethink Sans.

## Presets (7)

Measured on a 60 f clip that starts at frame 10. Frames below are counted from the clip start for entrances, and from the clip end for exits.

| Name in Library | File | Anchor / frames | What moves | Measured | Use for |
|---|---|---|---|---|---|
| Toast drop - spring | su_toast_drop | in / 20 | y −6% H → 0 (from above), fade over the first 30% | **4.4% overshoot, settles f18** | toasts, banners, anything arriving from the top of a UI |
| Toast exit up | su_toast_exit_up | out / 10 | y 0 → −6% H, fade from 30% | accelerating; moves in the last 10 f | the mirror of Toast drop |
| Card lift | su_card_lift | in / 18 | y +3% H → 0 and scale 0.94 → 1 (expo), fade over 40% | position and size settle **f12**; opaque by f7 | cards, modals, tiles, and text inside a card |
| Modal dismiss | su_modal_dismiss | out / 9 | scale 1 → 0.95, fade from 20% | accelerating; the last 9 f | closing a modal, card or popover |
| Panel in - left | su_panel_in_left | in / 22 | x −25% W → 0, no fade | expo; settles **f15** | sidebars, drawers (start under a frame edge or a mask) |
| Panel out - left | su_panel_out_left | out / 14 | x 0 → −25% W, no fade | accelerating; the last 14 f | the drawer closing |
| Tap ripple | su_tap_ripple | in / 18 | scale 0.25 → 1 (expo), opacity 0.7 → 0 from 15% | size settles **f12**; invisible by f17 | the ring under a click (a ring clip that starts on the tap frame, 18 f long) |

Presets are relative, like Motion Patterns: positions add to where the object is, and size and opacity multiply. One object can take an entrance and an exit preset on the same property; the toast template does exactly that.

## Templates (19) and recipes (2)

| Pattern | Kind | File / doc | Length |
|---|---|---|---|
| Cursor click | template | su_cursor_click / [su-cursor-click.md](su-cursor-click.md) | 60 f, press f26, ripple f28 |
| Notification toast | template | su_notification_toast / [su-notification-toast.md](su-notification-toast.md) | 120 f, exit 110–120 |
| Toggle switch | template | su_toggle_switch / [su-toggle-switch.md](su-toggle-switch.md) | 48 f, switches f14–24 |
| KPI tile | template | su_kpi_tile / [su-kpi-tile.md](su-kpi-tile.md) | 90 f, holds (add an exit on the instance) |
| Sidebar drawer | template | su_sidebar_drawer / [su-sidebar-drawer.md](su-sidebar-drawer.md) | 60 f, drawer f6–28 |
| SaaS lower third | template | su_lower_third / [su-lower-third.md](su-lower-third.md) | 150 f, pill settles f9, exit 141–150 |
| Feature title | template | su_feature_title / [su-feature-title.md](su-feature-title.md) | 90 f, headline settles f17 |
| CTA end card | template | su_cta_end_card / [su-cta-end-card.md](su-cta-end-card.md) | 120 f, all still by f40 |
| Modal over app | template | su_modal / [su-modal.md](su-modal.md) | 90 f, full frame; opens f6–20, closes f70–90 |
| Chart card | template | su_chart_card / [su-chart-card.md](su-chart-card.md) | 90 f, bars settle f28–46 |
| Chat thread | template | su_chat_thread / [su-chat-thread.md](su-chat-thread.md) | 120 f, bubbles at f0/26/52 |
| Dropdown menu | template | su_dropdown / [su-dropdown.md](su-dropdown.md) | 90 f, panel settles f16, hover f40 |
| Pricing plans | template | su_pricing_plans / [su-pricing-plans.md](su-pricing-plans.md) | 150 f, featured plan steps forward f40–56 |
| Browser window load | template | su_browser_load / [su-browser-load.md](su-browser-load.md) | 150 f, skeleton f10–70, content f64–113 |
| Submit to success | template | su_submit_success / [su-submit-success.md](su-submit-success.md) | 150 f, press f24, spinner f42–80, success f76–92 |
| Kanban drag | template | su_kanban_drag / [su-kanban-drag.md](su-kanban-drag.md) | 150 f, drag f42–96 |
| Integrations hub | template | su_integrations_hub / [su-integrations-hub.md](su-integrations-hub.md) | 150 f, all in by f46, pulses f54 and f98 |
| Zoom to card | template | su_zoom_focus / [su-zoom-focus.md](su-zoom-focus.md) | 150 f, full frame; in f20–46, out f104–128 |
| Review card | template | su_review_card / [su-review-card.md](su-review-card.md) | 150 f, all in by f55 |
| Rolling counter | recipe | [su-rolling-counter.md](su-rolling-counter.md) | 60 f, rolls f6–36 |
| Search typing | recipe | [su-search-typing.md](su-search-typing.md) | 80 f, types from f31 |

Templates arrive as a nested comp, the same as Motion Patterns templates (see [README.md](README.md#what-a-template-becomes-read-before-placing-one)). Their clip ids carry the prefixes `cur_`, `tst_`, `tgl_`, `kpi_`, `sbd_` (round 1) and `slt_`, `sft_`, `sec_`, `smd_`, `scc_`, `sct_`, `sdd_` (round 2) and `spp_`, `sbw_`, `sss_`, `skd_`, `sih_`, `szf_`, `srv_` (round 3); no two templates in the skills library share a prefix.

Round 2 (7 templates) was built and verified the same way on 2026-10-27: every lab comp lints 0 errors / 0 warnings, and each template placed into a fresh comp lints 0/0/0. The round-2 templates reuse presets from Motion Patterns (Pop - gentle, Pop - spring, Words rise - expo) and data-viz (Bar grow up - spring); the motion is baked into the templates as keys, so they do not need those packs installed.

## Round 3: briefs the pack could not serve before

Chosen from the brief→style table in [reading a brief](../references/craft/reading-a-brief.md) and the wiki's [UI demo](../../wiki/genres/ui-ux-demos.md) and [product launch](../../wiki/genres/product-launches.md) pages: "new pricing", "show the product", "sign up / checkout", "project management", "works with your tools", "zoom into the feature" and "customers love it". Built and verified on 0.1.6 (rev 1105) on 2026-10-28. Every move is baked as keys in `saas_ui_lab3.py` (no presets to apply). The small spring is one bezier, (0.34, 1.36, 0.64, 1): **4.3% overshoot** measured on every pop.

| Template | Brief it serves | Measured | Lint (lab) | Placed |
|---|---|---|---|---|
| Pricing plans | new pricing, plan launch | cards settle f12–20; featured plan 1.8% / 2.1% (position / size), settles f53–54; badge 4.3%, f61 | 0 / 0 | 0 / 0 / 0 |
| Browser window load | product hero shot, "it's fast" | window settles f15; skeleton gone f70; last bar 4.3%, f113 | 0 / 0 / 0 | 0 / 0 / 0 |
| Submit to success | sign-up, checkout, one-click | press 3.5%, f33; circle by f43; success 4.3%, f87; tick f88 | 0 / 0 | 0 / 0 / 0 |
| Kanban drag | project management, workflow | carry f48–84; drop settles f88–96; gap closes f97 | 0 / 0 | 0 / 0 / 0 |
| Integrations hub | integrations, ecosystem | hub 4.3%, f13; links 9 f each; tiles 4.3%, f31–46 | 0 / 0 | 0 / 0 / 0 |
| Zoom to card | UI demo camera, "the number that matters" | 0% overshoot; 1.7× by f46, push to 1.76×, out by f128 | 0 / 0 | 0 / 0 / 0 |
| Review card | social proof, testimonial | card f12; stars 4.3%, f21–33; quote f34 | 0 / 0 / 0 | 0 / 0 / 0 |

Each template was also checked with the text-gap audit (`audit_text_gaps.py`, no tight pairs) and with full-frame looks of the placed instance (Zoom to card moves inside its instance: no cut content, [KI-144](../references/known-issues.md#ki-144)).

## Sample film

`categories/saas-launch/saas-ui-showcase` is a 458 f (15.3 s) master at 1920×1080 and 30 fps. It cuts the lab comps together: search typing, sidebar drawer, KPI tile, a cursor clicking the toggle, the rolling counter, and the toast.

The cursor starts 14 f into its own comp (`sourceIn` 14), so its ripple lands on the frame the knob starts moving (master f244). The KPI and toast scenes carry a slow 3% scale push on their instances so the long holds never freeze. Lint on the master: 0 errors, 0 warnings, 0 notes.

## Round-2 sample film

`categories/saas-launch/saas-ui-showcase-2` is a 750 f (25 s) master at 1920 × 1080 that plays every round-2 template back to back, placed from the Library with `library.place` + `template.apply` (rebuild: `ai/scripts/motion/recipes/showcase2.py saas-ui`). Verified 0.1.6 (rev 1105), 2026-10-28, after the text-gap audit: master lint 0 / 0 / 0. `qc` (240 px) notes the long holds as freezes (fine for a hold).

## Pitfalls found while building this pack (0.1.6)

1. **In the stored preset format the easing on a key shapes the move that ARRIVES at that key.** Measured: the accelerating curve `cubic-bezier(0.333, 0, 0.667, 0.333)` (stored as Ease out) on the second key gave an accelerating move; the same curve on the first key left the move linear (peak 46.7 px/frame = constant speed). In design units a key's `ease` shapes the segment that LEAVES it, as in CSS; the app converts.
2. **Lint does not see masks.** `inspect lint` reports `cropped_at_rest` and `text_overlap` for the hidden lines of masked digit columns. The tool says so itself ("excludes masks"). Judge masked builds with `carvercat_look`. Logged as [KI-133](../references/known-issues.md#ki-133).
3. **A mask is set on its target** (`property.set {id: <target>, key: "mask", value: {"ref": "<mask object id>"}}`, then `parent.clear {ids:[mask, target]}` so the window stays still while the content moves; the mask must be on another track). The old `mask.make {ids:[...]}` took the FIRST id as the mask (measured on 0.1.6; [../references/effects/compositing-and-masks.md](../references/effects/compositing-and-masks.md)). The first release of this pack passed `[column, window]`. That made each digit column the matte and drew it in the window's colour. It only looked right because the digits and the windows were both white: recolouring the digits changed nothing. The lab and showcase now pass `[window, column]`. Visible difference: the digits' motion blur now shows while they roll; it was lost when the columns were mattes.
4. **"Clip to box" did not hide the extra lines of a multi-line title text** (mode titles, relative position animated). Use a mask instead ([KI-132](../references/known-issues.md#ki-132)).
5. **Lint wants text on screen long enough to read.** Back-to-back 2 f text clips (the old counter and type-on workaround for [KI-051](../references/known-issues.md#ki-051)) raise one `reading_time` warning per clip. Use the stagger type-on and the rolling counter instead.
6. **Text inside a card should not use a drop from above.** It lags the card and pokes out above it. Drop the card, and lift the text (Card lift) inside it.
7. **Pills:** `cornerRadius` cannot make a full pill. The toggle track is a 2-point path with a round-capped stroke, as `json-authoring.md` describes.
8. **A pill closes into a circle by trimming both ends of its round-capped stroke** towards the middle (start → 0.4995, end → 0.5005): only the round caps remain (round 3, [su-submit-success.md](su-submit-success.md)).
9. **Lint's minimum text size is a measured line height of 18 px.** In Rethink Sans that needs about 26 px Medium for mixed-case labels; capitals-only words measure smaller ("DR" at 24 px = 12.3 px). Round 3 labels at 22–24 px failed (15.7–17.6 px) and were raised to 26–36 px.
10. **A still camera hold on a zoomed UI raises `cropped_at_rest`** for everything the frame cuts (six warnings measured). A slow push through the hold (1.7 → 1.76×) clears them and keeps the hold alive ([su-zoom-focus.md](su-zoom-focus.md)).
11. **Draw order is creation order** in the lab scripts: anything dragged across other UI must be created after it ([su-kanban-drag.md](su-kanban-drag.md)).
12. **Parent card contents to the card** when the card itself moves or scales after its entrance (featured plan, dragged card, the zoom camera). A parented child's stored position is an offset from the comp centre (in design units a child's `x`, `y` are from its parent's top-left) (`rig()` in `cartoon_bounce_lab2.py`); see [json-authoring.md](../references/app/json-authoring.md).

Inspiration: common product-video conventions. No external text or code was used.
