# Accurate Source-Free Speech Classification via Meta-Learned Target-Centric Model Merging

- 论文编号：371
- 报告人：Ka Hyun Park
- 程序：Thursday 1 October 2026 / New Training Methods for ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/park26b_interspeech.pdf

## 问题
无源域数据、仅有多个预训练源分类器与少量目标标注时，如何适配未见目标域；常规迁移/数据选择不可用，现有模型合并易在少样本目标上过拟合。

## 方法
提出 MOCHEE：冻结 wav2vec2 等共享嵌入，只合并各源 MLP 分类头。用 Sinkhorn 软置换矩阵对齐隐单元（消除置换对称性），再学源权重 α 做对齐参数空间加权平均。α 不直接拟合目标训练集，而用 meta-reweighting：内环在目标 train 上虚更新置换参数 p，外环用目标 val 损失对 α 取元梯度（非负后 softmax）。源参数本身不更新。

## 实验与结果
CAMEO 情感跨语料：源 CREMA-D/SubESCO/RAVDESS/MESD，目标 CAFÉ、Oréau（六类情绪）。MOCHEE 在 CAFÉ Acc/Macro-F1 50.85/49.40，Oréau 35.30/34.85，优于 Uniform、Greedy Soup、Re-basin、TIES 等；相对最差基线 Macro-F1 可高约 14.5 点。即便基线再在目标上微调，MOCHEE（不微调）仍最好。消融：去置换对齐掉点大；去 α 学习也一致变差。权重演化显示目标英源时逐步抬高英语源 CREMA-D。

## 结论
在源自由、少目标标签设定下，对齐 + 元学习源重要性的目标中心合并，可比启发式合并更好泛化到未见目标样本。

## 点评
抓住“能共享模型不能共享数据”的现实约束，把合并权重当元学习对象而非验证集挑模型。软置换让异构训练头可平均；内环改 p 而非 θ 保留合并效率。局限在分类头合并与共享冻结前端假设，且效果依赖目标 train/val 划分质量。
