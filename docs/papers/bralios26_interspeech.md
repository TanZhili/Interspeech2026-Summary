# Elastic Time: Dynamic Frame Rate Bottlenecks for Neural Audio Coding

- 论文编号：3031
- 报告人：Dimitrios Bralios
- 程序：Wednesday 30 September 2026 / Neural Audio Codec Architectures
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bralios26_interspeech.pdf

## 问题
多数神经音频自编码器虽可变码率，但仍固定潜在帧率，对信息密度不均区域均摊时间预算，序列偏长。

## 方法
提出 Elastic Time（ET）：在冻结预训练自编码器上插 Re-Bottleneck；学轻量因果潜在预测器，决定可跳过并稍后重建的帧；推理用贪心边界选择（亦对比精确 DP）。在约 21.5 Hz 基帧率上按保留比例 ρ 做部署期速率控制，跨多域评 mel 距离与 FAD。

## 实验与结果
ρ∈[0.5,0.99] 对应约 10.75–21.29 Hz 平均帧率。贪心与 DP 接近；相对 CodecSlime 等，多数设置效率–质量更好，AudioCaps 上 CodecSlime mel-d 偶有略优。无需外部语义监督即可部署期调速率。

## 结论
内容自适应潜在抽稀可把固定帧率 AE 变成动态帧率，改善长上下文/生成下游的序列效率。

## 点评
把“可变码率”推进到“可变时间分辨率”，对连续潜在尤其关键。插件式设计友好；边界伪影与预测器误差在极低 ρ 时仍需小心。
