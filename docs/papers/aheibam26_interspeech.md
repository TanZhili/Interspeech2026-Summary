# From Rhythm Metrics to Latent Embeddings: Categorising English and Hindi Varieties in Northeast India

- 论文编号：3462
- 报告人：John Aheibam
- 程序：Tuesday 29 September 2026 / Cross-Linguistic and L2 Phonetic Studies
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/aheibam26_interspeech.pdf

## 问题
东北印度多 L1 背景者常用英语与印地语，但英语变体的节奏是否随 L1 分化、抑或趋同，尚不清楚。作者比较传统节奏指标与自监督 LID 潜表征能否区分五类 NE 印度英语与两类印地语。

## 方法
70 名说话人（7 组×10）：五类 L2 英语（Angami、Assamese、Khasi、Meiteilon、Mizo）与 L1/L2 印地语，均朗读 “The North Wind and the Sun”（英/印文本不同）。人工标注呼吸组与 V/C 间隔，计算八种节奏指标；LME 检验语言效应；HAC 与线性 SVM 做聚类/分类。另用 Voxlingua107-xls-r-300m-wav2vec 提取 2048 维嵌入（含额外 L1 英语），PCA→LDA 可视化，并与节奏指标相关。

## 实验与结果
LME：%V、ΔV、VarCo-V/C、ΔC、nPVI-V 等有显著语言效应，但五类英语指标范围较窄。HAC：印地语与 NE 英语大体分开，英语内部不按 L1 成簇。SVM：HIN/AHI 准确率约 78%/77%，英语变体交叉混淆、最高约 40% 出头（机会率 14.3%）；ΔV、VarCo-V、%V 最重要。嵌入 LDA：英语五类重叠成簇，印地与英语分离；PC1 与 %V 强相关（r=0.77）。

## 结论
NE 印度英语节奏大体相近、L1 分化微弱；印地语与英语节奏更易区分；潜嵌入捕获超出纯时长节奏的声学–韵律信息，且 %V 部分体现在嵌入主维度。作者强调传统语音学与潜表征结合的价值。

## 点评
把经典节奏度量与 SSL 嵌入并置，适合回答“变体可分性”问题。但英/印材料并非同一文本，节奏指标对文本分段结构敏感，印地–英语分离可能部分来自文本而非变体；英语组内重叠也提示朗读任务与小样本限制了 L1 影响的可观测性。
