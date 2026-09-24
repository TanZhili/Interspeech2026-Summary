# Balancing Speech Reconstruction and Noise Suppression Using Dual-Asymmetric Loss

- 论文编号：794
- 报告人：Merlin Carson
- 程序：Thursday 1 October 2026 / SE Architectures, Adaptation and Audio Front-Ends
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/carson26_interspeech.pdf

## 问题
SE 中语音质量与噪声抑制常此消彼长；资源受限模型更易偏一端。现有加权或 max 式 speech/noise 损失多不对齐相位、或不在每步同时优化两端，难用单一可调参数稳定地偏置训练目标。

## 方法
提出 Dual-Asymmetric Loss：由 \(L_{speech}\) 与 \(L_{noise}\) 线性组合 \(L=\lambda L_{speech}+(1-\lambda)L_{noise}\)。两项均含压缩复域与幅度（\(\alpha\)、\(c\) 沿用 CCMSE）；幅度用 ReLU 不对称差，复域用指示函数只在“过抑语音”或“残留噪声”的时频点计罚。\(\lambda\) 低偏抑噪、高偏保语音；\(\lambda=0.5\) 退化为缩放 CCMSE。在 LiSenNet、DPCRN、SEMamba、MP-SENet 上、VoiceBank-DEMAND 训练，并加 STFT consistency。

## 实验与结果
DNS5 Blind 与 VoiceBank-DEMAND 上，\(\lambda=0.35/0.5/0.65\) 分别抬高 BAK、平衡、抬高 SIG；\(\lambda=0.5\) 常得最高 SI-SDR。LiSenNet 扫 13 个 \(\lambda\)：与 SIG/BAK 的 PCC 为 0.95 / −0.96。\(\lambda\le0.25\) 过抑语音、\(\ge0.7\) 噪声泄漏。相对官方 SEMamba/MP-SENet 权重，在 DNS5 上 SIG/BAK/SI-SDR 有提升；WER 相对 noisy 降约 32–45%。

## 结论
单一 \(\lambda\) 可在多种因果/非因果架构上可控地权衡重建与抑噪，并与 DNSMOS 指标强相关；推荐大致落在 0.3–0.65。

## 点评
把不对称惩罚对称地扩到“残留噪声”一侧，并同时做复域，比只罚过抑更完整。依赖 DNSMOS 作调参读出；极端 \(\lambda\) 会明显失真，部署仍需按场景标定。
