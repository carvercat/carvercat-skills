# json_author: write Carvercat comps straight into a `.carverproj`

`cc.py` is the generator used for a 40-second, 22-subscene, 2,000-clip film (verified on 0.0.72). The how-to is in [../../../references/app/json-authoring.md](../../../references/app/json-authoring.md).

- `cc.py`:
  - `Doc` / `Comp` / `Obj` builders: rect, ellipse, ngon, star, path/line, text, nested comp, audio, null, adjustment, parent;
  - keys, custom eases, effects (glow, shadow, motion blur, blur, trim, stagger);
  - `Curve` (master-time curves that split exactly across subscene windows);
  - `textw()` (Rethink Sans widths, about 1% from the app).
- `templates.json`: clip templates taken from MCP-made clips. One per kind: rect, ellipse, polygon, star, path, text, textplain, adjust, nest, audio.
- `RethinkSans.ttf`: Google Fonts, SIL Open Font License. Used only by `textw()` for measuring.
- `assets.json` (optional, beside `cc.py`): named vector contours for `Comp.asset()`.

Loop:
1. `python3 build.py` (your script: `Doc(path)`, comps, then `doc.save()`).
2. In the app: `edit.open {path, force:true}`.
3. Look at the result.
4. Run `edit.save` once at the end.
