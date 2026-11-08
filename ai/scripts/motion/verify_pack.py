"""Verify a template pack on a real Carvercat host, headless and isolated.

    python3 verify_pack.py transitions --app /path/to/carvercat-host [--frames 7] [--out DIR] [--v1-ref GITREF]

(the app can also come from CARVERCAT_HOST; the resource root, the app repo root with fonts and the parameter registry,
from --resource-root or CARVERCAT_RESOURCE_ROOT). No user paths are built in. Every run uses FRESH temporary prefs, data
and cache folders; the pack is copied into a scratch user Library, so nothing installed is touched and the host is
started from a neutral working directory so it cannot find the repository's own library.

What it does, for every template of library/templates/<pack>/:
  1. PLACE   a fresh 16:9 comp and a fresh 9:16 comp each get the template (library.place + template.apply).
  2. LINT/QC carvercat_inspect lint and qc on each placed instance (counts of errors/warnings/notes; flashes).
  3. COMPARE the v1 original (the file as it was in git history before the first carvercat/2 version) is placed in a
     second isolated host; N frames of both are rendered at a small size and compared pixel by pixel.
  4. MEASURE the timings the pages state, under ONE definition (below).
It writes verify_<pack>.json and verify_<pack>.md into --out.

PIXEL METRIC (dark-aware). Both versions are placed above the same magenta underlay, and frames are compared on the raw
0..255 channel values, never through a brightness threshold (a brightness test calls two different dark panels "both
background" and gave a false 97.5 % match). Per frame it reports `mean` (mean channel difference), `changed` (share of pixels
where any channel differs by more than TOL = 6), `shape` (share of pixels that are template in one frame and underlay in the
other: the silhouette) and `colour` (mean RGB difference where both are template). A frame MATCHES when shape <= 2 % (colour is
reported, not judged: the v1 kit linearised colours, v2 writes exact hex, a known and intended shift). A template passes when
every compared frame matches.

OBJECT-LEVEL CHECK (mandatory; the pixel metric alone is blind to small text: a masked headline that was completely missing
scored 0.75-1.8 % shape). The template is placed in a 1920x1080 comp, the inner comp is opened and, at each compared frame,
`measure.boxes` (comp space, px, at the playhead, no render) lists every object with its box and, for text, its ink box (the drawn
extent; the layout box of a text can differ in width and padding without any visible change, so text is compared by ink).
For v1 and v2 the objects are matched (same type and name; the rest by order within the type) and:
  - `missing`   a v1 object has no v2 counterpart (also when the counterpart is absent from the list at a compared frame),
  - `textdiff`  a text object whose text content differs (whitespace-normalised),
  - `offset`    the largest |dx|, |dy|, |dw|, |dh| in px between the v1 and v2 box at any compared frame; over BOX_TOL = 16 px
                the object is reported in `moved` and fails,
  - `empty`     a text object whose ink is missing in v2 where v1 draws ink: in the render of the object's ink box (v1 ink box
                plus 4 px), the share of pixels departing from the box's dominant colour by more than 48/255 is `ink`; v2 is
                EMPTY when its ink area is under 40 % of v1's (v1 ink share at least 1 %), and `inkIoU` (overlap of the two ink
                masks) under 0.25 is a `textdiff` too. Both are reported per frame in `objects.texts`.
Any missing, empty, moved or text-different object makes the template FAIL whatever the pixel score. Templates with text are
compared pixel by pixel at HIRES (default 960x540) instead of 320x180, and exit code 1 means a FAIL.

HARNESS CORRECTIONS (folded in from verify_pack_wrap.py):
  1. An object whose clip has not started at a compared frame is not measured there: `measure.boxes` returns unresolved local
     coordinates for it (a v1 child reads relative to its parent, a v1 parent absolute) and the object is not drawn.
  2. The two ink masks of one object and frame (v1, v2) use ONE background colour, the dominant colour of the v1 crop. Each crop's own
     dominant colour flips between v1 and v2 when text and its panel cover about the same area (3137 vs 3125 pixels) and the IoU
     collapsed (0.08) although the pixels were identical.
  3. `--ink-templates 'Title A,Title B'` (or `--ink-all`): for those templates a text object's box is the RENDERED ink bounding box
     (pixels differing from the dominant colour inside the union of the v1 and v2 reported boxes), not measure.boxes' ink box, which
     differs for text under a rotating or scaling parent although the pixels are identical. The per-object boxes go to
     <out>/inkboxes.json. Use it only for a template whose object check fails on boxes while the pixels are proven equal, and say so
     in the report: it is evidence for one template, not a switch for a pack.
  4. `--timeout SECONDS` sets the client timeout of both hosts (big comps take minutes on a busy Mac; the default is the client's 120 s).

TIMING DEFINITION. The renders are opaque, so alpha says nothing. The template is rendered twice at the small size, above a
full-frame MAGENTA (#FF00FF) underlay and above a full-frame GREEN (#00FF00) one (colours no pack uses). Frame f is
  - `covered` when at least 99.5 % of pixels read the same in both renders within TOL (the underlay is hidden: alpha >= 0.98),
  - `visible` when at least 0.5 % of pixels differ from their own underlay by more than TOL in either render.
`covered window` = first..last covered frame of the instance (frames from the instance start); `cut` = its first frame.
`settled` = the first frame after the covered window from which the picture no longer changes (mean channel difference to the
last frame below 0.5). `gone` = the last visible frame + 1 (None when something is still on screen at the end). The pages'
words "covered f20-22", "settles f36" are checked against these. Recipes measured on a lab comp (no underlay) use
`change_window`: first frame that differs from frame 0 and first frame that equals the last frame.
"""
import argparse, json, os, re, shutil, struct, subprocess, sys, tempfile, time, zlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
from cc_client import Client  # noqa: E402

REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SMALL = (320, 180)          # measuring size (16:9)
TOL = 6
HIRES = (960, 540)         # compare size for templates with text
BOX_TOL = 16.0            # px, largest accepted box offset v1 -> v2 (comp space, 1920 wide)
INK_DEV = 48              # a pixel is ink when a channel departs this much from the box's dominant colour
INK_MIN_RATIO = 0.4       # v2 ink area / v1 ink area below this: EMPTY
INK_MIN_IOU = 0.25
SHAPE_TOL = 0.02          # a frame matches v1 when at most 2 % of pixels switch between template and underlay


# ------------------------------------------------------------------ PNG reading (stdlib only)
def read_png(path):
    """-> (width, height, rows) with rows a list of bytes of RGBA (8 bit); colour types 2, 6 (and 0, 4) supported."""
    data = open(path, 'rb').read()
    assert data[:8] == b'\x89PNG\r\n\x1a\n', 'not a PNG'
    pos, idat, w = 8, [], None
    while pos < len(data):
        n, typ = struct.unpack('>I4s', data[pos:pos + 8])
        body = data[pos + 8:pos + 8 + n]
        pos += 12 + n
        if typ == b'IHDR': w, h, depth, ctype, _, _, inter = struct.unpack('>IIBBBBB', body)
        elif typ == b'IDAT': idat.append(body)
        elif typ == b'IEND': break
    assert depth == 8 and inter == 0, 'only 8-bit non-interlaced PNG'
    ch = {0: 1, 2: 3, 4: 2, 6: 4}[ctype]
    raw = zlib.decompress(b''.join(idat))
    stride = w * ch
    prev = bytearray(stride)
    rows = []
    p = 0
    for _ in range(h):
        ft = raw[p]; line = bytearray(raw[p + 1:p + 1 + stride]); p += 1 + stride
        if ft == 1:
            for i in range(ch, stride): line[i] = (line[i] + line[i - ch]) & 255
        elif ft == 2:
            for i in range(stride): line[i] = (line[i] + prev[i]) & 255
        elif ft == 3:
            for i in range(stride):
                a = line[i - ch] if i >= ch else 0
                line[i] = (line[i] + ((a + prev[i]) >> 1)) & 255
        elif ft == 4:
            for i in range(stride):
                a = line[i - ch] if i >= ch else 0
                b = prev[i]; c = prev[i - ch] if i >= ch else 0
                pa, pb, pc = abs(b - c), abs(a - c), abs(a + b - 2 * c)
                pr = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                line[i] = (line[i] + pr) & 255
        prev = line
        if ch == 4: rows.append(bytes(line))
        elif ch == 3:
            out = bytearray(w * 4); out[0::4] = line[0::3]; out[1::4] = line[1::3]; out[2::4] = line[2::3]
            out[3::4] = b'\xff' * w; rows.append(bytes(out))
        elif ch == 1:
            out = bytearray(w * 4); out[0::4] = line; out[1::4] = line; out[2::4] = line; out[3::4] = b'\xff' * w; rows.append(bytes(out))
        else:
            out = bytearray(w * 4); out[0::4] = line[0::2]; out[1::4] = line[0::2]; out[2::4] = line[0::2]; out[3::4] = line[1::2]; rows.append(bytes(out))
    return w, h, rows


