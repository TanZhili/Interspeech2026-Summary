# Breaking Shortcut Learning for Cross-Trial EEG-Guided Target Speech Extraction via Two-Stage Training

- 论文编号：595
- 报告人：Wonchul Shin
- 程序：Wednesday 30 September 2026 / Clinical and Inclusive Speech Technology
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shin26_interspeech.pdf

## 问题
端到端 EEG 引导目标语音提取（TSE）在 within-trial 上 SI-SDR、attended-source accuracy 很高，但严格 cross-trial 时会崩塌。原因是 trial 内注意目标固定，模型可把 trial 特异 EEG 结构当“捷径”映射到目标说话人，而非学到与语音对齐的注意相关表征。

## 方法
提出 TRUST-TSE 两阶段框架。(1) Stage 1：对比预训练 EEG 编码器，将 EEG 段与对应 attended 语音的 mel 嵌入对齐；关键是 attended-speaker negative sampling——负样本取自同一 attended 说话人的其他非对齐段，使 trial 身份线索对对比损失无用。(2) Stage 2：冻结 EEG 编码器，用其嵌入条件化提取器；损失为基于 EEG–source 相似度差的 confidence-weighted SI-SDR（权重 \(w=\tanh(\kappa\Delta)\)），强调 EEG 对 attended/ignored 区分清晰的样本。诊断实验含 NeuroHeed 线性探针测 trial 可解码性，以及 test-time EEG shuffle、trial-wise EEG–audio permutation 等 mismatch 压力测试。

## 实验与结果
在 KUL 上，NeuroHeed within-trial 中位准确率近 90%，cross-trial 低于 chance，且常出现强负 SI-SDR。线性探针 8-way trial 分类准确率约 55–76%（远高于 12.5% chance）。两种 mismatch 压力测试下 within-trial SI-SDR/准确率几乎不变（约 12 dB / 87%），表明高分可不依赖段级 EEG–语音对齐。全文抽取在 Stage 1 负采样细节与完整对比表处截断，KUL/DTU 上 TRUST-TSE 相对端到端基线的完整数字未完整读到；摘要称其在严格 cross-trial 协议下优于端到端基线。

## 结论
作者认为 within-trial 高分常由 trial 捷径驱动，两阶段对比预训练加置信加权提取是提升 trial 鲁棒性的可行路径；TRUST-TSE 作为起点，代码已公开。

## 点评
问题诊断扎实：探针 + mismatch 实验把“高 within-trial ≠ 真正注意跟踪”说得很清楚。两阶段把表征学习与提取解耦，负采样设计直接针对 trial 身份捷径。全文在方法后半与主实验结果处被截断，点评无法核对 DTU/消融的具体增益；若完整结果与摘要一致，价值在评价协议与训练范式，而非单纯刷 within-trial 数字。
