# Learning Self-Supervised Spatial Representations via Soft Acoustic Contrastive Alignment

- 论文编号：641
- 报告人：Yotam Silverman
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/silverman26_interspeech.pdf

## 问题
多数音频 SSL 面向单通道频谱语义，对 TDOA、T60、DRR 等空间参数估计不够；标注空间信息昂贵，增强式对比又易破坏细微空间 cue。

## 方法
双流 MC-Conformer（空间/频谱编码器 + 解码器）在未标注双耳数据上做 CCSR 式掩码重建；对空间编码器投影 z 施加 Soft Acoustic Contrastive（SAC）损失：用 GCC-PHAT 估计的 TDOA、GCC 峰幅与三频段相干性构成特征 c，高斯核软权重对齐 batch 内潜空间相似度。下游只保留空间编码器 + 线性头，线性评估与全微调。

## 实验与结果
WSJ×仿真 RIR 预训练 50k；下游未见房间上五任务 MAE。Linear Eval 下 CCSR+LSAC：TDOA 1.06、T60 0.113、DRR 1.86、C50 0.998、ABS 0.067，优于 CCSR 基线；Fine-Tune 下 TDOA 0.288、T60 0.075 等亦最好或接近最好。t-SNE 显示 TDOA 等结构更清晰。

## 结论
把信号处理先验写入软对比目标可改善空间参数表示；局限在仿真数据，极端低 SNR 下 GCC 等特征不可靠可能削弱 SAC。

## 点评
不依赖房间元数据、用可解析声学特征做连续正样本权重，比硬增强对比更贴回归任务。与掩码重建可叠加是工程优点；真实混响与噪声下特征质量决定上限，需实地验证。
