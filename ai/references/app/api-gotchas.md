Override: [current-artwork-contract.md](current-artwork-contract.md) supersedes historical font availability lists and stale-look claims below. Query the installed editor; legacy observations remain version-specific evidence.

# Current toolkit corrections ? 10 October 2026

Prefer [creative-toolkit.md](creative-toolkit.md). Current inspect/probe does not change selection. Use explicit native IDs, capability keys and bounded batches; copied historical helpers and reports below are version-specific. The current editor endpoint is carvercat-mcp-editor.pid. Refusals stop dependent work. Pixel/font/color conversions are centralized in cc_scene; mixed RTL numbers still need explicit runs and actual preview inspection.

# Carvercat API gotchas (quick lookup)

Verified live, build seen 2026-10-01. Each line = symptom -> cause -> fix. Read this BEFORE scripting a build.

## Setup / connection
- No MCP tools in chat -> use the loopback relay: `ai/scripts/cc_client.py` (reads the port from `%TEMP%\carvercat-mcp-editor.pid` — older builds wrote `carvercat-mcp-window.pid`; it changes on every app restart). See `programmatic-build-relay.md`.
- An open desktop app does not prove that the PID-file relay endpoint is live. If the port refuses a connection, rediscover/restart the relay before mutations; for a save request, report the failed acknowledgement and independently compare the on-disk project path, timestamp, size and hash. Never claim `edit.save` succeeded from file existence alone.
- `carvercat_run` refusals are NOT errors: they return `changed:false, refused:true, why:...`. Always print/check `refused`. `cc_client.run` prints them even when quiet.
- A brand-new comp has VIDEO rows followed by AUDIO rows. Read `carvercat_list.tracks[]`: every row now publishes `index`, stable `id`, visible `label`, and `kind`. Never infer kind from the last row. `object.new` and `mask.make` refuse audio rows, and timeline drags/`clip.move` cannot cross video/audio.
- `object.new` places at the playhead unless the batch step carries `frame` (preferred: it also picks a free row); otherwise `view.seek` first (cc_build.new does). Returns `touched:[id]`. Object ids repeat per comp.
- Occupied row -> `object.new` refused "requested track is occupied": time ranges on one row must not overlap; give overlapping items separate rows.
- After `edit.new` the app has an empty default comp; see multi-section-caption-delivery.md.

## Keys, params, selection
- `key.set` / `key.handle` take `id` (preferred, 0.0.7x). Without `id` they act on the SELECTED object. Wrong selection gives misleading "no such property on this clip" / "not animated on this object". Reselect (`select.clip index=<list index>`) before every key call. List index shifts as objects are added: re-resolve it each time (cc_build.Obj.sel).
- `key.set` `easing` takes Linear / Ease in / Ease out / S-curve / Hold; any other name silently becomes Linear (0.0.72; very old builds ignored it). For exact curves use `key.handle`. Shape curves with `key.handle path frame side x y`: out (0.32,0), in (0.68,1). A handle needs an existing key at that frame.
- Key at frame = comp frame; set the playhead with `view.seek` before `key.set`.
- Param path forms: `tr.e_tr_placement_<id>.{position,scale,opacity}`, `src.e_src_shape_fill_<id>.*`, `src.e_src_shape_stroke_<id>.*`, `src.e_src_shape_geometry_{rectangle,ellipse}_<id>.{width,height,cornerRadius}`, `src.e_src_text_{font,fill,outline,relative}_<id>.*`, `fx.e_fx_trim_<id>.end`. Prefer `param.list` over constructing.
- Beta availability: `param.list` now reports `available` and `unavailable_reason` per Basement row. A listed path is not permission to write: declared-but-unimplemented controls remain visible and faded, and `param.promote`, reset, wiring and `property.set` refuse them without changing the project. Check `available` before automation. Working gradient paint uses the `gradient` object; do not write separate `gradientAngle`/`gradientSize`/related advanced registry fields, which do not drive the native picture. `media.trim.sourceIn` is a working clip field in Controls, not a promotable Basement lane.
- `property.set key=text value="..."` sets the text of the selected text object.
- Units: position y-UP 0..1; shape width/height = fractions of frame WIDTH; `cornerRadius` 0.5 = pill, 0.3 = rounded card; text size 0.088 ~ 62 px cap-height-ish (0.078 ~ 55 px); text tracking units unclear (values 6 and 0.12 garbled tiny text; leave unset).
- Colours are LINEAR light (Rec.709 inverse, see `lin()` in cc_build). RGBA arrays; fill/stroke alpha is the 4th component.
- Fill/stroke `paint` = solid | gradient | none. Gradient: `{"mode":"linear|radial","start":[x,y],"end":[x,y],"stops":[{"p":0,"color":[r,g,b],"a":1},...]}` in the object's box, y DOWN. Text gradient goes in `src.e_src_text_fill_<id>.gradient`.
- Imported media has no cornerRadius: make a rounded rectangle and `mask.make` (verified — see Masks below).

