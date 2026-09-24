import json
from pathlib import Path

root = Path(r"d:\projects\interspeech2026")
cat = json.loads((root / "data" / "paper_catalog.json").read_text(encoding="utf-8"))
papers = root / "docs" / "papers"
missing = []
have = 0
for i, c in enumerate(cat):
    sp = c.get("summary_path") or ""
    if not sp:
        if c.get("slug"):
            sp = str(papers / (c["slug"] + ".md"))
        else:
            pid = c.get("paper_id") or ("item-" + str(i))
            sp = str(papers / ("no-pdf-" + pid + ".md"))
    p = Path(sp)
    if p.exists() and p.stat().st_size > 200:
        have += 1
    else:
        missing.append((c.get("session_id"), c.get("paper_id"), c.get("slug"), (c.get("title") or "")[:80]))
print("catalog", len(cat), "have", have, "missing", len(missing))
for row in missing:
    print(" | ".join(str(x) for x in row))