def compare(a, b, tol=TOL):
    """-> dict for two RGBA frames of the same size:
    mean    mean channel difference 0..255 over every pixel and channel (alpha included)
    changed share of pixels where any channel differs by more than tol
    shape   share of pixels that are 'template' (not the magenta underlay) in one frame and underlay in the other: the silhouette
    colour  mean RGB difference over pixels that are template in BOTH frames (the colour shift, 0 when none)"""
    (w, h, ra), (w2, h2, rb) = a, b
    if (w, h) != (w2, h2): return None
    tot = changed = shape = both = 0; col = 0
    for x, y in zip(ra, rb):
        for i in range(0, len(x), 4):
            d0, d1, d2, d3 = abs(x[i] - y[i]), abs(x[i + 1] - y[i + 1]), abs(x[i + 2] - y[i + 2]), abs(x[i + 3] - y[i + 3])
            tot += d0 + d1 + d2 + d3
            if d0 > tol or d1 > tol or d2 > tol or d3 > tol: changed += 1
            xa = abs(x[i] - 255) > tol or x[i + 1] > tol or abs(x[i + 2] - 255) > tol
            ya = abs(y[i] - 255) > tol or y[i + 1] > tol or abs(y[i + 2] - 255) > tol
            if xa != ya: shape += 1
            elif xa: both += 1; col += d0 + d1 + d2
    n = w * h
    return {'mean': tot / (n * 4), 'changed': changed / n, 'shape': shape / n, 'colour': (col / (both * 3)) if both else 0.0}


def cover_stats(m, g):
    """m, g: the same frame over magenta and over green -> (covered share, visible share)"""
    w, h, rm = m; _, _, rg = g
    cov = vis = 0
    for x, y in zip(rm, rg):
        for i in range(0, len(x), 4):
            if abs(x[i] - y[i]) <= TOL and abs(x[i + 1] - y[i + 1]) <= TOL and abs(x[i + 2] - y[i + 2]) <= TOL: cov += 1
            if abs(x[i] - 255) > TOL or x[i + 1] > TOL or abs(x[i + 2] - 255) > TOL or y[i] > TOL or abs(y[i + 1] - 255) > TOL or y[i + 2] > TOL: vis += 1
    return cov / (w * h), vis / (w * h)


def change_window(imgs):
    """for a comp with no underlay: (first frame differing from frame 0, first frame equal to the last frame)"""
    n = len(imgs); first, last = imgs[0], imgs[n - 1]
    def d(a, b): return sum(sum(abs(p - q) for p, q in zip(x, y)) for x, y in zip(a[2][::4], b[2][::4])) / (len(a[2][::4]) * len(a[2][0]))
    start = next((f for f in range(n) if d(imgs[f], first) >= 0.5), None)
    settle = next((f for f in range(n) if all(d(imgs[g], last) < 0.5 for g in range(f, n))), None)
    return {'starts': start, 'settles': settle}


# ------------------------------------------------------------------ app
def find_app(args):
    app = args.app or os.environ.get('CARVERCAT_HOST') or os.environ.get('CARVERCAT_EXE')
    if not app or not os.path.exists(app): sys.exit('give the host with --app or CARVERCAT_HOST')
    return app


def start(app, root, pack_files, resource_root):
    """A fresh isolated host (own prefs/data/cache) whose user Library holds exactly pack_files {name: bytes}."""
    state = tempfile.mkdtemp(prefix='ccverify-')
    lib = os.path.join(state, 'data', 'library', 'templates', 'pack'); os.makedirs(lib)
    for name, blob in pack_files.items(): open(os.path.join(lib, name), 'wb').write(blob)
    cwd = os.getcwd(); os.chdir(tempfile.gettempdir())      # neutral cwd: the host must not find a repo library
    try: c = Client.stdio(app, state, resource_root=resource_root)
    finally: os.chdir(cwd)
    c.run('library.reload')
    return c, state


def git(*a):
    return subprocess.run(('git', '-C', REPO) + a, capture_output=True, text=True).stdout


def v1_files(pack, names, ref=None):
    """The v1 originals: the newest committed version of each file whose `format` is not carvercat/2 (or --v1-ref's)."""
    out = {}
    for n in names:
        rel = 'library/templates/%s/%s' % (pack, n)
        if ref:
            blob = subprocess.run(('git', '-C', REPO, 'show', '%s:%s' % (ref, rel)), capture_output=True).stdout
            if blob: out[n] = blob
            continue
        for h in git('log', '--format=%H', '--', rel).split():
            blob = subprocess.run(('git', '-C', REPO, 'show', '%s:%s' % (h, rel)), capture_output=True).stdout
            if blob and b'"format": "carvercat/2"' not in blob[:400]: out[n] = blob; break
    return out


