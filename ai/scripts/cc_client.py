"""Validated MCP client. No automatic mutation retries; stdlib only."""
import base64
import contextlib
import json
import os
from pathlib import Path
import socket
import subprocess
import tempfile
import time

INIT = {"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"carvercat-skills","version":"2"}}
class CarvercatError(RuntimeError):
    def __init__(self, message, receipt=None):
        super().__init__(message); self.receipt = receipt
class OutcomeUnknown(CarvercatError): pass
class Refused(CarvercatError):
    """A command or scene was refused. .receipt is the reply: code, why, valid, example."""
    @property
    def code(self):return (self.receipt or {}).get('code')
    @property
    def example(self):return (self.receipt or {}).get('example')

def endpoint():
    """Prefer current editor; legacy fallback only when no current pointer exists."""
    explicit = os.environ.get("CARVERCAT_MCP_ENDPOINT")
    paths = [Path(explicit)] if explicit else [Path(tempfile.gettempdir()) / n for n in
        ("carvercat-mcp-editor.pid", "carvercat-mcp-dev.pid", "carvercat-mcp-work.pid", "carvercat-mcp-window.pid")]
    for p in paths:
        if p.exists():
            fields = p.read_text().split()
            if len(fields) not in (2,3): raise CarvercatError(f"Invalid endpoint file: {p}")
            pid, port = map(int, fields[:2])
            if pid<1 or not 0<port<65536: raise CarvercatError(f"Invalid endpoint: {p}")
            if os.name == "nt":
                import ctypes
                kernel=ctypes.windll.kernel32
                kernel.OpenProcess.restype=ctypes.c_void_p
                handle=kernel.OpenProcess(0x1000,False,pid)
                if not handle: raise CarvercatError(f"Stale editor PID {pid}; rediscover the actual app, do not fall back silently")
                kernel.CloseHandle.argtypes=[ctypes.c_void_p];kernel.CloseHandle(handle)
            else:
                try: os.kill(pid, 0)
                except ProcessLookupError: raise CarvercatError(f"Stale editor PID {pid}; rediscover the actual app, do not fall back silently")
                except PermissionError: pass  # Alive, but owned by a different user; handshake must still match.
            return pid, port
    raise CarvercatError("No editor endpoint; open Carvercat or use Client.stdio for an isolated scratch process")

class Client:
    def __init__(self, *, process=None, timeout=120):
        self.process=process; self.timeout=timeout;self.request_count=0;self.receipts=[];self._next=1;self.identity=None;self._txn_revision=None
        if process: self._request("initialize",INIT)
    @classmethod
    def stdio(cls, exe, state_dir, resource_root=None):
        """A private headless document. A host built from source needs its resource folder (the app repo root, which
        holds the fonts and the parameter registry): pass resource_root or set CARVERCAT_RESOURCE_ROOT."""
        state=Path(state_dir).resolve();state.mkdir(parents=True,exist_ok=True)
        env=os.environ.copy();env["RUST_MIN_STACK"]="268435456"
        if resource_root:env["CARVERCAT_RESOURCE_ROOT"]=str(resource_root)
        for key,leaf in [("CARVERCAT_PREFS_DIR","preferences"),("CARVERCAT_DATA_DIR","data"),("CARVERCAT_CACHE_DIR","cache")]:
            p=state/leaf;p.mkdir(exist_ok=True);env[key]=str(p)
        env["CARVERCAT_MCP_SESSION"]="skills-scratch-"+str(os.getpid())
        # No --ui/--connect: owns an isolated document, never attaches to the visible editor.
        proc=subprocess.Popen([str(exe),"--mcp"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,text=True,encoding="utf8",env=env)
        try:
            client=cls(process=proc)
            client.load_fonts()
            return client
        except BaseException:
            proc.terminate()
            try:proc.wait(timeout=5)
            except subprocess.TimeoutExpired:proc.kill();proc.wait(timeout=5)
            raise
    def load_fonts(self):
        """A fresh headless process measures text only after its font list has loaded; this loads it (scene.apply does too)."""
        return self.tool("carvercat_authoring",mode="fonts",query="Open Sans")
    def close(self):
        if self.process:
            self.process.stdin.close()
            try:self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:self.process.terminate();self.process.wait(timeout=5)
    def __enter__(self):return self
    def __exit__(self,*args):self.close()
    def _read(self, stream):
        # Bounded stdio read so a hung subprocess cannot hang a build forever.
        import queue,threading
        q=queue.Queue()
        def read():
            try:q.put(stream.readline())
            except Exception as e:q.put(e)
        threading.Thread(target=read,daemon=True).start()
        line=q.get(timeout=self.timeout)
        if isinstance(line,Exception):raise line
        if not line:raise EOFError("MCP disconnected")
        return json.loads(line)
    def _request(self, method, params):
        request={"jsonrpc":"2.0","id":self._next,"method":method,"params":params};self._next+=1
        start=time.perf_counter();sent=False
        try:
            if self.process:
                self.process.stdin.write(json.dumps(request)+"\n");self.process.stdin.flush();sent=True
                reply=self._read(self.process.stdout)
            else:
                pid,port=endpoint()
                with socket.create_connection(("127.0.0.1",port),timeout=min(2,self.timeout)) as conn:
                    conn.settimeout(self.timeout)
                    with conn.makefile("rw",encoding="utf8") as stream:
                        stream.write(json.dumps({"jsonrpc":"2.0","id":0,"method":"initialize","params":INIT})+"\n");stream.flush()
                        init=json.loads(stream.readline())
                        if "error" in init:raise CarvercatError(str(init["error"]))
                        stream.write(json.dumps(request)+"\n");stream.flush();sent=True
                        line=stream.readline()
                        if not line:raise EOFError("MCP disconnected")
                        reply=json.loads(line)
            if reply.get("id")!=request["id"]:raise ValueError("Mismatched MCP response id")
        except CarvercatError:raise
        except Exception as e:
            if sent:raise OutcomeUnknown("Request sent once; outcome unknown. Inspect state before another mutation.") from e
            raise CarvercatError(f"Cannot connect: {e}") from e
        self.request_count+=1;self.receipts.append({"method":method,"params":params,"seconds":time.perf_counter()-start,"response":reply})
        if "error" in reply:
            if reply["error"].get("code")==-32001:raise OutcomeUnknown("Server timeout: request sent once; inspect before any further mutation.",reply)
            raise CarvercatError(str(reply["error"]),reply)
        return reply["result"]
    def call(self,name,args=None):
        result=self._request("tools/call",{"name":name,"arguments":args or {}})
        if result.get("isError"):raise CarvercatError("; ".join(c.get("text","") for c in result.get("content",[])),result)
        return result
    def tool(self,name,**args):
        """One tool call, parsed. A refusal (isError with a JSON body) comes back as data: read `refused`, `code`, `why`."""
        result=self._request("tools/call",{"name":name,"arguments":args or {}})
        blocks=[c["text"] for c in result.get("content",[]) if c.get("type")=="text"]
        if len(blocks)!=1:raise CarvercatError(f"Expected one text receipt from {name}",result)
        try:body=json.loads(blocks[0])
        except json.JSONDecodeError:body=blocks[0]
        if result.get("isError") and not isinstance(body,dict):raise CarvercatError(str(body),result)
        if result.get("isError") and isinstance(body,dict):body.setdefault("refused",True)
        return body
    def resource(self,uri):return self._request("resources/read",{"uri":uri})
    def state(self):return self.tool("carvercat_state")
    def bind(self, *, commit=None, comp=None, project=None):
        state=self.state()
        if commit and state["build"]["commit"]!=commit:raise CarvercatError("Unexpected build identity",state)
        if comp is not None and state.get("comp",{}).get("name")!=comp:raise CarvercatError("Unexpected comp identity",state)
        if project is not None and Path(state["document"]["path"] or "").resolve()!=Path(project).resolve():raise CarvercatError("Unexpected project file",state)
        self.identity=state;return state
    def run(self,command,*,quiet=True,expected_revision=None,transaction=None,dry_run=False,check=True,**args):
        """One carvercat_run call. A refusal raises CarvercatError carrying the reply: .receipt has code, why, valid, example.
        Pass check=False to get the refusal back as data (a refusal is an answer, not a crash)."""
        if expected_revision is None and self._txn_revision is not None and transaction not in ("abort","commit"):expected_revision=self._txn_revision
        data={"command":command,"args":args}
        if dry_run:data["dry_run"]=True
        if expected_revision is not None:data["expected_revision"]=expected_revision
        if transaction is not None:data["transaction"]=transaction
        r=self.tool("carvercat_run",**data)
        if check and isinstance(r,dict) and (r.get("refused") or r.get("conflict")):
            extra="" if not r.get("example") else f" (example: {json.dumps(r['example'])})"
            raise Refused(f"{command}: {r.get('code','')} {r.get('why',r)}{extra}",r)
        if isinstance(r,dict) and self._txn_revision is not None:self._txn_revision=r.get("revision",self._txn_revision)
        if not quiet:print(command,json.dumps(r,ensure_ascii=False))
        return r
    # -- design-unit helpers (API 1.0): plain wrappers, no logic of their own ---------------------------------
    def apply_scene(self,scene,*,mode="merge",dry_run=False,preflight=None):
        """scene.apply: ONE document, validated whole, one undo step. dry_run=True changes nothing.
        preflight='resolve'|'aftereffects' runs carve.preflight afterwards and returns (reply, preflight_reading)."""
        doc=scene.to_dict() if hasattr(scene,"to_dict") else scene
        # dry_run is an ARGUMENT of scene.apply here, not the envelope's dry_run of carvercat_run
        reply=self.tool("carvercat_run",command="scene.apply",args={"scene":doc,"mode":mode,"dry_run":dry_run})
        if not (reply.get("scene") or {}).get("validated",False):
            problems=(reply.get("scene") or {}).get("refused",[])
            why="; ".join(f"{x.get('object')} {x.get('path')}: {x.get('why')}" for x in problems[:8]) or str(reply.get("why"))
            raise Refused("scene.apply refused: "+why,reply)
        if preflight:return reply,self.preflight(preflight)
        return reply
    def scene(self,selector=None):
        """scene.get: the open comp as a scene document (the format apply_scene takes)."""
        r=self.run("scene.get",**({"selector":selector} if selector else {}))
        return r["readings"][0]["scene"]
    def query(self,selector,limit=200):
        return self.run("select.query",selector=selector,limit=limit)["readings"][0]["matches"]
    def ids(self,selector):return [m["id"] for m in self.query(selector)]
    def set(self,target,**props):
        """property.set of design keys on every object `target` (an id, a scene id as #id, or a selector) finds."""
        last=None
        for key,value in props.items():last=self.run("property.set",id=target,key=key,value=value)
        return last
    def get(self,target,key):return self.run("property.get",id=target,key=key)["readings"][0]
    def animate(self,target,**anim):
        """anim.set: keyframes=[{at, <props>, ease}] or to/from/fromTo + duration/delay/ease, stagger, motionPath."""
        if "from_" in anim:anim["from"]=anim.pop("from_")
        return self.run("anim.set",id=target,**anim)
    def path(self,d,frame=None,duration=None,**style):
        """object.path from SVG path data in px (y down; one subpath), then its design style. Returns the object id.
        (Inside a scene document use `Scene.path`, a `type: "path"` node.)"""
        extra={"duration":duration} if duration is not None else {}
        if frame is not None:self.run("view.seek",frame=frame)   # object.path places at the playhead
        oid=self.run("object.path",d=d,**extra)["touched"][0]
        if frame is not None:self.run("view.seek",frame=0)
        for key,value in style.items():self.run("property.set",id=oid,key=key,value=value)
        return oid
    def preflight(self,host):
        """carve.preflight: what carves exactly, approximately or not at all on 'resolve' or 'aftereffects'. Nothing is sent."""
        return self.run("carve.preflight",host=host)["readings"][0]
    def measure(self,ids=None):
        return self.run("measure.boxes",**({"ids":ids} if ids else {}))["readings"][0]
    def batch(self,steps,*,expected_revision=None,expected_document=None,dry_run=False,observe=None):
        if expected_revision is None:
            state=self.state();expected_revision=state["revision"];expected_document=state["document"]
        data={"steps":steps,"expected_revision":expected_revision,"dry_run":dry_run}
        if expected_document is not None:data["expected_document"]=expected_document
        if observe is not None:data["observe"]=observe
        return self.tool("carvercat_batch",**data)
    @contextlib.contextmanager
    def transaction(self):
        revision=self.state()["revision"]
        self.run("view.seek",frame=self.state()["playhead"],transaction="begin",expected_revision=revision)
        self._txn_revision=revision
        try:
            yield self
        except OutcomeUnknown:
            raise
        except Exception:
            # Unknown outcomes must be inspected by the caller, never automatically replayed.
            self.run("view.seek",frame=self.state()["playhead"],transaction="abort")
            raise
        else:self.run("view.seek",frame=self.state()["playhead"],transaction="commit")
        finally:self._txn_revision=None
    def look(self,path="look.png",**args):
        result=self.call("carvercat_look",args);images=[];texts=[]
        for c in result.get("content",[]):
            if c.get("type")=="image":images.append((c.get("mimeType"),base64.b64decode(c["data"])))
            elif c.get("type")=="text":
                try:texts.append(json.loads(c["text"]))
                except json.JSONDecodeError:texts.append(c["text"])
        files=[]
        for i,(_,data) in enumerate(images):
            target=Path(path) if len(images)==1 else Path(path).with_name(Path(path).stem+f"-{i}"+Path(path).suffix)
            target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data);files.append(str(target))
        return {"files":files,"metadata":texts,"unchanged":not images}

_default=Client()
def port():return endpoint()[1]
def call(name,args=None):return {"result":_default.call(name,args)}
def tool(name,**args):return _default.tool(name,**args)
def run(cmd,quiet=False,**args):return _default.run(cmd,quiet=quiet,**args)
def res(uri):return {"result":_default.resource(uri)}
def look(path="look.png",**args):return _default.look(path,**args)
