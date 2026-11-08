"""Write the explainer/ex-showcase sample project in design units: the four round-1 Explainer lab comps cut together into one 14.5 s
explainer, each placed as a nested comp (cc2 Comp.nest) in a master over a light ground.

    import explainer_showcase as SH; doc = SH.build(); doc.send(client, PROJECT.carverproj)

The first two scenes are holds and keep a slow 2 % push: it is keyed on their instances after they are placed (ShowDoc.send).
After sending: lint, look and qc the master. Docs: ai/patterns/explainer.md.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explainer_lab as L
from explainer_lab import Doc

SCENES = [("EX Process steps", 0, 120), ("EX Icon grid", 120, 90), ("EX Callout", 210, 75), ("EX Timeline", 285, 150)]
LENGTH = 435


class ShowDoc(Doc):
    """a Doc that can key the scale of a placed instance (cc2 places instances but does not key them)"""
    pushes = ()          # [(instance start frame, length, scale at the end)]

    def send(self, client, save_path):
        Doc.send(self, client, save_path)
        lst = client.tool('carvercat_list')
        inst = {int(o['start']): o for o in lst['objects'] if o.get('kind') == 'nestedTimeline'}
        for start, length, to in self.pushes:
            client.run('anim.set', id=inst[start]['id'], keyframes=[dict(at=0, ease='linear', scale=1.0),
                                                                  dict(at=length, scale=to)])
        client.run('edit.save', path=save_path)
        return save_path


def build():
    d = ShowDoc()
    L.process_steps(d); L.icon_grid(d); L.callout(d); L.timeline(d)
    comps = {c.name: c for c in d.comps}
    master = d.comp("Explainer showcase", LENGTH, "eshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL["bg"], f0=0, dur=LENGTH)
    for name, f0, dur in SCENES:
        master.nest(comps[name], f0=f0, dur=dur)
    d.pushes = [(f0, dur, 1.02) for name, f0, dur in SCENES[:2]]
    return d


if __name__ == "__main__":
    print(__doc__)
