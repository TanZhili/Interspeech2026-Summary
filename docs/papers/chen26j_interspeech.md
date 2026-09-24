# Spiking Vocos: An Energy-Efficient Neural Vocoder

- 论文编号：1086
- 报告人：Yukun Chen
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/chen26j_interspeech.pdf

## 问题
频域声码器如 Vocos 算力轻但仍非真正为低功耗优化；直接把 ANN 换成 SNN 常因二值脉冲信息瓶颈与时序建模不足而掉点。

## 方法
Spiking Vocos：在 ConvNeXt 点卷积前插入 PLIF 神经元，并用幅度捷径 |Zin|⊙Zout 保留幅值；自架构蒸馏对齐中间特征与幅相谱（含抗缠绕相位损失）；每块加入 Temporal Shift Module 融合过去/当前/未来通道。在 LibriTTS 训练，对比 ANN Vocos 与不同步数/消融。

## 实验与结果
4 步 + TSM + 蒸馏：UTMOS 3.74（ANN 3.82），PESQ 3.45；主观 MOS 3.69 接近 Vocos 3.80。理论能耗约 ANN 的 14.7%（>6.8× 能效）。单独 TSM 或蒸馏均可显著回升 4 步基线；8 步更接近 ANN 但延迟加倍。

## 结论
幅度捷径、自蒸馏与 TSM 协同可使脉冲频域声码器在感知质量接近 ANN 的同时大幅降能耗。

## 点评
把 SNN 约束对准声码器瓶颈（点卷积算力、幅值丢失、因果时序盲区）很对症。能耗为 45nm 理论估算，真实芯片部署与延迟–质量权衡仍需验证；PESQ 与主观差距也提示脉冲量化对信号级指标更敏感。
