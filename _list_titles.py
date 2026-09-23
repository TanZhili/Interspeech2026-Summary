import json
from pathlib import Path
sessions = json.loads(Path(r"d:\projects\interspeech2026\data\sessions.json").read_text(encoding="utf-8"))
for s in sessions:
    print(f"{s['id']}\t{len(s['items'])}\t{s['format']}\t{s['title']}")
