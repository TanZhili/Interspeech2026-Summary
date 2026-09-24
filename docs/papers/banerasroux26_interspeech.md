# Closing the Speech-Text Gap with Limited Audio for Effective Domain Adaptation in LLM-Based ASR

- 论文编号：3383
- 报告人：Sergio Burdisso
- 程序：Thursday 1 October 2026 / Multimodal Speech Processing and Speech LLM Systems
- 技术分类键：audio-llm
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/banerasroux26_interspeech.pdf

## 问题
LLM-based ASR（编码器+投影器+LLM）可用纯文本域适应，但会使 LLM 远离投影器产生的“噪声”表示，形成 modality gap；目标域语音又昂贵稀缺。

## 方法
SLAM-ASR：冻结 WavLM-Large 与投影器，仅用 LoRA 适应 Llama-3.2-3B。Mixed Batching（MB）：batch 混合源域配对语音、投影最近邻噪声 token、字符扰动文本，以及目标域配对语音与扰动文本。比较纯文本、全配对与不同比例目标语音的 MB。源域 DefinedAI B/I/H；目标含 Banking 与 SlideSpeech Agriculture/Musical Instruments。

## 实验与结果
Banking 上纯文本 WER 6.38% vs 全配对 4.55%（模态差距明显）。MB 用约 10% 目标语音（Banking≈3h37）即可达到或超过全语音微调；约 60% 语音时峰值最好。Agriculture/MI 等 OOD 域趋势一致。相对标准 ASR 微调，文本/MB 对源域遗忘更轻。

## 结论
少量目标语音混入以文本为主的 MB，可弥合 modality gap，在极少音频下逼近或优于全语音适应。

## 点评
实用结论清楚：文本负责域语言、少量音频负责对齐。batch 成分与 τ=50% 等设定较细；全语音充足时 MB 优势收窄，说明方法主打低资源。
