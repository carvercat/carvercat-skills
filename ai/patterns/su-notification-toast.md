# Notification toast

**Template** `su_notification_toast` · SaaS UI pack · **Verified 0.1.8.4 (rev 1130)**, comp `SU Notification toast`.

A 580×124 px white card with a 22 px radius and a soft shadow drops in at the top centre (y 136), with an accent icon disc, a title and a body line. It holds, then everything leaves upward together.

| Part | Clip start | Entrance | Exit |
|---|---|---|---|
| Toast card | 0 | Toast drop - spring | Toast exit up (110–120) |
| Toast icon (56 px disc) | 2 | Toast drop - spring | Toast exit up |
| Toast title ("New signup", Rethink Sans SemiBold 26 px) | 6 | Card lift | Toast exit up |
| Toast body (Regular 21 px, muted) | 9 | Card lift | Toast exit up |

Measured: the card drop overshoots **4.4%** and settles at **f18**. The body's lift settles at **f21** (12 f after it starts). All four exits run f110–119. Lint 0/0, plus info notes for repeated key values (baked presets) and the shadow spreading past the top edge while the card is still above the frame.

## Steps
1. Place and apply. Edit the text inside the nested comp (`comp.switch`).
2. For a longer hold, lengthen the nested comp (`comp.duration`) and drag the four clips' ends together, so the exit moves with them.
3. Stack two toasts by placing a second instance 140 px lower, 20–30 f later.

## Pitfalls
- Text inside a card must not drop from above, or it pokes out above the card while it lags behind. That is why the text uses Card lift.
- A Mixed-RTL body needs separate LTR number objects ([KI-040](../references/known-issues.md#ki-040)).
