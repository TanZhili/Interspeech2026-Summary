# Bridging the Distribution Gap in Real-World Far-Field Speech Enhancement via Lightweight Latent Representation Alignment

- 论文编号：3478
- 报告人：Biao Liu
- 程序：Thursday 1 October 2026 / SE Architectures, Adaptation and Audio Front-Ends
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/liu26s_interspeech.pdf

## 问题
真实远场相对近场干净语音存在严重中高频衰减与传播特性差异，仿真 RIR 训练易失配；轻量单阶段网络直接学复杂映射往往不足，大模型又算力过高。

## 方法
采集约 70 小时同步近场–远场配对（AISHELL-3 内容，10 场景，4/6/8 m）。两阶段轻量框架：冻结预训练 GTCRN 做粗去噪/去混响；DAC 式编码器学干净近场潜空间，轻量 ConvNeXt 映射网络把粗增强信号投到该潜空间，再解码重建。分阶段训练：先联合训 AE+映射，再冻编码器微调映射与解码器。对齐损失为潜空间 MSE，AE 用多尺度 Mel + 对抗。

## 实验与结果
真实远场测试集：Proposed 约 10.38 M / 0.8 GMAC/s，P.835 OVRL 2.94、SIG 3.23、BAK 4.01、P.808 3.35，优于在仿真或真实数据上训的 GTCRN、LiSenNet、因果 TF-GridNet。轻量基线直接用真实数据训练未必提升，说明难映射问题需对齐分解。

## 结论
粗增强 + 干净潜空间对齐可在低算力下缩小仿真–真实远场分布差，提升感知质量。

## 点评
把难题拆成“先抑噪再对齐近场流形”，对设备端远场很务实；自建配对数据是关键资产。映射依赖近场参考训练，无配对场景需另寻无监督对齐。
