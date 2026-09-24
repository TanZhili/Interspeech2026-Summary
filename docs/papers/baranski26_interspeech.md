# HALAS: A Human-Annotated Dataset of Hallucinations of Modern ASR Systems

- 论文编号：337
- 报告人：Mateusz Barański
- 程序：Thursday 1 October 2026 / Speech Benchmarks, Evaluation, and Resources
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/baranski26_interspeech.pdf

## 问题
端到端 ASR 会在自然语音上幻觉（无语音对应的插入、改意、循环重复），但既有检测/缓解多在非语音或人工加噪上评测，缺少真实未处理语音上的人工标注基准。

## 方法
在 Earnings-22 全量上跑七个低 WER 开源模型（Whisper large v2/v3/Turbo、CrisperWhisper、Canary-1B/Flash、Parakeet-TDT v2）；用去循环+归一化后的模型间平均 WER 挑难例；10 名标注员按“无语音对应”定义标 span（Hallucination / Looping / Looping Hallucination），双人标+仲裁（κ=0.87），并校正参考。得 HALAS：3,611 段，train 2,866（HR 33.6%）、test 745（HR 22.6%，>1 s 且≥3 词）。用代理指标做 ROC-AUC，并用 XGBoost / LLM 比对 / 解码器嵌入分类器（含多层扩展）做检测基准。

## 实验与结果
各模型幻觉率约 21.4–43.8%，循环约 1.1%；幻觉短语高度偏斜（平均 top-10 覆盖 55%），跨模型短语重叠明显；低 WER（可至约 6.25%）仍可幻觉。GPT-4o mini 严重度标注显示要么偏轻微填充、要么严重改意。代理指标中 CER/SeMaScore AUC 约 0.81/0.80，PPL 仅约 0.60。检测：Wv3 上 DE 单层 F1 53.1%，多层 DE 2,13,23 达 56.1%，优于参考依赖 LLM 判定；在非语音增强集上 F1 更高，说明 HALAS 更难。

## 结论
作者认为 HALAS 首次在真实语音上提供人工幻觉标注与检测基准，暴露跨模型共性与检测难度；数据集与推理配置已公开。注意采样偏向高模型分歧，不代表部署场景自然发生率。

## 点评
把评测从“非语音幻觉”拉回 earnings 通话真实错误，span 标注与跨模型分布分析有信息量。检测数字说明参考+LLM 也不够，嵌入分类器仍仅中等 F1；因故意富集难例，直接外推到“日常幻觉率”会偏高。
