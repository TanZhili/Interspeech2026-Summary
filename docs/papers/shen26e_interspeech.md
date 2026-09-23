# Adaptive Hard-Pair Sampling via Curriculum Learning for Speech Separation

- 论文编号：3139
- 报告人：Xueliang Zhang
- 程序：Tuesday 29 September 2026 / Source Separation 1
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/shen26e_interspeech.pdf

## 问题
端到端分离在平均 SI-SDR 上已较强，但对音色相近说话人仍易失败；均匀采样使难样本占比过低。既有难例重加权会改有效分布、伤均值，离线难例挖掘又昂贵。需要在线、自适应地加大难说话人对的采样。

## 方法
维护说话人对难度矩阵 D（由分离 SI-SDR 等分数 EMA 更新，并对称化）。每个混合先均匀抽锚说话人，再用温度 Softmax 按 D 抽干扰者：τ 随 epoch 线性衰减，早期近均匀、后期偏难对。仅在中间阶段（Ewarm=20 到 Estop=100）启用；前后仍用标准动态混合。难度更新与采样都在数据层，几乎不增训练开销。在 Libri2Mix 上对 Conv-TasNet、BSRNN、TF-GridNet 做动态混合对比。

## 实验与结果
τ0=20 时：Conv-TasNet 均值 SI-SDRi 保持 16.7 dB；BSRNN 21.0→21.3；TF-GridNet 21.9→22.7。更低初始温度会略伤均值。尾部：低于 10 dB SDRi 的样本数减少（如 TF-GridNet 27→7），bottom 30% 平均 SDRi 上升（Conv-TasNet 12.9→13.2，BSRNN 17.4→17.6，TF-GridNet 18.3→18.8）。难度矩阵可视化显示残差难对逐渐集中到少数说话人簇。

## 结论
课程式难对采样可改善相似音色尾部表现并常保住甚至提升均值，无需改损失或增网络组件；合适初始温度与中间阶段启用是关键。

## 点评
把“难例”落到说话人对矩阵并用温度课程控制，比固定重加权更贴近动态混合管线。强在几乎零开销、可插多种 backbone。脆弱处是难度信号早期不可靠（故需 warmup），且矩阵规模随说话人数平方增长；对超大说话人库可能需要稀疏或聚类近似。
