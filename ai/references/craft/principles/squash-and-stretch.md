# Squash and stretch

**What it does:** a shape that squashes on impact and stretches when it moves fast reads as soft, heavy and alive. Keep the volume roughly constant: when it gets wider it gets shorter.

## How in Carvercat
- Use the point **Scale** `[x, y]` (transform `scale`), not size. Presets in the Cartoon Bounce pack key `scaleX`/`scaleY`.
- **Pivot on the contact edge:** a landing squashes from the bottom (`transformOrigin` "50% 100%"; stored anchor `[0, −1]`), a stop from the leading edge ("100% 50%", stored `[1, 0]`, when moving right). With the default centre `transformOrigin` the shape lifts off the ground as it squashes.
- `scaleX`/`scaleY` cannot be staggered ([KI-134](../../known-issues.md#ki-134)): per-letter squash is impossible; squash whole objects.
- On a rig, scale the **pivot** (a visible part at the feet) and the children follow ([../../drawing/rigging.md](../../drawing/rigging.md)).

## Measured examples
| Template | Squash / stretch | Volume x·y | Timing |
|---|---|---|---|
| Squash land ([cartoon-bounce.md](../../../patterns/cartoon-bounce.md)) | stretch 85 × 120% falling, squash 130 × 72% on contact | 1.02 / 0.94 | lands **f8**, squash peak f11, settles **f20** |
| Character hop ([ct-character-hop.md](../../../patterns/ct-character-hop.md)) | crouch 115 × 80%, launch 85 × 120%, land 125 × 75% | 0.92 / 1.02 / 0.94 | land f40–41, recovered by **f56** |
| Button press ([ct-button-press.md](../../../patterns/ct-button-press.md)) | 105 × 88% on press | 0.92 | down f18–21, back by **f38** |
| Bouncing ball ([ct-bouncing-ball.md](../../../patterns/ct-bouncing-ball.md)) | 88 × 115% before contact, 130 × 70% on contact (lighter on later bounces) | 1.01 / 0.91 | 2 f before contact, 3 f to recover |
| Smear whoosh ([ct-smear-whoosh.md](../../../patterns/ct-smear-whoosh.md)) | 240 × 80% stretch at speed | — | first 8 f |

Volume stays within about 10% of 1 in every verified example.

## Dose by style
- Cartoon / kids: 115–130% (above).
- UI: about 105 / 95%, or none; SaaS presets use size only.
- Corporate and luxury: none.

## Traps
- A recovery baked from a spring can end in sub-pixel wobbles that lint reads as `jitter`; set 3 visible recovery keys (ease-in-out) instead ([ct-character-hop.md](../../../patterns/ct-character-hop.md)).
