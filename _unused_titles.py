import re
from pathlib import Path
html = Path(r"d:\projects\interspeech2026\data\isca_index.html").read_text(encoding="utf-8", errors="replace")
want = ["chuprina26", "xia26_interspeech", "ijjada26b", "myrgyyassov26"]
lines = []
for slug in want:
    i = html.find(slug)
    lines.append("==== " + slug + " " + str(i))
    if i >= 0:
        chunk = html[max(0, i - 400): i + 200]
        text = re.sub(r"<[^>]+>", " ", chunk)
        text = re.sub(r"\s+", " ", text)
        lines.append(text[:500])
Path(r"d:\projects\interspeech2026\data\unused_titles.txt").write_text("\n".join(lines), encoding="utf-8")
print("ok")
