import json
from collections import Counter
from pathlib import Path

data = json.loads(Path(r"d:\projects\interspeech2026\data\topics_assigned.json").read_text(encoding="utf-8"))
topics = {"asr", "asr-multitalker", "asr-decoding", "retrieval", "translation"}
matched = [s for s in data if s.get("topic") in topics]
print("sessions:", len(matched))
print("by topic:", dict(Counter(s["topic"] for s in matched)))
n_papers = sum(len(s.get("items") or []) for s in matched)
print("papers:", n_papers)
empty = sum(1 for s in matched for it in s.get("items") or [] if not (it.get("abstract") or "").strip())
print("empty abstracts:", empty)

out = Path(r"d:\projects\interspeech2026\_asr_bundle.json")
out.write_text(json.dumps(matched, ensure_ascii=False, indent=2), encoding="utf-8")
print("wrote", out)

# also compact index
for s in matched:
    print(
        "|".join(
            [
                s["id"],
                s["topic"],
                s["day"],
                s["time"],
                s["format"],
                s["title"],
                str(len(s.get("items") or [])),
                s["output_path"],
            ]
        )
    )
