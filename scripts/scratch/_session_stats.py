import json
from pathlib import Path
from collections import Counter

sessions = json.loads(Path(r"d:\projects\interspeech2026\data\sessions.json").read_text(encoding="utf-8"))
print("n", len(sessions))
sizes = Counter(len(s["items"]) for s in sessions)
print("size hist", sorted(sizes.items()))
print("--- small ---")
for s in sessions:
    if len(s["items"]) <= 2:
        print(s["id"], s["day"][:3], s["format"], s["title"][:80], "n", len(s["items"]), "abs", sum(len(i["abstract"]) for i in s["items"]))
print("--- formats ---")
print(Counter(s["format"] or "?" for s in sessions))
print("--- missing abs ---")
miss = 0
for s in sessions:
    for it in s["items"]:
        if len(it["abstract"]) < 40:
            miss += 1
print("short abstracts", miss)
