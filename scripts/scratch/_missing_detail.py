import json
import re
from pathlib import Path

root = Path(r"d:\projects\interspeech2026")
cat = json.loads((root / "data" / "paper_catalog.json").read_text(encoding="utf-8"))
papers = root / "docs" / "papers"
full = root / "data" / "fulltext"
html = (root / "data" / "isca_index.html").read_text(encoding="utf-8", errors="replace")

used = {c.get("slug") for c in cat if c.get("slug")}
slugs = re.findall(r'href="([^"]+_interspeech)\.html"', html)
unused = [s for s in slugs if s not in used]

lines = []
lines.append("unused slugs: " + ", ".join(unused))
for i, c in enumerate(cat):
    sp = c.get("summary_path") or ""
    if not sp:
        if c.get("slug"):
            sp = str(papers / (c["slug"] + ".md"))
        else:
            pid = c.get("paper_id") or ("item-" + str(i))
            sp = str(papers / ("no-pdf-" + str(pid) + ".md"))
    p = Path(sp)
    if p.exists() and p.stat().st_size > 200:
        continue
    txt = ""
    if c.get("slug"):
        t = full / (c["slug"] + ".txt")
        txt = "TXT" if t.exists() and t.stat().st_size > 400 else "no-txt"
    else:
        txt = "no-slug"
    abs_len = len(c.get("abstract") or "")
    lines.append(f"{txt}\tabs={abs_len}\t{c.get('session_id')}\t{c.get('paper_id')}\t{c.get('slug')}\t{(c.get('title') or '')[:100]}")

(root / "data" / "missing_summaries.txt").write_text("\n".join(lines), encoding="utf-8")
print("lines", len(lines))
