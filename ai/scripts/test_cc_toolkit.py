"""Adversarial SDK tests independent of a running editor."""
import json, unittest
from unittest.mock import patch
from cc_client import Client, CarvercatError, OutcomeUnknown, endpoint
from cc_scene import Box, linear_hex, Scene
class ToolkitTests(unittest.TestCase):
 def test_refusal_stops_dependent_work(self):
  c=Client()
  with patch.object(c,'_request',return_value={'isError':True,'content':[{'type':'text','text':'refused'}]}):
   with self.assertRaises(CarvercatError):c.run('object.new')
 def test_unknown_outcome_never_retries(self):
  c=Client()
  with patch('cc_client.endpoint',return_value=(1,1234)),patch('cc_client.socket.create_connection') as connect:
   connect.return_value.__enter__.return_value.makefile.return_value.__enter__.return_value.readline.side_effect=[json.dumps({'result':{}}),'']
   with self.assertRaises(OutcomeUnknown):c.run('property.set',key='text',value='x')
   self.assertEqual(connect.call_count,1)
 def test_server_timeout_is_unknown_not_retryable(self):
  c=Client()
  with patch('cc_client.endpoint',return_value=(1,1234)),patch('cc_client.socket.create_connection') as connect:
   stream=connect.return_value.__enter__.return_value.makefile.return_value.__enter__.return_value
   stream.readline.side_effect=[json.dumps({'result':{}}),json.dumps({'jsonrpc':'2.0','id':1,'error':{'code':-32001,'message':'stalled'}})]
   with self.assertRaises(OutcomeUnknown):c.run('property.set',key='text',value='x')
   self.assertEqual(connect.call_count,1)
 def test_scene_refuses_changed_revision(self):
  class Fake:
   def state(self):return {'comp':{'width':1920,'height':1080,'name':'Comp'},'revision':self.revision,'authoringUnits':{'textSizeToPixels':.597},'document':{'path':None,'scenePointer':'/scene'}}
   def tool(self,*a,**k):return {'comps':[{'index':0,'name':'Comp','open':True}]}
  c=Fake();c.revision='before';s=Scene(c);s.create('title','text');c.revision='after'
  with self.assertRaises(CarvercatError):s.apply()
 def test_geometry_rejects_invalid_sizes(self):
  with self.assertRaises(ValueError):Box(0,0,-1,20)
  with self.assertRaises(ValueError):Box(0,0,100,20).inset(11)
 def test_colors_preserve_hex_alpha(self):
  self.assertEqual(linear_hex('#FFFFFF80')[:3],[1,1,1]);self.assertAlmostEqual(linear_hex('#FFFFFF80')[3],128/255)
 def test_nonfinite_input_rejected(self):
  with self.assertRaises(ValueError):Box(float('nan'),0,10,10)
 def test_path_places_duration_track_and_handles_at_creation(self):
  s=Scene.__new__(Scene);s.width=100;s.height=200;s.ids={};s.ambiguous={};s.steps=[];s.pending_objects={}
  s.path('curve',[(10,20),(80,150)],start=100,duration=40,track=2,handles=[{'in':[0,0],'out':[10,20]},{'in':[-10,-20],'out':[0,0]}])
  step=s.steps[0];self.assertEqual(step['frame'],100);self.assertEqual(step['args']['track'],2);self.assertEqual(step['args']['duration'],40)
  self.assertEqual(step['args']['handles'][0]['out'],[.1,.1]);self.assertFalse(any(x['command']=='clip.trim' for x in s.steps))
  with self.assertRaises(ValueError):s.path('curve',[(0,0),(1,1)])
 def test_invalid_path_is_not_queued(self):
  s=Scene.__new__(Scene);s.width=100;s.height=100;s.ids={};s.ambiguous={};s.steps=[];s.pending_objects={}
  with self.assertRaises(ValueError):s.path('bad',[(0,0),(1,1)],duration=-1)
  self.assertEqual(s.steps,[]);self.assertEqual(s.pending_objects,{})
 def test_stale_current_endpoint_refuses_without_legacy_fallback(self):
  import os,tempfile
  from pathlib import Path
  if os.name=='nt':self.skipTest('POSIX PID probe; native Windows remains a device check')
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'current.pid';p.write_text('12345 32123')
   with patch.dict(os.environ,{'CARVERCAT_MCP_ENDPOINT':str(p)}),patch('cc_client.os.kill',side_effect=ProcessLookupError):
    with self.assertRaises(CarvercatError):endpoint()
 def test_current_endpoint_accepts_native_lease_field(self):
  import os,tempfile
  from pathlib import Path
  if os.name=='nt':self.skipTest('POSIX probe fixture')
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'current.pid';p.write_text('12345\n32123\n12345-native-lease')
   with patch.dict(os.environ,{'CARVERCAT_MCP_ENDPOINT':str(p)}),patch('cc_client.os.kill'):
    self.assertEqual(endpoint(),(12345,32123))
if __name__=='__main__':unittest.main()
