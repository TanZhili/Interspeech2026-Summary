# HARP: Harmonic-Aware Residual Partitioning for Neural Audio Codecs

- 论文编号：1759
- 报告人：Qiaoyu Yang
- 程序：Tuesday 29 September 2026 / Audio Coding and Signal Analysis
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yang26k_interspeech.pdf

## 问题
标准 RVQ 各阶段频谱纠缠：截断码本时高低频内容被不可预测地去掉，码率缩放不平滑。并行分带编码虽让频带特化，但碎片化潜空间、丢失跨频相干（谐波相位/幅度关系）。需要一种在单一 encoder–decoder 与统一 token 流内施加频率层级、同时保留谐波上下文的训练策略。

## 方法
HARP 只改训练损失，推理与标准 RVQ 相同。将 L=9 个 RVQ 阶段分为 K=4 组（默认 3-2-2-2）：Bass 0–1 kHz、Low-mid 1–4 kHz、High-mid 4–10 kHz、Treble 10–22 kHz。Cumulative decoding：每组用截至该组的累积量化潜变量解码，使高频组在低频已重建的上下文中学习。Subband contribution supervision：对各组波形增量（经 stop-gradient 隔离先前组梯度）做频带加权 mel 重建损失。Soft band weighting：可学习高斯中心/带宽加权 mel 箱，加固定地板 β 避免硬截断伪影。标准重建、对抗与 commitment 损失仍作用于最终输出。

## 实验与结果
摘要称在语音、音乐与通用音频上优于标准 RVQ 与并行分带，并在两种码率条件的 MUSHRA 上有感知提升；预训练模型与脚本公开。抽取全文在 soft band weighting 公式处截断，客观指标表与听测具体分数未出现在全文文件中。

## 结论
作者认为仅通过训练期累积解码与软分带监督，即可在标准 RVQ 架构内形成低频优先的频率层级，使丢弃后期阶段时先丢高频、质量更平滑，并保留谐波相干。

## 点评
思路抓住 RVQ“频谱无结构”与并行分带“有结构但丢跨带上下文”的互补缺陷，用训练目标而非新架构解决，部署成本为零，这对 token 流要接 LM 的场景很实用。正文实验段抽取不完整，具体增益与失败样本类型无法从文本核验；软目标是否在噪声/非谐和内容上仍稳定特化，是自然的脆弱点。
