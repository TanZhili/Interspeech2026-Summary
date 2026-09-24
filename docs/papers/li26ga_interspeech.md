# Gated Multi-graph Fusion via Graph Attention Networks for Alzheimer’s Disease Detection

- 论文编号：2578
- 报告人：Xiao Wei
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 2
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26ga_interspeech.pdf

## 问题
AD 自发言语存在非线性结构破坏与症状异质性；多数系统偏语义向量或简单融合，难刻画语篇“内容–结构–流向”与个体差异。

## 方法
ASR 转写后建三视图图：语义图、依存图、基于规范语料 PMI 的共现图（量化叙事逻辑相对健康常模的偏离）；图注意力编码后经自适应门控按样本融合。在 ADReSSo 上评估。

## 实验与结果
准确率 90.00%。消融表明 PMI 共现图与异质性感知门控对稳健分类关键。

## 结论
多图“内容–结构–流向”建模加门控融合，可提升 AD 自发言语检测并适配症状多样表现。

## 点评
用健康常模 PMI 刻画“叙事流向”偏离，比纯语义嵌入更贴语篇病理。依赖 ASR 质量；图构造与常模语料选择会影响跨域稳定性。
