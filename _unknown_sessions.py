import json
from pathlib import Path
sessions = json.loads(Path(r"d:\projects\interspeech2026\data\sessions.json").read_text(encoding="utf-8"))
for s in sessions:
    if not s["format"]:
        print("---", s["id"], "|", s["time"], "|", s["title"][:140], "| n", len(s["items"]))
        print("   header:", s["header"][:180])
        print("   item0:", s["items"][0]["type"][:40], "|", s["items"][0]["title"][:80])
