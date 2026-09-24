from pathlib import Path
html = Path(r"d:\projects\interspeech2026\data\isca_index.html").read_text(encoding="utf-8", errors="replace")
needles = [
    "Cross-Attention is Half",
    "BabAR",
    "Confusion-Transport",
    "Beyond Acoustic Sparsity",
    "Room Impulse Response Completion",
    "Mitigating Pruning",
    "Improving Text-to-Audio",
    "Factorization and Latent",
    "One Embedding",
    "Expressive Speech Translation",
    "Benchmarking Adult Addressee",
    "Sorting Clusters",
]
lines = []
for n in needles:
    i = html.find(n)
    lines.append(f"{n}\t{i}")
Path(r"d:\projects\interspeech2026\data\needle_hits.txt").write_text("\n".join(lines), encoding="utf-8")
print("ok")
