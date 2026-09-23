import re
from pathlib import Path
html = Path(r"d:\projects\interspeech2026\data\isca_index.html").read_text(encoding="utf-8", errors="replace")
print("len", len(html))
# sample around a paper link
i = html.find("barreiros26")
print(html[i-400:i+500])
print("--- count html ---", html.count("_interspeech.html"))
print("--- count pdf ---", html.count(".pdf"))
