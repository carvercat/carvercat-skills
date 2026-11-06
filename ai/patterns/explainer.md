# Explainer pack (`ex_`)

Clear motion for narrated explainers and tutorials: step-ins in reading order, a single emphasis pulse, a three-step process with drawn arrows, an icon grid, a pointer callout and a milestone timeline. Round 2 adds a speaker lower third, compare columns, flow diagram, key term, checklist, Venn, quiz and cycle; round 3 adds a branching cause and effect, pros and cons with a seesaw, a labelled diagram, icon steps, an FAQ accordion, a word definition with pronunciation, a tip carousel and a problem and solution split.

The pack lives in `library/templates/explainer/`. Install it as in [Installing a pack](README.md#installing-a-pack).

- The presets are built by `ai/scripts/motion/build_explainer_pack.py`.
- The templates come from `categories/explainer/ex-lab`, written by `ai/scripts/motion/explainer_lab.py`; round 2 from `ex-lab-2` (`explainer_lab2.py`) and round 3 from `ex-lab-3` (`explainer_lab3.py`).
- The sample film is `categories/explainer/ex-showcase`.
- Layout rules: [../references/craft/composition-and-layout.md](../references/craft/composition-and-layout.md).

**Status: verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test).**
- Public release binary, headless, isolated folders; the pack was added to a scratch copy's bundled Library ([FR-036](../references/known-issues.md#fr-036)).
- Lint was 0 errors and 0 warnings on every lab comp, and 0/0/0 on the showcase.
- Each template was placed into a fresh comp: lint 0/0/0 for all four.
- I checked every template name across all packs against the essentials pack. "Callout" collided, so this pack's version is **Pointer callout**.

