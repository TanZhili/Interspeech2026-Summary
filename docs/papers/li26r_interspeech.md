# INSPIRE: A Benchmark for Instruction-Aware Speech Retrieval

- 论文编号：1026
- 报告人：Chen-An Li
- 程序：Thursday 1 October 2026 / Benchmarking Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26r_interspeech.pdf

## 问题
传统语音检索按固定声学/语义相似度匹配，无法按自然语言指令切换相关准则（内容、说话人、风格、环境声及其组合）。指令感知检索在文本/图像已成熟，语音侧缺系统基准。

## 方法
提出 INSPIRE：给定口语查询 q 与文本指令 z，对库中文档打分排序。四个子集——DailyTalk（对话续接）、VCTK（同说话人，硬负例为同文异人）、Expresso（说话人/风格）、Synthetic（Natural Questions 经 GPT-4o-mini TTS + ESC-50 环境声，多属性组合）。每类意图用 GPT-5.2 生成 20 条指令再随机抽样。规模约 680 查询、4,080 查询–指令对、17,225 文档。基线四类：LALM 嵌入、ASR+字幕再 BM25/稠密文本检索、不看指令的 SSL 语音嵌入、CLAP 式对比音文；另有 LALM/文本重排。合成子集质量：Whisper WER≈0.03、说话人 SVM≈0.9998、emotion2vec 风格准确≈0.87、UTMOS≈3.76。

## 实验与结果
摘要结论：无一现有方法稳健覆盖全部意图；偏文本路径语义检索相对更好但弱于副语言属性，偏语音模型对声学属性稍好却难跟指令。正文在实验设置（LALM 列表）处截断，具体 nDCG/Recall 等数字未完整可读。

## 结论
作者将指令感知语音检索立为可评问题，并呼吁统一架构同时做指令跟随与细粒度声学匹配。

## 点评
子集设计把“同一查询、不同指令→不同正例”写死，问题定义清楚。合成多属性可控性强，但真实噪声/自发对话泛化仍开放；因结果段抽取缺失，量化对比只能采信摘要定性结论。
