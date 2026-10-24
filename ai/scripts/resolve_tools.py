"""DaVinci Resolve side helpers. Tested Resolve Studio 21.1, 2026-09-30.
CLI: python resolve_tools.py import-place <seq_dir> <prefix> <n_frames> <video_track> <timeline_local_start>
     python resolve_tools.py stills <outdir> <start> <end> <step>     (composite stills via Color page GrabStill)
"""
import sys, os
sys.path.append(r"C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\Modules")
os.environ.setdefault("RESOLVE_SCRIPT_LIB", r"C:\Program Files\Blackmagic Design\DaVinci Resolve\fusionscript.dll")
import DaVinciResolveScript as dvr

def ctx():
    r = dvr.scriptapp("Resolve"); pm = r.GetProjectManager(); pj = pm.GetCurrentProject()
    return r, pm, pj, pj.GetMediaPool(), pj.GetCurrentTimeline()

def import_place(seq_dir, prefix, n, track, local_start=0):
    r, pm, pj, mp, tl = ctx()
    if tl.GetTrackCount('video') < track: tl.AddTrack('video')
    base0 = tl.GetStartFrame()   # only the target range must be free, so several clips can share one track
    assert not [c for c in tl.GetItemListInTrack('video', track) if c.GetStart() < base0 + local_start + n and c.GetEnd() > base0 + local_start], f"V{track} is not free at that range"
    it = mp.ImportMedia([{"FilePath": os.path.join(seq_dir, prefix + "_%05d.png"), "StartIndex": 0, "EndIndex": n - 1}])[0]
    # Numeric 30.0 did not apply in the Cairo session: the PNG stayed at 24 fps.
    assert it.SetClipProperty("FPS", "30"), "Could not set source FPS"
    assert float(it.GetClipProperty("FPS")) == 30.0, "Source FPS did not persist"
    assert it.GetClipProperty("Alpha mode") == "Straight", it.GetClipProperty("Alpha mode")
    base = tl.GetStartFrame()
    mp.AppendToTimeline([{"mediaPoolItem": it, "startFrame": 0, "endFrame": n,   # endFrame=n gives n frames here (n-1 gave n-1)
                          "trackIndex": track, "recordFrame": base + local_start, "mediaType": 1}])
    got = [c for c in tl.GetItemListInTrack('video', track) if c.GetStart() == base + local_start][0]
    assert got.GetDuration() == n, got.GetDuration()
    pm.SaveProject()
    return got.GetStart(), got.GetEnd()

def stills(out, a, b, step, fps=30):
    r, pm, pj, mp, t = ctx(); r.OpenPage("color")
    alb = pj.GetGallery().GetCurrentStillAlbum(); base = t.GetStartFrame(); got = []
    def tc(f): return "%02d:%02d:%02d:%02d" % (f // (fps*3600), f // (fps*60) % 60, f // fps % 60, f % fps)
    for f in range(a, b, step):
        t.SetCurrentTimecode(tc(base + f)); got.append((f, t.GrabStill()))
    alb.ExportStills([s for _, s in got], out, "f", "png")   # files f_1.1.N.png in grab order
    for _, s in got: alb.DeleteStills([s])
    r.OpenPage("edit")

if __name__ == "__main__":
    if sys.argv[1] == "import-place": print(import_place(sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])))
    elif sys.argv[1] == "stills": stills(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
