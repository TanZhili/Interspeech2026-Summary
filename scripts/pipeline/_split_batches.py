import json
from pathlib import Path

root = Path(r"d:\projects\interspeech2026")
sessions = json.loads((root / "data" / "sessions.json").read_text(encoding="utf-8"))
batch_dir = root / "data" / "batches"
batch_dir.mkdir(parents=True, exist_ok=True)
n = 12
size = (len(sessions) + n - 1) // n
for i in range(n):
    chunk = sessions[i * size : (i + 1) * size]
    path = batch_dir / f"batch_{i:02d}.json"
    path.write_text(json.dumps(chunk, ensure_ascii=False, indent=2), encoding="utf-8")
    print(i, len(chunk), chunk[0]["id"], "->", chunk[-1]["id"], path.stat().st_size)
