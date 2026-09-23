# Transcription Policy as a Latent Variable: Activating Controllable Verbatim ASR with Word-Level Timing

- 论文编号：2792
- 报告人：Laurin Wagner
- 程序：Monday 28 September 2026 / Robust and Efficient ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/wagner26_interspeech.pdf

## 问题
现代 ASR 训练数据混杂 verbatim（含填充停顿、重复等）与 intended（流利化）标注，把转写风格当成未控隐变量，导致解码不稳、评测混淆（风格错配可占报告 WER 的约 60%）、词级时间戳不可靠。模型其实已编码两种风格，缺的是可控激活。

## 方法
1. **Coverage-aware decoder task tokens**：在并行 verbatim/intended 对上训练，用任务 token 显式切换策略；
2. **Supervised cross-attention finetuning**：选与 TIMIT 对齐相关最好的 \(k=10\) 头，对平均注意力与词区间二值目标做余弦距离；推理时能量 pause 模型 + 温度锐化 + Viterbi 得词时间戳；
3. 新任务 **verbatimize**：从 intended/异构文本生成规范 verbatim，用于语料富集。

## 实验与结果
- 仅英语训练即可零样本把德语不流畅 F1 **10%→79%**；
- 全量英-only 微调在 verbatim 精度、不流畅检测与 intended 质量上英德均超基线；
- 监督交叉注意使不流畅语音上的词时间戳优于强制对齐基线。
（抽取在方法中后部截断，完整数值表未全见。）

## 结论
把转写策略显式化为可控变量，可稳定激活 verbatim/intended，并改善词级 timing；verbatimize 支持可扩展语料建设。

## 点评
问题诊断（风格作隐变量）对临床/自发语音 ASR 很关键；任务 token + 对齐头监督是轻量可控方案。强在跨语零样本不流畅检测；脆弱在依赖并行风格对与 TIMIT 头选择，泛化到更多语言/病理语音仍待验证。
