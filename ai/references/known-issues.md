# Known issues

Read this when a Carvercat command, export or Resolve handoff behaves unexpectedly, before you report a "new" bug, and when you plan a job on an older build.
Every product bug, refusal, surprise and limitation found in field work, deduplicated and grouped by area. Feature requests are listed separately at the end.

Format: **ID: title.** Symptom. *Seen:* first build/date stated. *Workaround.* *Status:* `open`, `fixed in X`, or `unknown` (only what the evidence says). IDs are stable; never renumber, add new ones at the end of their area block.
Builds are Carvercat unless marked Resolve. "Exact-release 2026-10-01" = a pre-release build (export/lane/revision work). Workflows: [workflows/](workflows/job-playbook.md). Command basics: [mcp-essentials.md](app/mcp-essentials.md), [api-gotchas.md](app/api-gotchas.md).

## Contents
1. [MCP and agent API](#1-mcp-and-agent-api) (KI-001–KI-027, KI-117–KI-121 JSON authoring, KI-122–KI-125 session/fonts/batches)
2. [Timeline and clips](#2-timeline-and-clips) (KI-030–KI-037)
3. [Text and stagger](#3-text-and-stagger) (KI-040–KI-051)
4. [Effects](#4-effects) (KI-055–KI-059)
5. [Shapes and paths](#5-shapes-and-paths) (KI-060–KI-062, KI-108–KI-116 rigging, instances, maps)
6. [Audio](#6-audio) (KI-065–KI-068)
7. [Export](#7-export) (KI-070–KI-077)
8. [Resolve transfer and scripting](#8-resolve-transfer-and-scripting) (KI-080–KI-096, KI-126–KI-131)
9. [Performance](#9-performance) (KI-100–KI-102)
10. [UI](#10-ui) (KI-105–KI-107)
11. [Feature requests only](#11-feature-requests-only) (FR-001–FR-033)

## 1. MCP and agent API

**<a id="ki-001"></a>KI-001: Carvercat tools missing from the chat.** MCP enabled in the app, but no Carvercat tools in the session; the client config pointed at an older agent executable (an older pre-release build) while an early pre-release build was running. Cause not proven. *Seen:* an early pre-release build, 2026-09-28. *Workaround:* use the loopback relay through the published endpoint file ([workflows/resolve-handoff.md §1](workflows/resolve-handoff.md#1-connect-to-the-right-editor)); do not change global client config without authorisation. *Status:* unknown.

**<a id="ki-002"></a>KI-002: Key and property calls act on the selection, with misleading errors.** `key.set` returned "no such property on this clip" and `key.handle` "not animated on this object" when another object was selected; `inspect probe` changed the selection; an ellipse "scale" refusal was the same cause. *Seen:* 2026-09-30 (a pre-release build era). *Workaround:* use explicit IDs (batch steps, `cc_scene`); on old builds reselect before every key/property call. *Status:* probe no longer changes selection (toolkit notes, 2026-10-10); selection-bound legacy commands unknown.

**<a id="ki-003"></a>KI-003: `resolve.refresh` reply shows a stale `said`.** `answered=true` but `said` described the previous action. *Seen:* an early pre-release build. *Workaround:* read `carvercat_state` for `transfer.connected`, project and timeline. *Status:* unknown.

**<a id="ki-004"></a>KI-004: Relay endpoint stale or refusing.** The app stayed open but the advertised loopback port refused the final `edit.save`; another time the old PID/port file pointed at an absent install; a port rediscovered from the PID file gave `ConnectionRefusedError`. *Seen:* 2026-09-30, 2026-10-09/10 (0.1.4). *Workaround:* rediscover the current endpoint (`carvercat-mcp-editor.pid` on current builds), verify PID and handshake; never claim a save from file existence; compare path, mtime, size and hash. *Status:* open (see FR-020).

**<a id="ki-005"></a>KI-005: No save path or dirty flag in live state.** Persistence could only be proven by file existence plus save/reopen. *Seen:* an early pre-release build. *Workaround:* `edit.open` the saved file and read list/state. *Status:* unknown (current contract says to verify the document path through state; check your build).

**<a id="ki-006"></a>KI-006: `key.set` easing ignored.** `easing` accepted and ignored, even a bogus value. *Seen:* 2026-09-30. *Workaround:* set curves with `key.handle` on each key pair (out (0.32,0), in (0.68,1)). *Status:* differs by build: on 0.0.69–0.0.72 named easings (`Linear`, `Ease in`, `Ease out`, `S-curve`, `Hold`) work and other names silently become Linear ([mcp-essentials.md](app/mcp-essentials.md)).

**<a id="ki-007"></a>KI-007: `key.handle` rejects the cap alias path.** `transform.placement.position` worked for `key.set`/`key.list` but not `key.handle`. *Seen:* an early pre-release build. *Workaround:* use the exact stored path from `param.list`. *Status:* unknown.

**<a id="ki-008"></a>KI-008: Shape paint selectors absent from `param.list`.** Selectors are accepted but not listed; a builder that expected every writable selector in the list stopped. *Seen:* a pre-release build (0.1.4), 2026-10-09. *Workaround:* use the canonical declared capability key; the native command still validates it. *Status:* unknown (documented as expected in [creative-controls.md](app/creative-controls.md)).

**<a id="ki-009"></a>KI-009: Declared controls that are not live.** (a) Unsupported Basement parameters are listed but `available:false` with `unavailable_reason`; promote/reset/link/`property.set` refuse without change. Advanced gradient fields (`gradientAngle`, `gradientSize`…) do not drive the picture; the `gradient` paint object does. (b) Repeatable Stroke `opacity` is in the declaration snapshot but `param.promote` refused it, rolling back a 104-step plan. (c) Text gradient `gradientStart`/`gradientEnd` are not live, so text gradients stay static. *Seen:* (a) 2026-10-01; (b)(c) a 0.1.4 pre-release build, 2026-10-10. *Workaround:* check `available` before writing; for stroke alpha use `fx_set(alias, "opacity", …)` or RGBA via `fx_color`; keep text gradients static, animate shape-gradient endpoints. `native-controls.json` is discovery data, not a live availability list. *Status:* (a) by contract; (b) explained later (opacity is absorbed into Colour and is directly settable); (c) open.

**<a id="ki-010"></a>KI-010: Harmless no-ops reported as refusals.** `refused:true`/isError for: `stagger.set` with current values (`why=unchanged: already set to that`), `stagger.list` with valid readings, `comp.rename` unchanged, `key.handle` already set, `track.remove_empty` ("no empty tracks to remove"), and a same-place `clip.move` (aborts the whole batch). *Seen:* an early pre-release build 2026-09-28; still on a 0.1.4 pre-release build 2026-10-10. *Workaround:* read state and write only differing fields; tolerate only exact identified wording. *Status:* `clip.move` no-op fixed in 0.0.71; others open (FR-023).

**<a id="ki-011"></a>KI-011: Transient handle refusal after moving keys.** Moving a clip start 66→78 with keys at 78/85, a handle call refused `no keyframe at 7 on src.e_src_text_relative_clip_3.position`; the transaction rolled back. Isolated retries worked. *Seen:* a pre-release build, 2026-10-01. *Workaround:* confirm rollback and baseline, then rerun the full mutation once. *Status:* unknown (not reproduced).

**<a id="ki-012"></a>KI-012: Session reset leaves a blank Comp 1 open.** After a relaunch or a concurrent session change, the relay connected to a blank Comp 1 (zero clips); a `comp.switch` refusal followed, and a script that continued saved the blank document over the project. *Seen:* a pre-release build, 2026-10-01. *Workaround:* before export loops and saves, assert project identity (path, comps, revision), not only comp count; stop chains on failure. Recover from an export job's immutable source snapshot via `edit.open`. *Status:* unknown.

**<a id="ki-013"></a>KI-013: `edit.save` "Access is denied (os error 5)".** Saving to a writable job folder and to Documents failed; Temp worked. After an app restart direct saves worked. *Seen:* a pre-release build, 2026-09-30. *Workaround:* restart and retry; never leave the only copy in Temp. *Status:* unknown (unexplained).

**<a id="ki-014"></a>KI-014: Old Python helper hid envelope fields and refusals.** `cc_client.run(cmd, **args)` put `expected_revision`/`transaction` inside command args, printed refusals and returned them; `cc_build` kept going after a refused mutation. *Seen:* 2026-10-01. *Workaround:* current `Client.run` raises on refusals and `Client.batch` checks revision/document. *Status:* fixed in the current `Client` (creative-toolkit).

**<a id="ki-015"></a>KI-015: Installed app older than the published contract.** The running executable (a pre-release build) had no `revision`, list v1 string labels, and no top-level `expected_revision`, while source/schema did. *Seen:* 2026-10-01. *Workaround:* check live state for these fields before relying on them. *Status:* fixed in a pre-release build (fields exposed live).

**<a id="ki-016"></a>KI-016: `carvercat_look` stale or refused images.** Unchanged image refused unless `force:true`; `count:1` gave a stale image; the viewed `look.png` lagged one call. *Seen:* 2026-09-30. *Workaround:* numeric checks (PIL bbox on a black-ground look). *Status:* fixed in the current contract: dedup follows rendered bytes and `Client.look` returns an empty file list for unchanged images ([current-artwork-contract.md](app/current-artwork-contract.md)).

**<a id="ki-017"></a>KI-017: Non-ASCII output breaks Windows consoles.** Arabic and U+2018 printed as `?` or raised `UnicodeEncodeError` under cp1252. *Seen:* 2026-09-28/30. *Workaround:* `python -X utf8`, UTF-8 JSON, JSON escaping. *Status:* open (tooling; FR-030).

**<a id="ki-018"></a>KI-018: `select.clip` uses a shifting list index.** The index changes as objects are added or deleted. *Seen:* 2026-09-30. *Workaround:* re-resolve before each selection, or use explicit IDs. *Status:* unknown.

**<a id="ki-019"></a>KI-019: Scene aliases made from IDs break name-based rebind/fit.** *Seen:* an early 0.1.4 pre-release build. *Workaround:* keep validated name mappings; use measured placement for stable objects. *Status:* unknown.

**<a id="ki-020"></a>KI-020: `edit.new` adds an empty default comp.** `comp.new` then appends, so four new comps make five. *Seen:* a pre-release build. *Workaround:* reuse or verify-and-delete the default; assert comp identity before export. *Status:* unknown.

**<a id="ki-021"></a>KI-021: A "blank" comp can carry undo history.** No objects, but `undo=true`, `said='deleted Rectangle'`. *Seen:* an early pre-release build. *Workaround:* do not force-new or discard; configure and save it. *Status:* unknown.

**<a id="ki-022"></a>KI-022: Derived `fontResolved` cache changes on save.** Shape objects gained `Open Sans` in unused `textProps.fontResolved`; a legacy text cache string changed on save. *Seen:* an early pre-release build; 0.1.4 (2026-10-10). *Workaround:* exclude derived fields from comparisons; never hand-edit JSON to remove them. *Status:* unknown.

**<a id="ki-023"></a>KI-023: Project-JSON edits: force-reopen and cloned clips.** `edit.open {force:true}` discards unsaved app work; a clip cloned in JSON shows keys but does not animate. *Seen:* 0.0.69. *Workaround:* retime/restyle only MCP-created clips in JSON; keep the person's hands off during the loop. *Status:* unknown.

**<a id="ki-024"></a>KI-024: Group editing scope.** `key.set` on a child refuses ("outside the current editing scope") until `object.enter`; `object.new` refuses inside an entered group; `object.enter/exit` are not batchable. *Seen:* 0.0.69. *Workaround:* enter/exit around child keys; create at top level, then move into the group. *Status:* unknown.

**<a id="ki-025"></a>KI-025: Hidden clips still return measured bounds.** *Seen:* an early 0.1.4 pre-release build. *Workaround:* check enabled/hidden state and the actual composite before diagnosing missing text. *Status:* unknown.

**<a id="ki-026"></a>KI-026: No "remove all keys"; `key.remove` acts at the playhead and takes only `key`.** *Seen:* 0.0.69. *Workaround:* `Scene.replace_keys`, or `edit.undo`. *Status:* unknown.

**<a id="ki-027"></a>KI-027: `carvercat_authoring mode=controls query=` matches parameter names only** (e.g. `size`, `shadow`), not capability names; `carvercat_look` takes `from`/`to`, not `frame` (unsupported argument refuses). *Seen:* 0.0.69; an early pre-release build. *Workaround:* query by parameter name; use `from`/`to`. *Status:* unknown.

**<a id="ki-117"></a>KI-117: Positive text tracking written into project JSON rendered scrambled.** A tracked "POSITION" label drew as reversed, spaced glyphs. *Seen:* 0.0.72, 2026-10-20. *Workaround:* omit tracking on JSON-authored text. *Status:* open.

**<a id="ki-118"></a>KI-118: Large films overflow MCP batches.** Receipts and payloads for 1,000+ objects exceed transport limits and take hours. *Seen:* 0.0.72. *Workaround:* generate the comps into the `.carverproj` and reopen with `edit.open {force:true}` ([app/json-authoring.md](app/json-authoring.md)). *Status:* open (no documented import format).

**<a id="ki-119"></a>KI-119: Nested-comp instances ignore their parent's transform.** A camera null moved ordinary objects but not nested instances. *Seen:* 0.0.72. *Workaround:* bake the camera into the instance's own keys (in source time: local + `sourceIn`). *Status:* open.

**<a id="ki-120"></a>KI-120: `parent.assign` uses the first selected object as the parent**, not the last. *Seen:* 0.0.72. *Workaround:* select the parent first, or set `parentId` in JSON. *Status:* behaviour.

**<a id="ki-121"></a>KI-121: `cornerRadius` caps at 0.5 (of half the short side)**, so a true pill can't be a rectangle. *Seen:* 0.0.72. *Workaround:* 2-point path with a round-capped stroke. *Status:* behaviour.

**<a id="ki-122"></a>KI-122: Unsaved MCP work is lost when the connection drops or the app restarts.** Two scenes of batch edits vanished after an MCP "connection closed"; the app reopened with no document and the file on disk was the last `edit.save`. *Seen:* 0.0.82, 2026-10-22. *Workaround:* `edit.save` after every scene; prefer direct JSON editing ([app/json-authoring.md](app/json-authoring.md)). *Status:* open (no autosave/recovery).

**<a id="ki-123"></a>KI-123: Fonts installed per-user are missed when the app is started outside the MCP.** Almarai (HKCU-registered) resolved silently to Segoe UI after an external restart; every text measured and drew with the wrong face. Relaunching through `carvercat_session {allow_launch:true}` loaded it. *Seen:* 0.0.82, 2026-10-22. *Workaround:* check `carvercat_authoring fonts` after every app start; relaunch via the MCP. *Status:* open (see FR-022). *Update 2026-10-23:* it recurred in an instance that **was** launched through the MCP (Arabic previews and `observe` widths fell back to Segoe UI mid-session); only a close-and-relaunch fixed it. Check `fonts` before every measuring step, not only at start. Resolve itself rendered Almarai correctly in the transferred comps throughout.

**<a id="ki-124"></a>KI-124: `carvercat_batch` `observe` is capped at 16 entries and the cap is undocumented.** A batch with 20 observations was refused as a whole ("at most 16 observations"). *Seen:* 0.0.82. *Workaround:* 16 per batch; read the rest with `carvercat_authoring mode=geometry`. *Status:* behaviour (undocumented).

**<a id="ki-125"></a>KI-125: Batch receipts are very large.** A 200-step batch returned about 60 KB (one receipt per step, full geometry per observation), overflowing tool output. *Seen:* 0.0.82. *Workaround:* fewer, larger JSON edits instead of batches. *Status:* open (FR-032).

## 2. Timeline and clips

**<a id="ki-030"></a>KI-030: Visual objects and masks on the audio row were silently invisible.** `object.new track=<audio row>` succeeded but never rendered; `mask.make` with the mask on the audio row reported "masking 1 track" but did not mask. *Seen:* 2026-09-30. *Workaround:* read `carvercat_list.tracks[].kind`. *Status:* fixed in exact-release 2026-10-01 (creation and masks refuse audio rows; list v2 publishes `{index,id,label,kind}`).

**<a id="ki-031"></a>KI-031: Dragged audio clip appeared on a video lane.** *Seen:* user report, 2026-09-30. *Status:* fixed in exact-release 2026-10-01 (drags clamp to the original track kind).

**<a id="ki-032"></a>KI-032: `clip.move` is an overwrite edit.** A short object created at frame 0 took a temporarily free track; moving it into an occupied range trimmed another card to 3 frames and deleted an accent, with no warning. *Seen:* an early pre-release build. *Workaround:* create with full spans or with the batch step's `frame` so a free track is chosen; give overlapping items separate rows; verify durations after placement. *Status:* open (FR-018).

**<a id="ki-033"></a>KI-033: Creation lands at the live playhead.** `object.new`, `media.import` and adjustment layers placed at wherever the user last scrubbed (six text clips landed at 160 of 169; music at 61). *Seen:* 0.0.69. *Workaround:* give each batch step a `frame`; give `media.import` a `frame`; verify `left`. *Status:* fixed in 0.0.71 for batch steps with `frame`.

**<a id="ki-034"></a>KI-034: `object.path` defaulted to a free row and 90 frames.** Needed trim and move; overlapping path sets reused rows and produced shortened 10-frame objects with out-of-clip keys and lint errors. *Seen:* 2026-09-30. *Workaround:* distinct rows for simultaneous paths. *Status:* fixed in current contract (2026-10-15: `Scene.path` takes duration and exact track, validates room; no temporary 90-frame clip).

**<a id="ki-035"></a>KI-035: `media.import` auto-places clips.** Images fill rows 0..N−1; stills default to 90 frames; each audio file gets its own new audio track. *Seen:* 2026-09-28/30; 0.0.69. *Workaround:* import as a deliberate step, then set duration (e.g. 231) and move/delete explicitly; re-list between deletes. *Status:* open (FR-011).

**<a id="ki-036"></a>KI-036: `clip.move` cannot cross video/audio.** *Status:* by design since exact-release 2026-10-01.

**<a id="ki-037"></a>KI-037: Comp-local IDs repeat.** Every new comp restarts at `clip_1`. *Workaround:* assert the comp before targeting IDs; navigator targets pass the whole target. *Status:* unknown (behaviour).

## 3. Text and stagger

**<a id="ki-040"></a>KI-040: Mixed RTL text reverses numbers.** `40 شهر` rendered digits as `04`; numeric-only `10%` with rtl rendered `%01`. *Seen:* an early pre-release build 2026-09-28; a pre-release build 2026-10-09. *Workaround:* separate LTR number objects ([workflows/rtl-and-arabic.md §3](workflows/rtl-and-arabic.md#3-numbers-and-latin-inside-arabic)). *Status:* open.

**<a id="ki-041"></a>KI-041: Native stagger has only a uniform gap.** Irregular word onsets cannot be stored in the native source. *Seen:* an early 0.1.4 pre-release build. *Workaround:* Fusion Follower delay tables, reapplied after each resend. *Status:* open (FR-021).

**<a id="ki-042"></a>KI-042: Fonts installed after launch are not found.** `property.set` accepted Alan Sans but the probe showed Segoe UI until save, quit and relaunch. *Seen:* an early pre-release build; a pre-release build. *Workaround:* restart, reopen, re-probe. *Status:* open (FR-022).

**<a id="ki-043"></a>KI-043: Silent font substitution.** Sora, Outfit, Manrope, Lexend, Plus Jakarta Sans fell back to Segoe UI; only `look` notes said so; lint did not flag it. *Seen:* 2026-09-30. *Workaround:* `mode=fonts` queries, `require_font=True`, validate `font_exact`. *Status:* checks available in current builds; the old resolving-font list is not proof on another machine.

**<a id="ki-044"></a>KI-044: Font names and styles differ from what you expect.** Impact's style is Normal ("Regular" reports substitution); a packaged font's internal family differed from the installed live family (Bricolage Grotesque / ExtraBold was the working request). *Seen:* an early pre-release build; a 0.1.4 pre-release build. *Workaround:* discover names from the running app. *Status:* unknown.

**<a id="ki-045"></a>KI-045: Tracking garbles small text.** Size 0.036 with tracking 6 or 0.12 rendered mirrored letters ("TNEMGES"); tracking units undocumented. *Seen:* 2026-09-30. *Workaround:* leave tracking unset; Poppins SemiBold 0.04 worked. (Tracking 1 → 0.94 on larger price text was fine later.) *Status:* unknown.

**<a id="ki-046"></a>KI-046: Stagger-connected fill opacity only appears as a slot proxy.** `param.list` lacked `text.fill.opacity` after connection; `stagger.list` returns `stagger: null` for text without a card. *Seen:* a pre-release build. *Workaround:* use the slot's underlying `key`; treat null as no card. *Status:* unknown.

**<a id="ki-047"></a>KI-047: Outline needs paint on.** Default outline colour/thickness exist while `text.outline.paint` is off; setting thickness alone shows nothing. *Seen:* a pre-release build. *Workaround:* set `paint='solid'`, colour and thickness. *Status:* unknown (behaviour).

**<a id="ki-048"></a>KI-048: Outlined stagger reveals the stroke early.** *Seen:* a pre-release build. *Workaround:* connect and animate `stroke.opacity` with `fill.opacity`. *Status:* unknown (behaviour).

**<a id="ki-049"></a>KI-049: Extending a clip does not extend a relative-opacity exit.** After extending a 10% highlight from 20 to 44 frames, `text.relative.opacity` kept its old flicker/exit keys and hid the number at the old end. *Seen:* 0.1.4 (a pre-release build), 2026-10-10. *Workaround:* clear/retime the obsolete channel (`extend_hold` does this deliberately); check pixels past the old end. *Status:* authoring dependency, not a reproduced bug.

**<a id="ki-050"></a>KI-050: Stagger timing quirks.** The stagger replays the whole key timeline per part, so the last part ends `gap × (parts−1)` late and can overrun the comp; a text takes one staggered preset per property (a staggered exit on an entrance-staggered property is refused). *Seen:* 0.0.69–0.0.72. *Workaround:* gate with clip opacity; whole-block exits. *Status:* unknown.

**<a id="ki-051"></a>KI-051: `text.content` is not keyframeable.** No type-on counters. *Workaround:* cut text clips back to back. *Status:* unknown.

## 4. Effects

**<a id="ki-055"></a>KI-055: New Gaussian blur starts at size 10.** Text or groups render soft. *Seen:* 0.0.69. *Workaround:* key it or set 0. *Status:* unknown.

**<a id="ki-056"></a>KI-056: Glow `blend` > 0 hazes the layer even at `amount` 0.** Glow 1.2 on a small dot blew out to yellow. *Seen:* 0.0.69. *Workaround:* blend 0 except during pulses; 0.35 at size 14 stays orange. *Status:* changed by 0.0.72 — there blend 0 makes the glow invisible and amount drives burn; use the calibrated table in [effects/glow.md](effects/glow.md) (amount ≤ 0.8, blend 0.2 default).

**<a id="ki-057"></a>KI-057: Rectangle `angle` does not rotate.** *Workaround:* transform `rotation`. *Status:* unknown.

**<a id="ki-058"></a>KI-058: Shape fill `softEdge` softens permanently.** *Workaround:* use `motionblur` for fast wipes and stretches. *Status:* unknown.

**<a id="ki-059"></a>KI-059: Native pen default stroke covers the fill.** Blue marks were the default stroke over the intended fill. *Seen:* a 0.1.4 pre-release build. *Workaround:* `stroke:none` explicitly. *Status:* fixed in helper policy (closed filled paths now disable the default stroke in `cc_scene`); native default unchanged.

## 5. Shapes and paths

**<a id="ki-060"></a>KI-060: Stored path placement is not the rendered geometry centre.** Translating baked custom paths by the stored default centre collapsed a cluster; a trim line landed over a CTA. *Seen:* a 0.1.4 pre-release build. *Workaround:* measure actual bounds or use canonical point geometry. *Status:* open (FR-024).

**<a id="ki-061"></a>KI-061: Upscaling small paths with transform scale renders soft** (8–10×). *Workaround:* rebuild the path at size (scale points and handles), keep scale ≈1. *Status:* unknown.

**<a id="ki-062"></a>KI-062: Multi-part traced paths render from `shape.params.contours[].points`**, not `shape.params.points`; converting only one distorts the logo. *Seen:* 0.0.69. *Status:* unknown (behaviour).

**<a id="ki-108"></a>KI-108: Child drifts when the parent has an off-centre anchor and rotates.** *Seen:* 0.0.72. *Workaround:* parent to a pivot null at the joint ([drawing/rigging.md](drawing/rigging.md)). *Status:* open.

**<a id="ki-109"></a>KI-109: On comp instances the anchor does not compensate position, and short keys (`anchor`, `scale`, `blend`) are refused.** *Seen:* 0.0.72. *Workaround:* use `tr.e_tr_placement_<id>.*` and the camera maths in [maps/maps.md](maps/maps.md) §3b. *Status:* open.

**<a id="ki-110"></a>KI-110: `link.new` (ropes) only within one object.** Cross-object links refuse. *Seen:* 0.0.72. *Status:* open ([effects/basement-promote-ropes.md](effects/basement-promote-ropes.md)).

**<a id="ki-111"></a>KI-111: Gradient offset/angle/size/type are unavailable ("renderer does not read").** *Workaround:* key gradient start/end. *Seen:* 0.0.72. *Status:* open.

**<a id="ki-112"></a>KI-112: `text.font.size` minimum is 0.01 W; a smaller value refuses (and rolls back the whole batch).** *Seen:* 0.0.72.

**<a id="ki-113"></a>KI-113: `preset.apply` takes one `id` (ignores `ids`); `preset.apply`, `param.raise`, `template.apply`, `comp.new`, `key.box`, `object.enter/exit` are not batchable.** *Seen:* 0.0.72. *Workaround:* `carvercat_run` per object.

**<a id="ki-114"></a>KI-114: No arrow primitive; `authoring.arrow` does not exist as a command.** *Workaround:* shaft path + 3-point chevron path (`scripts/maps/map_overlay.py`). *Seen:* 0.0.72.

**<a id="ki-115"></a>KI-115: Misleading receipts** — `object.new` "unchanged: it is already that length" on creation; empty `why` on many `preset.apply`; `undo_steps` 0 after `track.add`; `validate` false failures on template instances. *Seen:* 0.0.72. *Workaround:* trust `touched`/aliases and a look.

**<a id="ki-116"></a>KI-116: `look` region/object crops misdraw backgrounds; `max_edge` ignored inside `looks[]`.** *Workaround:* full-frame looks. *Seen:* 0.0.72.

## 6. Audio

**<a id="ki-065"></a>KI-065: No per-clip gain.** *Seen:* 0.0.69/0.0.70. *Workaround:* bake gain into WAVs. *Status:* fixed in 0.0.71 (`media.audio.gain`).

**<a id="ki-066"></a>KI-066: Resolve stored a different gain than requested** (2.3 dB apart). *Seen:* Resolve 21.1. *Workaround:* read back with `GetProperties()` and record it. *Status:* unknown.

**<a id="ki-067"></a>KI-067: 24 fps source audio on a 30 fps timeline rounds endpoints by one frame;** music ended one frame before video. *Status:* unknown.

**<a id="ki-068"></a>KI-068: Adding SFX exposed a pre-existing music overhang** (43 frames past picture). *Workaround:* assert timeline end after audio changes; trim fallback in [workflows/resolve-handoff.md §7](workflows/resolve-handoff.md#7-audio-timeline-end-and-trims). *Status:* unknown.

## 7. Export

**<a id="ki-070"></a>KI-070: `carvercat_render` output was opaque.** RGBA with alpha 255 everywhere, black ground. *Seen:* an early pre-release build. *Workaround:* native `export.set` with `alpha:true`. *Status:* unknown.

**<a id="ki-071"></a>KI-071: `export.set` refuses everything for one unknown key.** Message "needs a `settings` object"; `export.plan`/`export.run` then refuse; flat args not accepted. *Seen:* 2026-09-30 (`collision` was unknown then; it is valid now). *Workaround:* pass only known keys inside `settings`. *Status:* open (error should name the key).

**<a id="ki-072"></a>KI-072: Blocking `export.run` outlived client timeouts** (45 s helper, 120 s relay window) while still rendering. *Seen:* an early pre-release build to 2026-09-30. *Workaround:* poll `export.status`, never replay. *Status:* fixed in exact-release 2026-10-01 (asynchronous durable jobs).

**<a id="ki-073"></a>KI-073: Intermittent glyph corruption in exported frames.** Jobs completed with correct counts and RGBA, but frames showed long triangles/lines, displaced strokes, missing fill, edge-reaching alpha, once a fully opaque white frame (alpha min=max=255); native look of the same frame was correct. Pausing transport, single-frame export and an app restart did not help; affected frames varied per attempt. *Seen:* a pre-release build clean (sourceDirty false), 2026-10-01. *Workaround:* none on that build; compare disk frames to native look. *Status:* fixed in a patched executable (base a pre-release build, sourceDirty true, builtUnixSeconds 1790848932): 1030 frames clean; not seen since. Root cause unconfirmed.

**<a id="ki-074"></a>KI-074: Live job JSON read raised `PermissionError` or returned partial JSON** on Windows. *Seen:* 2026-10-01. *Workaround:* bounded retry of the read. *Status:* unknown.

**<a id="ki-075"></a>KI-075: Render & Send never finished the handoff.** Durable 207-frame job complete, `error=null`, files decoded, but `deliver.status` stayed `phase=rendering`, `progress=null`, `receipt=null`, and no timeline clip was created; later Files exports also left the stale rendering phase. *Seen:* a pre-release build, 2026-10-09. *Workaround:* Files export + Resolve scripting import; do not replay. *Status:* open (not retested).

**<a id="ki-076"></a>KI-076: Recovery gaps.** Single-file (video) atomic restart/rename verification and fine-grained encoder sub-phases are not implemented. *Seen:* exact-release 2026-10-01. *Workaround:* inspect terminal status; never infer success from transport loss. *Status:* open.

**<a id="ki-077"></a>KI-077: Export nests output and writes hidden files.** `<dir>\<name>\<name>_00000.png` plus a hidden source snapshot (and progress JSON). *Seen:* 2026-09-30. *Status:* documented behaviour; FR-005 asks for a flat option.

## 8. Resolve transfer and scripting

**<a id="ki-080"></a>KI-080: Arabic word stagger reverses after Fusion transfer.** Native RTL reveal becomes left-first in Fusion; shaping and string are correct; the character-index delay mapping is wrong. *Seen:* an early 0.1.4 pre-release build, Resolve Studio 21.1.0.14, 2026-10-12. *Workaround:* mirror delay tables in the destination graph ([workflows/rtl-and-arabic.md §7](workflows/rtl-and-arabic.md#7-fusion-transfer-the-rtl-stagger-workaround)). *Status:* open (compiler fix pending).

**<a id="ki-081"></a>KI-081: Transfer scope stale after `comp.switch`.** Cached scope kept the previous comp's 207 frames; two sends were refused for straddling the next clip (no Resolve change). `deliver.plan` ready=true did not reveal it. *Seen:* an early pre-release build. *Workaround:* assert `transfer.scopes[comp].frames` equals the comp duration; opening Deliver refreshed it. *Status:* open.

**<a id="ki-082"></a>KI-082: Follower Order enum label misleads.** UI suggests Order 7; Order 7 removed the stagger; measured manual Order 6 works. *Seen:* an early pre-release build / Resolve 21.1.0.14. *Status:* unknown.

**<a id="ki-083"></a>KI-083: Fusion scripting return values and names.** `BezierSpline.SetKeyFrames` returns `None` on success; `SaveSettings` needed `OrderedDict` in `__main__`; modifier names are normalised on import (`Obj6FollowerDelaybyCharacterPosition`). *Workaround:* read back keys; discover via `GetConnectedOutput().GetTool()`. *Status:* unknown (Resolve behaviour).

**<a id="ki-084"></a>KI-084: A resend overwrites destination graph edits** (RTL correction, speech delay tables). *Workaround:* save and reapply after each resend. *Status:* open.

**<a id="ki-085"></a>KI-085: Keyed compound path rendered one contour in Fusion** (a currency symbol became a dash). *Seen:* an early pre-release build. *Workaround:* several simple positive filled paths (six worked). *Status:* open (needs isolated reproduction).

**<a id="ki-086"></a>KI-086: Low-alpha icon tiles rendered opaque in Fusion,** covering line icons. *Seen:* an early pre-release build. *Workaround:* remove the tiles. *Status:* open (needs isolated reproduction).

**<a id="ki-087"></a>KI-087: Native and Fusion glyph widths differ** with the same resolved family. *Workaround:* set final gaps from the destination composite. *Status:* unknown.

**<a id="ki-088"></a>KI-088: PNG sequence FPS on import.** Imported at 24 fps on a 30 fps timeline; `SetClipProperty("FPS", 30.0)` did not apply (161 frames became 201); setting 30 when it already reads 30 can return False. *Seen:* Resolve 21.1, 2026-09-28/30, 2026-10-01. *Workaround:* read first; set the string `"30"`; assert return and readback before append. *Status:* unknown (Resolve behaviour; helper fixed).

**<a id="ki-089"></a>KI-089: `AppendToTimeline` `endFrame` is exclusive count.** `endFrame=n−1` gave n−1 frames (433 vs 434). *Workaround:* `endFrame=n`, assert placed duration. *Status:* unknown.

**<a id="ki-090"></a>KI-090: `Gallery.ExportStills` races and misorders.** Returned True before all PNGs were readable (`FileNotFoundError`); stale grabs mixed in on retry; generated names gave a non-chronological sheet. *Seen:* a pre-release build, Resolve 21.1, 2026-09-30. *Workaround:* `ExportCurrentFrameAsStill` with explicit paths. *Status:* open (FR-017).

**<a id="ki-091"></a>KI-091: Still capture shows the wrong frame.** 0.2 s after a seek captured the previous overlay; timecode drifted during repeated captures (read 12:16 after seeking 5:01); first capture after timeline switches failed its assertion. *Workaround:* pause, settle (0.75–4 s), assert timecode before and after. *Status:* unknown.

**<a id="ki-092"></a>KI-092: Inactive timelines report false track flags and missing audio properties.** *Workaround:* activate before reading. *Status:* unknown.

**<a id="ki-093"></a>KI-093: No timeline-item edge trim in Resolve 21.1 scripting.** *Workaround:* delete-and-reappend fallback. *Status:* unknown.

**<a id="ki-094"></a>KI-094: `MediaPool.DeleteClips` returned False** for unused entries; removal not confirmed. *Status:* unknown.

**<a id="ki-095"></a>KI-095: Resolve refuses an adjustment layer with no effects.** *Seen:* 0.0.69. *Status:* unknown.

**<a id="ki-096"></a>KI-096: `GetSourceStartFrame()` is source-rate, not `sourceIn`.** Baseline comparisons need `GetLeftOffset()`. *Status:* unknown (Resolve behaviour).

**<a id="ki-126"></a>KI-126: Fusion transfer carrier arrives at 30 fps on a 24 fps timeline and plays 1.25× fast.** All sends share one carrier media-pool item; it read `FPS 30.0` after a fresh send. *Seen:* 0.0.82, Resolve Studio 21.1, 2026-10-22. *Workaround:* after each send read the carrier's FPS and `SetClipProperty("FPS", "24")` (string), then read it back. *Status:* open.

**<a id="ki-127"></a>KI-127: Some transferred comps land one frame short.** A 173-frame comp placed as 156–328 and a 109-frame comp as 667–775; six other comps placed at full length. *Seen:* 0.0.82, 2026-10-23. *Workaround:* assert each placed clip's start/end against the comp length; keep the last frame empty. *Status:* open.

**<a id="ki-128"></a>KI-128: Transfer reports `connected:false` after a fresh launch** until `resolve.refresh` is run, even with Resolve open on the right timeline. *Seen:* 0.0.82. *Workaround:* `resolve.refresh`, then check `carvercat_state transfer` shows the timeline before sending. *Status:* behaviour.

**<a id="ki-129"></a>KI-129: Transferred comps keep positions as fractions of frame height, so they don't adapt to another aspect.** A 1080×1920 caption comp placed on a 1080×1080 timeline rendered at full pixel size but with y squashed: a three-item stack and two-line blocks overlapped. *Seen:* 0.0.82 + Resolve Studio 21.1, 2026-10-23. *Workaround:* build a separate comp per aspect (copy the project JSON, set scene `height`/`timelineHeight`, remap each `position` y in pixels; see [resolve-handoff §5](workflows/resolve-handoff.md#other-aspect-ratios-from-one-edit-verified-2026-10-23)). *Status:* behaviour.

**<a id="ki-130"></a>KI-130: `Timeline.DeleteClips(list)` can return None and delete nothing.** Seen on a caption track with eight Fusion carriers (also earlier on a duplicated timeline). One item per call returned True every time; the same call with several items also worked on other timelines. *Seen:* Resolve Studio 21.1, 2026-10-22/23. *Workaround:* check the item count after deleting; fall back to one `DeleteClips([item])` per script call (a loop in one call hit the MCP's 10 s script limit). *Status:* unknown (Resolve).

**<a id="ki-131"></a>KI-131: Playhead seeks are ignored on the Edit page and the next still can be stale.** `SetCurrentTimecode` called while on the Edit page left the playhead where it was; stills exported in the same call as the seek sometimes showed an earlier frame. *Seen:* Resolve Studio 21.1, 2026-10-23. *Workaround:* `OpenPage('color')`, seek and read back the timecode in one call, then `ExportCurrentFrameAsStill` in the next call. *Status:* unknown (Resolve).

## 9. Performance

**<a id="ki-100"></a>KI-100: Duplicate clip IDs across timelines slow the UI.** A duplicated assembly with the same audio/nested IDs took UI work from ~20 ms to ~115 ms per frame and starved audio (`carvercat_state.audio.starved` rising). *Seen:* 0.0.69, Windows. *Workaround:* re-prefix every ID in the copy (`clip_N` → `clipv_N`, including property keys) in JSON, reopen ([performance.md](app/performance.md)). *Status:* unknown.

**<a id="ki-101"></a>KI-101: Hundreds of round trips per comp.** About 150 relay calls for one 434-frame comp. *Status:* fixed by `carvercat_batch` (≤256 steps; 48 → 2 requests in a benchmark; no render speed-up claimed).

**<a id="ki-102"></a>KI-102: Resolve Color-page stills cost about 1 s each.** *Status:* unknown.

## 10. UI

**<a id="ki-105"></a>KI-105: Export blocked the editor and hid progress.** *Status:* fixed in exact-release 2026-10-01 (background worker, Deliver opens, seek 0 ms during export).

**<a id="ki-106"></a>KI-106: Relaunch from another working directory exited.** Launching an early pre-release build from the chat's directory exited; from the app repository it worked. *Seen:* an early pre-release build. *Status:* unknown.

**<a id="ki-107"></a>KI-107: Project Navigator connector coordinates were wrong** in native review before release. *Seen:* a 0.1.4 release candidate, 2026-10-05. *Status:* fixed in that candidate (covered by a usage-attachment check).

## 11. Feature requests only

| ID | Request | Status (if stated) |
|---|---|---|
| <a id="fr-001"></a>FR-001 | Text background box / pill preset that auto-fits text width | partly covered by `cc_scene` components (`caption`, `number_highlight`, `card_group`) |
| <a id="fr-002"></a>FR-002 | `key.set` with explicit clip id; batch many keys/properties in one call | done: `carvercat_batch` |
| <a id="fr-003"></a>FR-003 | One-call stagger reveal (`text.reveal by=word gap=N slide=up`) | partly: `cc_scene` stagger/entrance helpers |
| <a id="fr-004"></a>FR-004 | Trim-path, gradient-stroke and mask presets; image + label card composite | partly: `image_card` component |
| <a id="fr-005"></a>FR-005 | Export to a flat folder with filename pattern and overwrite; report frame count and alpha mode | unknown |
| <a id="fr-006"></a>FR-006 | `object.new` returns full descriptor and accepts `start=` | partly: batch step `frame` (0.0.71) |
| <a id="fr-007"></a>FR-007 | `comp.duplicate` | done (exists; keeps IDs, see KI-100) |
| <a id="fr-008"></a>FR-008 | `carvercat_look` region crop/zoom | done (`region`; full-frame backgrounds may draw partly) |
| <a id="fr-009"></a>FR-009 | Accept hex in colour params | done in `cc_scene`; raw params stay linear |
| <a id="fr-010"></a>FR-010 | `mask.make` with explicit `mask=` and `over=` | unknown |
| <a id="fr-011"></a>FR-011 | `media.import` import-only (`place=false`) | open |
| <a id="fr-012"></a>FR-012 | Lint warns on font fallback; `inspect` reports text extents | done: `font_exact` validate, `mode=geometry` |
| <a id="fr-013"></a>FR-013 | `look` returns fresh path/hash and a diff-vs-previous mode | partly (dedup by bytes) |
| <a id="fr-014"></a>FR-014 | Text auto-width, group layout, align/distribute | done: `align.apply` (0.0.72), `cc_scene` fit/flow |
| <a id="fr-015"></a>FR-015 | Per-point corner radius; preset icon set | unknown |
| <a id="fr-016"></a>FR-016 | `export.run` returns a job id; status polling by default | done (exact-release 2026-10-01) |
| <a id="fr-017"></a>FR-017 | First-party Resolve verification helper: seek, settle, assert timecode, explicit-path export | open |
| <a id="fr-018"></a>FR-018 | Refuse/lint row collisions naming the conflicting clip and range | partly (current path creation validates room) |
| <a id="fr-019"></a>FR-019 | Keep comp-to-timeline content labels in project/job metadata | unknown |
| <a id="fr-020"></a>FR-020 | Save verification helper (path, size, mtime, hash); documented relay re-discovery | open |
| <a id="fr-021"></a>FR-021 | Durable, user-accessible per-word timing in the native source | open |
| <a id="fr-022"></a>FR-022 | Runtime font rescan without restart | open |
| <a id="fr-023"></a>FR-023 | Truthful no-op results instead of refusals | open |
| <a id="fr-024"></a>FR-024 | Effective-anchor discovery for baked paths | open |
| <a id="fr-025"></a>FR-025 | Higher-level component update helper | done: `scene.component` |
| <a id="fr-026"></a>FR-026 | People (not only agents) can select a Resolve clip, open its native source, edit, then **Place new**, **Replace selected clip** or **Update existing Fusion clip** with target preview, stale-target checks, truthful outcomes and no automatic replay; UI, MCP, schema and skills share one implementation | open (requirement, parked) |
| <a id="fr-027"></a>FR-027 | Track kind in `carvercat_list` | done (list v2) |
| <a id="fr-028"></a>FR-028 | Availability gate for declared controls that do not materialise | partly (`available` flag) |
| <a id="fr-029"></a>FR-029 | One-page docs: coordinates, aliases, stagger proxy paths, derived cache fields, which params apply to which kind | partly ([mcp-essentials.md](app/mcp-essentials.md) units) |
| <a id="fr-030"></a>FR-030 | Relay returns ASCII-safe JSON escapes | unknown |
| <a id="fr-031"></a>FR-031 | Async/long-deadline export client | done (async jobs) |
| <a id="fr-032"></a>FR-032 | Compact batch receipts (summary only, opt-in per-step detail) and a documented JSON import format for agent-written comps | open |
| <a id="fr-033"></a>FR-033 | Autosave / crash recovery of the open document | open |
