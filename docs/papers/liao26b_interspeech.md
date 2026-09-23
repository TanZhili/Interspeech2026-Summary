# High-Precision Prosodic Boundary Anchors from Acoustic Cues under Weak Supervision

- 论文编号：209
- 报告人：Hanyu Liao
- 程序：Monday 28 September 2026 / Tools and Techniques for Phonetic Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/liao26b_interspeech.pdf

## 问题
韵律边界检测多依赖 ToBI 等人工标注，成本高且许多语料缺失。虽有停顿、音高重置、能量变化等声学相关，如何在无人工边界标签下得到高置信正例并推广到全部词接缝，仍困难。

## 方法
弱监督分层锚点 + PU 学习：
1. 长停顿（如 ≥200 ms）得保守候选 B1；
2. 用音高重置与能量下降进一步筛成更严锚点 B2（强调 precision）；
3. 以高置信锚为 **正例**、其余为未标注，用 **nnPU**（\(\pi=0.01\)）训练轻量 MLP，对所有候选接缝输出连续 **boundary strength**。
特征在词接缝处用 Praat/Parselmouth 等提取；在大规模日语语料上验证。

## 实验与结果
摘要：日语大语料上，声学锚点 + PU 可恢复有意义的韵律边界模式，提供可解释、省标注的边界建模。
（抽取偏方法；具体 precision/AUC 表未完整出现在可读段。）

## 结论
优先高精度正锚再 PU 传播，可不依赖人工韵律标签估计边界强度，为后续合成/ASR/标点等提供数据高效路径。

## 点评
把“宁可少而准的正例”写进锚点层级，符合韵律边界感知上长停顿更可靠的语音学直觉。强在可解释声学配方；脆弱在 \(\pi\) 与停顿阈值敏感、且对无明显停顿的弱边界覆盖有限——作者亦以 precision 换 recall。
