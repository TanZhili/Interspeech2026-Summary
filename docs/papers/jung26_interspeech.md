# Listening Between the Lines: Joint Learning of ASR Embeddings and LLM-Augmented Linguistics for Dementia Detection

- 论文编号：939
- 报告人：Myungwoo Oh
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 2
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jung26_interspeech.pdf

## 问题
痴呆语音筛查需同时捕捉声学与语言生物标记，但多数系统单模态；信息单元等手工语言方案覆盖有限，LLM 又常作黑盒或仅对齐旧 IU 框架。

## 方法
Whisper 双用：编码器输出经时间网络+注意力池化得声学嵌入；ASR 转写经 LLM 抽取 46 维可解释语言特征（词汇/句法/语义连贯/语篇），筛选为 29 维；门控融合两模态。评测 ADReSS / ADReSSo。

## 实验与结果
说话人级 F1：ADReSS 89.47%、ADReSSo 90.14%。多模态优于单模态；优化 29 特征集含部分统计不显著特征却优于显著性过滤集，提示交互作用。相对部分先验工作相对 F1 提升约 19%。

## 结论
声学嵌入与 LLM 增广语言特征经门控融合，可在标准 Cookie Theft 基准上达到强 AD/CN 判别，并强调特征交互而非仅显著性筛选。

## 点评
把 LLM 当成可解释特征抽取器而非端到端分类器，利于临床可沟通性。与同场 park26c 同报 90.14% F1，需注意设定差异；转写错误与 LLM 提示敏感性仍是误差源。
