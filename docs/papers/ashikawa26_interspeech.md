# Audio-KWS-Gated Error Memory Retrieval for Incremental ASR Post-Correction

- 论文编号：363
- 报告人：Taira Ashikawa
- 程序：Wednesday 30 September 2026 / Robust and Real-World ASR Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ashikawa26_interspeech.pdf

## 问题
端到端 ASR 对稀有词与领域专有名词仍易错；LLM 二遍纠错可复用历史纠错记录，但全历史进 prompt 会撞上下文窗口，且仅靠噪声 ASR 假设做文本检索时，触发词被误识就会漏检相关记录。

## 方法
提出增量式 LLM ASR 后纠错框架：人类参考可用时，用 LLM 做错误分析，抽取 hypothesis–reference 短语对写入 error memory，并更新关键词库存与倒排索引（英语索引正误两侧；日语用 LLM 估计的读音作检索键）。对新音频段，用开词汇 Audio-KWS（AdaKWS，Whisper-medium 编码器冻结）在库存上打分，经阈值与 Top-N 得到关键词集合，再检索并按时效截断至最多 M=200 条记录，交给 LLM 做记录约束的保守编辑。

## 实验与结果
在 Earnings-21（英语，公开 ASR 假设）与 CSJ（日语，Whisper-large-v3）含至少一词的 20 个 bias-word 子集上评测。相对无 KWS 的近期历史基线，Top-20 英语约减 prompt 70.9%/65.1%（micro/macro），WER 28.92 vs 29.06，Bias-F1 0.856 vs 0.836；Top-10 日语约减 71.7%/66.7%，CER 14.62 vs 14.86，Bias-F1 0.673 vs 0.648。Top-30 精度最好但压缩更少；仅索引参考侧在日语上损害 Bias-F1。纠错 LLM 为 gpt-oss-20b。

## 结论
Audio-KWS 门控检索可在约 70% prompt 压缩下保持或提升 WER/CER 与 Bias-F1；未来需处理 KWS 漏检并加速分析/纠错推理。

## 点评
核心抓的是「纠错记忆膨胀」与「文本检索依赖错误假设」的耦合问题：用音频侧关键词门控历史，比单纯截断近期记录更贴合当前内容。日语读音键与表面编辑分离的设计合理，但系统依赖人类参考才能扩库存，且强过滤（Top-1）会明显伤 Bias-F1，SLA 上需在压缩与召回间折中。
