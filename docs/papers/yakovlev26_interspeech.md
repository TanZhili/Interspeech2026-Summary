# ReDimNet2: Scaling Speaker Verification via Time-Pooled Dimension Reshaping

- 论文编号：1447
- 报告人：Ivan Yakovlev
- 程序：Wednesday 30 September 2026 / Speaker Verification: Architectures, Losses, and LLMs
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yakovlev26_interspeech.pdf

## 问题
ReDimNet 全程保持时间分辨率，1D 通路算力随 C×T 增长，限制通道加宽；如何在维度重塑框架内引入时间池化以改善精度–算力帕累托前沿。

## 方法
在 2D 块对时间轴做步长卷积池化（减 T 不加倍 C，软放松 C·F·T 守恒）；1D 块在更短序列上运行；阶段加权聚合前最近邻上采样回输入 T，保留残差连通。定义 B0–B6（1.1M–12.3M 参、0.33–13 GMACs）。VoxCeleb2 两阶段训练（SF2-C，LM 微调 6 s），余弦打分无 AS-Norm。

## 实验与结果
几乎每个匹配算力点 ReDimNet2 优于 ReDimNet。B6：Vox1-O 0.29% EER、Vox1-H 0.99%，12.3M/13 GMACs，相对原 B6 约 −28% EER、−36% GMACs。B3 起超过 ResNet293；B6 优于 WavLM 并接近 W2V-BERT 2.0 而参数小约 48×。SITW/VOiCES/Vox1-B 域外平均 1.84 vs 原 1.87。大模型（B4–B6）种子方差更大。

## 结论
时间池化与维度重塑兼容，是扩展说话人嵌入网络的简单有效策略；代码与权重已开源。

## 点评
用整条 B0–B6 匹配算力对照做“消融”，证据比单点刷榜扎实。大模型训练不稳提示还需正则；与更大外部数据训练的 SOTA 对比时需注意数据量差异。
