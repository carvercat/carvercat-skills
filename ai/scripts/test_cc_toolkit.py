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
