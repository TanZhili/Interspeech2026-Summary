import csv
from pathlib import Path
from collections import Counter

data_dir = Path(r"d:\projects\interspeech2026\data")
for name in ["Program-Sat", "Program-Sun", "Program-Mon", "Program-Tue", "Program-Wed", "Program-Thu", "Program-Fri"]:
    p = data_dir / f"{name}.csv"
    with p.open(encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    types = Counter()
    papers = 0
    sessions = []
    current = None
    for r in rows[1:]:
        kind = (r[0] if r else "").strip()
        pid = (r[1] if len(r) > 1 else "").strip()
        title = (r[3] if len(r) > 3 else "").strip()
        types[kind] += 1
        if not pid and kind:
            current = kind
            sessions.append(kind[:120])
        elif pid:
            papers += 1
    print("\n====", name, "rows", len(rows)-1, "papers", papers, "sessionish", len(sessions))
    print("types", types.most_common(15))
    print("first sessions:")
    for s in sessions[:8]:
        print(" -", s)
