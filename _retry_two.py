import io
import urllib.request
from pathlib import Path
from pypdf import PdfReader

out = Path(r"d:\projects\interspeech2026\data\fulltext")
slugs = ["qiu26_interspeech", "zhao26f_interspeech"]

def clean(s: str) -> str:
    return s.encode("utf-8", errors="replace").decode("utf-8")

for slug in slugs:
    url = f"https://www.isca-archive.org/interspeech_2026/{slug}.pdf"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=90) as r:
        data = r.read()
    reader = PdfReader(io.BytesIO(data))
    raw = "\n".join((p.extract_text() or "") for p in reader.pages)
    text = clean(raw).strip()
    cut = None
    for marker in ("\nReferences\n", "\nREFERENCES\n"):
        i = text.rfind(marker)
        if i > len(text) * 0.45:
            cut = i
            break
    if cut:
        text = text[:cut].strip()
    if len(text) > 24000:
        text = text[:24000]
    dest = out / f"{slug}.txt"
    dest.write_text(text, encoding="utf-8")
    err = out / f"{slug}.err"
    if err.exists():
        err.unlink()
    print(slug, len(text))
