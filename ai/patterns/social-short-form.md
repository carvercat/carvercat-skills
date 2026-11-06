# Social Short-form pack (`ss_`, vertical 9:16)

Vertical 1080 × 1920 motion for Reels, Shorts and TikTok: a first-second hook, fast word captions, whip-ins, caption pages, a story progress bar, a follow end card, a name tag, a listicle, a before/after split, a poll sticker, a countdown, a post card, a highlight caption and a swipe-up transition. Round 3 adds a story tap-through, a link-in-bio card, a POV hook, a comment reply, this or that, a price drop, giveaway rules and a reaction picture-in-picture. Everything stays inside the social safe area.

The pack lives in `library/templates/social-short-form/`. Install it as in [Installing a pack](README.md#installing-a-pack).

- The presets are built by `ai/scripts/motion/build_social_short_form_pack.py`.
- The templates come from `categories/social-media-reels/ss-lab` (written by `ai/scripts/motion/social_short_form_lab.py`) and, for round 2, `categories/social-media-reels/ss-lab-2` (written by `ai/scripts/motion/social_short_form_lab2.py`), and for round 3, `categories/social-media-reels/ss-lab-3` (written by `ai/scripts/motion/social_short_form_lab3.py`).
- The sample short is `categories/social-media-reels/ss-showcase`, written by `ai/scripts/motion/social_short_form_showcase.py`.
- For 16:9 → 9:16 conversion and the safe-area numbers, see [../references/craft/vertical-and-safe-areas.md](../references/craft/vertical-and-safe-areas.md).

**Status: verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test).**
- Public release binary, headless, isolated folders; the pack was added to a scratch copy's bundled Library ([FR-036](../references/known-issues.md#fr-036)).
- Lint was 0 errors and 0 warnings on every lab comp, and 0/0/0 on the showcase master.
- `bounds_inside` (a `carvercat_authoring mode:validate` check in the build that measured it) passed for every visible object against the safe box [61, 268, 955, 1270].
- Each template was placed into a fresh **1080 × 1920** comp (`comp.format`): it applied at 1080 × 1920, and lint was 0/0/0 for all four.