## Text
- Word stagger: `stagger.new` -> `stagger.connect param=text.position` and `param=fill.opacity` -> `stagger.set by=word gap=N order=forward` -> key `text.relative.position` ([0,-0.04]->[0,0]) and `text.fill.opacity` (0->1) with the text selected. gap frames 3..12 (mean spoken interval).
- Fonts that resolve: Poppins Bold/SemiBold, Montserrat ExtraBold, Urbanist Bold, Space Grotesk Bold, Bebas Neue, Anton (Regular), Impact (style Normal). Substituted by Segoe UI (avoid): Sora, Outfit, Manrope, Lexend, Plus Jakarta Sans. Check `carvercat_look` `notes` for "requested X; resolved Y".
- Measure text width: `carvercat_inspect mode=probe object=<id> from=f to=f` -> `objects[0].rows[0][3]` (px, at a frame where it is fully visible). Card width = (w+pad)/1080.
- Turned-comma apostrophe (U+2018, e.g. Uzbek o‘ g‘): fine in Poppins. In Python source on Windows write files as UTF-8 (`Set-Content -Encoding utf8`) or use `\u2018` escapes; a cp1252 console shows it as `?`.

## Effects
- `effect.add cap=shadow|trim|glow|blur|stagger` (applies to the selected object). Trim-path ring/line draw: key `fx.e_fx_trim_<id>.end` 0->1 with ease handles.
- Shadow on captions gives readability without a background card. Do not box normal captions unless the brief says so.

## Preview / look
- `carvercat_look(from,to,count,detail:'thumb',ground:'checker')` returns an inline image; it refuses an UNCHANGED image unless `force:true` and can return a stale image otherwise. `cc_client.look` writes `look.png`; open it with a viewer.
- `carvercat_inspect mode=timing` lists visible objects; `mode=at frame x y` (pixel coords, y down) tells what is under a point.

## Export
- Prefer the permanent Deliver API for new automation: `deliver.open`, `deliver.panel`, `deliver.set`, `deliver.plan`, `deliver.run`, `deliver.status`, and `deliver.cancel`. `deliver.browse {settings:{action:"read"}}` reads the visible location picker. For Resolve, `deliver.set` also accepts `picture`, `audio`, `audioTrack` (1 means A1), `audioMode=individual|mixdown`, and `trimAudioToRange`. Both picture and audio default on. Resolve source media is materialised beside the saved `.carverproj`; an unsaved project must be saved before transfer.
- The legacy-compatible `export.set` takes `{"settings": {...}}` (NOT flat args). One unknown key refuses the whole call and later `export.plan`/`export.run` also refuse until a valid `export.set`. Valid: `format=sequence, sequenceType=png, alpha=true, range=comp, dir=<existing dir>, name=<name>, collision=ask|numbered|replace`.
- `export.run` is asynchronous. It opens Deliver in the visible editor and returns immediately with the durable job path in `why`; poll `export.status` without replaying the export. Status records are version 2 and include `state`/`phase`, `terminal`, `recoverable`, `done`, `total`, current `file`, immutable `source`, and `error`. A queued/running record whose worker disappeared becomes terminal `interrupted`; call `export.resume {job}` to continue from its snapshot.
- Export progress is non-modal: the user can scrub or inspect the timeline while frames render. If the agent makes a document edit, the window returns to Create so the user can watch the change; the immutable export continues and does not absorb later edits.
- For multi-command edits, read `carvercat_state.revision`, pass it back as top-level `expected_revision` on `carvercat_run`, and use `transaction=begin/commit`. A mismatch returns structured `conflict:true` before mutation. Any manual mouse/keyboard takeover rolls back an open, uncommitted agent transaction; committed agent work remains one normal undo step.
- Files land in `<dir>\<name>\<name>_00000.png` (+ hidden `.carvercat-export-source.json` in `<dir>`). One comp of 434 frames wrote quickly (<1 min).
- Verify with PIL: count, size, mode RGBA, `getchannel('A').getbbox()`.
- `edit.save path=<abs .carverproj>` saves; re-save after each comp is finished.

