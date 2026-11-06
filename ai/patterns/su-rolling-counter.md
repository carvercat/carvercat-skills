# Rolling counter

**Recipe** · SaaS UI pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `SU Counter` in `categories/saas-launch/saas-ui-lab`; generator `counter()` in `ai/scripts/motion/saas_ui_lab.py`.

An odometer counter: "$48,200" rolls up from "$00,000", with each digit column spinning into place. `text.content` cannot be keyed ([KI-051](../references/known-issues.md#ki-051)), so each digit is a column text "0⏎1⏎…" that moves behind its own mask window.

## Build (per digit)
1. **Measure once** with `carvercat_authoring mode:geometry`, on throwaway texts at the final size:
   - the line pitch: (height of "0⏎1⏎…⏎9" − height of "0") / 9. At Rethink Sans Bold 120 px this is **160.8 px**;
   - the ink right edge of every prefix of the number ("$", "$4", "$48", …);
   - the ink box of each single character.
2. **Place each column** so its target digit lands where it sits in the set number: x = text x + (prefix right − char width) − char ink left.
3. **Content:** `"0123456789"` repeated *loops* times, plus "0…target", one per line. The lab uses loops 0, 0, 1, 1, 2 from left to right, so the right-hand columns spin more.
4. **Keys:** position from centre + (lines − 1)/2 × pitch to centre − (lines − 1)/2 × pitch (pixels, y down), f6 → f36, Custom expo cubic-bezier(0.16, 1, 0.3, 1). Add the Motion blur effect, shutter 180.
5. **Mask:** a rectangle 124 px tall over the row (wider than the glyph by 60 px). Run `property.set {id:<column>, key:"mask", value:{"ref":"<window id>"}}` (the window is the mask), then `parent.clear {ids:[window, column]}`, so the window stays put while the column rolls. Referencing the column from the window instead makes the column the matte and draws it in the window's colour. The first release did that, and it only looked right because both were white.
6. "$" and "," are plain static texts at their measured x.

Measured: every column settles at **f25** (within 0.5%; the last 11 f are the expo tail). The fastest column (two extra turns) peaks at 626 px/frame, and motion blur turns that into a readable spin. The look shows a clean "$48,200" from f28, with the cut lines inside the window while rolling.

## Lint
The lab comp reports **13 warnings, all mask-blind**: `cropped_at_rest` for the hidden lines of each column, and `text_overlap` between hidden lines and the label. Lint states that it "excludes masks" ([KI-133](../references/known-issues.md#ki-133)). Prove the picture with `carvercat_look` instead. Placed as a nested comp in the showcase master, lint is 0/0/0.

## Pitfalls
- "Clip to box" does not hide the extra lines ([KI-132](../references/known-issues.md#ki-132)). Use masks.
- The old way, back-to-back 2 f text clips, gives one `reading_time` warning per clip, and the width jitters as the digit count changes.
- Keep the label more than one line pitch below the row, or hidden column lines overlap it in lint.
