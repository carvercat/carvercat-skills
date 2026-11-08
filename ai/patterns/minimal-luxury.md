# Minimal Luxury pack (`ml_`)

Slow, quiet and expensive: long fades, drifts, wide-tracked caps, a feathered wipe, a drawn product frame, a slow quote, a lower third, a monogram end card, a price card, a collection title, a light sweep, an attribute row, a framed word and a slow dip. Round 3 adds material swatches, a property feature, a collection index, fragrance notes, a save-the-date, a boutique address, a limited-edition number and an editorial spread. For fashion, fragrance, jewellery, hospitality and premium products.

The pack lives in `library/templates/minimal-luxury/`. Install it as in [Installing a pack](README.md#installing-a-pack).

- The presets are built by `ai/scripts/motion/build_minimal_luxury_pack.py`.
- The templates come from `categories/minimal-luxury/ml-lab` (written by `ai/scripts/motion/minimal_luxury_lab.py`) and, for round 2, `categories/minimal-luxury/ml-lab-2` (written by `ai/scripts/motion/minimal_luxury_lab2.py`), and for round 3, `categories/minimal-luxury/ml-lab-3` (written by `ai/scripts/motion/minimal_luxury_lab3.py`).
- The sample film is `categories/minimal-luxury/ml-showcase`, written by `ai/scripts/motion/minimal_luxury_showcase.py`.

**Status: Verified 0.1.8.1 (rev 1127).**
- Headless `carvercat-host` built from Carvercat 0.1.8.1 (rev 1127), fresh preferences, data and cache folders; the pack was installed into a scratch user Library. Measured with `ai/scripts/motion/verify_pack.py minimal-luxury` (full table below).
- Every template placed into a fresh 16:9 and a fresh 9:16 comp: lint 0 errors / 0 warnings / 0 notes, no flashes (qc), for all 20 templates.
- Shape against the v1 original (7 frames; limit 2 %): all 20 pass, worst 1.72 % (Collection title). The object-level check (missing, empty, moved, text objects) passes for all 20. No `--ink-templates` was needed.
- The showcase-2 master lints 0 / 0 / 0 (rebuilt by `ai/scripts/motion/recipes/showcase2.py minimal-luxury`). The per-part "settles" figures in the pages are the authored key frames and curves; they were not re-measured one by one.

**Fonts:** Rethink Sans must be installed. It is a free Google Font (SIL OFL), and the file is also in `ai/scripts/motion/json_author/RethinkSans.ttf`. Without it, text falls back to Arial ([KI-136](../references/known-issues.md#ki-136)).

Style rules:
- Everything is slower than you think: entrances 30–60 f, exits 30 f.
- No overshoot and no springs; decelerate and S curves (`cubic-bezier(0.333, 0, 0.667, 1)`) only.
- One metallic accent (gold `#C8A96A`) on warm black `#0E0D0B`, ivory type `#EDE6D6`.
- Wide tracking: caps at 1.35–1.8, small captions at 1.4–1.5.
- Lots of empty frame. Every hold keeps moving very slightly: a drift, a tracking breathe, or a 2% push.

## Presets (3)

| Name in Library | File | Anchor / frames | What moves | Measured | Use for |
|---|---|---|---|---|---|
| Slow fade in | ml_slow_fade | in / 36 | opacity 0 → 1 over the whole 36 f (standard), scale 1.03 → 1 (strong decelerate) | size settles **f28**, opacity **f32** | titles, products, logos, captions |
| Drift up - 4 s | ml_drift_up | in / 120 | y +0.6% H → 0, linear | linear over 120 f | holds; can sit on the same clip as Slow fade in |
| Slow fade out | ml_slow_fade_out | out / 30 | opacity 1 → 0 (standard), scale 1 → 1.015 | opacity reaches 0 about 4 f before the clip end | exits |

## Templates (20)

| Pattern | File / doc | Length |
|---|---|---|
| Tracked title | ml_tracked_title / [ml-tracked-title.md](ml-tracked-title.md) | 120 f |
| Feather wipe reveal | ml_feather_wipe / [ml-feather-wipe.md](ml-feather-wipe.md) | 75 f |
| Product frame | ml_product_frame / [ml-product-frame.md](ml-product-frame.md) | 120 f |
| Slow quote | ml_slow_quote / [ml-slow-quote.md](ml-slow-quote.md) | 150 f |
| Luxury lower third | ml_lower_third / [ml-lower-third.md](ml-lower-third.md) | 180 f, exit f140–180 |
| Monogram end card | ml_monogram_end / [ml-monogram-end.md](ml-monogram-end.md) | 150 f |
| Price card | ml_price_card / [ml-price-card.md](ml-price-card.md) | 150 f |
| Collection title | ml_collection_title / [ml-collection-title.md](ml-collection-title.md) | 150 f |
| Light sweep (gleam through a text mask) | ml_light_sweep / [ml-light-sweep.md](ml-light-sweep.md) | 120 f, gleam f30–110 |
| Attribute row | ml_attribute_row / [ml-attribute-row.md](ml-attribute-row.md) | 150 f |
| Framed word | ml_framed_word / [ml-framed-word.md](ml-framed-word.md) | 150 f |
| Slow dip (transition) | ml_slow_dip / [ml-slow-dip.md](ml-slow-dip.md) | 60 f, cut at f30 |
| Material swatches | ml_swatch_card / [ml-swatch-card.md](ml-swatch-card.md) | 180 f, swatches f16–80, sheen f70–170 |
| Property feature | ml_property_feature / [ml-property-feature.md](ml-property-feature.md) | 180 f, window f0–54 (mask), details f70–130 |
| Collection index | ml_collection_index / [ml-collection-index.md](ml-collection-index.md) | 210 f, rows f24–112, choice f150–180 |
| Fragrance notes | ml_fragrance_notes / [ml-fragrance-notes.md](ml-fragrance-notes.md) | 180 f, tiers f10–120, product f100 |
| Save the date | ml_invitation / [ml-invitation.md](ml-invitation.md) | 180 f, frame f0–66, copy f24–120 |
| Boutique address | ml_boutique_address / [ml-boutique-address.md](ml-boutique-address.md) | 180 f, pin f0–40, copy f24–116 |
| Limited edition number | ml_limited_edition / [ml-limited-edition.md](ml-limited-edition.md) | 150 f, number f12–66 (mask) |
| Editorial spread | ml_editorial_spread / [ml-editorial-spread.md](ml-editorial-spread.md) | 180 f, photo f0–60 (feathered mask), copy f30–126 |

Round 2 (8 templates) was built and verified the same way on 2026-10-27: every lab comp lints 0 errors / 0 warnings, each template placed into a fresh comp lints 0/0/0, and nothing overshoots. Clip-id prefixes: `mlt_`, `mme_`, `mpc_`, `mct_`, `mls_`, `mar_`, `mfr_`, `mdp_`.

## Round 3: briefs the pack could not serve before

Chosen from [reading a brief](../references/craft/reading-a-brief.md) ("fragrance, fashion, jewellery, hotel, premium product") and the wiki's [product launches](../../wiki/genres/product-launches.md), [title sequences](../../wiki/genres/title-sequences.md), [logo animation](../../wiki/genres/logo-animation.md) and [event openers](../../wiki/genres/event-openers.md) pages, against what rounds 1 and 2 already cover. Built 2026-10-28; Verified 0.1.8.1 (rev 1127), see the 0.1.8.1 block below. Every move is baked as keys in `minimal_luxury_lab3.py` (the pack's Slow fade in and Drift up written out; no presets to apply; three mask windows made with `mask.make`). Every easing lands with **0% overshoot** and every hold keeps moving (a drift, a tracking breathe, a sheen or a push). Names, places and numbers are sample copy; the two photos are gradient stand-ins. Frames are comp frames. Clip-id prefixes: `msw_`, `mpy_`, `mci_`, `mfn_`, `miv_`, `mba_`, `mle_`, `mes_`.

| Template | Brief it serves | Measured | Lint (lab) | Placed |
|---|---|---|---|---|
| Material swatches | materials, colourways, finishes | swatches opaque f47–75; sheen settles f142–162; names 144 px apart | 0 / 0 / 0 | 0 / 0 / 0 |
| Property feature | hotel suite, villa, residence listing | window settles f49; name opaque f71; rule f92; details f125; photo push 4% to f179 | 0 / 0 / 0 | 0 / 0 / 0 |
| Collection index | lookbook contents, chapters, "the looks" | rows land f58–106; the choice turns gold by f177 | 0 / 0 (8 notes) | 0 / 0 / 0 |
| Fragrance notes | notes pyramid, ingredients, care list | Notes 1 opaque f49, Notes 3 f105; Rule 3 f120; product f131 | 0 / 0 / 0 | 0 / 0 / 0 |
| Save the date | wedding, gala, invitation | frames f51 / f61; names f67; date f91; note f115 | 0 / 0 / 0 | 0 / 0 / 0 |
| Boutique address | store opening, "visit us", location | pin f36; name f65; address f93; hours f111 | 0 / 0 / 0 | 0 / 0 / 0 |
| Limited edition number | numbered piece, "one of 150" | number rise settles f53 (masked), opaque f36; OF 150 f101 | 0 / 0 / 0 | 0 / 0 / 0 |
| Editorial spread | magazine feature, lookbook page | feathered window settles f54; headline f71; standfirst f97 | 0 / 0 / 0 | 0 / 0 / 0 |

Notes are `repeated_key_value` (opacity held before the dim, intended). Each template was checked with the text-gap audit (`audit_text_gaps.py`): no flags; the closest pair is 29.8 px (Editorial spread, kicker / headline). Property feature, Limited edition number and Editorial spread move content inside a mask; full-frame looks of the placed instances (f30 and f179; f16, f24 and f100; f30 and f179) show nothing cut at rest ([KI-144](../references/known-issues.md#ki-144)). `qc` reads these comps as black and frozen like the rest of the pack; they were judged with looks.

### Round-3 pitfalls
1. **Measure every row of tracked words, even when lint is clean.** The swatch names first sat 400 px apart at tracking 1.3 and nearly touched (about 400 px each); the invitation's venue first measured 842 px inside a 920 px frame. Lint reported neither ([KI-138](../references/known-issues.md#ki-138)); `carvercat_authoring geometry` and the text-gap audit did.
2. **A feathered mask window must be larger than what it reveals by the feather on every side,** or the content stays soft-edged at rest. And it must still fit the frame: lint warns `cropped_at_rest` on a window that runs off-frame, although a mask is never drawn ([KI-151](../references/known-issues.md#ki-151)).
3. **Push the content, hold the window.** A photo that scales inside a still window keeps its frame edges where the window puts them; scaling the window instead moves the edges.
4. **A shape's gradient endpoints are live,** so a sheen across a swatch is two keyed endpoints on its own fill, no extra object ([ml-light-sweep.md](ml-light-sweep.md) does the same through a text mask).
5. **`inspect curves` reports 150% "overshoot" on a dim** (opacity 1 → 0.4): it is measured against the last key ([data viz round 3, pitfall 4](data-viz.md#round-3-pitfalls)). Read the keys before calling it a spring.
6. **Slow fades eat reading time.** A 36 f fade counts only from full opacity: the editorial standfirst (55 characters) first started at f76 and lint warned `reading_time`; and the index cannot dim its rows before about f135.
7. **Do not track roman numerals or short codes that must read as one word:** "III" at tracking 1.3 read as three letters.

## Sample film

`categories/minimal-luxury/ml-showcase` is a 465 f (15.5 s) master: tracked title → feather wipe (2% push) → product frame → slow quote. Lint 0/0/0. QC notes the product-frame hold (f221–314) as a "freeze": its 96 px analysis does not register a 0.6% drift.

## Round-2 sample film

`categories/minimal-luxury/ml-showcase-2` is a 1050 f (35 s) master at 1920 × 1080 that plays the round-2 templates back to back with Slow dip on one cut, placed from the Library with `library.place` + `template.apply` (rebuild: `ai/scripts/motion/recipes/showcase2.py minimal-luxury`). Verified 0.1.8.1 (rev 1127): master lint 0 / 0 / 0. Qc (240 px) reads most of it as frozen: the drifts, breathes and thin gold lines are below its threshold; judge with a look.

## Verified 0.1.8.1 (rev 1127): design-unit generators

All 20 templates were regenerated as carvercat/2 by the pack's lab modules (design units: px from the top-left, y down, degrees clockwise, exact hex colours, CSS easing); the lab, showcase, showcase-2 and recipe sample projects by the same modules. The `.carverpreset` files are unchanged and load in the app.
- Harness (`verify_pack.py`, 7 frames per template; 320 x 180, 960 x 540 for templates with text; shape limit 2 %). `covered` / `cut` / `settled` / `gone` use the harness definition (covered = the frame reads the same over a magenta and a green underlay; settled = first frame from which the picture no longer changes; gone = last visible frame + 1); None means the template never covers the frame or never goes blank.

| Template | lint 16:9 e/w/n | lint 9:16 e/w/n | v1 vs v2 | worst shape | colour shift | object check | box offset max px | worst ink IoU | covered | cut | settled | gone |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Attribute row | 0/0/0 | 0/0/0 | pass | 0.01 % | 2.4 | pass | 0.0 | 0.96 | None | None | None | None |
| Boutique address | 0/0/0 | 0/0/0 | pass | 0.01 % | 3.3 | pass | 0.1 | 0.88 | None | None | None | None |
| Collection index | 0/0/0 | 0/0/0 | pass | 0.00 % | 2.7 | pass | 0.0 | 0.69 | None | None | None | None |
| Collection title | 0/0/0 | 0/0/0 | pass | 1.72 % | 22.5 | pass | 0.1 | 0.48 | None | None | None | None |
| Editorial spread | 0/0/0 | 0/0/0 | pass | 0.01 % | 13.9 | pass | 0.1 | 0.95 | None | None | None | None |
| Feather wipe reveal | 0/0/0 | 0/0/0 | pass | 0.00 % | 2.8 | pass | 0.0 | 1.0 | None | None | None | None |
| Fragrance notes | 0/0/0 | 0/0/0 | pass | 0.01 % | 3.2 | pass | 0.1 | 0.97 | None | None | None | None |
| Framed word | 0/0/0 | 0/0/0 | pass | 0.05 % | 7.1 | pass | 0.5 | 0.96 | None | None | None | None |
| Light sweep | 0/0/0 | 0/0/0 | pass | 0.00 % | 8.8 | pass | 0.0 | 1.0 | None | None | None | None |
| Limited edition number | 0/0/0 | 0/0/0 | pass | 0.00 % | 3.5 | pass | 0.1 | 0.93 | None | None | None | None |
| Luxury lower third | 0/0/0 | 0/0/0 | pass | 0.11 % | 12.5 | pass | 0.1 | 0.32 | None | None | None | 168 |
| Material swatches | 0/0/0 | 0/0/0 | pass | 0.00 % | 14.7 | pass | 0.1 | 0.88 | None | None | None | None |
| Monogram end card | 0/0/0 | 0/0/0 | pass | 0.00 % | 3.6 | pass | 0.1 | 0.83 | None | None | None | None |
| Price card | 0/0/0 | 0/0/0 | pass | 0.09 % | 6.4 | pass | 0.1 | 0.87 | None | None | None | None |
| Product frame | 0/0/0 | 0/0/0 | pass | 0.00 % | 4.1 | pass | 0.1 | 0.99 | None | None | None | None |
| Property feature | 0/0/0 | 0/0/0 | pass | 0.01 % | 14.9 | pass | 0.0 | 0.91 | None | None | None | None |
| Save the date | 0/0/0 | 0/0/0 | pass | 0.01 % | 3.5 | pass | 0.1 | 0.88 | None | None | None | None |
| Slow dip | 0/0/0 | 0/0/0 | pass | 0.00 % | 8.0 | pass | 0.0 |  | [24, 36] | 24 | 59 | 55 |
| Slow quote | 0/0/0 | 0/0/0 | pass | 1.10 % | 28.1 | pass | 0.1 | 0.52 | None | None | None | None |
| Tracked title | 0/0/0 | 0/0/0 | pass | 0.00 % | 3.6 | pass | 0.1 | 0.98 | None | None | None | None |

- Colours are the exact hex of the style notes (the old kit linearised them): the colour shift to v1 is reported, not judged, and is intended.
- What changed: "Ease out" is the old curve; text boxes are centred on y; Light sweep keeps its 1000 x 320 fill still and keys the shape gradient endpoints (f30-110) behind the text mask (an earlier port slid the rectangle, which the object check flagged: Wordmark empty, fill moved 690 px); Material swatches keys the sheen endpoints again (an earlier port left the band static, which the pixel and object checks did not catch, a montage did). Slow dip: covered f24-36, settled f59, gone f55; Luxury lower third: gone f168 (harness definition).

## Pitfalls

1. **Tracking is keyframeable and centred text stays centred** while it changes, so a closing-in title needs no position keys. Keep a breathe under 10%.
2. **A feathered wipe is a mask with a soft edge.** The mask rectangle's `softEdge` (160 px here) becomes the feather. Start the mask a full width plus the feather to the left of its rest position, so frame 0 is clean.
3. **Two presets on one clip** work when they animate different properties (Product: Slow fade in on size and opacity, Drift up on the position).
4. **A gleam inside letters needs the text as the mask** of a gradient-filled shape with keyed `gradientStart`/`gradientEnd`. A text's own gradient endpoints are not live (KI-009 c), and a duplicate text as the mask trips lint `text_overlap` (KI-133). See [ml-light-sweep.md](ml-light-sweep.md).
5. **Wide tracking costs width.** At tracking 1.5–1.6, 56–88 px caps run 800–1850 px wide; check against the graphics-safe area before placing text off-centre.

Inspiration: common luxury-brand motion conventions (slow fades, tracked caps, thin metallic rules). No external text or code was used.
