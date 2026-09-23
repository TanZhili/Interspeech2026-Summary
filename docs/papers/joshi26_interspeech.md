# IndicContextEval: A Benchmark for Evaluating Context Utilisation in Audio Large Language Models Across 8 Indic Languages

- 论文编号：3272
- 报告人：Sakshi Joshi
- 程序：Tuesday 29 September 2026 / Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/joshi26_interspeech.pdf

## 问题
AudioLLM 可用文本提示做语境 ASR，但难分清是真用上下文还是靠预训练参数记忆；既有基准少变提示、少印度语、常合成音。

## 方法
发布 IndicContextEval：约 56 h 自然语音、555 说话人、8 语、23 专业域。七级提示 L0–L6：无语境→语言→域元数据→音频描述→英/本地实体列表→错误实体对抗。评五个模型（含 GPT-4o Transcribe、Gemini 3 Flash、Sarvam Audio、Gemma-3N 等），指标含 WER 与命名实体错误率 NEER。

## 实验与结果
模型间语境利用差异大：本地脚本实体（L5）使 GPT-4o/Gemini/Gemma 的 NEER 显著下降（Gemini L5 最佳约 17.39%）；对抗 L6 回落到接近 L1，显示依赖正确实体。部分模型几乎忽略提示或对提示不稳定。

## 结论
需显式评测 AudioLLM 的语境 grounding；IndicContextEval 的分级与对抗提示可区分记忆与利用。资源已公开。

## 点评
L0–L6 递增与对抗实体设计干净，直接回答“提示有没有用”。自然多语专业域是稀缺点。音频描述由 Gemini 生成，可能对同厂模型偏利；实体列表质量也会影响结论。
