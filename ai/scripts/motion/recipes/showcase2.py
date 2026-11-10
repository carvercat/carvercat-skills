"""Round-2 showcases: one master per style family, the family's round-2 templates placed back to back
from the Library (library.place + template.apply), plus the family's own transition at one cut.

    CARVERCAT_EXE=... CARVERCAT_STATE=... RECIPE_LAB=... python showcase2.py saas-ui kinetic-typography ...
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recipe_kit import *

FAMILIES = {
    "saas-ui": ("SaaS UI showcase 2", ['#1B1B4D', '#0E0E2A'], 1920, 1080,
                [("Feature title", 90), ("SaaS lower third", 150), ("Chat thread", 120), ("Dropdown menu", 90), ("Modal over app", 90),
                 ("Chart card", 90), ("CTA end card", 120)], None),
    "kinetic-typography": ("Kinetic Typography showcase 2", '#0B0B0F', 1920, 1080,
                [("Split title", 90), ("Line reveal", 60), ("Highlight sweep", 90), ("Kinetic lower third", 150), ("Stat punch", 90), ("Numbered list", 120),
                 ("Kinetic quote", 150), ("Follow end card", 120)], None),
    "data-viz": ("Data Viz showcase 2", ['#152036', '#0B111E'], 1920, 1080,
                [("Column chart", 90), ("Stacked bar", 90), ("Progress rings", 90), ("Comparison bars", 90), ("Timeline", 120),
                 ("Waffle chart", 90), ("Area chart", 90), ("Data table", 120)], None),
    "corporate-brand": ("Corporate Brand showcase 2", '#0B1F3A', 1920, 1080,
                [("Chapter title", 90), ("Brand quote", 150), ("Agenda", 150), ("Team row", 120), ("Split screen", 150),
                 ("Leader callout", 120), ("Brand end card", 120)], ("Brand panel wipe", 3, 20)),
    "minimal-luxury": ("Minimal Luxury showcase 2", '#0E0D0B', 1920, 1080,
                [("Light sweep", 120), ("Collection title", 150), ("Luxury lower third", 180), ("Price card", 150), ("Attribute row", 150),
                 ("Framed word", 150), ("Slow quote", 150), ("Monogram end card", 150)], ("Slow dip", 4, 30), "0.06 1.5px softness=0.4 colour=0.1"),
    "social-short-form": ("Social Short-form showcase 2", '#111014', 1080, 1920,
                [("Countdown (9:16)", 100), ("Name tag (9:16)", 120), ("Highlight caption (9:16)", 90), ("Before after split (9:16)", 120),
                 ("Post card (9:16)", 150), ("Poll sticker (9:16)", 150), ("Listicle (9:16)", 150)], ("Swipe up (9:16)", 4, 12)),
    "cartoon-bounce": ("Cartoon Bounce showcase 2", '#FFF4E0', 1920, 1080,
                [("Speech bubble", 90), ("Smear whoosh", 45), ("Button press", 60), ("Character hop", 90), ("Hanging sign", 90), ("Bouncy list", 120),
                 ("Ribbon lower third", 150), ("Sticker burst", 75), ("Cartoon end card", 120)], None),
    "funky": ("Funky showcase 2", '#FFE8D6', 1920, 1080,
                [("Swing headline", 90), ("Sale badge", 90), ("Squiggle underline", 90), ("Funky lower third", 150), ("Photo stack", 120),
                 ("Orbit end card", 150)], ("Star cover", 3, 18)),
    "futuristic-hud": ("Futuristic HUD showcase 2", '#05080F', 1920, 1080,
                [("Hex grid", 120), ("HUD ID lower third", 150), ("Segment loader", 130), ("Signal bars", 120), ("Target lock", 90),
                 ("Map ping", 120), ("Alert banner", 120)], ("Scan wipe", 3, 14)),
    "retro": ("Retro showcase 2", '#1A0B2E', 1920, 1080,
                [("Film countdown leader", 120), ("Chrome title", 90), ("Neon sign", 120), ("Arcade start screen", 150), ("VHS overlay", 120), ("Groovy badge", 90),
                 ("70s stripe lower third", 150), ("TV switch-off", 24)], ("Venetian blinds", 5, 26), "0.14 2.5px softness=0.4 colour=0.5"),
    "glitch": ("Glitch showcase 2", '#0A0A0A', 1920, 1080,
                [("Corrupted video title", 120), ("Block artifact title", 90), ("Stutter words", 100), ("Glitch lower third", 150), ("Terminal type-on", 150),
                 ("Error cascade", 120), ("RGB split mark", 90)], ("Pixel dissolve", 4, 19), "0.1 2.5px softness=0.2 colour=0.6"),
    "sports": ("Sports showcase 2", ['#2E7D32', '#1B5E20'], 1920, 1080,
                [("Match up", 90), ("GOAL slam", 60), ("Starting lineup", 150), ("Player spotlight", 120), ("Player lower third", 150), ("Standings table", 150),
                 ("Full-time score", 120)], ("Slash wipe", 2, 15)),
    "explainer": ("Explainer showcase 2", '#F7F7FA', 1920, 1080,
                [("Speaker lower third", 150), ("Key term card", 150), ("Compare columns", 150), ("Flow diagram", 150), ("Checklist", 150),
                 ("Venn diagram", 120), ("Cycle loop", 150), ("Quiz question", 180)], None),
}


def build(key):
    name, bg, w, h, scenes, tx, *rest = FAMILIES[key]
    grain = rest[0] if rest else None                         # a finishing grain layer over the whole master, e.g. "0.1 2px"
    n = sum(d for _, d in scenes)
    p = LAB + f"/sc2_{key}.carverproj"
    author(p, name, n, bg, w=w, h=h)
    shots, f = [], 0
    for t, d in scenes:
        shots.append((t, f, 2)); f += d
    if tx:                                                   # the family's transition centred on the cut after scene tx[1]
        cut = sum(d for _, d in scenes[:tx[1]])
        shots.append((tx[0], cut - tx[2], 3))
    with client() as c:
        place_all(c, p, name, shots, f"sc2_{key}", n=n, finish=(lambda c: add_grain(c, grain, n, w=w, h=h)) if grain else None)
    return p, n


if __name__ == "__main__":
    for key in sys.argv[1:]:
        print("=====", key); print(build(key))
