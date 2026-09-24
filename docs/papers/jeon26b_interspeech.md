# Ego-Noise-Aware Spatial Filtering for Reliable UAV Audition in Extreme Low-SNR Conditions

- 论文编号：1530
- 报告人：Chanhong Jeon
- 程序：Thursday 1 October 2026 / Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jeon26b_interspeech.pdf

## 问题
无人机自噪声强时域相关、频变组成与幅度平稳，分别破坏 DoA、噪声协方差与波束后残差抑制，极端低 SNR 下常规波束成形不可靠。

## 方法
无预训练、约 0.021 GMAC/s 的信号处理管线：相位一致性引导 TF bin 选择（偏离时域相关参考的 bin）估 DoA；按交叉频率 ν（文中 3 kHz）混合 closeness/directional 掩码估 NCM 并做 MVDR；用最小似然方向作 null 参考，方差调制 Wiener 后滤波压残差自噪声。圆形 4 麦阵、实测 Syma 自噪声 + TIMIT 仿真。

## 实验与结果
−25 dB 下 DoA 准确率达 98.12%，优于 MUSIC、SRP-PHAT、wHisK。消声/混响（T60=0.3 s）多 SNR 上 SI-SDR、PESQ、ESTOI、DNSMOS 整体优于 MPDR、directional/closeness MVDR、MMSE；后滤波贡献显著（如消声 −25 dB SI-SDR −2.45 vs 无后滤 −9.17）。

## 结论
围绕自噪声结构性质联合设计 DoA–NCM–后滤，可在极低 SNR 提升无人机听觉；实验主为悬停与固定阵几何。

## 点评
把 DoA 当全管线共享空间锚点而非仅导向向量，工程思路清楚、算力极低。强依赖悬停相关与固定 ν/σ；机动、非平稳自噪声与真实远场对话场景仍具挑战。
