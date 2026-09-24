# EffVOC: Low-Delay Efficient Speech Waveform Reconstruction from Spectral Representations Without Phase

- 论文编号：2407
- 报告人：Renzheng Shi
- 程序：Wednesday 30 September 2026 / Dereverberation, Bandwidth Extension and Restoration
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shi26f_interspeech.pdf

## 问题
从幅度/Mel 重建波形时，经典相位恢复算法延迟高或质量差；神经声码器质量高但常更复杂、延迟更大。需 20 ms 级低算法延迟的高效重建。

## 方法
EffVOC：基于低延迟 Encodec 式声码器改造，直接从幅度谱或 Mel 合成宽带/全带语音，无显式相位迭代。固定 20 ms 窗、5 ms 移；可配置通道宽度 F∈{64,32,16,8} 权衡算力与质量。

## 实验与结果
VCTK 16 kHz：F=64 幅度输入 PESQ-WB 4.31、MOS 4.17，延迟 20 ms，RTF≈0.65；F=32 仍 PESQ 4.24。优于同延迟 RTISI 变体；相对高延迟 GLA/DiffPhase 接近。Mel 输入 F=32 亦达 PESQ 4.21、MOS 4.15。更小 F 质量下降但算力大降。

## 结论
20 ms 低延迟神经重建在客观与 MOS 上达新 SOTA 区间，且可按 F 伸缩部署。

## 点评
把“算法延迟”定义钉死在帧长，便于与通信场景对齐。与高延迟相位法比质量优势明显；与大扩散模型比算力友好。全带与极小 F 时仍有可见质量折损。
