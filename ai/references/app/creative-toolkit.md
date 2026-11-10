# Creative toolkit: the Python helpers in design units

Start with [../../SKILL.md](../../SKILL.md) and [design-units.md](design-units.md). Standard library only (Pillow only for image evidence). The same call patterns without Python are in design-units.md. The app also ships its own official helper, `carvercat_py`; `ai/scripts/cc_client.py` and `cc_scene.py` are the transport and scene builder this skill keeps (outcome-unknown protection, no mutation replay, endpoint discovery) on top of the same calls.

## Connect

```python
import sys; sys.path.insert(0, "ai/scripts")
from cc_client import Client
c = Client()                                  # the current editor (reads its endpoint file; refuses a stale one)
c = Client.stdio(exe, state_dir, resource_root=app_checkout)   # a private headless document; never the user's editor
```

`Client.stdio` gives fresh preferences, data and cache folders under `state_dir`, loads the font list, and needs `resource_root` (or `CARVERCAT_RESOURCE_ROOT`) for a host built from source. A timed-out write raises `OutcomeUnknown`: inspect the document before any further write; nothing is replayed. A refusal raises `Refused` with `.code`, `.receipt["why"]`, `.receipt["valid"]` and `.example`; pass `check=False` to `run` to read a refusal as data.

## Build a scene (verified: example_creative.py, test_cc_toolkit.py)

```python
from cc_scene import Scene, Box, gradient
s = Scene(c, width=1920, height=1080, fps=30, duration="4s")
s.rectangle("plate", Box(160, 760, 900, 200), fill="#1a1c26", radius=24)
s.text("name", "Alex Morgan", box=Box(210, 775, 820, 100), size=88, weight=700)
s.keys("plate", "x", [(0, -900), (18, 160)], ease="cubic-bezier(.16,1,.3,1)")
s.stagger("name", by="words", each="100ms",
          keyframes=[{"at": 10, "props": {"opacity": 0, "y": 799}}, {"at": 26, "props": {"opacity": 1, "y": 775}, "ease": "ease-out"}])
s.apply(dry_run=True)                       # validated whole; nothing changes
reply, pre = s.apply(preflight="resolve")   # one undo step, then what carves exactly / approximately / not at all
```

- Boxes are px, top-left, y down. `size` is a true em in px. Leave `family` out for the app's bundled default.
- Scene ids come from the names (letters, digits, `_` and `-`; other characters become `-`); `s.target("Big title")` is the selector `#Big-title`. Apply the same scene again and only differences change.
- `entrance(names, frames, stagger, scale, rise)`, `envelope(name, start, hold_end, end, fade)`, `keys`, `stagger` write plain keyframes. Effects and paint are style keys: `blur`, `glow`, `shadow`, `grain`, `directional_blur`, `soft_edge`, `trim_path`, `paint`, `transform`.
- Feedback with no render: `measure`, `fit` (`text.fit`), `flow` (`layout.stack`), `align`, `check_zones` (`measure.overlaps within`), `contrast`, `review(path, frames)` (lint plus a look). Read the image.
- Components: `with s.component("Header") as h: h.rectangle(...)` gives scene ids `Header-Plate`, so repeating updates instead of duplicating.
- `title_pair`, `number_highlight`, `caption`, `card_group`, `icon_label` are small layouts in design units.
- Paths: `c.path("M 100 600 C ...", stroke=..., strokeWidth=...)` (or a `type: "path"` node with `d` in a scene document).
- Procedural style for one-off scripts: `cc_build` (`use(c)`, `card`, `text`, `new`, `stagger_caption`), same design keys.

## Renamed or removed from the earlier toolkit

`linear_hex`, `Scene.rebind`, `manifest`, `fx_set`, `fx_keys`, `remove_effect`, `image_card`, `Scene.path`, `Scene.position`, `place_center`, `patch`, `replace_keys`, `extend_hold`, revision `Box` helpers on y-up centres, and `Client.bind`'s scene pointer: the scene id is the identity, a scene applies as a whole and idempotently, and effects are style keys. `Scene.text(x, y)` was a centre; it is now the top-left of the layout box, or use `box=`.

## Verification

`ai/scripts/test_cc_toolkit.py` (offline tests always; live tests with `CARVERCAT_EXE`) and `ai/scripts/verify_examples.py` (every call sequence in these guides). Both start a private headless document and never touch an open app.
