import json, os
os.makedirs(r"d:\projects\interspeech2026\_work", exist_ok=True)
data = json.load(open(r"d:\projects\interspeech2026\data\batches\batch_05.json", encoding="utf-8"))
print("sessions", len(data))
total = 0
for i, s in enumerate(data):
    items = s["items"]
    papers = [p for p in items if p.get("paper_id")]
    total += len(papers)
    print(f"{i:02d} {s['id']} area={s['area']} {s['format']} items={len(items)} papers={len(papers)}")
    print(f"   {s['title']}")
    print(f"   -> {s['output_path']}")
    with open(rf"d:\projects\interspeech2026\_work\s{i:02d}.json", "w", encoding="utf-8") as f:
        json.dump(s, f, ensure_ascii=False, indent=2)
print("total papers with id", total)
# also compact index
with open(r"d:\projects\interspeech2026\_work\index.txt", "w", encoding="utf-8") as f:
    for i, s in enumerate(data):
        f.write(f"=== {i} {s['id']} ===\n")
        f.write(f"title: {s['title']}\n")
        f.write(f"day: {s['day']}\n")
        f.write(f"time: {s['time']}\n")
        f.write(f"format: {s['format']}\n")
        f.write(f"area: {s['area']}\n")
        f.write(f"header: {s['header']}\n")
        f.write(f"output: {s['output_path']}\n")
        for p in s["items"]:
            f.write(f"\n[{p.get('paper_id') or 'NOID'}] ({p.get('type')}) {p.get('time')}\n")
            f.write(f"title: {p.get('title')}\n")
            f.write(f"presenter: {p.get('presenter')}\n")
            f.write(f"authors: {p.get('authors')}\n")
            abs_ = (p.get("abstract") or "").strip()
            f.write(f"abstract: {abs_[:800]}\n")
        f.write("\n\n")
print("wrote index")
