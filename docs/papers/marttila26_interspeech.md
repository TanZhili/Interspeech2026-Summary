# Differentiable Pitch Matching with Auditory Models

- 论文编号：2043
- 报告人：David Marttila
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/marttila26_interspeech.pdf

## 问题
DDSP 合成常用 MSS 损失，但对频率参数梯度振荡，迫使依赖外部 f0 估计器；谱域损失（含 SOT）在缺失基频等“感知音高≠谱峰”时仍易失效。

## 方法
用可微 CARFAC 听觉模型得多通道活动；帧级构造稳定听觉像（SAI，ACF 或 TTI）、耳蜗图与音高图；对音高图做音色归一（按耳蜗能量去加重）后，用 1-Wasserstein + L1 定义听觉音高距离 L_APD。在纯音匹配任务上对目标（正弦、缺失基频谐波、方波、真唱元音）用梯度下降估频率，报告粗/细梯度方向正确率（CGA/FGA）与最小损失到真音高的音分误差。

## 实验与结果
TTI-2048 在多数目标上 CGA 最高（如 160 Hz 正弦 94.3%，缺失基频 95.8%），细尺度亦强；相对 OrigMSS/SOT 在缺失基频与复杂音色上更不易陷到远离真音高的极小。部分设定仍有数百音分偏差。

## 结论
基于听觉模型的可微音高距离可为频率参数提供更信息丰富的梯度，朝摆脱外部 f0 估计器的端到端 DDSP 迈进一步。边界是合成匹配任务、非完整训练管线。

## 点评
用缺失基频等感知用例打穿“谱=音高”假设，音色归一是关键工程点。强处是梯度方向指标设计清楚；脆弱处是计算贵、真唱元音仍难，且尚未嵌入完整 DDSP 训练证明端到端收益。