def place(c, name, w, h, underlay=None):
    """fresh comp of w x h, the template placed at frame 0 (above a magenta underlay if asked) and applied -> instance id"""
    c.run('comp.new', name='verify %s %dx%d' % (name, w, h))
    c.run('comp.format', width=w, height=h, fps=30)
    if underlay:
        c.apply_scene({'schema': 'carvercat/2.0', 'comp': {'width': w, 'height': h, 'fps': 30, 'duration': 300},
                       'children': [{'id': 'under', 'type': 'rect', 'name': 'Underlay',
                                     'style': {'x': 0, 'y': 0, 'width': w, 'height': h, 'fill': underlay, 'stroke': 'none'}}]})
    r = c.run('library.place', name=name, frame=0, **({'track': 1} if underlay else {}))
    oid = r['touched'][0]
    c.run('select.clip', id=oid, check=False)
    c.run('template.apply', id=oid, check=False)
    return oid


def counts(rep):
    """error/warning/note counts from an inspect lint reply (its summary line: "0 error(s), 0 warning(s), 0 note(s)")"""
    m = re.findall(r'(\d+) (error|warning|note)', rep.get('summary', '') if isinstance(rep, dict) else '')
    d = {k: int(v) for v, k in m}
    return {'errors': d.get('error', 0), 'warnings': d.get('warning', 0), 'notes': d.get('note', 0)}


def qc_summary(rep):
    """-> {'flashes': n, 'checks': [names]} from an inspect qc reply; black and freeze outside the template are expected"""
    f = rep.get('findings', []) if isinstance(rep, dict) else []
    return {'flashes': sum(1 for x in f if 'flash' in str(x.get('check', '')).lower()), 'checks': sorted(set(str(x.get('check')) for x in f))}


def render_frames(c, frames, outdir):
    os.makedirs(outdir, exist_ok=True)
    res = {}
    for f in frames:
        c.tool('carvercat_render', dir=outdir, at=f)
        res[f] = read_png(os.path.join(outdir, 'f%05d.png' % f))
    return res


def measure_timing(c, name, length, outdir):
    """-> (timing dict, magenta renders {frame: image}); places the template over magenta and over green (see TIMING DEFINITION)"""
    place(c, name, *SMALL, underlay='#FF00FF')
    im = render_frames(c, range(length), os.path.join(outdir, 'magenta'))
    place(c, name, *SMALL, underlay='#00FF00')
    ig = render_frames(c, range(length), os.path.join(outdir, 'green'))
    cov, vis = {}, {}
    for f in range(length): cov[f], vis[f] = cover_stats(im[f], ig[f])
    covered = [f for f in cov if cov[f] >= 0.995]
    visible = [f for f in vis if vis[f] >= 0.005]
    last = im[length - 1]
    settled = None
    if covered:
        dist = {}
        for f in range(covered[-1] + 1, length):
            a, b = im[f][2], last[2]
            dist[f] = sum(sum(abs(p - q) for p, q in zip(x, y)) for x, y in zip(a[::4], b[::4])) / (len(a[::4]) * len(a[0]))
        settled = next((f for f in range(covered[-1] + 1, length) if all(dist[g] < 0.5 for g in range(f, length))), None)
    return {'covered': [covered[0], covered[-1]] if covered else None, 'cut': covered[0] if covered else None,
            'settled': settled, 'visible': [visible[0], visible[-1]] if visible else None,
            'gone': (visible[-1] + 1) if visible and visible[-1] + 1 < length else None}, im



# ------------------------------------------------------------------ object-level check
def flatten(node, out=None):
    out = [] if out is None else out
    for ch in node.get('children', []) or []:
        out.append(ch); flatten(ch, out)
    return out


def object_track(c, title, frames):
    """Place the template in a fresh 1920x1080 comp, open its inner comp and measure every object at each frame
    -> {'objs': [{id,name,type,text}] (frame order of the first list), 'frames': {f: {id: reading}}}"""
    place(c, title, 1920, 1080)
    comps = c.tool('carvercat_list')['comps']
    inner = [x for x in comps if x['name'] == title]
    c.run('comp.switch', comp=(inner[-1] if inner else comps[-1])['index'])
    nodes = flatten(c.scene())
    text = {n.get('id'): n.get('text') for n in nodes if n.get('type') == 'text'}
    start = {}
    for n in nodes:
        st = n.get('start'); start[n.get('id')] = int(float(str(st).rstrip('f'))) if st is not None else 0
    by, objs = {}, None
    for f in frames:
        c.run('view.seek', frame=f)
        rd = c.measure()['objects']
        rd = [o for o in rd if f >= start.get(o['id'], 0)]     # a clip that has not started is not drawn, and its reading is unresolved (correction 1)
        by[f] = {o['id']: o for o in rd}
        if objs is None or len(rd) > len(objs):
            objs = [{'id': o['id'], 'name': o.get('name'), 'type': o.get('type'),
                     'text': text.get(o['id']) if text.get(o['id']) is not None else (' '.join(o['lines']) if o.get('lines') else None)} for o in rd]
    return {'objs': objs or [], 'frames': by}


