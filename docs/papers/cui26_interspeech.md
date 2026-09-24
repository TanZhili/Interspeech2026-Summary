# TurnGuide: Enhancing Meaningful Full Duplex Spoken Interactions via Dynamic Turn-Level Text-Speech Interleaving

- 论文编号：1141
- 报告人：Wenqian Cui
- 程序：Wednesday 30 September 2026 / LLMs and Conversational Interaction
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/cui26_interspeech.pdf

## 问题
端到端全双工语音语言模型（FD-SLM）能学打断/重叠等自然轮次，但相对文本 LLM 语义能力下降；在双通道连续音频中插入离散文本易破坏时序对齐与交互流畅性。

## 方法
TurnGuide：动态按轮切分助手语音，在轮级联合生成文本与语音，用文本引导语义同时保持声学流。基于 GLM-4-Voice 在 Fisher 上训练；对比 dGSLM、STI/SCI、Moshi 及 Moshi-style 训练变体；GPT-4o 语义评分（无条件/条件生成，多温度）。

## 实验与结果
TurnGuide 语义分显著高于基线（Overall 约 7.27–7.79，视变体；Moshi TS 约 5.58，SCI 约 5.91）。L2:1/L3:1 损失加权变体进一步提升；作者称在多样轮次事件上达 SOTA。金标文本引导亦强，但提出方法在多项设定上更好或接近。

## 结论
轮级而非帧级文本–语音交错，可把 LLM 语义迁入全双工语音交互而不严重破坏时间对齐。

## 点评
把“文本引导”下沉到轮边界，抓住了全双工对齐痛点。评测偏 GPT 语义分与 Fisher 续写，对真实打断延迟/重叠自然度覆盖有限；多数竞品未完全开源，对比面受约束。9B 级训练成本与延迟是部署考量。
