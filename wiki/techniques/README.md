# Techniques

How the recognisable moves of motion graphics are built, and how to build them in Carvercat.

| Page | One line | Key facts measured in Carvercat |
|---|---|---|
| [Masking and reveals](masking.md) | Windows and edges that reveal content | `mask` on the object to cut (old `mask.make {ids:[mask, content]}`); lint is mask-blind, use `mode:composite` |
| [Parallax](parallax.md) | Depth from different layer speeds | planes at 1 : 2 : 4 speed read clearly |
| [Shape morphing](morphing.md) | One object changing shape | polygon `sides` steps; star `Depth` and corner radius morph smoothly |
| [Kinetic typography](kinetic-type.md) | Words that move with meaning | 5 words, 4 f gap, 14 f move = 30 f |
| [Line drawing and trim paths](line-drawing.md) | Strokes that draw themselves | expo draw-on is half drawn 2 f in |
| [Stagger systems](stagger-systems.md) | Gap, order and spread rules | orders forward/reverse/centre/edges/random |
| [Seamless loops](looping.md) | No jump at the seam | key the closing value on frame = comp length; qc seam check is brightness-only |
| [Match cuts](match-cuts.md) | Cuts joined by a shared shape | land both sides with two `expect` sentences |
| [Rhythm editing](rhythm-editing.md) | Cutting to music | shots on beat frames; qc found no flash at 2 cuts a second |
| [Null object](null-object.md) | A parent that draws nothing: pivots, rigs, cameras | a null at (910, 150) swings a hanging sign about (960, 200); no width, height or opacity |
| [Camera-like moves in 2D](camera-moves-2d.md) | A camera null moves the world | children scale about the null's centre |
| [Faux 3D](faux-3d.md) | Extrusions, shading, turns | a gradient's `at X% Y%` is y-down |
| [Motion blur](motion-blur.md) | Smear on fast moves | added smear = speed × shutter ÷ 360 (57 px at 180°, 120 px/f) |
| [Animating scale vs size](scale-vs-size.md) | Magnify or resize | scale 3× tripled an 8 px stroke to 23 px |
| [Trails and echoes](trails-and-echoes.md) | Fading delayed copies | 4 copies, 2 f apart: an 8 f trail |
| [Gradients in motion](gradients-in-motion.md) | Sheens and drifts | key start/end; `gradientOffset` changes nothing (KI-111) |
| [Blend modes (measured)](blend-modes.md) | 16 modes, all in linear light | mid-grey 0.18 × 0.5: Multiply 70, Screen 196, Overlay 104 |
| [Animating tracking, word and line spacing](text-spacing-animation.md) | Spacing as motion | tracking stays centred; word spacing is not rendered |
| [Soft-edged and inverted masks](soft-and-inverted-masks.md) | Feathered wipes, knock-outs | 60 px `feather` = 61 px ramp; `mask: {ref, invert: true}` renders |
| [Soft edge and mask feather](soft-edge-and-feather.md) | `softEdge` (one per shape) and `feather` in px: the visible 10-90% ramp | 8 / 24 / 60 px rendered 8.2 / 24.0 / 60.6 px; exact in Resolve, approximate in After Effects |
| [Shadow and glow in motion](shadow-and-glow-in-motion.md) | Lift, power-on, pulse | `dropShadow` x y in px, blur is a sigma; a `glow` radius of 11.5 px reaches about 25 px |
| [Nested comps and time offsets](nested-comps-and-time.md) | Reuse, offsets, scenes as comps | an instance shows nothing after its inner comp ends; ignores parents |
| [Wiggle, shake and jitter](wiggle-and-jitter.md) | Deliberate noise vs accidental jitter | lint warns on ±1 px every-frame reversals; ±2 px and up passes |
| [Dashed and dotted strokes](stroke-dashes.md) | Routes, boundaries, selections | round caps add the stroke width to each dash; dash/gap keys do not animate |
| [Text outlines (measured)](text-outlines.md) | Outline width and alignment | band ≈ thickness × size × comp width; inside renders like centered |

Lab project: [labs/](../labs/README.md).
