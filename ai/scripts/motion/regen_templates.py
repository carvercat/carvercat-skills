"""Rewrite a pack's .carvertemplate files from a saved carvercat/2 lab project (the design-unit successor of
comp_to_template.py for whole packs).

    python regen_templates.py LAB.carverproj PACK_DIR OUT_DIR [--strict]

For every template in PACK_DIR the lab comp whose slugged name equals the template's file stem is found (`TX Slide wipe`
-> `tx_slide_wipe`). Its scene replaces the template's scene; everything else (id, name, category, tags, note, fonts,
frame) is kept. If no comp has that name, the one named like the template's display name is used. The objects kept are the ones the old
template had (matched by name; a lab object the app saved without a name matches its type's default name, "Star", "Rectangle" ...), so stand-in
backgrounds are dropped as before; null objects are always kept (they are parents, not content). A lab comp that was renamed so that it
no longer matches its template is NOT regenerated: it is reported on stderr as a WARNING (and with --strict the run exits 3), never silently. Clip ids are rewritten with the old template's own prefix (`clip_3` -> `tsw_3`) so two templates
applied to one comp never share ids. Files are written to OUT_DIR as carvercat/2 (`format`, `minApp`).
"""
import copy, difflib, json, os, re, sys

# the name the app gives an object nobody named
DEFAULT_NAME = {'rect': 'Rectangle', 'ellipse': 'Ellipse', 'polygon': 'Polygon', 'star': 'Star', 'text': 'Text', 'path': 'Path',
                'null': 'Null', 'shape': 'Shape'}


def slug(s):
    return re.sub(r'[^a-z0-9]+', '_', s.lower()).strip('_')


def old_names(t):
    """names of the objects an old template (v1 or v2) holds"""
    sc = t['scene']
    names, ids = set(), []
    def add(n, kind): names.add(n)
    if 'tracks' in sc:
        for tr in sc['tracks']:
            for c in tr['clips']:
                add(c.get('label') or c.get('text'), c.get('kind') or c.get('type')); ids.append(c['id'])
    else:
        for l in sc['layers']:
            for o in l['objects']:
                add(o.get('name'), o.get('type') or o.get('kind')); ids.append(o['id'])
    return names, ids


def keep(o, names):
    """does the old template have this lab object? By name; a null is always kept (below); an object the app saved WITHOUT a name (a star
    made by scene.apply, app bug of 0.1.8) is known by its type's default name, so it matches an old template that names it so ("Star")"""
    n = o.get('name')
    if n in names or is_null(o): return True
    return not n and DEFAULT_NAME.get(o.get('type') or o.get('kind')) in names


def is_null(o):
    """a null object is a transform only: it is kept whether or not the old template had one (a v1 template has no nulls, a rigged v2 one needs
    them as parents)"""
    return (o.get('type') or o.get('kind')) == 'null'


def close(name, candidates, cutoff=0.6):
    return difflib.get_close_matches(slug(name), [slug(c) for c in candidates], n=1, cutoff=cutoff)


def main():
    proj_path, pack, out = sys.argv[1:4]
    proj = json.load(open(proj_path, encoding='utf-8'))
    comps = {slug(c['name']): c for c in proj['comps']}
    os.makedirs(out, exist_ok=True)
    done, missing, used = [], [], set()
    strict = '--strict' in sys.argv
    for f in sorted(os.listdir(pack)):
        if not f.endswith('.carvertemplate'): continue
        stem = f[:-len('.carvertemplate')]
        old = json.load(open(os.path.join(pack, f), encoding='utf-8'))
        comp = comps.get(stem)
        if comp is None and old.get('name') and slug(old['name']) in comps:
            comp = comps[slug(old['name'])]; stem_used = slug(old['name'])      # the lab comp carries the template's display name
            print('note: %s matched the lab comp by the template name %r' % (stem, old['name']))
        else: stem_used = stem
        if comp is None: missing.append(stem); continue
        used.add(stem_used)
        names, ids = old_names(old)
        prefix = re.match(r'^(.*?)_?\d+$', ids[0]).group(1) + '_' if ids else 'tpl_'
        scene = copy.deepcopy(comp['scene'])
        for l in scene['layers']:
            l['objects'] = [o for o in l['objects'] if keep(o, names)]
        scene['layers'] = [l for l in scene['layers'] if l['objects']]
        text = re.sub(r'\bclip_(\d+)\b', lambda m: prefix + m.group(1), json.dumps(scene))
        tpl = {'format': 'carvercat/2', 'minApp': '0.1.8'}
        tpl.update({k: v for k, v in old.items() if k not in ('scene', 'format', 'minApp')})
        tpl['scene'] = json.loads(text)
        w, h = scene['width'], scene['height']
        tpl['frame'] = {'width': int(w), 'height': int(h), 'fps': float(scene['fps'])}
        json.dump(tpl, open(os.path.join(out, f), 'w', encoding='utf-8'), indent=1)
        n = sum(len(l['objects']) for l in scene['layers'])
        done.append((stem, n, len(ids)))
    for stem, n, m in done: print('%-28s objects %d (old %d)%s' % (stem, n, m, '' if n == m else '  DIFFERENT'))
    if missing: print('no lab comp for:', ', '.join(missing))
    # A renamed lab comp must not be skipped quietly: a lab comp nobody claimed that is close to the name of a template with no comp
    # (or to any template at all) is reported loudly, on stderr, and with --strict the run fails.
    unused = [k for k in comps if k not in used]
    stems = [f[:-len('.carvertemplate')] for f in os.listdir(pack) if f.endswith('.carvertemplate')]
    warned = []
    for k in unused:
        near = close(k, missing or stems, 0.75)
        if near and slug(near[0]) in [slug(m) for m in missing]:
            warned.append(k)
            sys.stderr.write('WARNING: lab comp %r matches no template, but template %r has no lab comp: was the comp renamed? '
                             '(the template was NOT regenerated)\n' % (comps[k]['name'], near[0]))
    if warned and strict: sys.exit(3)


if __name__ == '__main__':
    main()
