# Phoneme-Aware Mamba Watermark: An Active Defense System Against Purified Speech Deepfakes

- 论文编号：2105
- 报告人：Yanda Shao
- 程序：Thursday 1 October 2026 / Audio Watermarking and Source Verification
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/shao26_interspeech.pdf

## 问题
零样本语音克隆（如 YourTTS、sv2TTS）使深度伪造语音高度逼真，被动 Audio Deepfake Detection 对未见合成模型泛化不足。扰动式主动防御（AntiFake、VoiceGuard）又易被 PhonePuRe 等扩散净化抹除。需要一种能嵌入可检索身份信息、并在净化与克隆后仍可追踪的“阴影式”水印防御。

## 方法
提出基于 Mamba 的音素感知主动水印框架。输入语音经冻结 XLS-R 300M 提取语音表征，并与 STFT 复谱并行；水印编码器在说话人身份码条件下生成谱扰动，注入 100–1000 Hz 频带后经 iSTFT 重建。Montreal Forced Aligner 得到音素边界，构造稳定区 mask，将扰动集中在音素稳态区。编码器对比 Bi-LSTM、Dual-column Bidirectional Mamba 与 Multi-Head Mamba（含音素门控）；解码器为独立 8 层 CNN，从 log-magnitude STFT 恢复水印。训练含抗净化对抗：周期引入 PhonePuRe（RevDiffWave + Refiner），联合水印检索、扰动幅度、重建、干净语音假阳性与净化后可检索损失。水印用 Hamming(6,3) 将 16 bit 扩为 36 bit，按 1 s 块重复嵌入，检测时多数表决。

## 实验与结果
在 LibriSpeech train-clean-100 训练，VCTK 11 说话人做真实威胁仿真。对抗微调后 MH-Mamba 净化前/后 bit 准确率 91.56% / 84.55%，Retain Rate 92.34%，优于 LSTM 与 BiMamba。对 YourTTS/sv2TTS 克隆语音源追踪 TPR 近 100%，延迟约 1.0–1.2 s。PESQ>3.5、SNR>34 dB。消融显示音素引导显著提升 PhonePuRe 后保留率。

## 结论
将水印与音素稳态耦合，并以对抗训练对抗 PhonePuRe，可在 TTS 克隆链路中保持可追踪、低延迟、较透明的主动防御。作者认为这为应对新兴语音深度伪造提供了实用机制。

## 点评
做法抓住的是“净化—克隆后仍可检索”而非单纯干扰合成：用音素稳态承载水印，直接针对 PhonePuRe 的音素条件去噪路径。Mamba 长程建模与对抗净化训练配套合理，但依赖 MFA 对齐与固定频带注入，对噪声、语种或非对齐语音的稳健性正文未充分展开；UFL 理论上界约 2 s，短时伪造仍可能漏检。
