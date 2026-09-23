# Uncovering Latent Depression Severity for Binary Depression Detection via Advantage-weighting Ranking

- 论文编号：535
- 报告人：Manning Gao
- 程序：Tuesday 29 September 2026 / Multimodal and Non-Speech Healthcare Applications
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gao26d_interspeech.pdf

## 问题
基于音视频的自动抑郁检测（ADD）中，抑郁与非抑郁样本特征高度重叠，点式 BCE 把二者当独立名义类，忽略抑郁严重度的潜在序结构；vlog 数据集又只有二值标签，标准成对损失对所有 pair 均等加权，难以在模糊边界处拉开决策面。

## 方法
双流时间编码：1D Conv 投影 + Seq-TDNN，得到音/视表示后经模态 Transformer，再用 Mutual Transformer（a→v、v→a 与联合自注意力）融合，mean-pool + MLP 输出抑郁分数 s 与概率 p=σ(s)。核心是 Binary Advantage-weighting Ranking (BAR) Loss：由正负分数差构造难度矩阵，对难 pair 做 advantage 加权的 hinge 间隔分离（Lsep），并对类内分数做加权紧致（Lcom），再加概率分布正则（Lreg），总损失为 L_BCE + λ_BAR(Lsep+λ_com Lcom+λ_reg Lreg)。推理在验证集上网格搜索动态阈值 τ* 以最大化 F1。

## 实验与结果
数据：D-vlog（961 条，555 抑郁/406 非抑郁）、LMVD（1823 条，908/915）。Ours 在 LMVD 上 Acc/P/R/F1/Avg 为 76.50/75.00/79.12/77.01/76.91；在 D-vlog 上 F1 77.66、Avg 76.44，整体优于 Bi-LSTM、DepTrans、DepMamba、CAF-Mamba 等；DepMamba 在 D-vlog 上 Recall 略高但 F1 略低。消融：去掉 mutual transformer 或 advantage-weighting 均明显掉点（如 D-vlog Avg 从 76.44 落到 73.38/70.23）。训练中 active hard pairs 从 4184 降到 2463，剩余 hard pairs 平均余弦相似从 0.77 降到 0.57；LMVD 上间隔 m=1.15 最优。

## 结论
BAR Loss 用成对排序与难样本加权，从二值标签中恢复潜在序结构并缓解特征重叠，在野外 vlog 数据上达到或接近 SOTA。局限是目前仅评野外数据，作者计划扩展到 DAIC-WoZ 等临床集以验证域迁移。

## 点评
做法的关键不是再堆一个融合模块，而是把“抑郁程度是连续谱、标签却是二值”写成几何约束：难 pair 驱动间隔、类内方差压缩、再配动态阈值。与常见 BCE/简单 ranking 比，优势在显式打模糊重叠区；风险是超参多（Optuna 搜出的 m、β、λ 等）、依赖验证集调阈值，以及野外自报/志愿者标注与临床标准的鸿沟。