def match_objects(o1, o2):
    """v1 -> v2 object pairing: same type and name first, then by order within the type. -> ([(a, b|None)], [unmatched v2])"""
    left = list(o2); pairs = []
    for a in o1:
        k = next((b for b in left if b['type'] == a['type'] and b['name'] == a['name']), None)
        if k: left.remove(k)
        pairs.append([a, k])
    for pr in pairs:
        if pr[1] is None:
            k = next((b for b in left if b['type'] == pr[0]['type']), None)
            if k: left.remove(k); pr[1] = k
    return [tuple(x) for x in pairs], left


def norm(t):
    return ' '.join(str(t).split()) if t is not None else None


def ink_mask(img, rect, scale, bg=None, with_bg=False):
    """rect (x, y, w, h) in 1920 comp px -> list (rows) of bool per pixel: the ink pixels of that crop, or None. The ink is what departs
    from the background colour `bg` by more than INK_DEV; without `bg` it is the crop's dominant colour. with_bg=True returns
    (mask, bg) so a second crop can use the same colour."""
    w, h, rows = img
    x0 = max(0, int((rect['x'] - 4) * scale)); y0 = max(0, int((rect['y'] - 4) * scale))
    x1 = min(w, int((rect['x'] + rect['width'] + 4) * scale) + 1); y1 = min(h, int((rect['y'] + rect['height'] + 4) * scale) + 1)
    if x1 - x0 < 2 or y1 - y0 < 2: return None
    px = [rows[y][x0 * 4:x1 * 4] for y in range(y0, y1)]
    if bg is None:
        hist = {}
        for r in px:
            for i in range(0, len(r), 4):
                k = (r[i] >> 3, r[i + 1] >> 3, r[i + 2] >> 3); hist[k] = hist.get(k, 0) + 1
        bg = max(hist, key=hist.get); bg = (bg[0] * 8 + 4, bg[1] * 8 + 4, bg[2] * 8 + 4)
    m = [[abs(r[i] - bg[0]) > INK_DEV or abs(r[i + 1] - bg[1]) > INK_DEV or abs(r[i + 2] - bg[2]) > INK_DEV for i in range(0, len(r), 4)] for r in px]
    return (m, bg) if with_bg else m


def union_rect(a, b):
    x0, y0 = min(a['x'], b['x']), min(a['y'], b['y'])
    x1, y1 = max(a['x'] + a['width'], b['x'] + b['width']), max(a['y'] + a['height'], b['y'] + b['height'])
    return {'x': x0, 'y': y0, 'width': x1 - x0, 'height': y1 - y0}


def ink_bbox(img, rect, scale):
    """the rendered ink bounding box (comp px) of the crop around `rect`, or None"""
    m = ink_mask(img, rect, scale)
    if not m: return None
    x0 = max(0, int((rect['x'] - 4) * scale)); y0 = max(0, int((rect['y'] - 4) * scale))
    xs = [x for r in m for x, v in enumerate(r) if v]
    ys = [y for y, r in enumerate(m) if any(r)]
    if not xs: return None
    return {'x': (x0 + min(xs)) / scale, 'y': (y0 + min(ys)) / scale, 'width': (max(xs) - min(xs) + 1) / scale, 'height': (max(ys) - min(ys) + 1) / scale}


def ink_stats(m1, m2):
    """-> (v1 ink share of the crop, v2 ink / v1 ink, IoU) for two same-size masks"""
    a = sum(sum(r) for r in m1); b = sum(sum(r) for r in m2)
    inter = sum(sum(1 for p, q in zip(r1, r2) if p and q) for r1, r2 in zip(m1, m2))
    n = sum(len(r) for r in m1)
    return a / n, (b / a if a else 1.0), (inter / (a + b - inter) if a + b - inter else 1.0)


