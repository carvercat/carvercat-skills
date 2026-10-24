# Captions and voiceover

Read this when you build or revise captions over speech: timing words to a voiceover, retiming after the editor moved the VO, splitting a long edit into several caption comps, or styling English captions.
Arabic/RTL specifics are in [rtl-and-arabic.md](rtl-and-arabic.md); getting the result into Resolve is in [resolve-handoff.md](resolve-handoff.md) and [export-and-delivery.md](export-and-delivery.md). Command basics: [../mcp-essentials.md](../app/mcp-essentials.md), [../api-gotchas.md](../app/api-gotchas.md).

## Contents
1. [Timing sources](#1-timing-sources)
2. [Retiming captions to a moved or new voiceover](#2-retiming-captions-to-a-moved-or-new-voiceover)
3. [Word timing and stagger](#3-word-timing-and-stagger)
4. [Reading time and phrase splitting](#4-reading-time-and-phrase-splitting)
5. [Multi-section caption jobs](#5-multi-section-caption-jobs)
6. [Caption style that has been verified](#6-caption-style-that-has-been-verified)
7. [Smooth curves and card motion](#7-smooth-curves-and-card-motion)

## 1. Timing sources

- Re-read the live working timeline (video tracks, audio spans, subtitle tracks) before you author. Earlier task notes and handover descriptions are not current truth. A handover's approximate content labels have been wrong; the live cut and subtitles overrule them.
- Treat automatic captions (ASR) as timing and copy evidence that needs review, not as correct spelling or grammar. If the project has a second, corrected subtitle track, use it as the text source (one job's track 1 had "turiz 10" for "210").
- Preserve the checked caption words. You may split one phrase across several text objects for emphasis, correct a proper-noun spelling, or simplify filler wording only when the user approves. Keep every benefit and number.
- Keep the reference subtitle track and its text. Hide it only on the working duplicate, and only after the new overlay is delivered.
- Log each caption's comp-local start/end and its timeline start/end.

## 2. Retiming captions to a moved or new voiceover

Tested on an early pre-release build (2026-09-28) with local Resolve scripting.

1. Re-read the working timeline's V1/V2/V3 and audio spans.
2. Compare the current VO clip's source trims and duration with a trustworthy earlier baseline (for example the untouched original timeline). Activate each Resolve timeline before you query it, then re-activate the working timeline.
3. A constant offset is justified only if source in/out and duration match AND both timeline endpoints moved by the same amount. Example: left offset 110, right offset 41, duration 570 matched; both endpoints moved +37; the subtitle clips had not moved. New caption time = reference time + 37, with the first phrase clamped to the audio start.
4. Apply the offset to the new native caption timing. Never move the user's audio or video to fit stale reference subtitles. Save `reference.json` and `timing-offset.json` with the job.
5. Save an editable milestone, then create a separate comp whose local frame 0 maps to the verified timeline start.
6. Place the overlay on a free track above the footage (assert it is empty first). Afterwards verify every existing clip span/property and the settings are unchanged. Check the composite over both busy and bright/dark plates.
7. Hidden subtitle cues that moved by a different amount than the picture edit are not an authoritative replacement for source-edit timing. Re-read the picture cut.

## 3. Word timing and stagger

**Phrase timing is evidence; uniform word stagger is design.** Never label a uniform stagger "forced-aligned" without word-level evidence.

- Native word stagger: `stagger.new` → `stagger.connect` (`text.position`, `fill.opacity`) → `stagger.set by=word gap=N order=forward` → key `text.relative.position` ([0,-0.04]→[0,0]) and `text.fill.opacity` (0→1). Gap 3–12 frames (about the mean spoken interval); 3 frames is the common caption value. A typical upward entrance is 23 px over 9 frames with short eased fades.
- English: forward (left-to-right) word stagger inside ONE text object, plus a separate whole-object opacity fade for the exit. Six consecutive reveal samples are enough to prove order.
- The stagger replays the whole key timeline per part, exit keys included. The last part finishes `gap × (parts − 1)` frames late and can overrun the clip or comp end: gate it with the clip's `transform.placement.opacity`.
- A text takes one staggered preset per property; a staggered exit on a property already used by a staggered entrance is refused. Use a whole-block exit.
- Per-letter blur-in: `effect.add cap=blur`, `stagger.new`, connect `text.position`, `text.opacity` and `blur.size`, `stagger.set by=character gap=1.5..2`. Key `src.e_src_text_relative_<id>.position` [0,-0.045]→[0,0], `.opacity` 0→1 and `fx.e_fx_blur_<id>.size` ~22→0 over ~12 frames. A new blur starts at size 10, so always key or zero it.
- Native stagger has ONE uniform gap. It cannot store an irregular per-word speech schedule (open, see [KI-041](../known-issues.md#ki-041)). On the Fusion route (an early 0.1.4 pre-release build), the editable Follower character-delay curves in Resolve carry the irregular schedule; save and read them back, and reapply them after every resend because a resend overwrites them. The saved native source alone does not keep the schedule.

### Getting word onsets
- Offline forced alignment with the approved text: `pip install pocketsphinx` (bundles an en-US model). Run `Decoder.set_align_text` on 16 kHz mono audio per phrase (split at silences). Add out-of-vocabulary words with `add_word`. `Segment.start_frame`/`end_frame` are 10 ms units. Accuracy is about 1–2 frames. Script: `../../scripts/motion/vo_align.py`.
- A locally cached large-v3 transcription model plus approved-text forced alignment also worked; at 30 fps treat the result as approximate.
- Keep timeline onsets separate from comp-local frames and from the entrance duration.
- If an ASR onset spans a pre-speech pause and user review plus the waveform disagree, correct that one onset (one CTA word moved 21 frames later) without shifting later words.

## 4. Reading time and phrase splitting

- Use 2–5 word phrase cues; drop trailing commas and full stops. Cue boundaries must cover the voiced span without gaps. Holding a phrase across a picture cut is allowed when deliberate.
- Lint `reading_time` warnings on fast speech (e.g. 20 readable frames versus a suggested 25) are recommendations. Keep the spoken timing; do not extend a caption over the next spoken line. Record the remaining warnings in the job report.
- Shortest acceptable standalone label seen: 8 readable frames. Make percentages fixed values, not count-ups, in brief speech.
- An over-wide caption: split it into two semantic phrases with their own word timing. Do not shrink the global caption size for one line.
- A longer hold on a highlight can overlap the next caption in time. Keep the voice cue and place the highlight in a measured separate zone; run an all-visible-span overlap check.
- One-frame continuation fragments cannot take a two-key entrance with an out handle on the only key. Deduplicate same-frame key pairs or hold the continuation immediately.

## 5. Multi-section caption jobs

Tested on a pre-release build (2026-09-29): a four-section job at timeline frames 0..233..408..1017..1318, 1080×1920, 30 fps.

1. Capture the live target timeline, caption cues, source trims, occupied tracks and settings.
2. Divide at real editorial beats with exact integer boundaries. Define each section's local zero. Shared boundaries must not duplicate a frame (`[0,233)`, `[233,408)` …).
3. `edit.new` creates an empty default "Comp 1"; `comp.new` then appends. Query `carvercat_list` comps: reuse the default comp, or verify it has zero clips and `comp.delete` it. Never infer comp indices from loop order (one export loop exported the empty default comp as section 1 and shifted every section by one).
4. Before every edit and every export, switch to the discovered comp and assert its live name, width, height, fps and duration. Object IDs are comp-local and repeat (`clip_1` in every comp).
5. Probe resolved fonts per comp (see §6).
6. Export each section to its own versioned prefix and validate it (see [export-and-delivery.md](export-and-delivery.md#4-verify-every-output)). Old outputs from a wrong loop are invalid; never deliver them.
7. Place each section on the overlay track at its exact range; compare all other tracks and settings before/after ([resolve-handoff.md](resolve-handoff.md)).
8. Keep one-off design mutations out of reusable export scripts (a footer-size edit left in an exporter would undo a later revision).

## 6. Caption style that has been verified

| Item | Verified value |
|---|---|
| English fonts that resolved | Poppins Bold, Anton Regular, Impact **Normal** (not "Regular") |
| Readable white caption shadow | opacity 0.88, softness 0.006, downward offset 0.0035 |
| Tight shadow | `fx.e_fx_shadow_<id>` x .005, y -.005, softness .008, opacity .38 (defaults x .012, y -.012, opacity .5 read too far away) |
| Thin white outline | `text.outline.paint='solid'`, `text.outline.color=[1,1,1,1]`, `text.outline.thickness=0.018`. Thickness alone does nothing while paint is off. |
| Caption position (9:16) | centred x 540, y ~1110–1120 (about 58% down), clear of faces and map pins |
| Role sizes (one job) | headline 0.091, body 0.056; footer 0.049; amounts 0.158 |

- Shadow alone makes captions readable; do not box normal captions unless the brief asks.
- Fix type roles (one size per role) across cards; inconsistent sizes were the main user complaint in one revision.
- When the user says "no repeated orange", change text colour only; keep icon accents.
- Font rules (resolved-face probes, restart after install, style names): [rtl-and-arabic.md §1](rtl-and-arabic.md#1-fonts) applies to all scripts.

## 7. Smooth curves and card motion

- House rule: every animation has smooth curves, no linear segments. Give every keyed segment explicit untied handles: out (0.32, 0), in (0.68, 1). Settle curve (fast start, long landing): out (0.16, 0.95), in (0.30, 1).
- "All smooth" means enumerating every keyed underlying parameter with `param.list` (opacity, geometry, transform, text-relative reveals) and asserting frames and handles with `key.list`. Stagger slot proxy params duplicate the underlying text-relative curves: do not author them twice. Holds are constant values, not linear moves. Audits of 60, 129, 132 and 150 tracks have passed this way.
- To revise a move: read and remove the existing position keys, rebuild the intended entry/hold/exit keys, assert the `key.list` frame list, then sample per-frame positions to confirm monotonic easing. A good final still proves nothing about the motion.
- Top-anchored panel growth without squashing text: key the rectangle height from ~2 px to full over ~9 frames, and key its centre from `top + h0/2` to `top + h/2` with identical handles. Text stays independent and reveals after the panel opens. Probe `cy − height/2` across frames to verify the top edge is fixed.
- Stacked cards: newest group at opacity 1.0, older groups ease to 0.82; card, text, icon and accent fade together.
- Extending a highlight's hold: extending `clip.trim` and placement opacity does not extend an independent `text.relative.opacity` exit. Clear or retime the obsolete channel by its discovered path and check a rendered pixel past the old end ([KI-049](../known-issues.md#ki-049)).
- Glass cards: ~20% white fill, fine translucent white rim, subtle shadow. It is composited translucency; a PNG cannot blur the Resolve plate behind it.
