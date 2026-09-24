import urllib.request
url = "https://docs.google.com/spreadsheets/d/1R5fXMZr55X2CyN8Ehn7feLAVR4Zrz_djhQmrPelXxis/gviz/tq?tqx=out:csv&sheet=Program-Mon"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read(500)
        print("status", r.status, "lenhint", r.headers.get("content-length"))
        print(data[:400])
except Exception as e:
    if hasattr(e, "read"):
        body = e.read()[:800]
        print(type(e), e)
        print(body)
    else:
        print(type(e), e)
