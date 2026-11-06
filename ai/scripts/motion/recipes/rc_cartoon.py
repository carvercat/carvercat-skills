import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recipe_kit import *
p = LAB + "/rc_cartoon.carverproj"
N = 735
author(p, "Kids explainer 24s", N, '#FFF4E0')
SHOTS = [("Boing title", 0, 2), ("Speech bubble", 90, 2), ("Character hop", 180, 2), ("Bouncy list", 270, 2), ("Button press", 390, 2), ("Hanging sign", 450, 2), ("Sticker burst", 540, 2), ("Cartoon end card", 615, 2)]
with client() as c:
    place_all(c, p, "Kids explainer 24s", SHOTS, "rc_cartoon", n=N)
