# Transitions in Carvercat

How to move from one scene to the next so the film feels like one continuous piece.
Agent-neutral. Frames at 30 fps. Tested recipes for each transition live in
[../patterns/](../../patterns/README.md) (`tr-*`).

## Rules
1. **Motivate it.** A transition continues something already happening: an object's
   direction, the pointer, a beat, a shared shape or colour. If it is only there because
   it "looks cool", use a cut.
2. **2-3 transition types per film**, with the hard cut as the default for fast beats.
   A 5-7 beat reel wants at most 1-2 showy transitions.
3. **Overlap, don't queue.** Outgoing elements leave (Ease in, 8-12 f) while incoming
   ones arrive (Ease out), overlapping by 30-50 % (~4-6 f).
4. **Hit the beat.** Put the cut frame (or the transition's peak) on a music downbeat:
   frames per beat = 1800 / BPM.
5. **Keep screen direction.** Exit left -> the next scene arrives moving left.
6. **Motion blur, not blur.** Fast transition shapes get the `motionblur` effect so the
   leading edges smear; static heavy blur and full-frame glow flashes read as muddy.
7. **Accessibility.** At most 3 flashes per second; zoom-throughs and whips at most
   1-2 per film (motion-sickness triggers); nothing oscillating ~0.2 Hz for long.
8. **Sound.** Every transition gets a whoosh-into-hit whose transient lands exactly on
   the cut (see [sound-design.md](sound-design.md)).

## Catalogue - when each fits
| Transition | Frames | Fits | Carvercat build (see pattern) |
|---|---|---|---|
| Hard cut | 0 | beat edits, lists, energy | butt scenes on the beat |
| Crossfade | 8-15 | calm, time passing, luxury/real estate | opacity overlap of nested comps |
| Dip to black/white | 6-10 each way | chapters; white = celebratory | full-frame rect opacity |
| Push / slide | 12-20 | sequential steps, carousel | both scenes keyed on the same 2-key curve + handles; **verified** ([tr-push](../../patterns/tr-push.md)) |
| Shape stretch wipe | 12-20 | branded change of scene | rect width/height keys + `motionblur` (recipe not written yet) |
| Two-tone wipe | 12-16 | brand colour hand-off | two full-width rects 2-3 f apart, the top one leaves first; **template, verified** ([tr-two-tone-wipe](../../patterns/tr-two-tone-wipe.md)) |
| Iris / circle mask | 12-20 | reveal from a point (pointer, product) | ellipse grows from the point to (diagonal / diameter) x 1.05, expo in-out; **template, verified** ([tr-iris](../../patterns/tr-iris.md)) |
| Zoom-through | 12 out + 20 in | high energy into a detail | presets `Exit zoom through` + `Zoom settle`, overlapping 3-4 f; **verified** ([tr-zoom-through](../../patterns/tr-zoom-through.md)) |
| Whip pan | 9 + 9 | energy, sideways story | X +/-400 px with blur 24 / `motionblur` |
| Blur-through | 9 + 8 | soft scene change | blur 0->20 out, 20->0 in |
| Collapse to dot -> burst | 14 + 10 | hand-off into a logo or CTA | group scale -> ~0.03 to a centred dot; next scene bursts from the same point (recipe not written yet) |
| Match cut / shared element | 0-15 | product explainers | the same shape/colour/position on both sides of the cut |
| Scale swap | out fast + in 14-21 | swapping same-shape items | old scales to 0.6-0.8 and fades; new arrives with ~10 % overshoot |

## Hand-off checklist (for the frame either side of every cut)
- The outgoing scene's last frame and the incoming first frame share colour, position
  or motion direction.
- No element pops (appears or vanishes in one frame) unless it is meant to hit.
- When converting to 9:16, recheck hand-off points: the collapse dot must sit where the
  next scene's burst starts.
