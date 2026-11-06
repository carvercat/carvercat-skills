import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recipe_kit import *
p = LAB + "/rc_social.carverproj"
N = 465
author(p, "Tip reel 9x16 15s", N, '#111014', w=1080, h=1920)
SHOTS = [("Hook title (9:16)", 0, 2), ("Listicle (9:16)", 75, 2), ("Poll sticker (9:16)", 225, 2), ("Follow end card (9:16)", 375, 2),
         ("Swipe up (9:16)", 213, 3), ("Swipe up (9:16)", 363, 3)]
with client() as c:
    place_all(c, p, "Tip reel 9x16 15s", SHOTS, "rc_social", n=N)
