import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recipe_kit import *
p = LAB + "/rc_funky.carverproj"
N = 540
author(p, "Sale promo 18s", N, '#FFE8D6')
SHOTS = [("Swing headline", 0, 2), ("Sale badge", 90, 2), ("Photo stack", 180, 2), ("Squiggle underline", 300, 2), ("Orbit end card", 390, 2), ("Star cover", 162, 3)]
with client() as c:
    place_all(c, p, "Sale promo 18s", SHOTS, "rc_funky", n=N)
