# Linguistic Bias Mitigation for Spoofing Detection via Gradient Reversal and A Variational Information Bottleneck

- 论文编号：676
- 报告人：Mickael Rouvier
- 程序：Tuesday 29 September 2026 / Speaker Verification and Anti-Spoofing
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/dao26_interspeech.pdf

## 问题
ASVspoof 5 上 bona/spoof 的所说内容分布不匹配，检测器可能走语言捷径而非生成伪迹，导致跨库泛化差；无转录时难以直接对齐文本。

## 方法
SONAR 与自建短语内容教师嵌入的聚类/t-SNE 诊断语言偏置。IVLing-VIB：Common Voice 英语子集训 XLSR+MHFA 短语 ID 教师；学生含 spoof 头与经 GRL 的短语内容头，对抗压低语言信息；内容支路用 MHFA-VIB（对 key 做高斯后验+KL）约束抑制强度，避免误删有用伪迹线索。在 ASVspoof 5 训练，于 DF Arena 多英语集评测。

## 实验与结果
相对 MHFA，IVLing-VIB 跨集合并阈值 EER 约降 36% 至约 9%；多数单集最低（如 ITW 1.88%、ASV19 LA 4.07%）。相对挑战榜前列，ASVspoof 5 本集略高但其他库大幅更好，平均 EER 3.97%。

## 结论
语言偏置是跨数据退化的重要来源；教师–学生 GRL + VIB 可在无测试转录下学语言不变表示并提升泛化。

## 点评
把 shortcut 从静音等已知偏置扩到内容分布，分析与方法衔接清楚。教师在外部短语分类上的代理质量决定上限；过强对抗仍可能伤说话人/信道相关线索，VIB 是必要缓冲。
