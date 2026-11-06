# Cookbook

Short, task-shaped answers: one page per concrete question a Carvercat user or agent asks ("make text type
on", "duck the music"). Each page gives the goal, the steps with native Carvercat objects, parameters and
Library items, a result **measured in Carvercat 0.1.6** (frames, sizes, lint), the traps (linked to
[known issues](../../ai/references/known-issues.md)) and links to the wiki and `ai/` pages that explain why.

The other sections explain principles and techniques; the cookbook is where to start when you know what you
want on screen. The lab projects are in [labs/](../labs/README.md) (`cookbook-lab-*.carverproj`).

| Question | Page | Key measured fact |
|---|---|---|
| How do I make text type on letter by letter? | [type on text](type-on-text.md) | letter *i* at *k* + 1 + gap × (*i* − 1); spaces take a slot |
| How do I count a number up? | [count a number up](count-a-number-up.md) | digit columns behind masks; pitch 1.34 × font size; settles 19 f into a 30 f expo |
| How do I draw a line along a path? | [draw a line along a path](draw-a-line-along-a-path.md) | `trimEnd` S-curve f10–f40: half drawn at f25, 98% at f37 |
| How do I make a logo sting? | [logo sting](logo-sting.md) | 90 f: ring, mark, name, line, hold, exit; mark overshoot 9.8% |
| How do I loop seamlessly? | [seamless loop](seamless-loop.md) | last key on frame = comp length; qc seam 0.001 |
| How do I keep a lower third readable over busy video? | [readable lower third](readable-lower-third.md) | bare 1.29:1, shadow 1.01:1, 85% plate 2.92:1, 95% plate passes |
| How do I fake a camera push on a still? | [camera push on a still](camera-push-on-a-still.md) | `Photo push - 5 s` = scale 1 → 1.06 linear over 149 f |
| How do I sync a hit to a beat? | [hit on the beat](hit-on-the-beat.md) | 120 BPM = 15 f; exported clicks land on f0, 15, 30 … exactly |
| How do I fade music under voice? | [duck music under voice](duck-music-under-voice.md) | gain keys −12 dB measured −12.2 dB in the export; ramps linear in dB |
| How do I make a progress bar? | [progress bar](progress-bar.md) | `transformOrigin` `"0% 50%"` keeps the left edge fixed; `scale` `[v, 1]` |
| How do I make a ripple? | [ripple](ripple.md) | `Tap ripple`: scale 0.25 → 1 settles 11 f after the tap; gone after 17 f |
| How do I make a split-screen? | [split-screen](split-screen.md) | two instances behind two windows; left settles f13, right f17; lint warns mask-blind |
| How do I reveal an image through text? | [reveal an image through text](reveal-image-through-text.md) | text as the mask; nothing leaks outside the letters |
| How do I highlight a word in a sentence? | [highlight a word](highlight-a-word.md) | measure "prefix word" − "word": bounds drop a trailing space (KI-149) |
| How do I animate chart bars to values? | [chart bars to values](chart-bars-to-values.md) | `transformOrigin` `"50% 100%"`, `scale` `[1, value/max]`; bottom edge fixed; back out overshoots 9.8% |
| What is a good 9:16 caption style? | [vertical captions](vertical-captions.md) | centre x 490, y ≈ 1240; `Caption words pop` = words 3 f apart |
| How do I wipe from one scene to the next? | [wipe transition](wipe-transition.md) | panel covers f20–f28, cut under it at f24; qc no flash |
| How do I shake the screen on an impact? | [screen shake](screen-shake.md) | `Impact slam` lands at clip f5; six decaying swings over 12 f on a parent null |
| Which pop should I use? | [pop in](pop-in.md) | spring 16.2% over, gentle 4.4%, Stamp 4.6% under, data point 16.2% in 11 f |
| How do I pulse a button to draw attention? | [draw attention pulse](draw-attention-pulse.md) | `Emphasis pulse`: 1 → 1.15 at +6 f → 1 at +16 f |
| How do I make a 3-2-1 countdown? | [countdown](countdown.md) | 25 f per number lints clean; 15 f gets `reading_time` warnings |
| How do I fill a donut to a percentage? | [donut fill](donut-fill.md) | stroke starts at 3 o'clock, counter-clockwise; `rotate` `"-90deg"` and `trimStart` `"100%"` → 100% − v for clockwise from 12 |
| How do I end a video cleanly? | [end cleanly](end-cleanly.md) | black rect 0 → 1 to the last frame: f89 renders (0, 0, 0); music −60 dB measured −73 dBFS |
| How do I cross-dissolve? | [cross-dissolve](cross-dissolve.md) | fade only the incoming clip; fading both dips the mid frame (luma 0.36 vs 0.41) |
| How do I sweep a glint across a logo? | [glint sweep](glint-sweep.md) | text copy as the sheen's mask; sheen on the letters only, f15–f34 |
| How do I make a neon sign flicker on? | [neon flicker](neon-flicker.md) | `hold` opacity keys switch on their own frame; qc no flash for a small word |
| How do I bring in a bullet list? | [bullet list](bullet-list.md) | dot pops, text rises 2 f later, items 5 f apart; last settles f39 |
| How do I flip a card? | [card flip](card-flip.md) | front `scale` `[1, 1]` → `[0, 1]` accelerate, back `[0, 1]` → `[1, 1]` decelerate; edge-on frame shows nothing |
| How do I make something orbit? | [orbit](orbit.md) | parent to a rotating null: radius held 300.0 px every frame |
| How do I underline a word as it is said? | [underline a word](underline-a-word.md) | round caps add half the stroke at each end; inset 4 px for an 8 px line |
| How do I swap one word for another? | [word swap](word-swap.md) | two words, two identical windows; nothing leaks outside the slot |
| How do I animate a headline word by word? | [headline word by word](headline-word-by-word.md) | `Words rise - expo`: words 3 f apart, line still about 20 f after the first |
| How do I keep a background alive? | [background drift](background-drift.md) | blurred blobs out and back over the loop; qc seam 0.0; blur 60 spreads 207 px |
| How do I slide in a rounded image card? | [rounded image card](rounded-image-card.md) | `mask` set at a rest frame; made at f0 the card landed 60 px high |
| How do I point at something? | [point at something](point-at-something.md) | dot, leader `trimEnd` (98% at f18), label at the line's end |
| How do I rotate a hand about its end? | [clock hand](clock-hand.md) | `transformOrigin` `"50% 100%"`, centre half a length from the pivot: distance held 100.0 px |
| How do I stagger a grid from the centre? | [tile grid stagger](tile-grid-stagger.md) | delay = 3 f per cell of distance; 28 tiles settle f21–f29 |
| How do I bring a title into focus? | [focus in](focus-in.md) | blur 24 → 0 with scale 1.06 → 1, settles f19; blurred area 4.4× the sharp one |
| How do I drop a map pin onto a spot? | [map pin drop](map-pin-drop.md) | `Drop - bounce` on a tip null: starts 302.4 px up, first contact 9 f later, still from f34 |
| How do I bring in chat messages? | [chat message](chat-message.md) | bubble anchored at its tail corner: corner held at (620, 942); thread null pushes 108 px, expo 10 f |
| How do I pop a speech bubble out of a character? | [speech bubble](speech-bubble.md) | null on the tail tip, scale 0 → 1 back out: tip held at (860, 600), 9.8% over, settles f21 |
| How do I spin in a sale badge? | [sale badge spin-in](sale-badge-spin-in.md) | `Spin in`: −180° → 0 settles 16 f after start, scale 4.4% over; figure `Pop - spring`, word `Stamp` |
| How do I type text with a blinking cursor? | [typewriter with cursor](typewriter-with-cursor.md) | `hold` position keys at measured prefix edges: cursor 4–5 px after the ink at every letter |
| How do I roll end credits? | [credits roll](credits-roll.md) | `linear` from below to above: 857 px block in 360 f = 5.49 px/frame; fades need object-local endpoints |
| How do I put a picture-in-picture in a corner? | [picture-in-picture](picture-in-picture.md) | instance at scale 0.3 = 576 × 324 px; window masked at rest moves with it every frame |
| How do I make a before/after slider? | [before/after slider](before-after-slider.md) | window origin on the right, `scale` `[1 − v, 1]`, divider centre 1920 v: seam 4 px from the line centre every frame |
| How do I swap a lower third between two speakers? | [lower-third speaker swap](lower-third-speaker-swap.md) | plate origin on the left, `scale` x to each width: 40.0 px padding for both; never two names at once |
| How do I make a loading spinner? | [loading spinner](loading-spinner.md) | breathing arc: trim end then start, `rotate` 450deg per 60 f loop; qc seam 0.0; mirrored arc lints `never_visible` |
| How do I press a "subscribe" button with a cursor? | [subscribe button press](subscribe-button-press.md) | cursor anchored on its tip: tip held at (1010, 560); `hold` fill key turns grey on the click frame |
| How do I burst confetti? | [confetti burst](confetti-burst.md) | out 12 f decelerate, fall 50 f accelerate: 266–514 px spread at +12 f; all gone at f72 |
| How do I draw an arrow that points at something? | [animated arrow](animated-arrow.md) | head origin on its tip, rotated to the last handle's direction (`rotate` −31deg); shaft 98% drawn in 20 f |
| How do I build a stat card with a trend arrow? | [stat card with trend arrow](stat-card-trend-arrow.md) | triangle `rotate` −90deg points up, 90deg down; saturated delta text failed contrast (2.99:1), light tints pass |
| How do I make an end card with a web address? | [end card with URL](end-card-with-url.md) | everything settled by f40, then a 110 f hold; lints clean with contrast |
| How do I keep a title readable over bright footage? | [title over footage](title-over-footage.md) | black scrim at 0.55: lint error 1.58:1 → pass; box-mean contrast 1.19 → 2.84:1 |
| How do I move a highlight bar down a list? | [list highlight bar](list-highlight-bar.md) | bar on layout lines (ink centres drift up to 5.6 px); `hold` colour keys switch on their frame |
| How do I flip a split-flap digit? | [split-flap digit](split-flap-digit.md) | four masked copies, flaps anchored on the hinge: edge-on f26, done in 12 f, no leaks |
| How do I fake a slow-motion hold? | [slow-motion hold](slow-motion-hold.md) | 303 px/frame in, 3.3 px/frame drift, out again; no time remap for footage (FR-043) |
| How do I open a scene with an iris wipe? | [iris wipe](iris-wipe.md) | 1000 px circle scaled to 2.3: corners covered on the frame the diameter passes 2203 px |
| How do I zoom through from one scene into the next? | [zoom-through transition](zoom-through-transition.md) | A 1 → 4 accelerate stays opaque behind B (0.5 → 1 expo): edges never black, B full from f36 |
| How do I add a vignette? | [vignette](vignette.md) | radial gradient alpha 0 → 0.65 from 0.55 out: corner 40% darker; the shape follows the frame's aspect |
| How do I scribble a hand-drawn underline? | [hand-drawn underline](hand-drawn-underline.md) | two wobbly trimmed strokes: 10 px before and 14 px past the measured word; stroke 1 drawn f13–f19 |
| How do I pan across parallax layers? | [parallax layers](parallax-layers.md) | 1 : 2 : 4 speeds measured exactly; a 2400 px path is cropped to the comp box, so build layers from pieces |
| How do I make a story progress bar? | [story progress bar](story-progress-bar.md) | left-origin fills, `scale` `[0, 1]` → `[1, 1]` `linear` per card: 333.3 px segments, left edges pinned |
| How do I light up lyrics in sync? | [lyric line sync](lyric-line-sync.md) | one text per word, `hold` colour key on each onset: every word lit on its own frame |
| How do I loop a bounce cycle? | [bounce cycle](bounce-cycle.md) | `transformOrigin` on the bottom: squash sits on the ground (800.0); eyes keyed with the body stay inside |
| How do I drift a gradient background? | [gradient background drift](gradient-background-drift.md) | key `gradientStart`/`gradientEnd` round the corners: colours step a corner per 30 f; qc seam 0.0 |
| How do I draw a success checkmark? | [checkmark draw](checkmark-draw.md) | ring `trimEnd`, disc `Pop - gentle`, tick `trimEnd` decelerate: tick 98% drawn in 6 f |
| How do I drop a notification toast in and out? | [notification toast](notification-toast.md) | `Toast drop - spring` from 64.8 px above, settles +18 f; `Toast exit up` keys the clip's last 10 f |
| How do I morph one shape into another? | [blob morph](blob-morph.md) | `key.set` on `path.geometry`, same node count: midpoint radii = mean of the keys within 1 px; a 6-node key jumps (KI-161) |
| How do I make an mm:ss countdown clock? | [countdown clock](countdown-clock.md) | `hold` keys on digit columns behind windows: 01:05 to 00:00, red from f1650; 77 mask-blind lint warnings |
| How do I fill rating stars to 4.5? | [rating stars fill](rating-stars-fill.md) | per-star edge x = 620 + 4 × 140 + 0.5 × 120 = 1240; rightmost gold pixel 1239 |
| How do I animate a timeline with milestones? | [milestone timeline](milestone-timeline.md) | `linear` `trimEnd`: tip passes x 720, 1200, 1680 on f30, f50, f70 within 2 px; dots pop on arrival |
| How do I reveal text from outline to fill? | [outline to fill text](outline-to-fill-text.md) | outline drawn from f6, inside stays background until f20, full white f36 |
| How do I make a breaking-news bar with a ticker? | [breaking news bar](breaking-news-bar.md) | ticker copy spacing = run width with trailing spaces (2288 px, not 2251.7): gap constant 2288.0 every frame |
| How do I set safe-area guides for 4:5 and 1:1? | [safe-area guides](safe-area-guides.md) | `guide.add` at 5%: exactly lint's graphics-safe box; guides never render |
| How do I loop a weather icon? | [weather icon loop](weather-icon-loop.md) | rays on a null −45° per 60 f (eight rays repeat every 45°): qc seam 0.0 |
| How do I make sound-wave bars jump to the beat? | [sound-wave bars](sound-wave-bars.md) | 120 BPM = 15 f; `hold` peak keys land on the beat frame, rest 12 f later (38.4 px) |
| How do I reveal a wordmark from behind its logo mark? | [logo mask reveal](logo-mask-reveal.md) | wordmark cut at the window edge (x 791) until f24, settles x 820 by f40 |
| How do I make a Ken Burns photo slideshow? | [Ken Burns slideshow](ken-burns-slideshow.md) | zoom 1.00 to 1.12 with drift grown alongside: frame covered on all 240 frames; 15 f linear dissolves |
| How do I slide through testimonials? | [testimonial carousel](testimonial-carousel.md) | one shared curve on a strip: gap 100.0 px on every frame; separate in and out curves overlapped 309.5 px |
| How do I add numbered tutorial callouts? | [tutorial callouts](tutorial-callouts.md) | circle pop 12.5% over, line tip within 2 px of its aim, label rises 24 px; numbers trip text_too_small (KI-162) |
| How do I animate a price comparison table? | [price comparison table](price-comparison-table.md) | nested column comps: Pro at 1.06 is 468 px wide, 27 px from its neighbours; lint cropped_at_rest false alarm (KI-163) |
| How do I highlight table rows one at a time? | [table row highlight](table-row-highlight.md) | band lands on rows to the frame; text flips to ink 3 f early: 9.86:1 against 1.70:1 for white on amber |
| How do I end an app video with download badges? | [app store badge end card](app-store-badge-end-card.md) | icon 10.3% over, everything still from f42; lints clean with contrast |
| How do I reveal a photo grid? | [photo grid diagonal reveal](photo-grid-diagonal-reveal.md) | start 3 × (row + column), expo, no overshoot: whole 4 × 3 grid settles in 24 f |
| How do I make a podcast audiogram? | [podcast audiogram](podcast-audiogram.md) | bar i lights on round(i × 216 / 36) (Hold); progress 4.61 px/frame; waveform is hand-set (FR-047) |
| How do I put text on a curve? | [text on a curve](text-on-a-curve.md) | one text per letter, `rotate` = angle: all ten at radius 520.6–520.7 px, angles within 0.01 deg (no native text on a path, FR-050) |
| How do I time captions from a subtitle list? | [timed captions by hand](timed-captions-by-hand.md) | frame = round(seconds × fps): every cue on exactly start to end − 1; no SRT import (FR-049) |
