import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recipe_kit import *
p = LAB + "/rc_glitch.carverproj"
N = 430
author(p, "Music teaser 14s", N, '#0A0A0A')
SHOTS = [("Stutter words", 0, 2), ("Block artifact title", 100, 2), ("RGB split mark", 190, 2), ("Terminal type-on", 280, 2), ("Tracking band", 0, 3), ("Pixel dissolve", 171, 4)]
with client() as c:
    place_all(c, p, "Music teaser 14s", SHOTS, "rc_glitch", n=N, finish=lambda c: add_grain(c, "0.1 2.5px softness=0.2 colour=0.6", N))
