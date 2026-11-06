# Cartoon Bounce pack (`ct_`)

The classic principles, applied: squash and stretch, anticipation, follow-through on springs, and smear frames. Round 3 adds a rigged walk cycle, a map pin drop, a thought bubble, a squash-and-stretch logo reveal, a swinging price tag, a boing arrow, a comic POW and a kids' lesson title card. For kids' content, explainers with personality, playful brands and stickers.

The pack lives in `library/templates/cartoon-bounce/`. Install it as in [Installing a pack](README.md#installing-a-pack).

- The presets are built by `ai/scripts/motion/build_cartoon_bounce_pack.py`. Its `track()` helper chains several curves on one property (fall → squash → recover), which squash and stretch needs.
- The templates come from `categories/cartoon-bounce/ct-lab` (written by `ai/scripts/motion/cartoon_bounce_lab.py`) and, for round 2, `categories/cartoon-bounce/ct-lab-2` (written by `ai/scripts/motion/cartoon_bounce_lab2.py`), and for round 3, `categories/cartoon-bounce/ct-lab-3` (written by `ai/scripts/motion/cartoon_bounce_lab3.py`).
- The sample reel is `categories/cartoon-bounce/ct-showcase`.
- The principles themselves are in [../references/craft/motion-principles.md](../references/craft/motion-principles.md).

**Status: verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test).**
- Public release binary, headless, isolated folders; the pack was added to a scratch copy's bundled Library ([FR-036](../references/known-issues.md#fr-036)).
- Lint was 0 errors and 0 warnings on every lab comp and the preset bench, and 0/0/0 on the showcase.
- Each template was placed into a fresh comp: lint 0/0/0 for all four.

