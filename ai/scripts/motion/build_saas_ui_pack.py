"""Build the SaaS UI preset pack (library/templates/saas-ui/, prefix su_).

    python build_saas_ui_pack.py OUT_DIR

Same method as build_pattern_pack.py: curves from curves.py are baked to keys
with LINEAR joins (preset keys accept only the named easings). Values are
RELATIVE to the object: positions/angles add, size/opacity multiply.
Positions are frame fractions with Y UP. The templates in this pack are
extracted from built and checked lab comps with comp_to_template.py; the
pack's docs are ai/patterns/su-*.md.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pattern_pack import lane, fade_in, fade_out, lane_keys

P = []
def preset(pid, name, anchor, frames, lanes, tags, note):
    P.append(dict(pid=pid, name=name, anchor=anchor, frames=frames, lanes=lanes, tags=tags, note=note))

preset("su_toast_drop", "Toast drop - spring", "in", 20,
       [lane("center", [0, 0.06], [0, 0], "spring-gentle"), fade_in(0.3)],
       ["in", "toast", "notification", "drop", "spring"],
       "Drops 6% of the frame height from above and settles with a small spring. Notifications, toasts, banners at the top of a UI.")
preset("su_toast_exit_up", "Toast exit up", "out", 10,
       [lane("center", [0, 0], [0, 0.06], "emphasized-accel"), fade_out(0.3)],
       ["out", "toast", "notification", "accelerate"],
       "Leaves upward, accelerating, the way it came in. Pair with Toast drop - spring.")
preset("su_card_lift", "Card lift", "in", 18,
       [lane("center", [0, -0.03], [0, 0], "expo-out"), lane("size", 0.94, 1.0, "expo-out"), fade_in(0.4)],
       ["in", "card", "modal", "lift", "expo"],
       "Rises 3% while growing from 94% on an expo landing. Cards, modals, dashboard tiles.")
preset("su_modal_dismiss", "Modal dismiss", "out", 9,
       [lane("size", 1.0, 0.95, "emphasized-accel"), fade_out(0.2)],
       ["out", "modal", "card", "dismiss"],
       "Shrinks to 95% and fades, accelerating. Closing a modal, card or popover.")
preset("su_panel_in_left", "Panel in - left", "in", 22,
       [lane("center", [-0.25, 0], [0, 0], "expo-out")],
       ["in", "panel", "sidebar", "drawer", "expo"],
       "Travels a quarter of the frame width from the left with no fade, like a drawer. Sidebars and side panels; start it under a frame edge or a mask.")
preset("su_panel_out_left", "Panel out - left", "out", 14,
       [lane("center", [0, 0], [-0.25, 0], "emphasized-accel")],
       ["out", "panel", "sidebar", "drawer", "accelerate"],
       "The drawer closing: a quarter frame width to the left, accelerating, no fade.")
preset("su_tap_ripple", "Tap ripple", "in", 18,
       [lane("size", 0.25, 1.0, "expo-out"), lane("blend", 0.7, 0.0, "standard", 0.15, 1.0)],
       ["in", "tap", "ripple", "click", "cursor"],
       "Grows from 25% and fades out: the ring under a click. Put a ring clip that starts on the tap frame and is 18 f long; it ends invisible.")

def build(out_dir, tol=0.01):
    os.makedirs(out_dir, exist_ok=True)
    for p in P:
        d = {"presetVersion": 2, "id": "cc.su." + p["pid"][3:], "name": p["name"], "category": "animation",
             "tags": p["tags"] + ["saas ui"],
             "note": p["note"] + " Curve baked as keys (linear joins) - see the skill's ai/patterns/su-*.md docs.",
             "anchor": p["anchor"], "frames": p["frames"],
             "tracks": [{"property": l["prop"], "keys": lane_keys(l, p["frames"], tol)} for l in p["lanes"]]}
        with open(os.path.join(out_dir, p["pid"] + ".carverpreset"), "w") as f:
            json.dump(d, f, indent=1)
    pack = {"packVersion": 1, "id": "cc.saas-ui", "name": "SaaS UI", "origin": "carvercat-skills", "version": 1,
            "tier": "free",
            "note": "Product-UI motion: toasts, cards, modals, drawers, cursor clicks, toggles and KPI tiles. Source: carvercat-skills/ai/scripts/motion/build_saas_ui_pack.py and the lab comps in categories/saas-launch."}
    with open(os.path.join(out_dir, "pack.carverpack"), "w") as f:
        json.dump(pack, f, indent=1)
    return len(P)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "saas-ui"
    print(build(out), "presets ->", out)
