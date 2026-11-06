# Sports pack (`sp_`)

High-energy match graphics: slash-ins, impact slams, zoom-past exits, a score bug with a rolling score change, a player card, head-to-head stat bars and a GOAL slam.

The pack lives in `library/templates/sports/`. Install it as in [Installing a pack](README.md#installing-a-pack).

- The presets are built by `ai/scripts/motion/build_sports_pack.py` (multi-segment tracks).
- The templates come from `categories/sports/sp-lab`, written by `ai/scripts/motion/sports_lab.py`.
- The sample reel is `categories/sports/sp-showcase`.

**Status: verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test).**
- Public release binary, headless, isolated folders; the pack was added to a scratch copy's bundled Library ([FR-036](../references/known-issues.md#fr-036)).
- Lint was 0 errors and 0 warnings on every lab comp and the preset bench, and 0/0/0 on the showcase.
- qc at 240 px found no flashes.
- Each template was placed into a fresh comp: lint 0/0/0 for all four.

**Fonts:** Rethink Sans must be installed ([KI-136](../references/known-issues.md#ki-136)).

Style:
- Dark navy `#0B1020`; team red `#E63946` and blue `#1D7CF2`; highlight yellow `#FFD60A`.
- Diagonals everywhere (slanted panels, slash entrances), and fast: 8–14 f moves.
- One hit per beat, with the SFX on the impact frame.

## Presets (3)

| Name in Library | File | Anchor / frames | What moves | Measured | Use for |
|---|---|---|---|---|---|
| Slash in | sp_slash_in | in / 10 | centre from (−22% W, −12% H) diagonally to rest, hard expo; fade 0–20% | settles **f7** | panels, names, titles |
| Impact slam | sp_impact_slam | in / 12 | size 220% → 92% accelerating (impact at f5), then spring back to 100% | **6.7% overshoot past the impact; settles f8** | scores, GOAL, numbers |
| Zoom past | sp_zoom_past | out / 8 | size → 300% and fade, accelerating | the last 8 f | the exit before a hard cut |

## Templates (4)

| Pattern | File / doc | Length |
|---|---|---|
| Score bug | sp_score_bug / [sp-score-bug.md](sp-score-bug.md) | 120 f, score change at f52–68 |
| Player card | sp_player_card / [sp-player-card.md](sp-player-card.md) | 90 f |
| Head to head stats | sp_head_to_head / [sp-head-to-head.md](sp-head-to-head.md) | 90 f |
| GOAL slam | sp_goal_slam / [sp-goal-slam.md](sp-goal-slam.md) | 60 f, impact at f9 |

## Templates added in round 2 (8)

| Pattern | File / doc | Length |
|---|---|---|
| Player lower third | sp_lower_third / [sp-lower-third.md](sp-lower-third.md) | 150 f, exit in the last 8–12 f |
| Match up | sp_match_up / [sp-match-up.md](sp-match-up.md) | 90 f, VS at f12 |
| Standings table | sp_standings / [sp-standings.md](sp-standings.md) | 150 f |
| Full-time score | sp_full_time / [sp-full-time.md](sp-full-time.md) | 120 f |
| Starting lineup | sp_lineup / [sp-lineup.md](sp-lineup.md) | 150 f |
| Player spotlight (overlay) | sp_spotlight / [sp-spotlight.md](sp-spotlight.md) | 120 f |
| Replay stinger (transition) | sp_replay_stinger / [sp-replay-stinger.md](sp-replay-stinger.md) | 45 f |
| Slash wipe (transition) | sp_slash_wipe / [sp-slash-wipe.md](sp-slash-wipe.md) | 30 f, cut at f15 |

Round 2 was built and verified the same way on 2026-10-27: every lab comp lints 0 errors / 0 warnings, and each template placed into a fresh comp lints 0/0/0. Clip-id prefixes: `slt_`, `smu_`, `sst_`, `sft_`, `slu_`, `ssp_`, `srs_`, `ssw_`. Lab: `categories/sports/sp-lab-2`, written by `ai/scripts/motion/sports_lab2.py`.

## Sample reel

`categories/sports/sp-showcase` is a 300 f (10 s) master. The score bug and GOAL slam overlays play over a pitch stand-in (a green gradient), timed so that GOAL! lands at f58 just as the score starts to roll. Then the player card and head-to-head follow. Lint 0/0/0.

## Round-2 sample film

`categories/sports/sp-showcase-2` is a 780 f (26 s) master at 1920 × 1080 that plays the round-2 templates back to back with Slash wipe on one cut, placed from the Library with `library.place` + `template.apply` (rebuild: `ai/scripts/motion/recipes/showcase2.py sports`). Verified 0.1.6 (rev 1105), 2026-10-28: master lint 0 / 0 / 0. Qc (240 px) notes five holds as freezes (over real footage the picture moves underneath).

## Round 3: briefs the pack could not serve before

Chosen from [reading a brief](../references/craft/reading-a-brief.md) ("live match graphics, transfer news, a cup run") against what rounds 1 and 2 cover (the score bug and the standings table exist, so the score bug here adds a running clock and the table here shows a movement, not a static list). Built and verified on 0.1.6 (rev 1105) on 2026-10-28. Every move is baked as keys in `sports_lab3.py` (no presets to apply): `slash()` writes the pack's Slash in, `slam()` its Impact slam and `grow_x()` a bar growing from its left edge. Text that must read on the ground uses colours converted with the renderer's BT.709 curve ([KI-141](../references/known-issues.md#ki-141)); white text on the red and blue team panels is 36 px or larger. Teams, players, leagues, venues and scores are invented. Frames are comp frames. Clip-id prefixes: `slc_`, `ssu_`, `ssg_`, `stb_`, `sbr_`, `stm_`, `sfx_`, `smd_`.

| Template | Brief it serves | Measured | Overshoot | Lint (lab, contrast:true) | Placed |
|---|---|---|---|---|---|
| Live score clock ([sp-live-clock.md](sp-live-clock.md)) | live score bug with a timer, added time | boxes f0–19 (3 f apart); clock steps every 30 f from f20 (44:56 to 45:01); added-time tab f140–150, settles f147 | 0% | 0 / 0 / 0 | 0 / 0 / 0 |
| Substitution card ([sp-substitution.md](sp-substitution.md)) | substitution, player change | header settles f7; OFF row f8, arrow settles f21; ON row f22, name settles f34; exit f140–148 | 0% | 0 / 0 (13 notes) | 0 / 0 / 0 |
| Signing announcement ([sp-signing.md](sp-signing.md)) | transfer news, new signing | photo panel f7; name f19; contract bar f55; SIGNED stamp on f64, settles f72 | 16% (stamp, keyed from 150%) | 0 / 0 / 0 | 0 / 0 / 0 |
| Touchdown burst ([sp-touchdown-burst.md](sp-touchdown-burst.md)) | touchdown, try, celebration | sunbursts settle f13; slam f6, settles f13; 28 confetti f11–76; score strip settles f29 | 6.7% slam, 9.8% sunburst | 0 / 0 (28 notes) | 0 / 0 / 0 |
| Tournament bracket ([sp-bracket.md](sp-bracket.md)) | cup bracket, knockout stage | quarter-finals f4–50, semi-finals f58–98, final f102–128; CHAMPION slam f140, settles f147 | 6.7% (champion) | 0 / 0 / 0 | 0 / 0 / 0 |
| League table movement ([sp-table-move.md](sp-table-move.md)) | league table update, promotion climb | points 44 → 47 on f48; row out f56–66, climbs f66–86, back f86–96, settles f92; +3 badge settles f105 | 0% on the climb; 6.7% on the points slam | 0 / 0 (14 notes) | 0 / 0 / 0 |
| Fixture list ([sp-fixtures.md](sp-fixtures.md)) | this weekend's fixtures, kick-off times | panels f8–33, 5 f apart; VS chips settle f19+; LIVE tags f64 and f74, settle f71 | 6.7% (chip, tag) | 0 / 0 / 0 | 0 / 0 / 0 |
| Match-day poster ([sp-match-day.md](sp-match-day.md)) | match day promo, fixture poster | bands settle f8; slam f6, settles f13; crests f20 / f26, settle f31; VS f36; info bar settles f53 | 6.7% slam, 9.8% crests | 0 / 0 / 0 | 0 / 0 / 0 |

Notes are `repeated_key_value` on holds (the opacity before an exit, the confetti's) and `speed_jump` where the table row starts its move; intended. `inspect qc` at 240 px found no flashes on any round-3 comp (long holds read as freezes). Each template was checked with the text-gap audit (`audit_text_gaps.py`): no flags, except the Fixture list's VS text sitting on its own chip (intended); the closest other pair is 13 px (the table's +3 and its arrow). Full-frame looks of every placed template at its widest moving frame and its last frame show nothing cut ([KI-144](../references/known-issues.md#ki-144)), and every text sits inside its panel ([KI-157](../references/known-issues.md#ki-157)).

### Round-3 pitfalls
1. **Tracked caps are far wider than `textw` says.** The signing contract line (34 px, tracking 1.2) measures 562 px and the match-day info line (38 px, tracking 1.15) 1000 px; bars sized from `textw` cut off "2030" and "SU...IUM", and dark text off its yellow bar is invisible on the dark ground. Lint does not check text against its panel ([KI-157](../references/known-issues.md#ki-157)); measure with `carvercat_authoring geometry` and look at every panel.
2. **A slam from 220% on a stamp overlaps its neighbours in lint** (`text_overlap` 19%, SIGNED over FROM club). Start a stamp at 150% (16% past 100%), and put it on a dark plate so yellow reads on red.
3. **A name that slashes in across its own number fails `text_overlap` while it passes** (26%). Bring it in from the right (`from_right`), or start it after the number settles.
4. **A changing number needs reading time on both sides.** The table's 44 showed 14 f and failed `reading_time`; 28 f passes. A clock is one clip per second, each 30 f ([KI-051](../references/known-issues.md#ki-051)).
5. **Move the mover out of the column first.** The climbing row steps 240 px right, rises three places and steps back, so it never passes another row's text; the rows it passes drop one place meanwhile.
6. **Confetti is baked.** 28 rectangles on Linear keys every 2 f (throw, 6% drag a frame, gravity, one-way spin) read as a burst; `inspect curves` overshoot on baked lanes means nothing ([KI-152](../references/known-issues.md#ki-152)).
7. **A 3-gon points right.** Rotate +90 for an up arrow, −90 for down ([KI-150](../references/known-issues.md#ki-150)).
8. **Text on its own chip is flagged by the text-gap audit** (the VS label, −46 px); that is the label, not a collision.

## Pitfalls (0.1.6)

1. **Rolling one number into another through a window:** the outgoing text must be gone before the incoming one starts. Otherwise lint flags `text_overlap` (34% here), because it does not see the mask. Old exits f52–58, new enters f58–68.
2. **Outlined numbers:** set `text.fill` Paint to none and give `text.outline` Paint solid with a thickness (0.025 here).
3. **Bars from a centre line:** the left bar uses `transformOrigin "100% 50%"` (stored anchor [1, 0]; grows left), the right bar `"0% 50%"` (stored [−1, 0]; grows right), both on the same curve and frames.
4. **Big hits overlap neighbours.** Impact slam (220%) and Zoom past (300%) on text next to other text fail `text_overlap`; slam the hero only, fade the rest out.
5. **Mind the slide path.** Slash in comes from the lower left; a text that slides across another text's spot must start after it has passed.

Inspiration: common broadcast sports graphics conventions (score bugs, line-up cards, head-to-head stats). No external text or code was used.