**Fonts:** Rethink Sans must be installed ([KI-136](../references/known-issues.md#ki-136)).

Style:
- Fast: hooks in 10 f, words 3 f apart, scene changes every 1.5–2.5 s.
- Big ExtraBold type, white with a black outline over footage.
- One hot accent (`#FF3D7F`) and a yellow (`#FFE14D`) for the second voice.
- No looping bobs: lint reads a ping-pong as jitter (below).

## Presets (3)

| Name in Library | File | Anchor / frames | What moves | Measured | Use for |
|---|---|---|---|---|---|
| Hook punch | ss_hook_punch | in / 10 | scale 1.25 → 1 (expo), fade 0–20% | settles **f7**, opaque by f2 | the first-second hook: big words, a face, a product |
| Caption words pop | ss_caption_pop | in / 8, word gap 3 | scale 0.7 → 1 (gentle spring), fade 0–25% | **4.4% overshoot, settles f8** per word | captions that follow speech |
| Whip in - left | ss_whip_in_left | in / 10 | x −30% W → 0, hard expo | settles **f7**; peaks at 285 px/frame on its first frame | B-roll cards and stickers; add the Motion blur effect |

## Templates (20)

| Pattern | File / doc | Length |
|---|---|---|
| Hook title (9:16) | ss_hook_title / [ss-hook-title.md](ss-hook-title.md) | 75 f |
| Caption pages (9:16) | ss_caption_pages / [ss-caption-pages.md](ss-caption-pages.md) | 120 f (3 × 40 f) |
| Story progress bar (9:16) | ss_progress_bar / [ss-progress-bar.md](ss-progress-bar.md) | 150 f, stretch to your length |
| Follow end card (9:16) | ss_follow_cta / [ss-follow-cta.md](ss-follow-cta.md) | 90 f |
| Name tag (9:16) | ss_name_tag / [ss-name-tag.md](ss-name-tag.md) | 120 f, tag settles f7 |
| Listicle (9:16) | ss_listicle / [ss-listicle.md](ss-listicle.md) | 150 f, tips 30 f apart |
| Before after split (9:16) | ss_before_after / [ss-before-after.md](ss-before-after.md) | 120 f |
| Poll sticker (9:16) | ss_poll / [ss-poll.md](ss-poll.md) | 150 f, bars settle f42 / f48 |
| Countdown (9:16) | ss_countdown / [ss-countdown.md](ss-countdown.md) | 100 f, 25 f a beat |
| Post card (9:16) | ss_post_card / [ss-post-card.md](ss-post-card.md) | 150 f |
| Highlight caption (9:16) | ss_highlight_caption / [ss-highlight-caption.md](ss-highlight-caption.md) | 90 f, box f10–18 |
| Swipe up (9:16, transition) | ss_swipe_up / [ss-swipe-up.md](ss-swipe-up.md) | 24 f, cut at f12 |
| Story tap-through (9:16) | ss_story_tap / [ss-story-tap.md](ss-story-tap.md) | 160 f, 4 pages × 40 f, taps f36 / f76 / f116 |
| Link in bio (9:16) | ss_link_in_bio / [ss-link-in-bio.md](ss-link-in-bio.md) | 120 f, chip f27 |
| POV hook (9:16) | ss_pov_hook / [ss-pov-hook.md](ss-pov-hook.md) | 90 f, lines f13 / f17 |
| Comment reply (9:16) | ss_comment_reply / [ss-comment-reply.md](ss-comment-reply.md) | 120 f, card f10 |
| This or that (9:16) | ss_this_or_that / [ss-this-or-that.md](ss-this-or-that.md) | 150 f, pick f70–82 |
| Price drop (9:16) | ss_price_drop / [ss-price-drop.md](ss-price-drop.md) | 120 f, new price f40 |
| Giveaway rules (9:16) | ss_giveaway / [ss-giveaway.md](ss-giveaway.md) | 150 f, ticks f54–71 |
| Reaction picture-in-picture (9:16) | ss_reaction_pip / [ss-reaction-pip.md](ss-reaction-pip.md) | 120 f, cam f21 |

Round 2 (8 templates) was built and verified the same way on 2026-10-27: every lab comp lints 0 errors / 0 warnings, `bounds_inside` the safe box passed for every object, and each template placed into a fresh 1080 × 1920 comp applied at 1080 × 1920 and linted 0/0/0. Clip-id prefixes: `snt_`, `sli_`, `sba_`, `spl_`, `scd_`, `spc_`, `shc_`, `ssu_`.

## Round 3: briefs the pack could not serve before

Chosen from [reading a brief](../references/craft/reading-a-brief.md) ("Reels / Shorts / TikTok tips, engagement") and the wiki's [social ads](../../wiki/genres/social-ads.md) page: the native formats a creator or a shop asks for that rounds 1 and 2 did not have (the story bar was one continuous line, the swipe-up was only a transition, the poll shows results, not a pick). Built and verified on 0.1.6 (rev 1105) on 2026-10-28. Every move is baked as keys in `social_short_form_lab3.py`: `punch()`, `whip()` and `pop()` write the keys of Hook punch, Whip in - left and the round-2 badge pop, so there is nothing to apply after `edit.open`. Hook punch and the whips land with 0% overshoot; the badge pops (back curve) overshoot 9.3–9.8%, the pack's playful accent. Handles, prices, the URL and the panels are invented stand-ins. Frames below are comp frames. Clip-id prefixes: `sst_`, `slb_`, `spv_`, `scr_`, `sto_`, `spd_`, `sga_`, `srx_`.

| Template | Brief it serves | Measured | Lint (lab) | Placed |
|---|---|---|---|---|
| Story tap-through | multi-part story, "day 1 to day 4", tap for more | segments full f39 / f79 / f119 / f159; tap rings f36–49 (each page); hint f13 | 0 / 0 / 0 | 0 / 0 / 0 |
| Link in bio | "link in bio", swipe-up CTA, where to get it | LINK / IN BIO f11 / f15; chip f27; URL f29; pulse f40–57; note f39 | 0 / 0 / 0 | 0 / 0 / 0 |
| POV hook | "POV:" text hook, native on-screen text | POV plate f8 (9.3%); lines f13 / f17 | 0 / 0 / 0 | 0 / 0 / 0 |
| Comment reply | answer a viewer's comment | card f10 (9.7%); comment f17; caption f43 | 0 / 0 / 0 | 0 / 0 / 0 |
| This or that | A-or-B choice, "which one would you pick" | cards f15 / f19; VS f32 (9.7%); pick outline f77, tick f81, badge f82; other card dims by f78 | 0 / 0 / 0 | 0 / 0 / 0 |
| Price drop | price drop, flash deal, discount | old price f19; strike f27; new price f40 (9.7%); badge f52; deadline f57 | 0 / 0 / 0 | 0 / 0 / 0 |
| Giveaway rules | giveaway, contest, how to enter | rules f26 / f36 / f46; ticks f59–71; closing line f67; disclaimer f72 | 0 / 0 / 0 | 0 / 0 / 0 |
| Reaction picture-in-picture | reaction, duet, stitch, face cam | panel f7; tag f19; cam f21 (9.8%); credit f23; caption f37 | 0 / 0 / 0 | 0 / 0 / 0 |

Every object passed `bounds_inside` the safe box [61, 268, 955, 1270] at the end of its clip, and none reaches right of x 851 below y 1151 (measured with `geometry` bounds). Each template placed into a fresh comp formatted 1080 × 1920 applied "at 1080 x 1920" and linted 0/0/0. The text-gap audit (`audit_text_gaps.py`) found no tight pairs (closest 16.0 px, the comment reply's avatar and reply-to line). Full-frame looks of all eight placed instances (8 frames each, f0 to the last frame) show nothing cut, including the cards and chips that whip in from outside the frame ([KI-144](../references/known-issues.md#ki-144)).

### Round-3 pitfalls
1. **Holds make lint notes.** Opacity held at 1 and then keyed again (a fade-out, a dim) gives a `repeated_key_value` note; end the clip instead (the story hint cuts with its page) or start the object at its final look (the old price is muted from the start).
2. **`curves` overshoot is per lane, not per move** ([KI-152](../references/known-issues.md#ki-152)): the old price's fade-in-then-dim read as 66.7% overshoot. Quote overshoot only for one-move lanes.
3. **Big shapes popped from a corner make `speed_jump`.** A 780 px card scaled 0.5 → 1 from its corner on the back curve moved its far edge 11.6 → 1.9 px/frame in one frame (info note); from 0.8 it is clean.
4. **Text popped from 0 trips `text_too_small`.** "VS" at 60 px was reported at 17.5 px while scaling; pop text from 0.6 (shapes can still pop from 0).
5. **Layer order decides what a pick outline cuts.** Draw outlines and rings before the badges that sit on them, or the stroke runs through the badge's letters.
6. **Size plates from the text.** Plates behind native-style text (POV lines, the IN BIO plate, the REACTING TO tag) are `cc.textw` + padding; change the copy in the lab script and rebuild, or resize the plate by hand after placing.
7. **Lint knows no button column.** None of the checks above fails when an object sits under the like/comment column; measure the right edge below y 1151 yourself.

## Sample short

`categories/social-media-reels/ss-showcase` is a 285 f (9.5 s) vertical master: hook (0–75), caption pages (75–195), follow end card (195–285), with the progress bar nested over the whole length (its comp made 285 f long). Lint 0/0/0. QC: no freezes or flashes.

## Vertical authoring (measured on 0.1.6)

- **Direct JSON:** set `cc.W, cc.H = 1080, 1920` and `cc.EM = 1146.24 × 1080 / 1920`, and write scenes with `width`/`height` 1080/1920 (`VComp` in the lab script). Text size scales with comp width: 100 px Bold caps measure 71 px tall, as at 1920 wide. A 200 × 100 box and a 40 px dot landed exactly.
- **Placing a 9:16 template:** `comp.new`, then `comp.format {width:1080, height:1920}`, then `library.place` + `template.apply`, then `carve.preflight` before a send. It applies "at 1080 x 1920".
- **Safe area check:** `measure.overlaps {within: "safe"}` or `layout.safe {safe: "title"}` (measured here as `bounds_inside` with box [61,268,955,1270] per object). Captions are centred at x 490 so they end left of x 851 (the button column below y 1151).

## Round-2 sample film

`categories/social-media-reels/ss-showcase-2` is a 880 f (29 s) master at 1080 × 1920 that plays the round-2 templates back to back with Swipe up (9:16) on one cut, placed from the Library with `library.place` + `template.apply` (rebuild: `ai/scripts/motion/recipes/showcase2.py social-short-form`). Verified 0.1.6 (rev 1105), 2026-10-28: master lint 0 / 0 / 0. Qc (240 px) notes five holds as freezes.

## Pitfalls

1. **A looping bob fails lint.** An arrow bouncing up and down (decelerating/accelerating or S curve pairs) is reported as `jitter` ("5 sub-pixel reversals"). Use a single entrance and hold, or move to a new position each time.
2. **Outline over dark grounds is invisible in the lab** but is what makes captions readable over footage. Keep `text.outline` (paint solid, black, thickness 0.12, outside only, round corners).

Inspiration: common short-form social video conventions (hook in the first second, word captions, progress bars, follow end cards). No external text or code was used.
