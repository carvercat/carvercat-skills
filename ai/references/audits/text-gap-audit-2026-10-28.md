Historical report in the units of its time (fractions, y up); current work uses design units: ../app/design-units.md.

# Text gap audit, 2026-10-28

Why: lint `text_overlap` misses small overlaps between neighbouring texts ([KI-138](../known-issues.md#ki-138)). This audit measured every Library template in the skills repo instead.

How: `ai/scripts/motion/audit_text_gaps.py` loads every template's scene into one project and, in Carvercat 0.1.6 (rev 1105,; headless, isolated folders), reads each object's visible window and keys from `carvercat_inspect mode:timing`. Each object's **rest window** runs from the end of its first key cluster (the entrance) to the start of its last key cluster when that cluster ends the clip (the exit). For every pair of texts, and every text with a small shape (both sides 80 px or less: dots, separators, brackets, ticks), that are at rest together, it measures both objects' ink bounds with `carvercat_authoring mode:geometry` at the middle of the shared rest window. Gap = the empty space between the two boxes (negative = overlap). Pairs under 12 px are flagged.

Check of the method: on the first release of the Minimal Luxury Attribute row it reported the known overlap (−19.3 px between the first two words).

Result: 168 templates checked (all 13 style packs, both rounds, Transitions and Motion Patterns). Six were fixed in this audit or the one before; one Motion Patterns template is flagged and left unchanged; one flag is a false positive (an occluded title).

| Pack | File | Library name | Pairs | Smallest gap at rest | Pair | Frame | Status |
|---|---|---|---|---|---|---|---|
| cartoon-bounce | ct_blink_face.carvertemplate | Blinking face | 0 | — | no pairs at rest together | — | ok |
| cartoon-bounce | ct_boing_title.carvertemplate | Boing title | 0 | — | no pairs at rest together | — | ok |
| cartoon-bounce | ct_bouncing_ball.carvertemplate | Bouncing ball | 0 | — | no pairs at rest together | — | ok |
| cartoon-bounce | ct_bouncy_list.carvertemplate | Bouncy list | 3 | 133.8 px | Item text 2 / Item text 3 | 81 | ok |
| cartoon-bounce | ct_button_press.carvertemplate | Button press | 0 | — | no pairs at rest together | — | ok |
| cartoon-bounce | ct_character_hop.carvertemplate | Character hop | 0 | — | no pairs at rest together | — | ok |
| cartoon-bounce | ct_end_card.carvertemplate | Cartoon end card | 1 | 138.9 px | Sign-off / Next label | 90 | ok |
| cartoon-bounce | ct_hanging_sign.carvertemplate | Hanging sign | 1 | 244.0 px | Sign text / Nail | 65 | ok |
| cartoon-bounce | ct_ribbon_lower_third.carvertemplate | Ribbon lower third | 1 | 72.4 px | Ribbon name / Ribbon role | 78 | ok |
| cartoon-bounce | ct_smear_whoosh.carvertemplate | Smear whoosh | 0 | — | no pairs at rest together | — | ok |
| cartoon-bounce | ct_speech_bubble.carvertemplate | Speech bubble | 0 | — | no pairs at rest together | — | ok |
| cartoon-bounce | ct_sticker_burst.carvertemplate | Sticker burst | 0 | — | no pairs at rest together | — | ok |
| corporate-brand | cb_agenda.carvertemplate | Agenda | 45 | 36.0 px | Number 2 / Active marker | 93 | ok |
| corporate-brand | cb_chapter_title.carvertemplate | Chapter title | 3 | 35.8 px | Chapter name / Chapter note | 66 | ok |
| corporate-brand | cb_end_card.carvertemplate | Brand end card | 3 | 84.0 px | Wordmark / Mark inner | 77 | ok |
| corporate-brand | cb_leader_callout.carvertemplate | Leader callout | 5 | 48.4 px | Callout title / Callout note | 78 | ok |
| corporate-brand | cb_logo_resolve.carvertemplate | Logo resolve - frame | 1 | 38.8 px | Wordmark / Tagline | 73 | ok |
| corporate-brand | cb_lower_third.carvertemplate | Lower third - two boxes | 1 | 39.9 px | Name / Role | 69 | ok |
| corporate-brand | cb_panel_wipe.carvertemplate | Brand panel wipe | 0 | — | no pairs at rest together | — | ok |
| corporate-brand | cb_quote.carvertemplate | Brand quote | 3 | 23.4 px | Speaker / Speaker role | 93 | ok |
| corporate-brand | cb_split_screen.carvertemplate | Split screen | 3 | 29.7 px | Kicker / Heading | 92 | ok |
| corporate-brand | cb_team_row.carvertemplate | Team row | 15 | 15.6 px | Name 2 / Role 2 | 82 | ok |
| corporate-brand | cb_three_stats.carvertemplate | Three stats | 15 | 44.4 px | Number 3 / Label 3 | 67 | ok |
| corporate-brand | cb_title_card.carvertemplate | Title card - split rule | 3 | 19.2 px | Title / Year | 44 | fixed 2026-10-28 |
| data-viz | dv_area_chart.carvertemplate | Area chart | 0 | — | no pairs at rest together | — | ok |
| data-viz | dv_before_after.carvertemplate | Comparison bars | 10 | 218.4 px | Label Before / Value Before | 62 | ok |
| data-viz | dv_column_chart.carvertemplate | Column chart | 45 | 87.9 px | Axis 0 / Month 1 | 50 | ok |
| data-viz | dv_data_table.carvertemplate | Data table | 190 | 57.4 px | Cell 1.1 / Cell 2.1 | 72 | ok |
| data-viz | dv_donut.carvertemplate | Donut - fill | 1 | 25.8 px | Centre value / Centre label | 66 | ok |
| data-viz | dv_gauge.carvertemplate | Gauge | 3 | 28.2 px | Gauge value / Gauge label | 57 | ok |
| data-viz | dv_line_chart.carvertemplate | Line chart - draw | 51 | 23.5 px | Axis 25 / Point 1 | 55 | ok |
| data-viz | dv_progress_rings.carvertemplate | Progress rings | 15 | 175.8 px | Value 1 / Label 1 | 59 | ok |
| data-viz | dv_ranked_bars.carvertemplate | Ranked bars | 45 | 93.3 px | Label 2 / Label 3 | 51 | ok |
| data-viz | dv_stacked_bar.carvertemplate | Stacked bar | 30 | 16.0 px | Legend 4 / Swatch 4 | 67 | ok |
| data-viz | dv_timeline.carvertemplate | Timeline | 95 | 41.7 px | Year 1 / Milestone 1 | 69 | ok |
| data-viz | dv_waffle_chart.carvertemplate | Waffle chart | 201 | 57.8 px | Waffle value / Waffle label | 74 | ok |
| explainer | ex_callout.carvertemplate | Pointer callout | 1 | 585.6 px | Label / Target | 59 | ok |
| explainer | ex_checklist.carvertemplate | Checklist | 50 | 36.0 px | Check item 1 / Box 1 | 87 | ok |
| explainer | ex_compare_columns.carvertemplate | Compare columns | 100 | 35.0 px | Item 2.1 / Tick 2.1 | 106 | ok |
| explainer | ex_cycle.carvertemplate | Cycle loop | 10 | 189.6 px | Cycle label 4 / Cycle centre | 113 | ok |
| explainer | ex_flow_diagram.carvertemplate | Flow diagram | 14 | 123.7 px | Node label 3 / Flow arrow 2 head | 109 | ok |
| explainer | ex_icon_grid.carvertemplate | Icon grid | 15 | 287.8 px | Caption 2 / Caption 5 | 65 | ok |
| explainer | ex_key_term.carvertemplate | Key term card | 3 | 57.0 px | Term tag / Term | 84 | ok |
| explainer | ex_lower_third.carvertemplate | Speaker lower third | 3 | 22.0 px | LT role / LT dot | 82 | ok |
| explainer | ex_process_steps.carvertemplate | Process steps | 54 | 21.5 px | Step 3 title / Step 3 text | 95 | ok |
| explainer | ex_quiz.carvertemplate | Quiz question | 10 | 90.4 px | Option text 2 / Option text 3 | 115 | ok |
| explainer | ex_timeline.carvertemplate | Milestone timeline | 60 | 39.3 px | Year 4 / Milestone 4 | 137 | ok |
| explainer | ex_venn.carvertemplate | Venn diagram | 6 | 122.3 px | Set label 1 / Overlap label | 85 | ok |
| funky | fk_lower_third.carvertemplate | Funky lower third | 1 | 42.4 px | Name / Tag text | 83 | ok |
| funky | fk_memphis_shapes.carvertemplate | Memphis shapes | 0 | — | no pairs at rest together | — | ok |
| funky | fk_offset_title.carvertemplate | Offset shadow title | 0 | — | no pairs at rest together | — | ok |
| funky | fk_orbit_end.carvertemplate | Orbit end card | 1 | 290.3 px | Hub text / Follow | 98 | ok |
| funky | fk_pattern_drift.carvertemplate | Pattern drift | 0 | — | no pairs at rest together | — | ok |
| funky | fk_photo_stack.carvertemplate | Photo stack | 0 | — | no pairs at rest together | — | ok |
| funky | fk_sale_badge.carvertemplate | Sale badge | 1 | 48.8 px | Badge big / Badge small | 57 | ok |
| funky | fk_squiggle_underline.carvertemplate | Squiggle underline | 3 | 43.8 px | Phrase / Spark 3 | 68 | ok |
| funky | fk_star_cover.carvertemplate | Star cover | 0 | — | no pairs at rest together | — | ok |
| funky | fk_sticker_stack.carvertemplate | Sticker stack | 3 | 45.0 px | Sticker label 2 / Sticker label 3 | 49 | ok |
| funky | fk_swing_headline.carvertemplate | Swing headline | 0 | — | no pairs at rest together | — | ok |
| funky | fk_zigzag_ribbon.carvertemplate | Zigzag ribbon | 0 | — | no pairs at rest together | — | ok |
| futuristic-hud | fh_alert_banner.carvertemplate | Alert banner | 0 | — | no pairs at rest together | — | ok |
| futuristic-hud | fh_brackets.carvertemplate | Corner brackets scan | 4 | 20.7 px | Tag / Corner TL | 49 | ok |
| futuristic-hud | fh_hex_grid.carvertemplate | Hex grid | 0 | — | no pairs at rest together | — | ok |
| futuristic-hud | fh_id_lower_third.carvertemplate | HUD ID lower third | 11 | 18.1 px | Callsign / ID corner 1 | 78 | fixed 2026-10-28 |
| futuristic-hud | fh_loader.carvertemplate | Segment loader | 110 | 37.5 px | Done / Slot 1 | 116 | ok |
| futuristic-hud | fh_map_ping.carvertemplate | Map ping | 3 | 51.8 px | Ping coords / Ping name | 78 | ok |
| futuristic-hud | fh_radar.carvertemplate | Radar sweep | 0 | — | no pairs at rest together | — | ok |
| futuristic-hud | fh_readout.carvertemplate | Data readout | 28 | 45.4 px | Value 3 / Value 4 | 71 | ok |
| futuristic-hud | fh_reticle.carvertemplate | Targeting reticle | 1 | 300.5 px | Lock label / Centre dot | 65 | ok |
| futuristic-hud | fh_scan_wipe.carvertemplate | Scan wipe | 0 | — | no pairs at rest together | — | ok |
| futuristic-hud | fh_signal_bars.carvertemplate | Signal bars | 3 | 293.9 px | Signal label / Bar 9 | 113 | ok |
| futuristic-hud | fh_target_lock.carvertemplate | Target lock | 11 | 46.2 px | Lock text / Lock data | 70 | ok |
| glitch | gl_block_title.carvertemplate | Block artifact title | 0 | — | no pairs at rest together | — | ok |
| glitch | gl_error_cascade.carvertemplate | Error cascade | 3 | 90.0 px | Error body 4 / Error ok 4 | 75 | ok |
| glitch | gl_glitch_cut.carvertemplate | Glitch cut | 0 | — | no pairs at rest together | — | ok |
| glitch | gl_lower_third.carvertemplate | Glitch lower third | 1 | 19.7 px | LT name / LT role | 80 | ok |
| glitch | gl_noise_bars.carvertemplate | Noise bars overlay | 0 | — | no pairs at rest together | — | ok |
| glitch | gl_pixel_dissolve.carvertemplate | Pixel dissolve | 0 | — | no pairs at rest together | — | ok |
| glitch | gl_rgb_mark.carvertemplate | RGB split mark | 0 | — | no pairs at rest together | — | ok |
| glitch | gl_rgb_title.carvertemplate | RGB split title | 0 | — | no pairs at rest together | — | ok |
| glitch | gl_slice_shift.carvertemplate | Slice shift | 0 | — | no pairs at rest together | — | ok |
| glitch | gl_stutter_words.carvertemplate | Stutter words | 3 | — | no pairs at rest together | — | ok |
| glitch | gl_terminal.carvertemplate | Terminal type-on | 10 | 24.6 px | Term line 4 / Term cursor | 124 | ok |
| glitch | gl_tracking_band.carvertemplate | Tracking band | 0 | — | no pairs at rest together | — | ok |
| kinetic-typography | kt_beat_words.carvertemplate | Beat words | 6 | — | no pairs at rest together | — | ok |
| kinetic-typography | kt_end_card.carvertemplate | Follow end card | 1 | 96.4 px | Call / Handle | 76 | ok |
| kinetic-typography | kt_focus_pull.carvertemplate | Focus pull | 0 | — | no pairs at rest together | — | ok |
| kinetic-typography | kt_highlight_sweep.carvertemplate | Highlight sweep | 3 | 25.8 px | Part 2 / Part 3 | 61 | ok |
| kinetic-typography | kt_impact_stack.carvertemplate | Impact stack | 3 | 79.7 px | Line 2 / Line 3 | 57 | ok |
| kinetic-typography | kt_line_reveal.carvertemplate | Line reveal | 1 | 66.2 px | Headline / Subline | 45 | ok |
| kinetic-typography | kt_lower_third.carvertemplate | Kinetic lower third | 1 | 55.3 px | Name / Role | 84 | ok |
| kinetic-typography | kt_numbered_list.carvertemplate | Numbered list | 21 | 68.4 px | Item 2 / Item 3 | 89 | ok |
| kinetic-typography | kt_quote.carvertemplate | Kinetic quote | 3 | 125.8 px | Quote mark / Quote | 86 | ok |
| kinetic-typography | kt_split_title.carvertemplate | Split title | 3 | 37.0 px | Line 2 / Dot | 65 | ok |
| kinetic-typography | kt_stat_punch.carvertemplate | Stat punch | 1 | 200.2 px | Number / Label | 60 | ok |
| kinetic-typography | kt_word_swap.carvertemplate | Word swap | 6 | 20.6 px | Static / Word 3 | 106 | ok |
| minimal-luxury | ml_attribute_row.carvertemplate | Attribute row | 9 | 79.3 px | Attribute 1 / Separator 1 | 103 | fixed 2026-10-28 |
| minimal-luxury | ml_collection_title.carvertemplate | Collection title | 1 | 139.6 px | Collection / Season note | 122 | ok |
| minimal-luxury | ml_feather_wipe.carvertemplate | Feather wipe reveal | 0 | — | no pairs at rest together | — | ok |
| minimal-luxury | ml_framed_word.carvertemplate | Framed word | 0 | — | no pairs at rest together | — | ok |
| minimal-luxury | ml_light_sweep.carvertemplate | Light sweep | 0 | — | no pairs at rest together | — | ok |
| minimal-luxury | ml_lower_third.carvertemplate | Luxury lower third | 1 | 76.2 px | Name / Role | 103 | ok |
| minimal-luxury | ml_monogram_end.carvertemplate | Monogram end card | 3 | 53.1 px | Wordmark / Address | 124 | ok |
| minimal-luxury | ml_price_card.carvertemplate | Price card | 3 | 51.4 px | Material / Price | 116 | ok |
| minimal-luxury | ml_product_frame.carvertemplate | Product frame | 0 | — | no pairs at rest together | — | ok |
| minimal-luxury | ml_slow_dip.carvertemplate | Slow dip | 0 | — | no pairs at rest together | — | ok |
| minimal-luxury | ml_slow_quote.carvertemplate | Slow quote | 1 | 57.8 px | Quote / Author | 122 | ok |
| minimal-luxury | ml_tracked_title.carvertemplate | Tracked title | 1 | 104.0 px | Title / Tagline | 97 | ok |
| motion-patterns | mp_info_bar_chart.carvertemplate | Bar chart - grow | 0 | — | no pairs at rest together | — | ok |
| motion-patterns | mp_logo_stamp_reveal.carvertemplate | Logo - stamp reveal | 0 | — | no pairs at rest together | — | ok |
| motion-patterns | mp_lt_accent_bar.carvertemplate | Lower third - accent bar | 1 | 7.6 px | LT role / LT name | 59 | flag: Motion Patterns, left unchanged pending the user's decision ([KI-139](../known-issues.md#ki-139)) |
| motion-patterns | mp_tr_iris.carvertemplate | Colour iris | 0 | — | no pairs at rest together | — | ok |
| motion-patterns | mp_tr_two_tone_wipe.carvertemplate | Two-tone wipe | 0 | — | no pairs at rest together | — | ok |
| retro | rt_arcade_start.carvertemplate | Arcade start screen | 6 | 133.9 px | Arcade score / Arcade title | 83 | ok |
| retro | rt_blinds.carvertemplate | Venetian blinds | 0 | — | no pairs at rest together | — | ok |
| retro | rt_checker_wipe.carvertemplate | Checker wipe | 0 | — | no pairs at rest together | — | ok |
| retro | rt_chrome_title.carvertemplate | Chrome title | 1 | 113.8 px | Chrome word / Chrome sub | 60 | ok |
| retro | rt_groovy_badge.carvertemplate | Groovy badge | 1 | 49.3 px | Badge top / Badge bottom | 58 | ok |
| retro | rt_neon_sign.carvertemplate | Neon sign | 1 | 145.1 px | Neon word / Neon small | 84 | ok |
| retro | rt_rainbow_stripes.carvertemplate | Rainbow stripes | 0 | — | no pairs at rest together | — | ok |
| retro | rt_stripe_lower_third.carvertemplate | 70s stripe lower third | 1 | 20.6 px | LT name / LT role | 83 | fixed 2026-10-28 |
| retro | rt_sunburst_title.carvertemplate | Sunburst title | 1 | 56.7 px | Title / Subtitle | 59 | ok |
| retro | rt_synthwave.carvertemplate | Synthwave sun | 0 | — | no pairs at rest together | — | ok |
| retro | rt_tv_off.carvertemplate | TV switch-off | 0 | — | no pairs at rest together | — | ok |
| retro | rt_vhs_overlay.carvertemplate | VHS overlay | 14 | 20.0 px | REC label / REC dot | 52 | ok |
| saas-ui | su_chart_card.carvertemplate | Chart card | 3 | 197.0 px | Chart title / Bar 1 | 59 | ok |
| saas-ui | su_chat_thread.carvertemplate | Chat thread | 3 | 269.8 px | Message 1 / Message 3 | 97 | ok |
| saas-ui | su_cta_end_card.carvertemplate | CTA end card | 6 | 40.7 px | Wordmark / Tagline | 75 | ok |
| saas-ui | su_cursor_click.carvertemplate | Cursor click | 0 | — | no pairs at rest together | — | ok |
| saas-ui | su_dropdown.carvertemplate | Dropdown menu | 10 | 37.6 px | Item 3 / Item 4 | 64 | ok |
| saas-ui | su_feature_title.carvertemplate | Feature title | 3 | 38.2 px | Headline / Subline | 62 | ok |
| saas-ui | su_kpi_tile.carvertemplate | KPI tile | 3 | 23.9 px | KPI label / KPI value | 56 | ok |
| saas-ui | su_lower_third.carvertemplate | SaaS lower third | 3 | 18.6 px | Name / Role | 84 | fixed 2026-10-28 |
| saas-ui | su_modal.carvertemplate | Modal over app | 6 | 26.8 px | Modal title / Modal body | 55 | ok |
| saas-ui | su_notification_toast.carvertemplate | Notification toast | 3 | 16.0 px | Toast title / Toast icon | 66 | ok |
| saas-ui | su_sidebar_drawer.carvertemplate | Sidebar drawer | 1 | 12.0 px | Header title / Brand dot | 35 | ok: the title is under the open drawer (occluded) |
| saas-ui | su_toggle_switch.carvertemplate | Toggle switch | 0 | — | no pairs at rest together | — | ok |
| social-short-form | ss_before_after.carvertemplate | Before after split (9:16) | 1 | 564.4 px | Before label / After label | 75 | ok |
| social-short-form | ss_caption_pages.carvertemplate | Caption pages (9:16) | 3 | — | no pairs at rest together | — | ok |
| social-short-form | ss_countdown.carvertemplate | Countdown (9:16) | 6 | — | no pairs at rest together | — | ok |
| social-short-form | ss_follow_cta.carvertemplate | Follow end card (9:16) | 3 | 89.7 px | Handle / Button label | 59 | ok |
| social-short-form | ss_highlight_caption.carvertemplate | Highlight caption (9:16) | 3 | 18.1 px | Caption part 1 / Caption part 2 | 54 | ok |
| social-short-form | ss_hook_title.carvertemplate | Hook title (9:16) | 3 | 46.1 px | Hook line 1 / Hook line 2 | 44 | ok |
| social-short-form | ss_listicle.carvertemplate | Listicle (9:16) | 21 | 65.7 px | Badge num 3 / Tip 3 | 122 | ok |
| social-short-form | ss_name_tag.carvertemplate | Name tag (9:16) | 1 | 14.9 px | Tag name / Tag handle | 68 | ok |
| social-short-form | ss_poll.carvertemplate | Poll sticker (9:16) | 10 | 109.2 px | Question / Option 1 | 97 | ok |
| social-short-form | ss_post_card.carvertemplate | Post card (9:16) | 6 | 18.7 px | Post name / Post handle | 83 | fixed 2026-10-28 |
| social-short-form | ss_progress_bar.carvertemplate | Story progress bar (9:16) | 0 | — | no pairs at rest together | — | ok |
| social-short-form | ss_swipe_up.carvertemplate | Swipe up (9:16) | 0 | — | no pairs at rest together | — | ok |
| sports | sp_full_time.carvertemplate | Full-time score | 10 | 119.2 px | FT score / FT scorers | 79 | ok |
| sports | sp_goal_slam.carvertemplate | GOAL slam | 0 | — | no pairs at rest together | — | ok |
| sports | sp_head_to_head.carvertemplate | Head to head stats | 45 | 93.9 px | H2H title / Row label 1 | 49 | ok |
| sports | sp_lineup.carvertemplate | Starting lineup | 120 | 74.7 px | Num 5 / Player 5 | 97 | ok |
| sports | sp_lower_third.carvertemplate | Player lower third | 3 | 31.0 px | LT name / LT stat | 81 | ok |
| sports | sp_match_up.carvertemplate | Match up | 6 | 193.9 px | Team 1 / Match info | 61 | ok |
| sports | sp_player_card.carvertemplate | Player card | 3 | 54.4 px | Name / Position | 57 | ok |
| sports | sp_replay_stinger.carvertemplate | Replay stinger | 0 | — | no pairs at rest together | — | ok |
| sports | sp_score_bug.carvertemplate | Score bug | 10 | 60.6 px | Team B / Clock | 67 | ok |
| sports | sp_slash_wipe.carvertemplate | Slash wipe | 0 | — | no pairs at rest together | — | ok |
| sports | sp_spotlight.carvertemplate | Player spotlight | 1 | 52.9 px | Spot name / Spot arrow | 70 | ok |
| sports | sp_standings.carvertemplate | Standings table | 120 | 55.0 px | Cell 1.2 / Cell 2.2 | 86 | ok |
| transitions | tx_bars_stagger.carvertemplate | Bars stagger | 0 | — | no pairs at rest together | — | ok |
| transitions | tx_bubble_cover.carvertemplate | Bubble cover | 0 | — | no pairs at rest together | — | ok |
| transitions | tx_clock_wipe.carvertemplate | Clock wipe | 0 | — | no pairs at rest together | — | ok |
| transitions | tx_diagonal_wipe.carvertemplate | Diagonal wipe | 0 | — | no pairs at rest together | — | ok |
| transitions | tx_dip_to_colour.carvertemplate | Dip to colour | 0 | — | no pairs at rest together | — | ok |
| transitions | tx_slide_wipe.carvertemplate | Slide wipe | 0 | — | no pairs at rest together | — | ok |
| transitions | tx_split_doors.carvertemplate | Split doors | 0 | — | no pairs at rest together | — | ok |