def object_check(t1, t2, imgs1, imgs2, frames, scale, ink_boxes=False, ink_log=None):
    """The object-level verdict (see OBJECT-LEVEL CHECK). imgs1/imgs2: {frame: image} of the v1/v2 over the same underlay, at
    scale x 1920; t1/t2 from object_track."""
    pairs, extra = match_objects(t1['objs'], t2['objs'])
    if ink_boxes:                                     # correction 3: text boxes from the rendered ink
        for a, b in pairs:
            if b is None or a['type'] != 'text': continue
            for f in frames:
                ra, rb = t1['frames'][f].get(a['id']), t2['frames'][f].get(b['id'])
                if not ra or not rb or f not in imgs1 or f not in imgs2: continue
                ua = union_rect(union_rect(ra.get('ink') or ra['box'], rb.get('ink') or rb['box']), union_rect(ra['box'], rb['box']))
                A, B = ink_bbox(imgs1[f], ua, scale), ink_bbox(imgs2[f], ua, scale)
                if A and B:
                    ra['ink'], rb['ink'] = A, B
                    if ink_log is not None:
                        ink_log.append({'object': a['name'], 'frame': f, 'v1': {k: round(v, 1) for k, v in A.items()},
                                        'v2': {k: round(v, 1) for k, v in B.items()}, 'maxdiff': round(max(abs(A[k] - B[k]) for k in A), 1)})
    missing, empty, moved, textdiff, texts = [], [], [], [], []
    off_max = 0.0
    for a, b in pairs:
        if b is None: missing.append(a['name']); continue
        if a['type'] == 'text' and norm(a['text']) != norm(b['text']): textdiff.append('%s: %r -> %r' % (a['name'], a['text'], b['text']))
        worst = 0.0
        for f in frames:
            ra, rb = t1['frames'][f].get(a['id']), t2['frames'][f].get(b['id'])
            if ra is None: continue
            if rb is None:
                if a['name'] not in missing: missing.append(a['name'])
                continue
            # text: the drawn extent is the ink box (the layout box differs with box padding/width, not with what is drawn)
            A, B = (ra.get('ink') or ra['box']), (rb.get('ink') or rb['box'])
            if a['type'] == 'text' and bool(ra.get('ink')) != bool(rb.get('ink')): A, B = ra['box'], rb['box']
            worst = max(worst, abs(A['x'] - B['x']), abs(A['y'] - B['y']), abs(A['width'] - B['width']), abs(A['height'] - B['height']))
            if a['type'] == 'text' and ra.get('ink') and f in imgs1 and f in imgs2:
                m1 = ink_mask(imgs1[f], ra['ink'], scale, with_bg=True)
                m2 = ink_mask(imgs2[f], ra['ink'], scale, bg=m1[1]) if m1 else None      # correction 2: one background colour for both
                m1 = m1[0] if m1 else None
                if m1 and m2:
                    share, ratio, iou = ink_stats(m1, m2)
                    if share >= 0.01:
                        row = {'object': a['name'], 'frame': f, 'ink': round(share, 3), 'ratio': round(ratio, 2), 'inkIoU': round(iou, 2)}
                        texts.append(row)
                        if ratio < INK_MIN_RATIO:
                            if a['name'] not in empty: empty.append(a['name'])
                        elif iou < INK_MIN_IOU: textdiff.append('%s f%d: ink overlap %.2f' % (a['name'], f, iou))
        off_max = max(off_max, worst)
        if worst > BOX_TOL: moved.append('%s %.0f px' % (a['name'], worst))
    ok = not (missing or empty or moved or textdiff)
    return {'v1': len(t1['objs']), 'v2': len(t2['objs']), 'missing': missing, 'empty': empty, 'moved': moved, 'textdiff': textdiff,
            'extra': [b['name'] for b in extra], 'box_offset_max': round(off_max, 1), 'worst_ink_iou': min([x['inkIoU'] for x in texts], default=None),
            'texts': texts, 'pass': ok}


