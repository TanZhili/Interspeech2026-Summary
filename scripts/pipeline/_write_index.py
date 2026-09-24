import json
from pathlib import Path
from collections import defaultdict

root = Path(r"d:\projects\interspeech2026")
sessions = json.loads((root / "data" / "sessions.json").read_text(encoding="utf-8"))

day_order = []
by_day = defaultdict(list)
for s in sessions:
    if s["day"] not in by_day:
        day_order.append(s["day"])
    by_day[s["day"]].append(s)

lines = []
lines.append("# Interspeech 2026 技术总结")
lines.append("")
lines.append("会议：Interspeech 2026，悉尼，2026-09-27 至 2026-10-01。")
lines.append("")
lines.append("材料来自两处：")
lines.append("")
lines.append("- 官方日程与每篇论文摘要：[Program](https://interspeech2026.org/en-AU/pages/program/program)")
lines.append("- ISCA 归档按会场列出的论文：[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)")
lines.append("")
lines.append("每篇录用论文在官方程序中都有摘要，摘要写的是问题、方法与主要结论。下面的会场文档按这个摘要逐篇写技术内容，并在会场内做趋势归纳。ISCA 上的全文 PDF 可从论文页进入（约一千五百篇）。本套笔记没有把每一篇 PDF 的方法节再展开一遍；数字和模型名只保留摘要里写明的内容。")
lines.append("")
lines.append(f"共 {len(sessions)} 个 section，{sum(len(s['items']) for s in sessions)} 条报告（含 tutorial、keynote、show & tell）。")
lines.append("")
lines.append("## 按技术方向")
lines.append("")
lines.append("这些文档把不同天的同类会场合在一起。")
lines.append("")
topics = [
    ("01-ASR.md", "语音识别：鲁棒与高效、多语与低资源、多说话人、解码与检索、语音翻译"),
    ("02-TTS.md", "语音合成、声音转换、歌唱与音频生成"),
    ("03-全双工与口语对话.md", "全双工、轮替、口语对话与口语理解"),
    ("04-语音与音频大模型.md", "音频推理、语音大模型、自监督表示与基础模型后训练"),
    ("05-语音增强分离与编解码.md", "增强、分离、目标说话人提取、神经编解码"),
    ("06-说话人与深度伪造.md", "说话人识别、日志、隐私匿名化、反欺骗与水印"),
    ("07-情感与副语言.md", "语音情感、副语言、跨语言副语言"),
    ("08-医疗与临床语音.md", "临床表征、病理语音、辅助技术、儿童与医疗对话"),
    ("09-语音学与感知产生.md", "语音学、韵律、声调、发音、感知与脑机制"),
    ("10-多模态空间与声学事件.md", "音视频、空间音频、声学事件检测"),
    ("11-多语社区数据与评测.md", "多语与社区语言、数据、评测、可信与可解释"),
]
lines.append("| 文档 | 内容 |")
lines.append("| --- | --- |")
for fn, desc in topics:
    lines.append(f"| [by-topic/{fn}](by-topic/{fn}) | {desc} |")
lines.append("")
lines.append("## 按日期与 section")
lines.append("")
for day in day_order:
    lines.append(f"### {day}")
    lines.append("")
    for s in by_day[day]:
        rel = s["output_path"].split("docs/", 1)[-1]
        area = f", Area {s['area']}" if s.get("area") else ""
        fmt = s.get("format") or "Session"
        lines.append(f"- [{s['title']}]({rel}) — {s['time']} {fmt}{area}，{len(s['items'])} 篇")
    lines.append("")

(root / "docs" / "README.md").write_text("\n".join(lines), encoding="utf-8")
print("index lines", len(lines))
