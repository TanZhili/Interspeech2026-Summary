# Minimum Token Thresholds and Stabilisation for Reliable Automatic Vowel Alignment: Empirical Study on TIMIT Vowels and MFA

- 论文编号：934
- 报告人：Simon Gonzalez
- 程序：Monday 28 September 2026 / Tools and Techniques for Phonetic Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/gonzalez26d_interspeech.pdf

## 问题
强制对齐已成语音学标配，但声学测量要多少 token 才“够稳”、与人工边界可比，仍缺经验阈值。低资源与大规模社会语音学都需要最小样本量指南。

## 方法
在 TIMIT 元音上，以人工音素边界为金标准，用 **MFA** 自动对齐；对 Duration、F1、F2 递增抽样 token，逐步拟合混合效应模型，比较自动 vs 人工测量差异轨迹，定位 **稳定点**（趋势平台）与 Kendall τ。

## 实验与结果
- **85%**（33/39）元音–特征组合随 token 增加显著改进；F1 对所有元音均改进。
- 多数约在可用 token 的 **50%** 附近稳定；Duration 最早（约 **24% / ~30 tokens**），F1 约 36% / ~1088，F2 最晚（约 **56% / ~1335**）。
- 元音间差异大：如 IH 较早稳定（约 31%），AW/AO 更晚（约 82–86%）。

## 结论
给出按特征分化的最小 token 经验阈值：时长最省数、F2 最耗数；增大自动对齐样本通常使测量更接近人工金标准。

## 点评
把“对齐够不够”做成可操作的稳定点曲线，对社会语音学抽样设计很实用。强在特征分层；脆弱在仅 TIMIT+MFA——其他对齐器/语体/语言的阈值可能平移，不宜直接外推绝对数字。
