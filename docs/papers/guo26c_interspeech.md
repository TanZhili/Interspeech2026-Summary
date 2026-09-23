# Adaptive Federated Fine-Tuning of Self-Supervised Speech Representations

- 论文编号：2122
- 报告人：Xin Guo
- 程序：Wednesday 30 September 2026 / Self-supervised Speech Representation Learning
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/guo26c_interspeech.pdf

## 问题
联邦学习下微调 SSL 语音模型时，客户端算力差异会造成掉队，而不同下游任务所需表示深度也不同；全模型统一更新既低效又难在弱设备上跑通。

## 方法
以 Wav2Vec 2.0 Base 为骨干，在 Transformer 第 3/6/9/12 层挂早期出口预测头。客户端按本地资源与任务复杂度选最大训练深度 `L_max`，只前向/反向到该层。服务器做层向、深度加权的部分聚合：仅对训练过该层的客户端加权平均（权重含本地数据量与深度），使浅层由更多客户端更新、深层由高资源客户端精炼。

## 实验与结果
在 SUPERB 式五任务（KWS、ASR、ER、SID、ASV）上评测。同构联邦与集中式均显示最优出口因任务而异（如 ASR 偏好第 9 层，KWS 常偏好第 6 层）。异构深度设定下，层向部分聚合优于普通 FedAvg，部分任务甚至超过同构最优深度联邦（如 ASR test-clean 8.79 vs FedAvg 9.21；SID 15.30 vs 17.50）。深度从 12 降到 3 层可显著降低客户端显存（如 KWS 约 −43%）。

## 结论
早期出口 + 深度感知部分聚合可在异构联邦中协同训练 SSL 语音模型，兼顾效率与性能，并缓解掉队。

## 点评
抓住的是联邦里“设备异构 × 任务所需深度不同”的交叉约束，用弹性深度比单纯压缩参数更贴合 SSL 层级结构。脆弱点在于出口集合与任务最优深度仍需经验配置，ASV 依赖 SID 全局模型间接评估，真实边缘端通信/能耗未充分展开。
