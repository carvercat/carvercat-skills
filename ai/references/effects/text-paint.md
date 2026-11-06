# Text paint: fill, outline, hollow type

**Verified** (text-outline-hollow): hollow outline type: `fill` `#ffffff00` (alpha 0), `stroke` navy, outline thickness 0.03 on 240 px bold type gives clean outlined letters. On 0.0.72 the same hollow type was verified with `text.fill.color` alpha 0, `text.outline.color` navy and `text.outline.thickness` 0.03.

| control | design key | notes |
|---|---|---|
| fill colour | `fill` (CSS colour, alpha allowed) | a gradient is refused on text; the stored paint takes one ([fill-and-gradients.md](fill-and-gradients.md)) |
| outline colour | `stroke` (CSS colour) | |
| outline width | none: stored `src.e_src_text_outline_<id>.thickness`, 0 to 0.2 | RELATIVE TO THE TEXT SIZE (not the frame, not px): 0.02 to 0.04 for display type. The band straddles the glyph edge: an opaque fill hides its inner half. `strokeWidth` on a text is refused (`not-settable`, it is for shapes) |
| outline blur / glow | stored `text.outline.blur`, `glow` | outline-only softening (declared; not verified) |
| per-text relative transform | stored `text.relative.*` | used by stagger slots |

```json
{"command": "property.set", "args": {"id": "#t", "key": "fill", "value": "#ffffff00"}}
{"command": "property.set", "args": {"id": "#t", "key": "stroke", "value": "#1b2a6b"}}
{"command": "property.set", "args": {"id": "#t", "key": "src.e_src_text_outline_clip_3.thickness", "value": 0.03}}
```

Read the path from `param.list {id, match: "outline"}`.

## Rules
- **Always set `fill`.** New text rendered red on 0.0.72; scene nodes and `object.new {style}` take it in the same call.
- Hollow type needs `fontSize` of about 70 px or more and a bold `fontWeight`; thin weights plus outline look broken.
- Outline plus fill in different colours is the sticker/arcade look; keep the thickness at 0.04 or less.
- Legibility over busy imagery: a soft drop shadow (`"0 0 17px #00000080"`, [shadow.md](shadow.md)) or a pill behind beats a thick outline.
- For the outline to reveal with a stagger, connect its own opacity slot (`stroke.opacity`): fill opacity alone leaves the outline visible ([stagger.md](stagger.md)).
