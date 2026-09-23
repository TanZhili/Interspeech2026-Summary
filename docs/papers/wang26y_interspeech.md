# AugCodec: A Low-Bitrate Disentangled Neural Speech Codec via Data Augmentation

- 论文编号：1490
- 报告人：Dongmei Wang
- 程序：Monday 28 September 2026 / Neural Speech Codecs: Low-Bitrate and Disentangled Coding
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26y_interspeech.pdf

## 问题
解耦编解码器常从同一源抽全部属性，交叉干扰大；低帧率表示又难保语义，声转换 WER 偏高。

## 方法
AugCodec：语义支路用扩散 VC 语音 + wav2vec2.0（层平均）经 ConvNeXt 与帧堆叠压缩；说话人支路用同说话人另一句 + ECAPA-TDNN→FSQ；韵律支路保留 STFT 低频 + 粗 hop（160 ms）FSQ。增强损失对齐源与 VC 的语义编码器输出。语义 VQ + 全局说话人/韵律 FSQ，总约 12.5 Hz 三流。

## 实验与结果
LibriSpeech test-clean：AugCodec-3 WER 5.12、PESQ 1.99、UTMOS 3.04（约 400 bps），优于 BiCodec/Mimi 等同帧率设定。去增强损失 WER/PESQ 变差。声转换：12.5 Hz 下 WER 约 5.87 vs BiCodec 65.43。

## 结论
分源增强抽取语义/说话人/韵律可显著加强解耦与低比特重建，并改善声转换可懂度。

## 点评
用“输入变体”强迫属性分离，比同源多头+对抗更直接。推理重建改回原句提取，训练–推理分布差；VC 质量上限会渗入语义支路。
