# Line reveal

**Template** `kt_line_reveal` · Kinetic Typography pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `KT Line reveal`.

A 6 px accent rule draws out from its centre, and the headline rises from behind it as if the rule were a slot. The subline then lifts in underneath.

| Part | Frames | Motion | Measured |
|---|---|---|---|
| Rule (800 px path, y 610) | 0–14 | Trim Stroke start 0.5 → 0 and end 0.5 → 1, Custom expo | settles **f9** |
| Headline ("Launch day", 140 px, centred, y 520) | 8–26 | position +180 px → rest, Custom expo; masked by "Above the rule" (a full-width rectangle from y 300 down to 3 px above the rule) | settles **f20** |
| Subline (40 px Medium, muted, y 680) | 18–32 | opacity 0 → 1 (f18–26), rises 24 px (expo) | settles **f27** |

Lint 0 errors, 0 warnings (one info note: the expo's fast first frame).

## Steps
1. Place and apply; edit the texts inside the comp.
2. For a longer headline, lengthen the rule's path ends. The mask is full width, so it needs no change.
3. Building it by hand: `property.set {id:"headline", key:"mask", value:{"ref":"<mask rectangle id>"}}`, then `parent.clear {ids:[mask rectangle, headline]}`. Otherwise the mask follows the rising text and nothing is hidden.
