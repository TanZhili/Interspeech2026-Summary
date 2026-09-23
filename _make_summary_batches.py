"""Group extracted full texts into summarizer batches."""
import json
from pathlib import Path

root = Path(r"d:\projects\interspeech2026")
cat = json.loads((root / "data" / "paper_catalog.json").read_text(encoding="utf-8"))
full = root / "data" / "fulltext"
papers_dir = root / "docs" / "papers"
papers_dir.mkdir(parents=True, exist_ok=True)

items = []
for i, c in enumerate(cat):
    slug = c.get("slug") or ""
    if slug:
        text_path = full / f"{slug}.txt"
        summary_path = papers_dir / f"{slug}.md"
    else:
        pid = c.get("paper_id") or f"item-{i}"
        text_path = None
        summary_path = papers_dir / f"no-pdf-{pid}.md"
    c["summary_path"] = str(summary_path).replace("\\", "/")
    c["text_path"] = str(text_path).replace("\\", "/") if text_path else ""
    c["has_text"] = bool(text_path and text_path.exists() and text_path.stat().st_size > 800)
    items.append(c)

(root / "data" / "paper_catalog.json").write_text(
    json.dumps(items, ensure_ascii=False), encoding="utf-8"
)

ready = [c for c in items if c["has_text"] and not Path(c["summary_path"]).exists()]
batch_size = 8
batch_dir = root / "data" / "summary_batches"
batch_dir.mkdir(parents=True, exist_ok=True)
# clear old batch files
for p in batch_dir.glob("sum_*.json"):
    p.unlink()
n = 0
for i in range(0, len(ready), batch_size):
    chunk = []
    for c in ready[i : i + batch_size]:
        chunk.append({
            "summary_path": c["summary_path"],
            "text_path": c["text_path"],
            "paper_id": c["paper_id"],
            "title": c["title"],
            "presenter": c["presenter"],
            "authors": c["authors"],
            "session_id": c["session_id"],
            "session_title": c["session_title"],
            "day": c["day"],
            "time": c["time"],
            "topic": c["topic"],
            "pdf": c["pdf"],
        })
    path = batch_dir / f"sum_{n:03d}.json"
    path.write_text(json.dumps(chunk, ensure_ascii=False), encoding="utf-8")
    n += 1
print("ready", len(ready), "batches", n, "already", sum(1 for c in items if Path(c["summary_path"]).exists()))
