import json
from pathlib import Path

root = Path(r"d:\projects\interspeech2026")
data = json.loads((root / "data/batches/batch_11.json").read_text(encoding="utf-8"))
paths = []
total_items = 0
missing = []
for s in data:
    p = root / s["output_path"]
    paths.append(str(p))
    n = len(s["items"])
    total_items += n
    if not p.exists():
        missing.append(s["output_path"])
        continue
    text = p.read_text(encoding="utf-8")
    # check each paper id or title fragment appears in 覆盖核对
    for it in s["items"]:
        pid = (it.get("paper_id") or "").strip()
        title = it["title"]
        # for empty id items, check a distinctive title substring
        key = pid if pid else title[:40]
        if key not in text:
            missing.append(f"{s['id']}: missing coverage for {key}")

print("sessions", len(data))
print("items", total_items)
print("files_exist", sum(1 for s in data if (root / s["output_path"]).exists()))
print("issues", len(missing))
for m in missing[:20]:
    print(" ", m)
for p in paths:
    print(p)
