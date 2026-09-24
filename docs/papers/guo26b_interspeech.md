# COALA: Robust Contextualized Speech-augmented Language Modeling for ASR via Contrastive Regularizer and Biasing Score Estimation

- 论文编号：1097
- 报告人：Jhih-Rong Guo
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/guo26b_interspeech.pdf

## 问题
SLM 语境偏置在大列表与多实体共现时易因上下文窗口与干扰项退化；既往判别损失在多正样本上训练易塌或需辅助 log loss。

## 方法
COALA：冻结骨干 + LoRA，用判别投影器把实体 token 隐状态映射为长度归一化匹配分；提出 Multi-Positive Discriminative Loss（MPD）与 Decoupled Point-wise Discriminative Loss（DPD）缓解多正样本梯度冲突。推理可用 Biasing Target Identification（Top-K 打分）过滤后再送 ASR 提示，并用 `<unbiased>` 阈值。

## 实验与结果
LibriSpeech：DPD 在 test-clean 上 Recall#20 达 99.09%，可独立收敛；相对 Bias-Loss/CTC-Filter 等更稳。加 BTI 后，在 N=500/1000/5000 偏置列表上 B-WER 显著优于无筛选的大列表直接偏置，可扩展到大 N 而避免 OOM。

## 结论
专用打分空间 + 多正样本稳健目标，可在复杂多实体场景提升语境偏置，兼顾列表规模与 B-WER。

## 点评
把“从大列表筛相关实体”从生成分布中拆出，切中 SLM 窗口瓶颈。无偏置时基线 WER 偏高，对比需看相对增益；大 N 下仍依赖 Top-K 启发式与阈值，召回–误召平衡值得更细分析。
