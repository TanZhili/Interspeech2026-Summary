# Relating the Neural Representations of Vocalized, Mimed, and Imagined Speech

- 论文编号：2836
- 报告人：Rupesh Chillale
- 程序：Wednesday 30 September 2026 / Neurophysiology of Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/maghsoudi26_interspeech.pdf

## 问题
发声、默读口型（mimed）与想象言语的神经表征常被分开解码；它们共享多少结构、线性解码器能否跨条件迁移，对 BCI 很关键。

## 方法
VocalMind 单被试普通话 sEEG（110 电极，100 句×2/条件）：用时间滞后线性模型重建 NSL 皮层谱图，分别得 Gv/Gm/Gi，做条件内与跨条件测试；秩分析测刺激可分性；并复现卷积–RNN 非线性解码器对比。用打乱配对零模型检验显著性。

## 实验与结果
条件内重建显著优于零模型（p≪0.001），发声最优，默读次之，想象最弱；跨条件相关仍显著，默读↔发声迁移较强。秩分析显示默读训练解码器在发声上保留刺激结构（如 AUC 模式），想象侧较弱。非线性亦有跨条件迁移，但线性在刺激级可分性上更优。

## 结论
三种言语产生模式共享可迁移的神经–声学映射；线性解码器可解释且跨条件可用，利于无声输出的 BCI，但想象条件对齐与信息量仍受限。

## 点评
用跨条件迁移直接量“共享表征”，比单条件重建更有理论含量。强在线性可解释与秩分析；弱在单被试、想象对齐难，外推多被试需谨慎。
