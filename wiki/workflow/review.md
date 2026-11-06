---
id: workflow/review
title: Review and feedback
section: workflow
tags: [review, feedback, revisions, qc, lint, expect, rounds, checklist, notes]
styles: [all]
topics: [workflow, quality]
related: [workflow/animatics, workflow/delivery, principles/appeal, accessibility/photosensitivity, accessibility/readability]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.premiumbeat.com/blog/how-to-stop-video-revision-requests, https://ashoreapp.com/design-revision/, https://milanote.com/guide/motion-graphics-pre-production]
---

# Review and feedback

Review is where a film gets better or gets worse. Good review separates **what is objectively wrong**
(timing errors, typos, unreadable text, flashes) from **taste**, fixes the first automatically, and collects
the second in a few well-defined rounds.

## The idea

- **Self-review first**: catch every objective error before the client sees it. Clients who find typos stop
  trusting everything else.
- **Rounds with a purpose**: animatic (timing and story), first animation (motion and look), final (polish
  and corrections). Agree the number of rounds in the brief.
- **Batch notes**: one consolidated list per round with timecodes, not a stream of messages.
- **Review at delivery conditions**: phone size, muted, then full screen with sound.

## Rules of thumb

- Fresh eyes: review after a break, at full speed, twice (once for story, once for detail).
- Every note gets a timecode, an user and a status.
- Separate "must fix" (errors, legal, accessibility) from "could change" (taste).
- Re-run the automatic checks after every change; fixes break other things.

## Measured in Carvercat: what the automatic checks caught in the labs

| Check | Call | Caught in the wiki labs |
|---|---|---|
| Timing table | `carvercat_inspect {mode:"timing"}` | enter, move, settle and exit frames for every object |
| Lint | `carvercat_inspect {mode:"lint"}` | text too small (24 px Rethink Sans), reading time (3 frames short at every frame rate), text outside graphics safe, speed jumps at intended stops, an invisible null as `never_visible` |
| Contrast | `carvercat_inspect {mode:"lint", contrast:true}` | a 1.57:1 caption; grey text at 2.08–3.93 vs 4.5 wanted (Regular text under 34 px is not checked, [KI-142](../../ai/references/known-issues.md#ki-142)) |
| Your intent | `carvercat_inspect {mode:"expect", checks:[...]}` | a match cut landing within 2 px on both sides of the cut |
| Delivery QC | `carvercat_inspect {mode:"qc"}` | flashes over 3 a second over a quarter of the frame; near-black stretches flagged as `black`; loop seams (brightness only, [KI-140](../../ai/references/known-issues.md#ki-140)) |
| Masked work | `carvercat_inspect {mode:"composite"}` | when masked text actually starts and finishes contributing pixels |
| Pictures | `carvercat_look` | rendering surprises lint cannot see (squeezed corners in a scale flip, a shadow lost on a dark ground, which side a gradient lights) |

Numbers for time, pictures for composition: the checks found timing and legibility problems that a contact
sheet hid, and the looks found visual problems no number showed.

## Do and don't

- Do write `expect` sentences for the important moments when you plan them; re-run them after every edit.
- Do keep a review checklist per style ([review by style](../../ai/references/craft/review-by-style.md)).
- Don't send a version with open lint errors.
- Don't accept vague notes ("make it pop"); ask for the frame and the goal.

## Checklist

- [ ] `lint` (with `contrast:true`), `expect` and `qc` are clean or every finding is explained.
- [ ] Watched at phone size, muted, and full screen with sound.
- [ ] Notes batched with timecodes; must-fix separated from taste.
- [ ] Version number and changes listed in the delivery note.

## In Carvercat

- The cheapest-first review ladder (timing → lint → expect → look → detail → qc) is the app's own
  `carvercat://review` resource; the skill's version: [review checklist](../../ai/references/craft/review-checklist.md).
- Compare a new version against an approved look: `carvercat_look {baseline:"v1"}` then later
  `{baseline:"v1"}` again; or `{diff:true}` for cells changed since the previous look.
- Compare with a Resolve render: `carvercat_look {compare:"folder"}`.
- Revisions without breaking ids: [job playbook](../../ai/references/workflows/job-playbook.md).
