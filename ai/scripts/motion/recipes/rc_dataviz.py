import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recipe_kit import *
p = LAB + "/rc_dataviz.carverproj"
N = 645
author(p, "Quarterly results 21s", N, ['#152036', '#0B111E'])
SHOTS = [("Line chart - draw", 0, 2), ("Comparison bars", 90, 2), ("Donut - fill", 180, 2), ("Ranked bars", 270, 2), ("Progress rings", 360, 2), ("Data table", 450, 2), ("Gauge", 570, 2), ("Dip to colour", 255, 3)]
with client() as c:
    place_all(c, p, "Quarterly results 21s", SHOTS, "rc_dataviz", n=N)
