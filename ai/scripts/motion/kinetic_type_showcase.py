"""Write the kinetic-typography/kt-showcase sample project in design units: the five round-1 Kinetic Typography lab comps cut together
into one 14.3 s master, each placed as a nested comp (cc2 Comp.nest) over a dark ground.

    import kinetic_type_showcase as SH; doc = SH.build(); doc.send(client, PROJECT.carverproj)

Hard cuts, each scene plays its full length. The Impact stack's 50 f hold keeps a slow 4 % push, keyed on its instance after it is
placed (ShowDoc.send). After sending: lint, look and qc the master. Docs: ai/patterns/kinetic-typography.md.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kinetic_type_lab as L

# (comp, start in the master, length)
SCENES = [("KT Focus pull", 0, 60), ("KT Word swap", 60, 120), ("KT Impact stack", 180, 90),
          ("KT Line reveal", 270, 60), ("KT Beat words", 330, 100)]
LENGTH = 430


class ShowDoc(L.KDoc):
    pushes = ()          # [(instance start frame, length, scale at the end)]

    def send(self, client, save_path):
        L.KDoc.send(self, client, save_path)
        inst = {int(o['start']): o for o in client.tool('carvercat_list')['objects'] if o.get('kind') == 'nestedTimeline'}
        for start, length, to in self.pushes:
            client.run('anim.set', id=inst[start]['id'], keyframes=[dict(at=0, ease='linear', scale=1.0), dict(at=length, scale=to)])
        client.run('edit.save', path=save_path)
        return save_path


def build():
    d = ShowDoc()
    L.word_swap(d); L.impact_stack(d); L.line_reveal(d); L.beat_words(d); L.focus_pull(d)
    comps = {c.name: c for c in d.comps}
    master = d.comp("Kinetic type showcase", LENGTH, "kshow")
    master.rect("Background", 0, 0, 1920, 1080, L.COL['bg'], f0=0, dur=LENGTH)
    for name, f0, dur in SCENES:
        master.nest(comps[name], f0=f0, dur=dur)
    d.pushes = [(f0, dur, 1.04) for name, f0, dur in SCENES if name == "KT Impact stack"]
    return d


if __name__ == "__main__":
    print(__doc__)
