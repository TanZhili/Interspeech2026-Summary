# LLM-as-Joiner: Decoupling Alignment from Language Modeling in Label-synchronous ASR

- 论文编号：2149
- 报告人：Jaeyoung Lee
- 程序：Thursday 1 October 2026 / New Training Methods for ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/lee26u_interspeech.pdf

## 问题
把 LLM 当 speech-as-prefix 解码器时，模型既要学对齐又要做语言建模，上下文长达 T+U，内存与计算重；对齐本可由语音编码器更好承担。

## 方法
LLM-as-Joiner：Aligner-Encoder 产出 U 个 label-synchronous 语音状态（监督前 U 个编码器位置）；预训练 Llama-3.2-3B 在选定层 ℓ 注入语音（门控残差融合），下层当 predictor、上层当 joiner，仅上层 LoRA（rank 16），tokenizer/嵌入/LM head 不变、无 blank。同编码器并行训练轻量 LSTM+FFN 头以便无 LLM 部署。总损失：λ_llm L_llm + λ_lite L_lite + λ_ctc L_ctc（1.0/0.5/0.1）。

## 实验与结果
Conformer-L 从零训练。LibriSpeech：LLM head 3.2/5.6，优于 decoder-only 基线 3.7/7.1；Lite head 3.8/6.4，接近从零 Aligner 3.9/6.5。cv-5langs（de/en/es/fr/it）：LLM head 均 11.5，Lite 12.5，显著优于从零 Aligner 14.4；decoder-only 在多语未收敛。RTF：Lite 0.02，LLM head 0.65 vs decoder-only 0.90。消融：注入层 0/7 相近，14 变差；门控用 speech+text 对 Lite 更有利。

## 结论
用 Aligner 管对齐、LLM 管语言建模，可在更短上下文下提升识别，并让联合训练的轻量头隐式受益于 LLM。

## 点评
接口设计清晰：U 长度对齐面让 LLM 不必吞长语音前缀。对照实验刻意不用预训练语音编码器，突出架构差异。多语上 Lite 头收益更大，说明知识迁移对低资源语言更关键；晚注入失败提示融合仍需足够上层容量。