## Resolve delivery (Resolve Studio 21.1)
- `ImportMedia([{FilePath:".../NAME_%05d.png",StartIndex:0,EndIndex:n-1}])` imports one sequence clip; check `FPS` (may default 24; set 30) and `Alpha mode == Straight`.
- Pass FPS as a string: `SetClipProperty("FPS", "30")`, assert its return and read it back BEFORE appending. Once, numeric `30.0` did not apply, stretching 161 frames to 201 at a 30 fps timeline. The helper now fails before placement if FPS is not confirmed.
- `AppendToTimeline` `endFrame=n` gives n frames (n-1 gave n-1). Always assert the placed `GetDuration()` and `GetStart()==base+local_start`. Timelines often start at frame 108000 (01:00:00:00 at 30 fps): frames = start + local.
- `ProjectManager.SaveProject()` (not on the project object) saves the Resolve project.
- After adding or removing audio tracks/items, re-read `Timeline.GetEndFrame()` and assert it equals the intended last picture frame. A pre-existing music clip can extend past picture even when all newly added SFX end earlier.
- Resolve 21.1 exposes timeline-item source/end inspection but no scripting edge-trim method. Verified fallback for an exact final audio clip: make a `.drp` backup; capture media item, source start, record start, gain and transition; delete only that exact clip/transition; append the same media with a shorter source out; restore gain/transition; assert every audio track and final timeline end.
- Assert applied SFX gain from `GetProperties()` after `SetProperties()`. Record read-back values in the report; do not assume requested dB equals stored dB.
- Composite verification: export each frame with `Project.ExportCurrentFrameAsStill(<explicit frame-named path>)` (not Gallery GrabStill, whose names/order are unreliable), then contact-sheet with PIL. Allow the compositor to settle; assert timecode.
- Resolve still export can race the filesystem: `Gallery.ExportStills(...)` may return success before every PNG is stable enough for an immediate contact-sheet read. Clear stale `f_*.png` files in the target folder first, then poll until the exact expected PNG count exists before opening or renaming them. Otherwise sheet generation can hit `FileNotFoundError` or mix a prior grab into the new sheet.
- For ordered multi-frame QC, prefer `Project.ExportCurrentFrameAsStill(<explicit path>)` once per requested frame. Gallery-generated filenames/order produced a chronologically wrong sheet even after timecode settle and exact-count polling. Reliable loop: `SetCurrentTimecode`, wait ~0.75 s, assert `GetCurrentTimecode`, export to a filename containing the requested local frame, then build the sheet from those explicit names.
## Added after revision (2026-09-30)
- object.path points are frame fractions with y DOWN (unlike position, y-up); it takes `track`/`duration`; in a batch give the step `frame` and it lands on a free row. Never relocate with `clip.move` — it is an overwrite edit that trims/deletes clips underneath. Style it with the same shape fill/stroke keys (fill paint none, stroke gradient, width ~0.016) and animate with effect.add cap=trim (fx.e_fx_trim_<id>.end). Arrowheads: a second open 3-point path.
- Impact resolves with style Normal. Impact digit height ~0.54 x size x frame width.
- Reselect before property.set too, after any inspect probe (probe changes selection): 'no such property on this clip' means wrong selection.
- Ellipse tr.scale keys work once the ellipse is selected (earlier refusal was selection). Bar growth: key rectangle height and centre y together (centre = base + h/2/aspect).
- Verify layout numerically: export, then check alpha in a head box per frame (PIL/numpy) and composite over stills; do not trust a checker-ground look alone. Check overlay against the face box, safe area (top ~13%, y_up <= 0.87), and text width (one text about 0.1 size ~ 31 px/char).
- Settle curve (fast start, long soft landing) = key.handle out (0.16,0.95), in (0.30,1); verify with key.list (handles column). Shadow defaults (x .012, y -.012, opacity .5) read far away: tight look = x .005, y -.005, softness .008, opacity .38 via property.set fx.e_fx_shadow_<id>.<x|y|softness|opacity>. key.list needs key= (not path=) and the object selected.
- Group layout: measure text width (probe), then centre icon+gap+text as one unit instead of fixed x.

