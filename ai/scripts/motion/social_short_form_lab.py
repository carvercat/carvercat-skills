"""Write the Social Short-form lab comps (vertical 1080x1920) into a .carverproj.

    import social_short_form_lab as L; presets, masks = L.build(PROJECT.carverproj)

After writing: edit.open {path, force:true}; apply PRESETS (preset.apply); edit.save.
Check with carvercat_inspect, carvercat_look and carvercat_authoring validate
(bounds_inside the social safe box below); extract templates with comp_to_template.py
(--drop "Lab bg").

Vertical authoring with json_author/cc.py: set cc.W, cc.H = 1080, 1920 and scale the text
em with the comp width (cc.EM = 1146.24 * 1080 / 1920); VComp writes 1080x1920 scenes.
Measured on 0.1.6: a 200 x 100 px box and a 40 px dot land exactly; 100 px Bold caps
measure 71 px tall, as at 1920 wide.

Safe area for 1080 x 1920 (ai/references/craft/vertical-and-safe-areas.md): everything in
x 61-1016, y 268-1538; below y 1151 keep x > 851 clear; captions from x >= 130, <= 790 wide.
Fonts: Rethink Sans must be installed (KI-136).
Docs: ai/patterns/social-short-form.md. Pixel space 1080x1920, y down; comp frames, 30 fps.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "json_author"))
import cc
from cc import Doc, lin, BEZ

cc.W, cc.H = 1080, 1920
cc.EM = 1146.24 * 1080 / 1920
P = cc.P

COL = dict(bg=lin('111014'), white=lin('FFFFFF'), black=lin('000000'), yellow=lin('FFE14D'), pink=lin('FF3D7F'),
           muted=lin('A6A3AE'), card=lin('1E1C24'))
EXPO, BACK = BEZ['expo'], BEZ['back']
PRESETS, MASKS = [], []
SAFE = [61, 268, 955, 1270]                  # x, y, w, h of the social safe box


class VComp(cc.Comp):
    def scene(self):
        s = super().scene()
        s.update(timelineWidth=1080, timelineHeight=1920, width=1080, height=1920)
        return s


def comp(d, name, n, code):
    k = VComp(d, name, n, code); d.comps.append(k); return k


def lab_bg(k, n):
    k.rect("Lab bg", 0, 0, 1080, 1920, COL['bg'], f0=0, dur=n)


def outline(o, px=10):
    """white caption text with a round black outline, outside the glyphs"""
    o.set(o.src('text_outline', 'paint'), 'solid').set(o.src('text_outline', 'color'), COL['black'][:3])
    o.set(o.src('text_outline', 'thickness'), 0.12).set(o.src('text_outline', 'outsideOnly'), True)
    o.set(o.src('text_outline', 'corners'), 'round')
    return o


def hook_title(d):
    n = 75
    k = comp(d, "SS Hook title", n, "sht"); lab_bg(k, n)
    hl = k.rect("Highlight", 540, 520, 640, 120, COL['pink'], f0=6, dur=n - 6, center=True)
    hl.anchor(-1, 0); hl.scale([(6, [0.0, 1.0], 'Linear'), (14, [1.0, 1.0], EXPO)])
    k.text("Hook line 1", "STOP", 540, 380, 150, COL['white'], f0=0, dur=n, style='ExtraBold', align='center')
    PRESETS.append(("SS Hook title", "Hook line 1", "Hook punch"))
    k.text("Hook line 2", "SCROLLING", 540, 520, 110, COL['white'], f0=4, dur=n - 4, style='ExtraBold', align='center')
    PRESETS.append(("SS Hook title", "Hook line 2", "Hook punch"))
    k.text("Hook sub", "this changes everything", 540, 650, 48, COL['yellow'], f0=14, dur=n - 14, style='Bold', align='center')
    PRESETS.append(("SS Hook title", "Hook sub", "Caption words pop"))


def caption_pages(d):
    n = 120
    k = comp(d, "SS Caption pages", n, "scp"); lab_bg(k, n)
    pages = ["I tried this", "for 30 days", "and it worked"]
    for i, s in enumerate(pages):
        f = i * 40
        o = k.text(f"Caption {i + 1}", s, 490, 1250, 72, COL['white'], f0=f, dur=40, style='ExtraBold', align='center')
        outline(o)
        PRESETS.append(("SS Caption pages", f"Caption {i + 1}", "Caption words pop"))


def progress_bar(d, n=150, bg=True):
    k = comp(d, "SS Progress bar", n, "spb")
    if bg: lab_bg(k, n)
    x0, x1, y = 90, 990, 290
    k.line("Progress track", [(x0, y), (x1, y)], COL['muted'], px=8, f0=0, dur=n).opv(0.35)
    fill = k.line("Progress fill", [(x0, y), (x1, y)], COL['white'], px=8, f0=0, dur=n)
    fill.trim([(0, 0.0, 'Linear'), (n - 1, 1.0, 'Linear')], which='end')


def follow_cta(d):
    n = 90
    k = comp(d, "SS Follow CTA", n, "sfc"); lab_bg(k, n)
    av = k.ell("Avatar", 540, 760, 260, 260, COL['card'], f0=0, dur=n); av.stroke(COL['yellow'], 8)
    av.scale([(0, 0.0, 'Linear'), (12, 1.0, BACK)])
    k.text("Handle", "@carvercat", 540, 960, 64, COL['white'], f0=8, dur=n - 8, style='ExtraBold', align='center')
    PRESETS.append(("SS Follow CTA", "Handle", "Hook punch"))
    btn = k.line("Button", [(400, 1100), (680, 1100)], COL['pink'], px=110, f0=16, dur=n - 16)
    btn.scale([(16, 0.0, 'Linear'), (28, 1.0, BACK)])
    k.text("Button label", "Follow for part 2", 540, 1100, 40, COL['white'], f0=20, dur=n - 20, style='Bold', align='center')
    PRESETS.append(("SS Follow CTA", "Button label", "Hook punch"))
    arrow = k.text("Arrow", "↑", 540, 1250, 90, COL['yellow'], f0=30, dur=n - 30, style='ExtraBold', align='center')
    ax, ay = arrow.base
    # one rise, no looping bob: a ping-pong position reads as 'jitter' in lint (sub-pixel reversals at each turn)
    arrow.pos([(30, [ax, ay - 40 / 1920], 'Linear'), (42, [ax, ay], EXPO)])


def build(path, m=None):
    d = Doc(path); d.d.setdefault("bins", []); d.d.setdefault("media", [])
    PRESETS.clear(); MASKS.clear()
    hook_title(d); caption_pages(d); progress_bar(d); follow_cta(d)
    d.save()
    return PRESETS, MASKS


if __name__ == "__main__":
    print(__doc__)
