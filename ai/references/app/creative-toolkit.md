# Creative toolkit ? current contract

Start with ai/SKILL.md. Use Python's stdlib client and native Carvercat objects; Pillow is needed only for image-based test evidence.

## Connect and bind

Add the active skills repo's ai/scripts directory to sys.path. Client() uses the current carvercat-mcp-editor.pid, verifies its live process and opens loopback connections. CARVERCAT_MCP_ENDPOINT explicitly selects another endpoint file. Never silently fall back from a stale current editor to an old document. Client.bind(commit=..., comp=..., project=...) checks optional build and comp constraints; inspect its returned state and the current project before edits. Client.stdio(exe, scratch_state_dir) starts a separate headless document for tests and never connects to the user's editor.

Client.run raises on MCP errors/refusals instead of printing and continuing. Client.batch checks expected_revision and expected_document (project path/editing scope) and applies a bounded atomic native plan. A timed-out write raises OutcomeUnknown: inspect before further writes. There is no mutation replay. Client.look returns all written image paths plus all text metadata; unchanged images return an empty files list, never a stale file as fresh evidence.

## Pixel authoring

```python
from cc_client import Client
from cc_scene import Scene, Box, title_pair
client = Client()
identity = client.bind()
scene = Scene(client)
title_pair(scene, "A clear idea", "Native editable graphics",
           box=Box(240, 160, 1440, 320))
scene.apply()                       # one native batch, one undo step
scene.fit("title", Box(240, 160, 1440, 180))
scene.rebind()                      # deliberate acknowledgement after known changes
scene.anchor("title", Box(240, 160, 1440, 180))
scene.apply()
scene.entrance(["title", "subtitle"], start=0, frames=12, stagger=4)
scene.apply()
scene.review("review.png", frames=(0, 8, 20, 60))
client.run("edit.save", path="ABSOLUTE_JOB_PATH/design.carverproj")
scene.rebind()
scene.manifest("scene-map.json")
```

Coordinates/boxes are comp pixels, top-left/y-down. Times are explicit comp frames. Text size is nominal font em pixels, converted using the app's authoringUnits coefficient; visible glyph height depends on the resolved font. Shape dimensions divide by comp width, including height. Colors accept #RRGGBB/#RRGGBBAA and convert using the existing BT.709 transfer contract. Scene does not change native rendering or preferences.

Every creation has a stable semantic name. Scene.ids and the sidecar manifest map those names to native IDs. A manifest validates comp scope and live ID/name pairs on reopen; it is not a replacement for the saved project. Scene.apply refuses a changed revision; rebind is an explicit acknowledgement, not an automatic retry.

## Layout and components

fit uses native shaped bounds and a minimum font size, not character-count estimates. flow supports row/column, gap, padding, start/center/end cross alignment and RTL row order. anchor positions native bounds; check_zones tests safe areas and explicit subject rectangles. baseline uses native point-text bottom alignment for the last baseline, not glyph ink bottoms; paragraph text is refused. Animated rotation/relative transforms need sampled review rather than assuming static baseline alignment.

Components: title_pair, caption, number_highlight, card_group, icon_label and image_card. Preserve original native icons by registering their existing IDs with Scene.ids; icon_label arranges their labels rather than replacing icon artwork. image_card takes a stable existing project-pool media ID, measures cover scale, places a native image and creates a rounded mask. Asset import is a separate deliberate step because media.import may auto-place clips. Fit and lay out component text against real bounds before accepting it. RTL captions default to Almarai ExtraBold; verify actual font notes, never infer support from the family string.

Use entrance for coordinated scale/opacity or keys for custom curves. Repeated frames are deterministically deduplicated; a single key gets no invalid handle. envelope describes explicit fade/hold/exit. extend_hold deliberately replaces placement opacity and clears the obsolete relative-text opacity channel; use it only when that reset matches the intended design. Other relative/stagger/fill channels require inspection, not a blanket visibility reset.

## Revisions and review

Scene.patch changes only named properties/keys. It does not clear other keys; replace_keys deliberately replaces one channel. For full scenes, spec accepts objects keyed by semantic name with kind/start/duration/properties/keys. All scene plans are bounded by 256 native steps; split large jobs at deliberate component checkpoints. Atomic batches reject external side effects such as saving, exporting and Resolve actions.

Review uses the existing native inspect/looks. Inspect actual returned images, not just success flags. Tests and geometry do not establish creative taste, full-video playback or Resolve equivalence. Save native sources; verify exported samples independently before delivery. Presets/templates remain optional creative assets and are not automatically applied.

## Verification and measurement

