# Wiki labs

Small Carvercat projects used to measure the values quoted on `verified` wiki pages. Built on Carvercat
0.1.6 (rev 1105) by writing the project file directly, then opened headless and measured with
`carvercat_inspect` (`probe`, `curves`, `timing`, `lint`, `expect`, `composite`, `qc`) and checked by eye with
`carvercat_look`. No media; text uses Rethink Sans (install it first,
[KI-136](../../ai/references/known-issues.md#ki-136)). Open a lab with `edit.open {path, force:true}`
(or File > Open), `comp.switch` to a comp, and re-run the same inspect calls to reproduce a number.

All comps are 1920 × 1080 at 30 fps unless named otherwise. Positions below are comp pixels, y down.

## Reading the labs in design units

The `.carverproj` files keep the stored format (fractions of the frame, linear colours, y-up centres, counter-clockwise rotation) until the
project format changes (B1); they are not converted. Open one and ask for the design units instead: `edit.open {path, force: true}`, `comp.switch {index}`,
then `scene.get` returns the open comp as one scene document in px, y down, CSS colours and easing, with every number the pages quote. For example (checked on
a headless Carvercat 0.1.8 build):

| Stored in the lab | Design units | Where |
|---|---|---|
| `shape.fill.softEdge` 0.03125 | `softEdge` 60 px (`feather` 60 px on the mask) | `T Soft masks`, measurement lab 3 |
| shadow Offset X 0.01, Y −0.01, Softness 0.01 | `dropShadow` `"19.2px 10.8px 8.3136px #000000"` | `F Shadow glow`, measurement lab 3 |
| shadow Softness 0.02, y −0.006 (a toast) | `dropShadow` `"0 6.48px 16.6272px #00000040"` | `K Toast`, cookbook lab 7 |
| glow Size 10, Amount 0.4, Blend 0.2 | `glow` `"11.5px 0.4 0.2"` | `F Shadow glow` |
| blur Size 60 | `blur` `"69px"`; Size 24 is `"27.6px"` | `K Background drift`, `K Focus in` |
| text tracking 1.0 → 1.6, size 64 px | `letterSpacing` `"0px"` → `"64.31616px"` | `T Spacing`, measurement lab 3 |
| line spacing 1.0 → 1.5 | `lineHeight` 1.340034 → 2.01005 | `T Spacing` |
| `Ease in`, `Ease out`, `S-curve` on the arriving key | `ease` `cubic-bezier(0.333333, 0, 0.666667, 0.333333)`, `(0.333333, 0.666667, 0.666667, 1)`, `(0.333333, 0, 0.666667, 1)` on the leaving key | `E Curves`, measurement lab 2 |
| rotation −45 (counter-clockwise positive) | `rotate` 45 (clockwise positive) | `K Weather`, cookbook lab 8 |
| gradient start `[0.5, 1]`, end `[0.5, 0]` (y down) | `linear-gradient(0deg, #f4c27a 0%, #5b8fd9 100%)` | `K Still`, cookbook lab 1 |
| rectangle `cornerRadius` 0.15, width 0.2708, height 0.1667 of the frame width | `borderRadius` 24 px on a 520 × 320 card (`2r ÷ short side` = 0.15) | `K Card flip`, cookbook lab 3 |

Rules used for the conversions: `softEdge` px = stored × 1920; `blur` px = size × 1.15 × W ÷ 1920; shadow blur px = softness × 0.433 × W, offset x = stored × W,
offset y = −stored × H; glow radius = size × 1.15 × W ÷ 1920; `letterSpacing` px = (tracking − 1) × `fontSize` ÷ 0.597 for a variable font such as Rethink Sans;
`rotate` = −stored rotation; `borderRadius` px = stored cornerRadius × short side ÷ 2; `strokeWidth` px = stored × W; the stored text outline thickness stays a fraction
(px = thickness × `fontSize` ÷ 0.597). The pages quote the design number and, where a page measured on 0.1.6, say so. Lab measurements stay as measured on 0.1.6; the lab
files were not edited.

## principles-lab.carverproj

| Comp | What it holds | Used by |
|---|---|---|
| `W Spacing` | 9 dots, 1200 px in 20 f, one ease each (linear, quad in, quad out, S-curve, expo, standard, accelerate, decelerate, smooth) | [slow in and out](../principles/slow-in-slow-out.md), [timing and spacing](../principles/timing-and-spacing.md) |
| `W Overshoot` | scale 0 → 1 in 16 f with back curves y1 = 1.3, 1.56, 1.75, 2.0 and a three-key 8% overshoot | [exaggeration](../principles/exaggeration.md) |
| `W Squash` | bouncing ball, anchor on its bottom edge, squash `[1.25, 0.75]` at contact | [squash and stretch](../principles/squash-and-stretch.md) |
| `W Anticipation` | slide with a 60 px wind-up; pop with a dip to 0.9 | [anticipation](../principles/anticipation.md) |
| `W Arcs` | three straight-keyed points vs a dot on a rotating pivot null (radius 500 px) | [arcs](../principles/arcs.md) |
| `W Parabola` | a dot parented to a linear carrier null, Y eased up and down | [arcs](../principles/arcs.md) |
| `W Follow-through` | card and two content bars landing in cascade | [follow-through](../principles/follow-through-and-overlap.md) |
| `W Weight` | light dot 12 f expo vs heavy square 30 f smooth with a landing squash | [weight](../principles/weight.md) |
| `W Secondary` | hero pop with a trailing shadow and a ripple ring | [secondary action](../principles/secondary-action.md) |
| `W Rhythm` | six bars staggered 4 f and a dot pulsing every 15 f | [rhythm](../principles/rhythm.md) |
| `W Depth` | card flip on scale X with a shadow | [solid drawing](../principles/solid-drawing-2d.md) |
| `W Staging` | dimmed, blurred background cards, a hero card, a low-contrast caption (lint `low_contrast` 1.57:1) | [staging](../principles/staging.md) |
| `W Blocking` | two dots on the same three poses, `Hold` vs `S-curve` | [pose to pose](../principles/straight-ahead-and-pose-to-pose.md) |

## techniques-lab.carverproj

| Comp | What it holds | Used by |
|---|---|---|
| `T Masking` | wipe reveal (window scales from its left edge) and a rise-from-behind-a-rule reveal | [masking](../techniques/masking.md), [kinetic type](../techniques/kinetic-type.md) |
| `T Parallax` | three planes of cards at 2.2, 4.4 and 8.8 px a frame | [parallax](../techniques/parallax.md) |
| `T Morphing` | polygon sides 3 → 12, star depth 0.37 → 1, corner radius 0 → 0.5 | [morphing](../techniques/morphing.md) |
| `T Line drawing` | path draw-on, travelling dash (trim offset), circle draw-on | [line drawing](../techniques/line-drawing.md) |
| `T Loop good` / `T Loop bad` | a clean 60 f loop and a broken one that qc still passes | [looping](../techniques/looping.md) |
| `T Match cut` | dot grows into the next scene's sun at the centre | [match cuts](../techniques/match-cuts.md) |
| `T Camera` | three cards parented to a camera null scaling 1 → 1.3 | [camera moves](../techniques/camera-moves-2d.md) |
| `T Faux 3D` | 8-copy extrusion; radial-gradient spheres lit from two sides | [faux 3D](../techniques/faux-3d.md) |
| `T Stagger orders` | five lines, Stagger Text by word, gap 4, orders forward/reverse/centre/edges/random | [stagger systems](../techniques/stagger-systems.md) |
| `T Beat cuts` | five full-frame shots cut every 15 f (120 BPM) | [rhythm editing](../techniques/rhythm-editing.md) |

## timing-lab.carverproj

| Comp | What it holds | Used by |
|---|---|---|
| `S 24 fps`, `S 25 fps`, `S 30 fps`, `S 60 fps` | a one-second expo move starting at 0.5 s and a 34-character line held 2 s, at each rate | [frame rates](../sound-and-timing/frame-rates.md), [reading time](../sound-and-timing/reading-time.md) |

## access-lab.carverproj

| Comp | What it holds | Used by |
|---|---|---|
| `F full 15f` … `F full 3f` | full-frame black/white alternating every 15, 10, 6, 5, 4 and 3 frames | [photosensitivity](../accessibility/photosensitivity.md) |
| `F quarter area 4f`, `F small area 4f` | a white box of 25% and 6.25% of the frame flashing every 4 f | [photosensitivity](../accessibility/photosensitivity.md) |
| `F red 4f`, `F grey low 4f`, `F dark grey 4f` | red, mid-grey and dark-grey flicker every 4 f | [photosensitivity](../accessibility/photosensitivity.md) |
| `C Contrast` | grey text (#595959 to #959595) on black at 18–48 px, Regular and Bold | [contrast](../design/contrast.md), [readability](../accessibility/readability.md) |
| `C Sizes` | #595959 and #767676 text at 24–44 px: where lint's large-text rule starts | [contrast](../design/contrast.md) |
| `C Safe` | text stepping in from the left and top edges | [grids and layout](../design/grids-and-layout.md) |
| `C Colour` | linear vs unconverted colour patches, white at 50% opacity | [colour](../design/colour-psychology.md) |
| `D Fonts` | ten installed faces at the same size: caps, x-heights, widths | [typography pairing](../design/typography-pairing.md) |

The delivery measurements (H.264, ProRes 4444, GIF, PNG sequence) exported `C Sizes`; see
[delivery](../workflow/delivery.md).

## measure-lab-2.carverproj

| Comp | What it holds | Used by |
|---|---|---|
| `E Curves` | 25 easings on the same 1000 px, 20 f move | [easing reference](../principles/easing-reference.md) |
| `E Springs` | baked springs, damping 0.3 to 1.0 | [springs](../principles/springs.md) |
| `M Blur` | squares at shutter 0, 90, 180, 360 | [motion blur](../techniques/motion-blur.md) |
| `M Scale vs size` | a stroked rectangle grown by scale and by width/height | [scale vs size](../techniques/scale-vs-size.md) |
| `M Trails` | a leader and four delayed, fading copies | [trails and echoes](../techniques/trails-and-echoes.md) |
| `M Gradient`, `M Shimmer` | gradient offset with each repeat mode; a sheen moved by start/end keys | [gradients in motion](../techniques/gradients-in-motion.md) |
| `M Colour` | colour keys red→green and blue→yellow; red→green gradients with each interpolation | [colour transitions](../design/colour-transitions.md) |

## measure-lab-3.carverproj

| Comp | What it holds | Used by |
|---|---|---|
| `B Blend` | the 16 blend modes over one base colour | [blend modes](../techniques/blend-modes.md) |
| `B Mid grey` | linear 0.5 grey over linear 0.18 grey in six modes | [blend modes](../techniques/blend-modes.md) |
| `T Spacing` | tracking, word spacing and line spacing keyed | [text spacing animation](../techniques/text-spacing-animation.md) |
| `T Stagger modes` | Stagger Text `each` vs `total` | [stagger systems](../techniques/stagger-systems.md) |
| `T Soft masks` | a feathered wipe and an attempted inverted (knock-out) mask | [soft and inverted masks](../techniques/soft-and-inverted-masks.md) |
| `F Shadow glow` | shadow offsets and softness; glow amount, size and blend | [shadow and glow in motion](../techniques/shadow-and-glow-in-motion.md) |

## audio-lab.carverproj

| Comp | What it holds | Used by |
|---|---|---|
| `A Placement` | a click track clip starting at frame 15 | [audio in Carvercat](../sound-and-timing/audio-in-carvercat.md) |
| `A Gain`, `A Fade`, `A Mix` | a 440 Hz tone at −6 dB; a tone with keyed −60 → 0 → −60 dB fades; two tones summed | [audio in Carvercat](../sound-and-timing/audio-in-carvercat.md) |
| `F Shadow softness` | shadow edges at softness 0, 0.005, 0.01, 0.02, 0.04 | [shadow and glow in motion](../techniques/shadow-and-glow-in-motion.md) |

The audio comps reference two generated WAVs that are not shipped (the repository is text only); recreate them
with any tool: a 4 s, 48 kHz mono file with a 10 ms 1 kHz click every 0.5 s, and a 4 s 440 Hz sine at half
scale. Relink them after opening. Media paths in the file point to the lab machine.

## hierarchy-nest-lab.carverproj

| Comp | What it holds | Used by |
|---|---|---|
| `H Hierarchy` | hero, support and label text in six greys on #101418 | [visual hierarchy](../design/visual-hierarchy.md) |
| `N Inner`, `N Master` | one 60 f animation placed five ways (plain, source-in, late start, scaled, parented) | [nested comps and time](../techniques/nested-comps-and-time.md) |

## measure-lab-4.carverproj

| Comp | What it holds | Used by |
|---|---|---|
| `W Wiggle` | eight seeded random wiggles, ±1 to ±40 px, every 1 to 6 f | [wiggle and jitter](../techniques/wiggle-and-jitter.md) |
| `Q Frozen`, `Q Push 1pct`, `Q Push 3pct`, `Q Push 6pct` | a 4 s held card, still or slowly pushing | [holds and stillness](../principles/holds-and-stillness.md) |
| `S Dashes` | dashed strokes with keyed dash and gap | [stroke dashes](../techniques/stroke-dashes.md) |
| `M Intense` | tiles on a camera null zooming 3× and spinning | [motion sensitivity](../accessibility/motion-sensitivity.md) |

## measure-lab-5.carverproj

| Comp | What it holds | Used by |
|---|---|---|
| `P Outline` | "I" at 100 and 200 px with outline thickness 0.02, 0.05, 0.1 and each alignment | [text outlines](../techniques/text-outlines.md) |

## cookbook-lab-1.carverproj

Measures the first ten [cookbook](../cookbook/README.md) pages. `K Count up` holds three masks made with
`mask.make` (window first; today `mask` on the column) and `parent.clear`; `K Push preset` has `Photo push - 5 s` applied with
`preset.apply`. `K Beat hit` and `K Duck` reference three generated WAVs that are not shipped: a 4 s,
48 kHz mono file with a 10 ms 1 kHz click every 0.5 s; a 5 s bed of 220 Hz + 330 Hz sines at 0.25 each; a
2 s 1 kHz tone at 0.5, on 150 ms and off 50 ms. Relink them after opening.

*Fixed 2026-10-28:* the `K Still` sky was written through the old `cc.py` `gradient()` and rendered upside
down (warm at the top, [KI-155](../../ai/references/known-issues.md#ki-155)). Its object-local endpoints are now
start `[0.5, 1]`, end `[0.5, 0]` (`linear-gradient(0deg, #f4c27a 0%, #5b8fd9 100%)` in design units): rendered blue (92, 143, 217) at the top and warm (185, 171, 176) at mid-height.
Re-measured after the fix: the push widths on [camera push on a still](../cookbook/camera-push-on-a-still.md)
are unchanged (1920 → 1996.8 → 2072.6 and 1920 → 1978.0 → 2035.2 px) and both push comps lint 0 / 0 / 0.

| Comp | What it holds | Used by |
|---|---|---|
| `K Type on` | hard (gap 2, Hold) and soft (gap 1, 4 f fade) character type-on | [type on text](../cookbook/type-on-text.md) |
| `K Count up` | "250" as three masked digit columns rolling f10–f40 | [count a number up](../cookbook/count-a-number-up.md) |
| `K Draw path` | a curved route drawn with `trim.end`, start and end dots | [draw a line along a path](../cookbook/draw-a-line-along-a-path.md) |
| `K Logo sting` | ring draw, mark pop, wordmark rise, tagline, hold, exit (90 f) | [logo sting](../cookbook/logo-sting.md) |
| `K Loop` | 60 f loop: spinner, bob, pulse | [seamless loop](../cookbook/seamless-loop.md) |
| `K Lower third busy` | four lower thirds over 70 bright shapes: bare, shadow, 85% plate, 95% plate | [readable lower third](../cookbook/readable-lower-third.md) |
| `K Still`, `K Push linear`, `K Push preset` | a shape "photo" pushed 8% by hand and by the `Photo push - 5 s` preset | [camera push on a still](../cookbook/camera-push-on-a-still.md) |
| `K Beat hit` | 120 BPM click track and eight hits on the beat frames | [hit on the beat](../cookbook/hit-on-the-beat.md) |
| `K Duck` | music bed keyed down 12 dB under a voice clip | [duck music under voice](../cookbook/duck-music-under-voice.md) |
| `K Progress bar` | a fill with `transformOrigin` on its left, `scale` `[0, 1]` → `[0.72, 1]` | [progress bar](../cookbook/progress-bar.md) |

## cookbook-lab-2.carverproj

Measures cookbook pages 11–20. Masks in `K Split screen` and `K Text reveal` were made with `mask.make`
(mask first; today `mask` on the object to cut) and `parent.clear`; the presets were applied with `preset.apply`; `K Shake` parents the word and
tiles to a null with `parent.assign` (null selected last). `V Captions 9x16` is 1080 × 1920.

| Comp | What it holds | Used by |
|---|---|---|
| `K Ripple` | three `Tap ripple` rings 6 f apart and a hand-keyed ring | [ripple](../cookbook/ripple.md) |
| `K Left scene`, `K Right scene`, `K Split screen` | two scene comps sliding into masked halves, a divider drawing on | [split-screen](../cookbook/split-screen.md) |
| `K Image`, `K Text reveal` | a gradient "picture" drifting inside "OCEAN" | [reveal an image through text](../cookbook/reveal-image-through-text.md) |
| `K Highlight word` | a sentence in three texts with a marker behind "Friday" | [highlight a word](../cookbook/highlight-a-word.md) |
| `K Chart bars` | five bars anchored at the baseline, 4 f apart, back out | [chart bars to values](../cookbook/chart-bars-to-values.md) |
| `K Wipe` | scene A, a panel wipe, scene B cut under it at f24 | [wipe transition](../cookbook/wipe-transition.md) |
| `K Shake` | `Impact slam` on "GOAL" and a decaying shake on a parent null | [screen shake](../cookbook/screen-shake.md) |
| `K Pop in` | `Pop - spring`, `Pop - gentle`, `Stamp`, `Data point pop` side by side | [pop in](../cookbook/pop-in.md) |
| `K Pulse` | a button split at f20 with `Emphasis pulse` | [draw attention pulse](../cookbook/draw-attention-pulse.md) |
| `V Captions 9x16` | two caption pages with `Caption words pop` | [vertical captions](../cookbook/vertical-captions.md) |

## cookbook-lab-3.carverproj

Measures cookbook pages 21–30. `K Glint` masks the sheen with a copy of the text (`mask.make`, copy first; today `mask` on the sheen with the copy as `value`);
`K Orbit` parents the planet to the pivot with `parent.assign`. `K End fade` references the 5 s bed WAV of
cookbook lab 1 (not shipped).

| Comp | What it holds | Used by |
|---|---|---|
| `K Countdown 25f`, `K Countdown 15f` | 3-2-1-GO with a ring per number at 25 f and 15 f a beat | [countdown](../cookbook/countdown.md) |
| `K Donut`, `K Donut clockwise` | a 68% arc: `trimEnd` at `rotate` 0, and `rotate` −90deg (stored +90°) with `trimStart` | [donut fill](../cookbook/donut-fill.md) |
| `K End fade` | title, black fade f60–f89, music −60 dB over the same frames | [end cleanly](../cookbook/end-cleanly.md) |
| `K Dissolve over`, `K Dissolve both` | red to blue over 15 f: B over A, and both fading | [cross-dissolve](../cookbook/cross-dissolve.md) |
| `K Glint` | a rotated sheen masked by a copy of "NORTHWIND" | [glint sweep](../cookbook/glint-sweep.md) |
| `K Neon` | glowing "OPEN" with `Hold` opacity flicker | [neon flicker](../cookbook/neon-flicker.md) |
| `K Bullets` | title and four items, dots popping, text rising 5 f apart | [bullet list](../cookbook/bullet-list.md) |
| `K Card flip` | front and back cards with labels, flip at f18 | [card flip](../cookbook/card-flip.md) |
| `K Orbit` | a planet parented to a pivot turning −360° in 90 f | [orbit](../cookbook/orbit.md) |
| `K Underline` | round- and butt-capped underlines drawn under a measured word | [underline a word](../cookbook/underline-a-word.md) |

## cookbook-lab-4.carverproj

Measures cookbook pages 31–38. `K Word swap` masks each word with its own window; `K Image card` keeps the
mask linked (no `parent.clear`), made at f30 with the picture at rest; `K Headline` has `Words rise - expo`
applied with `preset.apply`.

| Comp | What it holds | Used by |
|---|---|---|
| `K Word swap` | "We build tools" → "teams" through two slot windows | [word swap](../cookbook/word-swap.md) |
| `K Headline` | a headline with `Words rise - expo` | [headline word by word](../cookbook/headline-word-by-word.md) |
| `K Background drift` | a gradient and two blurred blobs looping over 120 f | [background drift](../cookbook/background-drift.md) |
| `K Picture`, `K Image card` | a picture instance inside a 720 × 400 rounded window | [rounded image card](../cookbook/rounded-image-card.md) |
| `K Callout` | target dot, ring, leader line, label and sub-line | [point at something](../cookbook/point-at-something.md) |
| `K Clock hand` | a hand anchored at its bottom edge, one turn in 60 f | [clock hand](../cookbook/clock-hand.md) |
| `K Tile grid` | 28 tiles popping by distance from the centre | [tile grid stagger](../cookbook/tile-grid-stagger.md) |
| `K Focus in` | a title with blur, opacity and scale keyed into focus | [focus in](../cookbook/focus-in.md) |

## cookbook-lab-5.carverproj

Measures cookbook pages 39–48. Presets were applied with `preset.apply` (`Drop - bounce`, `Tap ripple`,
`Pop - spring`, `Spin in`, `Stamp`); `K Pin drop`, `K Chat` and `K Speech bubble` parent their parts to a null
with `parent.assign` at a frame where the null is at rest (f40, f0, f40). `K Picture in picture` keeps the mask
linked (made at f40); `K Before after` masks the After instance and clears the parent.

| Comp | What it holds | Used by |
|---|---|---|
| `K Pin drop` | a pin on a tip null with `Drop - bounce`, a ground shadow and a `Tap ripple` ring | [map pin drop](../cookbook/map-pin-drop.md) |
| `K Chat` | three messages growing from their tail corners under a thread null that pushes up | [chat message](../cookbook/chat-message.md) |
| `K Speech bubble` | body, tail fill and tail outline on a null at the tail tip; text with `Pop - spring` | [speech bubble](../cookbook/speech-bubble.md) |
| `K Sale badge` | a 16-point star with `Spin in`, "-30%" with `Pop - spring`, "SALE" with `Stamp` | [sale badge spin-in](../cookbook/sale-badge-spin-in.md) |
| `K Typewriter` | a character type-on with a cursor on `Hold` position and opacity keys | [typewriter with cursor](../cookbook/typewriter-with-cursor.md) |
| `K Credits` | a 15-row credits text rolling linearly over 360 f under two gradient fade bands | [credits roll](../cookbook/credits-roll.md) |
| `K Main feed`, `K Guest feed`, `K Picture in picture` | a guest instance at 0.3 in a rounded window with a border | [picture-in-picture](../cookbook/picture-in-picture.md) |
| `K Before`, `K After`, `K Before after` | two scenes, a right-anchored reveal window, divider and handle | [before/after slider](../cookbook/before-after-slider.md) |
| `K Speaker swap` | a left-anchored plate resizing between two speakers' names and roles | [lower-third speaker swap](../cookbook/lower-third-speaker-swap.md) |
| `K Spinner` | a steady quarter arc and a mirrored breathing arc, 60 f loop | [loading spinner](../cookbook/loading-spinner.md) |

## cookbook-lab-6.carverproj

Measures cookbook pages 49–58. Presets applied with `preset.apply` (`Tap ripple`, `Card lift`, `Pop - gentle`,
`Pop - spring`); `K Subscribe` parents the labels to the button at f0; `K Split flap` and `K Iris` make each mask
at a frame where its target or window is at scale 1 or open, then `parent.clear`.

| Comp | What it holds | Used by |
|---|---|---|
| `K Subscribe` | a button with a `hold` colour key, two labels, a tip-anchored cursor and a click ring | [subscribe button press](../cookbook/subscribe-button-press.md) |
| `K Confetti` | 30 pieces (seed 7) bursting out and falling, behind a headline | [confetti burst](../cookbook/confetti-burst.md) |
| `K Arrow` | a curved shaft drawn with `trimEnd` and a tip-origin head rotated −31deg (stored 31°) | [animated arrow](../cookbook/animated-arrow.md) |
| `K Stat card` | an up and a down KPI card with rotated triangles and delta chips | [stat card with trend arrow](../cookbook/stat-card-trend-arrow.md) |
| `K End card` | logo, headline, address and button, then a hold to f150 | [end card with URL](../cookbook/end-card-with-url.md) |
| `K Footage`, `K Title bare`, `K Title scrim` | a bright sky instance with a title, without and with a 55% black scrim | [title over footage](../cookbook/title-over-footage.md) |
| `K List highlight` | five items and a bar stepping down every 20 f, `Hold` colour keys | [list highlight bar](../cookbook/list-highlight-bar.md) |
| `K Split flap` | a 3 → 4 flip from four masked digit copies and two hinge-anchored flaps | [split-flap digit](../cookbook/split-flap-digit.md) |
| `K Speed ramp` | a fast-slow-fast title with matched curves, and one with plain eases | [slow-motion hold](../cookbook/slow-motion-hold.md) |
| `K Scene A`, `K Scene B`, `K Iris` | scene B revealed through a circle scaled 0 → 2.3 | [iris wipe](../cookbook/iris-wipe.md) |

## cookbook-lab-7.carverproj

Measures cookbook pages 59–68. Gradients are written with object-local endpoints (y down). `V Story progress`
is 1080 × 1920. Presets applied with `preset.apply` (`Pop - gentle`, `Toast drop - spring`, `Toast exit up`).

| Comp | What it holds | Used by |
|---|---|---|
| `K Zoom A`, `K Zoom B`, `K Zoom through` | scene A zooming 1 → 6 behind scene B arriving 0.5 → 1, motion blur | [zoom-through transition](../cookbook/zoom-through-transition.md) |
| `K Vignette` | a radial alpha gradient over a light background and title | [vignette](../cookbook/vignette.md) |
| `K Hand underline` | two wobbly trimmed strokes under "really" | [hand-drawn underline](../cookbook/hand-drawn-underline.md) |
| `K Parallax`, `K Parallax wide` | three hill layers at 1 : 2 : 4, built from two pieces and from one 2400 px piece | [parallax layers](../cookbook/parallax-layers.md) |
| `V Story progress` | three cards and three left-anchored segment fills | [story progress bar](../cookbook/story-progress-bar.md) |
| `K Lyric` | six word texts with `Hold` colour keys on uneven onsets | [lyric line sync](../cookbook/lyric-line-sync.md) |
| `K Bounce cycle` | a bottom-anchored blob, eyes keyed with it, shadow; 24 f loop | [bounce cycle](../cookbook/bounce-cycle.md) |
| `K Gradient drift` | a three-stop gradient with start and end keyed round the corners, 120 f loop | [gradient background drift](../cookbook/gradient-background-drift.md) |
| `K Checkmark` | ring trim, disc pop and tick trim | [checkmark draw](../cookbook/checkmark-draw.md) |
| `K Toast` | a toast in two clips per part: drop in and exit up | [notification toast](../cookbook/notification-toast.md) |

## cookbook-lab-8.carverproj

Measures cookbook pages 69–78. The blob comps are filled by agent commands only (`object.path`, `key.set` on
`path.geometry`); guides in the safe-area comps by `guide.add`; masks by `mask.make`; parenting by
`parent.assign`; presets by `preset.apply`. Text boxes were measured once with `carvercat_authoring mode:geometry` before laying out the clock, ticker and wordmark.
`S 4:5 safe` is 1080 × 1350 and `S 1:1 safe` is 1080 × 1080.

| Comp | What it holds | Used by |
|---|---|---|
| `K Blob morph`, `K Blob mismatch` | an 8-node blob keyed f0, f30, f60 (S-curve); the same with a 6-node key on f30 | [blob morph](../cookbook/blob-morph.md) |
| `K Countdown clock` | 65 s down to 0, three digit columns behind windows, `Hold` keys, red from f1650 (1980 f) | [countdown clock](../cookbook/countdown-clock.md) |
| `K Rating` | five grey stars, a nested gold row (comp `K Rating gold`), a left-anchored window scaled to 4.5 | [rating stars fill](../cookbook/rating-stars-fill.md) |
| `K Milestones` | a trimmed line with four dots, years and captions on the arrival frames | [milestone timeline](../cookbook/milestone-timeline.md) |
| `K Outline fill` | "BOLD MOVE" with outline thickness and fill opacity keys | [outline to fill text](../cookbook/outline-to-fill-text.md) |
| `K Breaking news` | label, plate, headline and two ticker copies crawling 2288 px in 300 f | [breaking news bar](../cookbook/breaking-news-bar.md) |
| `S 4:5 safe`, `S 1:1 safe` | guides at 5%, with texts at 2%, 6% and 11% from the left | [safe-area guides](../cookbook/safe-area-guides.md) |
| `K Weather` | sun with eight rays on a rotating null, a drifting cloud, three falling drops (60 f loop) | [weather icon loop](../cookbook/weather-icon-loop.md) |
| `K Sound bars` | nine bars with `Hold` scale Y peaks on every beat of 120 BPM (120 f) | [sound-wave bars](../cookbook/sound-wave-bars.md) |
| `K Logo reveal` | a mark, its letter and a wordmark sliding out behind a window | [logo mask reveal](../cookbook/logo-mask-reveal.md) |

## cookbook-lab-9.carverproj

Measures cookbook pages 79–88. Built by writing the project file; column comps are nested into `K Pricing`.
Colours are keyed with `Hold` easing where a switch must land on a frame.

| Comp | What it holds | Used by |
|---|---|---|
| `K Ken Burns` | three gradient "photos", zoom 1 → 1.12 (and back) with drift, 15 f dissolves (240 f) | [Ken Burns slideshow](../cookbook/ken-burns-slideshow.md) |
| `K Testimonials` | three cards on one 1200 px strip, `smooth` slides, three pager dots (252 f) | [testimonial carousel](../cookbook/testimonial-carousel.md) |
| `K Callouts` | a mock panel with three buttons and three numbered callouts, 40 f apart (150 f) | [tutorial callouts](../cookbook/tutorial-callouts.md) |
| `K Price col Basic`, `K Price col Pro`, `K Price col Team`, `K Pricing` | one column per comp, three instances staggered 6 f, Pro scaled 1.06 | [price comparison table](../cookbook/price-comparison-table.md) |
| `K Table` | five rows, a band stepping every 30 f, `Hold` text colour flips 3 f before landing | [table row highlight](../cookbook/table-row-highlight.md) |
| `K Badge card` | icon, name, tagline and two stand-in download badges (120 f) | [app store badge end card](../cookbook/app-store-badge-end-card.md) |
| `K Photo grid` | 4 × 3 tiles, delay 3 × (row + column), `expo` | [photo grid diagonal reveal](../cookbook/photo-grid-diagonal-reveal.md) |
| `K Audiogram` | cover, title, 36 waveform bars lit by `Hold` keys, linear progress fill (216 f) | [podcast audiogram](../cookbook/podcast-audiogram.md) |
| `K Arc text` | "HELLO WORLD" as ten rotated letter texts on a 520 px arc | [text on a curve](../cookbook/text-on-a-curve.md) |
| `K Captions` | six cue texts placed at round(seconds × 30) (450 f) | [timed captions by hand](../cookbook/timed-captions-by-hand.md) |

## Notes for re-measuring

- `carvercat_inspect {mode:"curves"}` reports overshoot % and the settle frame (within 0.5% of the end value).
- `carvercat_inspect {mode:"probe", detail:"detailed"}` gives every frame; concise mode drops rows that lie on
  a straight line.
- `carvercat_inspect {mode:"composite"}` is the only check that sees masks.
- Labs were run headless (`Carvercat --mcp` with private preference, data and cache folders), never attached
  to a running editor.
