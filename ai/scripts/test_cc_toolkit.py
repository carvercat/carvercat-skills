"""Tests of the Python toolkit.

Offline tests need nothing. Live tests run against a real headless Carvercat (`carvercat-host --mcp`) and are
skipped unless CARVERCAT_EXE names a built executable. Each live test gets a fresh document, fresh preferences, data
and cache folders, and never touches an open app:

    CARVERCAT_EXE=/path/to/carvercat-host python3 test_cc_toolkit.py
"""
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent / "motion" / "json_author"))
import cc2
from cc_client import CarvercatError, Client, OutcomeUnknown, Refused, endpoint
from cc_scene import Box, Scene, css_colour, gradient

EXE = os.environ.get("CARVERCAT_EXE")


class OfflineTests(unittest.TestCase):
    def test_refusal_raises_with_code_and_example(self):
        c = Client()
        reply = {"refused": True, "code": "bad-unit", "why": "no", "example": {"key": "x", "value": "10px"}}
        with patch.object(c, "tool", return_value=reply):
            with self.assertRaises(Refused) as ctx:
                c.run("property.set", id="a", key="x", value="10 px")
        self.assertEqual(ctx.exception.code, "bad-unit")
        self.assertEqual(ctx.exception.example["key"], "x")
        with patch.object(c, "tool", return_value=reply):
            self.assertTrue(c.run("property.set", check=False, id="a", key="x", value="10 px")["refused"])

    def test_unknown_outcome_never_retries(self):
        c = Client()
        with patch("cc_client.endpoint", return_value=(1, 1234)), patch("cc_client.socket.create_connection") as connect:
            connect.return_value.__enter__.return_value.makefile.return_value.__enter__.return_value.readline.side_effect = [json.dumps({"result": {}}), ""]
            with self.assertRaises(OutcomeUnknown):
                c.run("property.set", key="text", value="x")
            self.assertEqual(connect.call_count, 1)

    def test_server_timeout_is_unknown_not_retryable(self):
        c = Client()
        with patch("cc_client.endpoint", return_value=(1, 1234)), patch("cc_client.socket.create_connection") as connect:
            stream = connect.return_value.__enter__.return_value.makefile.return_value.__enter__.return_value
            stream.readline.side_effect = [json.dumps({"result": {}}), json.dumps({"jsonrpc": "2.0", "id": 1, "error": {"code": -32001, "message": "stalled"}})]
            with self.assertRaises(OutcomeUnknown):
                c.run("property.set", key="text", value="x")
            self.assertEqual(connect.call_count, 1)

    def test_box_is_px_top_left_and_rejects_bad_sizes(self):
        self.assertEqual(Box(100, 50, 200, 80).center, (200, 90))
        with self.assertRaises(ValueError):
            Box(0, 0, -1, 20)
        with self.assertRaises(ValueError):
            Box(0, 0, 100, 20).inset(11)
        with self.assertRaises(ValueError):
            Box(float("nan"), 0, 10, 10)

    def test_colours_are_css_strings_not_linear_arrays(self):
        self.assertEqual(css_colour("#FF7A00"), "#FF7A00")
        self.assertEqual(css_colour("orange"), "orange")
        with self.assertRaises(ValueError):
            css_colour("#FF7A0")
        with self.assertRaises(ValueError):
            css_colour([1, 0, 0])
        self.assertEqual(gradient([(0, "#ff7a00"), (100, "#1b1b1b")]), "linear-gradient(90deg, #ff7a00 0%, #1b1b1b 100%)")

    def test_scene_document_is_design_units(self):
        s = Scene(None, width=1080, height=1080, fps=30, duration="4s")
        s.rectangle("Plate", Box(80, 700, 820, 220), fill="#1a1c26", radius=22)
        s.text("Name", "Alex", box=Box(190, 719, 620, 110), size=96)
        s.entrance(["Plate"], frames=20, scale=1)
        doc = s.to_dict()
        self.assertEqual(doc["schema"], "carvercat/2.0")
        plate = doc["children"][0]
        self.assertEqual((plate["id"], plate["style"]["x"], plate["style"]["y"], plate["style"]["borderRadius"]), ("Plate", 80, 700, 22))
        self.assertEqual(plate["keyframes"][1]["at"], 20)
        self.assertEqual(doc["children"][1]["style"]["whiteSpace"], "normal")

    def test_scene_ids_are_slugged_and_stable(self):
        s = Scene(None, duration="2s")
        s.text("Big title", "x", x=0, y=0)
        self.assertEqual(s.target("Big title"), "#Big-title")
        s.text("Big title", "y", x=5, y=0)
        self.assertEqual(len(s.nodes), 1)
        self.assertEqual(s.nodes[0]["text"], "y")
        with self.assertRaises(CarvercatError):
            s.rectangle("Big title", Box(0, 0, 1, 1))

    def test_keys_merge_by_time(self):
        s = Scene(None)
        s.rectangle("a", Box(0, 0, 10, 10))
        s.keys("a", "x", [(0, 0), ("1s", 100)]).keys("a", "opacity", [(0, 0), ("1s", 1)], ease="linear")
        kf = s.nodes[0]["keyframes"]
        self.assertEqual(len(kf), 2)
        self.assertEqual(kf[0]["props"], {"x": 0, "opacity": 0})

    def test_component_prefix(self):
        s = Scene(None)
        with s.component("Header") as h:
            h.rectangle("Plate", Box(0, 0, 10, 10))
        self.assertEqual(s.nodes[0]["id"], "Header-Plate")

    def test_stale_current_endpoint_refuses_without_legacy_fallback(self):
        if os.name == "nt":
            self.skipTest("POSIX PID probe")
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "current.pid"
            p.write_text("12345 32123")
            with patch.dict(os.environ, {"CARVERCAT_MCP_ENDPOINT": str(p)}), patch("cc_client.os.kill", side_effect=ProcessLookupError):
                with self.assertRaises(CarvercatError):
                    endpoint()

    def test_current_endpoint_accepts_native_lease_field(self):
        if os.name == "nt":
            self.skipTest("POSIX probe fixture")
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "current.pid"
            p.write_text("12345\n32123\n12345-native-lease")
            with patch.dict(os.environ, {"CARVERCAT_MCP_ENDPOINT": str(p)}), patch("cc_client.os.kill"):
                self.assertEqual(endpoint(), (12345, 32123))

    def test_cc_project_writes_a_valid_carvercat_2_file(self):
        from cc_project import Project, check, srgb
        self.assertEqual(srgb("#FF0000"), "color(srgb 1.0 0.0 0.0 / 1.0)")
        self.assertEqual(srgb("#0f0"), srgb("#00FF00"))
        with self.assertRaises(ValueError):
            srgb("orange")
        p = Project("Offline")
        p.comp("A", width=1080, height=1920, frames=90)
        p.rectangle("Background", fill=("#1B1B4D", "#0E0E2A"))
        p.rectangle("Card", (100, 200, 400, 300), fill="#FF0000", radius=10, start=10, duration=50, track=1)
        doc = p.to_dict()
        self.assertTrue(check(doc))
        self.assertEqual(doc["format"], "carvercat/2")
        self.assertEqual([len(l["objects"]) for l in doc["comps"][0]["scene"]["layers"]], [1, 1])
        with self.assertRaises(ValueError):
            check({"format": "carvercat/1"})
        with self.assertRaises(ValueError):
            Project("x").rectangle("no comp")


