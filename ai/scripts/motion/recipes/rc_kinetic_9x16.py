import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recipe_kit import *
# A 9:16 re-cut of the kinetic quote reel: the 16:9 type templates fitted and zoomed so their lines fill the width,
# each kept moving with a 3% push, and a 9:16 follow card instead of the wide FOLLOW FOR MORE line.
p = LAB + "/rc_kinetic_9x16.carverproj"
N = 520
author(p, "Quote reel 9x16 17s", N, '#0B0B0F', w=1080, h=1920)
SHOTS = [("Focus pull", 0, 2, (0, 59, 0.03), 2.2), ("Word swap", 60, 2, (60, 179, 0.03), 1.9),
         ("Kinetic quote", 180, 2, (180, 329, 0.03), 1.55), ("Beat words", 330, 2, (330, 429, 0.03), 2.0),
         ("Follow end card (9:16)", 430, 2), ("Swipe up (9:16)", 168, 3)]
with client() as c:
    place_all(c, p, "Quote reel 9x16 17s", SHOTS, "rc_kinetic_9x16", n=N)
