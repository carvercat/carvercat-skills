# Job playbook

Read this at the start of any Carvercat job, and again when you are unsure whether to continue, stop, ask or report. It holds the generic rules for running a job end to end and the user's preferences for how agents work.
Task-specific workflows: [captions-and-voiceover.md](captions-and-voiceover.md), [rtl-and-arabic.md](rtl-and-arabic.md), [resolve-handoff.md](resolve-handoff.md), [export-and-delivery.md](export-and-delivery.md). Product defects: [../known-issues.md](../known-issues.md).

## Contents
1. [The job loop](#1-the-job-loop)
2. [Scope and permission](#2-scope-and-permission)
3. [Mutation safety](#3-mutation-safety)
4. [Review and verification](#4-review-and-verification)
5. [Revisions](#5-revisions)
6. [Working beside the user](#6-working-beside-the-user)
7. [Stopping and handing over](#7-stopping-and-handing-over)
8. [Reporting and files](#8-reporting-and-files)

## 1. The job loop

1. **Brief.** Restate the exact scope (sections, frame ranges, tracks, what must not change). Ask only when the brief is ambiguous.
2. **Bind.** Pull the skills repo; identify the live editor and record version, commit, `sourceDirty`, `builtUnixSeconds`; read live schemas and `tools/list`; read the live Resolve timeline ([resolve-handoff.md §1–3](resolve-handoff.md#1-connect-to-the-right-editor)).
3. **Prepare.** Duplicate the timeline, snapshot the baseline, create the companion project, save a milestone.
4. **Build one representative comp** (or one section) with native objects, then look at entrance, hold and exit frames.
5. **Review.** Show the user; fix systemic feedback in shared helpers (one measured title helper and one softer "pop" default fixed the same issue across five comps).
6. **Expand** to the remaining comps with the approved helpers.
7. **Deliver** with verified exports and placement; run a combined composite review after any design-system change (an isolated comp looked fine but overlapped a later hierarchy on the real timeline).
8. **Report** and save everything.

Keep one deterministic build script per comp; full rebuilds then take minutes and revision rounds are cheap. Use `carvercat_batch` (≤256 steps, one undo step) rather than hundreds of single calls: an equal-output scene went from 48 requests to 2.

## 2. Scope and permission

- Do exactly the requested scope. "Prepare only" means no creative edits. Do not change project or timeline settings, grading, footage, audio or captions outside scope.
- When the user says stop, stop creative work immediately, save, and write the handover. Resume only on an explicit go-ahead.
- No commits or pushes unless the user authorises them. A later authorisation covers what it names (e.g. publishing reviewed notes), not pending product work.
- Creative jobs do not change app source, rebuild the app, install software or change client configuration unless authorised. Never install a font automatically; ask.
- Recording a product requirement is not authorisation to implement it.
- If an action is blocked by policy (e.g. a file deletion), report it with the exact message; do not try an alternative route.

## 3. Mutation safety

- Every `refused:true` stops dependent work. Raise on it; never continue a builder after a refusal (an early script continued past a refused save).
- Some harmless no-ops are reported as refusals ([KI-010](../known-issues.md#ki-010)). Read state first and write only fields that differ; tolerate only exact, identified no-op wording. Never ignore arbitrary refusals.
- A timeout after a write is an unknown outcome: inspect state, files and durable records; never replay a mutation, export, transfer or save.
- Use explicit IDs and explicit frames, never the current selection or playhead, whenever they affect the result. Guard batches with `expected_revision` and the expected document.
- Comp-local IDs repeat across comps: switch to and assert the comp by its live name before targeting objects.
- Compare by stable identity. Comparing whole discovery dictionaries included mutable `selected` flags and matched the wrong object.
- Flush or combine pending plans before a step that reads existing channels.
- Checkpoint (save a milestone) before dependent or risky operations.
- Distinguish your own failures from product defects. Classify every problem as product bug, client/host configuration, operator error, or untested coverage. A failed report variable or assertion after acknowledged mutations is not a command failure: inspect state and resume deliberately; do not rebuild blindly.

## 4. Review and verification

- Never report a scene done without looking at actual frames. Successful writes did not catch wrong fonts, default strokes covering fills, or misplaced paths.
- Use numbers and pictures together: measured bounds and lint first, then full-resolution composites over the real footage.
- Probe resolved fonts for every text object before export.
- Claim precisely what you checked: "sampled composite QA", not "full playback"; "designed stagger", not "forced-aligned"; "verified on this build", not "fixed". Say which frames you actually looked at.
- Check subject safety on the composite: faces, torsos, hand gestures. Mirrored rays and bursts on a torso read as unintended emphasis.
- Keep pending items visible: user approval, full audio/playback review, lint warnings kept on purpose.

## 5. Revisions

- Save a named milestone (`before_<change>`) before each revision; keep accepted versions as separate saved projects or comps.
- New render prefix per revision; keep old renders and never deliver invalid intermediates.
- Change only what was asked; compare untouched comps against their pre-revision snapshot (ignoring derived cache fields such as `fontResolved`). Never hand-edit project JSON to remove derived differences.
- Re-read the live timeline after every user edit; preserve their changes.
- Prefer shared role sizes, spacing and motion helpers so one fix applies everywhere.

## 6. Working beside the user

- The user owns the interface. Their scrubbing is view state; their clicks during an open agent transaction roll it back. If they switch comps, your next commands act on their comp: check `carvercat_list` when a reply looks wrong, and ask them to keep hands off during scripted builds and force-reopen loops.
- Let the user watch: agent edits bring the workspace back to Canvas/Create.
- Work through MCP and Resolve scripting, not desktop UI automation; the PC may be locked.
- Preferences seen across jobs: smooth curves everywhere, no linear segments; captions without boxes unless asked; solid white Arabic without outline; fixed type roles; keep spoken timing over lint suggestions; preserve every user edit; numbers clear and static in fast speech.
- When the user reviews and accepts ("looks good"), record the exact words and what they reviewed.

## 7. Stopping and handing over

A stop or handover note states:
- saved project state: native master path, comps and what each contains, Resolve project/timeline, tracks and frame ranges used;
- what worked and which product/documentation issues were found (link [../known-issues.md](../known-issues.md));
- review status: what was checked, what is pending (user approval, audio review), warnings kept on purpose;
- where editable files, sequences and evidence are (a file index such as `EDITABLE-FILES.md` or a handover text in the job folder).

## 8. Reporting and files

- Keep a running job log in the job folder: live build, steps, observed vs expected, workaround, verification, status. Never record tokens or credentials.
- Promote tested, reusable workflows into `ai/references/`; put product defects in [../known-issues.md](../known-issues.md) with build and status. No project, client or person names there.
- Job media, projects, renders and evidence stay in the job folder, never in a repository, unless the user explicitly asks.
- Keep video-editing craft in the video-edit notes and Carvercat behaviour here.
