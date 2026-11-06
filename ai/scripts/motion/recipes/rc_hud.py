import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recipe_kit import *
p = LAB + "/rc_hud.carverproj"
N = 700
author(p, "Tech trailer 23s", N, '#05080F')
SHOTS = [("Hex grid", 0, 2), ("Target lock", 120, 2), ("Signal bars", 210, 2), ("Map ping", 330, 2), ("Alert banner", 450, 2), ("Segment loader", 570, 2), ("Scan wipe", 316, 3)]
with client() as c:
    place_all(c, p, "Tech trailer 23s", SHOTS, "rc_hud", n=N)
