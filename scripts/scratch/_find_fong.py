import json
from pathlib import Path
cat = json.loads(Path(r"d:\projects\interspeech2026\data\paper_catalog.json").read_text(encoding="utf-8"))
for c in cat:
    if c.get("slug") == "fong26_interspeech":
        Path(r"d:\projects\interspeech2026\data\_fong26.json").write_text(
            json.dumps(c, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print("found", c.get("session_id"), c.get("topic"), c.get("program_doc"))
