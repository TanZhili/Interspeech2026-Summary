"""Assemble program and topic documents from per-paper summaries.

A program or topic file is written only when every item assigned to it
already has a summary file, so partial runs do not publish an incomplete set.
"""
import json
from pathlib import Path

root = Path(r"d:\projects\interspeech2026")
cat = json.loads((root / "data" / "paper_catalog.json").read_text(encoding="utf-8"))
topics = json.loads((root / "data" / "topic_docs.json").read_text(encoding="utf-8"))
sessions = json.loads((root / "data" / "sessions.json").read_text(encoding="utf-8"))

# refresh summary paths if missing
papers_dir = root / "docs" / "papers"
for i, c in enumerate(cat):
    if not c.get("summary_path"):
        if c.get("slug"):
            c["summary_path"] = str(papers_dir / f"{c['slug']}.md")
        else:
            pid = c.get("paper_id") or f"item-{i}"
            c["summary_path"] = str(papers_dir / f"no-pdf-{pid}.md")

by_session = {}
for c in cat:
    by_session.setdefault(c["session_id"], []).append(c)

topic_of_key = {}
for doc_key, meta in topics.items():
    for t in meta["topics"]:
        topic_of_key[t] = doc_key

by_doc = {k: [] for k in topics}
for c in cat:
    doc = topic_of_key.get(c.get("topic") or "overview", "11-多语社区数据与评测")
    by_doc[doc].append(c)


def ready(items):
    missing = []
    for c in items:
        p = Path(c["summary_path"])
        if not p.exists() or p.stat().st_size < 200:
            missing.append(c["title"])
    return missing


def load_summary(c):
    return Path(c["summary_path"]).read_text(encoding="utf-8").strip()


def trend_path(kind, key, existing_file=None):
    p = root / "docs" / "trends" / kind / f"{key}.md"
    if p.exists() and p.stat().st_size > 80:
        return p.read_text(encoding="utf-8").strip()
    if existing_file and existing_file.exists():
        text = existing_file.read_text(encoding="utf-8", errors="replace")
        start = text.find("## 技术趋势")
        if start >= 0:
            rest = text[start + len("## 技术趋势") :]
            nxt = rest.find("\n## ")
            body = rest[:nxt].strip() if nxt >= 0 else rest.strip()
            if len(body) > 80 and "将在该组论文总结齐备后写入" not in body:
                return body
    return "技术趋势与评论将在该组论文总结齐备后写入。"


wrote_p = wrote_t = 0
for s in sessions:
    items = by_session.get(s["id"], [])
    if not items or ready(items):
        continue
    out = root / s["output_path"]
    parts = [
        f"# {s['title']}",
        "",
        f"- 日期：{s['day']}",
        f"- 时间：{s['time']}",
        f"- 形式：{s.get('format') or ''}",
        f"- Area：{s.get('area') or ''}",
        f"- 论文数：{len(items)}",
        "",
        "## 技术趋势与评论",
        "",
        trend_path("program", s["id"], out),
        "",
        "## 论文技术总结",
        "",
    ]
    seen = set()
    for c in items:
        sp = str(Path(c["summary_path"]).resolve())
        if sp in seen:
            continue
        seen.add(sp)
        parts.append(load_summary(c))
        parts.append("\n")
    out = root / s["output_path"]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(parts), encoding="utf-8")
    wrote_p += 1

for doc_key, meta in topics.items():
    items = by_doc[doc_key]
    if not items or ready(items):
        continue
    parts = [
        f"# {meta['title']}",
        "",
        f"- 论文数：{len(items)}",
        "- 规则：每篇论文至少进入一个技术分类；这里收录该分类下的全部单篇总结。",
        "",
        "## 技术趋势与评论",
        "",
        trend_path("topic", doc_key),
        "",
        "## 论文技术总结",
        "",
    ]
    seen = set()
    for c in items:
        sp = str(Path(c["summary_path"]).resolve())
        if sp in seen:
            continue
        seen.add(sp)
        parts.append(load_summary(c))
        parts.append("\n")
    out = root / "docs" / "by-topic" / f"{doc_key}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(parts), encoding="utf-8")
    wrote_t += 1

n_sum = sum(1 for c in cat if Path(c["summary_path"]).exists())
print("summaries", n_sum, "/", len(cat), "programs_written", wrote_p, "topics_written", wrote_t)
