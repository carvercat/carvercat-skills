"""Rebuild the round-2 showcase sample projects (categories/<cat>/<id>-showcase-2/project.carverproj) as carvercat/2.

    python3 regen_showcase2.py kinetic-typography explainer ...     # families of recipes/showcase2.py

Each master is the family's round-2 templates placed back to back from the Library (library.place + template.apply, the packs of
this checkout's library/templates installed into a fresh user Library) by recipes/showcase2.py, in an isolated headless host
(CARVERCAT_HOST, CARVERCAT_RESOURCE_ROOT). The saved project replaces the family's showcase-2 project. Nothing else is touched.
"""
import json, os, re, shutil, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
# family (recipes/showcase2.py FAMILIES key) -> the category folder and the showcase-2 project folder in it
CATEGORY = {"cartoon-bounce": "cartoon-bounce/ct-showcase-2", "corporate-brand": "corporate-brand/cb-showcase-2",
            "data-viz": "data-viz/dv-showcase-2", "explainer": "explainer/ex-showcase-2", "funky": "funky/fk-showcase-2",
            "futuristic-hud": "futuristic-hud/fh-showcase-2", "glitch": "glitch/gl-showcase-2",
            "kinetic-typography": "kinetic-typography/kt-showcase-2", "minimal-luxury": "minimal-luxury/ml-showcase-2",
            "retro": "retro/rt-showcase-2", "saas-ui": "saas-launch/saas-ui-showcase-2",
            "social-short-form": "social-media-reels/ss-showcase-2", "sports": "sports/sp-showcase-2"}


def main(keys):
    host = os.environ.get('CARVERCAT_HOST')
    if not host or not os.path.exists(host): sys.exit('set CARVERCAT_HOST')
    work = tempfile.mkdtemp(prefix='ccsc2-')
    os.environ.update(CARVERCAT_EXE=host, CARVERCAT_STATE=os.path.join(work, 'state'), RECIPE_LAB=os.path.join(work, 'lab'),
                      RECIPE_ROUTE='file')
    os.makedirs(os.environ['RECIPE_LAB'], exist_ok=True)
    sys.path.insert(0, os.path.join(HERE, 'recipes'))
    import showcase2, recipe_kit
    for key in keys:
        path, n = showcase2.build(key)
        dest = os.path.join(REPO, 'categories', CATEGORY[key], 'project.carverproj')
        shutil.copyfile(path, dest)
        recipe_kit.scrub_template_paths(dest)               # a placed template records where the host found it (a scratch path): keep the library-relative part
        print(key, n, 'frames ->', dest)


if __name__ == '__main__':
    keys = sys.argv[1:] or sorted(CATEGORY)
    unknown = [k for k in keys if k not in CATEGORY]
    if unknown: sys.exit('no CATEGORY entry for: ' + ', '.join(unknown))
    main(keys)
