# Slice shift

**Template** `gl_slice_shift` · Glitch pack · **verified 0.1.6 (rev 1105,; pack added to the bundled Library for the test)**, comp `GL Slice shift`.

A 460 px green hexagon with a white outline stands in for a logo. It is drawn five times, and each copy is masked by one 92 px horizontal band.

| Part | Frames | Motion |
|---|---|---|
| Slice *i* | 12, 15, 18, 21 → 24; 52 → 55 | held sideways jumps of 30–80 px (alternating direction by slice), then realign |

Lint 0/0; qc found no flashes. **To use your logo:** replace each of the five marks with the same logo object at the same position, keep each mask band where it is, and keep each mask object as the `ref` of its mark's `mask` key (`property.set {id:<mark>, key:"mask", value:{"ref":"<mask id>"}}`).
