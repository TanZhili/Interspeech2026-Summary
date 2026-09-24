# Speech Encoder Fusion for LLM-based Automatic Speech Recognition

- 论文编号：1039
- 报告人：Jakob Poncelet
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/poncelet26_interspeech.pdf

## 问题
Speech-LLM 通常绑定单一预训练声学编码器；不同编码器错误互补，简单拼接未必充分利用，多语/分离场景更需自适应融合。

## 方法
在投影到 LLM 前融合两路等长编码器特征：对比 concat、sigmoid 门控、帧内多头门控、位置 Transformer、时间交织 Transformer（再池化）。编码器冻结；2 层 MLP 投影 + QLoRA（rank 4）微调 LLM。荷兰语：Whisper-large-v3 + NeLF + Tweety-7B；英语：Whisper + Wav2Vec2-FT + Llama-3.1-8B；亦可融 ECAPA2 做带说话人标注转写；可选第二阶段把解码器假设并入提示。

## 实验与结果
荷兰语单语：时间 Transformer 最佳（clean/other 6.8/8.3），优于 concat 与单编码器。英语：sigmoid 门控最好（2.8/5.5）。联合英荷训练时多头门控最佳（NL 6.5 / EN 2.5）。分离 ASR：时间 Transformer SA-WER 18.1、Spk-Conf 3.6。并入解码假设后荷兰语可到 5.6/7.8，优于纯文本纠错。

## 结论
精心设计的并行编码器融合在开销有限下全面优于特征拼接，适用于单语、多语与分离 ASR；短时 ASR 设定下仍可进一步用历史文本与更大 LoRA 提升。

## 点评
系统比较多种融合，并覆盖低资源语与说话人编码器，实用价值高。LLM 侧 rank/量化偏弱，英语难追上专用 ASR；时间 Transformer 在分离任务上强、英语上未必最优，融合策略需按任务选型。
