# WaveNorm: A Low-Complexity Time-Domain Neural Adaptive Gain Control for Real-Time Speech Applications

- 论文编号：3588
- 报告人：Harish Rajamani
- 程序：Thursday 1 October 2026 / Speech Recognition, Enhancement and Real-Time Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ijjada26b_interspeech.pdf

## 问题
真实语音电平因距离、房间与设备大幅波动，损害 ASR、会议与助听；传统 AGC（如 WebRTC）靠包络与固定 attack/release，难区分语音/噪声，易延迟、削波或放大背景噪声；频域学习方法又增加延迟，不利于边缘实时。

## 方法
WaveNorm AGC 全时域、因果：20 ms 帧、10 ms 移。编码器为堆叠因果 Conv1D（核 3，dilation 2/4/8）+ grouped convolution + BN/PReLU，建模多尺度幅度与包络；瓶颈为 hidden 32 的 GRU 与 32 维全连接，保证增益平滑；解码器用转置 Conv1D 镜像上采样，端到端映射波形，隐式完成归一化与降噪，不显式输出增益系数。感受野约 27 样本（~0.56 ms）。损失为 0.5 MSE + 0.5 多分辨率谱损失（STFT 128–2048）；Adam 1e-3，200 epoch。

## 实验与结果
内部 48 kHz 语料 + DNS3：RMS −10 至 −70 dB，噪声 SNR −5 至 +20 dB。独立 AGC：在 VoiceBank+DEMAND 衰减与 TIMIT 放大设定下，相对 WebRTC、Carnival 更电平不变、增益更平滑，约 6 dB 降噪，Active Speech Level 近 −26 dBov，响度 −26 至 −28 LUFS，符合 ITU-T P.56/P.79。作前端时，在 DeepFilterNet2、DTLN、GTCRN 上最高约 +0.35 NISQA。模型 49 M MACs、55 KB 内存。

## 结论
WaveNorm 以极低时延与很小算存实现宽动态（至 −70 dB）稳定响度归一化，并在噪声下约 6 dB 降噪，避免传统 AGC 的削波与噪声放大，适合会议与边缘实时语音。

## 点评
把 AGC 做成时域端到端“内容感知电平映射”，用 GRU 约束增益平滑，是对规则包络跟踪的直接替代，而非再堆一套频域增强。数字披露偏概括（对比多为定性+少量 NISQA），对极端非平稳噪声与说话人切换时的 pumping 风险仍需更多公开对比表支撑；优势主要在边缘算力与标准响度合规。
