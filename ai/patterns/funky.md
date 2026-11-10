# Funky pack (`fk_`)

Bold, playful graphic motion: tilt pops, wiggles and spins, Memphis-style shapes, an offset-shadow title, a zigzag snake and slapped-down stickers. Round 3 adds a gig poster, a menu special, a new-drop reveal, marquee bands, a blob photo frame, a party invite, a countdown and a zine quote. For youth brands, events, music, food and anything that should feel loud and fun.

The pack lives in `library/templates/funky/`. Install it as in [Installing a pack](README.md#installing-a-pack).

- The presets are built by `ai/scripts/motion/build_funky_pack.py`, using the multi-segment `track()` builder.
- The templates come from `categories/funky/fk-lab`, written by `ai/scripts/motion/funky_lab.py`; round 2 from `categories/funky/fk-lab-2` (`funky_lab2.py`); round 3 from `categories/funky/fk-lab-3` (`funky_lab3.py`).
- The sample reel is `categories/funky/fk-showcase`.

**Status: verified 0.1.8.1 (rev 1127; headless, isolated folders, pack added to a scratch user Library), measured by `ai/scripts/motion/verify_pack.py funky` (fixed harness with the object-level checks).**
- The labs (`funky_lab.py`, `_lab2.py`, `_lab3.py`) and the showcase (`funky_showcase.py`) speak design units (`json_author/cc2.py`: px from the top-left, y down, degrees clockwise, CSS colours and easing) and are sent with `scene.apply`; library presets are applied with `preset.apply`; the blob frame's mask is a scene mask (its window is unparented again). `regen_pack.py` rebuilds the 20 templates and the lab and showcase projects (carvercat/2); a second run leaves `git status` unchanged (confirmed on the final commit). The preset files stay in the stored preset format; all four (Tilt pop, Slide in - wiggle, Spin in, Spin out) load and apply in 0.1.8.1.
- Each template was placed into a fresh 16:9 comp and a fresh 9:16 comp: lint 0 errors / 0 warnings / 0 notes for all 20; qc found no flashes.
- Against the v1 originals (7 frames each, text templates at 960 x 540): silhouettes match for 20 of 20 (worst 1.54 %, new-drop reveal; limit 2 %). Colours are exactly the stated hex values (colour shift 2-36, the menu special highest). Orbit end card: its lab comp is now named `FK Orbit end` so that the template regenerates from it.
- A real fault found by those numbers and fixed: the old kit stored a shadow's offset x against the frame width and y against the frame height, so every "12, 12" hard shadow was drawn 12 px right and 6.75 px down (measured on the old renders: shadow edges 6 px higher than the new ones at 1920). The lab drew a square 12 x 12 shadow. `hard_shadow` now draws dy = dx x 9/16 (the keyed shadows of the offset title 14 -> 14 / 7.875 and the new drop's panel 22 -> 22 / 12.375, the soft sticker and photo shadow 11.5 -> 6.48 down), and the new-drop reveal fell from 2.02 % to 1.54 %, the party invite headline overlap from 0.16 to 0.96, the offset title from 0.10 to 1.00.
- Object-level check: 20 of 20 pass (no object missing, empty or moved), run with `ai/scripts/motion/verify_pack.py`, which makes the two ink masks of one object use one background colour. The blob frame's name sits on a yellow plate: yellow and dark letters cover about the same area (3137 and 3125 pixels), the harness takes each crop's own dominant colour, it flipped between the old and new render and the overlap read 0.08 although no pixel differs by more than 48/255 (with one background the overlap is 0.995; the final run reads 0.95). With one mask colour per crop (the old harness behaviour) it lists the blob frame as FAIL.
- Final harness table (funky, 0.1.8.1 rev 1127; columns as on the Cartoon Bounce page):

