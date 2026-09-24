# How Frequency Band Importance Affects Neural Network Predictions and Human Perception for Speech Quality Assessment

- 论文编号：2382
- 报告人：Ada Lamba
- 程序：Thursday 1 October 2026 / Benchmarking Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lamba26_interspeech.pdf

## 问题
自动语音质量评估网络预测常与人类 MOS 相关不佳；需要弄清网络依赖哪些频带，以及人类是否对相同因素敏感，以解释人机不一致。

## 方法
对 MOSNet（CNN）、DNSMOS（CNN）、SCOREQ（wav2vec2 变体）用 SHAP、偏依赖图（PDP）与频带扰动（功率缩放 0.25–1000）分析 161 个 50 Hz 频带。评测集为未见训练数据的 IUCOSINE（100 条，MOS 分布匹配）。另做 IRB 听感实验：200 人英语流利受试者，对原声与单频带扰动对做质量分与偏好，并报告噪声量、语噪比、失真、噪声类型等因素影响。关注基频区、辅音/元音重要带，以及各模型 SHAP 幅度最大的经验带。

## 实验与结果
IUCOSINE 上 SCOREQ LCC/SRCC 约 0.63，DNSMOS/MOSNet 相关更低（约 0.19–0.23）。SHAP：三模型均更依赖低频带（约 <band 40）；MOSNet 高频几乎无影响，DNSMOS 高频多为负贡献。摘要：网络与人都对有害因素比有益因素更敏感，且网络关注输入中较小部分对应低频。正文在 PDP/扰动与听感结果中段截断，完整人机对照数字未全部可读。

## 结论
作者认为这是迈向统一人与网络可解释性的一步：若决策依赖频带不同，人机相关差可能来自决策机制差异而非单纯工程参数。

## 点评
多模型×多解释方法×听感对照的设计少见，直接针对质量评估人机失配。低频偏置与语音感知文献方向一致；SCOREQ 相关更高是否因其表示更宽频仍待结果段补全后核实。抽取截断限制了对扰动曲线与听感结论的定量复述。
