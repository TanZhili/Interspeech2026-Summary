# Sleep Sound Event Detection Powered by Learnable Multi-Resolution Adaptive Line Enhancer

- 论文编号：130
- 报告人：Chanwoo Park
- 程序：Tuesday 29 September 2026 / Audio Coding and Signal Analysis
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/park26_interspeech.pdf

## 问题
阻塞性睡眠呼吸暂停（OSA）常规 PSG 成本高、不便筛查；麦克风事件检测是潜在低成本替代。传统 Adaptive Line Enhancer（ALE）多只作预处理，滤出的增强谱送入网络，而自适应滤波内部的逐帧置信度图被丢弃。需要把 ALE 内部状态真正注入 SED 注意力与特征调制，以更好区分鼾声、低通气与阻塞性呼吸暂停并支持 AHI 估计。

## 方法
提出 ACF-SED。Multi-Resolution ALE Bank（MRAB）在共享 STFT 上并行三个可学习步长的 NLMS 滤波器，decorrelation delay/长度分别为 (τ,L)=(1,8)、(3,15)、(6,24)，输出事件/噪声分量与置信度图 Ci=|E|²/(|E|²+|Z|²)。双流 CNN 分别编码增强 mel 与噪声 mel；Learnable Confidence Pooler 在分辨率与频率轴上加权得到标量置信轨迹 c。Confidence-Guided Cross-Path（CCP）中事件路径用 Symmetric Confidence-Biased MHA 与 ALE-Aware Feature Modulation，噪声路径为轻量 FFN，再经门控交叉注意力融合；MLP+sigmoid 输出三类帧级概率（snore、hypopnea、obstructive apnea）。

## 实验与结果
摘要称在 Audio-Polygraphy Dataset for Sleep Apnea Analysis（APSAA）上 Event-F1、Segment-F1、PSDS 达 SOTA，并支持端到端 AHI 估计。抽取全文在 CCP 模块描述中部截断，具体对比数字与消融未保留。

## 结论
作者认为把多分辨率 ALE 置信度直接注入 Transformer 注意力与特征调制，可把经典自适应滤波状态变成 SED 的可学归纳偏置，从而提升睡眠呼吸事件检测并服务 AHI 筛查。

## 点评
设计点在于“ALE 不只是前端滤波，而是把周期性/非周期性置信度当作注意力偏置”，对医院谐波噪声与伪周期鼾声这类场景有明确物理动机。正文结果段缺失，SOTA 声明无法用数字核实；三类事件边界模糊与仅音频估计 AHI（缺真实睡眠时间）仍是临床落地的主要风险。
