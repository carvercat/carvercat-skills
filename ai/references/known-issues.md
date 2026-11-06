# Known issues

Read this when a Carvercat command, export or Resolve handoff behaves unexpectedly, before you report a "new" bug, and when you plan a job on an older build.
Every product bug, refusal, surprise and limitation found in field work, deduplicated and grouped by area. Feature requests are listed separately at the end.

Format: **ID: title.** Symptom. *Seen:* first build/date stated. *Workaround.* *Status:* `open`, `fixed in X`, or `unknown` (only what the evidence says). IDs are stable; never renumber, add new ones at the end of their area block.
Builds are Carvercat unless marked Resolve. "Exact-release 2026-10-01" = app commit (export/lane/revision work). Workflows: [workflows/](workflows/job-playbook.md). Command basics: [mcp-essentials.md](app/mcp-essentials.md), [api-gotchas.md](app/api-gotchas.md).

## Contents
1. [MCP and agent API](#1-mcp-and-agent-api) (KI-001–KI-027, KI-166–KI-170 design units, KI-117–KI-121 JSON authoring, KI-122–KI-125 session/fonts/batches, KI-152 curves, KI-155, KI-164 qc)
2. [Timeline and clips](#2-timeline-and-clips) (KI-030–KI-037)
3. [Text and stagger](#3-text-and-stagger) (KI-040–KI-051, KI-132–KI-136, KI-151, KI-154, KI-156, KI-157, KI-158, KI-160, KI-162)
4. [Effects](#4-effects) (KI-055–KI-059, KI-159)
5. [Shapes and paths](#5-shapes-and-paths) (KI-060–KI-062, KI-108–KI-116 rigging, instances, maps, KI-137, KI-150, KI-153, KI-161, KI-163)
6. [Audio](#6-audio) (KI-065–KI-068)
7. [Export](#7-export) (KI-070–KI-077)
8. [Resolve transfer and scripting](#8-resolve-transfer-and-scripting) (KI-080–KI-096, KI-126–KI-131)
9. [Performance](#9-performance) (KI-100–KI-102)
10. [UI](#10-ui) (KI-105–KI-107)
11. [Feature requests only](#11-feature-requests-only) (FR-001–FR-050)

## 1. MCP and agent API

**<a id="ki-001"></a>KI-001: Carvercat tools missing from the chat.** MCP enabled in the app, but no Carvercat tools in the session; the client config pointed at an older agent executable (c325) while c423 was running. Cause not proven. *Seen:* c423, 2026-09-28. *Workaround:* use the loopback relay through the published endpoint file ([workflows/resolve-handoff.md §1](workflows/resolve-handoff.md#1-connect-to-the-right-editor)); do not change global client config without authorisation. *Status:* unknown.

**<a id="ki-002"></a>KI-002: Key and property calls act on the selection, with misleading errors.** `key.set` returned "no such property on this clip" and `key.handle` "not animated on this object" when another object was selected; `inspect probe` changed the selection; an ellipse "scale" refusal was the same cause. *Seen:* 2026-09-30 (build era). *Workaround:* use explicit IDs (batch steps, `cc_scene`); on old builds reselect before every key/property call. *Status:* probe no longer changes selection (toolkit notes, 2026-10-10); selection-bound legacy commands unknown. *Status update (0.1.8):* with design units every per-object command takes `id` or a selector (`#title`, `text`), so nothing depends on the selection; the old selection-dependent forms remain. *Status update (0.1.8):* what a call made or touched stays selected for the next call, a batch included, and every per-object command takes an `id` or a selector anyway (verified: selection-and-fonts-in-a-fresh-process). Fixed on 6b.

**<a id="ki-003"></a>KI-003: `resolve.refresh` reply shows a stale `said`.** `answered=true` but `said` described the previous action. *Seen:* c423. *Workaround:* read `carvercat_state` for `transfer.connected`, project and timeline. *Status:* unknown.

**<a id="ki-004"></a>KI-004: Relay endpoint stale or refusing.** The app stayed open but the advertised loopback port refused the final `edit.save`; another time the old PID/port file pointed at an absent install; a port rediscovered from the PID file gave `ConnectionRefusedError`. *Seen:* 2026-09-30, 2026-10-09/10 (0.1.4). *Workaround:* rediscover the current endpoint (`carvercat-mcp-editor.pid` on current builds), verify PID and handshake; never claim a save from file existence; compare path, mtime, size and hash. *Status:* open (see FR-020).

**<a id="ki-005"></a>KI-005: No save path or dirty flag in live state.** Persistence could only be proven by file existence plus save/reopen. *Seen:* c423. *Workaround:* `edit.open` the saved file and read list/state. *Status:* unknown (current contract says to verify the document path through state; check your build).

**<a id="ki-006"></a>KI-006: `key.set` easing ignored.** `easing` accepted and ignored, even a bogus value. *Seen:* 2026-09-30. *Workaround:* set curves with `key.handle` on each key pair (out (0.32,0), in (0.68,1)). *Status:* differs by build: on 0.0.69–0.0.72 named easings (`Linear`, `Ease in`, `Ease out`, `S-curve`, `Hold`) work and other names silently become Linear ([mcp-essentials.md](app/mcp-essentials.md)). *Status update ():* fixed. `key.set {ease}` and `anim.set` take CSS easing and REFUSE a name they do not know (`bad-ease`); the old names still work as old names. `Ease in` and `Ease out` are not CSS `ease-in`/`ease-out`.

**<a id="ki-007"></a>KI-007: `key.handle` rejects the cap alias path.** `transform.placement.position` worked for `key.set`/`key.list` but not `key.handle`. *Seen:* c423. *Workaround:* use the exact stored path from `param.list`. *Status:* unknown.

**<a id="ki-008"></a>KI-008: Shape paint selectors absent from `param.list`.** Selectors are accepted but not listed; a builder that expected every writable selector in the list stopped. *Seen:* (0.1.4), 2026-10-09. *Workaround:* use the canonical declared capability key; the native command still validates it. *Status:* unknown (documented as expected in [creative-controls.md](app/creative-controls.md)).

**<a id="ki-009"></a>KI-009: Declared controls that are not live.** (a) Unsupported Basement parameters are listed but `available:false` with `unavailable_reason`; promote/reset/link/`property.set` refuse without change. Advanced gradient fields (`gradientAngle`, `gradientSize`…) do not drive the picture; the `gradient` paint object does. (b) Repeatable Stroke `opacity` is in the declaration snapshot but `param.promote` refused it, rolling back a 104-step plan. (c) Text gradient `gradientStart`/`gradientEnd` are not live, so text gradients stay static. *Seen:* (a) 2026-10-01; (b)(c) 0.1.4 Build18, 2026-10-10. *Workaround:* check `available` before writing; for stroke alpha use `fx_set(alias, "opacity", …)` or RGBA via `fx_color`; keep text gradients static, animate shape-gradient endpoints. `native-controls.json` is discovery data, not a live availability list. *Status:* (a) by contract; (b) explained later (opacity is absorbed into Colour and is directly settable); (c) open.

**<a id="ki-010"></a>KI-010: Harmless no-ops reported as refusals.** `refused:true`/isError for: `stagger.set` with current values (`why=unchanged: already set to that`), `stagger.list` with valid readings, `comp.rename` unchanged, `key.handle` already set, `track.remove_empty` ("no empty tracks to remove"), and a same-place `clip.move` (aborts the whole batch). *Seen:* c423 2026-09-28; still on 0.1.4 Build18 2026-10-10. *Workaround:* read state and write only differing fields; tolerate only exact identified wording. *Status:* `clip.move` no-op fixed in 0.0.71; others open (FR-023).

**<a id="ki-011"></a>KI-011: Transient handle refusal after moving keys.** Moving a clip start 66→78 with keys at 78/85, a handle call refused `no keyframe at 7 on src.e_src_text_relative_clip_3.position`; the transaction rolled back. Isolated retries worked. *Seen:*, 2026-10-01. *Workaround:* confirm rollback and baseline, then rerun the full mutation once. *Status:* unknown (not reproduced).

**<a id="ki-012"></a>KI-012: Session reset leaves a blank Comp 1 open.** After a relaunch or a concurrent session change, the relay connected to a blank Comp 1 (zero clips); a `comp.switch` refusal followed, and a script that continued saved the blank document over the project. *Seen:*, 2026-10-01. *Workaround:* before export loops and saves, assert project identity (path, comps, revision), not only comp count; stop chains on failure. Recover from an export job's immutable source snapshot via `edit.open`. *Status:* unknown.

**<a id="ki-013"></a>KI-013: `edit.save` "Access is denied (os error 5)".** Saving to a writable job folder and to Documents failed; Temp worked. After an app restart direct saves worked. *Seen:*, 2026-09-30. *Workaround:* restart and retry; never leave the only copy in Temp. *Status:* unknown (unexplained).

**<a id="ki-014"></a>KI-014: Old Python helper hid envelope fields and refusals.** `cc_client.run(cmd, **args)` put `expected_revision`/`transaction` inside command args, printed refusals and returned them; `cc_build` kept going after a refused mutation. *Seen:* 2026-10-01. *Workaround:* current `Client.run` raises on refusals and `Client.batch` checks revision/document. *Status:* fixed in the current `Client` (creative-toolkit).

**<a id="ki-015"></a>KI-015: Installed app older than the published contract.** The running executable had no `revision`, list v1 string labels, and no top-level `expected_revision`, while source/schema did. *Seen:* 2026-10-01. *Workaround:* check live state for these fields before relying on them. *Status:* fixed in (fields exposed live).

**<a id="ki-016"></a>KI-016: `carvercat_look` stale or refused images.** Unchanged image refused unless `force:true`; `count:1` gave a stale image; the viewed `look.png` lagged one call. *Seen:* 2026-09-30. *Workaround:* numeric checks (PIL bbox on a black-ground look). *Status:* fixed in the current contract: dedup follows rendered bytes and `Client.look` returns an empty file list for unchanged images ([current-artwork-contract.md](app/current-artwork-contract.md)).

**<a id="ki-017"></a>KI-017: Non-ASCII output breaks Windows consoles.** Arabic and U+2018 printed as `?` or raised `UnicodeEncodeError` under cp1252. *Seen:* 2026-09-28/30. *Workaround:* `python -X utf8`, UTF-8 JSON, JSON escaping. *Status:* open (tooling; FR-030).

**<a id="ki-018"></a>KI-018: `select.clip` uses a shifting list index.** The index changes as objects are added or deleted. *Seen:* 2026-09-30. *Workaround:* re-resolve before each selection, or use explicit IDs. *Status:* unknown.

**<a id="ki-019"></a>KI-019: Scene aliases made from IDs break name-based rebind/fit.** *Seen:* 0.1.4 Build46. *Workaround:* keep validated name mappings; use measured placement for stable objects. *Status:* unknown.

**<a id="ki-020"></a>KI-020: `edit.new` adds an empty default comp.** `comp.new` then appends, so four new comps make five. *Seen:*. *Workaround:* reuse or verify-and-delete the default; assert comp identity before export. *Status:* unknown.

**<a id="ki-021"></a>KI-021: A "blank" comp can carry undo history.** No objects, but `undo=true`, `said='deleted Rectangle'`. *Seen:* c423. *Workaround:* do not force-new or discard; configure and save it. *Status:* unknown.

**<a id="ki-022"></a>KI-022: Derived `fontResolved` cache changes on save.** Shape objects gained `Open Sans` in unused `textProps.fontResolved`; a legacy text cache string changed on save. *Seen:* c423; 0.1.4 (2026-10-10). *Workaround:* exclude derived fields from comparisons; never hand-edit JSON to remove them. *Status:* unknown.

**<a id="ki-023"></a>KI-023: Project-JSON edits: force-reopen and cloned clips.** `edit.open {force:true}` discards unsaved app work; a clip cloned in JSON shows keys but does not animate. *Seen:* 0.0.69. *Workaround:* retime/restyle only MCP-created clips in JSON; keep the person's hands off during the loop. *Status:* unknown.

**<a id="ki-024"></a>KI-024: Group editing scope.** `key.set` on a child refuses ("outside the current editing scope") until `object.enter`; `object.new` refuses inside an entered group; `object.enter/exit` are not batchable. *Seen:* 0.0.69. *Workaround:* enter/exit around child keys; create at top level, then move into the group. *Status:* unknown.

**<a id="ki-025"></a>KI-025: Hidden clips still return measured bounds.** *Seen:* 0.1.4 Build46. *Workaround:* check enabled/hidden state and the actual composite before diagnosing missing text. *Status:* unknown.

**<a id="ki-026"></a>KI-026: No "remove all keys"; `key.remove` acts at the playhead and takes only `key`.** *Seen:* 0.0.69. *Workaround:* `Scene.replace_keys`, or `edit.undo`. *Status:* unknown. *Status update (0.1.8):* `key.remove` still takes the stored key path (verified: `transform.placement.position` removes the position keys); *Status update :* `key.remove {id, key: "opacity", at}` removes a key by design name at a frame (the playhead when `at` is omitted; a frame with no key is refused and says where the key is); verified: keyed-soft-edge-feather-blur-trim. Fixed on 6b.

**<a id="ki-027"></a>KI-027: `carvercat_authoring mode=controls query=` matches parameter names only** (e.g. `size`, `shadow`), not capability names; `carvercat_look` takes `from`/`to`, not `frame` (unsupported argument refuses). *Seen:* 0.0.69; Build46. *Workaround:* query by parameter name; use `from`/`to`. *Status:* unknown.

**<a id="ki-117"></a>KI-117: Positive text tracking written into project JSON rendered scrambled.** A tracked "POSITION" label drew as reversed, spaced glyphs. *Seen:* 0.0.72, 2026-10-20. *Workaround:* omit tracking on JSON-authored text. *Status:* open.

**<a id="ki-118"></a>KI-118: Large films overflow MCP batches.** Receipts and payloads for 1,000+ objects exceed transport limits and take hours. *Seen:* 0.0.72. *Workaround:* generate the comps into the `.carverproj` and reopen with `edit.open {force:true}` ([app/json-authoring.md](app/json-authoring.md)). *Status:* open (no documented import format).

**<a id="ki-119"></a>KI-119: Nested-comp instances ignore their parent's transform.** A camera null moved ordinary objects but not nested instances. *Seen:* 0.0.72. *Workaround:* bake the camera into the instance's own keys (in source time: local + `sourceIn`). *Status:* open.

**<a id="ki-120"></a>KI-120: `parent.assign` uses the first selected object as the parent**, not the last. *Seen:* 0.0.72. *Workaround:* select the parent first, or set `parentId` in JSON. *Status:* behaviour. On 0.1.6 rev 1105 the active, **last-selected** object became the parent ("parented 1 to Pivot" after selecting the child, then the pivot), matching the command summary: 0.1.6: the active object is the parent; use `dry_run:true` to confirm.

**<a id="ki-121"></a>KI-121: `cornerRadius` caps at 0.5 (of half the short side)**, so a true pill can't be a rectangle. *Seen:* 0.0.72. *Workaround:* 2-point path with a round-capped stroke. *Status:* behaviour.

**<a id="ki-122"></a>KI-122: Unsaved MCP work is lost when the connection drops or the app restarts.** Two scenes of batch edits vanished after an MCP "connection closed"; the app reopened with no document and the file on disk was the last `edit.save`. *Seen:* 0.0.82, 2026-10-22. *Workaround:* `edit.save` after every scene; prefer direct JSON editing ([app/json-authoring.md](app/json-authoring.md)). *Status:* open (no autosave/recovery).

**<a id="ki-123"></a>KI-123: Fonts installed per-user are missed when the app is started outside the MCP.** Almarai (HKCU-registered) resolved silently to Segoe UI after an external restart; every text measured and drew with the wrong face. Relaunching through `carvercat_session {allow_launch:true}` loaded it. *Seen:* 0.0.82, 2026-10-22. *Workaround:* check `carvercat_authoring fonts` after every app start; relaunch via the MCP. *Status:* open (see FR-022). *Update 2026-10-23:* it recurred in an instance that **was** launched through the MCP (Arabic previews and `observe` widths fell back to Segoe UI mid-session); only a close-and-relaunch fixed it. Check `fonts` before every measuring step, not only at start. Resolve itself rendered Almarai correctly in the transferred comps throughout.

**<a id="ki-124"></a>KI-124: `carvercat_batch` `observe` is capped at 16 entries and the cap is undocumented.** A batch with 20 observations was refused as a whole ("at most 16 observations"). *Seen:* 0.0.82. *Workaround:* 16 per batch; read the rest with `carvercat_authoring mode=geometry`. *Status:* behaviour (undocumented).

**<a id="ki-125"></a>KI-125: Batch receipts are very large.** A 200-step batch returned about 60 KB (one receipt per step, full geometry per observation), overflowing tool output. *Seen:* 0.0.82. *Workaround:* fewer, larger JSON edits instead of batches. *Status:* open (FR-032).

**<a id="ki-140"></a>KI-140: `inspect qc` loop-seam check only compares brightness.** A 60 f comp whose square stopped at −80° (eased) instead of completing its cycle, and whose dot ended 20 px off its start, reported `loops_cleanly: true` (mean luma difference 0.003; the clean version 0.001). Position or rotation jumps at the seam are invisible to the check. *Seen:* 0.1.6 rev 1105, 2026-10-28, wiki techniques lab. *Workaround:* compare frame 0 with the predicted frame after the last using `inspect probe` or `expect` sentences ([../../wiki/techniques/looping.md](../../wiki/techniques/looping.md)). *Status:* open ([FR-038](#fr-038)).

**<a id="ki-164"></a>KI-164: `inspect qc` calls a slow Ken Burns zoom a freeze.** Three photos, each zooming 1.00 → 1.12 (2.56 px/frame in width) with a 1.1 px/frame drift, were reported as "nothing on screen changes for 2 s or more" for f0–75, f90–150 and f165–239 (a note: "fine for a hold, worth knowing"). The picture was moving in every frame (probe). *Seen:* 0.1.6 rev 1105, 2026-10-28, wiki cookbook round 3 (comp `K Ken Burns`; [../../wiki/cookbook/ken-burns-slideshow.md](../../wiki/cookbook/ken-burns-slideshow.md)). *Workaround:* read it as a note, not a fault; confirm motion with `inspect probe`. *Status:* unknown.

**<a id="ki-141"></a>KI-141: `json_author/cc.py` `lin()` converts hex with the sRGB curve; the renderer uses BT.709.** Rendered with `carvercat_render` and read back: #808080 written as `lin()` 0.2158 came out as 115/115/115 (not 128); #F2B03C came out as #F0A72C; a stored 0.5 renders 180, matching the BT.709 curve that `cc_scene.linear_hex` and the agent contract use. Mid-tones written through `cc.py` render about 10% darker than their hex. *Seen:* 0.1.6 rev 1105, 2026-10-28, wiki accessibility lab (comp `C Colour`). *Workaround:* convert with BT.709 (`v/4.5` below 0.081, else `((v+0.099)/1.099)^(1/0.45)`), e.g. `cc_scene.linear_hex`; check brand colours on a rendered frame ([../../wiki/design/colour-psychology.md](../../wiki/design/colour-psychology.md)). *Status:* open (helper, not the app).

**<a id="ki-155"></a>KI-155: `json_author/cc.py` `gradient()` writes the endpoints as comp coordinates with y up; shape gradient endpoints are object-local with y down.** A band written with `gradient(stops, (960, 0), (960, 160))` (alpha 1 → 0 from the top) rendered alpha 0 at the top and 1 at the bottom; a test rectangle red → blue from top to bottom rendered blue at the top. Written as object-local `start [0.5, 0]`, `end [0.5, 1]` the fade came out the right way. *Seen:* 0.1.6 rev 1105, 2026-10-28, wiki cookbook lab 5 (comp `K Credits`). *Workaround:* write the packed `gradient` `start`/`end` (or `gradientStart`/`gradientEnd`) in object-local units, `[0, 0]` top-left to `[1, 1]` bottom-right ([../../wiki/techniques/gradients-in-motion.md](../../wiki/techniques/gradients-in-motion.md), [../../wiki/cookbook/credits-roll.md](../../wiki/cookbook/credits-roll.md)). Text gradients use the same space (measured: `text_fill` `[0.5, 0]` → `[0.5, 1]` puts stop 0 at the top of the letters); a radial's `start` is its centre and the distance to `end` its radius. *Status:* fixed in the helper 2026-10-28: `gradient(stops, start, end)` now takes comp pixels, y down (the module's space), on the object at rest and stores them object-local; `local=True` takes object-local units; comp pixels work for `rect()` and `ell()` only. Audit of every gradient in the templates and samples ([audits/gradient-direction-audit-2026-10-28.md](audits/gradient-direction-audit-2026-10-28.md)): 15 rows checked, 3 templates fixed (`rt_synthwave` sun and `rt_chrome_title` chrome were upside down, `ml_product_frame` was lit from below) with the 8 saved samples that carry them; the rest read fine and are unchanged (stand-ins, close dark backgrounds, horizontal sweeps), except the wiki `cookbook-lab-1` Sky, which is upside down and left to the cookbook work. Re-measured on 0.1.6 rev 1105.

**<a id="ki-143"></a>KI-143: `inspect lint` minimum text size does not scale with the comp size.** On a 3840 × 2160 comp `text_too_small` still fires only under 18 px of line height in comp pixels: 28 px Rethink Sans (19.9 px tall, the size of 14 px text on an HD frame) passed, while the graphics-safe box did scale to `[192, 108, 3648, 2052]`. Small text on 4K and LED-wall comps passes lint. *Seen:* 0.1.6 rev 1105, 2026-10-28, wiki genres lab (comp `G 4K 3840x2160`). *Workaround:* pass `min_text_px` scaled to the comp height (36 at 2160 lines); `min_text_px: 36` flagged everything under a 50 px font size there ([../../wiki/genres/event-openers.md](../../wiki/genres/event-openers.md)). *Status:* open ([FR-039](#fr-039)). *Status update (0.1.8):* `fontSize` is a true px em and `text.fit` fits it with the canvas shaper, so a size is in px on every comp size; the lint threshold itself is unchanged.

**<a id="ki-152"></a>KI-152: `inspect curves` measures overshoot against the whole lane, so a second move reads as overshoot.** A text faded in (opacity 0 → 1, f12–14), held, then dimmed (1 → 0.6, f26–34) was reported with `overshoot_pct` **66.7** (consistent with (1 − 0.6) / 0.6: the held value above the last key), although no segment overshoots; one-move lanes on the same comp read 0%. A pack doc that quotes "0% overshoot" from this field can be wrong in either direction for multi-move lanes. *Seen:* 0.1.6 rev 1105, 2026-10-28, Social Short-form round 3 (comp `SS Price drop`, first build). *Workaround:* read overshoot per move: measure lanes with one move each, or judge each segment from the sampled values (`samples`) against its own two keys ([../patterns/ss-price-drop.md](../patterns/ss-price-drop.md)). *Status:* unknown (may be by design).

**<a id="ki-166"></a>KI-166: `scene.apply` refused a `path` node.** A scene object `{type: "path", d: "M ..."}` was refused with `model-refused: no such object: path`, alone or with other objects. *Seen:* Carvercat 0.1.8 (0.1.8-dev.3), headless, 2026-11-02. *Workaround:* create paths with `object.path` (`Client.path` in `ai/scripts/cc_client.py`). *Status:* fixed in 0.1.8: a `type: "path"` node takes SVG path data `d` on the node (not in `style`), `scene.get` returns `d`, and `get -> apply -> get` keeps it (verified: path-node-in-a-scene). `pointsPx` is also accepted by `object.path`.

**<a id="ki-167"></a>KI-167: A host built from source needed its resource folder, and a fresh process needed its fonts loaded.** Headless `carvercat-host --mcp` started outside the app checkout answered "no such property on this clip" for `softEdge` and refused `fontFamily: "Open Sans"` as not installed. Text outside a scene said "the installed fonts are still loading" until a font call had run. *Seen:* 0.1.8-dev, 2026-11-02. *Status:* fixed in 0.1.8 for the first two: the parameter registry is compiled in (a host started outside a checkout lists parameters and takes `softEdge`), and every command waits for fonts once, so no font call is needed first (verified: host-outside-the-checkout). *Still true:* the bundled font families (Open Sans) are found only through `CARVERCAT_RESOURCE_ROOT` (the app resource folder); without it `fontFamily: "Open Sans"` is refused as not installed. `Client.stdio(exe, state, resource_root=...)` sets it.

**<a id="ki-168"></a>KI-168: Keying by design name was limited.** `anim.set` and `key.set` refused `softEdge`, `feather`, `blur`, `glow`, `dropShadow`, `brightness`, `contrast`, `strokeWidth`, `borderRadius` and the trims (`bad-keys` / "no such property"), and `key.remove` took stored paths only. *Seen:* 0.1.8-dev. *Status:* fixed in 0.1.8: every number keys by its design name in `anim.set`, `key.set`, `anim.get`, `key.list`, `key.remove {key, at}` and a scene node's `keyframes`; a keyword or count (`strokeLinecap`, `mixBlendMode`, `fontWeight`) is refused with the reason; `borderRadius` is for rectangles only (an ellipse, polygon or star is refused: "only a rectangle has rounded corners"); a stagger tween still takes only opacity, x, y, rotate and scale (verified: keyed-soft-edge-feather-blur-trim, keyed-trim-write-on-and-off, keyed-stroke-width-and-border-radius, keyed-blur-focus-pull, keyed-glow-shadow-brightness, keyed-feather-wipe, stagger-restated-and-read-back).

**<a id="ki-169"></a>KI-169: A mask's `invert` flag survived `mask: none`.** A mask re-set without `invert` stayed inverted. *Seen:* 0.1.8-dev. *Workaround:* always write `invert` explicitly. *Status:* fixed in 0.1.8: `none` clears the flag, so a mask set again without `invert` is a normal mask (verified: mask-and-invert). Setting a mask over an object that is already masked is still refused; clear with `none` first.

**<a id="ki-170"></a>KI-170: `scene.get` did not nest a grandchild made with `parent.assign`.** With two nulls (or any parents) where a child is assigned to a parent that is itself a child (`parent.assign {ids: [inner, plate]}` then `{ids: [outer, inner]}`, or the other order), `scene.get` listed the plate at the top level with its parent-relative `x`, `y` (`-250, -50`) and left the inner null with no `children`; applied to a fresh comp the plate landed off the frame. *Seen:* 0.1.8-dev, headless, 2026-11-02. *Status:* fixed in 0.1.8. Verified on 0.1.8 (verified: null-rig-parent-assign): `scene.get` returns the outer null with the dot and the inner null as `children` and the plate under the inner null (parent-relative `x` -250, `y` -50); the document applies to the same comp and to a fresh one and reads back exactly, and the plate renders in place. No workaround is needed: a `parent.assign` rig round-trips through `scene.get` like one built from nested `children`.

## 2. Timeline and clips

**<a id="ki-030"></a>KI-030: Visual objects and masks on the audio row were silently invisible.** `object.new track=<audio row>` succeeded but never rendered; `mask.make` with the mask on the audio row reported "masking 1 track" but did not mask. *Seen:* 2026-09-30. *Workaround:* read `carvercat_list.tracks[].kind`. *Status:* fixed in exact-release 2026-10-01 (creation and masks refuse audio rows; list v2 publishes `{index,id,label,kind}`).

**<a id="ki-031"></a>KI-031: Dragged audio clip appeared on a video lane.** *Seen:* user report, 2026-09-30. *Status:* fixed in exact-release 2026-10-01 (drags clamp to the original track kind).

**<a id="ki-032"></a>KI-032: `clip.move` is an overwrite edit.** A short object created at frame 0 took a temporarily free track; moving it into an occupied range trimmed another card to 3 frames and deleted an accent, with no warning. *Seen:* c423. *Workaround:* create with full spans or with the batch step's `frame` so a free track is chosen; give overlapping items separate rows; verify durations after placement. *Status:* open (FR-018).

**<a id="ki-033"></a>KI-033: Creation lands at the live playhead.** `object.new`, `media.import` and adjustment layers placed at wherever the user last scrubbed (six text clips landed at 160 of 169; music at 61). *Seen:* 0.0.69. *Workaround:* give each batch step a `frame`; give `media.import` a `frame`; verify `left`. *Status:* fixed in 0.0.71 for batch steps with `frame`.

**<a id="ki-034"></a>KI-034: `object.path` defaulted to a free row and 90 frames.** Needed trim and move; overlapping path sets reused rows and produced shortened 10-frame objects with out-of-clip keys and lint errors. *Seen:* 2026-09-30. *Workaround:* distinct rows for simultaneous paths. *Status:* fixed in current contract (2026-10-15: `Scene.path` takes duration and exact track, validates room; no temporary 90-frame clip).

**<a id="ki-035"></a>KI-035: `media.import` auto-places clips.** Images fill rows 0..N−1; stills default to 90 frames; each audio file gets its own new audio track. *Seen:* 2026-09-28/30; 0.0.69. *Workaround:* import as a deliberate step, then set duration (e.g. 231) and move/delete explicitly; re-list between deletes. *Status:* open (FR-011).

**<a id="ki-036"></a>KI-036: `clip.move` cannot cross video/audio.** *Status:* by design since exact-release 2026-10-01.

**<a id="ki-037"></a>KI-037: Comp-local IDs repeat.** Every new comp restarts at `clip_1`. *Workaround:* assert the comp before targeting IDs; navigator targets pass the whole target. *Status:* unknown (behaviour).

## 3. Text and stagger

**<a id="ki-040"></a>KI-040: Mixed RTL text reverses numbers.** `40 شهر` rendered digits as `04`; numeric-only `10%` with rtl rendered `%01`. *Seen:* c423 2026-09-28; 2026-10-09. *Workaround:* separate LTR number objects ([workflows/rtl-and-arabic.md §3](workflows/rtl-and-arabic.md#3-numbers-and-latin-inside-arabic)). *Status:* open.

**<a id="ki-041"></a>KI-041: Native stagger has only a uniform gap.** Irregular word onsets cannot be stored in the native source. *Seen:* 0.1.4 Build46. *Workaround:* Fusion Follower delay tables, reapplied after each resend. *Status:* open (FR-021).

**<a id="ki-042"></a>KI-042: Fonts installed after launch are not found.** `property.set` accepted Alan Sans but the probe showed Segoe UI until save, quit and relaunch. *Seen:* c423;. *Workaround:* restart, reopen, re-probe. *Status:* open (FR-022).

**<a id="ki-043"></a>KI-043: Silent font substitution.** Sora, Outfit, Manrope, Lexend, Plus Jakarta Sans fell back to Segoe UI; only `look` notes said so; lint did not flag it. *Seen:* 2026-09-30. *Workaround:* `mode=fonts` queries, `require_font=True`, validate `font_exact`. *Status:* checks available in current builds; the old resolving-font list is not proof on another machine.

**<a id="ki-044"></a>KI-044: Font names and styles differ from what you expect.** Impact's style is Normal ("Regular" reports substitution); a packaged font's internal family differed from the installed live family (Bricolage Grotesque / ExtraBold was the working request). *Seen:* c423; 0.1.4 Build18. *Workaround:* discover names from the running app. *Status:* unknown.

**<a id="ki-045"></a>KI-045: Tracking garbles small text.** Size 0.036 with tracking 6 or 0.12 rendered mirrored letters ("TNEMGES"); tracking units undocumented. *Seen:* 2026-09-30. *Workaround:* leave tracking unset; Poppins SemiBold 0.04 worked. (Tracking 1 → 0.94 on larger price text was fine later.) *Status:* unknown.

**<a id="ki-046"></a>KI-046: Stagger-connected fill opacity only appears as a slot proxy.** `param.list` lacked `text.fill.opacity` after connection; `stagger.list` returns `stagger: null` for text without a card. *Seen:*. *Workaround:* use the slot's underlying `key`; treat null as no card. *Status:* unknown.

**<a id="ki-047"></a>KI-047: Outline needs paint on.** Default outline colour/thickness exist while `text.outline.paint` is off; setting thickness alone shows nothing. *Seen:*. *Workaround:* set `paint='solid'`, colour and thickness. *Status:* unknown (behaviour).

**<a id="ki-048"></a>KI-048: Outlined stagger reveals the stroke early.** *Seen:*. *Workaround:* connect and animate `stroke.opacity` with `fill.opacity`. *Status:* unknown (behaviour).

**<a id="ki-049"></a>KI-049: Extending a clip does not extend a relative-opacity exit.** After extending a 10% highlight from 20 to 44 frames, `text.relative.opacity` kept its old flicker/exit keys and hid the number at the old end. *Seen:* 0.1.4, 2026-10-10. *Workaround:* clear/retime the obsolete channel (`extend_hold` does this deliberately); check pixels past the old end. *Status:* authoring dependency, not a reproduced bug.

**<a id="ki-050"></a>KI-050: Stagger timing quirks.** The stagger replays the whole key timeline per part, so the last part ends `gap × (parts−1)` late and can overrun the comp; a text takes one staggered preset per property (a staggered exit on an entrance-staggered property is refused). *Seen:* 0.0.69–0.0.72. *Workaround:* gate with clip opacity; whole-block exits. *Status:* unknown.

**<a id="ki-051"></a>KI-051: `text.content` is not keyframeable.** No type-on counters. *Workaround:* cut text clips back to back (lint then warns `reading_time` per short clip). Lint-clean alternatives verified on 0.1.6: type-on with Stagger Text by character on the relative opacity ([../patterns/su-search-typing.md](../patterns/su-search-typing.md)); a masked rolling-digit counter ([../patterns/su-rolling-counter.md](../patterns/su-rolling-counter.md)). *Status:* unknown (FR-034).

**<a id="ki-132"></a>KI-132: "Clip to box" did not hide the extra lines of a multi-line text.** A 10-line title text (mode titles, box height one line, Clip to box on, vertical align top) still drew every line while its relative position was keyed. *Seen:* 0.1.6 rev 1105, 2026-10-27. *Workaround:* a mask rectangle per column (`mask.make {ids:[window, column]}`, window first, then `parent.clear`). *Status:* unknown (paragraphs mode not tried).

**<a id="ki-133"></a>KI-133: `inspect lint` ignores masks.** Masked content reports `cropped_at_rest` and `text_overlap` for parts the mask hides; the answer states "excludes masks". *Seen:* 0.1.6 rev 1105 (and the public release), rolling counter (13 such warnings). *Workaround:* judge masked builds with `carvercat_look`; nest them, since the instance in the parent comp lints clean. *Status:* by design today (FR-035).

**<a id="ki-138"></a>KI-138: Lint `text_overlap` does not report a small overlap between neighbouring texts.** Three tracked words 400 px apart (Regular 34 px, tracking 1.6, each about 432 px wide) ran into each other by about 30 px each, so "HANDMADE" and "FLORENCE" read as one word and a separator dot covered a letter; lint was 0 errors, 0 warnings, 0 notes. Other `text_overlap` reports in this build were 17–100% of the smaller box; this one was about 7%. *Seen:* 0.1.6 rev 1105, 2026-10-27, Minimal Luxury round 2 (Attribute row). *Workaround:* measure neighbouring texts with `carvercat_authoring mode:geometry` (bounds) and keep a gap, and check rows of words with a full-frame look; `ai/scripts/motion/audit_text_gaps.py` does this for every template ([audits/text-gap-audit-2026-10-28.md](audits/text-gap-audit-2026-10-28.md): 168 templates, five more fixed). *Status:* unknown (threshold not documented).

**<a id="ki-139"></a>KI-139: Motion Patterns "Lower third - accent bar" has a 7.6 px gap between its name and role at rest.** Found by the text-gap audit ([audits/text-gap-audit-2026-10-28.md](audits/text-gap-audit-2026-10-28.md)); lint does not report it ([KI-138](#ki-138)). *Seen:* 0.1.6 rev 1105, 2026-10-28. *Workaround:* after placing the template, move the role down 6–8 px inside its comp. *Status:* open; Motion Patterns is left unchanged and the fix is waiting on the user's decision.

**<a id="ki-144"></a>KI-144: Lint does not report content cut by the frame edge inside a moving nested instance.** A 16:9 template placed into a 1080 × 1920 comp and zoomed (instance size 2.0 with a 3% push) had its delta badge cut off at the right edge, and at 1.6 a progress ring was cut; lint was 0 / 0 / 0. Held still, the same zoomed instance is reported (`cropped_at_rest`, for the instance box), so the check sees the instance, not what is drawn inside it. *Seen:* 0.1.6 rev 1105, 2026-10-28, while making the 9:16 recipes. *Workaround:* check the widest element of every zoomed or moving instance with a full-frame `carvercat_look`; keep `content width × 0.5625 × zoom` under about 1040 px in a 1080-wide comp ([../recipes/vertical-recuts.md](../recipes/vertical-recuts.md)). *Status:* unknown.

**<a id="ki-151"></a>KI-151: Lint reports a mask window that runs past the frame as `cropped_at_rest`, although a mask is never drawn.** A feathered mask window (rectangle 1040 × 1160 px, Fill soft edge 140 px, the mask of a 760 × 880 px photo) at rest at the frame centre raised the warning "only 93% on screen while still" on the window; the photo it revealed was fully on screen. With the window shrunk to 960 × 1040 px the warning went away. Same root as [KI-133](#ki-133): lint treats a mask like a drawn object. *Seen:* 0.1.6 rev 1105, 2026-10-28, Minimal Luxury round 3 (comp `ML Editorial spread`). *Workaround:* keep mask windows inside the frame (size the content so content + 2 × feather fits), or ignore the warning on an object that is a mask. *Status:* unknown.

**<a id="ki-154"></a>KI-154: A mirrored shape (negative scale) reports a negative width, `on_screen` 0, and lint calls it `never_visible`.** A 200 px ring with scale `[-1, 1]` (to run its trim clockwise) probed `w` −200, `on_screen` 0.0, `visible` 0 on every frame and `inspect lint` gave the error `never_visible` "off frame for its whole clip", while `carvercat_render` drew it in every frame. *Seen:* 0.1.6 rev 1105, 2026-10-28, wiki cookbook lab 5 (comp `K Spinner`). *Workaround:* ignore that finding for mirrored objects and check them in a render, or mirror inside a nested comp ([../../wiki/cookbook/loading-spinner.md](../../wiki/cookbook/loading-spinner.md)). *Status:* unknown.

**<a id="ki-156"></a>KI-156: Lint `text_overlap` compares axis-aligned boxes, so rotated words that do not touch are reported overlapping.** On a price tag rigged to a nail and swinging in from 160°, "SALE" (ExtraBold 64 px) and "was $14" (Bold 54 px), 125 px apart on the tag, were reported overlapping by 15–18% at f5, when the tag was turned about 115°; a full-frame `carvercat_look` at f5 shows the two words well apart. Moving them a further 30 px apart did not clear it. Upright, the same pair lints clean. *Seen:* 0.1.6 rev 1105, 2026-10-28, Cartoon Bounce round 3 (comp `CT Price tag`). *Workaround:* bring rotated words on after the steep part of the move (here they pop at f16 and f22), or judge the frame with a look and accept the warning. *Status:* unknown.

**<a id="ki-157"></a>KI-157: Lint does not report text that runs past the panel it sits on.** In a 1300 px briefing panel (right edge at x 1610), three objectives at 34 px SemiBold with tracking 1.2 measured x 1020–1651 with `carvercat_authoring geometry`, so they ran about 40 px out of the panel onto the background; `inspect lint` (with `contrast:true`) was 0 errors, 0 warnings, 0 notes. Lint checks text against the frame and against other text, not against the shape behind it. *Seen:* 0.1.6 rev 1105, 2026-10-28, Futuristic HUD round 3 (comp `FH Mission briefing`, first build). *Workaround:* measure the text bounds against the plate with `carvercat_authoring geometry` and look at the full frame; wide-tracked caps are much wider than their character count suggests ([../patterns/fh-mission-briefing.md](../patterns/fh-mission-briefing.md)). *Status:* unknown (no check documented).

**<a id="ki-158"></a>KI-158: Lint reports every adjustment layer as the error `never_visible`.** In a 40 f comp, seven adjustment layers (one full-frame, six masked to horizontal bands, each with a horizontal `blur`) raised seven errors "off frame for its whole clip"; `carvercat_look` showed every one of them smearing the picture below. *Seen:* 0.1.6 rev 1105, 2026-10-28, Glitch round 3 (a datamosh-style smear, comp `GL Datamosh`, not kept). *Workaround:* judge adjustment layers with a look and accept those errors; templates in the Library use none (inside a placed template an adjustment layer only reaches the instance's own contents anyway). *Status:* unknown.

**<a id="ki-160"></a>KI-160: Lint `text_overlap` ignores masks.** Ticker headlines masked by a window that stopped at the tag (so they vanished under it) were reported overlapping the tag text by 16% once they had crawled under it; the render showed no overlap. Same family as [KI-151](#ki-151) (lint treats a mask window as drawn). *Seen:* 0.1.6 rev 1105, 2026-10-28, Glitch round 3 (comp `GL News ticker`). *Workaround:* keep texts that a mask hides apart in the layout (the tag moved to its own row above the band). *Status:* unknown.

**<a id="ki-162"></a>KI-162: Lint `text_too_small` fires on text that pops in from scale 0.** Three callout numbers (48 px Bold, scale 0 → 1 over 12 f with the `pop` bezier) raised "a line is 12.9 px tall at 1920x1080 (under 18)", 13.1 and 13.1; a logo letter popping the same way (110 px) raised "6.5 px tall". At rest all are far above 18 px; lint measured the small early frames. *Seen:* 0.1.6 rev 1105, 2026-10-28, wiki cookbook round 3 (comps `K Callouts`, `K Logo reveal`; [../../wiki/cookbook/tutorial-callouts.md](../../wiki/cookbook/tutorial-callouts.md)). *Workaround:* start the pop at scale 0.5 or more, or accept the warning after reading the size at rest with `inspect probe`. *Status:* unknown.

**<a id="ki-134"></a>KI-134: scaleX / scaleY cannot be staggered.** A staggered text preset with a `scaleY` track is refused: "scaleY could not be staggered" (the stagger takes the relative transform rows, Position, Scale, Rotation, Opacity, fill/stroke opacity and blur, or a Gaussian blur size). *Seen:* 0.1.6 rev 1105 (777df3c and), 2026-10-27. *Workaround:* uniform size, position, rotation or opacity per part; no per-letter flips. *Status:* unknown.

**<a id="ki-135"></a>KI-135: `carvercat_look` with `region` drew a full-frame background only as a corner strip.** On comps with a 1920×1080 background rectangle, a region look (for example [80, 800, 700, 220]) rendered the region black except a thin strip of the background colour. Text and other shapes in the region rendered correctly, and full-frame looks were correct. Seen on comps with and without masks. *Seen:* 0.1.6 rev 1105, 2026-10-27. *Workaround:* judge backgrounds from full-frame looks; use regions only to read text and shapes. *Status:* unknown.

**<a id="ki-136"></a>KI-136: Text resolves only installed fonts; the fonts inside the app bundle are not used for text.**
- The public 0.1.6 bundle ships Open Sans, Inter, Bricolage and JetBrains Mono in `Contents/Resources`.
- A text set to "Open Sans" Bold (also Inter SemiBold, Bricolage Grotesque ExtraBold) resolved to Arial in `carvercat_authoring mode:validate` `font_exact`.
- Rethink Sans (installed in `~/Library/Fonts`) and macOS system fonts such as Baskerville resolved exactly.

*Seen:* 0.1.6 rev 1105, 2026-10-27, headless. *Workaround:* install the font a template needs. Every verified style pack uses Rethink Sans (Google Fonts, SIL OFL; the file is in `ai/scripts/motion/json_author/RethinkSans.ttf`). Check with `font_exact` before rendering. *Status:* fixed for the app's bundled fonts in 0.1.8 (Carvercat uses them when not installed). Resolve and After Effects still need the font installed; Rethink Sans is not bundled.

**<a id="ki-142"></a>KI-142: `inspect lint contrast:true` skips Regular text under 34 px.** #595959 text on black (about 2:1 as rendered) got no `low_contrast` finding as Rethink Sans Regular at 24–32 px, while the same colour in Bold at the same sizes was an error, and Regular from 34 px was flagged. The thin, small text most at risk is not checked. Also: the check measures rendered ink, so ratios come out lower than the nominal colour ratio (#767676 on black, 4.6:1 nominal, measured 3.12:1 as 24 px Bold); the large-text rule (3:1) starts at a 34 px font size for both weights. *Seen:* 0.1.6 rev 1105, 2026-10-28, wiki accessibility lab (comps `C Contrast`, `C Sizes`). *Workaround:* check small Regular captions by their colour pair ratio by hand ([../../wiki/design/contrast.md](../../wiki/design/contrast.md)). *Status:* open.

**<a id="ki-145"></a>KI-145: `text.font.wordSpacing` is stored but not rendered by Carvercat.** Keyed 1 → 3 on a centred text, the measured width stayed 386 px at every frame while tracking and line spacing on neighbouring texts changed as expected. `carvercat_authoring mode:controls` reports "Resolve-only mapping; native text preview does not apply word spacing". *Seen:* 0.1.6 rev 1105, 2026-10-28, wiki measurement lab 3 (comp `T Spacing`). *Workaround:* tracking, or separate word clips ([../../wiki/techniques/text-spacing-animation.md](../../wiki/techniques/text-spacing-animation.md)). *Status:* open.

**<a id="ki-148"></a>KI-148: `text.outline.align` inside renders like centered.** Rethink Sans Bold "I" with a black outline at thickness 0.02, 0.05 and 0.1 (100 and 200 px): `inside` showed exactly the same outline width outside the glyph as `centered` (for example 7 px at 100 px / 0.1, 16–19 px at 200 px / 0.1), while `outside` doubled it (16 and 33 px). The control is listed as writable. *Seen:* 0.1.6 rev 1105, 2026-10-28, wiki measurement lab 5 (comp `P Outline`). *Workaround:* use centered (half the band shows) or outside ([../../wiki/techniques/text-outlines.md](../../wiki/techniques/text-outlines.md)). *Status:* open.

**<a id="ki-149"></a>KI-149: `carvercat_authoring geometry` bounds of a text stop at its last glyph; a trailing space is not counted.** Rethink Sans Bold 80 px, all left-aligned at x 360: "Ship it on " measured 321.9 px wide, but "Ship it on Friday" (561.4) minus "Friday" (214.0) puts the word at 347.4, so the space (25.5 px) is missing from the first. Placing a word at the right edge of "prefix + space" put it over the previous word; lint reported no overlap ([KI-138](#ki-138)). *Seen:* 0.1.6 rev 1105, 2026-10-28, wiki cookbook lab 2 (comp `K Highlight word`). *Workaround:* measure the prefix **with** the word and subtract the word's width (word left = right edge of "prefix word" − width of "word") ([../../wiki/cookbook/highlight-a-word.md](../../wiki/cookbook/highlight-a-word.md)). *Status:* unknown (may be by design: ink bounds).

## 4. Effects

**<a id="ki-055"></a>KI-055: New Gaussian blur starts at size 10.** Text or groups render soft. *Seen:* 0.0.69. *Workaround:* key it or set 0. *Status:* unknown. *Status update ():* fixed for design units: `blur` is px (a Gaussian sigma) and has no default; `none` takes it off. The size-10 default belongs to the stored parameter.

**<a id="ki-056"></a>KI-056: Glow `blend` > 0 hazes the layer even at `amount` 0.** Glow 1.2 on a small dot blew out to yellow. *Seen:* 0.0.69. *Workaround:* blend 0 except during pulses; 0.35 at size 14 stays orange. *Status:* changed by 0.0.72 — there blend 0 makes the glow invisible and amount drives burn; use the calibrated table in [effects/glow.md](effects/glow.md) (amount ≤ 0.8, blend 0.2 default). *Status update ():* `glow "radius colour strength mix"` states mix (default 0.2) and strength (default 0.8) in the string; the haze behaviour of a large mix is unchanged.

**<a id="ki-057"></a>KI-057: Rectangle `angle` does not rotate.** *Workaround:* transform `rotation`. *Status:* unknown. *Status update ():* fixed for design units: `rotate` turns any object clockwise.

**<a id="ki-058"></a>KI-058: Shape fill `softEdge` softens permanently.** *Workaround:* use `motionblur` for fast wipes and stretches. *Status:* unknown. *Status update (6b and one soft edge per shape):* `softEdge` is stated in px as the visible 10-90 % ramp, exact in Resolve and approximate in After Effects ([effects/soft-edge.md](effects/soft-edge.md)); it is the shape's one soft edge (fill and stroke together), keyable by name (verified: keyed-soft-edge-feather-blur-trim), so it can be animated to 0. A static soft edge still softens permanently.

**<a id="ki-059"></a>KI-059: Native pen default stroke covers the fill.** Blue marks were the default stroke over the intended fill. *Seen:* 0.1.4 Build18. *Workaround:* `stroke:none` explicitly. *Status:* fixed in helper policy (closed filled paths now disable the default stroke in `cc_scene`); native default unchanged.

**<a id="ki-146"></a>KI-146: `mask.invert` is accepted but does not change the render.** A plate masked by a 200 px text showed only inside the letters whether `mask.invert` was `on` on the mask, on the masked plate, or on both; `property.set` accepted every write. Controls list `Invert` with `binding: false`. Knock-out text and holes cannot be made with an inverted mask. *Seen:* 0.1.6 rev 1105, 2026-10-28, wiki measurement lab 3 (comp `T Soft masks`). *Workaround:* fake the knock-out with text in the background colour on a flat ground ([../../wiki/techniques/soft-and-inverted-masks.md](../../wiki/techniques/soft-and-inverted-masks.md)). *Status:* open.

**<a id="ki-147"></a>KI-147: Keyed stroke `Dash` and `Gap` do not animate.** On a dashed 6 px stroke, `shape.stroke.dashLength` keyed 10 → 60 px and `dashGap` keyed 10 → 60 px over 60 f rendered identical dash patterns at f0 and f59 (the first key's value), measured by pixel runs; controls list `dashGap` as keyframeable and do not list `dashLength`. Marching or growing dashes cannot be keyed. *Seen:* 0.1.6 rev 1105, 2026-10-28, wiki measurement lab 4 (comp `S Dashes`). *Workaround:* animate with `trim` or a moving mask window ([../../wiki/techniques/stroke-dashes.md](../../wiki/techniques/stroke-dashes.md)). *Status:* open.

**<a id="ki-159"></a>KI-159: Blur `clipping` none, domain and frame render the same, and a wide blur darkens the picture at the frame edges.** A horizontal blur (size 60, `lock` false, `sizeY` 0) on a full-frame adjustment layer over four flat colour stripes rendered the left edge at 135, 14, 37 (the stripe is 255, 26, 70) and the right edge at about 129 grey (the stripe is 240), with `clipping` set to `frame`, `none` or `domain`: identical pixels for all three. *Seen:* 0.1.6 rev 1105, 2026-10-28, Glitch round 3. *Workaround:* keep blurred bands short of the frame edges, or keep the blur small where it reaches an edge. *Status:* unknown.

## 5. Shapes and paths

**<a id="ki-060"></a>KI-060: Stored path placement is not the rendered geometry centre.** Translating baked custom paths by the stored default centre collapsed a cluster; a trim line landed over a CTA. *Seen:* 0.1.4 Build18. *Workaround:* measure actual bounds or use canonical point geometry. *Status:* open (FR-024).

**<a id="ki-061"></a>KI-061: Upscaling small paths with transform scale renders soft** (8–10×). *Workaround:* rebuild the path at size (scale points and handles), keep scale ≈1. *Status:* unknown.

**<a id="ki-062"></a>KI-062: Multi-part traced paths render from `shape.params.contours[].points`**, not `shape.params.points`; converting only one distorts the logo. *Seen:* 0.0.69. *Status:* unknown (behaviour).

**<a id="ki-108"></a>KI-108: Child drifts when the parent has an off-centre anchor and rotates.** *Seen:* 0.0.72. *Workaround:* parent to a pivot null at the joint ([drawing/rigging.md](drawing/rigging.md)). *Status:* open.

**<a id="ki-109"></a>KI-109: On comp instances the anchor does not compensate position, and short keys (`anchor`, `scale`, `blend`) are refused.** *Seen:* 0.0.72. *Workaround:* use `tr.e_tr_placement_<id>.*` and the camera maths in [maps/maps.md](maps/maps.md) §3b. *Status:* open.

**<a id="ki-153"></a>KI-153: `parent.assign` bakes the parent's pose at the playhead into the children; at parent scale 0 it writes scale 1,000,000.** Parenting keeps each child where it is drawn on the current frame. A pin's head, point and dot parented at f0 to a null whose `Drop - bounce` keys put it 302.4 px above its rest (0.28 × 1080) came to rest 302.4 px below the spot (head y 732.4 instead of 430). Parented at f0 to a bubble null keyed scale 0 → 1, the three children were written with `scaleX`/`scaleY` 1,000,000 and positions around 10⁵; every frame of that comp rendered as solid ink. *Seen:* 0.1.6 rev 1105, 2026-10-28, wiki cookbook lab 5 (comps `K Pin drop`, `K Speech bubble`). *Workaround:* parent before keying the parent, or `view.seek` to a frame where the parent is at its rest pose (position at rest, scale 1) first; or set `parentId` in the project file ([../../wiki/cookbook/map-pin-drop.md](../../wiki/cookbook/map-pin-drop.md), [../../wiki/cookbook/speech-bubble.md](../../wiki/cookbook/speech-bubble.md)). *Status:* the offset is behaviour (it keeps what you see); the scale-0 result is unknown.

**<a id="ki-110"></a>KI-110: `link.new` (ropes) only within one object.** Cross-object links refuse. *Seen:* 0.0.72. *Status:* open ([effects/basement-promote-ropes.md](effects/basement-promote-ropes.md)).

**<a id="ki-111"></a>KI-111: Gradient offset/angle/size/type are unavailable ("renderer does not read").** *Workaround:* key gradient start/end. *Seen:* 0.0.72. *Status:* open. Still so on 0.1.6 rev 1105, 2026-10-28: `gradientOffset` keyed 0 → 1 changed no rendered pixel with any `Repeat`; controls report `Repeat` as not read by the renderer and `Interpolate` as unavailable; start/end keys move the gradient ([../../wiki/techniques/gradients-in-motion.md](../../wiki/techniques/gradients-in-motion.md)).

**<a id="ki-112"></a>KI-112: `text.font.size` minimum is 0.01 W; a smaller value refuses (and rolls back the whole batch).** *Seen:* 0.0.72.

**<a id="ki-113"></a>KI-113: `preset.apply` takes one `id` (ignores `ids`); `preset.apply`, `param.raise`, `template.apply`, `comp.new`, `key.box`, `object.enter/exit` are not batchable.** *Seen:* 0.0.72. *Workaround:* `carvercat_run` per object.

**<a id="ki-114"></a>KI-114: No arrow primitive; `authoring.arrow` does not exist as a command.** *Workaround:* shaft path + 3-point chevron path (`scripts/maps/map_overlay.py`). *Seen:* 0.0.72.

**<a id="ki-115"></a>KI-115: Misleading receipts** — `object.new` "unchanged: it is already that length" on creation; empty `why` on many `preset.apply`; `undo_steps` 0 after `track.add`; `validate` false failures on template instances. *Seen:* 0.0.72. *Workaround:* trust `touched`/aliases and a look.

**<a id="ki-116"></a>KI-116: `look` region/object crops misdraw backgrounds; `max_edge` ignored inside `looks[]`.** *Workaround:* full-frame looks. *Seen:* 0.0.72.


**<a id="ki-137"></a>KI-137: A shape larger than the comp is cropped to a comp-sized box before its scale.** Ellipses 1800, 1920 and 2000 px wide (in a 1920 × 1080 comp) lost their top and bottom. A 2400 px circle and a 3800 px star rendered as rectangles, even when scaled down to 300 px on screen. *Seen:* 0.1.6 rev 1105, 2026-10-27. Paths too: 2400 px wide filled hill paths panned 60–240 px left left the frame's right edge uncovered (sky at x 1861–1919 by the end), while the same hills built from two 1200 px pieces covered it (wiki cookbook lab 7, comp `K Parallax wide`, 2026-10-28; [../../wiki/cookbook/parallax-layers.md](../../wiki/cookbook/parallax-layers.md)). *Workaround:* draw shapes no larger than the comp and scale them up with the transform (the Transitions pack draws 1000 px and scales 2.4–5×). *Status:* unknown.
## 6. Audio

**<a id="ki-150"></a>KI-150: A polygon's `angle` does not rotate it.** A 3-sided polygon (`shape.geometry.ngon`, 300 px) with `angle` 0, 45 and 90 rendered the same in `carvercat_look`, each with a corner pointing right; setting 90 with `property.set` on the live object (`src.e_src_shape_geometry_ngon_<id>.angle`) was accepted ("set", changed) and still drew the same picture. Five-point stars also start with a point to the right (their `angle` was not tried). The control is listed in `native-controls.json` (−360 to 360, not keyframeable). Same family as [KI-057](#ki-057) (rectangle `angle`). *Seen:* 0.1.6 rev 1105, 2026-10-28, building the Corporate Brand warning triangle and award star. *Workaround:* turn the shape with the transform `rotation` (+90 puts a point up; [../patterns/cb-safety-notice.md](../patterns/cb-safety-notice.md)). *Status:* unknown. *Status update ():* a polygon or star points right at `rotate` 0 and `rotate` turns it; its own `angle` is still stored and not drawn.

**<a id="ki-161"></a>KI-161: `key.set` on `path.geometry` accepts a key whose node count differs, and the shape then jumps instead of morphing.** On an 8-node blob keyed at f0 and f60, a middle key with a 6-node circle at f30 was accepted without a word. The render held the f0 shape through f30, jumped to the 6-node shape on f31 (ink 700 to 1218 px against 670 to 1258 on the centre row), held it to f59 and jumped back on f60; lint gave only a `speed_jump` note. With matching counts the same keys morph node by node. *Seen:* 0.1.6 rev 1105, 2026-10-28, wiki cookbook round 3 ([../../wiki/cookbook/blob-morph.md](../../wiki/cookbook/blob-morph.md)). *Workaround:* read the keys back with `key.list {key:"path.geometry"}` and count the points of every key; give every key the same contours and node count. *Status:* unknown (no check documented).

**<a id="ki-163"></a>KI-163: Lint reports a nested instance placed off the frame centre as `cropped_at_rest`, and `inspect probe` gives the child comp's frame as its size.** Three instances of 1920 × 1080 column comps (one card each, 440 × 600 px, at x 480, 960 and 1440) were all fully on screen, yet lint warned "only 75% on screen while still" (the two outer columns) and 89% (the middle one, 1.06 scale); `probe` reported w 1920, h 1080 for every instance. The instance's frame, not its content, is what is tested. *Seen:* 0.1.6 rev 1105, 2026-10-28, wiki cookbook round 3 (comp `K Pricing`; [../../wiki/cookbook/price-comparison-table.md](../../wiki/cookbook/price-comparison-table.md)). *Workaround:* measure the card from rendered pixels; judge with `carvercat_look`; centre the instance and put the offset inside the child comp when you need a clean lint. *Status:* unknown (compare [KI-144](#ki-144)).

**<a id="ki-065"></a>KI-065: No per-clip gain.** *Seen:* 0.0.69/0.0.70. *Workaround:* bake gain into WAVs. *Status:* fixed in 0.0.71 (`media.audio.gain`).

**<a id="ki-066"></a>KI-066: Resolve stored a different gain than requested** (2.3 dB apart). *Seen:* Resolve 21.1. *Workaround:* read back with `GetProperties()` and record it. *Status:* unknown.

**<a id="ki-067"></a>KI-067: 24 fps source audio on a 30 fps timeline rounds endpoints by one frame;** music ended one frame before video. *Status:* unknown.

**<a id="ki-068"></a>KI-068: Adding SFX exposed a pre-existing music overhang** (43 frames past picture). *Workaround:* assert timeline end after audio changes; trim fallback in [workflows/resolve-handoff.md §7](workflows/resolve-handoff.md#7-audio-timeline-end-and-trims). *Status:* unknown.

## 7. Export

**<a id="ki-070"></a>KI-070: `carvercat_render` output was opaque.** RGBA with alpha 255 everywhere, black ground. *Seen:* c423. *Workaround:* native `export.set` with `alpha:true`. *Status:* unknown.

**<a id="ki-071"></a>KI-071: `export.set` refuses everything for one unknown key.** Message "needs a `settings` object"; `export.plan`/`export.run` then refuse; flat args not accepted. *Seen:* 2026-09-30 (`collision` was unknown then; it is valid now). *Workaround:* pass only known keys inside `settings`. *Status:* open (error should name the key).

**<a id="ki-072"></a>KI-072: Blocking `export.run` outlived client timeouts** (45 s helper, 120 s relay window) while still rendering. *Seen:* c423 to 2026-09-30. *Workaround:* poll `export.status`, never replay. *Status:* fixed in exact-release 2026-10-01 (asynchronous durable jobs).

**<a id="ki-073"></a>KI-073: Intermittent glyph corruption in exported frames.** Jobs completed with correct counts and RGBA, but frames showed long triangles/lines, displaced strokes, missing fill, edge-reaching alpha, once a fully opaque white frame (alpha min=max=255); native look of the same frame was correct. Pausing transport, single-frame export and an app restart did not help; affected frames varied per attempt. *Seen:* clean (sourceDirty false), 2026-10-01. *Workaround:* none on that build; compare disk frames to native look. *Status:* fixed in a patched executable (base, sourceDirty true, builtUnixSeconds 1790848932): 1030 frames clean; not seen since. Root cause unconfirmed.

**<a id="ki-074"></a>KI-074: Live job JSON read raised `PermissionError` or returned partial JSON** on Windows. *Seen:* 2026-10-01. *Workaround:* bounded retry of the read. *Status:* unknown.

**<a id="ki-075"></a>KI-075: Render & Send never finished the handoff.** Durable 207-frame job complete, `error=null`, files decoded, but `deliver.status` stayed `phase=rendering`, `progress=null`, `receipt=null`, and no timeline clip was created; later Files exports also left the stale rendering phase. *Seen:*, 2026-10-09. *Workaround:* Files export + Resolve scripting import; do not replay. *Status:* open (not retested).

**<a id="ki-076"></a>KI-076: Recovery gaps.** Single-file (video) atomic restart/rename verification and fine-grained encoder sub-phases are not implemented. *Seen:* exact-release 2026-10-01. *Workaround:* inspect terminal status; never infer success from transport loss. *Status:* open.

**<a id="ki-077"></a>KI-077: Export nests output and writes hidden files.** `<dir>\<name>\<name>_00000.png` plus a hidden source snapshot (and progress JSON). *Seen:* 2026-09-30. *Status:* documented behaviour; FR-005 asks for a flat option.

## 8. Resolve transfer and scripting

**<a id="ki-080"></a>KI-080: Arabic word stagger reverses after Fusion transfer.** Native RTL reveal becomes left-first in Fusion; shaping and string are correct; the character-index delay mapping is wrong. *Seen:* 0.1.4 Build46, Resolve Studio 21.1.0.14, 2026-10-12. *Workaround:* mirror delay tables in the destination graph ([workflows/rtl-and-arabic.md §7](workflows/rtl-and-arabic.md#7-fusion-transfer-the-rtl-stagger-workaround)). *Status:* open (compiler fix pending).

**<a id="ki-081"></a>KI-081: Transfer scope stale after `comp.switch`.** Cached scope kept the previous comp's 207 frames; two sends were refused for straddling the next clip (no Resolve change). `deliver.plan` ready=true did not reveal it. *Seen:* Build46. *Workaround:* assert `transfer.scopes[comp].frames` equals the comp duration; opening Deliver refreshed it. *Status:* open.

**<a id="ki-082"></a>KI-082: Follower Order enum label misleads.** UI suggests Order 7; Order 7 removed the stagger; measured manual Order 6 works. *Seen:* Build46 / Resolve 21.1.0.14. *Status:* unknown.

**<a id="ki-083"></a>KI-083: Fusion scripting return values and names.** `BezierSpline.SetKeyFrames` returns `None` on success; `SaveSettings` needed `OrderedDict` in `__main__`; modifier names are normalised on import (`Obj6FollowerDelaybyCharacterPosition`). *Workaround:* read back keys; discover via `GetConnectedOutput().GetTool()`. *Status:* unknown (Resolve behaviour).

**<a id="ki-084"></a>KI-084: A resend overwrites destination graph edits** (RTL correction, speech delay tables). *Workaround:* save and reapply after each resend. *Status:* open.

**<a id="ki-085"></a>KI-085: Keyed compound path rendered one contour in Fusion** (a currency symbol became a dash). *Seen:* Build46. *Workaround:* several simple positive filled paths (six worked). *Status:* open (needs isolated reproduction).

**<a id="ki-086"></a>KI-086: Low-alpha icon tiles rendered opaque in Fusion,** covering line icons. *Seen:* Build46. *Workaround:* remove the tiles. *Status:* open (needs isolated reproduction).

**<a id="ki-087"></a>KI-087: Native and Fusion glyph widths differ** with the same resolved family. *Workaround:* set final gaps from the destination composite. *Status:* unknown.

**<a id="ki-088"></a>KI-088: PNG sequence FPS on import.** Imported at 24 fps on a 30 fps timeline; `SetClipProperty("FPS", 30.0)` did not apply (161 frames became 201); setting 30 when it already reads 30 can return False. *Seen:* Resolve 21.1, 2026-09-28/30, 2026-10-01. *Workaround:* read first; set the string `"30"`; assert return and readback before append. *Status:* unknown (Resolve behaviour; helper fixed).

**<a id="ki-089"></a>KI-089: `AppendToTimeline` `endFrame` is exclusive count.** `endFrame=n−1` gave n−1 frames (433 vs 434). *Workaround:* `endFrame=n`, assert placed duration. *Status:* unknown.

**<a id="ki-090"></a>KI-090: `Gallery.ExportStills` races and misorders.** Returned True before all PNGs were readable (`FileNotFoundError`); stale grabs mixed in on retry; generated names gave a non-chronological sheet. *Seen:* build, Resolve 21.1, 2026-09-30. *Workaround:* `ExportCurrentFrameAsStill` with explicit paths. *Status:* open (FR-017).

**<a id="ki-091"></a>KI-091: Still capture shows the wrong frame.** 0.2 s after a seek captured the previous overlay; timecode drifted during repeated captures (read 12:16 after seeking 5:01); first capture after timeline switches failed its assertion. *Workaround:* pause, settle (0.75–4 s), assert timecode before and after. *Status:* unknown.

**<a id="ki-092"></a>KI-092: Inactive timelines report false track flags and missing audio properties.** *Workaround:* activate before reading. *Status:* unknown.

**<a id="ki-093"></a>KI-093: No timeline-item edge trim in Resolve 21.1 scripting.** *Workaround:* delete-and-reappend fallback. *Status:* unknown.

**<a id="ki-094"></a>KI-094: `MediaPool.DeleteClips` returned False** for unused entries; removal not confirmed. *Status:* unknown.

**<a id="ki-095"></a>KI-095: Resolve refuses an adjustment layer with no effects.** *Seen:* 0.0.69. *Status:* unknown.

**<a id="ki-096"></a>KI-096: `GetSourceStartFrame()` is source-rate, not `sourceIn`.** Baseline comparisons need `GetLeftOffset()`. *Status:* unknown (Resolve behaviour).

**<a id="ki-126"></a>KI-126: Fusion transfer carrier arrives at 30 fps on a 24 fps timeline and plays 1.25× fast.** All sends share one carrier media-pool item; it read `FPS 30.0` after a fresh send. *Seen:* 0.0.82, Resolve Studio 21.1, 2026-10-22. *Workaround:* after each send read the carrier's FPS and `SetClipProperty("FPS", "24")` (string), then read it back. *Status:* open.

**<a id="ki-127"></a>KI-127: Some transferred comps land one frame short.** A 173-frame comp placed as 156–328 and a 109-frame comp as 667–775; six other comps placed at full length. *Seen:* 0.0.82, 2026-10-23. *Workaround:* assert each placed clip's start/end against the comp length; keep the last frame empty. *Status:* open.

**<a id="ki-128"></a>KI-128: Transfer reports `connected:false` after a fresh launch** until `resolve.refresh` is run, even with Resolve open on the right timeline. *Seen:* 0.0.82. *Workaround:* `resolve.refresh`, then check `carvercat_state transfer` shows the timeline before sending. *Status:* behaviour.

**<a id="ki-129"></a>KI-129: Transferred comps keep positions as fractions of frame height, so they don't adapt to another aspect.** A 1080×1920 caption comp placed on a 1080×1080 timeline rendered at full pixel size but with y squashed: a three-item stack and two-line blocks overlapped. *Seen:* 0.0.82 + Resolve Studio 21.1, 2026-10-23. *Workaround:* build a separate comp per aspect (copy the project JSON, set scene `height`/`timelineHeight`, remap each `position` y in pixels; see [resolve-handoff §5](workflows/resolve-handoff.md#other-aspect-ratios-from-one-edit-verified-2026-10-23)). *Status:* behaviour. *Status update (0.1.8):* the stored file still keeps fractions (the format changes at B1); in design units every position is px from the top-left, and `layout.fit` / `scene.apply` re-lay a scene for another comp size.

**<a id="ki-130"></a>KI-130: `Timeline.DeleteClips(list)` can return None and delete nothing.** Seen on a caption track with eight Fusion carriers (also earlier on a duplicated timeline). One item per call returned True every time; the same call with several items also worked on other timelines. *Seen:* Resolve Studio 21.1, 2026-10-22/23. *Workaround:* check the item count after deleting; fall back to one `DeleteClips([item])` per script call (a loop in one call hit the MCP's 10 s script limit). *Status:* unknown (Resolve).

**<a id="ki-131"></a>KI-131: Playhead seeks are ignored on the Edit page and the next still can be stale.** `SetCurrentTimecode` called while on the Edit page left the playhead where it was; stills exported in the same call as the seek sometimes showed an earlier frame. *Seen:* Resolve Studio 21.1, 2026-10-23. *Workaround:* `OpenPage('color')`, seek and read back the timecode in one call, then `ExportCurrentFrameAsStill` in the next call. *Status:* unknown (Resolve).

## 9. Performance

**<a id="ki-100"></a>KI-100: Duplicate clip IDs across timelines slow the UI.** A duplicated assembly with the same audio/nested IDs took UI work from ~20 ms to ~115 ms per frame and starved audio (`carvercat_state.audio.starved` rising). *Seen:* 0.0.69, Windows. *Workaround:* re-prefix every ID in the copy (`clip_N` → `clipv_N`, including property keys) in JSON, reopen ([performance.md](app/performance.md)). *Status:* unknown.

**<a id="ki-101"></a>KI-101: Hundreds of round trips per comp.** About 150 relay calls for one 434-frame comp. *Status:* fixed by `carvercat_batch` (≤256 steps; 48 → 2 requests in a benchmark; no render speed-up claimed).

**<a id="ki-102"></a>KI-102: Resolve Color-page stills cost about 1 s each.** *Status:* unknown.

## 10. UI

**<a id="ki-105"></a>KI-105: Export blocked the editor and hid progress.** *Status:* fixed in exact-release 2026-10-01 (background worker, Deliver opens, seek 0 ms during export).

**<a id="ki-106"></a>KI-106: Relaunch from another working directory exited.** Launching c423 from the chat's directory exited; from the app repository it worked. *Seen:* c423. *Status:* unknown.

**<a id="ki-107"></a>KI-107: Project Navigator connector coordinates were wrong** in native review before release. *Seen:* 0.1.4 Build75 candidate, 2026-10-05. *Status:* fixed in that candidate (covered by a usage-attachment check).

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
| <a id="fr-026"></a>FR-026 | People (not only agents) can select a Resolve clip, open its native source, edit, then **Place new**, **Replace selected clip** or **Update existing Fusion clip** with target preview, stale-target checks, truthful outcomes and no automatic replay; UI, MCP, schema and skills share one implementation | open (user requirement, parked) |
| <a id="fr-027"></a>FR-027 | Track kind in `carvercat_list` | done (list v2) |
| <a id="fr-028"></a>FR-028 | Availability gate for declared controls that do not materialise | partly (`available` flag) |
| <a id="fr-029"></a>FR-029 | One-page docs: coordinates, aliases, stagger proxy paths, derived cache fields, which params apply to which kind | partly ([mcp-essentials.md](app/mcp-essentials.md) units) |
| <a id="fr-030"></a>FR-030 | Relay returns ASCII-safe JSON escapes | unknown |
| <a id="fr-031"></a>FR-031 | Async/long-deadline export client | done (async jobs) |
| <a id="fr-032"></a>FR-032 | Compact batch receipts (summary only, opt-in per-step detail) and a documented JSON import format for agent-written comps | open |
| <a id="fr-033"></a>FR-033 | Autosave / crash recovery of the open document | open |
| <a id="fr-034"></a>FR-034 | A native number text: a keyframeable value with format (prefix, thousands separator, decimals) for counters, instead of masked digit columns | open (found building the SaaS UI pack) |
| <a id="fr-035"></a>FR-035 | `inspect lint` honours masks (visible area only) so masked counters and reveals lint clean | open (found building the SaaS UI pack) |
| <a id="fr-036"></a>FR-036 | A packaged build loads Library packs only from its own bundle (`install_channel::work_root` seals `roots_to_search` to `Contents/Resources`): no user Library path, no `CARVERCAT_RESOURCE_ROOT`, working-directory packs ignored. Add a user Library folder (e.g. under the data dir) that installed builds also scan, so packs like Motion Patterns, SaaS UI and Kinetic Typography install without editing the app bundle | fixed in Carvercat 0.1.8 (not in 0.1.7): [Installing a pack](../patterns/README.md#installing-a-pack) |
| <a id="fr-037"></a>FR-037 | Text can use the fonts shipped in the app bundle (Open Sans, Inter, Bricolage, JetBrains Mono), so templates have at least one font family that renders identically on every install | fixed in 0.1.8 for Carvercat's own text; other apps still need the font installed |
| <a id="fr-038"></a>FR-038 | `inspect qc` loop seam compares geometry too (positions, rotations, scales of frame 0 against the frame after the last), not only mean brightness ([KI-140](#ki-140)) | open (found building the wiki labs) |
| <a id="fr-039"></a>FR-039 | `inspect lint` `text_too_small` scales its default with the comp height (18 px at 1080 lines → 36 px at 2160) ([KI-143](#ki-143)) | open (found building the wiki labs) |
| <a id="fr-040"></a>FR-040 | `inspect lint` and `look` overlay optional platform safe zones for 9:16 (top ≈ 14%, bottom 20–35%, right button column), since text in those zones currently raises no finding | open (found building the wiki labs) |
| <a id="fr-041"></a>FR-041 | `inspect lint` recognises intentional nulls (an invisible object that is a parent of others) and does not report them as the error `never_visible` | open (found building the wiki labs) |
| <a id="fr-042"></a>FR-042 | `inspect lint` on a master checks text inside nested instances (or offers a recursive option): 29 showcase and recipe masters linted clean with `contrast:true` while their template comps, linted on their own, had 56 `low_contrast` findings ([../../wiki/workflow/lint-and-qc-audit.md](../../wiki/workflow/lint-and-qc-audit.md)) | open (found in the wiki audit) |
| <a id="fr-043"></a>FR-043 | Time remap for nested instances and video clips: a keyframeable source time (or speed) so footage and nested scenes can play in slow motion, freeze or speed ramp; today `sourceIn` only offsets the start and is not keyframeable ([../../wiki/cookbook/slow-motion-hold.md](../../wiki/cookbook/slow-motion-hold.md)) | open (found writing the wiki cookbook) |
| <a id="fr-044"></a>FR-044 | A QR-code object (text in, crisp modules out, error-correction level, quiet zone) for end cards; a hand-built QR from squares can't be generated or verified natively ([../../wiki/cookbook/end-card-with-url.md](../../wiki/cookbook/end-card-with-url.md)) | open (found writing the wiki cookbook) |
| <a id="fr-045"></a>FR-045 | Path morphs through the agent tools. **Settled 2026-10-28 (cookbook round 3):** it works. The renderer morphs `path.geometry` keyframes per node when contour and point counts match (the app's own fixture), and the agent tools set them: `object.path` draws the shape, `view.seek` and `key.set {key:"path.geometry", value:{closed, points:[{x,y,inX,inY,outX,outY,corner}]}, easing}` key it, `key.list` reads it back; on 0.1.6 rev 1105 an 8-node blob keyed f0/f30/f60 moved every node to the mean of its two keys at the midpoint within 1 px ([../../wiki/cookbook/blob-morph.md](../../wiki/cookbook/blob-morph.md), [../../wiki/techniques/morphing.md](../../wiki/techniques/morphing.md)). Remaining gap: a mismatch in node count is not refused ([KI-161](#ki-161)) | closed (works; the gap is KI-161) |
| <a id="fr-046"></a>FR-046 | A noise / film-grain effect (animated per-frame grain with amount, size and monochrome option, usable on an adjustment layer), so a texture overlay doesn't need imported footage; no native effect generates noise today (the effect caps are blur, glow, shadow, motion blur, fill, stroke, colour, transform, crop, outline, expand, trim) | open (found writing the wiki cookbook) |
| <a id="fr-047"></a>FR-047 | Audio-reactive control: a way to drive a scale, opacity or position from the level of an audio clip (an audiogram bar, a pulse on the kick) instead of keying every beat by hand ([../../wiki/cookbook/sound-wave-bars.md](../../wiki/cookbook/sound-wave-bars.md)) | open (found writing the wiki cookbook) |
| <a id="fr-048"></a>FR-048 | Timeline markers with names (chapter markers) that can be added, moved and listed by command, shown in `carvercat_state` and exported (for chapter lists or a Resolve marker hand-off). Today only the comp In/Out marks exist (`comp.mark.in`, `comp.mark.out`, `comp.mark.clear`) | open (found writing the wiki cookbook) |
| <a id="fr-049"></a>FR-049 | Subtitle import: read an SRT or VTT file into timed text clips (one per cue, start and length from the timecodes, one style), instead of one text clip per cue by hand ([../../wiki/cookbook/timed-captions-by-hand.md](../../wiki/cookbook/timed-captions-by-hand.md)) | open (found writing the wiki cookbook) |
| <a id="fr-050"></a>FR-050 | Text on a path: a text laid along an open or closed path with an offset along the path that can be keyframed. Today letters are separate texts placed and turned by hand ([../../wiki/cookbook/text-on-a-curve.md](../../wiki/cookbook/text-on-a-curve.md)); `text.outline` converts a text to Bezier contours but does not bend it | open (found writing the wiki cookbook) |
