# ReDimNet2: Scaling Speaker Verification via Time-Pooled Dimension Reshaping

- 论文编号：1447
- 报告人：Ivan Yakovlev
- 程序：Wednesday 30 September 2026 / Speaker Verification: Architectures, Losses, and LLMs
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yakovlev26_interspeech.pdf

## 问题
ReDimNet 在全程保留时间分辨率时，1D 通路通道加宽会使计算近似二次增长，限制在同等算力下把模型做宽。

## 方法
在维度重塑框架中引入时间池化：部分 stage 用与频率下采样相同的 strided conv2d 在时间维减半但不加倍通道，软放松 C·F·T 体积约束；stage 聚合前最近邻上采样对齐到输入 T，保留残差。复用原最佳 1D/2D 块。定义 B0–B6（约 1.1M/0.33 GMACs–12.3M/13 GMACs）。VoxCeleb2 两阶段训练（SF2-C + large-margin finetune），余弦打分无 AS-Norm。

## 实验与结果
几乎每个匹配算力点上 ReDimNet2 优于 ReDimNet。B6：Vox1-O 0.29% EER（相对 B6-v1 约降 28%），Vox1-H 0.99%，参数/GMACs 更少；相对 WavLM 等大 SSL 模型参数小约 48× 仍更优或接近。SITW/VOiCES/Vox1-B 域外平均 1.84，略好于 ReDimNet-B6。大模型（B4–B6）训练方差增大（B6 Vox1-O 0.32±0.05%）。

## 结论
时间池化与维度重塑兼容，能在不破坏残差逻辑下释放算力做宽模型，全面改善准确率–效率 Pareto 前沿。

## 点评
改动小、证据是整条规模曲线而非单点刷榜，对工程缩放很有说服力。大配置训练不稳需额外正则；与扩展数据训练的 W2V-BERT 等不在同一数据设定，比较需分栏阅读。
