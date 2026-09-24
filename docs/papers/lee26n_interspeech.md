# DroFiT: A Lightweight Band-Fused Frequency Attention Toward Real-Time UAV Speech Enhancement

- 论文编号：1620
- 报告人：Jeongmin Lee
- 程序：Thursday 1 October 2026 / Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lee26n_interspeech.pdf

## 问题
单麦无人机听觉被宽带准平稳桨叶/电机自噪声淹没；现有 SE 模型过大或 chunk 激活用量过高，难在机载内存与能耗预算内做帧级流式。

## 方法
DroFiT：全带/子带（Mel 式五组）编解码压缩频谱；Pre-TCN 抓准平稳谐波自噪声；频率轴 Transformer 在拼接的全带/子带 token 上做 MHSA 融合；Post-TCN 时域细化后预测复掩码。约 168k 参数，支持增量推理；另有 Linear Attention 的 Lite 与量化变体。VB-DEMAND×实测 DJI Flip 噪声，SNR 至 −30 dB。

## 实验与结果
相对 DCU-net、SMoLnet-T、DTLN、DCCRN，DroFiT 在多 SNR 上 SI-SDR/PESQ/ESTOI 最优或接近最优，算力较 DCU-net、SMoLnet-T 降约 15–26× 与 9–15×。消融去 Pre-TCN/子带/Post-TCN 均掉点；亦含真实外放近机录音评测。

## 结论
时频解耦 + 全/子带频注意力可在极轻量下做无人机 SE 与流式部署。

## 点评
针对桨叶谐波的 Pre-TCN 与“内存友好帧流”约束设计清晰。主结果来自仿真混合；真实机载麦克风与风噪/机动噪声分布可能更难，需看补充真实集表现。
