# Multi-View Based Audio Visual Target Speaker Extraction

- 论文编号：2035
- 报告人：Peijun Yang
- 程序：Tuesday 29 September 2026 / Target Speaker Extraction, Speech Separation and Audio Understanding
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yang26m_interspeech.pdf

## 问题
多数 AV-TSE 默认正面脸视频，真实场景常为侧脸/俯仰视角，正面化可能丢信息；多视角同步数据若只在训练时可用，如何把跨视角相关转成单视角测试增益仍不明确。

## 方法
MVTF-GridNet：唇编码器提各视角嵌入，线性插值对齐音频帧，LSTM 后做成对外积（带常数 1）建模乘性交互，再 Flatten+LayerNorm+Linear 并平均得融合视觉上下文，送入 TF-GridNet。训练可用随机三视角；推理缺视角则复制现有视角填满。损失 SI-SDR。

## 实验与结果
MEAD 中性情感、7 视角、两说话人混合（SNR −10–10 dB）。随机三视角训练的 MVTF 单视角平均 SI-SDR 15.718，优于仅正面 MVTF（14.102）与随机单视角 GridNet（15.089）；混合视角旋转测试上 MVTF 15.834，正面 GridNet 仅 10.425。多视角推理组合 SI-SDR 约 15.85。外积融合优于投影相加与注意力融合；相对 PIAVE 平均 SDR 约 10.81 vs 8.18（设定不完全严格可比）。

## 结论
训练期显式建模多视角乘性交互，可在单视角甚至头部转动混合视角测试下提升鲁棒性，且参数/算力增幅很小。

## 点评
把“姿态变化”从要矫正的噪声改成可学习的互补发音信息，外积融合比简单加和更贴合跨视角相关。强在训练–测试视角不对称仍有效；数据限于 MEAD 中性情感与固定相机几何，开放场景姿态连续变化需再验证。