class Cc2OfflineTests(unittest.TestCase):
    def test_bezier_points_become_path_data(self):
        d = cc2.bezier([(100, 100), (300, 100, (-50, 0), (50, 0)), (500, 300, (-40, -40), None)])
        self.assertEqual(d, "M 100 100 C 100 100 250 100 300 100 C 350 100 460 260 500 300")
        self.assertEqual(cc2.bezier([(0, 0), (10, 0), (10, 10)], closed=True), "M 0 0 L 10 0 L 10 10 L 0 0 Z")

    def test_path_node_has_data_and_no_box(self):
        doc = cc2.Doc(); k = doc.comp("A", 30, "a")
        p = k.path("Line", cc2.bezier([(200, 900), (1720, 900)]), "#00E5C3", 12)
        p.trim([(0, 0, "linear"), (20, 100, "ease-out")])
        n = k.scene()["children"][0]
        self.assertEqual((n["type"], n["d"], "x" in n["style"], n["style"]["strokeWidth"]), ("path", "M 200 900 L 1720 900", False, 12))
        self.assertEqual(n["keyframes"][1]["props"], {"trimEnd": "100%"})

    def test_null_and_children_count_from_the_parent(self):
        doc = cc2.Doc(); k = doc.comp("A", 30, "a")
        nul = k.null("Pivot", 960, 540)                                   # nominal 100 x 100 box: top-left (910, 490)
        box = k.rect("Sign", 1000, 500, 300, 200, "#FF7A00", center=False)   # top-left (1000, 500) in the comp
        nul.child(box)
        box.pos([(0, (1150, 600), "linear"), (10, (1250, 600), "linear")])
        nul.rot([(0, 0, "ease-out"), (30, 20, "linear")])
        scene = k.scene()
        self.assertEqual([c["id"] for c in scene["children"]], ["a_1"])            # the child is no longer top level
        n = scene["children"][0]
        self.assertEqual((n["type"], n["style"]["x"], n["style"]["y"], "width" in n["style"]), ("null", 910, 490, False))
        c = n["children"][0]
        self.assertEqual((c["style"]["x"], c["style"]["y"]), (90, 10))              # 1000 - 910, 500 - 490
        self.assertEqual(c["keyframes"][1]["props"], {"x": 190, "y": 10})

    def test_text_stagger_and_per_property_keys(self):
        doc = cc2.Doc(); k = doc.comp("A", 60, "a")
        t = k.text("Title", "HELLO", 960, 540, 120, "#FFFFFF")
        t.stagger(by="chars", each=2, keyframes=[(0, {"opacity": 0, "y": 40}, "ease-out"), (12, {"opacity": 1, "y": 0}, None)])
        n = k.scene()["children"][0]
        self.assertEqual(n["stagger"]["target"], "chars")
        self.assertEqual(n["stagger"]["keyframes"][0], {"at": 0, "props": {"opacity": 0, "y": 40}, "ease": "ease-out"})
        u = k.text("Other", "HI", 960, 800, 120, "#FFFFFF")
        u.tracking([(0, 30, "ease-out"), (40, 0, "linear")])
        u.size([(0, 100, "linear"), (40, 120, "linear")])
        self.assertEqual(k.scene()["children"][1]["keyframes"][0]["props"], {"fontSize": 100, "letterSpacing": 30})
        t.tracking([(0, 30, "ease-out"), (40, 0, "linear")])
        with self.assertRaises(ValueError):
            k.scene()

    def test_nested_comps_are_sent_before_the_comp_that_places_them(self):
        doc = cc2.Doc(); a = doc.comp("Outer", 60, "o"); b = doc.comp("Inner", 30, "i")
        a.nest(b, f0=10)
        self.assertEqual([c.name for c in doc.order()], ["Inner", "Outer"])

    def test_v1_corrections_are_doc_options_and_off_by_default(self):
        k = cc2.Doc().comp("A", 30, "a")
        k.rect("R", 0, 0, 400, 100, "#FFFFFF", r=50).key("opacity", [(0, 0.0, "Linear"), (10, 1.0, "Ease out")])
        self.assertEqual(k.scene()["children"][0]["keyframes"][0]["ease"], "ease-out")                  # the CSS curve, as before
        doc = cc2.Doc(v1_look=True); k = doc.comp("A", 30, "a")
        r = k.rect("R", 0, 0, 400, 100, "#FFFFFF", r=50).key("opacity", [(0, 0.0, "Linear"), (10, 1.0, "Ease out")])
        doc.cap_radii()
        n = k.scene()["children"][0]
        self.assertEqual(n["keyframes"][0]["ease"], "cubic-bezier(0.33333, 0.66667, 0.66667, 1)")        # the app model's Ease out
        self.assertEqual(n["style"]["borderRadius"], 25.0)                                               # a quarter of the short side
        self.assertEqual(cc2.ease("v1-s-curve"), "cubic-bezier(0.33333, 0, 0.66667, 1)")

    def test_hard_shadow_text_at_and_path_boxes(self):
        doc = cc2.Doc(path_boxes=True); k = doc.comp("A", 30, "a")
        o = k.rect("R", 0, 0, 100, 100, "#FFFFFF").hard_shadow("#000000", 16)
        self.assertEqual(o.style["dropShadow"], "16px 9px 0px #000000")
        t = k.text_at("T", "Hello", 100, 500, 50, "#FFFFFF", track=1.2, lh=1.1, align="right")
        self.assertEqual((t.style["letterSpacing"], t.style["lineHeight"], t.box[1], t.px), (16.75, 1.474, 500, 50))
        self.assertEqual(t.box[0], 100 - t.box[2] / 2)
        p = k.path("P", cc2.bezier([(100, 100), (300, 100, (-50, 0), (50, 0)), (500, 300)]), "#FFFFFF", 4)
        x, y, w, h = cc2.path_box(p.d)
        self.assertEqual((x, w, p.base), (100, 400, (300.0, p.base[1])))
        self.assertEqual(cc2.path_box("M 5 5 L 5 5")[2:], (1.0, 1.0))

    def test_masks_carry_path_and_text_content_for_the_second_pass(self):
        k = cc2.Doc().comp("A", 30, "a")
        win = k.rect("Window", 0, 0, 200, 200, "#FFFFFF"); line = k.path("Line", "M 0 0 L 10 10", "#FFFFFF", 2); txt = k.text("Word", "Hi", 100, 100, 40, "#FFFFFF")
        k.mask(line, win); k.mask(txt, win)
        kids = k.mask_scene({win.id: "w"})["children"]
        self.assertEqual((kids[0]["d"], kids[1]["text"]), ("M 0 0 L 10 10", "Hi"))


