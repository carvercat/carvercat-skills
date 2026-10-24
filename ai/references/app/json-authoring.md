# Writing comps straight into the project JSON

Read this when a build is too big for MCP batches (hundreds of objects, many comps, long films), or when you need exact, continuous motion across many sub-comps. Verified on Carvercat 0.0.72 (20 Oct 2026). The reference implementation is [`../../scripts/motion/json_author/`](../../scripts/motion/json_author/README.md).

## Standing rule: edit the project file directly

**Direct project-file editing is the default way to build and change Carvercat scenes.** Write the clips, keys and effects straight into the `.carverproj`, then reopen it in the app. It is the fastest route by a wide margin: one write and one reload, however many objects. MCP batches took about 10 minutes per caption scene; Python builder scripts that send hundreds of MCP calls were the slowest of all.

Where direct editing doesn't fit, use the closest option **for that step only**, then go back to the file:

| Situation | Use instead |
|---|---|
| You need measured geometry (shaped text widths, path bounds) before writing | A short MCP batch with `observe` or `carvercat_authoring geometry` on throwaway objects, then delete them |
| You need to check the installed font resolves | `carvercat_authoring fonts` |
| A one-line live tweak while the user is working in the app | `carvercat_run` / a small batch (don't force-reload under them) |
| Sending to Resolve, saving, switching comps, looking | MCP (`resolve.target`, `resolve.send`, `edit.save`, `comp.switch`, `carvercat_look`) |
| A structure you haven't written in JSON before | Build one in the app by MCP, `edit.save`, read its JSON, then copy that shape |

How to write the JSON:

- Write it yourself (Edit/Write on the file). Small helper calculations (widths, frame maths) are fine. Don't build a script that drives the MCP one call at a time.
- For whole films, a generator that writes the JSON in one go ([`json_author`](../../scripts/motion/json_author/README.md)) is still direct file editing and is allowed. A 2,000-clip project with 31 comps builds in seconds this way.

Safety around the reload:

1. `edit.save` in the app first, so the file on disk has everything (the app does not autosave; unsaved MCP work was lost on a disconnect, [KI-122](../known-issues.md#ki-122)).
2. Copy the file to a timestamped backup before writing.
3. Write, then `edit.open {path, force:true}`, `comp.switch`, `carvercat_look`.
4. Finish with `edit.save` so the app normalises the file.
5. Tell the user not to edit in the app during a force reload.

Older guidance kept for context:

- MCP batches remain the fallback for edits, single scenes and anything the file route can't express.
- JSON-authored clips render, animate and stay editable: shapes, text, keys, effects, nested comps and audio.
  - This replaces the older advice never to clone clips in JSON. That advice holds only for copying a clip with its ids. Fresh clips built from a template with new ids work.

## Loop

1. Run the script. It loads the project, replaces its `timelines` with the generated comps, and writes the file.
2. In the app:
   - `edit.open {path, force:true}`;
   - `comp.switch {index:N}`;
   - `look`.
3. Repeat. Keep the generator as the source of truth: don't hand-edit in the app between builds, because the next build overwrites it.
4. Finish with `edit.save` so the app normalises the file.

## Units and semantics (verified)

| Thing | Rule |
|---|---|
| Clip start/length | `left` and `width` are **pixels**: frame × `ppf` (4). |
| Keyframes | **Clip-local** frames: subtract the clip's start. |
| Keys inside a nested instance | Measured in **source time**: local frame + `sourceIn`. |
| Position | Fraction of the comp width, **y up**: `[x/1920, 1 − y/1080]`. It is the geometry **centre**. |
| Anchor | Pivot in half-sizes (−1 left/bottom, +1 top/right). In raw JSON the position does **not** move to compensate: the shape stays centred on its position, and scale/rotation pivot about the anchor. Grow from the top edge: `anchor [0, 1]` + scale y. |
| Width/height | Fraction of the comp width (both). |
| `cornerRadius` | Maximum 0.5. radius px = cr × min(w, h) / 2, so a full pill is impossible. Use a 2-point path with a round-capped stroke. |
| Text size | 1.0 = 1146.24 px em. Minimum 0.01. Align `left` puts the left edge at x; y is the cap-height centre. Rethink Sans widths from PIL match the app within about 1%. |
| Custom ease | On the arriving key: `{"easing":"Custom","customEase":[x1,y1,x2,y2]}`. |
| Stagger effect | `{id:"e_fx_stagger_<clip>", cap:"stagger", by, order, amount, amountMode:"each", seed, connected:[paths]}`. |
| Audio clip | Type `media` with `media{id,path,kind}`. It needs a matching entry in the project `media` pool. Gain is at `src.e_src_media_audio_<id>.gain`. |
| Parenting | `parentId` on the child. A non-nested child's screen position = parent_pos + s·(child − parent_static_pos). **Nested-comp instances ignore their parent**: bake camera moves into their own keys. |

## Continuous motion across sub-comps

- Split long scenes into short subscenes (1.5–2.5 s each) and nest them back-to-back in a master.
- So the cuts can't be seen, drive every moving property from **one master-time curve**, and cut it per window:
  - `Curve(spec).window(a, b)` returns clip-local keys for master frames a..b;
  - it splits each cubic-bezier ease at the window edges exactly (de Casteljau), so speed and position match on both sides of a cut.
  - Make sure the window holds the value **before the first key** when that key falls inside the window. A missing hold makes the property ramp from the window start. This was a real bug, fixed in `cc.py`.
- **World/camera:** build one big world in pixels (app window, other windows, cards) and move a camera null through named poses `(scale, world_point, screen_point)`. Parent ordinary objects to the camera, and bake the camera into nested instances (they ignore parents).
- **Persistent UI state** (a card the pointer drew, a panel that opened) is a function of master time, drawn in every subscene where it is live.

## Measuring text for a direct edit

- Latin text and numbers: measure with PIL straight from the font file (`ImageFont.truetype(path, round(size × 1080 × 0.597)).getbbox(txt)`). This avoids the app's font fallback ([KI-123](../known-issues.md#ki-123)). The app drew Almarai Latin about 5–8% wider than PIL's box, so leave about 15 px of slack before adjacent glyphs, e.g. a currency sign.
- Arabic needs shaping, which PIL lacks without raqm. Measure in the app (a `dry_run` batch with `observe` geometry), after confirming `carvercat_authoring fonts` resolves the family.
- Clips are identified by `label`; generated word clips have none. Find existing clips by label before replacing them, and keep ids unique by bumping `scene.clipCounter`.

## Pitfalls

- Bash heredocs over about 8 KB fail with E2BIG on the linked PC. Write big files in parts.
- Positive `tracking` on JSON-written plain text rendered scrambled. Leave tracking out ([KI-117](../known-issues.md#ki-117)).
- `parent.assign` (MCP) uses the **first** selected object as the parent ([KI-120](../known-issues.md#ki-120)).
- `authoring.arrow` exists inside batches even though the command list does not show it.

## Showing the app's own UI (screen recreations)

Check the live app before drawing a UI state, and keep a short note of what it really does:

- **Curve mode:**
  - Clicking a track's key icon makes it an amber dot, and the **track itself expands**.
  - The clip shrinks to a slim name strip.
  - A `▾ POSITION` group row shows white keyframe diamonds.
  - A near-black curve lane labelled "Position · Position X" holds thin teal curves and a dashed centre line.
  - The tracks below are pushed down. It is not a floating editor panel.
- **Send to DaVinci Resolve methods:** Resolve Studio, Free · Lua receiver, Copy Fusion · manual.
