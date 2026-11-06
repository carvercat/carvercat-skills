"""Build the Kinetic Typography preset pack (library/templates/kinetic-typography/, prefix kt_).

    python build_kinetic_type_pack.py OUT_DIR

Same method as build_pattern_pack.py: curves from curves.py baked to keys with
LINEAR joins; values RELATIVE to the object; positions in frame fractions, Y UP.
Text presets carry a `stagger` block (by word/character/line, gap in frames).
Templates are extracted from the lab comps (kinetic_type_lab.py) with
comp_to_template.py; docs are ai/patterns/kinetic-typography.md and kt-*.md.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pattern_pack import lane, fade_in, fade_out, lane_keys

P = []
def preset(pid, name, anchor, frames, lanes, tags, note, stagger):
    P.append(dict(pid=pid, name=name, anchor=anchor, frames=frames, lanes=lanes, tags=tags, note=note, stagger=stagger))

preset("kt_word_slam", "Words slam", "in", 14,
       [lane("size", 1.8, 1.0, "spring-gentle"), fade_in(0.18, "linear")],
       ["in", "word", "slam", "impact"],
       "Each word drops onto the screen from 180% and settles with a small rebound, 5 f apart. Short punchy lines (2-5 words); hit an impact sound on each landing.",
       dict(by="word", order="forward", gap=5))
preset("kt_char_zoom_in", "Letters zoom in", "in", 16,
       [lane("size", 2.4, 1.0, "expo-out"), fade_in(0.4)],
       ["in", "character", "zoom", "expo"],
       "Letters fly in from 240% toward their place, 1 f apart, on an expo landing. Single words and short titles.",
       dict(by="character", order="forward", gap=1))
preset("kt_char_pop", "Letters pop", "in", 18,
       [lane("size", 0.0, 1.0, "spring-bouncy"), fade_in(0.2, "linear")],
       ["in", "character", "pop", "spring", "playful"],
       "Each letter pops from zero with a 16% spring, 1 f apart. Short words; energetic, social and funky styles. (A per-letter vertical flip is not possible: scaleY cannot be staggered.)",
       dict(by="character", order="forward", gap=1))
preset("kt_word_drop_bounce", "Words drop - bounce", "in", 22,
       [lane("center", [0, 0.05], [0, 0], "bounce"), fade_in(0.1, "linear")],
       ["in", "word", "drop", "bounce", "playful"],
       "Words fall 5% of the frame height and bounce to rest, 4 f apart. Playful and funky styles only.",
       dict(by="word", order="forward", gap=4))
preset("kt_line_slide_left", "Lines slide in - left", "in", 20,
       [lane("center", [-0.06, 0], [0, 0], "expo-out"), fade_in(0.4)],
       ["in", "line", "slide", "expo", "editorial"],
       "Lines slide 6% of the frame width in from the left, 5 f apart. Lists, multi-line statements, left-aligned layouts.",
       dict(by="line", order="forward", gap=5))
preset("kt_word_exit_down", "Words exit down", "out", 12,
       [lane("center", [0, 0], [0, -0.03], "emphasized-accel"), fade_out(0.3)],
       ["out", "word", "accelerate"],
       "Word by word, sinking and accelerating, 2 f apart. Only on text WITHOUT a staggered entrance on its position (one staggered preset per property).",
       dict(by="word", order="forward", gap=2))

def build(out_dir, tol=0.01):
    os.makedirs(out_dir, exist_ok=True)
    for p in P:
        d = {"presetVersion": 2, "id": "cc.kt." + p["pid"][3:], "name": p["name"], "category": "animation",
             "tags": ["stagger"] + [t for t in p["tags"]] + ["kinetic typography"],
             "note": p["note"] + " Curve baked as keys (linear joins) - see the skill's ai/patterns/kinetic-typography.md.",
             "anchor": p["anchor"], "frames": p["frames"], "only": "text", "stagger": p["stagger"],
             "tracks": [{"property": l["prop"], "keys": lane_keys(l, p["frames"], tol)} for l in p["lanes"]]}
        with open(os.path.join(out_dir, p["pid"] + ".carverpreset"), "w") as f:
            json.dump(d, f, indent=1)
    pack = {"packVersion": 1, "id": "cc.kinetic-typography", "name": "Kinetic Typography", "origin": "carvercat-skills",
            "version": 1, "tier": "free",
            "note": "Type as the main actor: slams, zooms, pops, bounces, a word swap, impact stacks, line reveals, beat-cut words and a focus-pull title. Source: carvercat-skills/ai/scripts/motion/build_kinetic_type_pack.py and the lab comps in categories/kinetic-typography."}
    with open(os.path.join(out_dir, "pack.carverpack"), "w") as f:
        json.dump(pack, f, indent=1)
    return len(P)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "kinetic-typography"
    print(build(out), "presets ->", out)
