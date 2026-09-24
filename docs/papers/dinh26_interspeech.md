# Improving Audio Codec-based Speech Separation By Stacking Residual Vector Quantization Layers

- 论文编号：2296
- 报告人：Nhu Minh Phuong Dinh
- 程序：Thursday 1 October 2026 / Source Separation 2
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/dinh26_interspeech.pdf

## 问题
波形域分离算力高；神经音频编解码器（NAC）在压缩潜空间分离更省算力，但既有 Codecformer 在启用 RVQ 时把各层码本向量求和成单一嵌入，毁掉粗到细层次，导致性能下降。

## 方法
RVQ-Grid：冻结预训练 codec，将各层量化向量堆成 3D 网格 Z∈R^{N×D×T}；经 Conv2D 投影后，用 L 个双轴循环块交替沿码本轴（跨层 BiLSTM）与时间轴（时序 BiLSTM）建模；mask head 输出逐说话人、逐层 mask，再对码本维求和后经 codec 解码。实现 DAC（N=12）与 EnCodec（N=32）两变体，mask 激活对齐各 codec 内部激活。

## 实验与结果
WSJ0-2Mix：相对 Codecformer (DAC) SI-SDRi 从 5.0→8.1 dB（+3.1，摘要称 +3.6）；RVQ-Grid (EnCodec) SI-SDRi 8.6、WER 8.6%（Whisper large-v3-turbo），接近同 codec 条件下的 SepFormer 通路表现，MACs 约为 SepFormer 的 1/6。感知上 PESQ/STOI 明显优于 Codecformer。消融：更多 RVQ 层与更高码率持续提升；长序列训练（10–20 s）可再抬 SI-SDRi；GPU 显存随长度增长远缓于 SepFormer。

## 结论
显式保留 RVQ 层次可显著改善 codec 域分离与下游 ASR 可用性，同时保持压缩域高效；局限是 codec 冻结且非为分离设计。

## 点评
与“别把 RVQ 压扁”的思路一致，用码本×时间双轴建模很直接。SI-SDR 仍低于纯波形 SepFormer 属预期（有损重建），价值在边缘/传码场景；冻结通用 codec 是天花板，也是下一步可改点。