Run ai/scripts/test_cc_toolkit.py for error/identity/geometry tests. In the app repo, tools/d75_verify.py exercises isolated native title/cards/Arabic revisions, rollback, undo/reopen and preview outputs. tools/d75_benchmark.py runs equal scenes through the old selection loop and the new batch path and compares sampled pixels. Pass --exe, --skills and --output explicitly. Results are task-specific efficiency evidence, not an overall creativity score.

## Observed native film field test

Field-tested on a 58-element homepage build (word/character stagger, all eight effect types, three content comps in a 22-second master). Inspect/reuse existing stagger cards and avoid writing unchanged timing fields until the recorded no-op classification gap is corrected. Validate actual native parameter availability rather than treating the declaration catalog as complete live bindings. For baked custom paths, measure effective geometry centres before calculating a translation; do not assume the stored default centre is that geometry centre. Use native font notes to validate the active family name.


## Native discovery and revisions

`client.tool("carvercat_authoring", mode="controls", id=object_id)` returns actual paths, typed values, ranges, units and keys, plus unbound declarations. `writable`, `requires_promotion`, `promotable` and `absorbed_by` have distinct meanings: a stored opacity folded into a colour picker can be writable without its own promotable row. Unsupported controls must be identified before mutation. Scene.bindings uses this surface. Native availability does not establish Resolve visual parity; Resolve transfer still has renderer calibration limits.

Font discovery: use mode="fonts", query="Inter" or family/style/sample to obtain the actual resolved face and fallback flags. Scene.text records resolution, and require_font=True refuses substitution before queuing a partial text creation. Font resolution is cached per family/style and non-ASCII glyph set. Review receipts include resolutions.

Geometry: mode="geometry" returns measured bounds/geometry_centre and separate placement/anchor values. Scene.measure now observes the full pending plan through an atomic dry-run, so creation, styling, bounds placement and key replacement can be prepared together. The native document, revision and dirty state are restored; provisional IDs are never adopted. Coordinates are active-scene pixels. Exit a group to inspect its enclosing group/instance in parent space. Scene.position writes the placement anchor; Scene.place_center places measured artwork. Bounds placement on an animated position requires a deliberate curve revision rather than silently changing an ineffective static reference.

Scene.replace_keys can run with queued edits. It removes obsolete queued key operations for that object/channel, removes existing native keys, and queues the replacement in the same guarded plan. Refusal rolls back all steps. OutcomeUnknown still never triggers automatic replay.

```python
with scene.component("Header") as header:
    header.rectangle("Plate", Box(160, 70, 1600, 100), fill="#242424", radius=.25)
    header.text("Brand", "carvercat", x=380, y=120, size=48,
                family="Bricolage Grotesque", style="ExtraBold", require_font=True)
scene.apply()
# Repeating the same component preserves IDs. Only named fields change.
with scene.component("Header") as header:
    header.text("Brand", "A revised title", size=52)
scene.apply()
```

The namespace (`Header / child`) is an explicit ownership boundary, visible as ordinary layer names. Duplicate names and incompatible child types refuse. Default removal policy keeps omitted children; remove_missing=True deletes only omitted unique children within that namespace. retain(child) prevents removal. Existing effects are discovered and reused; repeated matching effects require an explicit entry. Native geometry paths can be updated through an editable path.geometry track without recreating their object. Manifests and save/reopen preserve stable IDs. Linked native comp instances remain linked; updating a definition uses its active scope.

Closed filled paths now deliberately disable the default stroke. Open paths retain the native stroke unless overridden. Explicit strokes remain available. This is helper policy, not a claim that native default paint is broken.

Parented placement: native geometry exposes local_bounds, parent-composed bounds, pivot_pixels and placement_basis. place_bounds/place_center invert this basis to reach a measured point under rotated/scaled parents. Zero-scale parents refuse. These coordinates are in the active scene; group and comp navigation changes that coordinate space, so keep scope explicit.

## Speech schedules and measured destination review

For spoken-word Stagger, keep timeline onsets separate from comp-local frames and the entrance duration. Reject an ASR onset that spans a pre-speech pause when user review and audio/cue evidence disagree; correct the affected onset without shifting later words automatically. Native uniform gap approximates irregular spacing. On the measured early pre-release Fusion route, editable Follower character-delay curves carry the irregular schedule plus temporary RTL correction; save/read back those curves and reapply them after a native resend. Do not claim that the saved native source alone retains the destination schedule.

For multi-part line icons, measure the whole assembly, choose a uniform maximum size and translate scaled parts around that assembly's center. Center text/unit groups by their combined measured widths. Verify actual destination font metrics, layer visibility and spacing after transfer; native bounds are insufficient proof of visible or pixel-equivalent output.

Check the fresh active source/comp and transfer scope before each individual replacement. When the user manually changes footage mid-session, preserve the original snapshot and admit only the explicitly authorized differences in the working baseline. Final proofs must include unchanged user tracks/neighbors, the saved graph and actual rendered samples.
