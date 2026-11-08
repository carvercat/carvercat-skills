"""Load every .carverpreset of the Motion Patterns pack in a fresh headless Carvercat and apply it to a shape (or a text, for the
staggered ones). The presets stay in the app's stored preset format (built by build_pattern_pack.py); this only proves they load and apply.

    python3 motion_patterns_presets_check.py [--app HOST] [--resource-root ROOT]

Prints one line per preset: applied, number of keyframes it wrote (comp.scene), and exits 1 if any preset is not listed by the
library, is refused, or writes nothing.
"""
import argparse, json, os, shutil, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
from cc_client import Client  # noqa: E402
PACK = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'library', 'templates', 'motion-patterns'))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--app'); ap.add_argument('--resource-root')
    a = ap.parse_args()
    app = a.app or os.environ.get('CARVERCAT_HOST'); rr = a.resource_root or os.environ.get('CARVERCAT_RESOURCE_ROOT')
    state = tempfile.mkdtemp(prefix='ccpresets-')
    cwd = os.getcwd(); os.chdir(tempfile.gettempdir())
    try: c = Client.stdio(app, state, resource_root=rr)
    finally: os.chdir(cwd)
    lib = os.path.join(state, 'data', 'library', 'templates', 'motion-patterns'); os.makedirs(lib)
    presets = []
    for f in sorted(os.listdir(PACK)):
        if f.endswith(('.carverpreset', '.carverpack')): shutil.copy(os.path.join(PACK, f), lib)
        if f.endswith('.carverpreset'): presets.append(json.load(open(os.path.join(PACK, f))))
    c.run('library.reload')
    bad = 0
    for p in presets:
        text = bool(p.get('only') == 'text')
        c.run('comp.new', name='preset ' + p['name'])
        node = {'id': 'o', 'type': 'text' if text else 'rect', 'name': 'Target', 'style': {'x': 400, 'y': 400, 'width': 800, 'height': 200, 'fill': '#FFFFFF'}}
        if text: node.update(text='Check these words', style={'x': 400, 'y': 400, 'width': 800, 'height': 200, 'fill': '#FFFFFF', 'fontSize': 80, 'whiteSpace': 'normal', 'fontFamily': 'Open Sans'})
        c.apply_scene({'schema': 'carvercat/2.0', 'comp': {'width': 1920, 'height': 1080, 'fps': 30, 'duration': 60}, 'children': [node]})
        oid = c.tool('carvercat_list')['objects'][0]['id']
        c.run('select.clip', id=oid, check=False)
        r = c.run('preset.apply', name=p['name'], id=oid, check=False)
        sc = c.run('scene.get')['readings'][0]['scene']['children'][0]
        keys = len(sc.get('keyframes', [])); staggered = 'stagger' in sc
        ok = not r.get('refused') and (keys > 0 or staggered)
        bad += not ok
        print('%-4s %-28s keys %-3d%s  %s' % ('OK' if ok else 'FAIL', p['name'], keys, ' stagger' if staggered else '', '' if ok else r.get('why')), flush=True)
    c.close(); shutil.rmtree(state, ignore_errors=True)
    print('%d presets, %d failed' % (len(presets), bad)); sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
