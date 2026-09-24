# A Causal Reference-Enhanced Keep-Speech Active Noise Control Method

- 论文编号：1608
- 报告人：Li Rao
- 程序：Wednesday 30 September 2026 / Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/rao26_interspeech.pdf

## 问题
耳机 ANC 参考麦同时拾取噪声与语音，控制器会把语音一并抵消，损害对话可懂度；DeepANC 等端到端替换控制滤波会引入帧延迟，难满足因果余量。

## 方法
RSE-KSANC：用因果 WaveNet 变体增强参考信号（压语音、留噪声），FIR 控制滤波仍由 RLS 自适应；输入为原始参考与误差侧估计的含噪语音 ˆdv。训练目标对比 Lenh（误差域噪声抑制+保语音，代入 Wiener 最优 w）与 Lrefsep（参考端噪声提取 MSE）。约 9.53M 参数、零算法附加延迟。用实测耳机 IR（多方向/距离）与 LibriTTS+带限噪声及 DCASE 真实噪声评测。

## 实验与结果
Lenh 配置在 −5～15 dB SNR 上 STOI/DNSMOS 全面优于未处理、传统 ANC、DeepANC 与 Lrefsep；如 SNR=5 dB 时 STOI 88.67%、DNSMOS 2.36。真实风扇/引擎等噪声下同样领先。传统 ANC 在高 SNR 甚至因压语音而差于未处理。

## 结论
在参考支路做零延迟语音抑制、保留经典滤波器，可在严格因果下实现 keep-speech ANC，并泛化到未见方向、噪声与 SNR。

## 点评
把“智能”放在参考增强而非替换控制律，是兼顾因果与可部署性的好折中。Lenh 对齐最终误差目标，优于纯参考分离。模型仍偏大（约 9.5M），作者也指出需压缩以进耳机。
