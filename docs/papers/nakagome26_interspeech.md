# MixProLAP: Mixture-Induced Uncertainty Modeling for Probabilistic Language-Audio Pretraining

- 论文编号：360
- 报告人：Yu Nakagome
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/nakagome26_interspeech.pdf

## 问题
真实场景多事件重叠、同一场景可有多种文本描述，音频–文本对齐存在多对多歧义；确定性点嵌入的对比学习难以表达不确定性。掩码式不确定性模拟也不够贴近真实混合。

## 方法
MixProLAP：各模态表示为分布，做不确定性感知跨模态对齐；用音频–文本对混合构造重叠声，捕捉语义包含关系；引入多级 inclusion loss。相对 deterministic CLAP 基线（同数据同预训练权重、InfoNCE）比较。

## 实验与结果
零样本检索：AudioCaps 训练时 A→T R@1 26.85（CLAP 24.23）；Clotho 训练在 Clotho A→T R@1 15.60（CLAP 13.40）。消融显示 mixing + multi-level inclusion 优于谱/词掩码不确定性策略。

## 结论
作者认为混合诱导的概率对齐能更好建模多事件与多样描述歧义，提升检索鲁棒性。

## 点评
用真实感混合代替掩码来造不确定性，切中声学场景本质；概率嵌入也便于解释语义密度。T→A 部分设定提升不均，说明分布建模对检索方向不对称，仍需更细校准。
