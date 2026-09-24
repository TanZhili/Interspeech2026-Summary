# Modality Importance is Not Static: Temporal Dynamics via Gating in Multimodal Emotion Recognition

- 论文编号：1399
- 报告人：Jiyeon Ryu
- 程序：Wednesday 30 September 2026 / Multimodal Emotion Recognition
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ryu26_interspeech.pdf

## 问题
对话情绪跨话轮展开，但多数 MER 做静态句级融合，隐含模态重要性时间不变；是否真存在随时间、随类别变化的模态权重，缺少可控证据。

## 方法
解耦单模态编码与融合：冻结 GPT-2 / HuBERT / VideoMAE（视频可解冻末两块），导出 768-D 特征。对比静态 MLP、无门控 GRU、local/contextual/emotion-query 门控。emotion-query 用可学习类查询与前一时刻状态产生类条件模态分布，再边缘化为时间步权重（上下文 K=8）。IEMOCAP 6 类 LOSO；用时间与时间×模态遮挡及 AOPC 做忠实归因。

## 实验与结果
静态 logits MLP Macro-F1/UA≈0.48；无门控 GRU≈0.557；emotion-query 0.5731/0.5734，优于同协议 Transformer/MulT/MMER，且参数约 0.076M。相对静态 mean(F1,UA) 约 +9.01，相对无门控 +1.63。hap/fru/sur 提升更明显。门控轨迹显示文本平均权重最高但各模态 std>0；AOPC 随 top-k 遮挡单调上升。

## 结论
模态重要性非平稳；时间建模是主增益，类条件动态门控再补一小步。MER 宜视为动态决策而非静态融合。未来需更自然对话语料验证。

## 点评
目标明确是证伪“静态模态重要性”，用协议对齐消融 + 扰动归因，比堆 SOTA 更有分析价值。IEMOCAP 部分剧本、干净转写抬高文本权重；未宣称跨数据集 SOTA。
