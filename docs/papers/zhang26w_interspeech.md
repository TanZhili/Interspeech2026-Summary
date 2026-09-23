# BACH: Benchmarking Audio Codecs for Bio-Acoustic Health

- 论文编号：1588
- 报告人：Zixing Zhang
- 程序：Tuesday 29 September 2026 / Multimodal and Non-Speech Healthcare Applications
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26w_interspeech.pdf

## 问题
远程医疗依赖心音、鼾声、肺音等生物声学信号的传输与分类，但信号量大、维度高，压缩时能否保住诊断线索尚不清楚。通用音频 codec 在语音/音乐上保真度高，却未必保留生物声学中的短促、稀疏、不规则临床线索；现有 Codec-SUPERB、ARCH、AudioCodecBench 等评测也未系统覆盖健康声学任务。

## 方法
提出 BACH，在统一管线中评测八个约 1 kbps 的神经音频 codec（DAC、EnCodec、WavTokenizer、BigCodec、SpeechTokenizer、FACodec、UniCodec、SemantiCodec），覆盖多码本、单码本、解耦与语义类设计。评测分三条路径：Original（原始音频+预训练 HuBERT 特征）、Compressed（直接用 quantizer 表示）、Reconstructed（codec 重建后再经 HuBERT）。下游分类器统一为线性投影 + Transformer Encoder + 前馈头；分类报 Acc/F1，重建报 UTMOS、PESQ、STOI。五个数据集：Snoring、HeartSound、ICBHI、MSTI、VocalSound。

## 实验与结果
Compressed 域 Acc/F1 普遍低于 Original（如 Original 在 Snoring/HeartSound/ICBHI/MSTI/VocalSound 上 Rec 基线约 96.0/100.0/94.5/78.2/90.6）。语义/解耦类 codec 在 Compressed 域更强：SpeechTokenizer、FACodec 总体最优（如 FACodec HeartSound Com. 99.5/99.5，SpeechTokenizer MSTI Com. 41.5/41.8 显著高于多数模型个位数 Acc）。重建保真与下游任务不对齐：DAC/EnCodec 重建指标较好但任务相对弱；SpeechTokenizer 重建偏低但任务强。增加码本深度主要抬升 PESQ，对下游 F1 增益有限。

## 结论
BACH 表明现有 codec 难以同时兼顾重建保真与诊断语义保留；面向医疗应用的 codec 需联合优化感知质量与任务相关信息。作者计划扩展更多生物声学任务与真实场景鲁棒性评估。

## 点评
工作把“codec 好不好”从听感指标拆成 original / compressed / reconstructed 三视图，直接打在健康声学分类上，抓的是医疗传输场景里真正要保的是语义而非 MOS。强处是暴露重建–任务错位，以及语义引导 quantizer（SpeechTokenizer/FACodec）的相对优势；脆弱处在于下游仍依赖 HuBERT+小分类头、码率统一到约 1 kbps、且部分数据集很短（如鼾声约 1 秒），对 codec 泛化结论需谨慎外推。
