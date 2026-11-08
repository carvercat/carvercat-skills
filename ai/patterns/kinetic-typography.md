# Kinetic Typography pack (`kt_`)

Type as the main actor: slams, letter zooms and pops, bouncing words, sliding lines, a rotating word slot, an impact stack, a rule-line reveal, beat-cut words, a focus-pull title, a lower third, a split title, a highlight sweep, a quote, a stat punch, a numbered list and a follow end card. Round 3 adds a karaoke lyric line, a manifesto scroll, an echo stack, opening credits, a strike-and-replace, a zoom through a letter and a justified poster lockup.

The pack lives in `library/templates/kinetic-typography/`. Install it as in [Installing a pack](README.md#installing-a-pack). It adds to Motion Patterns (Words rise, Letters cascade, Words pop, Lines reveal, Letters shimmer, Words swing, Words exit up) and does not repeat them.

- The presets are built by `ai/scripts/motion/build_kinetic_type_pack.py`.
- The templates are extracted with `comp_to_template.py` from `categories/kinetic-typography/kt-lab/project.carverproj` (written by `ai/scripts/motion/kinetic_type_lab.py`) and, for round 2, `categories/kinetic-typography/kt-lab-2/project.carverproj` (written by `ai/scripts/motion/kinetic_type_lab2.py`), and for round 3, `categories/kinetic-typography/kt-lab-3/project.carverproj` (written by `ai/scripts/motion/kinetic_type_lab3.py`).
- The sample film is `categories/kinetic-typography/kt-showcase`, written by `ai/scripts/motion/kinetic_type_showcase.py`.

**Status: verified 0.1.8.1 (rev 1127; headless, isolated folders, `ai/scripts/motion/verify_pack.py`).** Every template was placed in a fresh 16:9 and a fresh 9:16 comp (lint 0/0/0, qc no flash), compared with its v1 original at 7 frames (silhouette at most 2 %, object-level check: every object present with its text, ink and box), and the lab projects were rebuilt as carvercat/2 by `kinetic_type_lab*.py`. The lab comps themselves lint 0 errors on 0.1.8.1; the warnings that remain (`text_overlap` between neighbouring text boxes at single frames while parts move) are listed on each template page.
- The build was the public release binary, run headless (`--mcp`) with isolated preferences, data and cache folders, on 2026-10-27. The program binary is byte-identical to the published release.
- A packaged build loads Library packs only from its own bundle ([FR-036](../references/known-issues.md#fr-036)). So for the preset and placement tests this pack, and saas-ui, were copied into the `Contents/Resources/library/templates` folder of a scratch copy of the app.
- Each item was checked with `carvercat_inspect mode:curves` (overshoot, settle), `carvercat_look`, and `carvercat_inspect mode:lint` (0.1.6: 0 errors, 0 warnings on every comp and on the showcase master; on 0.1.8.1 the lab comps lint 0 errors, and some report `text_overlap` warnings, see the template pages; the showcase master lints 0/0/0). Each template was also placed into a fresh comp with `library.place` + `template.apply`, and lint was 0/0/0 for all five.
- The same numbers were measured earlier on the verification build. They are identical.

**Fonts:** the templates use Rethink Sans, which must be installed on the machine. It is a free Google Font (SIL OFL), and the file is in `ai/scripts/motion/json_author/RethinkSans.ttf`. Without it, text falls back to Arial ([KI-136](../references/known-issues.md#ki-136)). Check with `carvercat_authoring mode:validate` `font_exact`.

Style: kinetic. ExtraBold Rethink Sans, off-white `#F4F1EA` on near-black `#0B0B0F`, accent `#FF4D2E`, second accent `#FFD23F`. Fast in (8–14 f), long readable holds, and one idea per beat.

## Presets (6, all text, all staggered)

Measured per part (word, letter or line) on a clip that starts at frame 10. "Settle" is the frame from the start of the part after which the value stays within 0.5%. The whole text takes another gap × (parts − 1) frames ([KI-050](../references/known-issues.md#ki-050)).

| Name in Library | File | Anchor / frames, stagger | What moves | Measured | Use for |
|---|---|---|---|---|---|
| Words slam | kt_word_slam | in / 14, word gap 5 | scale 1.8 → 1 (spring), fade 0–18% | **4.6% overshoot, settles f13** | punchy 2–5 word lines; an impact sound on each landing |
| Letters zoom in | kt_char_zoom_in | in / 16, character gap 1 | scale 2.4 → 1 (expo), fade 0–40% | settles **f11** | single words and short titles |
| Letters pop | kt_char_pop | in / 18, character gap 1 | scale 0 → 1 (bouncy spring), fade 0–20% | **16.2% overshoot, settles f16** | energetic social and funky words |
| Words drop - bounce | kt_word_drop_bounce | in / 22, word gap 4 | y −5% H → 0, bounce | settles **f22** | playful brands only |
| Lines slide in - left | kt_line_slide_left | in / 20, line gap 5 | x −6% W → 0 (expo), fade 0–40% | settles **f16** | lists, left-aligned statements |
| Words exit down | kt_word_exit_down | out / 12, word gap 2 | y 0 → +3% H, accelerating, fade from 30% | the last 12 f per word | text without a staggered position entrance |

## Templates (19) and the tracking recipe

| Pattern | Kind | File / doc | Length |
|---|---|---|---|
| Word swap | template | kt_word_swap / [kt-word-swap.md](kt-word-swap.md) | 120 f, a new word every 36 f |
| Impact stack | template | kt_impact_stack / [kt-impact-stack.md](kt-impact-stack.md) | 90 f |
| Line reveal | template | kt_line_reveal / [kt-line-reveal.md](kt-line-reveal.md) | 60 f |
| Beat words | template | kt_beat_words / [kt-beat-words.md](kt-beat-words.md) | 100 f, 25 f a word |
| Focus pull (with the tracking breathe recipe) | template + recipe | kt_focus_pull / [kt-focus-pull.md](kt-focus-pull.md) | 60 f |
| Kinetic lower third | template | kt_lower_third / [kt-lower-third.md](kt-lower-third.md) | 150 f, exits in the last 12 f |
| Split title | template | kt_split_title / [kt-split-title.md](kt-split-title.md) | 90 f, lines settle f10 / f14 |
| Highlight sweep | template | kt_highlight_sweep / [kt-highlight-sweep.md](kt-highlight-sweep.md) | 90 f, marker f14–26 |
| Kinetic quote | template | kt_quote / [kt-quote.md](kt-quote.md) | 150 f, readable from about f48 |
| Stat punch | template | kt_stat_punch / [kt-stat-punch.md](kt-stat-punch.md) | 90 f, ring f4–34 |
| Numbered list | template | kt_numbered_list / [kt-numbered-list.md](kt-numbered-list.md) | 120 f, rows 12 f apart |
| Follow end card | template | kt_end_card / [kt-end-card.md](kt-end-card.md) | 120 f, all still by f34 |
| Karaoke line | template | kt_karaoke_line / [kt-karaoke-line.md](kt-karaoke-line.md) | 150 f, words fill f14–100 |
| Manifesto scroll | template | kt_manifesto_scroll / [kt-manifesto-scroll.md](kt-manifesto-scroll.md) | 240 f, a line every 40 f, final read f170 |
| Echo stack | template | kt_echo_stack / [kt-echo-stack.md](kt-echo-stack.md) | 120 f, echoes in by f28 |
| Opening credits | template | kt_opening_credits / [kt-opening-credits.md](kt-opening-credits.md) | 210 f, 3 cards of 50 f, title f150–170 |
| Strike and replace | template | kt_strike_replace / [kt-strike-replace.md](kt-strike-replace.md) | 120 f, strike f34–41, answer by f67 |
| Zoom through letter | template | kt_zoom_through / [kt-zoom-through.md](kt-zoom-through.md) | 120 f, zoom f40–58 |
| Poster lockup | template | kt_poster_lockup / [kt-poster-lockup.md](kt-poster-lockup.md) | 120 f, all still by f27 |

Template clip ids carry the prefixes `kws_`, `kis_`, `klr_`, `kbw_`, `kfp_` (round 1) and `klt_`, `kst_`, `khs_`, `kqt_`, `ksp_`, `knl_`, `kec_` (round 2) and `kko_`, `kms_`, `kes_`, `kcr_`, `ksr_`, `kzt_`, `kjl_` (round 3); no two templates in the skills library share one.

Round 2 (7 templates) was built and verified the same way on 2026-10-27: every lab comp lints 0 errors / 0 warnings, and each template placed into a fresh comp lints 0/0/0. Round 2 also uses Motion Patterns presets that ship in the bundled essentials (Words rise - expo, Pop - spring, Stamp, Exit down - accelerate, Exit fade - fast, Letters shimmer in); the motion is baked into the templates as keys.

## Round 3: briefs the pack could not serve before

Chosen from [reading a brief](../references/craft/reading-a-brief.md) ("manifesto, quote, lyrics, type-only") and the wiki's [lyric videos](../../wiki/genres/lyric-videos.md), [title sequences](../../wiki/genres/title-sequences.md) and [kinetic type](../../wiki/techniques/kinetic-type.md) pages (repetition, masking-style reveals, variation in size). Built on 0.1.6 (rev 1105) on 2026-10-28; re-verified on 0.1.8.1 (rev 1127) on 2026-11-07. Every move is baked as keys in `kinetic_type_lab3.py` (no presets to apply). The pack's expo landings give **0% overshoot** on every part. Frames below are comp frames.

| Template | Brief it serves | Measured | Lint (lab) | Placed |
|---|---|---|---|---|
| Karaoke line | lyric video, sing-along | words in by f22; each fills in 3 f on its sung frame, pop still 12 f later (last f112) | 0 / 0 / 0 | 0 / 0 / 0 |
| Manifesto scroll | manifesto, mission, values | a line every 40 f, settles 10 f after its start; pushes still by f140; all lines back to full by f179 | 0 / 0 (15 notes) | 0 / 0 / 0 |
| Echo stack | hype opener, music drop, repetition | hero f7; echoes in by f24 / f28, then drift 6–12 px | 0 / 0 / 0 | 0 / 0 / 0 |
| Opening credits | title sequence, film credits, speaker order | name tracking f21; 32 opaque frames per card; title lands f170, rule f170 | 0 / 0 (6 notes) | 0 / 0 / 0 |
| Strike and replace | myth vs fact, "not X, Y", rebrand | strike f41; claim dimmed f52; answer f59 / f67 | 0 / 0 / 0 | 0 / 0 / 0 |
| Zoom through letter | type-led transition, "dive in" | 1 → 34× f40–58, background only from f56; second word f70 | 0 / 0 (2 notes) | 0 / 0 / 0 |
| Poster lockup | event announcement, festival poster | four lines justified to 1000 px of ink; still f12–27 | 0 / 0 / 0 | 0 / 0 / 0 |

Each template was also checked with the text-gap audit (`audit_text_gaps.py`: no tight pairs, closest 17.0 px between two karaoke words) and with full-frame looks of the placed instances. Zoom through letter, Manifesto scroll, Echo stack and Opening credits move inside their instance; the looks show nothing cut except the intended letter edges during the zoom ([KI-144](../references/known-issues.md#ki-144)).

## Sample film

`categories/kinetic-typography/kt-showcase` is a 430 f (14.3 s) master at 1920×1080 and 30 fps, cutting focus pull → word swap → impact stack (with a 4% push over its hold) → line reveal → beat words. Lint: 0 errors, 0 warnings, 0 notes. QC: no freezes or flashes.

## Round-2 sample film

`categories/kinetic-typography/kt-showcase-2` is a 810 f (27 s) master at 1920 × 1080 that plays every round-2 template back to back, placed from the Library with `library.place` + `template.apply` (rebuild: `ai/scripts/motion/regen_showcase2.py kinetic-typography`, which runs `recipes/showcase2.py`). Verified 0.1.8.1 (rev 1127), 2026-11-07: master lint 0 / 0 / 0, written as carvercat/2. `qc` (240 px) notes the long holds as freezes (fine for a hold).

## Pitfalls found while building this pack (0.1.6, still true on 0.1.8.1)

1. **scaleY (and scaleX) cannot be staggered.** `preset.apply` refuses a staggered preset with "scaleY could not be staggered". Per-letter flips are therefore not possible. Use size, position, rotation or opacity ([KI-134](../references/known-issues.md#ki-134)).
2. **Set the window as the mask of the text:** `property.set {id: <text>, key: "mask", value: {"ref": "<window id>"}}`, then `parent.clear {ids:[window, text]}` so that the window stays still while the text moves (the mask must be on another track). The old `mask.make` took the FIRST id as the mask; the other order turned the text into the matte, and the result was drawn in the window's colour.
3. **Lint counts two words in one slot as overlapping text.** In the word swap the outgoing word's exit (8 f) ends on the frame the next word starts, so no frame holds both.
4. **A fade-in costs reading time.** Lint counts only fully opaque frames, so a 25 f word with a 2 f fade reads as 23 f. The beat words cut in at full opacity and use scale for the hit.
5. **Size the mask window to the measured ink** (`measure.boxes`, including descenders, plus 6 px). A window 1.24× the font size let a rolling word show 20 px above the line.
6. **Staggered presets cannot share a property on one text** ([stagger.md](../references/effects/stagger.md)). Almost every preset fades (`blend`), so in practice it is one staggered preset per text. A second one is refused: "blend could not be staggered - that is already in a slot of the Stagger" (Words exit down on a name that already had Letters zoom in). Use a non-staggered exit (Exit down - accelerate, Exit fade - fast) on staggered text.
7. **A pop from 0 on a glyph fails lint** (`text_too_small`, "a line is 7.0 px tall"). Use Stamp or Words slam, which start large.

8. **Lint checks `text_overlap` while texts move, not only at rest.** Echoes sliding out from behind the hero word raised four warnings at f13 and f16. A slam from 1.3 on the word beside another raised one (17%). Start moving texts clear of their neighbours (Echo stack, [kt-echo-stack.md](kt-echo-stack.md)), or use a rise instead of a slam next to another word.
9. **Colour is keyframeable on `text.fill`.** Use it for a karaoke fill or a claim that dims in place. One text has one colour, so per-word colour still means one text per word.
10. **Outline-only text:** set `text.fill` Paint to none and `text.outline` Paint to solid, with Thickness about 0.035 at 150 px (Echo stack; outline measurements in [text outlines](../../wiki/techniques/text-outlines.md)).
11. **Justify and align on measured bounds.** `measure.boxes` bounds (earlier `carvercat_authoring geometry`) are 3–5% narrower than the `cc.textw` advance, by a different amount per word. Measure throwaway texts first: the two-pass `KT3 Measure` comp in `kinetic_type_lab3.py`.
12. **A zoom into a point needs scale and position on one easing.** Then the target moves in a straight line onto the frame centre: end position = C − z·(T − C) ([kt-zoom-through.md](kt-zoom-through.md)).
13. **`inspect curves` reports `settles_at` in comp frames.** A word clip that starts at f8 with colour keys at f100–103 reported 103, not 95. The round-1 and round-2 tables were measured on clips starting at 0 or 10 and say so.

Inspiration: common kinetic-typography conventions (rotating-word headlines, beat-synced word cuts, rule reveals). No external text or code was used.