@unittest.skipUnless(EXE and os.path.exists(EXE), "set CARVERCAT_EXE to a built carvercat-host to run the live tests")
class LiveTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.c = Client.stdio(EXE, self.tmp.name)
        self.addCleanup(self.c.close)

    def lower_third(self):
        s = Scene(self.c, width=1080, height=1080, fps=30, duration="4s")
        s.rectangle("plate", Box(80, 700, 820, 220), fill="#1a1c26", radius=22)
        s.text("name", "Alex Morgan", box=Box(190, 719, 620, 110), size=96, weight=700)
        s.entrance(["plate", "name"], frames=16, stagger=4)
        return s

    def objects(self):
        return self.c.tool("carvercat_list")["objects"]

    def test_dry_run_changes_nothing_then_apply_is_one_undo_step(self):
        s = self.lower_third()
        dry = s.apply(dry_run=True)
        self.assertFalse(dry["scene"]["applied"])
        self.assertEqual(self.objects(), [])
        done = s.apply()
        self.assertEqual(sorted(s.ids), ["name", "plate"])
        self.assertTrue(any(c["key"] == "borderRadius" and c["unit"] == "px" for c in done["changes"]))
        self.c.run("edit.undo")
        self.assertEqual(self.objects(), [])

    def test_refusal_lists_every_problem_and_changes_nothing(self):
        bad = {"schema": "carvercat/2.0", "children": [{"id": "a", "type": "rectangle", "style": {"colour": "red"}}, {"id": "a", "type": "rect"}]}
        with self.assertRaises(Refused):
            self.c.apply_scene(bad)
        self.assertEqual(self.objects(), [])

    def test_round_trip_and_idempotent_apply(self):
        s = self.lower_third()
        s.apply()
        doc = self.c.scene()
        self.c.apply_scene(doc)
        self.assertEqual(self.c.scene(), doc)
        again = s.apply()
        self.assertEqual([c for c in again["changes"] if not c["key"].startswith("$")], [])

    def test_path_and_null_nodes_round_trip(self):
        s = Scene(self.c, width=1920, height=1080, fps=30, duration="2s")
        s.null("pivot", 910, 150)
        s.rectangle("sign", Box(-100, 150, 300, 200), fill="#ff7a00", parent="pivot")      # measured from the null's top-left
        s.path("line", "M 200 900 L 1720 900", stroke="#00e5c3", stroke_width=12, strokeLinecap="round")
        s.keys("pivot", "rotate", [(0, 0), (30, 20)])
        s.keys("line", "trimEnd", [(0, "0%"), (30, "100%")])
        s.apply()
        doc = self.c.scene()
        kinds = {n["id"]: n["type"] for n in doc["children"]}
        self.assertEqual(kinds, {"pivot": "null", "line": "path"})
        self.assertEqual([k["id"] for k in doc["children"][0]["children"]], ["sign"])
        self.assertTrue(doc["children"][1]["d"].startswith("M 200"))
        self.c.apply_scene(doc)
        self.assertEqual(self.c.scene(), doc)

    def test_selectors_set_and_measure_in_px(self):
        self.lower_third().apply()
        self.assertEqual(len(self.c.query("text")), 1)
        self.c.set("rect, text", opacity=0.5)
        box = self.c.measure(["#name"])["objects"][0]["box"]
        self.assertAlmostEqual(box["width"], 620, places=2)
        self.assertEqual(self.c.preflight("resolve")["host"], "resolve")

    def test_preflight_says_approximate_for_soft_edge_on_after_effects(self):
        s = Scene(self.c, width=1920, height=1080, fps=30, duration="2s")
        s.ellipse("glow", Box(660, 240, 600, 600), fill="#7a5cff", alpha=0.5)
        s.soft_edge("glow", 120)
        reply, pf = s.apply(preflight="aftereffects")
        items = {i["key"]: i["status"] for o in pf["objects"] for i in o["items"]}
        self.assertEqual(items["softEdge"], "approximate")
        self.assertEqual(self.c.preflight("resolve")["summary"]["approximate"], 0)

    def test_feathered_mask_reveal(self):
        s = Scene(self.c, width=1920, height=1080, fps=30, duration="3s")
        s.rectangle("bg", Box(0, 0, 1920, 1080), fill="#101018")
        s.text("quote", "Quiet confidence", box=Box(360, 440, 1200, 200), size=120, align="center", color="#f4f1ea")
        s.rectangle("wipe", Box(360, 380, 1200, 320), fill="#ffffff")
        s.apply()
        quote, wipe = s.ids["quote"], s.ids["wipe"]
        self.c.run("property.set", id=quote, key="mask", value={"ref": wipe})
        self.c.run("property.set", id=wipe, key="feather", value=60)
        self.c.run("parent.clear", ids=[wipe, quote])
        self.c.run("anim.set", id=wipe, keyframes=[{"at": 0, "x": -1260, "ease": "ease-in-out"}, {"at": "1.5s", "x": 360}])
        keys = self.c.run("anim.get", id=wipe)["readings"][0]["keys"]
        self.assertEqual([k["value"] for k in keys["x"]], [-1260, 360])
        info = self.c.get(wipe, "softEdge")
        self.assertEqual(info["value"], 60)

    def test_cc_build_helpers(self):
        import cc_build
        cc_build.use(self.c)
        self.c.run("comp.format", width=1080, height=1080, fps=30)
        plate = cc_build.card(x=80, y=700, w=820, h=220)
        name = cc_build.text("Alex Morgan", x=190, y=719, w=620, h=110, size=96)
        plate.anim([{"at": 0, "x": -460, "ease": "cubic-bezier(.16,1,.3,1)"}, {"at": 20, "x": 80}])
        self.assertEqual(self.c.get(name.id, "fontSize")["value"], 96)
        keys = self.c.run("anim.get", id=plate.id)["readings"][0]["keys"]["x"]
        self.assertEqual([k["value"] for k in keys], [-460, 80])

    def test_component_updates_not_duplicates(self):
        for title in ("one", "two"):
            s = Scene(self.c, width=1920, height=1080, fps=30, duration="2s")
            with s.component("Header") as h:
                h.rectangle("Plate", Box(160, 70, 1600, 100))
                h.text("Brand", title, box=Box(200, 85, 900, 70), size=48)
            s.apply()
        self.assertEqual(len(self.objects()), 2)

    def test_cc2_path_null_stagger_and_text_keys_live(self):
        doc = cc2.Doc(); k = doc.comp("Rig", 60, "r")
        nul = k.null("Pivot", 960, 540)
        sign = nul.child(k.rect("Sign", 1000, 500, 300, 200, "#FF7A00"))
        nul.rot([(0, 0, "ease-out"), (30, 20, "linear")])
        k.path("Line", cc2.bezier([(200, 900), (960, 700, (-100, 0), (100, 0)), (1720, 900)]), "#00E5C3", 12).trim([(0, 0, "linear"), (30, 100, "ease-out")])
        t = k.text("Title", "HELLO WORLD", 960, 200, 120, "#FFFFFF")
        t.stagger(by="words", each=4, keyframes=[(0, {"opacity": 0}, "ease-out"), (10, {"opacity": 1}, None)])
        u = k.text("Spaced", "TRACKING", 960, 800, 100, "#FFFFFF")
        u.tracking([(0, 20, "ease-out"), (30, 0, "linear")])
        u.size([(0, 100, "ease-in"), (30, 120, "linear")])           # a second ease on the same frames: keyed after the apply
        out = Path(self.tmp.name) / "rig.carverproj"
        doc.send(self.c, str(out))
        scene = self.c.scene()
        kinds = {n["id"]: n["type"] for n in scene["children"]}
        self.assertEqual(sorted(kinds.values()), ["null", "path", "text", "text"])
        pivot = next(n for n in scene["children"] if n["type"] == "null")
        self.assertEqual([c["type"] for c in pivot["children"]], ["rect"])
        self.assertEqual(pivot["children"][0]["style"]["x"], 90)
        text = next(n for n in scene["children"] if n.get("name") == "Title")
        self.assertEqual(text["stagger"]["target"], "words")
        spaced = next(n for n in scene["children"] if n.get("name") == "Spaced")
        keys = self.c.run("anim.get", id="#" + spaced["id"])["readings"][0]["keys"]
        self.assertEqual([x["value"] for x in keys["letterSpacing"]], [20, 0])
        self.assertEqual([x["value"] for x in keys["fontSize"]], [100, 120])
        self.assertEqual(json.loads(out.read_text())["format"], "carvercat/2")

    def test_cc2_nested_comp_is_placed_as_an_instance_live(self):
        doc = cc2.Doc(); outer = doc.comp("Outer", 60, "o"); inner = doc.comp("Inner", 30, "i")
        inner.rect("Panel", 0, 0, 1920, 1080, "#5B5BF6")
        outer.rect("Bg", 0, 0, 1920, 1080, "#14151C")
        outer.nest(inner, f0=12)
        doc.send(self.c, str(Path(self.tmp.name) / "nest.carverproj"))
        comps = {c["name"]: c for c in self.c.tool("carvercat_list")["comps"]}
        self.assertIn("Inner", comps)
        self.c.run("comp.switch", comp=comps["Outer"]["index"])
        inst = [o for o in self.objects() if o["kind"] == "nestedTimeline"]
        self.assertEqual((len(inst), inst[0]["start"], inst[0]["length"]), (1, 12.0, 30.0))

    def test_cc_project_file_opens_reads_back_and_saves_as_v2(self):
        from cc_project import Project
        p = Project("Live")
        p.comp("A", width=1080, height=1920, frames=90)
        p.rectangle("Background", fill=("#1B1B4D", "#0E0E2A"))
        p.rectangle("Card", (100, 200, 400, 300), fill="#FF0000", radius=10, start=10, duration=50, track=1)
        p.ellipse("Dot", (800, 400, 200, 200), fill="#0000FF", track=2)
        path = Path(self.tmp.name) / "p.carverproj"
        p.save(path)
        self.c.run("edit.open", path=str(path), force=True)
        doc = self.c.scene()
        self.assertEqual((doc["comp"]["width"], doc["comp"]["height"], doc["comp"]["duration"]), (1080, 1920, "90f"))
        kids = {k["name"]: k for k in doc["children"]}
        self.assertEqual(kids["Background"]["style"]["fill"], "linear-gradient(180deg, #1b1b4d 0%, #0e0e2a 100%)")
        self.assertEqual((kids["Card"]["start"], kids["Card"]["duration"], kids["Card"]["style"]["borderRadius"]), ("10f", "50f", 30.0))
        self.assertEqual((kids["Dot"]["style"]["x"], kids["Dot"]["style"]["fill"]), (800, "#0000ff"))
        out = Path(self.tmp.name) / "saved.carverproj"
        self.c.run("edit.save", path=str(out))
        self.assertEqual(json.loads(out.read_text())["format"], "carvercat/2")


if __name__ == "__main__":
    unittest.main()
