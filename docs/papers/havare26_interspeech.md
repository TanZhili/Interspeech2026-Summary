# CodeVaani: A Multilingual, Voice-Based Code Learning Assistant

- 论文编号：3608
- 报告人：Jayant Havare
- 程序：Tuesday 29 September 2026 / Speech and Language Learning Technologies
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/havare26_interspeech.pdf

## 问题
印度等非英语语境编程教育默认英语与文本交互；口语编程问句语码混合、术语 OOV，标准 ASR 易错，下游代码助手失效。

## 方法
接入 IITB LMS 的 CodeVaani：Indic-Conformer（Indic）/Whisper（英语）→ Gemma-27B（DPO）做代码感知转写修正（如 ask key→ASCII）→ Codestral-22B 同语种答疑；React/Django + 双 H100。

## 实验与结果
28 名初学者：>89% 评 fair 及以上，26 人中 25 愿采用。500 条真人问句：相对 Saaras V3，各语 WER 大幅下降（如 Gujarati 45.3%→8.1%，English 70.5%→12.4%）。相对 Whisper/Qwen3-Omni/Phi-4，框架 WER/PER/WFED 最低（例 WER 8.1%）。

## 结论
语音优先、多语代码助手可降低英语门槛；转写精炼是关键。后续多轮对话与端到端低延迟。

## 点评
对准“代码混合 ASR + 纠错”真实痛点，评测扎实；规模仍偏小、多轮与延迟未解决。