| Template | lint 16:9 | lint 9:16 | flashes | worst shape % | colour shift | objects | box offset px | worst ink IoU |
|---|---|---|---|---|---|---|---|---|
| Blob photo frame | 0/0/0 | 0/0/0 | 0 | 0.01 | 19 | pass | 0.2 | 0.95 |
| Funky countdown | 0/0/0 | 0/0/0 | 0 | 0.00 | 13 | pass | 0.0 | 1.00 |
| Gig poster | 0/0/0 | 0/0/0 | 0 | 0.68 | 14 | pass | 4.0 | 0.68 |
| Funky lower third | 0/0/0 | 0/0/0 | 0 | 0.00 | 10 | pass | 0.0 | 0.98 |
| Marquee bands | 0/0/0 | 0/0/0 | 0 | 0.01 | 6 | pass | 1.4 | 0.92 |
| Memphis shapes | 0/0/0 | 0/0/0 | 0 | 0.02 | 7 | pass | 0.0 | - |
| Menu special | 0/0/0 | 0/0/0 | 0 | 0.58 | 36 | pass | 3.0 | 0.79 |
| New drop reveal | 0/0/0 | 0/0/0 | 0 | 1.54 | 13 | pass | 10.3 | 0.66 |
| Offset shadow title | 0/0/0 | 0/0/0 | 0 | 0.01 | 5 | pass | 0.0 | 1.00 |
| Orbit end card | 0/0/0 | 0/0/0 | 0 | 0.00 | 9 | pass | 0.0 | 1.00 |
| Party invite | 0/0/0 | 0/0/0 | 0 | 0.01 | 8 | pass | 0.3 | 0.96 |
| Pattern drift | 0/0/0 | 0/0/0 | 0 | 0.00 | 2 | pass | 0.0 | - |
| Photo stack | 0/0/0 | 0/0/0 | 0 | 0.01 | 4 | pass | 0.0 | - |
| Sale badge | 0/0/0 | 0/0/0 | 0 | 0.00 | 8 | pass | 0.0 | 1.00 |
| Squiggle underline | 0/0/0 | 0/0/0 | 0 | 0.05 | 11 | pass | 0.0 | 1.00 |
| Star cover | 0/0/0 | 0/0/0 | 0 | 0.01 | 4 | pass | 0.0 | - |
| Sticker stack | 0/0/0 | 0/0/0 | 0 | 0.01 | 6 | pass | 0.0 | 0.99 |
| Swing headline | 0/0/0 | 0/0/0 | 0 | 0.01 | 8 | pass | 0.0 | 1.00 |
| Zigzag ribbon | 0/0/0 | 0/0/0 | 0 | 0.13 | 8 | pass | 0.0 | - |
| Zine quote | 0/0/0 | 0/0/0 | 0 | 0.03 | 8 | pass | 1.0 | 0.98 |

- Things the conversion changed on purpose: the named eases are the app's model curves (Ease in (1/3, 0, 2/3, 1/3), Ease out (1/3, 2/3, 2/3, 1), S-curve (1/3, 0, 2/3, 1)); a corner radius is capped at a quarter of the short side, as the old kit drew it; a rotate key stops at 360 deg, so the party invite's confetti turn at most 360 (the old 420 was capped).
- Numbers on these pages that come from the keys (overshoot percentages, "settles" frames of the presets and stamps) are unchanged: the keys are the same.

