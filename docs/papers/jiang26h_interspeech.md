# An Ultra-Low-Bitrate Neural Speech Codec with Plain-to-Pseudo Synergistic Vector Quantization

- 论文编号：3506
- 报告人：Xiao-Hang Jiang
- 程序：Monday 28 September 2026 / Neural Speech Codecs: Low-Bitrate and Disentangled Coding
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jiang26h_interspeech.pdf

## 问题
RVQ 后续级贡献递减却同等耗比特，超低码率（如 0.5 kbps）质量骤降；放大模型可达质量但部署重。

## 方法
P2PSynCodec：MDCT + 轻量 ConvNeXt 编解码；Plain-to-Pseudo Synergistic VQ——1 个 plain VQ 产出可传输基本 token，N 个伪 VQ 用 Conformer+BiLSTM 由基本/先前伪 token 预测辅助 token（零传输比特），码本查找后求和送解码器。训练期可与教师编解码器协同。16 kHz 仅 0.5 kbps。

## 实验与结果
LibriTTS 0.5 kbps：UTMOS 3.947，接近甚至优于若干高复杂度基线，参数 22.99M、FLOPs 3.31G（远小于 BigCodec）。ABX：0.5 kbps 听感可与 2.0 kbps 级编解码竞争。伪 VQ 数量影响分析显示适度 N 提升质量。

## 结论
用可预测伪量化级换“零比特辅 token”，可在超低码率逼近更高码率重建质量且保持轻量。

## 点评
把 RVQ 尾部浪费改成解码端预测，码率会计直接砍到单 VQ。伪 VQ 依赖 plain token 信息量；信道误码时预测链可能级联失败，需额外保护策略。
