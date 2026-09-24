# Bootstrapping Endangered Language ASR with Short-Form Corpora

- 论文编号：1302
- 报告人：Christopher Bartley
- 程序：Tuesday 29 September 2026 / Low-Resource & Endangered Language Speech Processing
- 技术分类键：multilingual
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bartley26_interspeech.pdf

## 问题
濒危语言常缺 3–15 秒句级对齐语料，却有短词/短语发音资源与长录音文本；大模型路线算力门槛高，社区难以起步。

## 方法
用 Kaldi GMM-HMM（CPU 可训）在英语 LibriSpeech 上系统缩短训练单元，量化短式相对句级的代价。再对 Cornish、Manx、Hawaiian、Jejueo、Mohawk：以短式语料训 monophone → Viterbi 强制对齐长录音 → 自举 triphone 解码并按 LibriSpeech 流程切分，得到句级集。合并 short+utterance 训练 GMM/DNN-HMM，并与零样本 OmniASR、MMS、Whisper 及 LoRA 微调 Whisper 在 in-domain / OOD 上对比；外源文本降 OOV 后重建 4-gram LM。

## 实验与结果
英语上平均时长降至约 1s 前 WER 基本稳定，更短则上升；稀缺数据下句级格式重要性下降。五语 monophone 对齐成功率均 >70%；三语 bootstrapped 解码 WER <5%。自建 GMM 已在多数语上优于零样本多语大模型；DNN+增强 LM 整体最强，外源 LM 平均降约 5.82 点 WER。Jejueo/Mohawk 仍极难；文本稀缺时 Whisper-FT 在 OOD 更优。

## 结论
不必以句级监督为起点：短式资源可自举对齐长录音并训出可用 ASR，且 CPU 系统可在 OOD 上以远低于大模型的算力取得更好表现。应更好利用社区已有非常规数据。

## 点评
把“格式不对”重新定义为可对齐的数据问题，对濒危语社区路径现实。强在英语对照实验与开源五语切分集；弱在部分长录音保留率低（如 Hawaiian 仅约 23% 时长）、OOD 测试集很小，且 HMM 与 E2E 的可比边界依赖文本资源。