def pick(length, n):
    n = max(2, min(n, length))
    return sorted(set(round(i * (length - 1) / (n - 1)) for i in range(n)))


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pack'); ap.add_argument('--app'); ap.add_argument('--resource-root')
    ap.add_argument('--frames', type=int, default=7, help='frames compared per template')
    ap.add_argument('--out', default=None); ap.add_argument('--v1-ref', default=None)
    ap.add_argument('--pack-dir', default=None, help='read the v2 templates from this folder instead of library/templates/<pack> (a scratch copy, e.g. a deliberately broken one)')
    ap.add_argument('--repo', default=None, help='the skills repo (or worktree) holding library/templates and the git history; default: this script\'s own')
    ap.add_argument('--only', default=None, help='comma list of template file stems')
    ap.add_argument('--lab', default=None, help='lab module (build() -> cc2.Doc): also lint and measure its recipe comps')
    ap.add_argument('--recipes', default=None, help='comma list of lab comp names to measure with --lab')
    ap.add_argument('--ink-templates', default=None, help="comma list of template display names whose text boxes are measured from the rendered ink (see HARNESS CORRECTIONS)")
    ap.add_argument('--ink-all', action='store_true', help='measure every template that way (only to investigate)')
    ap.add_argument('--timeout', type=float, default=None, help='client timeout in seconds for both hosts (default: the client\'s 120)')
    args = ap.parse_args()
    ink_titles = set((args.ink_templates or '').split(',')) - {''}
    ink_log = []
    global REPO
    if args.repo: REPO = os.path.abspath(args.repo)
    app = find_app(args)
    rr = args.resource_root or os.environ.get('CARVERCAT_RESOURCE_ROOT')
    if rr is None:
        cand = os.path.abspath(os.path.join(REPO, '..', 'carvercat'))
        rr = cand if os.path.isdir(cand) else None
    packdir = args.pack_dir or os.path.join(REPO, 'library', 'templates', args.pack)
    names = sorted(f for f in os.listdir(packdir) if f.endswith('.carvertemplate'))
    if args.only: names = [n for n in names if n[:-len('.carvertemplate')] in args.only.split(',')]
    out = os.path.abspath(args.out or tempfile.mkdtemp(prefix='verify-%s-' % args.pack))
    os.makedirs(out, exist_ok=True)
    new = {n: open(os.path.join(packdir, n), 'rb').read() for n in names}
    old = v1_files(args.pack, names, args.v1_ref)
    c2, s2 = start(app, None, new, rr)
    c1, s1 = (start(app, None, old, rr) if old else (None, None))
    for c in (c1, c2):
        if c is not None and args.timeout: c.timeout = args.timeout
    build = c2.state().get('build', {})
    report = {'pack': args.pack, 'build': build, 'tolerance': TOL, 'size': list(SMALL), 'templates': []}
    try:
        for n in names:
            stem = n[:-len('.carvertemplate')]
            meta = json.loads(new[n]); title = meta['name']
            print('...', stem, flush=True); t0 = time.time()
            row = {'template': stem, 'name': title, 'format': meta.get('format'), 'place': {}, 'compare': None, 'timing': None}
            length = None
            for label, (w, h) in (('16:9', (1920, 1080)), ('9:16', (1080, 1920))):
                try:
                    oid = place(c2, title, w, h)
                    objs = [o for o in c2.tool('carvercat_list')['objects'] if o['id'] == oid]
                    length = int(objs[0]['length']) if objs else None
                    lint = c2.tool('carvercat_inspect', mode='lint')
                    qc = c2.tool('carvercat_inspect', mode='qc', **{'from': 0, 'to': (length or 36) - 1}, width=96)
                    row['place'][label] = {'placed': True, 'length': length, 'lint': counts(lint), 'qc': qc_summary(qc)}
                except Exception as e:
                    row['place'][label] = {'placed': False, 'error': str(e)[:300]}
            # small 16:9 comps for the pixel work
            try:
                length = length or 36
                tim, imgs2 = measure_timing(c2, title, length, os.path.join(out, stem, 'v2'))
                row['timing'] = tim
                if c1 is not None and n in old:
                    fr = pick(length, args.frames)
                    t1, t2 = object_track(c1, title, fr), object_track(c2, title, fr)
                    texty = any(o['type'] == 'text' for o in t1['objs'] + t2['objs'])
                    size = HIRES if texty else SMALL
                    if texty:
                        place(c2, title, *size, underlay='#FF00FF')
                        imgs2c = render_frames(c2, fr, os.path.join(out, stem, 'v2hi'))
                    else: imgs2c = imgs2
                    place(c1, title, *size, underlay='#FF00FF')
                    imgs1 = render_frames(c1, fr, os.path.join(out, stem, 'v1'))
                    cmp_rows = []
                    for f in fr:
                        m = compare(imgs1[f], imgs2c[f])
                        cmp_rows.append({'frame': f, 'mean': round(m['mean'], 3), 'changed': round(m['changed'], 5), 'shape': round(m['shape'], 5),
                                         'colour': round(m['colour'], 2), 'match': m['shape'] <= SHAPE_TOL})
                    row['compare'] = {'size': list(size), 'frames': cmp_rows, 'pass': all(r['match'] for r in cmp_rows)}
                    use_ink = args.ink_all or title in ink_titles
                    log = []
                    row['objects'] = object_check(t1, t2, imgs1, imgs2c, fr, size[0] / 1920.0, ink_boxes=use_ink, ink_log=log)
                    if use_ink:
                        row['objects']['ink_boxes'] = True
                        ink_log += [dict(template=title, **x) for x in log]
            except Exception as e:
                row['error'] = str(e)[:400]
            report['templates'].append(row)
            ob = row.get('objects')
            print('%-24s place %s  compare %s  objects %s  timing %s  %.0fs' % (stem, {k: (v.get('lint') if v.get('placed') else 'FAIL') for k, v in row['place'].items()},
                  None if not row['compare'] else ('PASS' if row['compare']['pass'] else 'DIFF'),
                  None if not ob else ('PASS' if ob['pass'] else 'FAIL missing=%s empty=%s moved=%s textdiff=%s' % (ob['missing'], ob['empty'], ob['moved'], ob['textdiff'])),
                  row['timing'], time.time() - t0))
            row['seconds'] = round(time.time() - t0, 1)
    finally:
        for c in (c1, c2):
            if c: c.close()
        for s in (s1, s2):
            if s: shutil.rmtree(s, ignore_errors=True)
    if args.lab: report['recipes'] = verify_lab(app, rr, args.lab, (args.recipes or '').split(','), out)
    json.dump(report, open(os.path.join(out, 'verify_%s.json' % args.pack), 'w'), indent=1)
    if ink_log: json.dump(ink_log, open(os.path.join(out, 'inkboxes.json'), 'w'), indent=1)
    write_md(report, os.path.join(out, 'verify_%s.md' % args.pack))
    bad = [r['template'] for r in report['templates'] if template_fail(r)]
    print('report:', out)
    if bad: print('FAIL:', ', '.join(bad)); sys.exit(1)


