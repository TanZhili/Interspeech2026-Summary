# DP-BCT: A Dual-Path model for predicting BackChannel Timing

- 论文编号：3216
- 报告人：Jin Yea Jang
- 程序：Tuesday 29 September 2026 / Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jang26b_interspeech.pdf

## 问题
附和时机相对 Backchannel Opportunity Point（BOP）延迟因功能类别而异；单路径多任务可能因快/慢响应分布冲突而互相干扰。

## 方法
在 K-MIND（115h 韩语双人对话）上按 MUMIN 映射 CP/CPU/A/E，并用双过程理论把 CP 归为 fast、其余为 slow。BOP 定义为主说话人持续静音约 200ms。Cox PH 检验类别间 BOP-relative latency。DP-BCT 将 fast/slow 分到双路径做帧级 onset 与类别预测，对比单路径 SP-BCT。

## 实验与结果
Cox：slow 相对 CP 的 HR 0.71–0.85（均 p<.001）；均值延迟 CP 145ms，CPU/A/E 约 295–376ms。DP-BCT Macro-F1 0.6254 vs SP-BCT 0.4862（+0.1392，相对约 +28.6%）。

## 结论
功能类别确有不同 BOP 相对延迟；结构上拆开快/慢路径可显著提升附和时机与类别预测。

## 点评
用生存分析把“何时插话”量化，再把归纳偏置写进双路径，动机清晰。DPT 分组是解释性代理而非认知测量；静音定义的 BOP 可能漏掉非停顿型附和机会。
