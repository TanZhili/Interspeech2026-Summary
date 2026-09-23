# BridgeCodec: Mamba Enhanced Neural Audio Codec with Schrödinger Bridge at Low Bitrate

- 论文编号：1338
- 报告人：Zijian Lin
- 程序：Monday 28 September 2026 / Neural Speech Codecs: Low-Bitrate and Disentangled Coding
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lin26d_interspeech.pdf

## 问题
神经编解码器编码器–解码器强耦合，异构设备/非对称带宽下无法互通；标准扩散要求高斯先验，会冲掉源潜变量中的语音结构。

## 方法
BridgeCodec：冻结源编码器与目标解码器，用 Schrödinger Bridge 在潜空间做最优传输映射；骨干为 Mamba 增强 U-Net 捕捉长程依赖。两阶段：潜空间对齐再音频域精炼。极端设定：8 kHz 轻量源 → 48 kHz 目标，1 kbps。

## 实验与结果
相对源编解码：STOI 0.23→0.88，MEL 10.01→1.65，SIM 0.81→0.96，MOS 4.12（接近目标 4.24）。1 NFE 仍稳健，利于低延迟。WER 略升（约 2.11 vs 源 1.92）归因于高频生成幻觉。

## 结论
SB + Mamba 可桥接失配、冻结端点，在超低码率下完成窄带→宽带重建并保持互通。

## 点评
把“互通缺口”形式化为潜空间运输而非重训端点，工程价值高。验证集中在一对 8→48 kHz 设定；跨任意编解码器对的泛化与延迟仍取决于桥接模型大小。