**Fonts:** Rethink Sans must be installed ([KI-136](../references/known-issues.md#ki-136)).

Style:
- Light ground `#F7F7FA`, ink `#1F2333`, muted `#6B7184`; blue `#3B6EF6`, coral `#FF6B5B` and green `#2BB673` as step colours.
- Everything enters in reading order (left to right, top to bottom) at the speed of the narration.
- One emphasis at a time.
- Round 3 uses deeper accents so every text passes lint at 4.5:1: blue `#2B58D6`, coral `#B93222`, green `#17794A`, muted `#565C70` (see the round-3 pitfalls).

## Presets (2)

| Name in Library | File | Anchor / frames | What moves | Measured | Use for |
|---|---|---|---|---|---|
| Step in | ex_step_in | in / 14 | x −2.5% W → 0 (strong decelerate), fade over 50% | settles **11 f** after its start; opaque by 7 f | labels, list items, captions |
| Emphasis pulse | ex_emphasis_pulse | in / 16 | scale 1 → 1.15 (first 40%) → 1 (S curve `cubic-bezier(0.333, 0, 0.667, 1)`), **once** | settles **16 f** after its start | "look here": split the clip where the narration names it |

## Templates (4)

| Pattern | File / doc | Length |
|---|---|---|
| Process steps | ex_process_steps / [ex-process-steps.md](ex-process-steps.md) | 120 f |
| Icon grid | ex_icon_grid / [ex-icon-grid.md](ex-icon-grid.md) | 90 f |
| Pointer callout | ex_callout / [ex-callout.md](ex-callout.md) | 75 f |
| Milestone timeline | ex_timeline / [ex-timeline.md](ex-timeline.md) | 150 f |

## Templates added in round 2 (8)

| Pattern | File / doc | Length |
|---|---|---|
| Speaker lower third | ex_lower_third / [ex-lower-third.md](ex-lower-third.md) | 150 f, fades out at the end |
| Compare columns | ex_compare_columns / [ex-compare-columns.md](ex-compare-columns.md) | 150 f, light background included |
| Flow diagram | ex_flow_diagram / [ex-flow-diagram.md](ex-flow-diagram.md) | 150 f, light background included |
| Key term card | ex_key_term / [ex-key-term.md](ex-key-term.md) | 150 f, light background included |
| Checklist | ex_checklist / [ex-checklist.md](ex-checklist.md) | 150 f, light background included |
| Venn diagram | ex_venn / [ex-venn.md](ex-venn.md) | 120 f, light background included |
| Quiz question | ex_quiz / [ex-quiz.md](ex-quiz.md) | 180 f, answer at f100 |
| Cycle loop | ex_cycle / [ex-cycle.md](ex-cycle.md) | 150 f, light background included |

Round 2 was built and verified the same way on 2026-10-27: every lab comp lints 0 errors / 0 warnings, and each template placed into a fresh comp lints 0/0/0. Clip-id prefixes: `elt_`, `ecc_`, `efd_`, `ekt_`, `ecl_`, `evn_`, `eqz_`, `ecy_`. Lab: `categories/explainer/ex-lab-2`, written by `ai/scripts/motion/explainer_lab2.py`. Unlike round 1 (overlays), the full-frame round-2 layouts carry their light ground as a "Light background" object, so their ink text stays readable wherever they are placed.

## Round 3: briefs the pack could not serve before

Chosen from [reading a brief](../references/craft/reading-a-brief.md) and the wiki's [explainers](../../wiki/genres/explainers.md), [infographics](../../wiki/genres/infographics.md) and [UI and UX demos](../../wiki/genres/ui-ux-demos.md) pages, against what rounds 1 and 2 already cover (a straight three-box flow, old-vs-new columns, a single key term, a quiz, a timeline) and the cookbook's [animated arrow](../../wiki/cookbook/animated-arrow.md), [bullet list](../../wiki/cookbook/bullet-list.md) and [before and after slider](../../wiki/cookbook/before-after-slider.md). Built and verified on 0.1.6 (rev 1105) on 2026-10-28. Every move is baked as keys in `explainer_lab3.py` (no presets to apply): `step_in()` writes the pack's Step in, `pulse()` its Emphasis pulse. Every text passes lint `contrast:true` at 4.5:1: round 3 uses deeper accents (blue #2B58D6, coral #B93222, green #17794A, muted #565C70, all at 5.1:1 or better on the ground), converted with the renderer's BT.709 curve. Names, numbers and claims are sample copy; the phone is a shape stand-in. Frames are comp frames. Clip-id prefixes: `ece_`, `epc_`, `eld_`, `eis_`, `efq_`, `ewd_`, `etp_`, `epb_`. Every template carries its own "Light background".

| Template | Brief it serves | Measured | Overshoot | Lint (lab, contrast:true) | Placed |
|---|---|---|---|---|---|
| Cause and effect ([ex-cause-effect.md](ex-cause-effect.md)) | why prices rise, how one event leads to the next (a chain that branches) | cause card settles f13; links draw f24-36 and f58-70; effect cards settle f43, f51; result settles f77; one pulse to 105% (f96-112) | arrow heads 9.8%; pulse 5% | 0 / 0 / 0 | 0 / 0 / 0 |
| Pros and cons ([ex-pros-cons.md](ex-pros-cons.md)) | "should you...?", trade-offs, a decision with a verdict | lists f6-52 and f50-84; seesaw f84; tilt from f96, one overshoot (116.5%), settles f117; verdict settles f129 | icon discs 9.8%; seesaw 16.5% (curves read 19%, baked) | 0 / 0 (25 notes) | 0 / 0 / 0 |
| Labelled diagram ([ex-labelled-diagram.md](ex-labelled-diagram.md)) | anatomy of, what's inside, parts of a product | body settles f12; labels at f34, 56, 78, 100 (dot, leader f+2-14, label f+10); last settles f119 | dots 9.3% | 0 / 0 / 0 | 0 / 0 / 0 |
| Icon steps ([ex-icon-steps.md](ex-icon-steps.md)) | how it works in three steps, onboarding | cards f0, 34, 68 (settle +13); icons draw from card + 12; arrows f24, f58; title 3 settles f95 | tiles 9.8% | 0 / 0 / 0 | 0 / 0 / 0 |
| FAQ card ([ex-faq-card.md](ex-faq-card.md)) | common questions, support and help | rows f6, 14, 22; row 1 opens f44: panel settles f52, chevron turns 180 deg by f58, rows below settle f53; answer settles f61 | 0% | 0 / 0 (20 notes) | 0 / 0 / 0 |
| Word definition ([ex-word-definition.md](ex-word-definition.md)) | word of the day, glossary, language lessons | word settles f9; speaker f22; syllables pulse f48 and f60 (112%); definition settles f59; example settles f83 | speaker 9.8%; pulses 12% | 0 / 0 (4 notes) | 0 / 0 / 0 |
| Tip carousel ([ex-tip-carousel.md](ex-tip-carousel.md)) | "3 tips", do's and don'ts, swipe-through lessons | cards slide in f6, 72, 138 (18 f, quint) with the one leaving; each tip on screen 66 f or more; dot settles f149 | 0% | 0 / 0 (23 notes) | 0 / 0 / 0 |
| Problem and solution ([ex-problem-solution.md](ex-problem-solution.md)) | pain-point pitch, the old way vs the fix | problem f4-46; disc settles f59; solution wipe f56-76 (settles f69); headline settles f87; ticks f94-114 | disc 9.8% | 0 / 0 / 0 | 0 / 0 / 0 |

Notes are `repeated_key_value` on holds and `speed_jump` where a card slides or the seesaw starts to tip (intended). `inspect qc` at 240 px found no flashes on any round-3 comp (the FAQ, labelled diagram, word definition and problem and solution report the final hold as a freeze). Each template was checked with the text-gap audit (`audit_text_gaps.py`): no flags; the closest pair is 20 px (the word definition's dash; a label and its leader line). The audit caught a 10.1 px label-to-note gap in the labelled diagram and the FAQ's letter-in-disc, both fixed. Text bounds were measured against each card, pill and panel with `carvercat_authoring geometry` (the script also raises when a line is wider than its box). Full-frame looks of every placed template at its moving frames and its last frame show nothing cut ([KI-144](../references/known-issues.md#ki-144), [KI-157](../references/known-issues.md#ki-157)).

### Round-3 pitfalls
1. **The old accents fail as text fills.** White on coral #FF6B5B is 2.9:1 and on green #2BB673 2.6:1 (earlier labels measured 2.9-4.3). Use #B93222 and #17794A for fills that carry white text, and check tags at 32 px: a 28 px white tag on #C93A28 read 3.77:1 at one frame.
2. **Tracking below 1.0 garbles text.** 0.35 drew "CAUSE" as "ESUAC" (reversed, overlapping); 1.0 is normal spacing and each 1.0 more adds about 1.3 em. Tracked caps use 1.07 ([KI-117](../references/known-issues.md#ki-117), [KI-045](../references/known-issues.md#ki-045)). At 1.4 to 1.6 caps run far past their pills (lint reported 1.01:1 for the part of "SOLUTION" outside its pill, [KI-157](../references/known-issues.md#ki-157)).
3. **Line spacing is a multiplier of the font's own leading.** 1.1 rendered a 1.46 em pitch and 1.2 about 1.6 em; use 0.9-1.0 for headlines and short body lines.
4. **Move the whole strip with one ease.** The carousel's leaving and arriving cards used different eases first and really overlapped for a few frames (lint `text_overlap` 15-35%); the same ease over the same frames keeps them a fixed 1100 px apart.
5. **Bake what rides a rotating part.** The seesaw's balls sit on the beam ends: end point plus the beam normal, computed every frame from one damped curve, so the overshoot is real and settles by f117. `inspect curves` reads baked lanes wrongly (19% for 16.5%, [KI-152](../references/known-issues.md#ki-152)).
6. **An accordion is anchored scale plus a position shift.** The answer panel grows with scale Y anchored at its top behind the open row, and the rows below slide by the same distance over the same frames.
7. **Keys must start inside the clip.** Position keys that began 2 f before a Q letter's own clip start were a lint error (`key_outside_clip`).
8. **Small text can trip `text_too_small`.** A "-" and a lower-case "noun" at 28-30 px are 6 px and 15.6 px tall (limit 18): draw the dash as a line, set the part of speech in capitals.
9. **A letter inside a small disc is an "overlap" to the audit.** The FAQ's Q at 60 px was flagged (-40.7 px); at 84 px (over the audit's 80 px limit) it is not.

## Sample film

`categories/explainer/ex-showcase` is a 435 f (14.5 s) master: process steps → icon grid (2% push on both) → pointer callout → timeline. Lint 0/0/0. QC at 96 px reports the thin-line timeline as a freeze.

## Round-2 sample film

`categories/explainer/ex-showcase-2` is a 1200 f (40 s) master at 1920 × 1080 that plays the round-2 templates back to back, placed from the Library with `library.place` + `template.apply` (rebuild: `ai/scripts/motion/recipes/showcase2.py explainer`). Verified 0.1.6 (rev 1105), 2026-10-28: master lint 0 / 0 / 0. Qc (240 px) notes the reading holds after each build as freezes.

## Pitfalls and facts (0.1.6)

1. **A 3-gon at rotation 0 points right** (measured). An arrow head for a line at math angle θ (counter-clockwise, y up) takes the stored rotation θ; in design units (clockwise, y down) that is `rotate` −θ.
2. **Leave the last item time to be read.** The timeline's last milestone landed at f110 of 120 and lint flagged `reading_time` (7 f readable). The comp now runs to 150 f.
3. **Template names share one Library namespace** with the bundled packs; a duplicate name shows twice in `library.list`. Check before naming.

Inspiration: common explainer-video conventions (numbered steps, icon grids, callouts, timelines). No external text or code was used.
