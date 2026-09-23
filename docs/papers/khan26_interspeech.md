# Dual-Branch Gated Fusion for Open-Set Audio Deepfake Source Tracing

- 论文编号：3008
- 报告人：Khalid Malik
- 程序：Monday 28 September 2026 / Speech Deepfake Detection: Robustness, Generalization, Attribution
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/khan26_interspeech.pdf

## 问题
开集源追踪需识别未见合成系统并拒绝过自信；纯 SSL 在域内强但 OOD 过承诺，手工特征更稳但不够判别；朴素拼接会被高维 SSL 淹没。

## 方法
双分支：冻结 XLSR-53（1024-d）与 66-d CORES（MFCC+Δ/ΔΔ、chroma、ZCR、RMS、谱质心/带宽/滚降/对比/平坦度）。各投影到 256-d，输入条件门控软加权融合。联合训练：标签平滑 CE + 能量间隔损失促 ID/OOD 分离 + 门控多样性防单支塌缩。

## 实验与结果
MLAAD：ID Acc 97.6%、EERc 4.9%、FPR95 10.4%（相对文中参考基线 FPR95 相对降约 83.5%），约 0.9M 参数。消融显示固定拼接/单支难以兼顾 ID 与开集拒绝。

## 结论
输入条件门控融合 SSL 与多维手工描述子，可在保持高域内归因准确率的同时改善未见合成器的开集拒绝。

## 点评
明确针对“SSL 过拟合训练分布”与“手工特征保守”的互补性，门控比固定融合更对症。CORES 组合本身不新，价值在开集目标下的自适应加权与能量间隔；对极端未见管线仍依赖能量分数标定。
