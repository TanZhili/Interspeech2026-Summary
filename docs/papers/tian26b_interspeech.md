# DDSN: A Wrapped-Phase-Aware Decoupled Dual-Stream Network for Speech Packet Loss Concealment

- 论文编号：1295
- 报告人：Hao Tian
- 程序：Wednesday 30 September 2026 / Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/tian26b_interspeech.pdf

## 问题
频域 PLC 常联合建模实/虚部，忽略幅度与相位差异，导致相位错位与结构伪影；长突发丢包尤甚。批次元数据标题写作 Physics-Aware，正文为 Wrapped-Phase-Aware。

## 方法
DDSN：幅度与相位双流因果 U-Net（相位用 (cosθ,sinθ)），共享膨胀 TCN 抓全局上下文；SARG 用幅度先验作缩放残差引导相位（1+α·Mask），避免 sigmoid 门控在低能量区掐断相位；相位经 L2/SVD 投影回单位圆，幅度做 |A|^0.5 压缩。损失含流形约束、多分辨率 STFT、相位一致性与感知项。

## 实验与结果
VCTK 合成与 Interspeech 2022 PLC 盲测上，DDSN 在 PESQ/STOI/PLCMOS/DNSMOS 上优于 TFGAN、FRN 等；长突发下 PLCMOS 更稳。消融（40% PLR）支持解耦、SARG 与流形约束各自贡献。

## 结论
显式 wrapping 相位建模与非衰减式幅度→相位引导，可在因果约束下改善突发丢包重建稳定性。

## 点评
把“相位被幅度优化淹没”当作 PLC 核心失败模式，并用残差引导而非硬门控，设计针对性强。闭式 2×2 SVD 利于实时；与批次元标题不一致处，以正文为准。
