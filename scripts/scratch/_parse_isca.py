import re
from collections import Counter
from pathlib import Path

p = Path(r"C:\Users\bt58802469\.cursor\projects\d-projects-interspeech2026\uploads\index-1.html")
data = p.read_text(encoding="utf-8")
print("len", len(data), "lines", data.count("\n"))
hrefs = set(re.findall(r'href="([^"]+)"', data))
print("hrefs", len(hrefs))
for h in sorted(hrefs)[:80]:
    print(h[:250])
