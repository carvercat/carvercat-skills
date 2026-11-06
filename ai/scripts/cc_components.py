"""Named components in design units. The implementation lives in cc_scene (`Scene.component(name)`); this module
keeps the old import path working.

    from cc_components import Component
    with Component(scene, "Header") as header:
        header.rectangle("Plate", Box(160, 70, 1600, 100), fill="#242424", radius=24)
        header.text("Brand", "carvercat", box=Box(200, 85, 900, 70), size=48, weight=800)
    scene.apply()        # applying again with the same child names updates the same objects

The scene ids are `Header-Plate` and `Header-Brand`; a selector reaches them with `#Header-Plate`.
Gone from the old component: `remove_missing`, `retain`, `modify`, `effect` (use `Scene.set`, `mode: "replace"` of
scene.apply, which removes only objects that carry a scene id the new document leaves out).
"""
from cc_scene import Component  # noqa: F401
