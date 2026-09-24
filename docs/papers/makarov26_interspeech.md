# Repurposing a Speech Classifier for Guided Diffusion-Based Speech Generation

- 论文编号：3448
- 报告人：Rostislav Makarov
- 程序：Wednesday 30 September 2026 / Acoustic Signal Analysis and Generation
- 技术分类键：signal
- 全文：https://www.isca-archive.org/interspeech_2026/makarov26_interspeech.pdf

## 问题
扩散条件生成常用分类器引导，需独立训 score 模型与噪声条件分类器，双模型推理贵。能否把常规训练的语音分类器主干直接复用为生成骨干？

## 方法
在 log-Mel 空间：冻结噪声条件分类器，挂轻量 Score Subnet。取编码器多尺度前向特征 tap，并对 JEM 式边际 \(\log p(X_t)\) 反传得梯度 tap，RMS 归一化后交叉注意力融合，自深到浅上采样解码预测 score；仅训 Subnet（DSM）。条件采样时同一分类器做标准引导。评测 SC09（spoken digits），HiFi-GAN 声码。

## 实验与结果
无条件：Score Subnet（总参 12.3M/可训 4.4M，12.07 GMACs）ScoreQ 3.10、FID 0.17，与全训 U-Net（16.6M，14.56 GMACs）相当或略优，并优于 DiffWave/SaShiMi 等开源基线。条件（γ=3）：质量持平 U-Net+分类器，但总参/计算更低（16.44 vs 22.74 GMACs）。去梯度 tap 更省算力但多数指标变差。低数据/标签子集上，Subnet+引导 FID 优于引导 U-Net。

## 结论
冻结分类器 + 轻量 score 子网可在单骨干上实现条件语音扩散生成，降参降算；梯度 tap 有用。低数据复用分类器表示时优势更明显。

## 点评
把 JEM“分类器暗含能量模型”用到表示级而非端到端训能量模型，避开归一化不稳，策略聪明。SC09 任务偏简单，是否推广到开放词汇/长语句仍未知；但“判别–生成共用骨干”对边缘部署很有吸引力。
