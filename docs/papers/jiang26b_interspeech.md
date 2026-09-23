# VoCodec: A Low-bitrate Streamable Neural Speech Codec with Voicing-driven Quantization

- 论文编号：466
- 报告人：Yang Ai
- 程序：Monday 28 September 2026 / Neural Speech Codecs: Low-Bitrate and Disentangled Coding
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jiang26b_interspeech.pdf

## 问题
多数神经语音编解码器对每帧均匀量化，未利用浊音感知更敏感、清音可少码的事实，低码率浪费比特。

## 方法
VoCodec（因果 StreamCodec 风格）：MDCT + 因果 ConvNeXt/LSTM 编码；能量检测器在 F0 搜索带判浊/清；浊帧 RSVQ、清帧简单 SQ，并传 1 bit 浊音标志。掩码训练加速流式。16 kHz 平均约 1.1 kbps（随浊音比约 0.55–1.55）。

## 实验与结果
LibriTTS 1.1 kbps：STOI 0.916、ViSQOL 4.115、MUSHRA 75.18，优于多数流式基线，接近非流式 BigCodec；参数 9.31M、FLOPs 2.62G。相对均匀量化约省 27% 码率。ABX 偏好与 1.5 kbps 他法可竞争。浊/清分项 LSD 显示优先保浊音质量。

## 结论
按浊音驱动分配码率，可在流式低码率下保持高重建质量并显著省比特。

## 点评
把传统 CELP 的浊清分治迁入神经 RSVQ/SQ，感知分配逻辑清晰。能量阈值浊音检测粗，噪声/混响下误判会错配量化器；与内容自适应码率（非仅浊清）仍可结合。
