import urllib.parse
import urllib.request
from pathlib import Path

out = Path(r"d:\projects\interspeech2026\data")
out.mkdir(parents=True, exist_ok=True)
sheets = ["Program-Sat", "Program-Sun", "Program-Mon", "Program-Tue", "Program-Wed", "Program-Thu", "Program-Fri"]
base = "https://docs.google.com/spreadsheets/d/1R5fXMZr55X2CyN8Ehn7feLAVR4Zrz_djhQmrPelXxis/gviz/tq?tqx=out:csv&sheet="

for name in sheets:
    url = base + urllib.parse.quote(name)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    dest = out / f"{name}.csv"
    print("fetch", name)
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    dest.write_bytes(data)
    print(name, len(data))
