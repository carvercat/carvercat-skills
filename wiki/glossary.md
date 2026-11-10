# Glossary

Motion-design terms as this wiki uses them, with the Carvercat name where one exists. Names and values are the
**design units**: px from the frame's top-left with y down, `rotate` in degrees clockwise, CSS colours and easing,
`opacity` 0 to 1, time as frames, `"1.5s"` or `"500ms"`; the full list is `carvercat://schema/design`. Frames are at 30 fps unless stated.
Old stored names (`cap.param` such as `transform.placement.scale`) are named only in each page's "old names" note.

| Term | Meaning | In Carvercat |
|---|---|---|
| Accent | The one colour, word or move that carries emphasis in a frame. | One accent colour per frame; see [visual hierarchy](design/visual-hierarchy.md). |
| Anchor | The point an object scales and rotates about. | `transformOrigin`, as in CSS: `"50% 50%"` centre, `"0% 50%"` left edge, `"50% 100%"` bottom edge. Old: `anchor` in half-sizes. |
| Animatic | A timed sequence of rough frames with scratch sound, used to approve timing before animation. | [Animatics](workflow/animatics.md). |
| Anticipation | A small opposite move before the main action. | [Anticipation](principles/anticipation.md). |
| Arc | A curved path of motion. | Position keys interpolate in straight lines; arcs come from a rotating pivot null or a carrier null ([arcs](principles/arcs.md)). |
| Back curve | An easing that overshoots its target once. | `ease: "cubic-bezier(0.34, 1.56, 0.64, 1)"` ≈ 9.8% overshoot ([exaggeration](principles/exaggeration.md)). |
| Bar / phrase | 4 beats / 4 or 8 bars of music. | [Beat sync](sound-and-timing/beat-sync.md). |
| Beat | One pulse of the music; frames per beat = fps × 60 ÷ BPM. | 120 BPM = 15 f at 30 fps. |
| Blend mode | How a layer's colour combines with what is below it. | `mixBlendMode`, the 16 CSS names, all computed in linear light ([blend modes](techniques/blend-modes.md)). |
| Blocking | Showing only key poses as jumps to judge timing. | `ease: "hold"` ([pose to pose](principles/straight-ahead-and-pose-to-pose.md)). |
| Breakdown | The in-between pose that defines how a move travels (its arc, its overshoot). | An extra key between start and end. |
| Bumper / ident | A short branded clip between programmes or sections. | [Broadcast packages](genres/broadcast-packages.md). |
| Comp | A composition: a timeline with its own size, rate and length. Nested comps appear as instances. | `comp.new`, `comp.format`, `comp.place`; the unit of Carvercat work. |
| Contrast ratio | Luminance ratio between text and background (WCAG): 4.5:1 body, 3:1 large. | `carvercat_inspect {mode:"lint", contrast:true}` ([contrast](design/contrast.md)). |
| Crossfade | One object fading out while another fades in at the same place. | Two opacity keys in opposite directions. |
| Custom ease | An exact cubic-bezier easing. | `ease: "cubic-bezier(x1, y1, x2, y2)"` on the key the segment leaves ([slow in and out](principles/slow-in-slow-out.md)). |
| Damping ratio (ζ) | How quickly a spring's swings die out: low wobbles, 1 arrives without overshoot. | Baked springs: ζ 0.5 ≈ 16% overshoot ([springs](principles/springs.md)). |
| Decibel fade | A level change keyed in dB. | `media.audio` `Level (dB)` keys interpolate linearly in dB, so fades sound late ([audio](sound-and-timing/audio-in-carvercat.md)). |
| Draw on | A stroke that appears along its length. | `trimEnd` `"0%"` → `"100%"` ([line drawing](techniques/line-drawing.md)). |
| Ease in | Accelerating (slow start, fast end). `ease-in`; the model's old `Ease in` is a gentler t² (quad in). | For exits. |
| Ease out | Decelerating (fast start, slow end). `ease-out`; the model's old `Ease out` is 1 − (1 − t)² (quad out). | For arrivals. |
| Easing | How a move spends its frames: where it is fast and where slow. | The key's `ease`, a CSS string: `linear`, `ease-in`, `ease-out`, `ease-in-out`, `cubic-bezier(...)`, `steps(...)`, `spring(...)`, `hold` ([names](principles/easing-reference.md#names-used-in-this-wiki)). |
| Exaggeration | Pushing a move past realism so it reads. | Overshoot, squash, anticipation. |
| Expo out | A strongly front-loaded deceleration, about 83% of the travel in the first quarter. | `ease: "cubic-bezier(0.16, 1, 0.3, 1)"`. |
| Faux 3D / 2.5D | Depth made from 2D layers, gradients and offsets. | [Faux 3D](techniques/faux-3d.md). |
| Flash | A pair of opposing luminance changes; more than 3 a second is a seizure risk. | `carvercat_inspect {mode:"qc"}` ([photosensitivity](accessibility/photosensitivity.md)). |
| Follow-through | Parts that keep moving after the main body stops. | Offset keys 2–5 f ([follow-through](principles/follow-through-and-overlap.md)). |
| Graphic-safe / title-safe | The inner frame area where text is guaranteed visible. | Lint `outside_graphics_safe`; `carvercat_look {overlay:["safe"]}`. |
| Hold | (1) A period where nothing moves. (2) A key easing that jumps. | `ease: "hold"` on a key keeps its value until the next key. |
| Hook | The first 1–3 s of a social video that must stop the scroll. | [Social ads](genres/social-ads.md). |
| Instance | A placed copy of a nested comp. | Shows nothing after its inner comp ends; ignores parenting ([nested comps](techniques/nested-comps-and-time.md)). |
| Key / keyframe | A stored value at a frame. | `anim.set` / `key.set` over MCP, `at` in frames, `"1.5s"` or `"500ms"` from the start of the object. |
| Kinetic type | Typography that moves with meaning. | [Kinetic typography](techniques/kinetic-type.md). |
| Linear light | Colour values proportional to physical light, before the display curve. | Carvercat stores and blends colours in linear light and displays them with the BT.709 curve ([colour](design/colour-psychology.md)). |
| Lint | Carvercat's automatic mistake finder. | `carvercat_inspect {mode:"lint"}`: reading time, text size, safe area, overlaps, speed jumps, jitter, contrast (opt-in). |
| Lower third | A name and role caption in the lower part of the frame. | Templates in most packs, e.g. `Lower third - two boxes`. |
| Mask / matte | A shape that limits where another object is visible. | `mask: "<mask id>"` on the object to cut, or `clipPath` ([masking](techniques/masking.md)). |
| Match cut | A cut joined by a shared shape, colour or movement. | [Match cuts](techniques/match-cuts.md). |
| Morph | A shape changing into another. | Keyframeable geometry ([morphing](techniques/morphing.md)). |
| Grain | Fine random texture added to a picture: film grain, tape or digital noise. | `grain "0.25 1.5px"` (amount, size, `softness=`, `colour=`, `held`, `seed=`), keyable; on an adjustment layer it grains everything below ([film grain](techniques/film-grain.md)). |
| Directional blur | A streak along one angle, used for speed. | `directionalBlur "40px 30deg"` (length, angle counter-clockwise), keyable ([directional blur and speed](techniques/directional-blur-and-speed.md)). |
| Motion blur | Smearing of fast-moving objects. | `effect.add {cap: "motionblur"}`: `motionblur.shutter` 0–360, `motionblur.samples` 2–64 (no design key yet). |
| Negative space | Empty space that shapes and focuses a composition. | [Negative space](design/negative-space.md). |
| Null | An object that is only a transform, used as a parent or pivot; it draws nothing. | `object.new {kind: "null"}`; no width, height or opacity ([null object](techniques/null-object.md)). |
| On twos | Each pose held for two frames. | `Hold` keys every 2 f; Retro pack presets. |
| Onion skin | Several frames ghosted into one image. | `carvercat_look {onion:true}`. |
| Overlap | Parts of one object moving at slightly different times. | Offset keys or Stagger Text. |
| Overshoot | Going past the target before settling. | `inspect curves` reports `overshoot_pct`. |
| Parallax | Near layers moving faster than far ones. | [Parallax](techniques/parallax.md). |
| Parenting | One object's transform carrying another's. | `parent.assign` (the active, last-selected object is the parent on 0.1.6). |
| Pose to pose | Animating key poses first, then in-betweens. | [Pose to pose](principles/straight-ahead-and-pose-to-pose.md). |
| Preset | A saved animation for one object. | `preset.apply {name, id}`; `.carverpreset`. |
| Probe | A per-frame table of an object's centre, size, rotation, scale and opacity. | `carvercat_inspect {mode:"probe"}`. |
| Reading time | How long text must hold to be read. | Lint: 17 characters a second, at least 5/6 s ([reading time](sound-and-timing/reading-time.md)). |
| S-curve | Ease in and out. Measured as 3t² − 2t³. | `ease: "cubic-bezier(0.333333, 0, 0.666667, 1)"`; CSS `ease-in-out` is a similar but different curve. |
| Safe area | Margins kept clear for overscan or platform UI. | [Vertical and safe areas](../ai/references/craft/vertical-and-safe-areas.md). |
| Secondary action | A smaller motion reacting to the main one. | [Secondary action](principles/secondary-action.md). |
| Settle | The frame after which a value stays within 0.5% of its end. | `inspect curves` `settles_at`; `inspect timing` `settles`. |
| Shutter angle | Exposure per frame as an angle: 180° = half a frame. | `motionblur.shutter`; smear = speed × angle ÷ 360 ([motion blur](techniques/motion-blur.md)). |
| Softness (shadow) | The blur of a drop shadow. | `dropShadow` blur, in px, a Gaussian σ: `"0 8px 6px #0000004d"` ([shadow and glow](techniques/shadow-and-glow-in-motion.md)). |
| Source in | How far into a nested comp an instance starts playing. | `sourceIn` on the instance clip, in frames. |
| Spacing | How far an object moves between frames. | `inspect probe`. |
| Squash and stretch | Deformation that shows impact and speed, keeping volume. | `scale` `[x, y]` with `transformOrigin` on the contact edge, e.g. `"50% 100%"`. |
| Stagger | The same animation on several items, each later. | Stagger Text effect; offset keys for objects ([stagger systems](techniques/stagger-systems.md)). |
| Soft edge | A shape's fill or stroke fading out at its edge. Its size is the visible 10 to 90% ramp, in px. | `softEdge` in px (one per shape, fill and stroke together; `strokeSoftEdge` is its old name), keyable ([soft edge and feather](techniques/soft-edge-and-feather.md)). |
| Feather | The soft edge of a mask: the mask shape's own soft edge, in px. | `feather` in px on a shape that is a mask (the Soft edge row, icon 555); exact in Resolve, approximate in After Effects ([soft edge and feather](techniques/soft-edge-and-feather.md)). |
| Staging | Presenting one idea clearly. | [Staging](principles/staging.md). |
| Storyboard | Key frames of a film in order with notes. | [Storyboards](workflow/storyboards.md). |
| Style frame | A finished-quality still that sets the look. | [Storyboards](workflow/storyboards.md). |
| Template | A saved group of coordinated objects. | `library.place` + `template.apply`; becomes a nested comp. |
| Timing | How many frames a move takes. | [Timing and spacing](principles/timing-and-spacing.md). |
| Trim | Showing only part of a stroke's length. | `trimStart`, `trimEnd`, `trimOffset`, in %. |
| Vestibular | Relating to the inner-ear balance system; large motion can make some people ill. | [Motion sensitivity](accessibility/motion-sensitivity.md). |
| Wipe | A transition where an edge sweeps across the frame. | [Transitions pack](../ai/patterns/transitions.md). |