## Masks / rounded image cards
- `mask.make`: select the IMAGE first (`select.clip`), then `select.add` the SHAPE; the last-selected (active) object becomes the mask over the others. Result: image cropped to the shape (verified by pixel bbox).
- The mask shape MUST be on a video row. Current builds enforce this: `object.new` on an audio row and `mask.make` involving an audio-row object refuse before mutation. Read `carvercat_list.tracks[].kind`, add a video track if needed, and retry deliberately.
- Masked shape hides itself and is parented to the image (`parent.clear` to unlink). Wrong order (shape first) masks the wrong way and renders blank.
- `look` PNG shown by `view` can lag one call behind; verify numerically (PIL bbox on a `ground:'black'` look) instead of trusting the viewer.
- `media.import` auto-places clips on rows 0..N-1; delete/move them before building. `clip.enable on=False` on a clip is not needed; `edit.delete` shifts indices, so re-list between deletes.
- Masked image cards: set the image's cover-fit scale BEFORE `mask.make`; the shape keeps its authored world size then scales in proportion with the image, and moves with it (parent link), so animate only the image (opacity/scale/position) and the mask follows. Do NOT pre-inflate the shape. Add a separate no-fill gradient-stroke rectangle for the frame and animate it with the same keys.
- Stacking: a HIGHER row number draws ON TOP. Put pills/labels on rows above the card rows (add tracks with `track.add` first).
- `resolve_tools.import_place` now only requires the target range on the track to be free, so several clips can share V2.

## Arabic outlined captions and raster sizing
- After a stagger connection, fill opacity may appear only as a slot proxy in `param.list`. Read `stagger.list` and use the slot's underlying `key`; do not construct an ID or assume its cap remains separately listed.
- Outlined word reveals need `stroke.opacity` connected and animated alongside `fill.opacity`. Otherwise an outline may expose a word before the fill.
- Measure an imported media object's scale-1 probe width. For a desired visible width, divide by that width multiplied by the asset's alpha-bbox-width/file-width ratio. File dimensions alone gave undersized flags in this session.
- `stagger.list` returns `stagger: null` for text without a card. Treat that as an absent card, not an empty dictionary.

## Export visual QA — observed 2026-10-01
- On a pre-release build, alpha sequence/still exports intermittently produced glyph triangles and stray lines despite terminal complete and correct PNG dimensions. Pausing transport did not resolve it; no verified workaround. Do not accept a job from count/alpha checks alone: compare temporal disk frames to native look and inspect glyph geometry.

- Follow-up: patched executable with a patched pre-release base passed a 1030-frame export and sampled Resolve composite review. Prior failure is historical for the clean build. Still validate actual outputs. After any session reset/refusal, stop dependent scripts and verify project identity before save; durable job completion alone does not prove the currently open document is the intended project.


