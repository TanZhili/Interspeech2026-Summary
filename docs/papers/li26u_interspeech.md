# Geometric Second-Order Feature Correlation Learning for Self-Supervised Speech Emotion Recognition

- 论文编号：1210
- 报告人：Shuanglin Li
- 程序：Monday 28 September 2026 / Speech Emotion Recognition and Representation 1
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/li26u_interspeech.pdf

## 问题
SSL 帧级特征对 SER 很强，但一阶池化（均值/注意力）默认特征独立，丢掉通道间二阶相关；直接高维协方差又难算且在 SPD 流形上做欧氏操作会产生 swelling/伪熵。

## 方法
冻结 SSL 骨干提特征 X；SOC 层：可学习投影到低维子空间 → 中心化协方差 + 迹归一 → Log-Euclidean 映射到切空间 → 半向量化 → MLP 分类。作为可插拔模块，端到端可微。

## 实验与结果
在 ESD、RAVDESS（EmoBox 说话人无关协议）上，相对标准 GAP，SOC 分别提升约 4.68% / 4.42%；WavLM 上 ESD 峰值 WA 73.50%。去掉 LEM 分别掉约 1.45% / 1.65%。相对一阶注意力等基线持续更优。

## 结论
在子空间用 SPD + LEM 建模特征相关，可恢复一阶聚合丢失的判别信息，稳定聚合高维 SSL 特征用于 SER。

## 点评
把“情感在相关结构里”落到可插入的几何层，比盲目双线性池化更自洽。子空间维 d 与数值稳定仍是工程关键；效果依赖冻结骨干质量，未证明对端到端微调 SSL 同样必要。
