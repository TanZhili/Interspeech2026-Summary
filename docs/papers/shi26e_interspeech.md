# Leveraging Modality-Specific Label Distributions for Enhanced Multimodal Emotion Recognition

- 论文编号：2076
- 报告人：Xiaohan Shi
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shi26e_interspeech.pdf

## 问题
多模态情绪识别（MER）多设计复杂融合，却常用统一多模态标签，忽略各模态自身标签分布；EmotionTalk 上仅 24.5% 样本三模态标签完全一致，跨模态情绪倾向差异被浪费。

## 方法
提出 MoLD：HuBERT/RoBERTa/DINOv2 提特征后经 Mamba 精炼；各模态经池化+FC 预测模态特异标签分布 E⋆_m；Cross-Modality Fusion 用两次交叉注意力聚合另两模态得 H^(fus)_m，再与 E⋆_m 拼接。三模态表征拼接后分类。损失：CE + 各模态 KL（分布学习）+ InfoNCE 模态相似损失，权重为可学 softmax。

## 实验与结果
EmotionTalk 七类。多模态 MoLD UAR/F1 58.96%/59.67%，超 Cross-Attention（56.05/57.25）与 MLP（54.08/53.66）。消融去 LD/MS/CMF 均掉点。单模态设定下语音/文本/视频亦优于 MLP。Oracle 分布上界约 66.56% UAR。

## 结论
显式建模模态特异标签分布并约束跨模态一致性，可同时提升单模与多模 MER。边界依赖提供模态级标签的语料。

## 点评
抓住“统一标签掩盖模态分歧”这一数据事实，把 LDL 从单模扩展到跨模交互。强处是分析与消融清晰；脆弱处是视频编码器冻结、中文语料特定，以及分布标签质量决定上限。
