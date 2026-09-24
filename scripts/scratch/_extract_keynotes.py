from pathlib import Path
p = Path(r"C:\Users\bt58802469\.cursor\projects\d-projects-interspeech2026\agent-tools\234d6ec4-72cf-4ed1-9059-30b1d718d7f1.txt")
data = p.read_text(encoding="utf-8", errors="replace")
# unescape lightly
text = data.replace("\\n", "\n").replace("\\u003c", "<").replace("\\u003e", ">").replace('\\"', '"')
needles = ["John H. L. Hansen", "Steven Bird", "Jen Hay", "Junichi Yamagishi", "Know your Problem"]
for n in needles:
    i = text.find(n)
    print("\n====", n, i)
    if i >= 0:
        print(text[max(0, i-400): i+900])
