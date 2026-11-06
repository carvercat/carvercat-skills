import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recipe_kit import *
p = LAB + "/rc_sports.carverproj"
N = 420
author(p, "Sports score update 14s", N, ['#2E7D32', '#1B5E20'])
SHOTS = [("Score bug", 0, 2), ("GOAL slam", 49, 3), ("Replay stinger", 120, 3), ("Player lower third", 150, 2),
         ("Full-time score", 300, 2), ("Slash wipe", 285, 4)]
with client() as c:
    place_all(c, p, "Sports score update 14s", SHOTS, "rc_sports", n=N)
