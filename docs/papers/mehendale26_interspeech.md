# Indic DiarBench: A Multilingual Joint Diarization and ASR Benchmark for Indian Languages

- 论文编号：2484
- 报告人：Deovrat Mehendale
- 程序：Wednesday 30 September 2026 / Speaker Diarization 1
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mehendale26_interspeech.pdf

## 问题
印度语 ASR 进展多在单说话人；会议/对话需联合日志化与说话人归因 ASR，但现有基准几乎不含 22 种法定印度语，且常把日志化与 ASR 拆开评，掩盖短段/重叠上的级联失败。

## 方法
发布 Indic DiarBench：约 108h，覆盖全部 22 种 scheduled 语言。近场会议 ~53h（22 语）、远场 ~27h（前 8 语）、YouTube in-the-wild ~28h（前 10 语）。人工校正说话人归因转写 + RTTM；支持英–印语码混的两种转写规范。指标：无 collar DER、cpWER、WDER。评测能联合输出 ASR+日志化的商用 API 与多模态 LLM（不含纯日志化模型）。

## 实验与结果
时长加权：Indic 特化 Sarvam DER 16.0 / cpWER 38.8 / WDER 33.1 最优；AWS 23.5 / 43.7；其他 API 与 GPT-4o/Gemini 明显更差（Gemini DER 74.0 但 WDER 尚可）。错误分解：Sarvam 较均衡；LLM 以 Miss 为主。重叠率与 DER/cpWER 强相关；近场高重叠语（如 Telugu、Maithili、Dogri）更难；Dravidian 近场 cpWER 约高 Indo-Aryan 5 点。

## 结论
开放基准填补印度多说话人归因转写空白；联合评测显示特化管线领先，通用 LLM/API 在时间戳与小话语上仍弱。数据偏评估用，in-the-wild 仅 10 语。

## 点评
22 语 + 三声学条件 + 联合指标，对包容性语音技术很有建设性。只评“能联合输出”的系统公平于应用场景，但排除 Pyannote 等使与学术日志化文献不可直接比。码混双规范降低假 WER 惩罚，设计务实。
