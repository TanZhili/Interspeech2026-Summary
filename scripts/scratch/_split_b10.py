import json
from pathlib import Path

p = Path(r"d:\projects\interspeech2026\data\batches\batch_10.json")
data = json.loads(p.read_text(encoding="utf-8"))
out = Path(r"d:\projects\interspeech2026\_batch10_sessions")
out.mkdir(exist_ok=True)
print("sessions", len(data))
total = 0
for i, s in enumerate(data):
    items = s.get("items", [])
    total += len(items)
    empty = 0
    for it in items:
        a = (it.get("abstract") or "").strip()
        if not a or "no abstract" in a.lower() or "does not include" in a.lower():
            empty += 1
    sid = s["id"]
    path = s["output_path"]
    print(f"{i:02d} {sid} papers={len(items)} emptyish={empty} path={path}")
    (out / f"session_{i:02d}.json").write_text(
        json.dumps(s, ensure_ascii=False, indent=2), encoding="utf-8"
    )
print("total_items", total)
