"""Snapshot native parameter declarations; live availability remains authoritative."""
import argparse,json,hashlib
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--app',required=True);p.add_argument('--check',action='store_true');a=p.parse_args();source=Path(a.app)/'schema/registry.json';data=source.read_bytes();registry=json.loads(data);caps={}
for item in registry['params']:
 if item.get('status')!='shipped':continue
 cap=item['id'];caps.setdefault(cap,[]).append({k:item.get(k) for k in ['param','label','type','min','max','default','options','keyframeable','container','factoryPromote','absorbedBy']})
result={'version':1,'registrySha256':hashlib.sha256(data).hexdigest(),'authority':'Declarations only. Discover actual native bindings, values, units and availability with carvercat_authoring mode=controls; param.list describes panel/promotion state; unavailable native controls must not be treated as rendered. Repeated effects use exact entry aliases.','caps':caps}
target=Path(__file__).resolve().parents[1]/'ai/references/app/native-controls.json';text=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
if a.check:
 assert target.read_text(encoding='utf8')==text,'Native control snapshot stale'
else:target.write_bytes(text.encode('utf8'))
print(f'{len(caps)} capabilities / {sum(map(len,caps.values()))} declared parameters')
