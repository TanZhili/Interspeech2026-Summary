# Tracing the Origins: Legacy Codec Identification in Neural Audio Transcoding

- 论文编号：2354
- 报告人：Shinee Youn
- 程序：Wednesday 30 September 2026 / Speech and Language Representation
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/heo26b_interspeech.pdf

## 问题
RVQ 神经音频编解码（EnCodec 等）把信号变成离散 token，传统基于线性假设的编解码取证在神经转码后失效；legacy→neural 叠加伪迹下能否识别原始传统编解码器，尚缺乏系统框架。

## 方法
输入 EnCodec RVQ token，经预训练码本嵌入后过三模块：(1) Layer-Causal RVQ Transformer（层间因果掩码注意力建模层次依赖）；(2) Dynamic Layer-wise Attentive Aggregator（全局层权 + 时变层注意后沿层聚合）；(3) Temporal Context Transformer（捕捉预回声/带宽等时序签名）→ MLP 分类。数据：VCTK 先经 FFmpeg 的 MP3/AAC/Opus/Vorbis/G.711 再 48 kHz EnCodec 转码，比特率 32–128 kbps，说话人无关划分。

## 实验与结果
- 固定比特率编解码识别：32/64/96/128 kbps 准确率 99.99%/99.70%/98.36%/97.32%（均 >97%），低比特率更易辨。
- 固定编解码比特率分类：AAC/Vorbis >99%；MP3 84.43%、Opus 71.01%（96 vs 128 kbps 易混）。
- 18 类联合识别：完整模型 Acc 89.34%、Macro-F1 89.31%，相对 CNN+MLP 基线（73.71%）提升 >15%；LCR-Trans 贡献最大。

## 结论
legacy 编解码伪迹在神经转码后仍可检测；固定比特率识别很强，高比特率 MP3/Opus 与部分低比特率跨编解码混淆仍是难点。未来需扩编解码覆盖并加强高比特率分辨。

## 点评
把 NAC 当成“传输信道”而非不可穿透黑箱，用 RVQ 层次因果与层注意去拆叠加伪迹，问题定义清晰。近完美的固定比特率识别令人印象深刻，但联合 18 类与 Opus 高码率仍露怯，说明“透明区”伪迹收敛才是真难点。当前仅 EnCodec 转码、VCTK 语音，泛化到音乐/其他 NAC 仍待证。
