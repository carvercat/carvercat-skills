import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recipe_kit import *
p = LAB + "/rc_corp.carverproj"
N = 660
author(p, "Annual report opener 22s", N, '#0B1F3A')
SHOTS = [("Title card - split rule", 0, 2), ("Three stats", 90, 2), ("Chapter title", 180, 2), ("Brand quote", 270, 2),
         ("Team row", 420, 2), ("Brand end card", 540, 2), ("Brand panel wipe", 160, 3), ("Brand panel wipe", 520, 3)]
with client() as c:
    place_all(c, p, "Annual report opener 22s", SHOTS, "rc_corp", n=N)
