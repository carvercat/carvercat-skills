# Chat thread

**Template** `su_chat_thread` · SaaS UI pack · **Verified 0.1.8.4 (rev 1130)**, comp `SU Chat thread` in `categories/saas-launch/saas-ui-lab-2`.

Three message bubbles (560×104 px, radius 40): white on the left, accent on the right, 150 px apart. 120 f, holds.

| Part | Clip start | Motion | Measured |
|---|---|---|---|
| Bubble 1–3 | 0, 26, 52 | scale 0 → 1 from the tail corner (transformOrigin "0% 100%" received, "100% 100%" sent; anchor ∓1, −1), 12 f, back ease cubic-bezier(0.34, 1.56, 0.64, 1); opacity 0 → 1 in 3 f | **9.8% overshoot, settles 11 f after its start** (f11, f37, f63) |
| Message 1–3 (Medium 32 px) | bubble + 5 | Card lift | |

Lint 0 errors, 0 warnings (notes: `speed_jump` on each bubble, the back ease). Placed into a fresh comp: lint 0/0/0.

## Steps
1. Place and apply. Edit the messages; keep each to one line (about 28 characters at 32 px).
2. Pace: 26 f between messages reads comfortably for short lines. Longer lines: about 1 f per character.
3. More messages: copy a bubble and message pair, 150 px lower and 26 f later; shorten the gap or scroll the thread (a position key on the whole instance).

## Pitfalls
- A bubble that grows from its centre looks like a pop, not a message. The anchor on the bottom tail corner (left for received, right for sent) is what sells it.

Inspiration: messaging-app UI conventions. No external text or code was used.