**Fonts:** Rethink Sans must be installed ([KI-136](../references/known-issues.md#ki-136)).

Style:
- Cream ground `#FFF4E0`, dark ink outlines `#2B1B3D`, saturated red / yellow / blue / green.
- Big springs (16–31% overshoot) are allowed here and nowhere calmer.
- Set squashes about the contact edge (anchor at the bottom for a landing, at the leading edge for a stop).

## Presets (4)

Measured on a 40 f clip that starts at frame 10, anchor at the bottom edge for the first two.

| Name in Library | File | Anchor / frames | What moves | Measured | Use for |
|---|---|---|---|---|---|
| Squash land | ct_squash_land | in / 20 | falls 8% H accelerating while stretched (85% × 120%), squashes to 130% × 72% on contact, springs back | lands **f8**, squash peak f11, scale settles **f20** | anything landing; `transformOrigin "50% 100%"` (stored anchor [0, −1]) |
| Anticipate jump out | ct_anticipate_jump | out / 20 | crouch to 118% × 78% (first 35%), then stretch to 82% × 130% and shoot up 60% H, accelerating | crouch 7 f, launch 13 f | exits with energy; `transformOrigin "50% 100%"` (stored anchor [0, −1]) |
| Jelly in | ct_jelly_in | in / 28 | width on a wobbly spring, height on a bouncy one | width **30.7%**, height **16.2%** overshoot; settles **f21** | blobs, characters, buttons |
| Pop - wobbly | ct_pop_wobbly | in / 22 | scale 0 → 1 on a wobbly spring | **30.8% overshoot, settles f17** | stars, stickers, props |

## Templates (4)

| Pattern | File / doc | Length |
|---|---|---|
| Bouncing ball | ct_bouncing_ball / [ct-bouncing-ball.md](ct-bouncing-ball.md) | 90 f |
| Boing title | ct_boing_title / [ct-boing-title.md](ct-boing-title.md) | 90 f |
| Blinking face | ct_blink_face / [ct-blink-face.md](ct-blink-face.md) | 100 f |
| Smear whoosh | ct_smear_whoosh / [ct-smear-whoosh.md](ct-smear-whoosh.md) | 45 f |

## Templates added in round 2 (8)

| Pattern | File / doc | Length |
|---|---|---|
| Speech bubble | ct_speech_bubble / [ct-speech-bubble.md](ct-speech-bubble.md) | 90 f |
| Button press | ct_button_press / [ct-button-press.md](ct-button-press.md) | 60 f, contact f21 |
| Character hop (rigged) | ct_character_hop / [ct-character-hop.md](ct-character-hop.md) | 90 f, lands f40 |
| Sticker burst | ct_sticker_burst / [ct-sticker-burst.md](ct-sticker-burst.md) | 75 f |
| Cartoon end card | ct_end_card / [ct-end-card.md](ct-end-card.md) | 120 f |
| Ribbon lower third | ct_ribbon_lower_third / [ct-ribbon-lower-third.md](ct-ribbon-lower-third.md) | 150 f, exit in the last 20 f |
| Hanging sign (rigged) | ct_hanging_sign / [ct-hanging-sign.md](ct-hanging-sign.md) | 90 f, still from f42 |
| Bouncy list | ct_bouncy_list / [ct-bouncy-list.md](ct-bouncy-list.md) | 120 f |

Round 2 was built and verified the same way on 2026-10-27: every lab comp lints 0 errors / 0 warnings, and each template placed into a fresh comp lints 0/0/0 (the parented rigs survive placement). Clip-id prefixes: `csb_`, `cbp_`, `cch_`, `csk_`, `cec_`, `crl_`, `chs_`, `cbl_`.

## Round 3: briefs the pack could not serve before

Chosen from [reading a brief](../references/craft/reading-a-brief.md) ("kids, playful lesson, mascot") and the wiki's [explainers](../../wiki/genres/explainers.md), [logo animation](../../wiki/genres/logo-animation.md), [social ads](../../wiki/genres/social-ads.md) and [infographics](../../wiki/genres/infographics.md) pages, against what rounds 1 and 2 already cover (the essentials pack's static stickers named Thought, Pin, Tag and Arrow do not animate these beats). Built and verified on 0.1.6 (rev 1105) on 2026-10-28. Every move is baked as keys in `cartoon_bounce_lab3.py` (no presets to apply, no masks); springs are hand-set visible extremes. Every squash keeps its volume: the lab refuses any non-uniform scale key outside x·y 0.9–1.05, and the extremes are in the table. Real arcs use the methods in [arcs](../references/craft/principles/arcs.md): parabolas baked every 2 f (logo ball, walk hips) and rotation about a visible pivot (price tag, walk limbs). Five templates are rigged on a visible, centred pivot. Names, prices and places are sample copy; the map is a shape stand-in. Frames are comp frames. Clip-id prefixes: `cwk_`, `cmp_`, `ctb_`, `clr_`, `cpt_`, `cba_`, `cpw_`, `clt_`.

| Template | Brief it serves | Measured | x·y (squash) | Lint (lab) | Placed |
|---|---|---|---|---|---|
| Walk cycle (rigged) ([ct-walk-cycle.md](ct-walk-cycle.md)) | the mascot walks in, a character arrives | 8 steps f10–106, stride 122 px, planted feet; hips settle f106, stop squash f119; blink f126 | 0.95 (leg tuck) – 0.999 | 0 / 0 (30 notes) | 0 / 0 / 0 |
| Bouncy map pin ([ct-map-pin.md](ct-map-pin.md)) | find us, new store, location | lands f16, 122 × 80% on its point, settles f29; card f41; text f49 | 0.976–1.003 | 0 / 0 (3 notes) | 0 / 0 / 0 |
| Thought bubble ([ct-thought-bubble.md](ct-thought-bubble.md)) | the character wonders, imagine | face f17; dots f12–32; cloud jelly f41; thought f51; 12 px float to f120 | 0.996–1.012 | 0 / 0 (2 notes) | 0 / 0 / 0 |
| Squash logo reveal ([ct-logo-reveal.md](ct-logo-reveal.md)) | toy brand, kids' channel ident | contacts f14, 30, 42 on baked parabolas; 130 × 74% squash; ball settles f54; word in by f66; tagline f75 | 0.962–1.008 | 0 / 0 (2 notes) | 0 / 0 / 0 |
| Swinging price tag ([ct-price-tag.md](ct-price-tag.md)) | price drop, sale | swings 160 → −38, 21, −10, 4, 0° (f58); strike f71; new price stamps f76, settles f91; kick settles f86 | 0.986–1.0 | 0 / 0 (6 notes) | 0 / 0 / 0 |
| Boing arrow ([ct-boing-arrow.md](ct-boing-arrow.md)) | tap here, look at this, tutorial | label f15; arrow draws f6–22; boing 110 × 92% settles f41; button poked 86 × 114%, settles f39 | 0.98–1.012 | 0 / 0 (5 notes) | 0 / 0 / 0 |
| Comic POW ([ct-comic-pow.md](ct-comic-pow.md)) | a big hit, BAM moment | bursts settle f15 / f17 (118% / 116% peak); POW! slams from 240%, squash 116 × 86% at f8, settles f18 | 0.996–1.0 | 0 / 0 / 0 | 0 / 0 / 0 |
| Lesson title card ([ct-lesson-title.md](ct-lesson-title.md)) | kids' lesson, episode title | card lands f14, 112 × 86%, settles f27; badge f38; last title letter f74; star f55; subtitle f75 | 0.963–1.008 | 0 / 0 (2 notes) | 0 / 0 / 0 |

Notes are `speed_jump` on impacts and on the walk's start (intended: contacts are hard stops) and `repeated_key_value` on held keys. Pop and squash peaks are given as keyed values: `inspect curves` reports, for example, 300% "overshoot" on the ball's scale because it measures against the last key ([KI-152](../references/known-issues.md#ki-152)). Each template was checked with the text-gap audit (`audit_text_gaps.py`): no flags; the closest pair is 19 px (map pin, place / note). Full-frame looks of every placed template at its widest moving frame and its last frame show nothing cut ([KI-144](../references/known-issues.md#ki-144)); the price tag, map pin and logo ball enter from outside the frame by design.

### Round-3 pitfalls
1. **A walk needs Linear leg rotation and baked hips.** The stance foot stays planted only if the leg turns at constant speed and the hips move one stride (`2 L sin θ`) per step; the hip height `ground − L cos θ` gives the bob for free. Easing the legs makes the feet skate; two hip keys per step make a "^" path ([ct-walk-cycle.md](ct-walk-cycle.md)).
2. **Rigs need a visible, centred pivot at the joint** (feet, the point of a pin, a nail, an arrow's tail, a cloud's core). Children with off-centre anchors are fine as leaves (legs, arms turn about hip and shoulder); a parent with an off-centre anchor makes its children drift ([KI-108](../references/known-issues.md#ki-108)).
3. **Lint compares axis-aligned text boxes.** Two words on a rotating tag were reported overlapping (`text_overlap` 15–18%) while the tag was steep, although they never touched ([KI-156](../references/known-issues.md#ki-156)). Bring the words on after the big swing.
4. **Text that pops from 0 trips `text_too_small`** on its first visible frame (10.6 px for a 30 px note). Pop text from 60%, or fade it in a few frames after its plate.
5. **A slam from big covers its neighbours.** The price stamp from 190% overlapped the old price's box (47%); 135% clears it. Size the slam to the free space, not to the drama.
6. **Hand-set the spring extremes.** Every pop here is 3 visible extremes (for example 112 → 95 → 102 → 100%) with S curves (`cubic-bezier(0.333, 0, 0.667, 1)`) between; a baked spring's sub-pixel tail reads as `jitter` ([pitfall 6](#pitfalls-016)).
7. **Squash by the axis that matches the motion.** Scale is axis-aligned, so the boing arrow stretches x and squashes y because the arrow runs mostly horizontally; a steep arrow needs the opposite.

## Sample reel

`categories/cartoon-bounce/ct-showcase` is a 325 f (10.8 s) master: bouncing ball → smear whoosh → blinking face → boing title. Lint 0/0/0, QC clean.

## Round-2 sample film

`categories/cartoon-bounce/ct-showcase-2` is a 795 f (26 s) master at 1920 × 1080 that plays the round-2 templates back to back, placed from the Library with `library.place` + `template.apply` (rebuild: `ai/scripts/motion/recipes/showcase2.py cartoon-bounce`). Verified 0.1.6 (rev 1105), 2026-10-28: master lint 0 / 0 / 0. Qc (240 px) notes three holds as freezes.

## Pitfalls (0.1.6)

1. **Per-letter squash is impossible** (scaleX/scaleY cannot be staggered, [KI-134](../references/known-issues.md#ki-134)). The Boing title bounces each letter's position instead.
2. **Position is one point.** The ball's horizontal travel takes the same ease as its vertical bounce on each key, so it slows slightly at each peak. For constant horizontal speed, nest the ball in a comp that moves sideways linearly.
3. **Blinks and squashes use the point Scale (`tr ... scale` [x, y]).** A preset's `size` multiplies on top of it, which is why an eye can both pop (preset) and blink (keys).
4. **No looping bobs** (lint: jitter, see the social pack). The face blinks instead of bobbing.
5. **Rigs in the stored JSON: a child's position is an offset from the comp centre** (measured 0.1.6; stored value). In design units a child's `x`, `y` are from its parent's top-left. For the stored form write `0.5 + (child − pivot)`, use a visible part as the pivot (an invisible null fails lint `never_visible`), and see [../references/app/json-authoring.md](../references/app/json-authoring.md).
6. **A spring's tail can fail lint.** Baked springs end in sub-pixel wobbles that lint reads as `jitter` when they drive a swing or a recovery for many frames. Hand-set 3–5 visible extremes instead.

Inspiration: the classic principles of animation (squash and stretch, anticipation, smear frames). No external text or code was used.
