# ArtNet: A JEPA-Like Articulatory Predictive Framework for Robust Zero-Shot Phoneme Recognition

- 论文编号：304
- 报告人：Yaqian Zhou
- 程序：Monday 28 September 2026 / Tools and Techniques for Phonetic Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/hu26_interspeech.pdf

## 问题
零样本跨语音素识别中，直接声学→音素映射脆弱：未见语言上替换错误占主导（文中宏观约 84.7% PER 来自 substitution），且大量替换源于已学音素表征不稳而非仅未见音素。

## 方法
**ArtNet**（类 JEPA）：在 SSL 特征上预测结构化 **发音特征**，而非直接符号；**VIB** 抑制语言特异变异。推理配合 **VSIA（vector-space inventory alignment）** 做音素清单对齐。比较 TDNN 等 ArtNet 变体；源语言训练、七种未见语言零样本测 PER / PFER（音素特征错误率）。

## 实验与结果
Table 1（节选）：ArtNet+VSIA 平均 PER **45.54%**（ArtNet 单独 54.94；基线更高），相对竞争基线约 **20.56% 相对 PER 下降**、**7.01% 相对 PFER 下降**；部分语言绝对 PER 降幅约 28 点量级。

## 结论
以发音特征预测为桥梁可增强跨语声学鲁棒性；与清单向量对齐结合后，零样本音素识别显著优于直接映射基线。

## 点评
把 JEPA“预测结构化表征”迁到发音特征空间，针对替换错误主导的诊断对症。强在 PER/PFER 双指标与多语零样本；脆弱在发音特征定义与清单映射质量——VSIA 增益大，说明仅预测仍不够，还需目标音系几何对齐。
