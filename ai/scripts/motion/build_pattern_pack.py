"""Build the Motion Patterns preset pack (Carvercat .carverpreset files) from
the curve vocabulary in curves.py.

    python build_pattern_pack.py OUT_DIR [--tol 0.01]

Each preset is a spec below: lanes of (property, from, to, curve, start, end)
where start/end are fractions of the preset span (a lane can occupy part of
it, e.g. a fade over the first 40%). Curves are baked to keys with LINEAR
joins, because Carvercat preset keys accept only the named easings
(Linear / Ease in / Ease out / S-curve / Hold) and anything else silently
falls back to Linear. Values are RELATIVE to the object (positions/angles
add, size/opacity/scaleX/scaleY multiply) - Carvercat's rule.

The FIRST tag is the Library shelf (in / out / stagger), so staggered presets lead with "stagger".

Carvercat position offsets are in frame fractions with Y UP (Fusion space):
[0, -0.04] starts 4% of the frame height BELOW the rest position.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from curves import named, bake, spring, bezier

C = named

def lane(prop, frm, to, curve="expo-out", start=0.0, end=1.0):
    return dict(prop=prop, frm=frm, to=to, curve=curve, start=start, end=end)

def fade_in(end=0.5, curve="standard"):  return lane("blend", 0.0, 1.0, curve, 0.0, end)
def fade_out(start=0.5, curve="emphasized-accel"): return lane("blend", 1.0, 0.0, curve, start, 1.0)

P = []
def preset(pid, name, anchor, frames, lanes, tags, note, only=None, stagger=None):
    P.append(dict(pid=pid, name=name, anchor=anchor, frames=frames, lanes=lanes,
                  tags=tags, note=note, only=only, stagger=stagger))

# ---------------------------------------------------------------- entrances
preset("mp_rise_expo", "Rise - expo", "in", 18,
       [lane("center", [0, -0.045], [0, 0], "expo-out"), fade_in(0.45)],
       ["in", "rise", "expo"], "Fast start, long soft landing (expo-out). The default entrance for anything that is not a hero.")
preset("mp_slide_left_expo", "Slide from left - expo", "in", 20,
       [lane("center", [-0.09, 0], [0, 0], "expo-out"), fade_in(0.4)],
       ["in", "slide", "left", "expo"], "Enters from the left with an expo-out landing. Pair with an exit to the right for continuity.")
preset("mp_slide_right_expo", "Slide from right - expo", "in", 20,
       [lane("center", [0.09, 0], [0, 0], "expo-out"), fade_in(0.4)],
       ["in", "slide", "right", "expo"], "Enters from the right with an expo-out landing.")
preset("mp_pop_spring", "Pop - spring", "in", 24,
       [lane("size", 0.0, 1.0, "spring-bouncy"), fade_in(0.2, "linear")],
       ["in", "pop", "spring", "overshoot"], "Scale 0 to 1 with a 16% overshoot and one settle - the classic spring pop. Icons, badges, stickers.")
preset("mp_pop_gentle", "Pop - gentle", "in", 20,
       [lane("size", 0.6, 1.0, "spring-gentle"), fade_in(0.35)],
       ["in", "pop", "spring", "subtle"], "From 60% with a 5% overshoot. Cards, photos, UI panels - premium rather than playful.")
preset("mp_stamp", "Stamp", "in", 14,
       [lane("size", 1.9, 1.0, "spring-gentle"), fade_in(0.18, "linear")],
       ["in", "stamp", "slam", "logo"], "Slams down from 190% and settles with a small rebound. Logos, prices, a single hero word. Add an impact SFX on the landing frame (~frame 4).")
preset("mp_drop_bounce", "Drop - bounce", "in", 24,
       [lane("center", [0, 0.28], [0, 0], "bounce"), fade_in(0.1, "linear")],
       ["in", "drop", "bounce", "playful"], "Falls from above and bounces three times. Playful brands only.")
preset("mp_swing_in", "Swing in", "in", 26,
       [lane("angle", -16, 0, "spring-bouncy"), lane("size", 0.9, 1.0, "expo-out"), fade_in(0.3)],
       ["in", "rotate", "spring"], "Rotates in from -16 deg and settles past zero once. Tags, labels, stickers.")
preset("mp_flip_in_x", "Flip in (X)", "in", 20,
       [lane("scaleX", 0.0, 1.0, "spring-gentle"), fade_in(0.25, "linear")],
       ["in", "flip", "card"], "Opens horizontally like a card turning. Works on cards and icons; avoid on long text.")
preset("mp_grow_y", "Grow up (Y)", "in", 16,
       [lane("scaleY", 0.0, 1.0, "expo-out")],
       ["in", "grow", "bar", "chart"], "Scale Y from 0. Set the anchor to the bottom edge first so it grows upward (bars, columns).")
preset("mp_grow_x", "Grow across (X)", "in", 18,
       [lane("scaleX", 0.0, 1.0, "expo-out")],
       ["in", "grow", "underline", "progress"], "Scale X from 0. Set the anchor to the left edge first so it draws across (underlines, progress bars, dividers).")
preset("mp_zoom_settle", "Zoom settle", "in", 20,
       [lane("size", 1.22, 1.0, "expo-out"), fade_in(0.4)],
       ["in", "zoom", "photo"], "Arrives from 122% and settles. Photos, product shots, backgrounds.")

# ---------------------------------------------------------------- exits
preset("mp_exit_up_accel", "Exit up - accelerate", "out", 12,
       [lane("center", [0, 0], [0, 0.05], "emphasized-accel"), fade_out(0.35)],
       ["out", "rise", "accelerate"], "Leaves upward, accelerating. Exits are ~70% of their entrance duration.")
preset("mp_exit_down_accel", "Exit down - accelerate", "out", 12,
       [lane("center", [0, 0], [0, -0.05], "emphasized-accel"), fade_out(0.35)],
       ["out", "sink", "accelerate"], "Leaves downward, accelerating.")
preset("mp_exit_left_accel", "Exit left - accelerate", "out", 14,
       [lane("center", [0, 0], [-0.1, 0], "emphasized-accel"), fade_out(0.4)],
       ["out", "slide", "left"], "Leaves to the left, accelerating. Pair with Slide from right on the next item for a push.")
preset("mp_exit_shrink_anticipate", "Exit shrink - anticipate", "out", 14,
       [lane("size", 1.0, 0.0, "anticipate-out"), fade_out(0.6)],
       ["out", "shrink", "anticipation"], "Swells 8% (wind-up) then shrinks away fast. Icons, badges.")
preset("mp_exit_fade_fast", "Exit fade - fast", "out", 8,
       [lane("blend", 1.0, 0.0, "emphasized-accel")],
       ["out", "fade"], "A quick accelerating fade. Use for supporting elements under a stronger exit.")
preset("mp_exit_zoom_through", "Exit zoom through", "out", 12,
       [lane("size", 1.0, 2.4, "emphasized-accel"), fade_out(0.45)],
       ["out", "zoom", "transition"], "Pushes toward camera and fades. Combine with the next scene's Zoom settle for a zoom-through transition.")

# ---------------------------------------------------------------- kinetic text (staggered)
preset("mp_text_word_rise", "Words rise - expo", "in", 16,
       [lane("center", [0, -0.03], [0, 0], "expo-out"), fade_in(0.5)],
       ["in", "stagger", "word", "expo"], "Word by word, rising with an expo-out landing. The workhorse headline entrance.",
       only="text", stagger=dict(by="word", order="forward", gap=3))
preset("mp_text_char_cascade", "Letters cascade - spring", "in", 20,
       [lane("center", [0, 0.035], [0, 0], "spring-gentle"), fade_in(0.3)],
       ["in", "stagger", "character", "spring"], "Letters drop from above in order with a soft spring. Short words (under ~14 characters).",
       only="text", stagger=dict(by="character", order="forward", gap=2))
preset("mp_text_word_pop", "Words pop - spring", "in", 22,
       [lane("size", 0.0, 1.0, "spring-bouncy"), fade_in(0.2, "linear")],
       ["in", "stagger", "word", "pop", "spring"], "Each word pops from zero with overshoot. Energetic, social-first copy.",
       only="text", stagger=dict(by="word", order="forward", gap=4))
preset("mp_text_line_reveal", "Lines reveal - decelerate", "in", 20,
       [lane("center", [0, -0.025], [0, 0], "emphasized-decel"), fade_in(0.5)],
       ["in", "stagger", "line", "editorial"], "Line by line, calm and editorial. Body copy, quotes, multi-line statements.",
       only="text", stagger=dict(by="line", order="forward", gap=6))
preset("mp_text_char_shimmer", "Letters shimmer in", "in", 10,
       [lane("blend", 0.0, 1.0, "standard")],
       ["in", "stagger", "character", "random", "fade"], "Letters fade on in random order. Luxury, quiet reveals.",
       only="text", stagger=dict(by="character", order="random", gap=1))
preset("mp_text_word_swing", "Words swing in", "in", 24,
       [lane("angle", 12, 0, "spring-bouncy"), lane("center", [0, -0.02], [0, 0], "expo-out"), fade_in(0.3)],
       ["in", "stagger", "word", "rotate"], "Each word tips up from 12 deg and settles. Playful titles.",
       only="text", stagger=dict(by="word", order="forward", gap=4))
preset("mp_text_word_exit_up", "Words exit up", "out", 12,
       [lane("center", [0, 0], [0, 0.03], "emphasized-accel"), fade_out(0.3)],
       ["out", "stagger", "word"], "Word by word, leaving upward and accelerating.",
       only="text", stagger=dict(by="word", order="forward", gap=2))


def interp(a, b, p):
    if isinstance(a, list): return [round(x + (y - x) * p, 5) for x, y in zip(a, b)]
    return round(a + (b - a) * p, 5)

def lane_keys(l, frames, tol):
    span = (l["end"] - l["start"]) * frames
    pts = bake(C[l["curve"]], max(2, round(span)), tol)
    keys = []
    if l["start"] > 0: keys.append(dict(at=0, value=l["frm"], easing="Linear"))
    for t, p in pts:
        at = round(l["start"] + t * (l["end"] - l["start"]), 4)
        keys.append(dict(at=at, value=interp(l["frm"], l["to"], p), easing="Linear"))
    if l["end"] < 1: keys.append(dict(at=1, value=l["to"], easing="Linear"))
    # dedupe by at
    out = []
    for k in keys:
        if out and out[-1]["at"] == k["at"]: out[-1] = k
        else: out.append(k)
    return out

def build(out_dir, tol):
    os.makedirs(out_dir, exist_ok=True)
    for p in P:
        d = {"presetVersion": 2, "id": "cc.mp." + p["pid"][3:], "name": p["name"], "category": "animation",
             "tags": (["stagger"] + [t for t in p["tags"] if t != "stagger"] if p["stagger"] else p["tags"]) + ["motion patterns"], "note": p["note"] + " Curve baked as keys (linear joins) - see the skill's patterns/ docs.",
             "anchor": p["anchor"], "frames": p["frames"],
             "tracks": [{"property": l["prop"], "keys": lane_keys(l, p["frames"], tol)} for l in p["lanes"]]}
        if p["only"]: d["only"] = p["only"]
        if p["stagger"]: d["stagger"] = p["stagger"]
        with open(os.path.join(out_dir, p["pid"] + ".carverpreset"), "w") as f:
            json.dump(d, f, indent=1)
    pack = {"packVersion": 1, "id": "cc.motion-patterns", "name": "Motion Patterns", "origin": "carvercat-skills",
            "version": 1, "tier": "free",
            "note": "Springs, expo landings, anticipation and staggered type, baked from the carvercat-skills curve vocabulary. Source: carvercat-skills/ai/scripts/motion/build_pattern_pack.py"}
    with open(os.path.join(out_dir, "pack.carverpack"), "w") as f: json.dump(pack, f, indent=1)
    return len(P)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "motion-patterns"
    tol = float(sys.argv[sys.argv.index("--tol") + 1]) if "--tol" in sys.argv else 0.01
    print(build(out, tol), "presets ->", out)


def previews(out_dir):
    """500x500 card per preset: each lane's progress curve (0 -> 1, overshoot shown)."""
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        print("Pillow not installed - previews skipped"); return
    cols = [(250, 191, 46), (120, 170, 255), (230, 230, 230)]
    for p in P:
        im = Image.new("RGB", (500, 500), (9, 10, 16)); d = ImageDraw.Draw(im)
        x0, x1, y0, y1 = 40, 460, 380, 120          # y0 = progress 0, y1 = progress 1
        for gy in (y0, y1): d.line([(x0, gy), (x1, gy)], fill=(45, 48, 60), width=2)
        for i, l in enumerate(p["lanes"]):
            c = C[l["curve"]]; pts = []
            for k in range(201):
                t = k / 200
                u = 0 if t < l["start"] else 1 if t > l["end"] else (t - l["start"]) / max(1e-9, l["end"] - l["start"])
                v = c(u)
                if p["anchor"] == "out": v = v  # exits plot progress towards the exit value
                pts.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * v))
            d.line(pts, fill=cols[i % 3], width=5 if i == 0 else 3)
        d.text((x0, 30), p["name"], fill=(240, 240, 240))
        lanes = ", ".join(f"{l['prop']}:{l['curve']}" for l in p["lanes"])
        d.text((x0, 52), f"{p['anchor']} - {p['frames']} f" + (f" - stagger {p['stagger']['by']}/{p['stagger']['gap']}f" if p['stagger'] else ""), fill=(160, 160, 170))
        d.text((x0, 420), lanes[:70], fill=(160, 160, 170))
        im.save(os.path.join(out_dir, p["pid"] + ".png"))


if __name__ == "__main__" and "--previews" in sys.argv:
    previews(sys.argv[1])
    print("previews written")
