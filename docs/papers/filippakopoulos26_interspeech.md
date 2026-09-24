# Segregate, Refine, Integrate: Decomposing Multimodal Fusion for Sentiment Analysis

- 论文编号：1299
- 报告人：Alexandros Potamianos
- 程序：Thursday 1 October 2026 / Emotion, Prosody, and Articulation
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/filippakopoulos26_interspeech.pdf

## 问题
多模态情感分析需同时精炼单模态表征并建模跨模态交互，二者常被缠在同一融合操作里；DeepMLF 等用可学习 fusion token，但 token 池未区分模态，交互拓扑缺少结构性约束。

## 方法
提出 SeRIn（Segregate, Refine, Integrate）：在冻结预训练 LM 上，将 fusion token 分成 audio / visual / audiovisual 三组；用无参数的模态约束注意力掩码隔离单模态通路，AV 通路只读不写；MM Block 内以 Internally Gated Cross-Attention（IGCA）注入对应编码器上下文，再以模态约束 IGSA 巩固；仅在最终 Integration Head 解除隔离做全交互。AV Encoder 与 DeepMLF 对齐并固定，以隔离“交互拓扑”这一变量。

## 实验与结果
摘要称在 CH-SIMS 与 CMU-MOSEI 上相对已有方法达到 SOTA、各项指标均提升；消融显示收益来自结构化交互而非额外容量；视觉损坏下门控出现无监督的模态重加权。全文抽取在 MM Block / IGSA 公式中途截断，表格与具体数值未见。

## 结论
作者认为将单模态精炼与跨模态整合在架构上分阶段，比仅靠优化惩罚更能保证模态特化；交互拓扑应与深度、容量并列为融合设计轴。

## 点评
用掩码固定“何时混、何时不混”，比软正交损失更可解释。全文后半（完整实验与门控分析）缺失，SOTA 数字无法从可读写正文核对；依赖 DeepMLF 式冻结 LM + fusion token，适用范围主要在该范式内。
