# Noisy Environment Adaptation of Neural Speech Codec via Focal Mask and Noise Feature Separation

- 论文编号：512
- 报告人：Shaokai Li
- 程序：Monday 28 September 2026 / Neural Speech Codecs: Low-Bitrate and Disentangled Coding
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26e_interspeech.pdf

## 问题
神经语音编解码器在真实噪声下重建严重退化；多数嵌入空间增强只盯干净目标、忽略待抑制噪声成分，低码率低 SNR 更差。

## 方法
FocalSE 接在 DAC 连续嵌入空间：focal modulation 压缩/解压 + Transformer 得 focal mask，掩蔽噪声嵌入得增强嵌入；SEMamba 过滤后减去增强嵌入分离噪声嵌入；ResNet1D-18 做噪声类别识别。先清洁预训练 DAC，再冻编码器微调 FocalSE。

## 实验与结果
LibriTTS+ESC50，6/2.5 kbps × −5–10 dB：完整 FocalSE 全面优于 DAC、SECE、FD-CBR 及去掉 NR/ND 变体（如 6 kbps/−5 dB：PESQ 2.116、STOI 0.892、SI-SDR 5.403）。噪声分离与识别两者都带来增益。参数约 222M（完整）。

## 结论
在编解码器嵌入空间联合干净恢复、噪声分离与噪声识别，可显著提升低码率低 SNR 重建。

## 点评
相对只学干净掩码，显式分离噪声并分类提供互补监督，切中低 SNR 难点。算力与参数较基线 DAC 明显增大；依赖 DAC 与 ESC50 噪声类型，未见噪声外推需另测。
