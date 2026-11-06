import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recipe_kit import *
p = LAB + "/rc_saas.carverproj"
N = 900
author(p, "SaaS feature launch 30s", N, ['#1B1B4D', '#0E0E2A'])
SHOTS = [("Feature title", 0, 2, (20, 89, 0.03)), ("Chat thread", 90, 2), ("Dropdown menu", 210, 2), ("Modal over app", 300, 2),
         ("Chart card", 390, 2), ("KPI tile", 480, 2, (500, 569, 0.03)), ("Notification toast", 570, 2), ("Stat punch", 690, 2), ("CTA end card", 780, 2),
         ("Slide wipe", 282, 3), ("Slide wipe", 762, 3)]
with client() as c:
    place_all(c, p, "SaaS feature launch 30s", SHOTS, "rc_saas", n=N)
