# Dictionary-Free Discrete Key-Value Attention for Improving Speech Enhancement

- 论文编号：2881
- 报告人：Zihao Cui
- 程序：Thursday 1 October 2026 / SE Architectures, Adaptation and Audio Front-Ends
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/cui26b_interspeech.pdf

## 问题
Harmonic Attention（HAtt）用手工谐波字典改善浊音谱重建，但对清音/无声段弱；依赖先验的固定字典限制了更全面的 key–value 结构化表征。

## 方法
提出 Dictionary-Free Discrete Attention（DFDA）：用 Finite Scalar Quantization（FSQ）在注意力前离散化 key 与 value（轻量 encoder–quantizer–decoder，无需显式可学习 codebook），形成信息瓶颈以稳住语音相关模式、抑制噪声随机波动。嵌到 TFGridNet：前两层注意力换成 DFDA；并与前端 HAtt 组合。损失为压缩幅度/复谱 + SI-SNR。

## 实验与结果
约 25k 小时语音 + DNS 噪声 + RIR 训练；seen 与 Emilia/LibriSpeech unseen 评测。TFGridNet+HAtt+DFDA 在 Emilia 上 PESQ 2.89、ESTOI 90.7、SISNR 16.55，优于基线与单用 DFDA/HAtt；UV SSNR 最高（seen 8.84），验证清音恢复。DFDA 仅增约 0.48 GMACs。

## 结论
数据驱动的离散 key–value 与谐波先验互补，联合使用可同时加强谐波与清音结构，提升质量与可懂度。

## 点评
把神经编解码里的 FSQ 瓶颈搬进 SE 注意力，避开手工字典，与 HAtt 的互补叙事清楚。对比主要相对 TFGridNet 变体，生成式 SE 骨干上的迁移仍待验证。
