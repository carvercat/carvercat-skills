"""Reproducible scratch example; never modifies the visible editor."""
import argparse
from pathlib import Path
from cc_client import Client
from cc_scene import Scene,Box,title_pair,card_group
p=argparse.ArgumentParser();p.add_argument('--exe',required=True);p.add_argument('--output',required=True);a=p.parse_args();out=Path(a.output).resolve();out.mkdir(parents=True,exist_ok=True)
with Client.stdio(Path(a.exe).resolve(),out/'state') as c:
 s=Scene(c);title_pair(s,'One idea, three steps','Discover / Compose / Refine',box=Box(250,140,1420,260))
 for i,label in enumerate(['Discover','Compose','Refine']):card_group(s,f'step{i}',f'0{i+1}',label,box=Box(250+i*490,500,440,280))
 s.apply();s.fit('title',Box(250,140,1420,170));s.rebind();s.entrance(['title','subtitle'],frames=12,stagger=4);s.apply()
 s.review(out/'preview.png',frames=(0,8,20,60));c.run('edit.save',path=str(out/'example.carverproj'));s.rebind();s.manifest(out/'objects.json')
 print(out/'example.carverproj')
