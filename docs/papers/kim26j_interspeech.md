# MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation

- 论文编号：1150
- 报告人：Dohwan Kim
- 程序：Thursday 1 October 2026 / Source Separation 2
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/kim26j_interspeech.pdf

## 问题
多通道分离判别模型在 SI-SDR 等参考指标上已很强，但常引入不自然伪迹，DNSMOS/UTMOS 等听感指标偏弱；纯生成或迭代修正延迟高，Fast-GeCo 一类一步修正又需两阶段蒸馏、轨迹截断与纯 SI-SNR 微调，存在分布失配且听感次优。

## 方法
MeCo：在复杂 STFT 域，以判别分离结果 ˆs（t=1）与多通道混合 y 为条件，用 Mean Flows 学习平均速度场，一步映射到干净语音（t=0），无需微调解码轨迹。引入 Data-Space Optimization (DSO)：xr-loss（等价对 MeanFlow 损失按间隔 Δ² 加权，惩罚长位移误差）+ Endpoint SI-SDR（训练时模拟一步端点重建并优化 SI-SDR）。骨干 NCSN++；判别前端含轻量 DeFTAN2、SpatialNet、CrossNet；修正器仅在 DeFTAN2 输出上训练后零样本接到其他分离器。

## 实验与结果
域内：WSJ0+WHAM! 四麦混响噪声；域外：Librispeech+DEMAND、低资源语言+DEMAND。一步修正仅 +1 NFE、RTF +0.0068。DeFTAN2+MeCo 在域内 SI-SDR 10.08、DNSMOS 3.19、UTMOS 3.70、NISQA 4.50，全面优于 Fast-GeCo/MeanFlow；域外与跨语言同样领先。消融显示 xr-loss 与 Endpoint SI-SDR 互补。

## 结论
作者认为 MeCo 是首个面向多通道分离的一步生成修正器，在保真与听感上同时达到 SOTA；文末提到独立按说话人修正等局限（正文截断处提及）。

## 点评
用平均速度场直接做判别→干净的一步传输，比扩散蒸馏更干净；DSO 把“生成轨迹误差”与“端点 SI-SDR”绑在一起，解释了为何听感与保真可兼得。脆弱点包括按说话人独立修正、依赖前端分离质量，以及跨分离器零样本仍受前端伪迹形态约束。
