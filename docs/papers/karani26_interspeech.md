# mmWave Radar Aware Dual-Conditioned GAN for Speech Reconstruction of Signals With Low SNR

- 论文编号：2330
- 报告人：JASH KARANI
- 程序：Thursday 1 October 2026 / Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/karani26_interspeech.pdf

## 问题
玻璃墙后 mmWave FMCW 语音捕获带限且 SNR 极低（约 −5 至 −1 dB），难重建可懂全带语音；许多方法依赖大数据、预训练模块或偏乐观 SNR。

## 方法
RAD-GAN 两阶段：Stage-1 在带限（≤1 kHz）干净 mel 上用 mel + MR-STFT 预训练 HiFi-GAN 生成器；Stage-2 用 Residual Fusion Gate 融合噪声 mel 与 WaveVoiceNet 增强 mel，对抗微调，判别器含 MPD、MSD 与提出的双分支 Multi-Mel Discriminator。RASE 2026 数据：直接膈肌振动与铝箔二次表面两任务，约 42 h 配对。

## 实验与结果
加权分 0.333（Task1 0.387 / Task2 0.297）优于 WaveVoiceNet、HiFi-GAN、DCCTN、AP-BWE、DiffWave、CDiffuSE；DNSMOS 2.688 等更均衡。消融显示 MMD/MR-STFT、预训练、WVN 条件逐步抬分。无数据增强、无外部预训练骨干。

## 结论
双条件融合 + 两阶段训练可在小数据、极低 SNR mmWave 设定下提升带宽扩展重建；Task2 更难但加权更看重。

## 点评
先稳住低带到全带映射再引入对抗与多 mel 判别，适合噪声相位不可靠场景。指标靠加权综合而非单一 PESQ；数据规模相对小、场景特定，跨雷达硬件泛化未知。
