# Learning to Attend to Depression-Related Patterns: An Adaptive Cross-Modal Gating Network for Depression Detection

- 论文编号：1075
- 报告人：Hangbin Yu
- 程序：Wednesday 30 September 2026 / Pathological Speech Assessment 3
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yu26c_interspeech.pdf

## 问题
抑郁相关声学/文本线索稀疏、局部出现；多数方法对整段均匀池化，假设各帧同等重要，易淹没诊断性片段。

## 方法
双分支：冻结 HuBERT（第 12 层）取声学帧特征；WeNet ASR 转写后用指令感知 Qwen-Embedding-0.6B 取文本 token。ACMG 用掩码均值池化得全局上下文，跨模态（或单模态）拼接后经 sigmoid 产生帧/token 门控权重，逐元素重加权；再经各模态 Transformer，拼接送 MLP 预测严重度。

## 实验与结果
PDCD2025（三分类 Healthy/Mild/Moderate，5-fold）：最优 Cross-modal ACMG + Qwen 平均 Acc 81.25%（相对无 ACMG 的 Transformer(Qwen) +1.47；相对 RoBERTa 基线更高）。DAIC-WOZ 开发集 F1 69.39（相对无门控 64.38）。声学门控与能量负相关（整体 −0.329）；文本门控抬高负向情感等词。

## 结论
自适应跨模态门控能突出低能量停顿等与负向文本线索，提升抑郁检测；未来可探索其他门控权重计算方式。

## 点评
直接针对“稀疏诊断线索”设计门控，可视化与能量相关分析增强可解释性。转写质量与指令嵌入选择影响上限；DAIC 仅报开发集，跨语/场景泛化仍待看。
