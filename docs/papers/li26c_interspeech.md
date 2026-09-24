# MSR-Codec: A Low-Bitrate Multi-Stream Residual Codec for High-Fidelity Speech Generation with Information Disentanglement

- 论文编号：301
- 报告人：Jingyu Li
- 程序：Wednesday 30 September 2026 / Neural Audio Codec Architectures
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26c_interspeech.pdf

## 问题
生成用神经编解码常要较高码率；语义/音色/韵律纠缠也限制可控合成与转换。

## 方法
MSR-Codec 将语音编码为四路：semantic、timbre、prosody、residual，多尺度残差逐步融合重建 Mel，再经声码器。基于该 codec 建两阶段轻量 TTS（先语义后韵律细节）。评重建、TTS（WER/SIM）与音色–韵律解耦的声音转换；开源代码与模型。

## 实验与结果
在约 424/524/612 等低码率配置下重建质量有竞争力。两阶段 TTS 相对若干更大模型 WER 更低、说话人相似度更高，且数据需求小、生成更快。VC 实验显示可较独立地迁移音色而不绑死韵律。

## 结论
多流通用残差分解能同时服务低码率高保真与可控生成；解耦能力经 TTS/VC 验证。

## 点评
把 disentanglement 做成显式四流而非事后分析，对 SLM-TTS 管线很实用。码率–质量表与对照系统细节需对照 PDF 完整表；四流设计的训练稳定性与码本利用率是常见风险点。
