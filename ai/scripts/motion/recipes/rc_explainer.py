import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recipe_kit import *
p = LAB + "/rc_explainer.carverproj"
N = 750
author(p, "How it works 25s", N, '#F7F7FA')
SHOTS = [("Key term card", 0, 2), ("Flow diagram", 150, 2), ("Process steps", 300, 2), ("Checklist", 420, 2), ("Quiz question", 570, 2), ("Dip to colour", 285, 3)]
with client() as c:
    place_all(c, p, "How it works 25s", SHOTS, "rc_explainer", n=N)