## Revision delivery and cleanup
- While polling an acknowledged export, a live durable JSON read can transiently raise PermissionError or expose partial JSON on Windows. Retry the read within a bounded deadline; do not replay deliver.run to solve a read failure.
- Resolve may return false from setting FPS to30 when the imported item already reports30. Read the value first, set only if needed, then verify readback before changing timeline clips.
- For a flag accompanying native word stagger, align its reveal with the associated word's delayed start, not automatically the caption clip's first frame. Probe visible bounds to place icon+gap+text as one group. Preserve curved entries/exits.
- A requested unused-render cleanup requires checking all timelines in the target project, not only the active timeline. Distinguish timeline references, media-pool entries, and files on disk. Older prefixes are not sufficient evidence of disuse. Keep editable sources and source snapshots outside sequence deletion scope.
- A false MediaPool.DeleteClips result does not confirm removal. Verify state before claiming success. A filesystem cleanup being policy-blocked is not an API limitation.

## Project Navigator
- Read carvercat_state.navigator node targets and pass the whole target to workspace.navigator open. Shared definition opens the comp; an exact usage restores parent/group path and selects that clip. Clip IDs alone are ambiguous across comps. Map is pan-only; workspace preferences never belong in the project. See project-navigator.md.

## Extending an authored text highlight (2026-10-10)

- Extending `clip.trim` and the placement-opacity envelope does not extend an independent `text.relative.opacity` exit. Inspect every effective opacity/reveal channel; an old relative-text key can keep the longer clip invisible. Clear or retime only the obsolete channel through its discovered `param.list` path, then verify a rendered pixel sample beyond the original endpoint.
- A longer hold can overlap the next spoken caption in time. Preserve the voice/caption cue and place the highlight in a measured separate zone; use an all-visible-span overlap check and actual Resolve composites across any new footage cut.
- Move all icon paths, container and label when mirroring an accumulating card group. Arabic text direction alone does not make the card's column order right-first.
- Original JSON metadata such as `textProps.fontResolved` is not authoritative font evidence. Use current native probe/look font notes and actual exported glyphs; compare canonical font properties separately from a legacy cache string.

## Arabic Fusion Follower direction and transfer scope — 12 October 2026

- Clean88e8fd3 / ResolveStudio21.1.0.14: nativeArabicwordstagger transfers with left-first reveal. Glyph shaping/string is correct. A temporary destination-graph correction mirrors the character-index delay table Dnew(i)=Dold(N-1-i), retains measured manualOrder6 and the keyed opacity/offset curves, then checks real entry frames. Flat delays and Latin/numeric strings need no inversion. Re-send recreates the defect until compiler mapping is fixed. Do not treat this as generic mixed-bidi/ligature certification.
- After comp.switch, check that transfer.scopes[comp].frames equals the new comp duration before any write; this build can retain the old cached span. Ready deliver.plan alone was insufficient. A refused straddler send changes no timeline item, but inspect before another attempt.
- Fusion modifier names may be normalized on import; discover the curve through DelayByCharacterPosition.GetConnectedOutput().GetTool(). SetKeyFrames can return None on a successful write; read back exact key positions/values.

## Actual Fusion review and audit/capture sequencing

- A native geometry measurement may return bounds for a hidden clip. Verify its enabled/hidden state and actual composite before diagnosing missing text as a font/compiler problem.
- Native/Fusion glyph widths can differ even with the intended resolved family. Final symbol gaps and card padding need actual destination review.
- A keyed compound currency path rendered only one contour in the measured transfer; six simple positive filled native paths worked. Low-alpha icon tiles appeared opaque in the actual Fusion result; removing the tiles exposed the line drawings. These are bounded observations needing isolated reproduction, not general fixes or proven causes.
- An all-timeline protection audit calls SetCurrentTimeline repeatedly. Let the final target selection settle before setting the capture timecode, then verify exact timecode before and after export. Immediate1.1-second capture assertions failed in one run; a4-second settle after the audit passed. Playback/navigation can invalidate the observation; a successful setter alone is not a capture proof.
- Native look takes from/to, not frame. An unsupported argument is a known refusal; correct the observation only, without repeating completed authoring or transfer.
- Manual aliases made from object IDs are not a substitute for validated name mappings in name-based rebind/fit. Preserve binding identity and use measured placement for the intended stable objects.
- Fusion SaveSettings needed OrderedDict in Python __main__ in this session. SetKeyFrames can return None on success; validate the exact stored key/value table instead of treating that return as failure.

See [known-issues](../known-issues.md) for pending RTL/scope and placement items.
