# How Bilingual Are SSL Speech Models? Cross-Lingual Probing of Articulatory Encoding with Finnish and Russian EMA

- 论文编号：1324
- 报告人：Ruchi Pandey
- 程序：Tuesday 29 September 2026 / Speech Production and Perception 1
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/pedro26_interspeech.pdf

## 问题
SSL 表征含丰富语音信息，但跨语言如何编码发音动作、对芬兰语–俄语等类型距离语对是否仍语言无关，缺少 EMA 探测证据。

## 方法
双语芬–俄说话人 EMA（舌/唇等 X/Z）；线性探测 SSL 层预测轨迹，Pearson r；约 5 分钟配对数据即可训。实验矩阵含跨模型、层、数据量、LOSO 说话人泛化、朗读 vs 自发、语言熟练度（Table 1）。

## 实验与结果
多语模型更优：如 MMS-300m、XLSR-53 (RU FT)、XLS-R (FI FT) 平均 r≈0.686–0.689（最高约 0.68）。中间层最有效；舌运动比唇更可预测；结构化任务准确更高；跨熟练度泛化强。

## 结论
SSL 含部分语言无关的发音子空间，支持跨语发音可解释性与相关语音技术应用。

## 点评
用同一双语者 EMA 控说话人，干净检验跨语发音编码。强在 LOSO 与任务类型分解；脆弱点在线性探测可能低估非线性编码，被试规模限制个体差异结论。
