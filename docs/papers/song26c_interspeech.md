# Segment-wise Embedding based Graph Attention Network for Effective Speech Emotion Recognition

- 论文编号：969
- 报告人：Haoyu Song
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/song26c_interspeech.pdf

## 问题
小规模情绪语料上直接微调大 PTM 易过拟合；话语级 one-hot 标签模糊（多情绪共现、短暂情绪片段），平均/最大池化易稀释；变长序列难做序列到单一标签映射。

## 方法
冻结 HuBERT-large（取第 19 块 1024 维帧特征），其上接 1D Swin-Transformer 段级适配器。后训练：师生 EMA 自蒸馏，联合话语级 KL 一致、块掩码预测（L_MP）与 KoLeo 均匀性正则。微调：把话语切成多段 SSE 作图节点，两层残差 GAT 动态聚合，读出话语向量；损失 CE + 监督对比（SCL）缓解标签歧义。

## 实验与结果
IEMOCAP 5-fold：WA/UA 76.22%/76.84%。MER2023：F1 71.53%，valence MSE 0.9844。作者称相对 SOTA 有显著提升。抽取文本在微调 SCL 公式处附近截断，完整对比表与消融细节部分不可见。

## 结论
段级嵌入图注意力可在变长话语上突出情绪显著段，后训练缓解分布偏移，SCL 提升对模糊标签鲁棒性。边界是依赖强 PTM 与两阶段流程成本。

## 点评
把 SER 当作“稀疏情绪事件检测”而非整句均值分类，用 GAT 替代池化是合理归纳偏置。强处是适配器后训练防过拟合；脆弱处是图全连接对短句可能过度、以及全文截断使相对基线的增益幅度难以逐项核对。
