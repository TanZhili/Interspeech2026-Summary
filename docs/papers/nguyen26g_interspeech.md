# Domain-Aware Mispronunciation Detection and Diagnosis Using Language-Specific Statistical Graphs

- 论文编号：3239
- 报告人：Hanh Nguyen
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/nguyen26g_interspeech.pdf

## 问题
MDD 中不同 L1 学习者的音素替换模式系统不同；仅用发音学类别构图（同类全连接、无向、等权）无法刻画跨类混淆、稀有同组替换与方向性错误。

## 方法
从训练数据统计定向替换频率，为每个 L1 建有向加权音素混淆图（边权为条件概率，排除正确发音）。MDD-LSSG：wav2vec2-large-xlsr-53 声学编码器 + 按 batch 的 L1 选图，共享参数 GCN 生成 L1 相关音素嵌入；规范音素序列查表得语言侧表示，与声学做 cross-attention 后 CTC 预测。在 L2-ARCTIC 上按说话人划分训练/测试。

## 实验与结果
检测 F1 59.52%，高于 L1-aware Aux/Look-up Embed（56.41/56.83）、MDDGCN（56.49）、CAT-GCN-MDD（58.24）。诊断 DER 20.88，与强基线接近。多数 L1 上 F1 最优；西班牙语 t-SNE 显示统计图把 /d/-/dh/、/t/-/th/ 等跨类高频混淆对拉近，而类别图仍按类别簇分离。

## 结论
用数据驱动的 L1 特定统计混淆图注入语言分支，比类别先验图与简单 L1 条件嵌入更能提升 MDD 检测，并改善音素嵌入几何。

## 点评
把“谁容易把谁错成谁”做成有向图先验，比扁平 L1 ID 更结构化。图依赖训练集替换统计，小 L1 或未见错误模式会偏；与声学侧融合仍是经典 cross-attn+CTC，增益主要来自语言先验质量。
