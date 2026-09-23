# Multi-Loss Learning for Speech Emotion Recognition with Energy-Adaptive Mixup and Frame-Level Attention

- 论文编号：1219
- 报告人：Yizhong Geng
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26u_interspeech.pdf

## 问题
SER 受情绪复杂与标注稀缺制约；既有 mixup（如 LAM）均匀混合片段、忽略能量动态，可能漏掉与情绪相关的能量线索；简单池化也难突出多帧关键线索。

## 方法
Energy-Adaptive Mixup（EAM）：随机截取短于半长的片段，把干扰段按 SNR∈[−5,10] dB 缩放能量后叠加主段，用能量与时长比构造软标签 λ_mix。特征走预训练 WavLM→CNN/Transformer。Frame-Level Attention Module（FLAM）：多头自注意力后可学习向量加权池化得话语向量。Multi-loss：KL（对齐软标签）+ Focal + Center + 帧级 Context Broadcasting 后的 SupCon，加权求和。说话人/会话独立交叉验证。

## 实验与结果
IEMOCAP：WA/UA 78.47%/79.14%，超 LAM（75.37/76.04）及若干多模态方法。MSP-IMPROV：58.55%/58.34%。RAVDESS：93.40%/92.28%。SAVEE 说话人均 UA 72.3%。消融显示 EAM、FLAM 与各损失逐步抬升；t-SNE 显示 MLL 后类簇更清晰。

## 结论
能量感知混合、帧级注意力与多损失协同可显著提升跨自发/表演数据的 SER，并增强特征可分性。作者称在四个数据集上均超既有 SOTA。

## 点评
相对“只换骨干”，本文把数据增强物理化（SNR 能量）并与软标签、对比/中心损失对齐。强处是四数据集与细消融；脆弱处是超参与损失权重经验设定多、表演集（RAVDESS）高分可能夸大可迁移性，以及 WavLM 冻结/微调细节需读者自行注意域偏移。
