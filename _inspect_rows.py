import csv
from pathlib import Path

p = Path(r"d:\projects\interspeech2026\data\Program-Mon.csv")
with p.open(encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f))

# print rows where paper id empty
n = 0
for i, r in enumerate(rows):
    pid = (r[1] if len(r) > 1 else "").strip()
    if not pid:
        n += 1
        cells = [c.replace("\n", " ")[:140] for c in r[:8]]
        print(f"\nROW {i}")
        for j, c in enumerate(cells):
            if c.strip():
                print(j, c)
print("\nempty pid rows", n)
