import json
import re
from pathlib import Path

html = Path(r"d:\projects\interspeech2026\data\isca_index.html").read_text(encoding="utf-8", errors="replace")
# links like href="barreiros26_interspeech.html">Title authors
# Try several patterns
patterns = [
    r'href="([^"]+_interspeech\.html)"[^>]*>(.*?)</a>',
    r'href="(https://www\.isca-archive\.org/interspeech_2026/[^"]+_interspeech\.html)"[^>]*>(.*?)</a>',
]
for p in patterns:
    ms = re.findall(p, html, flags=re.I | re.S)
    print("pattern", p[:40], "n", len(ms))

# show a raw slice written as ascii escapes
i = html.lower().find("barreiros26")
Path(r"d:\projects\interspeech2026\data\_slice.txt").write_text(html[i-500:i+800], encoding="utf-8")
print("slice written", i)
