# Quantifying Dimensional Independence in Speech: An Information-Theoretic Framework for Disentangled Representation Learning

- 论文编号：1654
- 报告人：Bipasha Kashyap
- 程序：Wednesday 30 September 2026 / Speech and Language Representation
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/kashyap26_interspeech.pdf

## 问题
情绪、语言内容与病理标记共享声学通道，但解缠质量常靠下游任务间接判断。若维度间互信息很高，完全解缠可能理论上不可行；需要能量化跨维统计依赖的原则性框架。

## 方法
对手工声学特征划分 Emotional（28维）、Linguistic（33）、Pathological（16）以及 Source（9，声门）/ Filter（32，声道），用 Praat / librosa / openSMILE 提取。以 MINE（EMA 稳定下界）+ CLUB（方差钳位上界）+ KSG（k-NN 非参校验）做有界互信息估计，并按不确定性自适应加权得到最终 MI；再对语义维做 Source–Filter 归因比例。在 RAVDESS、IEMOCAP、L2-ARCTIC、GMU Accent、UA-Speech、MDVR-KCL 的全部 8 种 corpus 组合上评估。

## 实验与结果
- 跨维 Final MI 均 <0.15 nats（Emotion–Linguistic 0.12、Emotion–Pathology / Linguistic–Pathology 0.10），Δ 较紧；Source–Filter 显著更高（0.47±0.38）。
- 归因：情绪约 80% 来自 source；语言与病理分别为 filter 主导（约 60%、58%）。
- 跨组合一致性较好；跨维估计约 8–16 epoch 收敛，Source–Filter 需满 100 epoch。

## 结论
在所考手工特征空间中，三语义维近独立，解缠在理论上可行；Source–Filter 耦合更高但低于经典直觉预期。局限：未验证 wav2vec2/HuBERT 等学习表示、静态特征、分组有重叠、病理/情绪范式覆盖有限。

## 点评
把解缠从“下游涨了几个点”换成可复现的 MI 上下界，方法论价值大于任何单一数字。结论强依赖手工特征与操作化分组，作者也明确承认：测到的是这套特征集的依赖，不是抽象“情绪/语言/病理”本身。对编码器设计的启示（分路、按维对齐 source/filter）需在学习表示上再验证才站得住。
