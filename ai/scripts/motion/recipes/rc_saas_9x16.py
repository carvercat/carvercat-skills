import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recipe_kit import *
# A 9:16 re-cut of the SaaS launch: 9:16 hook, caption and swipes; the 16:9 product templates are placed into the
# vertical comp (template.apply fits them into a 1080 x 608 band), zoomed on their content and kept moving with a
# 3% push (a zoomed instance held still is larger than the frame: lint cropped_at_rest).
p = LAB + "/rc_saas_9x16.carverproj"
N = 555
author(p, "SaaS launch 9x16 18s", N, ['#1B1B4D', '#0E0E2A'], w=1080, h=1920)
SHOTS = [("Hook title (9:16)", 0, 2), ("Highlight caption (9:16)", 75, 2),
         ("Chart card", 165, 2, (165, 254, 0.03), 2.4), ("KPI tile", 255, 2, (255, 344, 0.03), 3.4),
         ("Stat punch", 345, 2, (345, 434, 0.03), 2.8), ("CTA end card", 435, 2, (435, 554, 0.03), 2.2),
         ("Swipe up (9:16)", 153, 3), ("Swipe up (9:16)", 423, 3)]
with client() as c:
    place_all(c, p, "SaaS launch 9x16 18s", SHOTS, "rc_saas_9x16", n=N)
