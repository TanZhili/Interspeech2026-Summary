import csv
import json
import re
from pathlib import Path

DATA = Path(r"d:\projects\interspeech2026\data")
DAYS = {
    "Program-Sun": "Sunday 27 September 2026",
    "Program-Mon": "Monday 28 September 2026",
    "Program-Tue": "Tuesday 29 September 2026",
    "Program-Wed": "Wednesday 30 September 2026",
    "Program-Thu": "Thursday 1 October 2026",
    "Program-Fri": "Friday 2 October 2026",
    "Program-Sat": "Saturday 26 September 2026",
}

SESSION_RE = re.compile(
    r"^(?:[★\u2605\s]*)?(?P<day>Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday).+?-\s*(?P<time>[0-9]{1,2}:[0-9]{2}\s*-\s*[0-9]{1,2}:[0-9]{2}|[0-9]{1,2}:[0-9]{2}-[0-9]{1,2}:[0-9]{2})\s*-\s*(?P<rest>.+)$",
    re.I,
)
FMT_RE = re.compile(
    r"^(?:(?P<idx>\d+)\s*-\s*)?(?P<fmt>Oral|Poster|Long Oral|Long - Oral|Challenge|Special Session|Show And Tell|Show and tell|Keynote speaker)\s*(?P<num>\d+)?\s*-\s*(?P<title>.+)$",
    re.I,
)


def clean(s: str) -> str:
    s = (s or "").replace("\u00a0", " ").replace("\ufeff", "")
    s = s.replace("★", "").strip()
    s = re.sub(r"\s+", " ", s)
    return s


def parse_header(text: str):
    text = clean(text)
    m = SESSION_RE.match(text)
    if not m:
        return None
    rest = m.group("rest").strip()
    area = ""
    fmt = ""
    title = rest
    m_area = re.match(r"Area\s*(?P<area>\d+)\s*-\s*(?P<rest>.+)$", rest, re.I)
    rest2 = rest
    if m_area:
        area = m_area.group("area")
        rest2 = m_area.group("rest").strip()
    m2 = FMT_RE.match(rest2)
    if m2:
        fmt = clean(m2.group("fmt"))
        title = clean(m2.group("title"))
    title = re.sub(r"\s*\[Cross-area long papers Oral session\]\s*$", "", title, flags=re.I).strip()
    title = re.sub(r"\s*\|\s*CHILDSPACE\s*$", "", title, flags=re.I).strip()
    return {
        "time": re.sub(r"\s*", "", m.group("time")),
        "area": area,
        "format": fmt,
        "title": title,
        "header": text,
    }


def slugify(text: str) -> str:
    text = text.lower()
    text = text.replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text[:70] or "session"


sessions = []
sid = 0
for fname, day in DAYS.items():
    path = DATA / f"{fname}.csv"
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    current = None
    for r in rows[1:]:
        kind = clean(r[0] if r else "")
        pid = clean(r[1] if len(r) > 1 else "")
        time = clean(r[2] if len(r) > 2 else "")
        title = clean(r[3] if len(r) > 3 else "")
        presenter = clean(r[4] if len(r) > 4 else "")
        abstract = (r[5] if len(r) > 5 else "").replace("\u00a0", " ").strip()
        authors = clean(r[6] if len(r) > 6 else "")
        meta = parse_header(kind) if kind and not pid and not title else None
        if meta:
            sid += 1
            current = {
                "id": f"{fname[-3:].lower()}-{sid:03d}",
                "day": day,
                "day_key": fname,
                **meta,
                "items": [],
            }
            sessions.append(current)
            continue
        if not current:
            # tutorials / satellite / stray
            if title or abstract:
                sid += 1
                current = {
                    "id": f"{fname[-3:].lower()}-{sid:03d}",
                    "day": day,
                    "day_key": fname,
                    "time": time,
                    "area": "",
                    "format": kind or "Other",
                    "title": kind or title[:80],
                    "header": kind,
                    "items": [],
                }
                sessions.append(current)
            else:
                continue
        if title or abstract or pid:
            current["items"].append(
                {
                    "paper_id": pid,
                    "time": time,
                    "type": kind,
                    "title": title,
                    "presenter": presenter,
                    "authors": authors,
                    "abstract": abstract,
                }
            )

# drop empty
sessions = [s for s in sessions if s["items"]]
DAY_DIR = {
    "Saturday 26 September 2026": "2026-09-26-saturday",
    "Sunday 27 September 2026": "2026-09-27-sunday",
    "Monday 28 September 2026": "2026-09-28-monday",
    "Tuesday 29 September 2026": "2026-09-29-tuesday",
    "Wednesday 30 September 2026": "2026-09-30-wednesday",
    "Thursday 1 October 2026": "2026-10-01-thursday",
    "Friday 2 October 2026": "2026-10-02-friday",
}
day_counts = {}
for s in sessions:
    day_counts[s["day"]] = day_counts.get(s["day"], 0) + 1
    n = day_counts[s["day"]]
    folder = DAY_DIR.get(s["day"], "other")
    s["output_path"] = f"docs/by-program/{folder}/{n:02d}-{s['id']}-{slugify(s['title'])}.md"

out = DATA / "sessions.json"
out.write_text(json.dumps(sessions, ensure_ascii=False, indent=2), encoding="utf-8")
print("sessions", len(sessions))
print("papers", sum(len(s["items"]) for s in sessions))
print("abstract chars", sum(len(it["abstract"]) for s in sessions for it in s["items"]))
by = {}
for s in sessions:
    by.setdefault(s["day"][:3], 0)
    by[s["day"][:3]] += 1
print("by day sessions", by)
print("sample", sessions[5]["title"], len(sessions[5]["items"]))
