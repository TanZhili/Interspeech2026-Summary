# Enhancing BEST-RQ Pseudo-Label Quality Through Online Refinement for Automatic Speech Recognition

- 论文编号：650
- 报告人：Jingjing Xu
- 程序：Monday 28 September 2026 / From Self-Supervised Pre-training to Phonetic Analysis of Speech Models
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/xu26b_interspeech.pdf

## 问题
BEST-RQ 用固定随机投影量化器在线生成伪标签，训练简单，但监督弱于 HuBERT 式迭代精炼：伪标签来自低层 log-Mel、对随机初始化敏感，下游 ASR 仍有提升空间。

## 方法
在保持在线伪标签生成的前提下，对量化器做三项改动：
1. **PCA 投影**：用增量 PCA 替代随机线性降维，约一个 epoch 后冻结主成分。
2. **迭代码本精炼**：按最近邻统计更新码本条目为对应质心。
3. **码本蒸馏**：另增较小码本，用中间层与码本重构特征的时间自相似矩阵差作为蒸馏损失，使伪标签贴近更富语言学信息的中间表征；约训练 30% 后仅在未掩码帧上启用。

预训练：Librispeech 960h、VGG+12 Conformer、掩码预测；微调：1h/10h（Libri-light）与 100h（Librispeech），CTC + 音素目标，4-gram LM 解码。

## 实验与结果
三项叠加在 100h 微调下，test-other WER 从 BEST-RQ 基线 10.1% 到 8.8%（约 12% 相对下降），逐步各约 3–4% 相对增益；1h/10h 上同样持续改善，并优于文中复现的 BiRQ。单码本 + PCA + 迭代精炼可达约 9.2%，与六随机码本相当，而训练时间开销远小于多码本。EMD 分析显示精炼后不同初始化码本分布更接近。蒸馏层消融中中间层（如 {5,6,7}/{6,7,8}）最好。

## 结论
直接改进 BEST-RQ 量化器即可提高伪标签质量与表示学习效果，在极少额外预训练代价下获得明显 ASR 增益。

## 点评
问题抓的是“固定随机量化器的目标质量与初始化方差”，用 PCA + 在线质心更新替代多码本集成，再用时间结构蒸馏补上 HuBERT 式中间层信息，路线比堆码本更省算力。可能脆弱点：增量 PCA 早期停更、蒸馏开启时机与层选择需调；多码本已较稳时再加同类精炼收益变小。
