import io
import urllib.request
from pypdf import PdfReader
from pathlib import Path

url = "https://www.isca-archive.org/interspeech_2026/barreiros26_interspeech.pdf"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=60) as r:
    data = r.read()
print("bytes", len(data))
reader = PdfReader(io.BytesIO(data))
print("pages", len(reader.pages))
text = "\n".join((p.extract_text() or "") for p in reader.pages)
out = Path(r"d:\projects\interspeech2026\data\_sample_fulltext.txt")
out.write_text(text, encoding="utf-8")
print("chars", len(text))
print("head", text[:400].encode("unicode_escape").decode())
