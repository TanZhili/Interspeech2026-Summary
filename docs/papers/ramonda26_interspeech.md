# Readability Does Not Predict Speech Recognition Errors: Contrasting Human and Machine Perception.

- 论文编号：2439
- 报告人：Baptiste Ramonda
- 程序：Wednesday 30 September 2026 / New Architecture and Analyses for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ramonda26_interspeech.pdf

## 问题
人类在噪声中依赖可读性补偿理解，早期 ASR 也常因文本复杂度/困惑度升高而 WER 变差。现代端到端 ASR 是否仍对文本可读性敏感，还是已与语言学复杂度解耦？真人口语会随难度改变发音，需控制声学混杂。

## 方法
用 CLEAR 语料（4718 段）经 Amazon Polly TTS 固定语速/韵律，再加 DEMAND babble（SNR 0/10/20 dB）与 OpenAIR 混响（0.1/0.9）。可读性用多指标合成的 Global Readability Index（GRI），并对照 Bradley-Terry 简易度；可懂度用 WER；另看预测熵与压缩比作“认知努力”代理。ASR：PocketSphinx、Vosk、Wav2Vec2 Base、Whisper Tiny/Medium。并用 LibriSpeech train-clean-100 拼接自然语音做验证。

## 实验与结果
- GRI 与人类 BT 简易度强负相关（r=−0.56）；原文与转写 GRI 相关 r=0.97。
- 干净条件：Whisper Tiny/Medium 与 GRI 近正交（r≤0.03）；Wav2Vec2 r=0.24、Vosk r=0.14；PocketSphinx r=0.05（作者认为是高错误率饱和）。
- 与人类感知难度均呈负相关（r∈[−0.35,−0.19]）。
- Whisper Tiny 在 0 dB 噪声下与 GRI 仍几乎无相关（r=0.06）；自然语音上 r=−0.02。
- 预测熵与 GRI r=−0.01，压缩比 r=−0.08，未见复杂度带来的内部犹豫或简化。

## 结论
现代 E2E ASR 的转写错误与文本可读性近乎无关，即使在噪声/混响下也成立；声学转写已独立于文本结构复杂度。这支持 listenability 设计中可读性与 ASR 模块可分开优化。仍与人类感知难度保持相关，非结构因素有待厘清。

## 点评
TTS 控制把“文本难度→发音变化”拆开，结论对 Whisper 类模型很清晰。PocketSphinx 的低相关被解释为误差饱和，提醒架构对比要看误差底线。残余的“人类难度相关”说明 ASR 仍踩在某些与人共享的难例上，只是不是经典可读性公式能抓住的那一类。
