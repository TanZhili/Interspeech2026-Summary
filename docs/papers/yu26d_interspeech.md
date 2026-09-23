# Sweep-RSE: Streaming Region-of-Interest Speech Extraction in Multi-Talker Scenarios via Explicit Spatial Sweeping

- 论文编号：1631
- 报告人：Hogeon Yu
- 程序：Tuesday 29 September 2026 / Source Separation 1
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/yu26d_interspeech.pdf

## 问题
AR/VR 与助听等场景需要按用户自定义空间窗口做 Region-of-Interest 语音提取，但 ReZero、DPARNet-RSE 等依赖隐式边界条件，在稠密干扰或空区域（Q=0）时易漏提或误放。本文要做轻量、全因果、显式空间扫描的流式方案。

## 方法
Sweep-RSE：先把窗口中心相位对齐到虚拟正前方；CH-SDB 用复数卷积保相位；Physics-Informed Spatial Sweep Attention（SSA）在窗口内用 L 个候选导向矢量扫相位相干性并做动态波束成形；Gated Context Fusion 拼接参考、对齐目标与差分特征以抑区外干扰；因果 Dual-Path Block（改自 SpatialNet）做时频谱细化；Region Speech Detector（RSD）门控空区输出。4 麦方形阵仿真（gpuRIR + VCTK + WHAM!），窗口宽随机 10°–90°，联合 SI-SDR + 0.1 BCE 训练。

## 实验与结果
因果版约 1.66M 参数、3.05 GMACs。Standard/Realistic：Q=0 能量衰减约 96–98 dB（远高于 SpatialNet 等）；Q=1 SI-SDR 10.60/12.88 dB，Q=2 为 13.04/12.64 dB。同 backbone 的隐式 proxy：ReZero-Proxy / DPARNet-Proxy 在 Realistic Q=1 约 10.3–10.4 dB，显式 Align & Sweep 达 12.88 dB（+2.4 dB 以上）。注意力图显示峰值跟随偏心目标而非只盯窗口中心。

## 结论
显式 Align & Sweep 加 RSD，在稠密多讲者与空窗口场景上显著优于隐式条件化，并以 O(1) 流式复杂度与很小算力支持边缘实时；未来拟在 ROI 内进一步拆分多说话人。

## 点评
把“区域提取”从学边界嵌入改成物理可解释的相位相干扫描，空区衰减与高干扰增益是最硬的证据。同 backbone 的 proxy 对照设计得很干净。局限是仿真阵列与固定扫描分辨率；真实阵列校准误差、移动目标与 ROI 内多源拆分仍未覆盖。
