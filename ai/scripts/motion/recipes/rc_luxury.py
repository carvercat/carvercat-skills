import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recipe_kit import *
p = LAB + "/rc_luxury.carverproj"
N = 840
author(p, "Product teaser 28s", N, '#0E0D0B')
SHOTS = [("Light sweep", 0, 2), ("Collection title", 120, 2), ("Product frame", 270, 2), ("Attribute row", 390, 2), ("Price card", 540, 2), ("Monogram end card", 690, 2), ("Slow dip", 240, 3), ("Slow dip", 660, 3)]
with client() as c:
    place_all(c, p, "Product teaser 28s", SHOTS, "rc_luxury", n=N)
