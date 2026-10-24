# Motion principles for Carvercat (30 fps)

The craft layer of the Carvercat skill: how long things take, how they ease, how a
scene is choreographed, and how a promo is paced. Written for any agent (Claude, GPT,
Gemini, ...) or person driving Carvercat. Numbers are frames at 30 fps
(1 f ~ 33 ms, 15 f = 0.5 s, 30 f = 1 s). Sources and licences: [SOURCES.md](../../SOURCES.md).

Read with: [typography.md](typography.md), [transitions.md](transitions.md),
[sound-design.md](sound-design.md), [review-checklist.md](review-checklist.md),
and the tested recipes in [../patterns/](../../patterns/README.md).

---

## 1. Durations - use a scale, not random numbers

Pick durations from one scale per project and reuse them: **6, 9, 12, 18, 24, 36 f**.
Identical elements get identical timing. Random durations read as amateur; one
duration for everything reads as PowerPoint.

| Band | Frames | Typical use |
|---|---|---|
| Micro | 3-6 | icon tick, key pulse, colour flash, emphasis pop |
| Small | 6-12 | short nudges (< 10 % of frame width), per-letter units inside a stagger, button press |
| Medium | 12-20 | text lines, cards, chips, lower thirds - most entrances |
| Large | 20-30 | full-frame wipes, big scale changes, window unfolds |
| Dramatic | 30-60 | logo resolves, hero product reveal (once per video) |

Feel by length: 2-4 f snappy, 6-8 f energetic, 12-15 f normal, 20-30 f heavy, 40 f+ weighty.

- **Exits are 20-30 % shorter than entrances** (18 f in -> 12-14 f out). Viewers have
  already seen the element; get it out of the way.
- **Distance costs time, but not linearly**: doubling the travel adds ~30-50 % time.
  Big/heavy elements move slower than small ones.
- **Phase ratio** for a character-like move: anticipation : action : settle ~ 20 : 50 : 30
  (a 30 f move = ~6 f wind-up, ~15 f travel, ~9 f settle).
- **Land, then hold still.** After an element arrives leave it alone >= 15-20 f before
  anything else happens to it. A composed frame holds >= 1-1.5 s.
- A multi-element build resolves within **1-2 s**; longer only for the hero moment.

### Text read time (non-negotiable)
People read ~3 words/s (20 characters/s). After a line has *finished* animating it must
stay still on screen for

    hold >= max(25 f, words x 10 f) + 10 f      (4 words -> 50 f, 8 words -> 90 f)

Use ~17 characters/s for numbers, dense data or non-native audiences. Nothing over ~7 s
on one card. Kinetic text tied to a voiceover appears **on the spoken word or 0-4 f
before it** (use `scripts/motion/vo_align.py` for word frames).

### Speed register and scene shape
- Speed bands set the register: 5-9 f urgent, 9-15 f professional, 15-24 f luxury,
  24-60 f cinematic. Vary across the piece - the slowest scene ~3x the fastest.
- Scene shape: **build** (first 0-30 %), **breathe** (30-70 %, one ambient motion),
  **resolve** (70-100 %). Don't start the first move on frame 0 - offset it 3-9 f.
- Mid-film scenes don't need their own exit animation: the transition IS the exit.
  Only the last scene animates its elements out.
