import json
from pathlib import Path
cat = json.loads(Path(r"d:\projects\interspeech2026\data\paper_catalog.json").read_text(encoding="utf-8"))
used = {c["slug"] for c in cat if c["slug"]}
# reload isca norms from catalog pdfs only; unused not in catalog
# parse match by searching html titles already in a slim file
import re
html = Path(r"d:\projects\interspeech2026\data\isca_index.html").read_text(encoding="utf-8", errors="replace")
slugs = re.findall(r'href="([^"]+_interspeech)\.html"', html)
unused = [s for s in slugs if s not in used]
Path(r"d:\projects\interspeech2026\data\unused_slugs.txt").write_text("\n".join(unused), encoding="utf-8")
print("unused", len(unused))
print("\n".join(unused))
