"""Social Short-form lab round 1 in design units (vertical 1080 x 1920; cc2.py: px from the top-left, y down, degrees clockwise,
CSS colours and easing).

    import social_short_form_lab as L; doc = L.build(); doc.send(client, PROJECT.carverproj)

Four comps: hook title, caption pages, progress bar, follow CTA. Rounds 2 and 3 (social_short_form_lab2.py, ..._lab3.py) and the
showcase import the helpers below. The helpers (PDoc with stored-preset application, twos, text placement, model-level
properties) come from retro_lab.py: they are plain design-unit helpers, PDoc.PACK picks the pack whose .carverpreset files are
installed into the scratch Library before the presets are applied.

Safe area for 1080 x 1920 (ai/references/craft/vertical-and-safe-areas.md): everything in x 61-1016, y 268-1538; below y 1151
keep x > 851 clear; captions from x >= 130, <= 790 wide. Fonts: Rethink Sans must be installed (KI-136).
Docs: ai/patterns/social-short-form.md. Rotation is degrees CLOCKWISE (the old kit stored counter-clockwise: angles are negated).
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import retro_lab as R
from retro_lab import EASE_IN, EASE_OUT, SCURVE, twos, hold_keys, anchor, more, line as _line, model_set, css, BEZ, bezier

W, H = 1080, 1920
COL = dict(bg=css('111014'), white=css('FFFFFF'), black=css('000000'), yellow=css('FFE14D'), pink=css('FF3D7F'),
           muted=css('A6A3AE'), card=css('1E1C24'))
EXPO, BACK = BEZ['expo'], BEZ['back']
SAFE = [61, 268, 955, 1270]                  # x, y, w, h of the social safe box


class SDoc(R.PDoc):
    PACK = 'social-short-form'


def comp(d, name, n, code):
    return d.comp(name, n, code, width=W, height=H)


def text(*a, **kw): return R.text(*a, **kw)


def line(k, name, pts, col, px=2, f0=0, dur=None):
    return _line(k, name, pts, col, px, f0=f0, dur=dur)       # scales and turns about the middle of its box


def lab_bg(k, n):
    k.rect("Lab bg", 0, 0, W, H, COL['bg'], f0=0, dur=n)


def outline(o):
    """white caption text with a round black outline, outside the glyphs (the text outline has no design key: model properties)"""
    for key, v in (('paint', 'solid'), ('color', [0.0, 0.0, 0.0]), ('thickness', 0.12), ('align', 'outside'), ('corners', 'round')):
        model_set(o, 'src.e_src_text_outline_{id}.' + key, v)
    return o


def hook_title(d):
    n = 75
    k = comp(d, "SS Hook title", n, "sht"); lab_bg(k, n)
    hl = k.rect("Highlight", 540, 520, 640, 120, COL['pink'], f0=6, dur=n - 6, center=True)
    anchor(hl, -1, 0); hl.scale([(6, [0.0, 1.0], 'Linear'), (14, [1.0, 1.0], EXPO)])
    d.preset(k, text(k, "Hook line 1", "STOP", 540, 380, 150, COL['white'], f0=0, dur=n, style='ExtraBold'), "Hook punch")
    d.preset(k, text(k, "Hook line 2", "SCROLLING", 540, 520, 110, COL['white'], f0=4, dur=n - 4, style='ExtraBold'), "Hook punch")
    d.preset(k, text(k, "Hook sub", "this changes everything", 540, 650, 48, COL['yellow'], f0=14, dur=n - 14, style='Bold'), "Caption words pop")


def caption_pages(d):
    n = 120
    k = comp(d, "SS Caption pages", n, "scp"); lab_bg(k, n)
    for i, s in enumerate(["I tried this", "for 30 days", "and it worked"]):
        f = i * 40
        o = text(k, f"Caption {i + 1}", s, 490, 1250, 72, COL['white'], f0=f, dur=40, style='ExtraBold')
        outline(o)
        d.preset(k, o, "Caption words pop")


def progress_bar(d, n=150, bg=True):
    k = comp(d, "SS Progress bar", n, "spb")
    if bg: lab_bg(k, n)
    x0, x1, y = 90, 990, 290
    line(k, "Progress track", [(x0, y), (x1, y)], COL['muted'], 8, f0=0, dur=n).opv(0.35)
    fill = line(k, "Progress fill", [(x0, y), (x1, y)], COL['white'], 8, f0=0, dur=n)
    fill.trim([(0, 0.0, 'Linear'), (n - 1, 1.0, 'Linear')], which='end')


def follow_cta(d):
    n = 90
    k = comp(d, "SS Follow CTA", n, "sfc"); lab_bg(k, n)
    av = k.ell("Avatar", 540, 760, 260, 260, COL['card'], f0=0, dur=n); av.stroke(COL['yellow'], 8)
    av.scale([(0, 0.0, 'Linear'), (12, 1.0, BACK)])
    d.preset(k, text(k, "Handle", "@carvercat", 540, 960, 64, COL['white'], f0=8, dur=n - 8, style='ExtraBold'), "Hook punch")
    btn = line(k, "Button", [(400, 1100), (680, 1100)], COL['pink'], 110, f0=16, dur=n - 16)
    btn.scale([(16, 0.0, 'Linear'), (28, 1.0, BACK)])
    d.preset(k, text(k, "Button label", "Follow for part 2", 540, 1100, 40, COL['white'], f0=20, dur=n - 20, style='Bold'), "Hook punch")
    arrow = text(k, "Arrow", "↑", 540, 1250, 90, COL['yellow'], f0=30, dur=n - 30, style='ExtraBold')
    ax, ay = arrow.base
    # one rise, no looping bob: a ping-pong position reads as 'jitter' in lint (sub-pixel reversals at each turn)
    arrow.pos([(30, (ax, ay + 40), 'Linear'), (42, (ax, ay), EXPO)])


def comps(d):
    hook_title(d); caption_pages(d); progress_bar(d); follow_cta(d)


def build():
    d = SDoc(); comps(d)
    return d


if __name__ == "__main__":
    print(__doc__)
