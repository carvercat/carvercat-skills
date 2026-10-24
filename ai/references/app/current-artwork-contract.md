# Native artwork contract (October 2026)

Read alongside live resources, not as a replacement for their schemas. This guide
supersedes the historical font list and stale-preview advice in api-gotchas.md.
Source verification does not certify a different installed build or Windows device.

## Identify the actual editor

Verify version, document path, scene pointer,
comp dimensions, frame rate and revision through MCP state before any mutation.
On macOS, discover the installed Carvercat app locally and use the executable
inside its Contents/MacOS folder for explicitly isolated Client.stdio work.
Do not launch a separately built verification binary as the user's editor. Windows
installed packaging can be MSIX/alias or a fixed Dev executable: inspect the actual
installation, do not invent a universal path or convert distribution implicitly.
Client() uses the current editor endpoint pointer and validates PID and handshake;
a stale current pointer refuses instead of selecting an unrelated legacy editor.
Client.stdio(exe, owned_state_dir) is a separate scratch document and preference
profile. An example's edit.new is permitted only in that owned scratch process.
No runtime or project clearing follows merely from a discovery failure.

Read resources/list then current carvercat:// command, authoring and parameter
resources. No-selection describe is a selection contract, not the capability
catalog. For Windows scripts use UTF-8 JSON through stdin/structured arguments;
never interpolate artwork text into PowerShell commands. Preserve Unicode and
literal quotes. Client/Scene handle protocol encoding and typed values.

## Mutation, receipts and observation

Bind stable IDs, exact scope and revision; use guarded batches with expected
revision/document. Scene.target(name) returns a stable ID or {$ref:name} for
pending creation. edit.group supports a single member and creation aliases;
explicit order is the exact selected ID set back-to-front, one member per source
track. Omitted order preserves native ordering. Inspect masks and child IDs after
grouping; do not fabricate entry IDs. Refused later batch steps restore the original
document and redo branch. Dry-run IDs cannot be retained after rollback.
Known refusal stops dependent work. Unknown outcome is inspected, never blindly
replayed, especially export, transfer, save and updater restart. Observations do
not justify scope changes. Preview pixels and saved editable geometry are both
required; success receipts alone are insufficient.

Project bins use native bin.* discovery and comp.move_to_bin/copy/cut/paste
contracts from the live command list. Use comps arrays of stable comp IDs. Cut
moves definitions; copy mints new IDs. Cross-document stale clipboard intents
refuse; nested definition references must survive save/reopen. clip.stack moves
sibling dedicated tracks in the current scope, retaining clip IDs/timing/masks;
shared multi-clip tracks, cross-scope and locked crossings intentionally refuse.

## Paint, geometry and fonts

Use carvercat_authoring controls/paint groups to distinguish physically bound,
panel-visible and explicitly promoted controls. Promote only the intended absent
control, then set its native path. RGB/RGBA arrays are finite numeric 3/4-channel
values, HDR RGB is allowed, alpha stays 0..1. Gradient stops, positions, points and
mode follow live declarations; a malformed color object is not a color. Rounded
stroke requires explicit cap/join controls; unchanged global defaults are intentional.
Scene.paint and maintained control helpers cover native formats; inspect current
receipts rather than patching generated JSON to imitate a row.

Scene.path points and optional handle offsets are comp pixels, y down; it converts
both to normalized native coordinates. Duration is frames and track is the exact
existing zero-based video track; native creation validates room and locks before
minting. There is no temporary 90-frame clip followed by a trim. Use comp.duration
for authored comp duration and existing object.new placement for primitives.

Only enabled publicly installed OS/user fonts are project fonts. Bundled UI fonts
are not guaranteed project choices. Query carvercat_authoring mode=fonts with family,
style and the actual Unicode sample; inspect effective family/style/glyph coverage.
Mac and Windows fallbacks can differ. Scene.check_font(require=True) demands exact
resolution, while ordinary authoring accepts the platform's installed fallback.
Never automatically install a font. Do not reuse the old Poppins/Montserrat/etc list
as proof. Font-file hashes/index/axes explain the resolved face; no bytes transfer.

text.outline is an explicit native authoring conversion, not automatic Resolve
font transport. It snapshots effective shaping/layout and current-frame paint into
editable closed contours, retaining timing/transforms/effects/masks and inert
original-text provenance. Counters and complex scripts require native image review.
Unsupported raster glyphs or richer animated/shading features refuse. text.restore
refuses edited curves unless force:true deliberately discards those changes.

path.trace is a seeded connected foreground assist for cropped reference images,
not automatic scene interpretation. Source image stays unchanged. Choose source
pixel seed, color/alpha mode, threshold and pixel tolerance; boundary leaks refuse
unless explicitly allowed. Inspect closed contours and holes, split decoration,
then shade/mask separately. path.simplify works on one static editable path and
measures sampled bidirectional comp-pixel deviation; this is not an analytic bound.
Animated/live Boolean/locked/overcomplex cases refuse. Trace is outside atomic batch.

## Native visual acceptance

carvercat_look dedup follows rendered bytes and scope/request identity. force:true
resends equal pixels, not a fix for stale authored state. Use contentMode metadata
to tell composite, isolation and hidden objects apart. Compare reference sequences
with compare_space=comp (full reference cropped to the effective comp ROI) or view
(already cropped). Square aspect expansion affects the effective ROI. Match exact
frame, output size, background and alpha before claiming a difference; use folders
of f00000.png or supported {frame} patterns, not an unsupported single-file contract.
Nested definition/media/reference changes invalidate the relevant rendered result.

Inspect actual entrance/hold/exit and saved/reopened native pictures; retain IDs,
geometry and source assets. Exaggerated PNG zoom alone is not an AA defect. Existing
export scale/supersampling contracts and real output dimensions must be discovered,
then measure alpha edges, render cost and matched-size comparisons. Do not duplicate
an authoring comp merely to fake an export-control gap. Independent decor, sensible
hierarchy and footage fit remain human visual criteria; bounded geometric checks
cannot certify creative quality. Actual Windows output/UI/MCP and font matrices
remain platform qualification tasks when no device is available.

## File navigation and updater

file-picker.mode is shared Carvercat/System preference. System means native file,
folder or save chooser for the actual operation. Explicit-path MCP remains suitable
for scratch work. Cancellation/stale chooser receipts preserve the document and
save/export drafts; Save As adopts a path only after successful write.

app.update status exposes the one-control updater state. Check → Download → Update
(prepare) → Restart captures the dirty project/history/redo/workspace/drafts before
replacement. Active/unknown external jobs defer. Do not bypass signature/publisher
checks or replay external transfer on restart. Update availability depends on the
release channel of the installed build.
