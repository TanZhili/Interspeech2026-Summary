import csv
from pathlib import Path
for name in ["Program-Mon", "Program-Tue", "Program-Wed", "Program-Thu"]:
    p = Path(r"d:\projects\interspeech2026\data") / f"{name}.csv"
    with p.open(encoding="utf-8", newline="") as f:
        header = next(csv.reader(f))
    print("\n====", name)
    print(header[0][:500])
    print("--- title col ---")
    print(header[3][:300] if len(header) > 3 else "")
