# Towards Enabling Multilingual Multitask SpeechLLMs in Data-Scarce Settings

- 论文编号：1229
- 报告人：Seraphina Fong
- 程序：Tuesday 29 September 2026 / Audio & Speech Language Models: Evaluation, Representations, and Emerging Capabilities
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/fong26b_interspeech.pdf

## 问题
SpeechLLM 的多语言与多任务常被分开研究，且多依赖大规模数据；低资源场景下，每任务–语言仅有数小时标注时，能否把高资源 ASR 预训练迁移到 ASR、语音翻译（ST）与话题分类（TID），以及零样本跨语言/跨任务能走多远，仍不清楚。

## 方法
统一 SpeechLLM：冻结 Whisper-large-v3-turbo 编码器 + 冻结 EuroLLM-1.7B-Instruct，仅训线性投影器（约 17.31M；语音嵌入下采样 k=5）。任务用特定 prompt，交叉熵训练。流程：可选 CommonVoice ASR 预训练（200h IT 或 500h IT/ES/EN/FR/DE）→ 在 SIB-Fleurs（IT/ES/GL/CS/FIN，每任务约 3–5h）上多任务微调；另对比从零训练、Qwen2-Audio-7B-Instruct 零样本，以及 MEUSLI（28 欧语）投影器 + LoRA。

## 实验与结果
从零多任务：单语 WER 约 129–162%、BLEU 近 0；多语从零对 Romance 更稳，对 CS/FIN 仍差。IT ASR 预训练后 IT 多任务：WER 5.4%、BLEU 48.2%、TID Acc 81.5%。零样本跨语言强弱随与 IT 的语系距离变化（ES 最好，CS/FIN 最差）；排除某任务微调则该任务零样本失败（如无 TID 监督则 Acc/F1 为 0）。多语 CV 预训练后，单语微调通常比联合多语微调更稳；MEUSLI 强多语投影器上两者差距缩小。相对 Qwen2，有监督低资源微调在五语上更均衡。

## 结论
ASR 预训练自举 + 每任务不足 5 小时目标语微调，可使多语言多任务 SpeechLLM 在低资源下可行；跨语言零样本受语言相近性约束，未见任务的零样本不成立，仍需任务监督。研究范围限于三任务与欧洲语言。

## 点评
抓的是「投影器级 ASR 预训练能否撬动低资源多任务」的迁移问题，实验矩阵（单/多语预训练、零样本语言/任务、MEUSLI）设计清楚。强在用同一音频并行标注隔离多任务效应；脆弱点在编码器与 LLM 全冻、依赖欧洲语系与 SeamlessM4T 派生译文，以及 TID 仅七类——对更远语系与更难生成任务的外推需谨慎。
