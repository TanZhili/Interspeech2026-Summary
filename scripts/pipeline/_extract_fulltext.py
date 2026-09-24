"""Download Interspeech 2026 PDFs and save extracted body text."""
import io
import json
import time
import traceback
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(r"d:\projects\interspeech2026")
CAT = json.loads((ROOT / "data" / "paper_catalog.json").read_text(encoding="utf-8"))
OUT = ROOT / "data" / "fulltext"
OUT.mkdir(parents=True, exist_ok=True)
LOG = ROOT / "data" / "extract_log.jsonl"
WORKERS = 8


def body_text(raw: str) -> str:
    cut = None
    for marker in ("\nReferences\n", "\nREFERENCES\n", "\n8. References", "\n7. References", "\n6. References"):
        i = raw.rfind(marker)
        if i > len(raw) * 0.45:
            cut = i
            break
    text = raw if cut is None else raw[:cut]
    text = text.strip()
    if len(text) > 24000:
        text = text[:24000]
    return text


def one(rec: dict) -> str:
    slug = rec["slug"]
    dest = OUT / f"{slug}.txt"
    if dest.exists() and dest.stat().st_size > 800:
        return "skip"
    url = rec["pdf"]
    last_err = ""
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
            reader = PdfReader(io.BytesIO(data))
            raw = "\n".join((p.extract_text() or "") for p in reader.pages)
            text = body_text(raw)
            if len(text) < 400:
                raise RuntimeError(f"short text {len(text)}")
            dest.write_text(text, encoding="utf-8")
            return "ok"
        except Exception as e:
            last_err = f"{type(e).__name__}: {e}"
            time.sleep(1.5 * (attempt + 1))
    (OUT / f"{slug}.err").write_text(last_err, encoding="utf-8")
    return "err"


def main():
    jobs = [c for c in CAT if c.get("slug")]
    # unique slugs
    seen = set()
    uniq = []
    for c in jobs:
        if c["slug"] in seen:
            continue
        seen.add(c["slug"])
        uniq.append(c)
    print("jobs", len(uniq), flush=True)
    ok = skip = err = 0
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(one, rec): rec["slug"] for rec in uniq}
        done = 0
        for fut in as_completed(futs):
            slug = futs[fut]
            done += 1
            try:
                status = fut.result()
            except Exception:
                status = "err"
                (OUT / f"{slug}.err").write_text(traceback.format_exc(), encoding="utf-8")
            if status == "ok":
                ok += 1
            elif status == "skip":
                skip += 1
            else:
                err += 1
            if done % 25 == 0 or done == len(uniq):
                line = f"{done}/{len(uniq)} ok={ok} skip={skip} err={err}\n"
                print(line, end="", flush=True)
                with LOG.open("a", encoding="utf-8") as f:
                    f.write(json.dumps({"done": done, "ok": ok, "skip": skip, "err": err}) + "\n")
    print("finished", ok, skip, err, flush=True)


if __name__ == "__main__":
    main()
