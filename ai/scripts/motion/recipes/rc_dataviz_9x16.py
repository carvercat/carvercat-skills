import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recipe_kit import *
# A 9:16 re-cut of the quarterly results: the 16:9 charts whose text stays readable when fitted and zoomed
# (effective text = template px x 0.5625 x zoom), each kept moving with a 3% push, and a 9:16 follow card.
p = LAB + "/rc_dataviz_9x16.carverproj"
N = 525
author(p, "Quarterly results 9x16 17s", N, ['#152036', '#0B111E'], w=1080, h=1920)
SHOTS = [("Comparison bars", 0, 2, (0, 89, 0.03), 1.5), ("Donut - fill", 90, 2, (90, 179, 0.03), 2.2),
         ("Progress rings", 180, 2, (180, 269, 0.03), 1.45), ("Waffle chart", 270, 2, (270, 359, 0.03), 1.45),
         ("Gauge", 360, 2, (360, 434, 0.03), 2.4), ("Follow end card (9:16)", 435, 2), ("Swipe up (9:16)", 423, 3)]
with client() as c:
    place_all(c, p, "Quarterly results 9x16 17s", SHOTS, "rc_dataviz_9x16", n=N)
