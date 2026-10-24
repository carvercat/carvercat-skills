# Export and delivery

Read this when you render anything out of Carvercat: PNG sequences with alpha, stills, MP4s; when an export call times out or is interrupted; and before you hand any file to Resolve or to a person.
Placement in Resolve is in [resolve-handoff.md](resolve-handoff.md). Command basics: [../mcp-essentials.md](../app/mcp-essentials.md), [../api-gotchas.md](../app/api-gotchas.md).

## Contents
1. [Settings](#1-settings)
2. [The export job model](#2-the-export-job-model)
3. [Agent exports, visibility and interruption](#3-agent-exports-visibility-and-interruption)
4. [Verify every output](#4-verify-every-output)
5. [Orchestration guards](#5-orchestration-guards)
6. [Delivery checklists](#6-delivery-checklists)

## 1. Settings

- Overlay delivery is native export, not `carvercat_render`. On an early pre-release build `carvercat_render` wrote RGBA PNGs with alpha 255 everywhere on a black ground ([KI-070](../known-issues.md#ki-070)).
- PNG sequence with alpha:
  `export.set {settings: {format:"sequence", sequenceType:"png", alpha:true, scale:100, range:"comp", dir:<existing dir>, name:<versioned name>, collision:"ask"|"numbered"|"replace"}}` → read `export.plan` → `export.run` once.
- MP4: `export.set {settings: {format:"video", videoCodec:"h264", container:"mp4", range:"comp", sound:true, soundCodec:"aac", dir, name, collision:"replace"}}` → `export.run`.
- `export.set` takes a `settings` object, not flat arguments. One unknown key refuses the whole call and later `export.plan`/`export.run` refuse until a valid `export.set` ([KI-071](../known-issues.md#ki-071)).
- A still: range `playhead` after seeking.
- Output layout: `<dir>\<name>\<name>_00000.png`. The source snapshot (`.carvercat-export-source.json`, or `.<name>.carvercat-export-source.json`) and the progress record `.<name>.carvercat-export.json` sit beside it. Native export is straight RGBA at the comp size.
- For Resolve delivery, the Deliver API (`deliver.*`) is the permanent route; see [resolve-handoff.md §5](resolve-handoff.md#5-route-b-native-fusion-transfer).

## 2. The export job model

Current since the 2026-10-01 exact-release build (first seen live on a pre-release build). Older builds blocked the call.

- `export.run` returns at once with the durable job path in `why`. Poll `export.status`; never call `export.run` again for the same work.
- Each job owns an immutable document snapshot (revision + source hash). Later edits are not in it; Deliver says so.
- States: `queued → running → complete`, with terminal `stopped`, `failed`, `interrupted`. Status v2 fields: `state`/`phase`, `terminal`, `recoverable`, `done`, `total`, current `file`, immutable `source`, `error`, settings and intended outputs.
- A queued/running record whose worker disappeared (e.g. app restart) becomes `interrupted`. `export.resume {job}` continues an image sequence from its snapshot and recorded progress. Atomic single-file (video) restart is not yet guaranteed ([KI-076](../known-issues.md#ki-076)).
- A user cancel leaves a terminal `stopped` record with progress and reason.
- Transport loss never cancels an export and never authorises a replay. Treat a timed-out reply as unknown; read durable status and file counts.
- Reading a live job JSON on Windows can briefly raise `PermissionError` or return partial JSON. Retry the read within your deadline; never replay the export to fix a read error.
- Superseded: on builds before the async model, `export.run` blocked and outlived client timeouts (45 s in one helper, the relay's 120 s window in another) while frames kept rendering. The workaround then was a dedicated 1800 s socket deadline in a background process. Not needed on current builds.

Speed reference: a 434-frame 1080×1920 comp wrote in under a minute.

## 3. Agent exports, visibility and interruption

Requirements, implemented and verified in the 2026-10-01 exact-release build. Check the live build exposes `carvercat_state.revision`, top-level `expected_revision` and v2 `carvercat_list` tracks before relying on them; an older installed executable (a pre-release build) did not.

- Any export, human or agent, opens Deliver and keeps live or terminal status visible there.
- Export runs in a background worker; the editor must stay responsive (a timeline seek measured 0 ms during a live 180-frame export; limit 250 ms). The user can scrub, zoom and navigate; this never cancels the export.
- When an agent issues a document command, the workspace returns from Deliver to Create (Canvas) so the person can watch the work.
- Multi-command edits: read `carvercat_state.revision`, pass it as top-level `expected_revision`, use `transaction=begin/commit`. A stale revision returns `conflict:true` with `expected_revision` and `current_revision` before any mutation: re-read list/state, then decide.
- A manual mouse or key press during an open agent transaction is a takeover: the uncommitted transaction rolls back before the gesture lands. Committed agent work stays as normal undo history and is never secretly undone.
- User and agent mutations pass through one serialized command boundary; no silent last-writer-wins.
- Every new command, option, state field or refusal must land in the generated app schema AND as a tested workflow or gotcha in this skills repo. Work is not complete with only one of them.

## 4. Verify every output

Completion status is necessary, not sufficient. A job once reported terminal complete with correct counts while frames held corrupted glyphs ([KI-073](../known-issues.md#ki-073)).

For every PNG sequence:
1. Durable record: terminal `complete`, `done == total`, `error == null`.
2. Exact frame count; contiguous names with no gaps or extras.
3. Decode every file (Pillow): exact width × height, mode RGBA.
4. First and last frames fully transparent when the design fades in/out; a visible interior frame has alpha 0..255. Check section boundaries in multi-section jobs.
5. Flag edge-reaching alpha (`getchannel('A').getbbox()` touching the frame edge) and frames with alpha min = max = 255.
6. Compare temporal samples of disk frames with native `carvercat_look` at the same frames; inspect glyph geometry (triangles, stray lines, displaced strokes, missing fill).
7. Review alpha over the actual bright footage. A glass panel pixel such as RGBA(233,233,233,40) looks opaque white when viewed alone on black.
8. Numeric layout checks: alpha inside a head/face box per frame, safe area (top ~13%, y_up ≤ 0.87), text width; then composite over real plates.

Stills: unique explicit filenames, exact expected count, decode each. Video: check duration, frame count, fps, audio presence, first/last frame, and no black or music-only tail; loudness/true-peak needs a separate master review.

## 5. Orchestration guards

- Before each export: switch to the comp and assert live name, width, height, fps and duration ([captions-and-voiceover.md §5](captions-and-voiceover.md#5-multi-section-caption-jobs)).
- Before saving: compare the open project's identity (path, comps, revision), not only the comp count. A session reset once left a blank Comp 1 open; a follow-on script exported and saved it over the real project ([KI-012](../known-issues.md#ki-012)). Recovery came from the export job's immutable source snapshot, reopened through MCP.
- Stop any shell chain when a predecessor fails; do not let a later step run after a refusal.
- Every render gets a new versioned prefix (`_v1`, `_v2`, `_fixed_01`…). Keep older versions; mark invalid attempts and never import them.
- Durable job completion does not prove the currently open document is the intended project.
- An intentionally stopped intermediate export is never delivered.

## 6. Delivery checklists

| Deliverable | Must pass before handoff |
|---|---|
| PNG sequence for Resolve | §4 steps 1–7; versioned prefix; Resolve import at timeline fps, Straight alpha, exact start/duration ([resolve-handoff.md §4](resolve-handoff.md#4-route-a-import-png-sequences)) |
| Native Fusion clip | ready plan with fresh scope; one send; preserved neighbours; graph contents; saved/reopened; RTL correction if Arabic |
| Verification stills | timecode asserted before and after; explicit names; count reached |
| MP4 / master | duration and fps; audio present and balanced by listening; loudness/true peak; first/last frame; no black or audio-only tail |
| Editable source | saved `.carverproj` in the job folder (never only in Temp), reopened and checked; file index of comps, assets and sequences |
