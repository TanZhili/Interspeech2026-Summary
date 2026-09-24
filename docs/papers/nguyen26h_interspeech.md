# What Does a Pathological Speech Assessment Model Know about Acoustic Features? A Case Study on Oral and Oropharyngeal Cancer Patients

- 论文编号：3343
- 报告人：Tuan Nguyen
- 程序：Thursday 1 October 2026 / Pathological Speech Assessment 4
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/nguyen26h_interspeech.pdf

## 问题
病理语音评估中，深度学习性能强但难解释，手工声学特征可解释却缺乏统一选择标准。需要把两者桥接起来，弄清可懂度模型到底编码了哪些声学信息。

## 方法
对 Nguyen 等基于 Wav2Vec 2.0 Large、先 ASR 微调再回归可懂度的模型（C2SI 朗读任务 MAE 0.68）做层间解释：用 opensmile 提取 eGeMAPS 25 个 LLD（25 ms 对齐），以 PWCCA 度量各 Transformer 层嵌入与 LLD 的线性相关。个体层分析看各 LLD 相关排序随层变化；组层分析只取最后一层，将 LLD 重组为 Prosodic / Spectral / Voice Quality 三类并取组内均值相关。语料为法语 C2SI：口腔/口咽癌患者与对照，专家共识可懂度 0–10。

## 实验与结果
早期层 MFCC 1–4 相关最高；随深度增加，MFCC 2–4 排名下降，共振峰能量、F0、HNR 等上升，但 MFCC 1 全程保持最高相关。共振峰带宽、jitter、shimmer、H1–H2 等整体相关最低。末层组相关：Spectral 0.77、Prosodic 0.71、Voice Quality 0.65。末层与 eGeMAPS 整体相关下降，提示可能编码超出该特征集的信息。

## 结论
该可懂度模型表征主要对齐频谱与韵律信息，与无喉受累的 OOC 人群损伤特点一致；MFCC 1 等强相关 LLD 可作为可解释替代特征的候选。作者建议扩展特征集、SSL 架构与病症类型，并推动统一临床参考特征集。

## 点评
用临床可懂的手工特征当“尺子”量 SSL 层表征，比只报 MAE 更利于临床信任。组相关差异与“无喉癌”人群设定吻合，解释力强；但相关≠因果，且作者也承认“高相关特征可替代深度学习”仍待实证验证。
