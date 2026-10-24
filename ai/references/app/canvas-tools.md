# Canvas tool families and option popups

The native app has one Canvas-owned top tools surface. Selection, Shapes, Draw
and View reveal their variants on hover; following families move within reserved
space while the contextual settings anchor and Canvas remain fixed. Text is a
single tool. Narrow layouts expose All tools; its popup retains every family
member and applicable option group, with scrolling in short windows.

Read `carvercat_state.canvasTools` for the actual families, shortcuts, readiness,
active member, mode, visible control rectangles and open popup controls. The
canonical registry supplies that state, rendering and input; do not infer tools
from a screenshot or assume the HTML mockup contains the entire production set.

Use `carvercat_run` with the existing `tool.arm`, `tool.marquee`, `tool.pivot`,
`tool.default`, point-edit and `path.combine` commands. Switching tools finishes
an open Pen draft and clears point selection when leaving point-edit tools.
Unavailable Zoom and Knife remain unavailable; Blade remains on the timeline.

New commands:

```json
{"command":"tool.mode","args":{"mode":"mask"}}
{"command":"tool.mode","args":{"mode":"normal"}}
{"command":"tool.options","args":{"group":"settings","open":true}}
{"command":"tool.options","args":{"group":"points","open":true}}
{"command":"tool.options","args":{"group":"pathfinder","open":true}}
{"command":"tool.options","args":{"group":"tools","open":true}}
{"command":"tool.options","args":{"group":"tools","open":false}}
```

Mask requires a selected target; refusal does not change mode. Option groups
must apply to the current tool/selection. Opening a popup is workspace UI state,
not a document edit; it does not move the Canvas or reserve extra height.
Popups close through Escape, their close button, or a consumed outside click.
F6 focuses the toolbar; arrows/Tab navigate and Enter invokes the focused
control. The original A/S/P/T/V family shortcuts and 1..n member choices remain.

Selection options preserve Touch/Enclose and multi-selection pivot choices.
Point options preserve Corner, Smooth, Break, Join and Remove, including Join
availability and point-count readouts. Pathfinder preserves the four Boolean
operations and Release compound. Properties and next-object defaults remain
editable through the existing Properties system; there is no added Appearance
group. Existing Canvas/Deliver, Composition Settings and bottom Canvas controls
are retained.

Align/Distribute actions and Pencil Softness were proposal controls in the
browser mockup. This migration does not implement those future features or
expose inert substitutes. Text/stroke alignment properties remain available.

## Complete Canvas panel polish

The Canvas toolbar, pasteboard/composition viewport and bottom controls now
share one thin outlined rounded shell. Deliver content uses the same protected
interior. Contextual options are right-aligned behind a divider; Composition
Settings precedes the far-right labelled Deliver/Canvas action. Smaller controls
retain the original icon set and command behavior.

Hover widths and sibling positions animate over 180ms with continuous reversal;
contraction keeps visible variants until they leave the clipped animated region.
Reduced motion uses 90ms and Off snaps. `canvasTools.familyProgress`,
`familyRects` and `toolsRegion` expose current visible geometry; do not assume
an expanded family is at its final width immediately. Popups still overlap
without changing Canvas bounds. Use semantic tool commands instead of raw input.
