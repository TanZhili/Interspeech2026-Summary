# Probing Linguistic Information in Speech Embeddings: A Diagnostic Analysis across Acoustic and Structural Domains

- 论文编号：905
- 报告人：Simon Gonzalez
- 程序：Wednesday 30 September 2026 / New Architecture and Analyses for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/gonzalez26b_interspeech.pdf

## 问题
现代语音嵌入广泛用于 ASR 与语音–语言模型，但其语言学可解释性不足：不清楚哪些声学/语音学/更高层结构信息可被线性读出，以及信息如何沿层级分布。

## 方法
在 FLEURS 子集（36 语、43185 条、约 136 小时）上，用 W2V-BERT 2.0（约 600M，多语）提取帧级嵌入，时间维 median pooling 得话语向量（长句切 10 秒再 median）。从音频提取声学（jitter/shimmer、谱平坦度、ZCR、centroid 等）、语音学（时长、语速、pitch range、RMSE）与结构特征（Stanza：UPOS 熵、lemma 复杂度、从句复杂度、CTTR）。用 Lasso 回归学习嵌入→特征映射，五折选参，报告 train/test \(R^2\)。

## 实验与结果
线性关联强度随层级递减：
- 声学最强：Shimmer \(R^2\)=0.59，Flatness 0.56，ZCR 0.51 等。
- 语音学：Duration 0.51，Speech Rate 0.32；RMSE 0.19、Pitch Range 0.15 较弱。
- 结构：CTTR 0.43 仍可观；UPOS 0.04、Clause 0.02、Lemma 近 0。

作者强调是分布式、梯度式关联，而非维度与语言学单位一一对应。

## 结论
嵌入对贴近信号实现的声学/时序特征最敏感，词汇复杂度有可测关联，形态与句法复杂度线性可及性有限。结果受数据集、特征与模型选择约束；嵌入宜与符号语言学分析互补，尤其利好低资源场景中的可扩展诊断。

## 点评
这是一份清晰的“能线性读出什么”的诊断图：靠近声学的特征最强，句法最弱，符合自监督目标更贴信号的直觉。Median pooling 可能抹掉跨帧结构关系，因此弱句法关联未必等于模型完全不编码结构；若要追问更高层信息，需要更强探测或保留时序结构的读出方式。
