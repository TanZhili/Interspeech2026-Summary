# Low-Framerate Speech Tokenization via Two-Stage Latent Patch Modeling

- 论文编号：2863
- 报告人：Théodor Lemerle
- 程序：Wednesday 30 September 2026 / Speech Synthesis: Speech Features, Codec and Representations
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/lemerle26_interspeech.pdf

## 问题
低帧率语义语音 tokenizer 对下游 TTS 很重要，但通常要把波形压缩、对抗训练与语义监督绑在一起训，算力贵、难在消费级 GPU 复现；离散大码本/多层量化也易塌缩、下游建模复杂。

## 方法
提出两阶段连续编解码 Z-CODEC。第一阶段 WavVAE：轻度压缩（100 Hz、瓶颈维 24），SNAC 式编码器 + Vocos 风格 ConvNeXt/iSTFT 解码，用对抗目标吸收波形建模难度。第二阶段 PatchAE：把 `z` 按 patch（8 帧）压到 12.5 Hz 的 `˜z`（连续 VAE 或 FSQ，约 1.1 kbps），用潜空间 flow matching 从 `˜z` 重建高帧率 patch；在 velocity head 上对 WavLM-large 第 6 层特征做余弦语义对齐。下游 TTS 为 encoder–decoder Transformer + 轻量 MLP 预测到 PatchVAE 潜空间的速度场。整套可在单卡 RTX 4070/4090 上训练。

## 实验与结果
数据为 HiFiTTS2 + LibriTTS。LibriTTS test-clean 上，WavVAE 重建 PESQ 达 4.14；完整 Z-CODEC（VAE/FSQ）在 12.5 Hz 上与 Mimi、Higgs、XY-Tokenizer 等可比（FSQ：PESQ 2.23、UTMOSv2 3.05、dCER 0.59%）；去掉 WavLM 监督后 dCER 升至 1.49%。MUSHRA 主观质量与 Higgs 同属前列。TTS（0.24B）CER 1.1%，NMOS/SMOS 与更大参数的 F5-TTS、SparkTTS 接近。编解码在 RTX 4090 上约 130× 实时。

## 结论
分阶段把对抗波形建模与低帧率语义压缩解耦，可在消费级硬件上得到高质量低帧率（连续/离散）tokenizer，并支撑可训练的连续潜空间 TTS；当前非因果、仅英语。

## 点评
关键设计是“先把波形难点锁在高帧率 VAE，再在潜空间做 patch 压缩+FM+SSL”，用训练可负担性换端到端一体优化。强在复现门槛与低帧率质量；脆弱点是第二阶段解码依赖多步 ODE、非因果限制流式，且语义对齐质量高度依赖 WavLM 蒸馏。
