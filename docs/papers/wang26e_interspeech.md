# Predictive Directional Selective Fixed-Filter Active Noise Control for Moving Sources via a Convolutional Recurrent Neural Network

- 论文编号：271
- 报告人：Boxiang Wang
- 程序：Wednesday 30 September 2026 / Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/wang26e_interspeech.pdf

## 问题
定向选择性固定滤波 ANC（D-SFANC）按当前 DoA 选预训控制器，对移动源存在帧滞后，过渡期降噪变差。

## 方法
PD-SFANC：预训 36 个方位（10° 网格）宽带 FxLMS 控制器库；协处理器上 CRNN 用 K=4 帧多通道 STFT 幅相预测下一帧 DoA，提前切换滤波器；实时控制器按采样率输出抗噪。四面体 4 麦参考阵，16 kHz，帧长 0.5 s。数据含仿真白噪与 UrbanSound8K，多房间/SNR。

## 实验与结果
CRNN DoA 分类在 SNR≥20 dB 准确率 >90%，10 dB 约 87%。移动源仿真中，相对 FxLMS、SFANC、D-SFANC 等，PD-SFANC 能更稳地维持高噪声降低水平（NRL），多数时段 NRL 高于 15 dB，过渡更平滑。

## 结论
用时序预测消除滤波器切换滞后，可显著改善移动噪声场景的动态降噪，且参数端到端学习、无需手工调参。

## 点评
“预测下一帧再换滤波器”直接对准 D-SFANC 的滞后痛点，双速率架构也利于落地。当前限定单源与离散方位库；连续轨迹、多源与实物验证是自然延伸。
