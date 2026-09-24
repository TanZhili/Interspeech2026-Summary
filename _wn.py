import json
from pathlib import Path
cat = json.loads(Path(r"d:\projects\interspeech2026\data\paper_catalog.json").read_text(encoding="utf-8"))
for c in cat:
    if "WaveNorm" in (c.get("title") or "") or c.get("slug") == "ijjada26b_interspeech":
        print(c["session_id"], c.get("paper_id"), c.get("slug"), c["title"][:90])
