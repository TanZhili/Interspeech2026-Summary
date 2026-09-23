# Towards Robust Generative Speech Enhancement Using Vector Quantisation-Based Neural Audio Codec

- 论文编号：2564
- 报告人：Haixin Zhao
- 程序：Tuesday 29 September 2026 / Language-Model and Codec-Token Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhao26i_interspeech.pdf

## 问题
基于 VQ 的神经音频编解码（NAC）语音增强中，连续潜空间预测与离散 token 分类两种策略的信息建模差异仍不清楚；连续建模常不用 VQ，作者假设 VQ 本身可独立于离散分类带来鲁棒性。预训练编解码在干净语音上训练，对失真输入存在失配。

## 方法
以 DAC（K=12、码本 1024、维 1024）为基座，提出：dNAC-SE——对噪声潜表示做残差 VQ 后用 enhancer 预测各码本 logits（IM/JM/HM 三种残差建模）；cNAC-SE——在连续潜空间回归干净表示，再经 VQ 作干净先验正则，并与无 VQ 的判别式变体对比。Enhancer 为 6 层 Transformer，梯形掩码约 1 s 因果上下文。损失：cNAC-SE 用潜空间 L2 + 多分辨率波形损失；dNAC-SE 用加权 CE。编码器/解码器可冻结或微调（soft/hard）。在 DNS3 约 140 小时合成数据上训练，用 DNS-MOS 评估。

## 实验与结果
dNAC-SE 中 JM 最好且算力更低；全微调 cNAC-SE 在 With Reverb / Without / Real 上 OVRL 约 2.91 / 3.37 / 3.19，全面优于各 dNAC-SE，enhancer 仅 2.58 GMAC/s。相对判别式 cNAC-SE，有 VQ 正则在混响未见失真上增益更明显。对标 CDiffuSE、SGMSE、StoRM、SELM 等，cNAC-SE 多数 DNS-MOS 领先。PCA 显示 cNAC-SE 相对干净先验的偏差更紧、更居中。

## 结论
连续潜空间增强 + VQ 干净先验正则优于离散 token 分类；VQ 鲁棒性可与离散建模解耦。全编解码微调有效。局限是完整 codec 管线算力仍可能限制端侧部署。

## 点评
把“VQ 当正则还是当分类目标”拆开验证，理论图示与 PCA 支撑了连续回归在误差几何上更稳。强在机制解释；脆弱点是评测以非参考 DNS-MOS 为主、且依赖干净先验码本，对分布外失真的先验覆盖仍是瓶颈。
