"""Rebuild a pack's lab, send it to a headless Carvercat and rewrite the pack's templates (the whole chain in one command).

    python3 regen_pack.py transitions_lab --pack transitions --app /path/to/carvercat-host [--keep PROJECT.carverproj] [--no-templates] [--timeout 900]

LAB is a lab or showcase module's name here (it must have build() -> cc2.Doc). The lab is sent with scene.apply to a fresh isolated
host (fresh prefs/data/cache), saved as a carvercat/2 project, and regen_templates.py rewrites library/templates/<pack>
from it. Nothing outside the scratch folders and the pack folder is touched. App: --app or CARVERCAT_HOST; resource root:
--resource-root or CARVERCAT_RESOURCE_ROOT (the app repo root, for fonts and the parameter registry).
"""
import argparse, importlib, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..'))
from cc_client import Client  # noqa: E402

REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('lab'); ap.add_argument('--pack', required=True)
    ap.add_argument('--app'); ap.add_argument('--resource-root'); ap.add_argument('--keep', help='save the project here (a .carverproj)')
    ap.add_argument('--timeout', type=float, default=900, help='client reply timeout in seconds (a big comp takes minutes on a busy Mac; the client\'s own default is 120)')
    ap.add_argument('--no-templates', action='store_true', help='only write the project (sample projects such as a showcase)')
    a = ap.parse_args()
    app = a.app or os.environ.get('CARVERCAT_HOST')
    if not app or not os.path.exists(app): sys.exit('give the host with --app or CARVERCAT_HOST')
    rr = a.resource_root or os.environ.get('CARVERCAT_RESOURCE_ROOT')
    if rr is None:
        cand = os.path.abspath(os.path.join(REPO, '..', 'carvercat'))
        rr = cand if os.path.isdir(cand) else None
    doc = importlib.import_module(a.lab).build()
    state = tempfile.mkdtemp(prefix='ccregen-')
    proj = os.path.abspath(a.keep) if a.keep else os.path.join(state, 'lab.carverproj')
    cwd = os.getcwd(); os.chdir(tempfile.gettempdir())
    try: c = Client.stdio(app, state, resource_root=rr)
    finally: os.chdir(cwd)
    c.timeout = max(getattr(c, 'timeout', 120), a.timeout)
    try:
        doc.send(c, proj)
    finally:
        c.close()
    if a.no_templates: print('project:', proj); return
    pack = os.path.join(REPO, 'library', 'templates', a.pack)
    subprocess.check_call([sys.executable, os.path.join(HERE, 'regen_templates.py'), proj, pack, pack])


if __name__ == '__main__':
    main()
