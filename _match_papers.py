import json
import re
from difflib import SequenceMatcher
from pathlib import Path

root = Path(r"d:\projects\interspeech2026")
html = (root / "data" / "isca_index.html").read_text(encoding="utf-8", errors="replace")


def norm(s: str) -> str:
    s = (s or "").lower().replace("&", " and ")
    s = s.replace("–", " ").replace("—", " ").replace("−", " ")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return " ".join(s.split())


papers = []
parts = re.split(r'<h4 class="w3-center">(.*?)</h4>', html, flags=re.S)
for i in range(1, len(parts), 2):
    session = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", parts[i])).strip()
    body = parts[i + 1] if i + 1 < len(parts) else ""
    for href, block in re.findall(
        r'href="([^"]+_interspeech\.html)"[^>]*>(.*?)</a>', body, flags=re.S
    ):
        text = re.sub(r"<br\s*/?>", "\n", block, flags=re.I)
        text = re.sub(r"<[^>]+>", "", text)
        lines = [re.sub(r"\s+", " ", ln).strip() for ln in text.splitlines()]
        lines = [ln for ln in lines if ln]
        title = lines[0] if lines else ""
        authors = lines[1] if len(lines) > 1 else ""
        slug = href.replace(".html", "")
        papers.append(
            {
                "session_isca": session,
                "title": title,
                "authors": authors,
                "slug": slug,
                "pdf": f"https://www.isca-archive.org/interspeech_2026/{slug}.pdf",
                "norm": norm(title),
            }
        )

by_norm = {}
for p in papers:
    by_norm.setdefault(p["norm"], []).append(p)

sessions = json.loads((root / "data" / "sessions.json").read_text(encoding="utf-8"))
assigned = json.loads((root / "data" / "topics_assigned.json").read_text(encoding="utf-8"))
topic_of = {s["id"]: s["topic"] for s in assigned}

catalog = []
used = set()
unmatched = []
for s in sessions:
    for it in s["items"]:
        key = norm(it["title"])
        hit = None
        cands = [p for p in by_norm.get(key, []) if p["slug"] not in used]
        match = "none"
        if cands:
            hit = cands[0]
            match = "exact"
        else:
            best = None
            best_r = 0.0
            for p in papers:
                if p["slug"] in used or not key or not p["norm"]:
                    continue
                r = SequenceMatcher(None, key, p["norm"]).ratio()
                if r > best_r:
                    best_r = r
                    best = p
            if best is not None and best_r >= 0.92:
                hit = best
                match = "fuzzy"
        rec = {
            "paper_id": it.get("paper_id") or "",
            "title": it["title"],
            "presenter": it.get("presenter") or "",
            "authors": it.get("authors") or "",
            "abstract": it.get("abstract") or "",
            "session_id": s["id"],
            "session_title": s["title"],
            "day": s["day"],
            "time": s["time"],
            "format": s.get("format") or "",
            "area": s.get("area") or "",
            "program_doc": s["output_path"],
            "topic": topic_of.get(s["id"], "overview"),
            "slug": hit["slug"] if hit else "",
            "pdf": hit["pdf"] if hit else "",
            "isca_session": hit["session_isca"] if hit else "",
            "match": match,
        }
        if hit:
            used.add(hit["slug"])
        else:
            unmatched.append(rec["title"])
        catalog.append(rec)

(root / "data" / "paper_catalog.json").write_text(
    json.dumps(catalog, ensure_ascii=False), encoding="utf-8"
)
report = {
    "isca_papers": len(papers),
    "program_items": len(catalog),
    "matched": sum(1 for c in catalog if c["slug"]),
    "exact": sum(1 for c in catalog if c["match"] == "exact"),
    "fuzzy": sum(1 for c in catalog if c["match"] == "fuzzy"),
    "unmatched": len(unmatched),
    "unmatched_titles": unmatched,
    "isca_unused": len(papers) - len(used),
}
(root / "data" / "match_report.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
)
print(
    "isca", report["isca_papers"],
    "program", report["program_items"],
    "matched", report["matched"],
    "exact", report["exact"],
    "fuzzy", report["fuzzy"],
    "unmatched", report["unmatched"],
    "unused", report["isca_unused"],
)
