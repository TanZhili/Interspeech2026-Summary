import urllib.request
from pathlib import Path
url = "https://www.isca-archive.org/interspeech_2026/index.html"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
dest = Path(r"d:\projects\interspeech2026\data\isca_index.html")
with urllib.request.urlopen(req, timeout=120) as r:
    data = r.read()
dest.write_bytes(data)
print(len(data), r.headers.get("content-type"))
