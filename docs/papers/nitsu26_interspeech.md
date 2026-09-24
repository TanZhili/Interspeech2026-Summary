# Pseudo-Spatially Conditioned TF-Locoformer with MHCA+FiLM Fusion for Single-Channel Speech Separation

- 论文编号：2027
- 报告人：Daichi Nitsu
- 程序：Thursday 1 October 2026 / Source Separation 2
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/nitsu26_interspeech.pdf

## 问题
单通道分离在噪声混响下困难，因推理时缺少 ITD/ILD/IPD 等空间线索；多通道模型可用这些线索，但部署常只有单麦。需要在训练期利用多通道“特权信息”、推理仍仅单通道的方案。

## 方法
伪空间条件化：（1）对比预训练——SC/MC 两套独立权重 ResNet 空间编码器；triplet 中 anchor 为单通道混合物，positive 为同空间配置不同内容的双通道，negative 为同内容不同空间配置的双通道，使嵌入偏空间配置而非语音内容；（2）与 TF-Locoformer 联合微调，用 MHCA+FiLM 融合模块在每个 Locoformer 块前注入伪空间嵌入（MHCA 得自适应嵌入，FiLM 做特征仿射调制）。推理仅用单通道左耳信号。

## 实验与结果
WHAMR!（8 kHz）：Proposed (S) SI-SNRi 17.7 / SDRi 16.1（基线 17.4/15.9，+1.0M 参数）；(M) 18.9/17.2（复现基线 18.6/16.9，+1.2M）。无噪声 NF-WHAMR! 上 (S) 从 21.4→22.0 SI-SNRi。消融：可训练编码器 + MHCA+FiLM 最优；triplet 内容重叠越少越好；推理时错配/全局平均嵌入会使性能掉到无条件基线以下。

## 结论
用多通道特权信息对比学习伪空间嵌入，再经 MHCA+FiLM 条件化单通道分离器，可在小参数开销下稳定提升 WHAMR! 表现。

## 点评
把“训练见多麦、推理单麦”做成空间表征迁移，比硬加 DOA 头更软。增益约 0.3 dB 量级但统计一致；嵌入错配会伤性能，说明模型确实依赖该条件，也意味着嵌入质量/域偏移会成为新脆弱点。
