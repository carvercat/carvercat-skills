# Project Navigator

Tested against the native 0.1.4 review build, 2026-10-05.

Read `carvercat_state.navigator` before navigating. It includes the current
lineage and graph nodes, each with an exact `target`. Pass that target unchanged
to `carvercat_run`:

```json
{"command":"workspace.navigator","args":{"action":"open","data":{"parent":"<comp ID>","instance":"<clip ID>","groups":[]}}}
```

Use the actual target returned by state; the IDs above are placeholders.
`{"definition":"<comp ID>"}` opens the shared composition for editing.
A usage target returns to its parent, restores its group path and selects that
specific clip. A reused composition appears once with a count. Expand its
usages with `action:"usages", data:{"id":"<comp ID>"}` and read state again.

Workspace actions use the same command: `move` with `slot:top|between|below`,
`mode` with `mode:path|map`, `resize` with `height`, `expand` with `on`, `pan`
with pixel deltas `x,y`, `center`, and `reset`. Placement and mode persist
independently in workspace preferences. They do not dirty or enter the project.
The graph uses fixed-size, automatically aligned nodes: there is no zoom action.

In the UI, single-click selects a graph node; double-click or Enter opens it.
Drag empty graph space to pan. Drag the header grip to a dock target, or click
the grip for the placement menu. The bottom edge resizes a docked Navigator.
Tab opens Map only with Canvas, Timeline or Navigator focus; Escape returns to
Path. Ordinary input-field Tab traversal remains available.

Re-read state after navigation or document edits. Clip IDs can repeat across
compositions; a clip ID alone cannot identify a usage. Do not substitute a
composition definition for an exact usage when per-instance context matters.

Side columns (8 October 2026): use `workspace.column` with `column:left|right`
and either `width` in logical pixels or `collapsed:true|false`. Omitting both
inspects the column. Expanded bounds are 320-520; dragging below 296 collapses
to a 42px rail and reaching 344 restores. Explicit restore keeps the previous
width and panel mask. `workspace.panel` with `on:true` opens only that rail
icon's panel. The final expanded panel points left and closes the whole column,
regardless of its stack order; folded sibling headers do not count as bodies.
These are workspace preferences, never document edits.
