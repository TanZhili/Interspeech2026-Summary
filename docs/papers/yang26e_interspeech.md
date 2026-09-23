# Schrödinger Bridge Mamba for One-Step Speech Enhancement

- 论文编号：682
- 报告人：Jing Yang
- 程序：Monday 28 September 2026 / Neural Speech Enhancement: Survey, Diffusion and Flow Matching
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/yang26e_interspeech.pdf

## 问题
Schrödinger Bridge（SB）语音增强可缓解扩散的 mean prior mismatch，但常用 NCSN++ 骨干往往需多步求解、实时性差；而 Mamba 虽已用于 SE，多停留在确定性映射/掩码，未与 SB 轨迹监督结合。作者强调训练范式与骨干归纳偏置应对齐。

## 方法
SBM：在退化分布与干净分布之间用 VE 调度构造 OT 中间态 x_t = μ_x(t)+σ_x(t)z，以 STFT 上的 x_t 与时间嵌入训练 Mamba 骨干做 data prediction（幅度/复数 MSE 与多分辨率项）。骨干基于 oSpatialNet-Mamba，加时间条件与全频带 Mamba 层，小 look-ahead（约 2–4 帧、<40 ms 算法时延）。推理固定 t=1（退化先验）单步直出干净谱。

## 实验与结果
训练约 800 h 干净语音 + 噪声 + RIR，SNR ∈[−10,20]，联合去噪去混响。评测 DNS（含/无混响、真实录音）与 VoiceBank-Demand。约 3.93M 参数、RTF≈0.0048。DNS With Reverb / Real Recordings 上多项 DNSMOS、NISQA、语义/说话人相似度等领先；无混响与 VBD 上与 ZipEnhancer 互有胜负。优于同骨干映射基线、FM-Mamba、一/多步 SB-NCSN++、SBCTM、SB-UFOGen。消融：SB 相对 mapping 在 MHSA/LSTM/Mamba 上均提升，且 Mamba+SB 最强。

## 结论
作者认为 SB 轨迹监督与 Mamba 状态演化归纳偏置协同，可在单步推理下取得高质量联合去噪去混响，并具备竞争 RTF；强调范式–骨干对齐对连续时间序列建模的启示。

## 点评
卖点不在发明新扩散公式，而在论证“中间态轨迹 + 选择性 SSM”比“同骨干硬映射”或“同 SB 换 NCSN++”更匹配。一、挑战场景（混响/真实录音）优势更清晰；对齐敏感指标上相对强判别模型未必全面占优，作者也提到双讲训练策略会影响部分语义分。流式 look-ahead 与边缘部署潜力写在设计里，正文未给大规模端侧实测。
