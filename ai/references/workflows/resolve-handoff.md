# Resolve handoff

Read this when a job starts from or ends in a DaVinci Resolve project: preparing a working timeline and blank Carvercat companion, connecting Carvercat to Resolve, importing PNG sequences, sending native Fusion clips, exporting verification stills, and proving that nothing else changed.
Rendering and validating the files themselves is in [export-and-delivery.md](export-and-delivery.md). Tested on Resolve Studio 21.1 / 21.1.0.14 (Windows) unless noted.

## Contents
1. [Connect to the right editor](#1-connect-to-the-right-editor)
2. [Prepare the Resolve project](#2-prepare-the-resolve-project)
3. [Read and protect the timeline](#3-read-and-protect-the-timeline)
4. [Route A: import PNG sequences](#4-route-a-import-png-sequences)
5. [Route B: native Fusion transfer](#5-route-b-native-fusion-transfer)
6. [Still export and composite review](#6-still-export-and-composite-review)
7. [Audio, timeline end and trims](#7-audio-timeline-end-and-trims)
8. [Save, back up and clean up](#8-save-back-up-and-clean-up)

## 1. Connect to the right editor

- Identify the actual running editor and record version, commit, `sourceDirty` and `builtUnixSeconds` from `carvercat_state`. Read `carvercat://index`, `tools/list`, `carvercat_list`, `carvercat_state` and the live command/conventions resources. Trust `tools/list`, not prose tool counts.
- If the chat has no Carvercat tools, use the loopback relay. Current builds publish the endpoint in `carvercat-mcp-editor.pid` (`Client()` validates PID and handshake; `CARVERCAT_MCP_ENDPOINT` selects another file). Superseded: older builds used `%TEMP%\carvercat-mcp-window.pid` (PID on line 1, port on line 2). Protocol: one JSON-RPC object per line, one response per id-bearing request.
- Confirm the PID is the visible app you mean and owns the listener. Never hard-code a port (it changes every restart), never start a second hidden document, and do not change the chat client's global MCP config without authorisation. A stale config pointing at an old agent executable was a possible cause of missing tools ([KI-001](../known-issues.md#ki-001)).
- An open app does not prove the endpoint is live. A refused port or a stale PID file means rediscover (re-read the endpoint file after any restart) before any mutation ([KI-004](../known-issues.md#ki-004)).
- Use bounded read timeouts. A timeout after a mutation is an unknown outcome: reconnect and inspect; never replay.

## 2. Prepare the Resolve project

Tested on an early pre-release build (2026-09-28).

1. Inspect the open Resolve project and all timeline names. Identify the source timeline exactly; refuse an ambiguous match. If the intended copy name already exists, inspect it instead of making another.
2. Preserve the open Carvercat document. An empty object list does not prove a clean history (a "blank" comp reported `undo=true`, `said='deleted Rectangle'`).
3. Duplicate with `source_timeline.DuplicateTimeline(name)`, activate the copy, save the Resolve project. Compare source and copy (settings, ranges, track names, enabled states, clip timing/properties, captions) with EACH timeline active during its own read. Leave the copy active.
4. Create a job-owned output folder. Match `comp.format` to the timeline's width, height and fps; set `comp.rename` and `comp.duration`. Store a blank companion until the brief arrives. Do not guess graphics or insert a dummy clip.
5. `edit.save` to an absolute `.carverproj` path. Check the file exists, then `edit.open` it and confirm with list/state.
6. `resolve.refresh`, then read `carvercat_state` for `transfer.connected`, project and timeline. The refresh reply's `said` field can describe the previous action ([KI-003](../known-issues.md#ki-003)). Connection does not prove send/compiler access.
7. Record files, timeline identity, build and open issues in the job report.

A saved blank companion proves setup only. Fusion send, rendering, timing, fonts, alpha, audio and Resolve parity are checked when the edit uses them. Never publish sample projects or put unfinished client work in the template library.

## 3. Read and protect the timeline

- An inactive timeline returns false track flags and missing audio properties. Activate a timeline before reading it, then restore the working one.
- Before any delivery, snapshot every video/audio/subtitle item (name, file reference, source offsets, start/end/duration, enabled state, properties, fades), track names, timeline and project settings. Compare after every placement. Snapshot ALL timelines when the job replaces items, and after save/close/reopen.
- Baseline `sourceIn` is `GetLeftOffset()` (timeline units). `GetSourceStartFrame()` is source-rate and gave false differences.
- The user may change the edit while you work (trimmed cuts, moved overlays, added music/SFX, new tracks, Render in Place clips). Re-read the current timeline before every delivery; never reuse an earlier insertion frame. Keep the original baseline and admit only differences the user explicitly authorised.
- Back up first: export a `.drp` (project) or `.drt` (timeline) before replacing items.
- The overlay target range must be free. Check only the target range (several clips may share one track); a whole-empty-track assertion is too strict.
- API snapshots do not prove every grade or Fusion node.

## 4. Route A: import PNG sequences

1. Validate the sequence on disk first ([export-and-delivery.md](export-and-delivery.md#4-verify-every-output)).
2. Import as one clip: `MediaPool.ImportMedia([{"FilePath": ".../NAME_%05d.png", "StartIndex": 0, "EndIndex": n-1}])`.
3. Check clip FPS: PNG sequences imported at **24 fps** on a 30 fps timeline. Read FPS first; if it is not the timeline rate, `SetClipProperty("FPS", "30")` with a **string**, assert the return value and read it back BEFORE appending. Numeric `30.0` did not apply and stretched 161 frames to 201. Setting FPS that already reads 30 can return False; read-before-write avoids a false stop ([KI-088](../known-issues.md#ki-088)).
4. Check `Alpha mode == Straight`.
5. Append with `AppendToTimeline` using `endFrame = n` (n−1 gave an n−1 frame clip, 433 instead of 434). Then assert `GetStart() == timeline_start + local_start` and `GetDuration() == n`. Endpoint conventions can differ between versions: always assert.
6. Timeline frames = timeline start frame + local frame (one project started at 108000).
7. To replace an earlier version, delete only that exact item without ripple, then append. Never delete unknown items.
8. Use `SetTrackEnable` with readback to hide the reference subtitle track on the working duplicate. Renaming the overlay track (e.g. "Carvercat Captions & Graphics") is fine on the duplicate.

## 5. Route B: native Fusion transfer

Tested on an early 0.1.4 pre-release build with Resolve Studio 21.1.0.14: nine editable Fusion carrier clips individually replaced existing PNG items.

- Deliver API: `deliver.open`, `deliver.panel`, `deliver.set`, `deliver.plan`, `deliver.run`, `deliver.status`, `deliver.cancel`; `deliver.browse {settings:{action:"read"}}` reads the location picker. For Resolve `deliver.set` accepts `picture`, `audio`, `audioTrack` (1 = A1), `audioMode=individual|mixdown`, `trimAudioToRange`; picture and audio default ON. Source media is materialised beside the saved `.carverproj`, so save first.
- Before EACH send, assert: current `scenePointer`; `transfer.scopes[comp].frames` equals the current comp duration (scope can lag `comp.switch`, [KI-081](../known-issues.md#ki-081)); exact source identity and revision; destination project/timeline UUIDs, track and start; picture on, audio off when only graphics are wanted; a ready editable-fusion plan. `deliver.plan` ready=true alone is not proof. Opening Deliver refreshed a stale scope.
- Send once. A refused send (e.g. a stale 207-frame range straddling the next clip) changed nothing in Resolve, but inspect before any further attempt. Prepared manifest entries for refused sends are not placements.
- After each send: snapshot every other track, item ID, property, source offset, fade and every other timeline; verify the carrier graph contains `TextPlus`, animation modifiers and `MediaOut`; confirm "no unsupported objects" in the payload.
- Arabic stagger needs the destination-graph correction in [rtl-and-arabic.md §7](rtl-and-arabic.md#7-fusion-transfer-the-rtl-stagger-workaround). Irregular speech schedules live in Follower tables and must be reapplied after a resend.
- Destination font metrics differ from native: drive final gaps (e.g. a currency symbol gap) from the actual composite. Hidden clips still return native bounds. Compound keyed paths and low-alpha tiles have rendered wrongly ([KI-085](../known-issues.md#ki-085), [KI-086](../known-issues.md#ki-086)).
- Replacing a carrier gives a new item identity; it does not certify a same-item Update or a user-facing workflow (not implemented for people yet, [FR-026](../known-issues.md#fr-026)).
- Render & Send on a pre-release build completed the PNG job but never created the timeline clip ([KI-075](../known-issues.md#ki-075)). The verified fallback is Files export + Route A.

### Scene-by-scene send and "render in place" (verified 0.0.72 + Resolve Studio 21.1, 2026-10-20)

- A film split into sub-comps transfers cleanly one comp at a time: `comp.switch` → `resolve.target {frame:<timeline frame>, track:1}` → `deliver.set {settings:{picture:true, audio:false}}` (once) → `deliver.plan` (ready, range = comp) → `deliver.run`. 22 comps landed back-to-back with no gaps, including comps that nest kit comps (one became a 5,300-tool Fusion clip).
- Heavy sends often reply `answered:false` although the clip arrives. Treat it as unknown: read the track in Resolve (`GetItemListInTrack`) before sending the next one; never resend blindly.
- Audio is cleaner placed with the Resolve API than sent: import the WAVs into bins, then `AppendToTimeline` with `startFrame:0, endFrame:<frames>, recordFrame:<start>, mediaType:2` (endFrame = duration gave exact lengths). Pack SFX into non-overlapping lanes; each sound stays its own clip.
- Resolve's scripting API has **no Render in Place**. Equivalent: render each Fusion clip with its own **single-clip** render job (`SetCurrentRenderMode(1)`, `MarkIn/MarkOut` = the clip, `CustomName`), import the files, place them on V2 at the same frames, `SetTrackEnable('video', 1, False)`. Do **not** use individual-clips mode: every transferred clip shares one carrier media name, so each render overwrote the same file.
- `StopRendering()` can need a second call; `DeleteAllRenderJobs()` fails silently while a job is still rendering.
- To replace one scene: delete its carrier on the caption track, `resolve.refresh`, `resolve.target {frame, track}`, check `carvercat_state transfer` names the right timeline, send, then read the carrier's FPS and set `"24"` if needed ([KI-126](../known-issues.md#ki-126)). Deleting several carriers at once can silently fail ([KI-130](../known-issues.md#ki-130)).

### Other aspect ratios from one edit (verified 2026-10-23)

Making a 1080×1080 version from a 1080×1920 edit (timeline duplicated, resolution changed, mismatch = scale to fit):

- **16:9 video:** set `ZoomX`/`ZoomY` to 1920/1080 (1.778) to fill the square. Clips shot vertically and reframed for 9:16 need a `Tilt` (−250 here) to keep the face in; a negative tilt moved the picture down. Pan values are not pixel-exact: test, measure the still, then interpolate.
- **Fusion-animated stills** (Background + Merge + Transform): set the Background tool to the new size; the existing cover scale still fills, and the motion keys need no change.
- **Nested 9:16 timelines:** zoom the nest item to fill (1.778 for square).
- **Captions:** transferred comps don't reflow ([KI-129](../known-issues.md#ki-129)). Copy the caption project JSON, set every scene's `height` and `timelineHeight`, and remap each placement position in pixels (keep x; y_new = y_old − offset, chosen per element group). Then fix by eye: stacks that hit the logo, cards over faces, blocks touching hair. Send each comp to the new timeline's caption track.
- **QC every scene with a still:** the crop moves subjects relative to captions.

## 6. Still export and composite review

- Reliable loop: pause playback; `SetCurrentTimecode`; wait to settle; assert `GetCurrentTimecode`; `Project.ExportCurrentFrameAsStill(<explicit path containing the frame number>)`; check the call succeeded; assert the timecode again; use unique filenames. Build contact sheets only from those explicit names.
- Settle times that were needed: 0.2 s captured the previous PNG overlay over refreshed video; 0.75 s worked for a plain seek; 1.5 s after replacing sequences; about 4 s after an audit that calls `SetCurrentTimeline` repeatedly (1.1 s failed). The first capture right after switching timelines can fail its timecode assertion; recheck read-only, then capture without redoing placement.
- `Gallery.ExportStills(...)` can return True before every PNG exists (`FileNotFoundError` on the next read), and its generated names produced a non-chronological sheet. If you must use it, clear only the job's temporary `f_*.png`, then poll until the exact expected count exists ([KI-090](../known-issues.md#ki-090)). Color-page stills cost about 1 s each.
- Concurrent playback or the user moving the playhead invalidates captures. Treat contact sheets as design samples, not frame-accurate sync proof. When a composite looks temporally wrong, compare the source PNG for that frame.
- Review composites across each entrance, the complete stack, exits, final caption, the next cut, busy and bright backgrounds, and the final picture frame. Check faces, torsos and hand gestures, not only face boxes.

## 7. Audio, timeline end and trims

- After adding or removing audio, re-read `Timeline.GetEndFrame()` and assert it equals the last intended picture frame. Adding SFX exposed a 43-frame pre-existing music overhang.
- Assert applied gain with `GetProperties()` after `SetProperties()`: requested and stored values differed by 2.3 dB once. Record read-back values.
- Resolve 21.1 has no scripting edge-trim. Verified fallback for one audio clip: `.drp` backup; capture media item, source start, record start, gain and transition; delete only that clip/transition; append the same media with a shorter source out; restore gain and transition (e.g. −16.700012 dB, centred 8-frame `Cross Fade 0 dB`); assert every audio track and the timeline end.
- 24 fps source audio on a 30 fps timeline can round endpoints by one frame.
- Copying audio between timelines: preserve source gain, pan, pitch, speed (e.g. 78%) and fades; record placements in a JSON manifest. Put SFX on dedicated tracks and leave dialogue untouched.
- Structural checks do not replace a full-speed listening review.

## 8. Save, back up and clean up

- Save Resolve with `ProjectManager.SaveProject()` (not a method of the project object). Export a fresh `.drp` after final QA.
- Save the native project too; keep milestones and a file index of editable comps, assets and sequences.
- Unused-render cleanup: audit every track of every timeline in the project, and separate timeline references, media-pool entries and files on disk. Old prefixes are not proof of disuse. Keep editable sources and export snapshots out of scope. A False from `MediaPool.DeleteClips` is not a removal; verify state. If filesystem deletion is blocked by policy, stop and report; do not try another route.
