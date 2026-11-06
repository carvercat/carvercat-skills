import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recipe_kit import *
p = LAB + "/rc_kinetic.carverproj"
N = 550
author(p, "Quote reel 18s", N, '#0B0B0F')
SHOTS = [("Focus pull", 0, 2), ("Word swap", 60, 2), ("Kinetic quote", 180, 2), ("Beat words", 330, 2), ("Follow end card", 430, 2), ("Split doors", 162, 3)]
with client() as c:
    place_all(c, p, "Quote reel 18s", SHOTS, "rc_kinetic", n=N)
