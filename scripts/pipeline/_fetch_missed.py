import io
import re
import urllib.request
from pathlib import Path
from pypdf import PdfReader

root = Path(r"d:\projects\interspeech2026")
html = (root / "data" / "isca_index.html").read_text(encoding="utf-8", errors="replace")
needles = [
    "Cross-Attention is Half",
    "BabAR",
    "Beyond Acoustic Sparsity",
    "Room Impulse Response Completion",
    "Improving Text-to-Audio",
    "Sorting Clusters",
]
extra = ["xia26_interspeech", "ijjada26b_interspeech", "myrgyyassov26_interspeech"]
found = []
for n in needles:
    i = html.find(n)
    if i < 0:
        continue
    window = html[max(0, i - 800): i]
    hrefs = re.findall(r'href="([^"]+_interspeech)\.html"', window)
    slug = hrefs[-1] if hrefs else ""
    found.append((n, slug))

for slug in extra:
    found.append((slug, slug))

out = root / "data" / "fulltext"
lines = []

def clean(s):
    return s.encode("utf-8", errors="replace").decode("utf-8")

for name, slug in found:
    if not slug:
        lines.append("NO SLUG " + name)
        continue
    dest = out / (slug + ".txt")
    if dest.exists() and dest.stat().st_size > 800:
        lines.append("HAVE " + slug)
        continue
    url = f"https://www.isca-archive.org/interspeech_2026/{slug}.pdf"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=90) as r:
            data = r.read()
        reader = PdfReader(io.BytesIO(data))
        raw = "\n".join((p.extract_text() or "") for p in reader.pages)
        text = clean(raw).strip()
        if len(text) > 24000:
            text = text[:24000]
        dest.write_text(text, encoding="utf-8")
        lines.append(f"OK {slug} {len(text)} {name}")
    except Exception as e:
        lines.append(f"ERR {slug} {type(e).__name__} {e}")

(root / "data" / "rematch_log.txt").write_text("\n".join(lines), encoding="utf-8")
print("\n".join(lines))