**Fonts:** Rethink Sans must be installed ([KI-136](../references/known-issues.md#ki-136)).

Style:
- Peach ground `#FFE8D6`, ink `#1B1035`; purple, orange, pink, teal and yellow at full saturation.
- Rotation is part of every entrance.
- After landing, things keep turning slowly **one way**: never a back-and-forth loop, which lint reads as jitter.

## Presets (4)

Measured on a 40 f clip that starts at frame 10.

| Name in Library | File | Anchor / frames | What moves | Measured | Use for |
|---|---|---|---|---|---|
| Tilt pop | fk_tilt_pop | in / 18 | scale 0 → 1 (bouncy spring), rotate +14° → 0 (wobbly spring), fade 0–15% | size **16.2%**, angle **30.9%** overshoot; settles **f16** | shapes, stickers, titles |
| Slide in - wiggle | fk_slide_wiggle | in / 24 | x +40% W → 0 (expo over the first 60%), rotate −12° → 0 (wobbly) | lands **f10**; angle **30.3%**, settles **f19** | cards and props arriving from the right |
| Spin in | fk_spin_in | in / 20 | rotate +180° → 0 (expo), scale 0.3 → 1 (gentle spring), fade 0–20% | angle settles **f16**; size 4.4%, settles **f18** | badges, logos, icons |
| Spin out | fk_spin_out | out / 14 | rotate 0 → −90°, scale 1 → 0, accelerating | the last 14 f | the exit for Tilt pop and Spin in |

## Templates (4)

| Pattern | File / doc | Length |
|---|---|---|
| Memphis shapes | fk_memphis_shapes / [fk-memphis-shapes.md](fk-memphis-shapes.md) | 90 f |
| Offset shadow title | fk_offset_title / [fk-offset-title.md](fk-offset-title.md) | 90 f |
| Zigzag ribbon | fk_zigzag_ribbon / [fk-zigzag-ribbon.md](fk-zigzag-ribbon.md) | 60 f |
| Sticker stack | fk_sticker_stack / [fk-sticker-stack.md](fk-sticker-stack.md) | 75 f |

## Templates added in round 2 (8)

| Pattern | File / doc | Length |
|---|---|---|
| Funky lower third | fk_lower_third / [fk-lower-third.md](fk-lower-third.md) | 150 f, spins out in the last 14 f |
| Sale badge | fk_sale_badge / [fk-sale-badge.md](fk-sale-badge.md) | 90 f |
| Swing headline | fk_swing_headline / [fk-swing-headline.md](fk-swing-headline.md) | 90 f |
| Pattern drift (background) | fk_pattern_drift / [fk-pattern-drift.md](fk-pattern-drift.md) | 150 f |
| Squiggle underline | fk_squiggle_underline / [fk-squiggle-underline.md](fk-squiggle-underline.md) | 90 f |
| Orbit end card (rigged) | fk_orbit_end / [fk-orbit-end.md](fk-orbit-end.md) | 150 f |
| Photo stack | fk_photo_stack / [fk-photo-stack.md](fk-photo-stack.md) | 120 f |
| Star cover (transition) | fk_star_cover / [fk-star-cover.md](fk-star-cover.md) | 36 f, cut at f18 |

Round 2 was built and verified the same way on 2026-10-27: every lab comp lints 0 errors / 0 warnings, and each template placed into a fresh comp lints 0/0/0. Clip-id prefixes: `flt_`, `fsb_`, `fsw_`, `fpd_`, `fsq_`, `foe_`, `fps_`, `fsc_`. Lab: `categories/funky/fk-lab-2`, written by `ai/scripts/motion/funky_lab2.py`.

## Round 3: briefs the pack could not serve before

Chosen from [reading a brief](../references/craft/reading-a-brief.md) ("sale, offer, youth brand, event promo") and the wiki's [event openers](../../wiki/genres/event-openers.md), [social ads](../../wiki/genres/social-ads.md) and [product launches](../../wiki/genres/product-launches.md) pages, against what rounds 1 and 2 already cover (shapes, titles, stickers, a sale badge, a lower third, an end card): the music-event, food, drop, party and quote briefs a youth brand or venue asks for, plus a scrolling band, a shaped photo frame and a countdown. Built and verified on 0.1.6 (rev 1105) on 2026-10-28. Every move is baked as keys in `funky_lab3.py`: `stamp()` (the round-1 sticker slam with a turn), `pop()` (Tilt pop on the pop curve), `slide_in()` (Slide in - wiggle) and `spin_in()` (Spin in), so there is nothing to apply after `edit.open`; the blob frame has one mask window made with `mask.make`. Stamps land with **9.3–9.8%** overshoot, shape pops with **15.8%**, the style's bounce; everything that keeps moving after landing turns or scrolls one way. Names, dates, prices and pictures are invented stand-ins. Frames are comp frames. Clip-id prefixes: `fgp_`, `fmn_`, `fnd_`, `fmq_`, `fbf_`, `fpi_`, `fcd_`, `fzq_`.

| Template | File / doc | Brief it serves | Measured | Lint (lab) | Placed |
|---|---|---|---|---|---|
| Gig poster | fk_gig_poster / [fk-gig-poster.md](fk-gig-poster.md) | gig, club night, live-music announcement | record lands f10; act lines f15 / f27 (9.8%); date f30; venue f41; 150 f | 0 / 0 / 0 | 0 / 0 / 0 |
| Menu special | fk_menu_special / [fk-menu-special.md](fk-menu-special.md) | today's special, lunch deal, new dish | ribbon f7; dish f19 / f24; plate f21; price badge f36 (15.8%); pill f44; 150 f | 0 / 0 / 0 | 0 / 0 / 0 |
| New drop reveal | fk_new_drop / [fk-new-drop.md](fk-new-drop.md) | streetwear or merch drop, collection release | NEW / DROP f11 / f21; panel lands f19 (angle 15.8%, f27); slab f31; tape f29; 120 f | 0 / 0 / 0 | 0 / 0 / 0 |
| Marquee bands | fk_marquee_bands / [fk-marquee-bands.md](fk-marquee-bands.md) | scrolling ticker, crossing tape bands | bands f8 / f14; words linear, one copy cycle per 150 f (seamless) | 0 / 0 / 0 | 0 / 0 / 0 |
| Blob photo frame | fk_blob_frame / [fk-blob-frame.md](fk-blob-frame.md) | meet the team, guest intro, profile photo | blob window f13 (15.8%, mask); name f26; role f37; 120 f | 0 / 0 / 0 | 0 / 0 / 0 |
| Party invite | fk_party_invite / [fk-party-invite.md](fk-party-invite.md) | birthday or launch party, "you're invited", RSVP | headline f13; pills f30 / f36 / f42; RSVP f51; confetti in side lanes; 150 f | 0 / 0 / 0 | 0 / 0 / 0 |
| Funky countdown | fk_countdown / [fk-countdown.md](fk-countdown.md) | 3-2-1-go into a drop or a show (16:9) | per 30 f beat: burst f10 (15.8%), number f8 (9.3%); hard cuts; 120 f | 0 / 0 / 0 | 0 / 0 / 0 |
| Zine quote | fk_zine_quote / [fk-zine-quote.md](fk-zine-quote.md) | loud quote, DIY / zine look, fan testimonial | words f12 to f42, 6 f apart; tape f54; credit f55; 150 f | 0 / 0 / 0 | 0 / 0 / 0 |

Each template placed into a fresh comp applied "at 1920 x 1080" and linted 0/0/0. The text-gap audit (`audit_text_gaps.py`) flags nothing (closest pair 24.6 px, NEW / DROP, with their shadows between). Full-frame looks of the placed instances (8 frames each, plus single frames of the record and panel coming in from outside the frame, the scrolling bands, the turning blob window and the confetti) show nothing cut ([KI-144](../references/known-issues.md#ki-144)).

### Round-3 pitfalls
1. **Stacked big lines cannot slam from 1.45.** The sticker slam on a 160 px line under a 48 px kicker grew over the kicker (`text_overlap` 100%) and the next line (71%), and a 10° turn on a 660 px line made `speed_jump` notes (12.9 → 1.0 px/frame). Slam big lines from 1.15 with a 4° turn over 12 f, and start the next line after the previous one lands.
2. **No second key on the landing frame.** A drift that starts on the frame where the entrance's last rotation key sits writes two keys on one frame: lint **error** `same_frame_keys`. Let the drift add only its end key (`drift_spin()`).
3. **Long scrolling texts fail reading time.** One text of 85 characters needs 150 opaque frames; split a marquee into one clip per word (25 f each), spaced by `cc.textw`.
4. **A word that is on screen only while transparent is `never_visible`** (error). Keep only clips that are on screen after their fade.
5. **Lint does not see confetti over text** ([KI-138](../references/known-issues.md#ki-138)): a falling piece crossing a detail pill (−6.9 px) was found only by the text-gap audit. Keep decorations in lanes outside the text.
6. **Overshoot is per move** ([KI-152](../references/known-issues.md#ki-152)): a spark's entrance plus its drift on one rotation lane read 28.6%; quote the one-move lanes (the size pops).
7. **Ink parts vanish on dark grounds.** Venue lines, credits, the blob ring and outlines are ink (`#1B1035`), drawn for the peach ground; over dark footage recolour them.

## Sample reel

`categories/funky/fk-showcase` is a 315 f (10.5 s) master: Memphis shapes → offset title → sticker stack → zigzag ribbon. Lint 0/0/0. QC notes two holds as "freezes" (f26–89, f109–179): the 25° drift turns are under its 96 px threshold.

## Round-2 sample film

`categories/funky/fk-showcase-2` is a 690 f (23 s) master at 1920 × 1080 that plays the round-2 templates back to back with Star cover on one cut, placed from the Library with `library.place` + `template.apply` (rebuild: `ai/scripts/motion/recipes/showcase2.py funky`). Rebuilt and verified 0.1.8.1 (rev 1127), 2026-11-07, as a `carvercat/2` file from the corrected templates: master lint 0 / 0 / 0. Qc (240 px) notes three holds as freezes (f19-89, f292-405, f455-539).

## Pitfalls (0.1.6)

1. **Two overlapping texts for a shadow fail lint** (`text_overlap` 100%). Use the native **Drop shadow** on the same text: `dropShadow` with blur 0 and alpha 1 in the colour you want, and key its offset x/y to make it step out.
2. **A preset and your own keys can share a property.** Tilt pop's angle keys (0–18 f) and a later linear drift on the same rotation track coexist (15 keys, measured).
3. **No looping bobs or wiggles after landing.** Use one-way drifts.
4. **Tilt pop and Spin in start text small.** Measured: Tilt pop failed lint `text_too_small` on 48 px and 110 px text and passed on 150 px and 240 px. Use Stamp and add a small rotation key for the style's turn.
5. **Shapes that never enter the frame are a lint error** (`never_visible`). Cull pattern cells whose whole path is off frame.

Inspiration: Memphis-design and retro-pop motion conventions. No external text or code was used.
