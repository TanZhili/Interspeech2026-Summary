# Neuromorphic Speech Enhancement with Dual-Branch Spiking Neural Networks

- 论文编号：1797
- 报告人：Wenbin Jiang
- 程序：Thursday 1 October 2026 / SE Architectures, Adaptation and Audio Front-Ends
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/meng26d_interspeech.pdf

## 问题
SNN 增强参数少、适合神经形态硬件，但二值脉冲与单分支谱建模使质量仍落后主流 ANN；现有工作少在双路径框架里系统利用幅度与复谱的互补性。

## 方法
GSU-DBNet：STFT 实部/虚部/幅度三通道经带 CBAM 的卷积编码器 → 两层双路径 GSU（频向 BiGSU、时向因果 GSU）→ 双分支转置卷积解码器：复分支 tanh 输出作 DeepFilter 系数，幅度分支 sigmoid 掩码乘噪声幅度，再加权融合。GSU 仅单遗忘门更新膜电位并以 Heaviside 发脉冲（三角 surrogate）。损失为压缩谱 MSE + SI-SNR。

## 实验与结果
VoiceBank+DEMAND：394K 参数下 PESQ 3.04、CSIG 4.28、CBAK 3.57、COVL 3.68、SSNR 9.94，优于 DPSNN（PESQ 2.20）与 Spiking-FSN（2.66），并超过若干更大 ANN（如 DCCRN/FullSubNet+/GaGNet）。消融显示双分支、双路径均必要；多门 SLSTM 参数升而 PESQ 不升反降；平均放电率约 37%。

## 结论
单门 GSU + 双路径双分支可在极少参数下拉近与 ANN 的 PESQ 差距；二值输出瓶颈下加门无益，适合稀疏事件驱动部署方向。

## 点评
把 ANN 里成熟的双路径/双谱思想迁到 spiking 单元，参数效率叙事清晰。评测主要在合成 VoiceBank；真正神经形态芯片上的能耗/时延未实证，CSIG 仍略逊 TSTNN。
