# USDnet++: Distilling Signal Processing Based Dereverberation for Unsupervised Neural Speech Dereverberation

- 论文编号：2044
- 报告人：Zhong-Qiu Wang
- 程序：Wednesday 30 September 2026 / Dereverberation, Bandwidth Extension and Restoration
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/pang26_interspeech.pdf

## 问题
无监督去混响 USDnet 仅靠线性滤波重建观测约束；WPE/WPD 等信号处理结果通常抬高目标 SNR，可作弱监督，但不宜直接当硬标签。

## 方法
USDnet++：在原有“DNN 输出经线性滤波重建混合”之外，增加使滤波后估计逼近 SPD（WPE/WPD）结果的损失；可多阶段交替 DNN 与 SPD 精炼；亦可把 SPD 结果作额外输入再训。骨干 TF-GridNet；DNN 估计直达声支撑 WPE/WPD。

## 实验与结果
WSJ0CAM-DEREVERB（8 麦）：混合 PESQ 1.64 / SI-SDR −3.6 dB；USDnet 2.64 / 3.1 dB；USDnet++ 用 USDnet-WPD 作 SPD 达 2.86 / 3.9 dB。Oracle-WPD 指导可达 2.95 / 4.9 dB。多阶段 refinement 进一步提升。

## 结论
把 SPD 当弱约束而非硬目标，可稳定改进无监督神经去混响，并与 WPE/WPD 形成互补闭环。

## 点评
保留 USDnet 物理重建思想，又吃到经典算法的 SNR 红利，折中合理。性能仍受 SPD 上限牵制（相对监督 Oracle）；真实远场噪声/多说话人是否同样有效需外推谨慎。
