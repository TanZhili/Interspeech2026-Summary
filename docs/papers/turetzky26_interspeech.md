# Knowing What to Stress: A Discourse-Conditioned Text-to-Speech Benchmark

- 论文编号：2743
- 报告人：Avihu Dekel
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/turetzky26_interspeech.pdf

## 问题

同一句子因语篇语境不同需强调不同词（对比焦点），现代 TTS 虽能显式控重音，但能否仅从语境推断并实现恰当词级重音尚不清楚；缺对比控制基准。

## 方法

提出 CAST：对比语境对——相同目标句 + 两种语境，语义上要求不同重音词。用结构化提示生成并由多模型裁判过滤；113 对（226 项），位置与语用类型均衡。评测系统在无语境 / 拼接语境 / 指令语境 / 显式重音下合成，用 WHISTRESS 检测重音，报告 Hit、Pair-Contrast、Pair-Correct。另释放大约 10k 合成训练资源。

## 实验与结果

各系统 Pair-Correct 接近 0；提供语境（拼接或指令）相对无语境无明显提升。显式重音上界更高（如 CosyVoice3 Pair-Contrast 40.3、Pair-Correct 10.6），但仍不可靠。人类校验：标签多数一致率高；检测器与人一致程度落在听者间一致性范围内。文中亦报告文本 LM 能较好从语境恢复目标重音，而 TTS 难落地到声学。

## 结论

作者认为当前 TTS 普遍不能可靠做语篇条件重音；实现能力（显式）与推理能力（语境）之间存在鸿沟。CAST 与流水线开源以推动语境感知韵律。

## 点评

用“同句异境”设计干净隔离语境效应，Pair-Correct 严格卡死句内偏置。结论对下一代对话 TTS 很刺耳但证据清楚。自动检测器 κ 不高反映突显感知本身主观；基准规模中等，扩展合成语料可支撑训练但评测需防污染。
