# Score bug

**Template** `sp_score_bug` · Sports pack · **Verified 0.1.8.1 (rev 1127)**, comp `SP Score bug` in `categories/sports/sp-lab`.

A 64 px tall bug at the top left (x 96, y 64): LIV (red box), the score (dark box), MCI (blue box), and the clock "67:12" (grey box). The labels are ExtraBold 30–34 px.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Boxes | 0, 3, 6, 9 | scale X 0 → 1 from the left, Custom expo | settle 7 f after each start |
| Labels | 6–15 | appear with their boxes | |
| Score "2 - 1" | 52–58 | leaves 50 px upward (accelerating arrival cubic-bezier(0.333, 0, 0.667, 0.333)), masked by the score window | |
| Score "3 - 1" (yellow) | 58–68 | enters from 50 px below (expo), masked | expo over 10 f (first measured as a 52–62 entrance: settled 7 f after its start) |
| Underline | 60–68 | scale X 0 → 1 under the score, expo | settles **f65** |

Lint 0/0/0. A live clock needs one text per second, or the SaaS [rolling counter](su-rolling-counter.md). `text.content` cannot be keyed ([KI-051](../references/known-issues.md#ki-051)).