def template_fail(r):
    """FAIL = the pixel compare differs, the object check fails or could not run, or the template did not run"""
    if r.get('error'): return True
    if r.get('objects') and not r['objects']['pass']: return True
    return bool(r.get('compare') and not r['compare']['pass'])


def verify_lab(app, rr, lab, names, out):
    """Build the lab (a cc2.Doc), send it to a fresh host, and for each named comp: lint, and the change window (first frame
    that differs from frame 0, first frame equal to the last; see change_window) at the small size."""
    import importlib
    sys.path.insert(0, HERE)
    doc = importlib.import_module(lab).build()
    state = tempfile.mkdtemp(prefix='ccverify-lab-')
    cwd = os.getcwd(); os.chdir(tempfile.gettempdir())
    try: c = Client.stdio(app, state, resource_root=rr)
    finally: os.chdir(cwd)
    rows = []
    try:
        doc.send(c, os.path.join(state, 'lab.carverproj'))
        comps = {x['name']: x for x in c.tool('carvercat_list')['comps']}
        for n in [x for x in names if x]:
            c.run('comp.switch', comp=comps[n]['index'])
            length = next(k.length for k in doc.comps if k.name == n)
            lint = counts(c.tool('carvercat_inspect', mode='lint'))      # at the comp's own size: shrinking it first gave false text_overlap warnings
            c.run('comp.format', width=SMALL[0], height=SMALL[1], fps=30)
            imgs = render_frames(c, range(length), os.path.join(out, 'lab', n.replace(' ', '_')))
            row = {'comp': n, 'length': length, 'lint': lint}; row.update(change_window(imgs)); rows.append(row)
            print('%-20s lint %s  %s' % (n, lint, change_window(imgs)), flush=True)
    finally:
        c.close(); shutil.rmtree(state, ignore_errors=True)
    return rows


def write_md(rep, path):
    L = ['# Verify %s' % rep['pack'], '', 'Build: `%s`. Size %dx%d, tolerance %d/255. Definitions: see verify_pack.py.' %
         (json.dumps(rep['build'])[:120], rep['size'][0], rep['size'][1], rep['tolerance']), '',
         '| Template | 16:9 lint e/w/n | 9:16 lint e/w/n | v1 vs v2 | worst shape | colour shift | objects | missing | empty | box offset max px | worst ink IoU | covered | cut | settled | gone | s |', '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    def lc(p): return '%(errors)d/%(warnings)d/%(notes)d' % p['lint'] if p.get('placed') else 'FAIL'
    for r in rep['templates']:
        cm = r['compare']; t = r['timing'] or {}
        ob = r.get('objects')
        L.append('| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
            r['name'], lc(r['place'].get('16:9', {})), lc(r['place'].get('9:16', {})),
            'n/a' if not cm else ('pass' if cm['pass'] else 'DIFF'),
            '' if not cm else '%.2f %%' % (100 * max(x['shape'] for x in cm['frames'])),
            '' if not cm else '%.1f' % max(x['colour'] for x in cm['frames']),
            'n/a' if not ob else ('pass' if ob['pass'] else 'FAIL'),
            '' if not ob else ', '.join(ob['missing']) or 0, '' if not ob else ', '.join(ob['empty']) or 0,
            '' if not ob else ob['box_offset_max'], '' if not ob or ob['worst_ink_iou'] is None else ob['worst_ink_iou'],
            t.get('covered'), t.get('cut'), t.get('settled'), t.get('gone'), r.get('seconds', '')))
    det = [r for r in rep['templates'] if r.get('objects') and not r['objects']['pass']]
    if det:
        L += ['', '## Object-level FAILS', '']
        for r in det:
            o = r['objects']
            L.append('- **%s**: missing %s; empty %s; moved %s; text differs %s' % (r['name'], o['missing'], o['empty'], o['moved'], o['textdiff']))
    if rep.get('recipes'):
        L += ['', '| Recipe comp | length | lint e/w/n | starts | settles |', '|---|---|---|---|---|']
        for r in rep['recipes']: L.append('| %s | %d | %d/%d/%d | %s | %s |' % (r['comp'], r['length'], r['lint']['errors'], r['lint']['warnings'], r['lint']['notes'], r['starts'], r['settles']))
    open(path, 'w').write('\n'.join(L) + '\n')


if __name__ == '__main__':
    main()
