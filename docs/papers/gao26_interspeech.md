# NoiseLoRA-SV: Hierarchical Noise-Conditioned Adaptation with Embedding Distillation for Robust Speaker Verification

- 论文编号：64
- 报告人：Dai Gao
- 程序：Monday 28 September 2026 / Speaker Verification: Advances in Speaker Embeddings
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gao26_interspeech.pdf

## 问题
噪声下 SV 性能下降；静态后端与固定 LoRA 难应对非平稳噪声。级联增强易引入伪影，全量微调又贵。需要推理时按实例动态适配且参数开销可控的方案。

## 方法
NoiseLoRA-SV：CRN 重建噪声谱，MS-NRH 提全局 Z_global 与局部 Z_local；超网络由 Z_global 生成 LoRA A/B，浅层 Global LoRA 残差注入，深层 HNC 再乘由 Z_local 卷积得到的帧级门控。说话人骨干为轻微调 ECAPA-TDNN（亦可接 HuBERT/WavLM）。损失：AAM-Softmax + λ_noise MSE 噪声重建（0.1）+ λ_dist 掩码 InfoNCE 对比蒸馏（1.0，温度 0.07）对齐干净教师嵌入。VoxCeleb1 + MUSAN（SNR 0–20 dB）训练；测 MUSAN 已见与 NonSpeech100 未见噪声；LoRA rank=4，嵌入 192 维。

## 实验与结果
已见噪声平均 EER 3.05%（干净 1.70%），优于 ParaNoise-SV 3.40%、Diff-SV 3.90% 等。消融：去蒸馏 3.34%、去噪声损失 3.47%、静态 LoRA 3.28%、单块 LoRA 3.60%。未见噪声平均 3.60%（ParaNoise-SV 3.90%）。显式噪声重建优于类/SNR 属性估计（未见 3.60 vs 4.09）。跨骨干：ECAPA/HuBERT/WavLM 均降 EER，参数如 ECAPA 14.73M→24.19M。

## 结论
层次噪声条件 LoRA + 重建与对比蒸馏，能在中等参数开销下做实例级噪声稳健 SV，并对未见噪声与多种骨干可迁移。

## 点评
把“噪声条件生成 LoRA”与帧级门控绑在一起，比静态 PEFT 更贴非平稳场景；蒸馏对齐干净流形是稳健性关键。代价是推理仍跑噪声 CRN+超网络，边缘部署需权衡；训练噪声合成协议与基线对齐度也会影响绝对 EER 比较。
