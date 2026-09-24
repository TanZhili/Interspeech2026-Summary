import json
from pathlib import Path

matched = json.loads(Path(r"d:\projects\interspeech2026\_asr_bundle.json").read_text(encoding="utf-8"))
out_dir = Path(r"d:\projects\interspeech2026\_asr_sessions")
out_dir.mkdir(exist_ok=True)
for s in matched:
    lines = []
    lines.append(f"# {s['id']} | {s['topic']} | {s['day']} | {s['time']} | {s['format']}")
    lines.append(f"TITLE: {s['title']}")
    lines.append(f"PATH: {s['output_path']}")
    lines.append(f"N: {len(s['items'])}")
    lines.append("")
    for it in s["items"]:
        lines.append("=" * 60)
        lines.append(f"ID: {it.get('paper_id', '')}")
        lines.append(f"TITLE: {it.get('title', '')}")
        lines.append(f"PRESENTER: {it.get('presenter', '')}")
        lines.append("ABSTRACT:")
        lines.append((it.get("abstract") or "").strip())
        lines.append("")
    (out_dir / f"{s['id']}.txt").write_text("\n".join(lines), encoding="utf-8")
print("wrote", len(matched), "files to", out_dir)
