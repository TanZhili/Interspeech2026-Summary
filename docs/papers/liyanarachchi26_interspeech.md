# Paediatric-HGNN: A Hybrid Heterogeneous Graph Neural Network for Detecting Disfluency in Children’s Speech via Multiscale Acoustic Fusion

- 论文编号：1131
- 报告人：Rashini Liyanarachchi
- 程序：Wednesday 30 September 2026 / Child Speech and Health
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liyanarachchi26_interspeech.pdf

## 问题
成人口吃检测模型难迁移到儿童：声学变异大，病理口吃与典型发展性不流畅高度重叠，黑盒模型临床可解释性不足。

## 方法
Paediatric-HGNN（CaPIN）：异构图连接词节点（词汇意图）与帧节点（细粒度声学），多尺度融合；仅用 UCLASS + FluencyBank Voices-CWS 儿科自发语料；说话人独立 5 折；主评测 3 类（Fluent / Core Stutter / Typical Disfluency），并报 4 类对照；对比成人 SEP-28k 迁移与 ResNet+BiLSTM、StutterNet 等。

## 实验与结果
加权准确率 82.4%±2.7%；Fluent F1 0.904，Typical Disfluency F1 0.386，Core Stutter F1 0.280。成人迁移后 Typical Disfluency F1 骤降至约 0.08。4 类 UCLASS 上 Fluent F1 0.90，相对多数基线明显更高，病理细类仍难。

## 结论
儿科专用图建模与词–帧层级交互有助于区分发展性与病理不流畅；成人 SOTA 不能直接当儿科诊断工具。层次注意力提供一定可解释性。

## 点评
抓住“典型不流畅 vs 核心口吃”这一临床关键区分，并用词节点注入语义，是正确问题设定。Core/Typical F1 仍偏低，类别稀少与自发语料限制明显；与基线的分类体系对齐依赖映射，跨论文对比需谨慎。
