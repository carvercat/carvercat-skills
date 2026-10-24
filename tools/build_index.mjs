// Generates INDEX.json, INDEX.md and categories/<c>/INDEX.json from every card.json.
// `--check` writes nothing and exits 1 if a card is invalid or an index is stale.
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const check = process.argv.includes("--check");
const REQUIRED = ["schema", "id", "title", "category", "tags", "summary", "use_when",
  "canvas", "contains", "parameters", "carvercat_version", "dependencies", "license", "status", "copy_notes"];
const errors = [];
const outputs = new Map();
const catsDir = path.join(root, "categories");
const byCat = {};

for (const cat of fs.existsSync(catsDir) ? fs.readdirSync(catsDir).sort() : []) {
  const cdir = path.join(catsDir, cat);
  if (!fs.statSync(cdir).isDirectory()) continue;
  for (const slug of fs.readdirSync(cdir).sort()) {
    const pdir = path.join(cdir, slug);
    if (!fs.statSync(pdir).isDirectory()) continue;
    const rel = `categories/${cat}/${slug}`;
    const cardPath = path.join(pdir, "card.json");
    if (!fs.existsSync(cardPath)) { errors.push(`${rel}: card.json missing`); continue; }
    if (!fs.existsSync(path.join(pdir, "project.carverproj"))) errors.push(`${rel}: project.carverproj missing`);
    let card;
    try { card = JSON.parse(fs.readFileSync(cardPath, "utf8")); }
    catch (e) { errors.push(`${rel}: card.json is not valid JSON`); continue; }
    for (const k of REQUIRED) if (!(k in card)) errors.push(`${rel}: card missing "${k}"`);
    if (card.id !== `${cat}/${slug}`) errors.push(`${rel}: id "${card.id}" must equal "${cat}/${slug}"`);
    if (card.category !== cat) errors.push(`${rel}: category "${card.category}" must equal folder "${cat}"`);
    (byCat[cat] ||= []).push({
      id: card.id, title: card.title, summary: card.summary, tags: card.tags,
      status: card.status, path: rel, card: `${rel}/card.json`, project: `${rel}/project.carverproj`,
    });
  }
}

const cats = Object.keys(byCat).sort();
for (const c of cats) {
  outputs.set(`categories/${c}/INDEX.json`, JSON.stringify({ schema: 1, category: c, projects: byCat[c] }, null, 2) + "\n");
}
outputs.set("INDEX.json", JSON.stringify({
  schema: 1,
  categories: cats.map((c) => ({ category: c, index: `categories/${c}/INDEX.json`, count: byCat[c].length })),
  projects: cats.flatMap((c) => byCat[c].map((p) => ({ id: p.id, title: p.title, summary: p.summary, tags: p.tags, card: p.card }))),
}, null, 2) + "\n");
outputs.set("INDEX.md", "# Index (generated - do not edit)\n\n" + cats.map((c) =>
  `## ${c}\n\n` + byCat[c].map((p) => `- [${p.title}](${p.path}/card.json) - ${p.summary}`).join("\n")).join("\n\n") + "\n");

for (const [rel, text] of outputs) {
  const file = path.join(root, rel);
  const have = fs.existsSync(file) ? fs.readFileSync(file, "utf8") : null;
  if (have !== text) {
    if (check) errors.push(`${rel}: stale or missing (run node tools/build_index.mjs)`);
    else fs.writeFileSync(file, text);
  }
}
if (errors.length) { console.error(errors.join("\n")); process.exit(1); }
console.log(check ? "index ok" : `indexed ${cats.reduce((n, c) => n + byCat[c].length, 0)} project(s)`);
