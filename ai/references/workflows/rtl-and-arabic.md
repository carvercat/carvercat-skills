# Arabic and RTL text

Read this when a job has Arabic (or any right-to-left) text: fonts, reading direction, word stagger, numbers inside Arabic phrases, brand colours, and delivering RTL work as PNG sequences or Fusion clips.
General caption timing is in [captions-and-voiceover.md](captions-and-voiceover.md); Resolve steps in [resolve-handoff.md](resolve-handoff.md). Known defects referenced here are listed in [../known-issues.md](../known-issues.md).

## Contents
1. [Fonts](#1-fonts)
2. [Reading direction and word stagger](#2-reading-direction-and-word-stagger)
3. [Numbers and Latin inside Arabic](#3-numbers-and-latin-inside-arabic)
4. [Layout of RTL groups](#4-layout-of-rtl-groups)
5. [Colour conversion](#5-colour-conversion)
6. [PNG delivery of RTL work](#6-png-delivery-of-rtl-work)
7. [Fusion transfer: the RTL stagger workaround](#7-fusion-transfer-the-rtl-stagger-workaround)
8. [Windows text-encoding traps](#8-windows-text-encoding-traps)

## 1. Fonts

- Only enabled, publicly installed OS/user fonts are project fonts. Query `carvercat_authoring mode=fonts` with family, style and an actual Arabic sample, and check the resolved face. A successful family write does not prove glyph coverage. Use `require_font=True` / `Scene.check_font(require=True)` or the `font_exact` validation check when substitution must be refused.
- Fonts that resolved with Arabic: Almarai (Regular/Bold/ExtraBold, face 0 of `Almarai-ExtraBold.ttf`), Alan Sans (Light to Black; its ExtraBold file contains Arabic). Default RTL caption font in `cc_scene` is Almarai ExtraBold. Number fonts used beside Arabic: Poppins Bold, Barlow Condensed SemiBold, Impact Normal.
- A missing font silently falls back to Segoe UI (seen with Almarai absent from the system and per-user font folders). Install it only with the user's consent (Almarai came from Google Fonts' official repository), keep a copy in the job assets folder, then save, quit normally and relaunch the app: a font installed after launch is not picked up ([KI-042](../known-issues.md#ki-042)). Re-probe after reopening.
- On an early pre-release build a relaunch from the chat's directory exited; launching the same executable with the app repository as working directory worked.
- Style names are font-specific: Impact's style is **Normal**; requesting "Regular" resolves the same file but reports a substitution.
- The live family name can differ from a bundled file's internal family or CSS alias. Discover the name from the running app.
- `textProps.fontResolved` in project JSON is a derived cache and changes on save. It is not font evidence; use native probe/look font notes and exported glyphs.

## 2. Reading direction and word stagger

- Set `readingDirection` to `rtl` (promote its stored param path if needed). Do not reverse the string.
- Word stagger with `order: forward` reveals the **rightmost** (first-read) Arabic word first, because stagger follows logical string order. `reverse` would reverse the reading order. Verified on an early pre-release build in rendered frames 9/13/17/21/25 and in later builds.
- Stagger by word. Do not break Arabic into characters or separate per-word objects.
- Verify the first revealed word in rendered or composited intermediate frames, not on a fully revealed still. Keep an inverted-RTL expectation as a negative test (it must fail).
- Outlined Arabic: connect `stroke.opacity` as well as `fill.opacity` with matching curves, or the outline exposes a word before its fill.
- After a stagger connection, `param.list` may show fill opacity only as a slot proxy. Read `stagger.list` and use the slot's underlying `key`. `stagger.list` returns `stagger: null` for text without a card: handle with `(value or {})`.
- Preference seen in recent Arabic jobs: solid white Arabic fill, no outline (outline paint none, thickness 0), keep the soft shadow. When removing an outline, also remove any animated fill-colour switch that would bring the old colour back.

## 3. Numbers and Latin inside Arabic

Mixed bidi is not handled inside one text object ([KI-040](../known-issues.md#ki-040)):

| Input | Rendered |
|---|---|
| `40 شهر` with explicit rtl | digits shown as `04` |
| numeric-only `10%` with rtl | `%01` |

- Put digits and Latin in a separate LTR text object (Poppins Bold, Impact Normal or Barlow Condensed SemiBold), Arabic in its own RTL object, and position the runs so the reading order is right. Keep the source text unchanged.
- In one job the user needed the numeral on the right of its noun; check the specific number/unit order with a native speaker or the user.
- Coordinate entrance timing (number first was accepted) and inspect transient overlaps during the entrance, not only final bounds.
- Do not infer mixed-number correctness from correct Arabic shaping. Check native look, exported frames and the Resolve composite.

## 4. Layout of RTL groups

- Measure every run with native bounds, then centre the number/unit/label group by its combined measured width. Accepted gaps: number/unit 22–40 px; tight label groups 24 px (after the user rejected 94–113 px).
- Fitted translucent plates: at least 20 px clearance around payment/area text, at least 10 px around labels.
- Right-align Arabic to a shared edge with the icon beside it (one job: text anchors x 738, icons x 816 on 1080 wide).
- RTL direction does not reorder a card group. When mirroring an accumulating group (first item on the right), move icons, containers and labels together.
- A flag or icon that belongs to one word: start its reveal on that word's delayed stagger start (e.g. frame 60 for the second word), not the clip's first frame; end it with its phrase.
- Sizing an imported image: measure its scale-1 probe width, multiply by the asset's alpha-bbox-width / file-width ratio, then scale to the wanted visible width. File width alone gave undersized flags.
- A generated "transparent" cutout can still contain a background wash. Check the alpha footprint, not just the presence of an alpha channel.
- `cc_scene` `flow` supports RTL row order.

## 5. Colour conversion

Current builds: give hex to `cc_scene` (BT.709 transfer); do not linearise twice.

For raw writes, colours are linear light encoded with Rec.709. For an 8-bit display value v, c = v/255:
`linear = c/4.5` if c < 0.081, else `((c + 0.099)/1.099)^(1/0.45)`.

- Superseded: an early pre-release build's live conventions said sRGB. sRGB-decoding a navy `#282965` exported as RGB(24,25,87) instead of (40,41,101); inverse Rec.709 gave the exact (40,41,101). A later pre-release build's conventions already describe inverse Rec.709.
- Always confirm a brand colour by reading actual exported PNG pixels.

## 6. PNG delivery of RTL work

Use the native export route in [export-and-delivery.md](export-and-delivery.md) and placement in [resolve-handoff.md](resolve-handoff.md). RTL-specific checks:
- Sample entrance frames of every multiword line on disk and in Resolve: the first word appears on the right, later words build to the left.
- Check mixed-number digit order in the Resolve composite.
- Check Arabic shaping and ligatures at full resolution.

## 7. Fusion transfer: the RTL stagger workaround

Applies to Carvercat an early 0.1.4 pre-release build with Resolve Studio 21.1.0.14. Status: open, temporary destination-only fix ([KI-080](../known-issues.md#ki-080)).

Symptom: native Arabic word entrances read right-to-left, but after native Fusion transfer an intermediate frame reveals the LEFT word first. Glyph shaping and the final string are correct. The defect is the mapping of character-index delay tables between native and Fusion text layout.

Fix inside each destination Fusion graph:
1. Find the Follower curve through the connected input: `DelayByCharacterPosition.GetConnectedOutput().GetTool()`. The live modifier name is normalised on import (seen `Obj6FollowerDelaybyCharacterPosition`), so do not use the compiler's pre-import name.
2. Mirror the delay function by character index: `Dnew(i) = Dold(N-1-i)`. Use stepped keys so all characters of a word share one delay. Example for 8 characters: `[[0,0],[3,4],[6,8]]` → `[[0,8],[2,4],[5,0]]`.
3. Keep the text string, font, placement, opacity/offset splines and clip ranges unchanged.
4. Only variable-delay Arabic Followers need this (36 in one nine-clip job). Flat-delay Arabic Followers (25 there) and numeric/Latin-only text need no inversion.
5. Keep the measured manual Follower **Order 6**. UI labels suggest Order 7, but Order 7 removed the stagger in a real trial. Do not map enum labels to numbers without a frame check.
6. `BezierSpline.SetKeyFrames` returns `None` on success: read back exact keys. `SaveSettings` needed an `OrderedDict` in Python `__main__`.
7. Verify real entry frames per comp, then save/close/reopen the Resolve project and confirm the corrected tables survived. Export original and corrected `.setting` files to the job folder.

Resending from the unchanged source recreates the defect; reapply the tables (and any irregular speech schedule) after every resend. This is not a certification of general mixed-direction or ligature parity.

## 8. Windows text-encoding traps

- Windows Python consoles default to cp1252 and fail printing Arabic (`UnicodeEncodeError`). Use `python -X utf8`, write JSON as UTF-8, or print with JSON escaping. A print error after a mutation does not mean the mutation failed: inspect state.
- Never interpolate Arabic (or any artwork text) into PowerShell commands; pass UTF-8 JSON through stdin or structured arguments. Generate derived scripts from saved Python files.
