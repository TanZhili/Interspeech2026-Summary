# Modality Importance is Not Static: Temporal Dynamics via Gating in Multimodal Emotion Recognition

- 论文编号：1399
- 报告人：Jiyeon Ryu
- 程序：Wednesday 30 September 2026 / Multimodal Emotion Recognition
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ryu26_interspeech.pdf

## 问题
多模态情绪识别常做静态按句融合，默认模态贡献时间不变；对话中文本/语音/视觉重要性是否随时间与类别变化，缺少协议对齐的实证与归因验证。

## 方法
解耦：GPT-2、HuBERT、VideoMAE 提单模态特征后冻结主干。对比静态 MLP、时序 GRU、local/contextual/emotion-query 门控。emotion-query 用可学类别查询与上一时刻状态算类条件模态权重再边缘化为 α_t。IEMOCAP 6 类（exc→hap）5-fold LOSO，K=8；用时间遮挡与 time×modality 遮挡的 AOPC 检验忠实性。

## 实验与结果
Temporal EQ-Gate：Macro-F1 0.5731、UA 0.5734；相对静态 logits MLP 平均提升约 +9（mean(F1,UA)），相对无门控 GRU +1.63；并超过同协议 Transformer/MulT/MMER，参数仅约 0.076M。hap/fru/sur 等类受益更明显。门权重均值文本最高但各模态标准差非零；AOPC 随 top-k 遮挡单调上升。McNemar/bootstrap 相对静态显著。

## 结论
模态重要性非平稳且类条件；显式时序门控比单纯加大融合容量更有效，多模态 SER 应视为动态决策而非静态融合。

## 点评
用“分析优先、不大模型堆叠”把假设钉死，并用扰动 AOPC 补注意力不可信问题，证据结构清晰。IEMOCAP 偏剧本、文本干净，文本权重大部分来自标签对齐；自然对话外推仍待验证。
