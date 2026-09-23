# A Gated Multi-Task Whisper Framework for Speech, Emotion, and Scene Understanding

- 论文编号：135
- 报告人：Manjiri Bhat
- 程序：Monday 28 September 2026 / Audio segmentation
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/bhat26_interspeech.pdf

## 问题
辅助场景需同时做 ASR、SER、ASC，独立模型低效；Whisper 在非语音段易幻觉。需要统一框架并按输入类型条件激活任务头。

## 方法
Whisper-small 共享编码器 + 三路门控（干净语音 / 非语音 / 噪声语音）与 ASR、SER、ASC 头。训练用加权多任务损失（门控权重大），分两阶段：先训编码器与分类头（解码器冻结），再联合微调。推理按门控路由：干净→ASR+SER；非语音→仅 ASC；噪声→三者全开。构造 ESAS-32K（约 32k，情感语音与 SPASS 场景在多 SNR 混合）。

## 实验与结果
70/10/20 划分：门控 Acc≈99.98%，SER 98.2%，ASC 94.5%；加 n-gram 限制后 WER 可到约 0.41%。无门控时非语音幻觉率约 96%，有门控约 0.015–0.4%。优于若干单任务 Whisper/专用模型；低资源划分下门控仍稳健。

## 结论
门控多任务 Whisper 可在统一模型中条件激活 ASR/SER/ASC，并显著抑制非语音幻觉，适合情境感知音频分析。

## 点评
把 VAD 式路由做成可学习三分类并与多任务联合，直接打中 Whisper 非语音幻觉痛点。ESAS-32K 为模拟混合，真实嘈杂场景泛化待证；训练时不用门控路由、仅推理用，门控错误会系统性关掉错误任务头。
