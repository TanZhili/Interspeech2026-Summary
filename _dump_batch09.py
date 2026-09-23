import json
from pathlib import Path

root = Path(r"d:\projects\interspeech2026")
data = json.loads((root / "data/batches/batch_09.json").read_text(encoding="utf-8"))
out = root / "_batch09_sessions"
out.mkdir(exist_ok=True)
print(f"sessions={len(data)}")
for i, s in enumerate(data):
    path = out / f"session_{i:02d}.json"
    path.write_text(json.dumps(s, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{i:02d}\t{s['id']}\tn={len(s['items'])}\t{s['output_path']}")
