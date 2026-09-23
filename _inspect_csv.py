import csv
from pathlib import Path

p = Path(r"d:\projects\interspeech2026\data\Program-Mon.csv")
with p.open(encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f))
print("nrows", len(rows))
print("ncols", max(len(r) for r in rows))
print("--- header ---")
print(rows[0])
print("--- row1 ---")
print(rows[1][:12])
print("--- row2 ---")
print([c[:80] for c in rows[2][:12]])
print("--- nonempty counts ---")
for i, h in enumerate(rows[0]):
    n = sum(1 for r in rows[1:] if i < len(r) and r[i].strip())
    print(i, n, repr(h)[:80])
