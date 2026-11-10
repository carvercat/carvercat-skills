# Effects, paint and transforms through MCP

Read [design-units.md](design-units.md) first. All effects, paint and transforms are design keys on `property.set`, `key.set`, `anim.set`, `object.new {style}` and a scene node's `style`; the per-effect guides with verified recipes are in [../effects/README.md](../effects/README.md). `carvercat://schema/design` is the live table (range, default, animatable, carve status) and `carvercat_describe` lists what the selected object has.

```python
s.blur("card", 8)                                  # blur: "8px", a Gaussian sigma (edge ramp 2.563 x 8 px)
s.glow("path", radius=14, color="#ffcc00", strength=0.6, mix=0.2)
s.shadow("card", x=0, y=12, blur=16, color="#00000061")   # y is DOWN; blur is a sigma
s.grain("film", 0.08, 1.5, softness=0.4, colour=0.1)       # grain: "0.08 1.5px softness=0.4 colour=0.1 seed=1" (put it on an adjustment layer)
s.directional_blur("panel", 160, 0)                         # a streak: "160px 0deg", angle counter-clockwise from the right
s.set("card", "filter", "blur(4px) grain(0.2 2px) brightness(1.2)")
s.apply(preflight="aftereffects")
```

## Fill, stroke, gradients

`fill` and `stroke` are CSS colours (`#RRGGBB`, `#RRGGBBAA`, `rgb()`, `hsl()`, names), `none`, or gradients: `linear-gradient(90deg, #ff7a00 0%, #1b1b1b 100%)`, `radial-gradient(circle 200px at 25% 75%, ...)` (stops in `%`; the app blends in linear light for you; After Effects keeps only the first and last stop, and says so). `cc_scene.gradient([(0, "#31566A"), (100, "#B48EAD")], angle=90)` builds the string. `strokeWidth` px, `strokeAlign` inside|center|outside, `strokeLinecap`, `strokeLinejoin`, `strokeDasharray` (`"24 12"`, `dotted`: the model lays dashes out once as a whole count; the reply's `dashEffective` says what is drawn). Text takes `fill` as a colour; text gradients and the outline width are still on the stored path ([../effects/text-paint.md](../effects/text-paint.md)).

## Position, transform, animation

`x`, `y` are the top-left of the object's box in px, y down; `rotate` clockwise degrees; `scale`; `opacity`; `transformOrigin` as CSS. `anim.set` writes `keyframes`, tweens (`to`/`from`/`fromTo`), a GSAP-style `stagger` and a `motionPath`; `key.set {at, ease}` writes one key. A key's `ease` shapes the segment leaving it; keyframes with no `ease` are linear. Every shape and effect number keys by its design name: `blur`, `glow`, `dropShadow`, `brightness`, `contrast`, `softEdge`, `feather`, `borderRadius`, `strokeWidth`, `trimStart`, `trimEnd`, `trimOffset`, `fontSize`, `letterSpacing`, `lineHeight` (verified: keyed-soft-edge-feather-blur-trim); `key.remove {key, at}` removes one by name. A keyword or count (`strokeLinecap`, `mixBlendMode`, `fontWeight`) is refused with the reason. See each effect guide.

## Stagger text and path trim

Text stagger is `anim.set {from|to|keyframes, stagger: {target: chars|words|lines, each|amount, from: start|end|center|edges|random, ease}}` on a text object, or `stagger` on a scene node. `trimStart`, `trimEnd`, `trimOffset` are `%`; a trim starts at a fixed point (shapes: the right of the centre, counterclockwise on screen; paths: the first point). Preserve the authored open or closed path and the fill/stroke choice: a reveal on a filled shape is not a stroke reveal.

## Limits

Declared is not drawn: `carve.preflight` and the carve status in each reply say what each host does. `saturate`, `hue-rotate`, `invert`, `grayscale`, `sepia` and `backdrop-filter` are refused with the reason. `contrast` is approximate in Resolve and unsupported in After Effects.
