import urllib.request
url = "https://www.isca-archive.org/interspeech_2026/barreiros26_interspeech.pdf"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD")
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print(r.status, r.headers.get("content-type"), r.headers.get("content-length"), r.geturl())
except Exception as e:
    print(type(e), e)
    if hasattr(e, "code"):
        print("code", e.code)
        print(e.headers)
