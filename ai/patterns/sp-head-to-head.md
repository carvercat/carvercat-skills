# Head to head stats

**Template** `sp_head_to_head` · Sports pack · **Verified 0.1.8.1 (rev 1127)**, comp `SP Head to head`.

"HEAD TO HEAD" (ExtraBold 48 px, tracked) over three rows (SHOTS 14–9, POSSESSION 58%–42%, CORNERS 7–3). Each row has a grey label, a red bar growing left and a blue bar growing right from the centre (gap 940–980 px, bar length ∝ share), and the values at the outer ends.

| Part (row *i*) | Frames | Motion | Measured |
|---|---|---|---|
| Bars | 8 + 8*i* to 22 + 8*i* | scale X 0 → 1, transformOrigin "100% 50%" and "0% 50%" (anchors [1, 0] and [−1, 0]), Custom expo | settle 9 f after each start |
| Values | from 20 + 8*i* | appear once the bars are near full length | |

Lint 0/0. For new numbers, set each bar's width to 1008 × share (both sides of a row together) and move the value texts to the bar ends.
