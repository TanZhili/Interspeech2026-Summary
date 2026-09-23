# Latency Controllable Speech Enhancement

- 论文编号：2997
- 报告人：Hiroshi Sato
- 程序：Tuesday 29 September 2026 / Real-Time, Low-Latency and Edge Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/sato26_interspeech.pdf

## 问题
应用延迟预算从助听的数毫秒到电话/离线的数百毫秒不等；多数增强模型只训一个固定 lookahead，多预算就要存多套全模型。需要单系统可切换延迟并尽量共享参数。

## 方法
在因果 Conv-TasNet 骨干上插入 Lookahead Module（LAM）：堆叠膨胀 depthwise 1-D 卷积，通过因果/非因果块的二进制模式控制 lookahead 帧数。Latency Control Adapter（LCA）为每个延迟预算备一个 LAM 适配器，推理时切换；可跨适配器共享因果块与非因果块参数。Intra-batch multi-latency training：同一 batch 过全部 K 个适配器并平均损失。标准设定 τenc=20 ms，K=7，总延迟约 20–650 ms；另测 τenc=5 ms 超低延迟设定。

## 实验与结果
LibriSpeech+DNS4 噪声：LCA 相对为每延迟训整模的多模型基线，多数点 SDR/DNSMOS 更高（标准设定平均约 +0.13 dB SDR；超低延迟设定平均约 +0.53 dB）。存参：七模型共 104.1M → LCA 共享 16.5M / 不共享 24.5M（约降 76%），推理 MACs 与单 LAM 相同（1.46 G/s）。消融：冻结骨干只训适配器、去掉因果块结构、或每 batch 只随机选一个适配器都会掉点。即使最终只用最低延迟，联合训仍可相对纯因果提升（如 5 ms 设定 +0.45 dB SDR）。

## 结论
LCA 实现运行时可切换的多延迟增强：共享骨干、只换轻量适配器，在恒定推理算力下减少存储并常优于分模型训练。

## 点评
与“每延迟重训整网/改 padding”不同，这篇强调部署侧一模型多模式与跨延迟蒸馏。Intra-batch 联合损失是增益来源。代价是训练算力随 K 线性放大；适配器插入位置与 lookahead 离散集合仍需先验设计。
