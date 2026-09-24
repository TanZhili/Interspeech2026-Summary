# Disentangling Reasoning in Large Audio-Language Models for Ambiguous Emotion Prediction

- 论文编号：2031
- 报告人：Jiaheng Dong
- 程序：Thursday 1 October 2026 / Speech Emotion Recognition and Representation 3
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yu26f_interspeech.pdf

## 问题
SER 常压成单一标签，忽略情感模糊性；LALM 虽能生成更丰富输出，但对模糊情感的分布式推理仍弱，且常见 CoT/RL 后训练面向“唯一正确答案”任务，易坍缩到确定性解释。

## 方法
把模糊情感识别重写为分布推理：用多标注者投票得到软标签 p^GT，并用 GPT-4o 按 Keywords→文本分析→音频分析→综合 协议生成 ambiguity-aware CoT。在 Qwen2-Audio-7B-Instruct 上以 LoRA 接入：KL 对齐预测情感分布与软标签；SFT/DPO/GRPO（及注入金标轨迹的 GRPOz）均可插拔该目标。分布从情感词 token logit 的 softmax 读出。

## 实验与结果
IEMOCAP（5-fold LOSO）与 CREMA-D。指标 JS↓、BC↑、R²↑、Brier↓。IEMOCAP 上 GRPOz 最佳（JS 0.20、BC 0.82）；CREMA-D 上 DPO 最佳（JS 0.17、BC 0.86）。相对 Base/Audio-Reasoner 一致提升。消融：KL 优于仅 CE；跨域时 CoT 对泛化帮助更大。

## 结论
作者认为分布对齐与结构化 CoT 可拆开决策层不确定性与推理增强，并在多种后训练策略上有效；未来可扩展更广任务与模型。

## 点评
把“模糊情感”正式做成软标签+推理轨迹，比单标签 SER 更贴人感知。CoT 依赖闭源模型合成，轨迹质量与成本是隐患；不同数据集上 DPO/GRPOz 谁更强与类别维度有关，说明后训练选择不能一刀切。
