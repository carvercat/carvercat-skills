import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recipe_kit import *
p = LAB + "/rc_retro.carverproj"
N = 384
author(p, "Retro night promo 13s", N, '#1A0B2E')
SHOTS = [("Chrome title", 0, 2), ("Neon sign", 90, 2), ("Arcade start screen", 210, 2), ("TV switch-off", 360, 2), ("Venetian blinds", 184, 3)]
with client() as c:
    place_all(c, p, "Retro night promo 13s", SHOTS, "rc_retro", n=N)
