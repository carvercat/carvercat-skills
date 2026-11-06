---
id: cookbook/count-a-number-up
title: Count a number up
section: cookbook
tags: [counter, count up, odometer, rolling digits, number, stat, kpi, ticker]
styles: [saas-ui, data-viz, corporate-brand, sports, kinetic-typography]
topics: [text, masking, data]
related: [techniques/masking, techniques/motion-blur, genres/data-stories, cookbook/type-on-text, cookbook/progress-bar]
verified: 0.1.6 (rev 1105)
source_inspiration: [https://www.framer.com/marketplace/components/odometer-counter-fx/, https://pub.dev/packages/motion_number]
---

# Count a number up

**Goal.** A number that rolls up to its value ("250") like an odometer, settling on a clean, readable
figure.

## Steps

Text content cannot be keyed, so each digit is a **column** of digits that slides behind a window.

1. **Measure the line pitch** once at your size with `carvercat_authoring mode:geometry`: pitch =
   (height of the text "0⏎1⏎…⏎9" − height of "0") / 9. Measure the right edge of each prefix ("2",
   "25", "250") too, so each column lands where its digit sits in the set number.
2. **One text per digit**, content "0⏎1⏎…⏎target". Give the right-hand columns extra turns
   (`"0123456789"` repeated before the final run), so the units spin fastest, as on a real counter.
3. **Key the column position** from centre + (lines − 1)/2 × pitch to centre − (lines − 1)/2 × pitch
   (`y` is the top of the layout box: y = centre − height/2), one shared span and ease for all columns (expo out reads as "counting, then landing").
4. Add **Motion blur** (`effect.add {cap: "motionblur"}`, `motionblur.shutter` 180) to each column.
5. **Window**: a rectangle a little taller than one digit over each column. Run
   `property.set {id: "<column>", key: "mask", value: "<window>"}`, then `parent.clear {ids: ["<window>"]}`, so the window
   stays still while the column moves.

## Measured in Carvercat 0.1.6

Comp `K Count up` in [cookbook lab 1](../labs/README.md#cookbook-lab-1carverproj): "250" at 140 px
Rethink Sans Bold, keys f10 → f40, expo out (`cubic-bezier(0.16, 1, 0.3, 1)`).

| Column | Lines | Peak speed | Settles (`inspect curves`) |
|---|---|---|---|
| hundreds 0 → 2 | 3 | 73 px/frame | f29 |
| tens 0 → 5, one extra turn | 16 | 548 px/frame | f29 |
| units 0 → 0, two extra turns | 21 | 731 px/frame | f29 |

- Line pitch at 140 px Bold: (1790 − 101) / 9 = **187.7 px** (1.34 × the font size).
- `carvercat_look`: "000" at f10, digits still rolling at f28, a clean "250" from **f33**.
- `inspect lint`: 0 errors, **4 warnings** (`cropped_at_rest` for the hidden lines of the tens and units
  columns) and 4 notes (`speed_jump` per column, `outside_graphics_safe`). All are mask-blind; the picture
  is correct.

## Traps

- `text.content` is not keyframeable: [KI-051](../../ai/references/known-issues.md#ki-051).
- "Clip to box" does not hide the extra lines; use a mask: [KI-132](../../ai/references/known-issues.md#ki-132).
- Lint ignores masks, hence the warnings above. Judge with `carvercat_look`, or nest the counter (the
  instance lints clean): [KI-133](../../ai/references/known-issues.md#ki-133).
- Put the window in `value` and the column in `id`: swapped, the column becomes the matte. (Old: `mask.make {ids:[window, column]}`, the first id is the mask.)

## In Carvercat

- Curve names on this page (expo out) are `ease` strings: [names](../principles/easing-reference.md#names-used-in-this-wiki).
- Recipe with currency sign and comma: [rolling counter](../../ai/patterns/su-rolling-counter.md).
- Library: `Big number`, `Stat punch` ([kt-stat-punch](../../ai/patterns/kt-stat-punch.md)), `KPI tile`
  ([su-kpi-tile](../../ai/patterns/su-kpi-tile.md)), `Three stats`
  ([cb-three-stats](../../ai/patterns/cb-three-stats.md)).
- Background: [masking](../techniques/masking.md), [motion blur](../techniques/motion-blur.md),
  [data stories](../genres/data-stories.md).
