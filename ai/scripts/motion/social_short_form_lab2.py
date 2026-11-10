"""Social Short-form round 2 in design units (vertical 1080 x 1920): eight more lab comps (name tag, listicle, before/after,
poll sticker, countdown, post card, highlight caption, swipe-up transition).

    import social_short_form_lab2 as L; doc = L.build(); doc.send(client, PROJECT.carverproj)

Same palette, vertical authoring and safe-area rules as social_short_form_lab.py: everything inside the social safe box SAFE,
and nothing right of x 851 below y 1151 (the button column). Check with carvercat_inspect, carvercat_look and carvercat_authoring
validate (bounds_inside SAFE); extract templates with regen_pack.py. Docs: ai/patterns/social-short-form.md.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from social_short_form_lab import (SDoc, COL, EXPO, BACK, SAFE, W, H, comp, lab_bg, outline, text, line, css, BEZ, anchor)
from cc import textw

ACCEL, SMOOTH = BEZ['accel'], BEZ['smooth']


def grow_x(o, f, d=10, ax=-1):
    anchor(o, ax, 0); o.scale([(f, [0.0, 1.0], 'Linear'), (f + d, [1.0, 1.0], EXPO)]); return o


def name_tag(d):
    n = 120
    k = comp(d, "SS Name tag", n, "snt"); lab_bg(k, n)
    grow_x(k.rect("Tag", 120, 960, 560, 150, COL['white'], r=36, f0=0, dur=n), 0, 10)
    d.preset(k, text(k, "Tag name", "Maya Ortiz", 160, 1010, 56, COL['black'], f0=4, dur=n - 4, style='ExtraBold', align='left'), "Hook punch")
    d.preset(k, text(k, "Tag handle", "@mayamakes", 160, 1070, 38, COL['pink'], f0=8, dur=n - 8, style='Bold', align='left'), "Hook punch")


def listicle(d):
    n = 150
    k = comp(d, "SS Listicle", n, "sli"); lab_bg(k, n)
    d.preset(k, text(k, "List header", "3 THINGS\nI WISH I KNEW", 540, 420, 96, COL['white'], f0=0, dur=n, style='ExtraBold', lh=1.05), "Hook punch")
    for i, s in enumerate(["Start before you're ready", "Post every day", "Reply to every comment"]):
        y, f = 700 + i * 150, 24 + i * 30
        b = k.ell(f"Badge {i + 1}", 170, y, 96, 96, COL['pink'], f0=f, dur=n - f)
        b.scale([(f, 0.0, 'Linear'), (f + 10, 1.0, BACK)])
        d.preset(k, text(k, f"Badge num {i + 1}", str(i + 1), 170, y, 56, COL['white'], f0=f + 2, dur=n - f - 2, style='ExtraBold'), "Hook punch")
        d.preset(k, text(k, f"Tip {i + 1}", s, 250, y, 50, COL['white'], f0=f + 4, dur=n - f - 4, style='Bold', align='left'), "Caption words pop")


def before_after(d):
    n = 120
    k = comp(d, "SS Before after", n, "sba"); lab_bg(k, n)
    d.preset(k, k.rect("Before panel", 80, 290, 920, 560, css('2A2833'), r=28, f0=0, dur=n), "Hook punch")          # stand-ins for two clips
    d.preset(k, k.rect("After panel", 80, 900, 920, 560, css('3A2F55'), r=28, f0=16, dur=n - 16), "Whip in - left")
    for name, txt, y, f, col in [("Before label", "BEFORE", 360, 6, COL['white']), ("After label", "AFTER", 970, 22, COL['yellow'])]:
        o = text(k, name, txt, 130, y, 64, col, f0=f, dur=n - f, style='ExtraBold', align='left'); outline(o)
        d.preset(k, o, "Hook punch")


def poll(d):
    n = 150
    k = comp(d, "SS Poll", n, "spl"); lab_bg(k, n)
    d.preset(k, k.rect("Poll card", 540, 820, 820, 560, COL['white'], r=40, f0=0, dur=n, center=True), "Hook punch")
    d.preset(k, text(k, "Question", "Coffee or tea?", 540, 640, 64, COL['black'], f0=4, dur=n - 4, style='ExtraBold'), "Caption words pop")
    for i, (opt, v, col) in enumerate([("Coffee", 0.62, COL['pink']), ("Tea", 0.38, css('6C5CE7'))]):
        y, f = 790 + i * 170, 30 + i * 6
        d.preset(k, k.rect(f"Track {i + 1}", 190, y - 55, 700, 110, css('EDEBF2'), r=30, f0=10, dur=n - 10), "Hook punch")
        grow_x(k.rect(f"Bar {i + 1}", 190, y - 55, 700 * v, 110, col, r=30, f0=f, dur=n - f), f, 18)
        d.preset(k, text(k, f"Option {i + 1}", opt, 230, y, 48, COL['white'], f0=f + 6, dur=n - f - 6, style='Bold', align='left'), "Hook punch")   # white on the bar: wait for it
        d.preset(k, text(k, f"Percent {i + 1}", f"{round(v * 100)}%", 850, y, 48, COL['black'], f0=f + 14, dur=n - f - 14, style='ExtraBold', align='right'), "Hook punch")


def countdown(d):
    per = 25
    n = per * 4
    k = comp(d, "SS Countdown", n, "scd"); lab_bg(k, n)
    for i, s in enumerate(["3", "2", "1", "GO"]):
        f = i * per
        ring = k.ell(f"Ring {i + 1}", 540, 900, 420, 420, None, f0=f, dur=per); ring.stroke(COL['pink'] if s == "GO" else COL['white'], 14)
        ring.rotv(-90.0); ring.trim([(f, 1.0, 'Linear'), (f + per, 0.0, 'Linear')], which='start')   # draws round as the beat runs
        o = text(k, f"Count {i + 1}", s, 540, 900, 300 if s != "GO" else 220, COL['yellow'] if s == "GO" else COL['white'], f0=f, dur=per,
                 style='ExtraBold')
        o.scale([(f, 1.35, 'Linear'), (f + 8, 1.0, EXPO)])        # a hard cut in, no fade: readable for all 25 f


def post_card(d):
    n = 150
    k = comp(d, "SS Post card", n, "spc"); lab_bg(k, n)
    d.preset(k, k.rect("Post", 540, 820, 860, 520, COL['white'], r=36, f0=0, dur=n, center=True), "Hook punch")
    d.preset(k, k.ell("Post avatar", 190, 640, 96, 96, COL['pink'], f0=4, dur=n - 4), "Hook punch")
    d.preset(k, text(k, "Post name", "Maya Ortiz", 260, 620, 40, COL['black'], f0=6, dur=n - 6, style='ExtraBold', align='left'), "Hook punch")
    d.preset(k, text(k, "Post handle", "@mayamakes", 260, 672, 30,   # audit 2026-10-28: 10.7 px gap to the name before
                     css('6B6880'), f0=8, dur=n - 8, style='Medium', align='left'), "Hook punch")
    d.preset(k, text(k, "Post text", "Nobody talks about how\nmuch editing is just\ndeleting things.", 150, 830, 52, COL['black'], f0=14, dur=n - 14,
                     style='Bold', align='left', lh=1.15), "Caption words pop")
    d.preset(k, text(k, "Post stats", "12.4K likes", 150, 1010, 30, css('6B6880'), f0=50, dur=n - 50, style='Medium', align='left'), "Hook punch")


HC_PX = 72


def highlight_caption(d):
    n = 90
    k = comp(d, "SS Highlight caption", n, "shc"); lab_bg(k, n)
    parts = ["this is", "actually", "free"]
    sp = textw(" ", HC_PX, 'ExtraBold'); ws = [textw(s, HC_PX, 'ExtraBold') for s in parts]
    x0 = 490 - (sum(ws) + 2 * sp) / 2                                   # centred at x 490, like the caption pages
    xs = [x0, x0 + ws[0] + sp, x0 + ws[0] + ws[1] + 2 * sp]
    y = 1250
    hl = k.rect("Caption highlight", xs[1] - 12, y - HC_PX * 0.6, ws[1] + 24, HC_PX * 1.2, COL['pink'], r=14, f0=10, dur=n - 10)
    grow_x(hl, 10, 8)
    for i, (s, x) in enumerate(zip(parts, xs)):
        f = [0, 12, 6][i]
        o = text(k, f"Caption part {i + 1}", s, x, y, HC_PX, COL['white'], f0=f, dur=n - f, style='ExtraBold', align='left')
        outline(o)
        d.preset(k, o, "Caption words pop")


def swipe_up(d):
    n = 24
    k = comp(d, "SS Swipe up", n, "ssu")
    p = k.rect("Swipe panel", 540, 960, 1000, 1000, COL['pink'], f0=0, dur=n, center=True)
    p.sc([1.08, 1.92])                                                   # drawn 1000 px, scaled to 1080 x 1920 (KI-137)
    bx, by = p.base
    p.pos([(0, (bx, by + H), 'Linear'), (10, (bx, by), BEZ['whip']), (14, (bx, by), 'Linear'), (n, (bx, by - H), ACCEL)])
    p.mblur(360)
    p.dirblur_keys([(0, 240, 90, 'Linear'), (10, 0, 90, 'Linear'), (14, 0, 90, 'Linear'), (n, 240, 90, 'Linear')])   # a vertical streak on the swipe


def comps(d):
    name_tag(d); listicle(d); before_after(d); poll(d); countdown(d); post_card(d); highlight_caption(d); swipe_up(d)


def build():
    d = SDoc(); comps(d)
    return d


if __name__ == "__main__":
    print(__doc__)