- Spring equivalents (from Remotion's spring maths at 30 fps): a critically damped
  "smooth" spring ~ Ease out settling in ~22 f; the default spring overshoots ~16 % and
  settles in ~28 f; a "snappy" UI spring overshoots ~4 % in ~15 f. Recreate with keys.

## 2. Easing - in Carvercat terms

Carvercat stores the easing on a key and applies it to the segment **leaving** that key
(key A "Ease out" -> the move from A to B decelerates into B).

| Situation | Carvercat easing |
|---|---|
| Element **enters / arrives** | `Ease out` (decelerate) |
| Element **leaves for good** | `Ease in` (accelerate) |
| Element moves A->B while staying on screen, camera moves, transitions | `S-curve` |
| Constant mechanical motion: rotation, drift, ticker, progress bar, loop | `Linear` - only here |
| Steps: counters, cursor blink, on/off, stop-motion | `Hold` |
| Arrivals with personality: logo, icon, CTA, playful brand | overshoot (below) |

The named curves are gentle (`Ease out` = bezier [0.33,0.67,0.67,1]). For premium motion
write an exact curve in the project file - every keyframe accepts
`"easing":"Custom","customEase":[x1,y1,x2,y2]` (CSS order; honoured by preview, render
and the Resolve/Fusion export). Over MCP the same curve takes two `key.set` keys plus
`key.handle` on each: out (x1,y1) on the first, in (x2,y2) on the second, `tied:false`.
Verified on 0.0.72 to match the CSS curve frame for frame
([../patterns/custom-curves.md](../../patterns/custom-curves.md)).

| Curve | customEase | Use |
|---|---|---|
| Expo-out (premium arrive) | `[0.16, 1, 0.3, 1]` | hero text, cards, UI windows |
| Emphasized decelerate | `[0.05, 0.7, 0.1, 1]` | strong single entrances |
| Standard | `[0.2, 0, 0, 1]` | on-screen moves |
| Emphasized accelerate (exit) | `[0.3, 0, 0.8, 0.15]` | exits, things leaving fast |
| Expressive in / out | `[0, 0, 0.3, 1]` / `[0.4, 0.14, 1, 1]` | brand moments |

**Overshoot** - Carvercat has no spring parameter. Three ways, best first:
1. Apply a spring preset from the Motion Patterns pack (`Pop - spring` 16 %, `Pop - gentle`
   about 4.5 %, `Swing in`, `Stamp`). The springs are simulated and baked into keys
   (`../scripts/motion/curves.py`).
2. One overshoot: a back-out handle, `key.handle` out (0.34, 1.56), in (0.64, 1). That gives
   about 10 %.
3. By hand: `start -> target x 1.08 at ~65-70 % of the duration (Ease out) -> target (S-curve)`.
- 5-15 % past target for UI/product; 20-50 % only for playful/kinetic work.
- Settle within 6-12 f, at most 1-3 decaying swings.
- Never overshoot full-frame transitions or camera moves.

Rules: moves under ~5 f get ease-out only; keep **one easing family per piece** and vary
duration, not curve style; no linear keys on anything that starts or stops.

## 3. The 12 principles, applied

1. **Squash & stretch** - on landing, scaleX/scaleY opposite (~105/95 UI, 115/85 playful),
   area roughly constant; consistent across same-type elements.
2. **Anticipation** - 2-4 f backwards at 10-25 % of the action (0.95 before popping to 1;
   10 px left before sliding right). Hero beats only; skip on utility moves.
3. **Staging** - one focal point per beat. Push the rest back (30-60 % opacity, blur,
   darker). A paused frame must read on its own - frame 0 included.
4. **Pose to pose** - key start / end / settle poses first, then refine curves.
5. **Follow-through & overlap** - children lag their parent 2-5 f; the container lands,
   content lands 2-4 f later; on exit content leaves first, then the container.
6. **Slow in / out** - every keyed transform eases; check the curve for kinks.
7. **Arcs** - moves > ~15 % of frame width travel on a gentle curve, not a straight
   diagonal (offset the mid key). UI-like moves stay straight.
8. **Secondary action** - shadows, glows, ripples, particles respond 2-4 f after the
   primary, smaller, never competing.
9. **Timing** - speed = weight and importance. Reuse the duration scale.
10. **Exaggeration** - hero element ~10-20 % push; supporting elements ~0.
11. **Solid drawing / depth** - one light direction, one shadow angle and softness;
    parallax foreground ~1.5-2x background speed; at most 3 speeds.
12. **Appeal** - clean silhouettes at every pose, no jitter, every move has a reason,
    the accent colour appears once per frame.

## 4. Choreography & hierarchy

- **Stagger gaps**: 1-2 f per letter, 2-4 f per word, 3-6 f per line/card; hero ->
  subtitle -> CTA at ~0 / 3-6 / 10 f. Total spread <= ~15-20 f; more than 5-6 items ->
  group them. In Carvercat use the Stagger Text effect (`stagger.set {by, gap}`) for
  text, and offset key times for objects.
- **Order of reveal**: importance first, then reading order. Background/container ->
  headline -> support -> CTA last (it keeps attention).
- **Motion budget**: one primary motion at a time, at most 1-2 things moving together;
  the rest is still or drifting slowly (Linear, 10-60 s cycles). Stillness is emphasis.
- **Priority by motion**: primary = fastest/most distinctive; secondary = medium, once;
  tertiary = subtle; background = slow loops.
- **Continuity**: keep screen direction (exit left -> next enters from the right moving
  left); carry a shared element across the cut (colour field, shape, logo, the pointer);
  one easing family; one light direction. To relocate something for no story reason,
  fade it out and in at the new place instead of flying it.
- **Never static** (house rule): every scene has an IN, a living MID (a pointer action,
  a counter, a drift, a pulse) and an OUT that hands over to the next scene.

## 5. Pacing for promo & social video

- **Hook in 1-3 s** (30-90 f): product or payoff on screen early; frame 0 is a readable
  image, not an empty background waiting for a logo build.
- Lengths: social bumper 6 s; direct response 15-30 s; SaaS explainer 45-90 s.
- Shot / beat length: hype 1-2.5 s; one SaaS feature beat 3-5 s (one idea, one
  headline, one UI action); text card = read time + 0.5 s; end card 2-4 s with the CTA
  held >= 2 s.
- **Music grid**: frames per beat = 1800 / BPM (120 BPM -> 15 f, 100 -> 18 f). Cut on
  downbeats, land major reveals on bar 1 of a phrase (every 60/120 f at 120 BPM). Time
  the *landing* (end of the ease) to the beat; anticipation sits just before it.
- Structure: hook -> context -> 3-5 feature beats -> proof -> CTA, with one held
  breather every ~8-12 s.
- **Sound off**: the story must read from visuals + on-screen text alone.

## 6. Anti-patterns (seen in the wild and in our own first drafts)

- Linear keys on things that start/stop; ease-in-out on everything.
- All elements same duration and same start frame; or random durations.
- Exits as slow as entrances. Content and container leaving together.
- Too many things moving; text still moving while it should be read; holds too short.
- Bounce on everything / on camera moves / on full-frame transitions.
- Per-letter stagger on long sentences; staggers spreading > 20 f.
- Transitions picked "because they look cool"; more than 2-3 transition styles;
  unmotivated zooms/spins; > 3 flashes per second (WCAG 2.3.1).
- Pure opacity fades as the only motion - combine with a small move or scale.
- Animating width/height when scale would do (scale reads smoother and keeps strokes).
- No motion blur on fast moves (strobing); motion blur on slow text (mush).
- **Carvercat-specific**: glow `blend` > 0 leaves a soft haze even at `amount` 0;
  a new blur starts at size 10 (soft text); full-frame glow flashes and heavy blur on
  collapses read as muddy; logos "flying in from random places" - pop pieces in place.
