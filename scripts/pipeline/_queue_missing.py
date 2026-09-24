import json
from pathlib import Path

root = Path(r"d:\projects\interspeech2026")
cat = json.loads((root / "data" / "paper_catalog.json").read_text(encoding="utf-8"))
papers = root / "docs" / "papers"

# Known slug fixes: program title substring -> existing or new slug
fixes = {
    "Cross-Attention is Half": "papi26_interspeech",
    "BabAR": "lavechin26_interspeech",
    "Beyond Acoustic Sparsity": "geng26_interspeech",
    "Room Impulse Response Completion": "xu26p_interspeech",
    "Improving Text-to-Audio": "kuan26_interspeech",
    "Mixture of Spectral Experts": "qiu26_interspeech",
    "SA-HRTF": "zhao26f_interspeech",
    "Explicit Context-Driven Neural Acoustic": "si26_interspeech",
    "Listening with Attention": "kumar26_interspeech",
    "Structurally-Unified Tokenization": "rathore26_interspeech",
    "Eye and Mouth Cues": "xia26_interspeech",
    "WaveNorm": "ijjada26b_interspeech",
    "Geniohyoid": "myrgyyassov26_interspeech",
}

full_jobs = []
abstract_jobs = []
for i, c in enumerate(cat):
    title = c.get("title") or ""
    for key, slug in fixes.items():
        if key in title and not c.get("slug"):
            c["slug"] = slug
            c["pdf"] = f"https://www.isca-archive.org/interspeech_2026/{slug}.pdf"
            break
        if key in title and c.get("slug") in ("", None):
            c["slug"] = slug
    slug = c.get("slug") or ""
    if slug:
        sp = str(papers / (slug + ".md"))
    else:
        pid = c.get("paper_id") or ("item-" + str(i))
        sp = str(papers / ("no-pdf-" + str(pid) + ".md"))
    c["summary_path"] = sp
    p = Path(sp)
    if p.exists() and p.stat().st_size > 200:
        continue
    txt = root / "data" / "fulltext" / (slug + ".txt") if slug else None
    rec = {
        "summary_path": sp,
        "text_path": str(txt) if txt else "",
        "paper_id": c.get("paper_id") or "",
        "title": title,
        "presenter": c.get("presenter") or "",
        "authors": c.get("authors") or "",
        "session_id": c.get("session_id"),
        "session_title": c.get("session_title"),
        "day": c.get("day"),
        "time": c.get("time"),
        "topic": c.get("topic"),
        "pdf": c.get("pdf") or "",
        "abstract": c.get("abstract") or "",
    }
    if txt and txt.exists() and txt.stat().st_size > 400:
        full_jobs.append(rec)
    else:
        abstract_jobs.append(rec)

(root / "data" / "paper_catalog.json").write_text(json.dumps(cat, ensure_ascii=False), encoding="utf-8")
(root / "data" / "missing_fulltext.json").write_text(json.dumps(full_jobs, ensure_ascii=False, indent=2), encoding="utf-8")
(root / "data" / "missing_abstract.json").write_text(json.dumps(abstract_jobs, ensure_ascii=False, indent=2), encoding="utf-8")
print("full", len(full_jobs), "abstract", len(abstract_jobs))
