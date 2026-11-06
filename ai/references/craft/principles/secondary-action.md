# Secondary action

**What it does:** a smaller action that supports the main one (a blink, a shadow, a ripple) adds life without stealing focus.

## How in Carvercat
- Start it 2–4 f after the primary, keep it smaller and quieter, and never let it compete with the hero.
- Typical secondary actions and their tools:
  - a contact shadow that shrinks with height (scale and opacity keys on a flat ellipse);
  - a ripple or press ring (scale up and fade, one way);
  - a blink after a landing (eye scale Y to 10% and back, keys at least 4 f apart);
  - sparkles, satellites, glints (Spin in, orbit, gradient gleam).

## Measured examples
| Template | Primary | Secondary | Numbers |
|---|---|---|---|
| Character hop ([ct-character-hop.md](../../../patterns/ct-character-hop.md)) | the hop | shadow shrinks to 55% at the peak; blink f64–70 | blink 24 f after landing |
| Button press ([ct-button-press.md](../../../patterns/ct-button-press.md)) | the press | ring 0.9 → 1.35, fading over 16 f | from f21 (contact) |
| Cursor click ([su-cursor-click.md](../../../patterns/su-cursor-click.md)) | the press | Tap ripple | ripple 2 f after the press |
| Squiggle underline ([fk-squiggle-underline.md](../../../patterns/fk-squiggle-underline.md)) | the phrase | three sparkles spin in from f20 | 4 f apart |
| Light sweep ([ml-light-sweep.md](../../../patterns/ml-light-sweep.md)) | the wordmark | a gleam crosses it | f30–110 |

## Traps
- Ping-pong secondary motion (a bob, a wiggle) is read by lint as `jitter`; keep secondary motion one way, or a single event.
