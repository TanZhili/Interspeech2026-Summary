# Multilingual and Cross-lingual Lexical Stress Detection Using SSL Feature Vectors

- 论文编号：2914
- 报告人：Abdulrahman Alhabshi
- 程序：Monday 28 September 2026 / Tools and Techniques for Phonetic Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/alhabshi26_interspeech.pdf

## 问题
词重音对可懂度重要，但阿语与英语实现不同，多语与跨语检测困难。需检验固定 SSL 特征 + 轻量分类器在单语、联合多语与跨语迁移上的表现差异。

## 方法
冻结 SSL 编码器（HuBERT、WavLM、XLS-R）提特征；两阶段分类：**音节级 Pre-net（DNN）** + **词内音节依赖 Post-net（TDNN）**。比较单语、阿–英联合多语、双向跨语迁移。

## 实验与结果
- 多语训练接近单语：英约 **97%**、阿约 **90%**（摘要）；实测多语均值阿 87.87%、英 95.24%；最高如 HuBERT Post-net 英 **97.08%**、WavLM Post-net 阿 **89.77%**。单语基准约英 97.49%、阿 90.56%，优于先前约 91%/82%。
- Post-net 相对 Pre-net 有稳定小幅增益。
- 跨语明显下降且方向不对称：英→阿均值约 **68%**（最佳 XLS-R Post-net 79.17%）；阿→英约 **76%**（最佳 86.69%）。跨语时多语预训练的 XLS-R + Post-net 最稳。

## 结论
SSL 特征支撑高准确阿/英重音检测；联合多语几乎不损单语，跨语则依赖方向与时序建模；Post-net 与多语预训练有助于迁移。

## 点评
把重音检测做成可控的训练体制对比，突出类型学差异（阿语量敏感 vs 英语元音弱化）解释迁移不对称。强在三编码器×两阶段网格；跨语仍远低于单语，说明“共享韵律特征”不能替代目标语音系约束。
