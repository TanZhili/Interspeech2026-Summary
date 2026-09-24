# OmniCodec: Low Frame Rate Universal Audio Codec with Semantic–Acoustic Disentanglement

- 论文编号：494
- 报告人：Jingbin Hu
- 程序：Wednesday 30 September 2026 / Neural Audio Codec Architectures
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hu26b_interspeech.pdf

## 问题
多数神经 codec 偏语音高保真重建，缺跨语音/音乐/通用声音的低帧率统一建模；高重建质量也不等于语义可信息，限制下游生成。

## 方法
OmniCodec：分层多码本；首批码本注入预训练理解模型（Qwen3-Omni-AuT）音频编码器的语义，其余码本专注声学；self-guidance 提升码本利用率与重建。支持 12.5 Hz 与 6.25 Hz。在 LibriSpeech、GTZAN、AudioSet 子集与下游生成任务相对 Mimi 等对比。

## 实验与结果
同码率下相对 Mimi-16L，OmniCodec-32L（12.5 Hz）PESQ-WB 等多项更优（如约 3.02 vs 2.88），Mel/MCD/主观 MOS 亦有提升；6.25 Hz 变体仍可用。语义侧 PPL 等指标显示表征更利于生成；作者亦指出语音解耦仍有挑战。

## 结论
预训练理解编码器语义注入 + 声学码本分层，可在低帧率全域 codec 上兼顾重建与下游语义效用。

## 点评
把“理解模型编码器当语义教师”接到通用 codec，方向对下游 LM 生成很关键。语音域解耦未完全解决；开源承诺落地后更易复现帧率–码本配置。
